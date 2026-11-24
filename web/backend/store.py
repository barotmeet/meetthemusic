"""JSON-on-disk store for users and user submissions.

Files live in `data/` next to this module:
  data/users.json       -> [{"id","username","email","password_hash","role","created_at"}]
  data/submissions.json -> [{"id","user_id","category","payload","status","admin_note",
                              "created_at","reviewed_at","reviewed_by"}]

We use a single-process file lock so concurrent Flask workers (reloader, threads) do
not corrupt the JSON. Persistence is intentional — restarting the server keeps the
contributions, the users, and the admin moderation queue.
"""
from __future__ import annotations

import json
import os
import secrets
import threading
import time
import uuid
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from werkzeug.security import check_password_hash, generate_password_hash

DATA_DIR = Path(__file__).resolve().parent / "data"
USERS_PATH = DATA_DIR / "users.json"
SUBS_PATH = DATA_DIR / "submissions.json"

_LOCK = threading.RLock()


# ---------- low-level file helpers ----------
def _ensure_files() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for p, default in ((USERS_PATH, []), (SUBS_PATH, [])):
        if not p.exists():
            p.write_text(json.dumps(default, indent=2), encoding="utf-8")


def _read(path: Path) -> list[dict]:
    _ensure_files()
    with path.open("r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def _write(path: Path, items: list[dict]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
    os.replace(tmp, path)


@contextmanager
def _txn():
    """Atomic read-modify-write over both files."""
    with _LOCK:
        users = _read(USERS_PATH)
        subs = _read(SUBS_PATH)
        yield users, subs
        _write(USERS_PATH, users)
        _write(SUBS_PATH, subs)


# ---------- id + timestamp helpers ----------
def _now() -> float:
    return time.time()


def _new_id() -> str:
    return uuid.uuid4().hex[:12]


# ---------- users ----------
class UserExists(Exception):
    pass


class AuthError(Exception):
    pass


def get_user_by_id(user_id: str) -> dict | None:
    return next((u for u in _read(USERS_PATH) if u["id"] == user_id), None)


def get_user_by_username(username: str) -> dict | None:
    needle = (username or "").strip().lower()
    return next(
        (u for u in _read(USERS_PATH) if u["username"].lower() == needle),
        None,
    )


def get_user_by_email(email: str) -> dict | None:
    needle = (email or "").strip().lower()
    return next(
        (u for u in _read(USERS_PATH) if u.get("email", "").lower() == needle),
        None,
    )


def list_users() -> list[dict]:
    """Public-safe list (no password hashes)."""
    return [
        {k: v for k, v in u.items() if k != "password_hash"}
        for u in _read(USERS_PATH)
    ]


def create_user(username: str, email: str, password: str, role: str = "user") -> dict:
    username = (username or "").strip()
    email = (email or "").strip().lower()
    if not username or not email or not password:
        raise AuthError("username, email and password are required")
    if len(password) < 6:
        raise AuthError("password must be at least 6 characters")
    with _txn() as (users, _):
        if any(u["username"].lower() == username.lower() for u in users):
            raise UserExists("username already taken")
        if any(u.get("email", "").lower() == email for u in users):
            raise UserExists("email already registered")
        user = {
            "id": _new_id(),
            "username": username,
            "email": email,
            "password_hash": generate_password_hash(password),
            "role": role if role in ("user", "admin") else "user",
            "created_at": _now(),
        }
        users.append(user)
        return {k: v for k, v in user.items() if k != "password_hash"}


def authenticate(username_or_email: str, password: str) -> dict:
    needle = (username_or_email or "").strip().lower()
    user = (
        get_user_by_username(needle)
        or get_user_by_email(needle)
    )
    if not user or not check_password_hash(user["password_hash"], password or ""):
        raise AuthError("invalid credentials")
    return {k: v for k, v in user.items() if k != "password_hash"}


def ensure_admin(username: str = "admin", password: str = "admin123") -> dict | None:
    """Create the default admin if no admin exists yet. Returns the admin or None."""
    with _txn() as (users, _):
        if any(u.get("role") == "admin" for u in users):
            return None
        admin = {
            "id": _new_id(),
            "username": username,
            "email": f"{username}@classicalverse.local",
            "password_hash": generate_password_hash(password),
            "role": "admin",
            "created_at": _now(),
        }
        users.append(admin)
        return {k: v for k, v in admin.items() if k != "password_hash"}


def set_user_role(user_id: str, role: str) -> dict:
    if role not in ("user", "admin"):
        raise AuthError("role must be 'user' or 'admin'")
    with _txn() as (users, _):
        u = next((x for x in users if x["id"] == user_id), None)
        if not u:
            raise AuthError("user not found")
        # Don't allow demoting the last admin
        if role == "user":
            remaining = [x for x in users if x.get("role") == "admin" and x["id"] != user_id]
            if not remaining:
                raise AuthError("cannot demote the last admin")
        u["role"] = role
        return {k: v for k, v in u.items() if k != "password_hash"}


def delete_user(user_id: str) -> None:
    with _txn() as (users, subs):
        u = next((x for x in users if x["id"] == user_id), None)
        if not u:
            raise AuthError("user not found")
        if u.get("role") == "admin":
            remaining = [x for x in users if x.get("role") == "admin" and x["id"] != user_id]
            if not remaining:
                raise AuthError("cannot delete the last admin")
        users[:] = [x for x in users if x["id"] != user_id]
        subs[:] = [s for s in subs if s.get("user_id") != user_id]


# ---------- submissions ----------
ALLOWED_CATEGORIES = {
    "raga", "taal", "knowledge",
    "bandish", "artist", "kriti",
    "guru", "concert", "archive",
    "course", "thread",
}


def _public_user(u: dict) -> dict:
    return {"id": u["id"], "username": u["username"], "role": u.get("role", "user")}


def list_submissions(
    status: str | None = None,
    user_id: str | None = None,
) -> list[dict]:
    items = _read(SUBS_PATH)
    if status:
        items = [s for s in items if s["status"] == status]
    if user_id:
        items = [s for s in items if s["user_id"] == user_id]
    # newest first
    items.sort(key=lambda s: s["created_at"], reverse=True)
    return items


def get_submission(sub_id: str) -> dict | None:
    return next((s for s in _read(SUBS_PATH) if s["id"] == sub_id), None)


def _validate_payload(category: str, payload: dict) -> tuple[dict, str | None]:
    """Returns (cleaned_payload, error_message)."""
    if not isinstance(payload, dict):
        return {}, "payload must be an object"
    if category not in ALLOWED_CATEGORIES:
        return {}, f"unknown category '{category}'"

    def need(*keys: str) -> str | None:
        for k in keys:
            v = payload.get(k)
            if v is None or (isinstance(v, str) and not v.strip()):
                return f"'{k}' is required"
        return None

    if category == "raga":
        err = need("name", "tradition", "thaat", "time", "mood",
                   "aroh", "avroh", "description")
        if err:
            return {}, err
        return ({
            "name": str(payload["name"]).strip(),
            "slug": str(payload.get("slug") or payload["name"]).strip().lower()
                    .replace(" ", "-"),
            "tradition": str(payload["tradition"]).strip(),
            "thaat": str(payload["thaat"]).strip(),
            "time": str(payload["time"]).strip(),
            "mood": str(payload["mood"]).strip(),
            "aroh": str(payload["aroh"]).strip(),
            "avroh": str(payload["avroh"]).strip(),
            "pakad": str(payload.get("pakad", "—")).strip() or "—",
            "vadi": str(payload.get("vadi", "—")).strip() or "—",
            "samvadi": str(payload.get("samvadi", "—")).strip() or "—",
            "description": str(payload["description"]).strip(),
            "youtube": str(payload.get("youtube", "")).strip(),
            "spotify": str(payload.get("spotify", "")).strip(),
        }, None)

    if category == "taal":
        err = need("name", "tradition", "beats", "structure", "claps", "bols")
        if err:
            return {}, err
        try:
            beats = int(payload["beats"])
        except (TypeError, ValueError):
            return {}, "'beats' must be a number"
        return ({
            "name": str(payload["name"]).strip(),
            "slug": str(payload.get("slug") or payload["name"]).strip().lower()
                    .replace(" ", "-"),
            "beats": beats,
            "structure": str(payload["structure"]).strip(),
            "claps": str(payload["claps"]).strip(),
            "bols": str(payload["bols"]).strip(),
            "tradition": str(payload["tradition"]).strip(),
            "youtube": str(payload.get("youtube", "")).strip(),
            "spotify": str(payload.get("spotify", "")).strip(),
        }, None)

    # knowledge article
    if category == "knowledge":
        err = need("title", "body")
        if err:
            return {}, err
        tags = payload.get("tags") or []
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(",") if t.strip()]
        return ({
            "slug": str(payload.get("slug") or payload["title"]).strip().lower()
                    .replace(" ", "-"),
            "title": str(payload["title"]).strip(),
            "body": str(payload["body"]).strip(),
            "tags": list(tags) if isinstance(tags, list) else [],
            "youtube": str(payload.get("youtube", "")).strip(),
            "spotify": str(payload.get("spotify", "")).strip(),
        }, None)

    # ---------- bandish / kriti (compositions) ----------
    if category in ("bandish", "kriti"):
        err = need("title", "raga", "taal", "composer", "language",
                   "lyrics", "description")
        if err:
            return {}, err
        return ({
            "slug": str(payload.get("slug") or payload["title"]).strip().lower()
                    .replace(" ", "-"),
            "title": str(payload["title"]).strip(),
            "raga": str(payload["raga"]).strip(),
            "taal": str(payload["taal"]).strip(),
            "composer": str(payload["composer"]).strip(),
            "language": str(payload["language"]).strip(),
            "difficulty": str(payload.get("difficulty", "Intermediate")).strip(),
            "lyrics": str(payload["lyrics"]).strip(),
            "translation": str(payload.get("translation", "")).strip(),
            "youtube": str(payload.get("youtube", "")).strip(),
            "spotify": str(payload.get("spotify", "")).strip(),
            "description": str(payload["description"]).strip(),
        }, None)

    # ---------- artist ----------
    if category == "artist":
        err = need("name", "tradition", "discipline", "description")
        if err:
            return {}, err
        instruments = payload.get("instruments") or ""
        if isinstance(instruments, str):
            instruments = [i.strip() for i in instruments.split(",") if i.strip()]
        return ({
            "slug": str(payload.get("slug") or payload["name"]).strip().lower()
                    .replace(" ", "-"),
            "name": str(payload["name"]).strip(),
            "tradition": str(payload["tradition"]).strip(),
            "discipline": str(payload["discipline"]).strip(),
            "gharana": str(payload.get("gharana", "—")).strip() or "—",
            "era": str(payload.get("era", "")).strip(),
            "instruments": list(instruments) if isinstance(instruments, list) else [],
            "youtube": str(payload.get("youtube", "")).strip(),
            "spotify": str(payload.get("spotify", "")).strip(),
            "description": str(payload["description"]).strip(),
        }, None)

    # ---------- guru ----------
    if category == "guru":
        err = need("name", "tradition", "discipline", "description")
        if err:
            return {}, err
        return ({
            "slug": str(payload.get("slug") or payload["name"]).strip().lower()
                    .replace(" ", "-"),
            "name": str(payload["name"]).strip(),
            "tradition": str(payload["tradition"]).strip(),
            "discipline": str(payload["discipline"]).strip(),
            "gharana": str(payload.get("gharana", "—")).strip() or "—",
            "specialty": str(payload.get("specialty", "")).strip(),
            "experience": str(payload.get("experience", "")).strip(),
            "mode": str(payload.get("mode", "")).strip(),
            "youtube": str(payload.get("youtube", "")).strip(),
            "spotify": str(payload.get("spotify", "")).strip(),
            "description": str(payload["description"]).strip(),
        }, None)

    # ---------- concert ----------
    if category == "concert":
        err = need("title", "artist", "venue", "date", "description")
        if err:
            return {}, err
        return ({
            "slug": str(payload.get("slug") or payload["title"]).strip().lower()
                    .replace(" ", "-"),
            "title": str(payload["title"]).strip(),
            "artist": str(payload["artist"]).strip(),
            "venue": str(payload["venue"]).strip(),
            "city": str(payload.get("city", "")).strip(),
            "date": str(payload["date"]).strip(),
            "type": str(payload.get("type", "")).strip(),
            "livestream": bool(payload.get("livestream")),
            "youtube": str(payload.get("youtube", "")).strip(),
            "spotify": str(payload.get("spotify", "")).strip(),
            "description": str(payload["description"]).strip(),
        }, None)

    # ---------- archive ----------
    if category == "archive":
        err = need("title", "type", "year", "description")
        if err:
            return {}, err
        try:
            year = int(payload["year"])
        except (TypeError, ValueError):
            return {}, "'year' must be a number"
        return ({
            "slug": str(payload.get("slug") or payload["title"]).strip().lower()
                    .replace(" ", "-"),
            "title": str(payload["title"]).strip(),
            "type": str(payload["type"]).strip(),
            "year": year,
            "youtube": str(payload.get("youtube", "")).strip(),
            "spotify": str(payload.get("spotify", "")).strip(),
            "description": str(payload["description"]).strip(),
        }, None)

    # ---------- course (learn) ----------
    if category == "course":
        err = need("title", "level", "tradition", "description")
        if err:
            return {}, err
        lessons = payload.get("lessons")
        if lessons is None or lessons == "":
            lessons_value = 0
        else:
            try:
                lessons_value = int(lessons)
            except (TypeError, ValueError):
                return {}, "'lessons' must be a number"
        return ({
            "slug": str(payload.get("slug") or payload["title"]).strip().lower()
                    .replace(" ", "-"),
            "title": str(payload["title"]).strip(),
            "level": str(payload["level"]).strip(),
            "tradition": str(payload["tradition"]).strip(),
            "duration": str(payload.get("duration", "")).strip(),
            "lessons": lessons_value,
            "youtube": str(payload.get("youtube", "")).strip(),
            "spotify": str(payload.get("spotify", "")).strip(),
            "description": str(payload["description"]).strip(),
        }, None)

    # ---------- forum thread (community) ----------
    if category == "thread":
        err = need("title", "body", "tag")
        if err:
            return {}, err
        return ({
            "slug": str(payload.get("slug") or payload["title"]).strip().lower()
                    .replace(" ", "-"),
            "title": str(payload["title"]).strip(),
            "tag": str(payload["tag"]).strip(),
            "body": str(payload["body"]).strip(),
            "youtube": str(payload.get("youtube", "")).strip(),
            "spotify": str(payload.get("spotify", "")).strip(),
        }, None)

    return {}, f"unsupported category '{category}'"


def create_submission(user_id: str, category: str, payload: dict) -> dict:
    if category not in ALLOWED_CATEGORIES:
        raise AuthError(f"unknown category '{category}'")
    cleaned, err = _validate_payload(category, payload)
    if err:
        raise AuthError(err)
    with _txn() as (_, subs):
        sub = {
            "id": _new_id(),
            "user_id": user_id,
            "category": category,
            "payload": cleaned,
            "status": "pending",
            "admin_note": "",
            "created_at": _now(),
            "reviewed_at": None,
            "reviewed_by": None,
        }
        subs.append(sub)
        return sub


def review_submission(sub_id: str, admin_id: str, approve: bool, note: str = "") -> dict:
    with _txn() as (_, subs):
        sub = next((s for s in subs if s["id"] == sub_id), None)
        if not sub:
            raise AuthError("submission not found")
        if sub["status"] != "pending":
            raise AuthError(f"submission already {sub['status']}")
        sub["status"] = "approved" if approve else "rejected"
        sub["admin_note"] = (note or "").strip()
        sub["reviewed_at"] = _now()
        sub["reviewed_by"] = admin_id
        return sub


def submissions_with_users(user_id: str | None = None,
                            status: str | None = None) -> list[dict]:
    """Submissions decorated with public author info."""
    users = {u["id"]: _public_user(u) for u in _read(USERS_PATH)}
    out = []
    for s in list_submissions(status=status, user_id=user_id):
        s = dict(s)
        s["author"] = users.get(s["user_id"], {"id": s["user_id"], "username": "unknown"})
        out.append(s)
    return out
