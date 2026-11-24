"""ClassicalVerse — Flask backend.

Responsibilities:
  * JSON API for the 10 static modules

  * User accounts (register, login, logout, profile)
  * User-contributed submissions for raga / taal / knowledge, gated by admin approval
  * Admin moderation queue (approve / reject with a note)
  * Serves the static frontend (index.html, css/, js/, pages/) from the same dir
"""
import os
import secrets
from datetime import timedelta
from functools import wraps
from pathlib import Path

from flask import (
    Flask, abort, jsonify, request, send_from_directory, session,
)

import data
import store

# Project layout puts the static frontend (index.html, css/, js/, pages/) inside `backend/`
# alongside this file. CV_ROOT can override it; otherwise we serve from this file's directory.
ROOT = Path(os.environ.get("CV_ROOT", Path(__file__).resolve().parent))
FRONTEND = ROOT  # no separate /frontend folder in this layout

app = Flask(__name__, static_folder=None)
app.config.update(
    SECRET_KEY=os.environ.get("CV_SECRET", secrets.token_hex(32)),
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    PERMANENT_SESSION_LIFETIME=timedelta(days=14),
)


# ---------- session helpers ----------
SESSION_USER_KEY = "uid"


def current_user() -> dict | None:
    uid = session.get(SESSION_USER_KEY)
    if not uid:
        return None
    u = store.get_user_by_id(uid)
    if not u:
        session.pop(SESSION_USER_KEY, None)
        return None
    return {k: v for k, v in u.items() if k != "password_hash"}


def login_required(fn):
    @wraps(fn)
    def wrapper(*a, **kw):
        u = current_user()
        if not u:
            return jsonify({"error": "auth required"}), 401
        request.current_user = u  # type: ignore[attr-defined]
        return fn(*a, **kw)
    return wrapper


def admin_required(fn):
    @wraps(fn)
    def wrapper(*a, **kw):
        u = current_user()
        if not u:
            return jsonify({"error": "auth required"}), 401
        if u.get("role") != "admin":
            return jsonify({"error": "admin only"}), 403
        request.current_user = u  # type: ignore[attr-defined]
        return fn(*a, **kw)
    return wrapper


# ---------- startup ----------
def _apply_submission(sub: dict) -> None:
    cat = sub["category"]
    payload = sub["payload"]
    if cat == "raga":
        data.add_raga(payload)
    elif cat == "taal":
        data.add_taal(payload)
    elif cat == "knowledge":
        data.add_knowledge(payload)
    elif cat in ("bandish", "kriti"):
        data.add_bandish(payload)
    elif cat == "artist":
        data.add_artist(payload)
    elif cat == "guru":
        data.add_guru(payload)
    elif cat == "concert":
        data.add_concert(payload)
    elif cat == "course":
        data.add_course(payload)
    elif cat == "thread":
        data.add_thread(payload)
    elif cat == "archive":
        data.add_archive(payload)


def _bootstrap() -> None:
    """Create the default admin (if missing) and re-apply previously-approved
    submissions so they appear in the public lists after a server restart."""
    admin = store.ensure_admin()
    if admin:
        app.logger.warning(
            "ClassicalVerse: seeded default admin user '%s' (id=%s). "
            "Change the password after first login.", admin["username"], admin["id"],
        )
    for sub in store.list_submissions(status="approved"):
        try:
            _apply_submission(sub)
        except Exception as exc:  # noqa: BLE001
            app.logger.warning(
                "Failed to re-apply approved sub %s: %s", sub.get("id"), exc,
            )


# ---------- JSON error handlers ----------
@app.errorhandler(404)
def _not_found(e):
    if request.path.startswith("/api/"):
        return jsonify({"error": "not found"}), 404
    return e, 404


@app.errorhandler(500)
def _server_error(e):
    return jsonify({"error": "server error"}), 500


# ---------- JSON API (read-only modules) ----------
@app.get("/api/modules")
def api_modules(): return jsonify(data.MODULES)


@app.get("/api/ragas")
def api_ragas(): return jsonify(data.RAGAS)


@app.get("/api/ragas/<slug>")
def api_raga(slug):
    item = next((r for r in data.RAGAS if r["slug"] == slug), None)
    if not item: abort(404)
    related = [b for b in data.BANDISHES if b["raga"] == item["name"]]
    return jsonify({"raga": item, "bandishes": related})


@app.get("/api/bandishes")
def api_bandishes(): return jsonify(data.BANDISHES)


@app.get("/api/bandishes/<slug>")
def api_bandish(slug):
    item = next((b for b in data.BANDISHES if b["slug"] == slug), None)
    if not item: abort(404)
    related = next((r for r in data.RAGAS if r["name"] == item.get("raga")), None)
    return jsonify({"bandish": item, "raga": related})


@app.get("/api/taals")
def api_taals(): return jsonify(data.TAALS)


@app.get("/api/taals/<slug>")
def api_taal(slug):
    item = next((t for t in data.TAALS if t["slug"] == slug), None)
    if not item: abort(404)
    related = [b for b in data.BANDISHES if b.get("taal") == item["name"]]
    return jsonify({"taal": item, "bandishes": related})


@app.get("/api/artists")
def api_artists(): return jsonify(data.ARTISTS)


@app.get("/api/artists/<slug>")
def api_artist(slug):
    item = next((a for a in data.ARTISTS if a["slug"] == slug), None)
    if not item: abort(404)
    return jsonify({"artist": item})


@app.get("/api/gurus")
def api_gurus(): return jsonify(data.GURUS)


@app.get("/api/gurus/<slug>")
def api_guru(slug):
    item = next((g for g in data.GURUS if g["slug"] == slug), None)
    if not item: abort(404)
    return jsonify({"guru": item})


@app.get("/api/concerts")
def api_concerts(): return jsonify(data.CONCERTS)


@app.get("/api/concerts/<slug>")
def api_concert(slug):
    item = next((c for c in data.CONCERTS if c["slug"] == slug), None)
    if not item: abort(404)
    return jsonify({"concert": item})


@app.get("/api/courses")
def api_courses(): return jsonify(data.COURSES)


@app.get("/api/courses/<slug>")
def api_course(slug):
    item = next((c for c in data.COURSES if c["slug"] == slug), None)
    if not item: abort(404)
    return jsonify({"course": item})


@app.get("/api/community")
def api_community(): return jsonify(data.FORUM_THREADS)


@app.get("/api/community/<slug>")
def api_thread(slug):
    item = next((t for t in data.FORUM_THREADS if t["slug"] == slug), None)
    if not item: abort(404)
    return jsonify({"thread": item})


@app.get("/api/archives")
def api_archives(): return jsonify(data.ARCHIVES)


@app.get("/api/archives/<slug>")
def api_archive(slug):
    item = next((a for a in data.ARCHIVES if a["slug"] == slug), None)
    if not item: abort(404)
    return jsonify({"archive": item})


@app.get("/api/knowledge")
def api_knowledge(): return jsonify(data.KNOWLEDGE)

# ---------- Auth API ----------
@app.post("/api/auth/register")
def api_register():
    body = request.get_json(silent=True) or {}
    try:
        user = store.create_user(
            username=body.get("username", ""),
            email=body.get("email", ""),
            password=body.get("password", ""),
        )
    except store.UserExists as exc:
        return jsonify({"error": str(exc)}), 409
    except store.AuthError as exc:
        return jsonify({"error": str(exc)}), 400
    session.permanent = True
    session[SESSION_USER_KEY] = user["id"]
    return jsonify({"user": user}), 201


@app.post("/api/auth/login")
def api_login():
    body = request.get_json(silent=True) or {}
    try:
        user = store.authenticate(
            body.get("username", ""),
            body.get("password", ""),
        )
    except store.AuthError as exc:
        return jsonify({"error": str(exc)}), 401
    session.permanent = True
    session[SESSION_USER_KEY] = user["id"]
    return jsonify({"user": user})


@app.post("/api/auth/logout")
def api_logout():
    session.pop(SESSION_USER_KEY, None)
    return jsonify({"ok": True})


@app.get("/api/auth/me")
def api_me():
    u = current_user()
    return jsonify({"user": u})


# ---------- Profile: my submissions ----------
@app.get("/api/profile")
@login_required
def api_profile():
    u = request.current_user  # type: ignore[attr-defined]
    subs = store.submissions_with_users(user_id=u["id"])
    return jsonify({"user": u, "submissions": subs})


# ---------- Submissions (user) ----------
@app.post("/api/submissions")
@login_required
def api_create_submission():
    u = request.current_user  # type: ignore[attr-defined]
    body = request.get_json(silent=True) or {}
    category = (body.get("category") or "").strip()
    payload = body.get("payload") or {}
    try:
        sub = store.create_submission(u["id"], category, payload)
    except store.AuthError as exc:
        return jsonify({"error": str(exc)}), 400
    return jsonify({"submission": sub}), 201


# ---------- Admin moderation ----------
@app.get("/api/admin/submissions")
@admin_required
def api_admin_list():
    status = request.args.get("status")  # pending | approved | rejected | None
    return jsonify(store.submissions_with_users(status=status))


@app.post("/api/admin/submissions/<sub_id>/approve")
@admin_required
def api_admin_approve(sub_id):
    admin = request.current_user  # type: ignore[attr-defined]
    note = (request.get_json(silent=True) or {}).get("note", "")
    try:
        sub = store.review_submission(sub_id, admin["id"], True, note)
    except store.AuthError as exc:
        return jsonify({"error": str(exc)}), 400
    _apply_submission(sub)
    return jsonify({"submission": sub})


@app.post("/api/admin/submissions/<sub_id>/reject")
@admin_required
def api_admin_reject(sub_id):
    admin = request.current_user  # type: ignore[attr-defined]
    note = (request.get_json(silent=True) or {}).get("note", "")
    try:
        sub = store.review_submission(sub_id, admin["id"], False, note)
    except store.AuthError as exc:
        return jsonify({"error": str(exc)}), 400
    return jsonify({"submission": sub})


# ---------- Admin: module management (delete any entry) ----------
@app.delete("/api/admin/<module_name>")
@admin_required
def api_admin_delete_module_entry(module_name):
    """Delete an entry from one of the content lists by ?slug=... (or ?title=... for threads)."""
    slug = (request.args.get("slug") or "").strip()
    if not slug:
        return jsonify({"error": "slug required"}), 400
    table = {
        "ragas": data.RAGAS, "taals": data.TAALS, "bandishes": data.BANDISHES,
        "artists": data.ARTISTS, "gurus": data.GURUS, "concerts": data.CONCERTS,
        "courses": data.COURSES, "archive": data.ARCHIVES, "archives": data.ARCHIVES,
        "knowledge": data.KNOWLEDGE,
    }.get(module_name)
    if table is None:
        return jsonify({"error": f"unknown module '{module_name}'"}), 404
    for i in range(len(table) - 1, -1, -1):
        if table[i].get("slug") == slug:
            table.pop(i)
            break
    else:
        return jsonify({"error": "not found"}), 404
    # threads are deleted by title, not slug
    if module_name == "threads":
        for i in range(len(data.FORUM_THREADS) - 1, -1, -1):
            if data.FORUM_THREADS[i].get("title") == slug:
                data.FORUM_THREADS.pop(i)
                break
    # refresh module counts
    if module_name in ("ragas",): data.MODULES[0]["count"] = len(data.RAGAS)
    if module_name in ("bandishes",): data.MODULES[1]["count"] = len(data.BANDISHES)
    if module_name in ("taals",): data.MODULES[2]["count"] = len(data.TAALS)
    if module_name in ("artists",): data.MODULES[3]["count"] = len(data.ARTISTS)
    if module_name in ("gurus",): data.MODULES[4]["count"] = len(data.GURUS)
    if module_name in ("concerts",): data.MODULES[5]["count"] = len(data.CONCERTS)
    if module_name in ("courses",): data.MODULES[6]["count"] = len(data.COURSES)
    if module_name in ("threads",): data.MODULES[7]["count"] = len(data.FORUM_THREADS)
    if module_name in ("archive", "archives"): data.MODULES[8]["count"] = len(data.ARCHIVES)
    if module_name in ("knowledge",): data.MODULES[9]["count"] = len(data.KNOWLEDGE)
    return jsonify({"ok": True})


# ---------- Admin: user management ----------
@app.get("/api/admin/users")
@admin_required
def api_admin_list_users():
    return jsonify(store.list_users())


@app.post("/api/admin/users/<user_id>/role")
@admin_required
def api_admin_set_role(user_id):
    body = request.get_json(silent=True) or {}
    role = (body.get("role") or "").strip()
    if role not in ("user", "admin"):
        return jsonify({"error": "role must be 'user' or 'admin'"}), 400
    try:
        user = store.set_user_role(user_id, role)
    except store.AuthError as exc:
        return jsonify({"error": str(exc)}), 400
    return jsonify({"user": user})


@app.delete("/api/admin/users/<user_id>")
@admin_required
def api_admin_delete_user(user_id):
    try:
        store.delete_user(user_id)
    except store.AuthError as exc:
        return jsonify({"error": str(exc)}), 400
    return jsonify({"ok": True})


# ---------- Static frontend ----------
@app.get("/")
def root(): return send_from_directory(FRONTEND, "index.html")


@app.get("/<path:filename>")
def static_files(filename):
    # Never let the static handler swallow API routes, regardless of decorator order.
    if filename == "api" or filename.startswith("api/"):
        abort(404)
    # Reject any traversal attempts before touching the filesystem.
    if ".." in Path(filename).parts:
        abort(404)
    target = FRONTEND / filename
    if target.is_dir():
        idx = target / "index.html"
        if idx.exists():
            return send_from_directory(target, "index.html")
    if target.exists():
        return send_from_directory(FRONTEND, filename)
    # Try .html fallback (e.g. /ragas -> pages/ragas.html)
    html_try = FRONTEND / "pages" / f"{filename}.html"
    if html_try.exists():
        return send_from_directory(FRONTEND / "pages", f"{filename}.html")
    # Try /<thing>-item fallback (e.g. /archive?slug=... -> pages/archive-item.html)
    if "." not in filename:
        item_try = FRONTEND / "pages" / f"{filename}-item.html"
        if item_try.exists():
            return send_from_directory(FRONTEND / "pages", f"{filename}-item.html")
    # Top-level pages (login.html, signup.html, submit.html, profile.html, admin.html)
    top_try = FRONTEND / f"{filename}.html"
    if top_try.exists():
        return send_from_directory(FRONTEND, f"{filename}.html")
    abort(404)


_bootstrap()


if __name__ == "__main__":
    print(f"Serving frontend from: {FRONTEND}")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
