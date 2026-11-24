"""End-to-end smoke test for the auth + submission + admin flow.

Spins up the Flask test client (no network needed) and exercises:
  1. register a regular user
  2. submit a raga, a taal, and a knowledge article
  3. verify they do NOT appear in the public lists yet
  4. log in as the seeded admin
  5. list pending submissions, approve one and reject one
  6. verify the approved one IS now in the public list
  7. fetch the contributor's profile and confirm status messages

Run:  python test_flow.py
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

# Make sure we run against a clean store for repeatable results
HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
if DATA.exists():
    for f in DATA.glob("*.json"):
        f.unlink()

# Boot the app — this also seeds the default admin
sys.path.insert(0, str(HERE))
import app as cv_app  # noqa: E402

client = cv_app.app.test_client()


def check(label: str, ok: bool, detail: str = "") -> None:
    mark = "PASS" if ok else "FAIL"
    print(f"  [{mark}] {label}{(' — ' + detail) if detail else ''}")
    if not ok:
        sys.exit(1)


def show(label: str, resp) -> None:
    body = resp.get_data(as_text=True)
    try:
        body = json.dumps(json.loads(body), indent=2)[:400]
    except Exception:
        body = body[:400]
    print(f"  >> {label} {resp.status_code} {body}")


print("== 1. Register regular user ==")
r = client.post("/api/auth/register", json={
    "username": "alice", "email": "alice@x.com", "password": "secret1",
})
show("register alice", r)
check("register returns 201", r.status_code == 201)
alice_id = r.get_json()["user"]["id"]
check("alice is 'user' role", r.get_json()["user"]["role"] == "user")

print("\n== 2. Submit a raga ==")
r = client.post("/api/submissions", json={
    "category": "raga",
    "payload": {
        "name": "Demo Raga", "tradition": "Hindustani", "thaat": "Bilawal",
        "time": "Morning", "mood": "Devotional",
        "aroh": "S R G M P D N S", "avroh": "S N D P M G R S",
        "description": "A raga submitted by alice.",
    },
})
show("submit raga", r)
check("submit returns 201", r.status_code == 201)
raga_sub_id = r.get_json()["submission"]["id"]

print("\n== 3. Submit a knowledge article ==")
r = client.post("/api/submissions", json={
    "category": "knowledge",
    "payload": {
        "title": "On the Pakad",
        "body": "The pakad is the catchphrase of a raga — a short melodic motif that uniquely identifies it.",
        "tags": ["theory", "intermediate"],
    },
})
show("submit knowledge", r)
check("submit returns 201", r.status_code == 201)
know_sub_id = r.get_json()["submission"]["id"]

print("\n== 4. Public list should NOT contain the new entries yet ==")
r = client.get("/api/ragas")
public_ragas = r.get_json()
check("no Demo Raga publicly visible",
      not any(x["name"] == "Demo Raga" for x in public_ragas),
      f"({len(public_ragas)} ragas visible)")

r = client.get("/api/knowledge")
public_knowledge = r.get_json()
check("no 'On the Pakad' publicly visible",
      not any(x["title"] == "On the Pakad" for x in public_knowledge))

print("\n== 5. Profile shows pending entries ==")
r = client.get("/api/profile")
show("profile", r)
check("profile returns 200", r.status_code == 200)
profile = r.get_json()
check("profile lists 2 submissions", len(profile["submissions"]) == 2)
check("all are pending",
      all(s["status"] == "pending" for s in profile["submissions"]))

print("\n== 6. Log in as admin ==")
r = client.post("/api/auth/logout")
r = client.post("/api/auth/login", json={"username": "admin", "password": "admin123"})
show("admin login", r)
check("admin login returns 200", r.status_code == 200)
check("admin role", r.get_json()["user"]["role"] == "admin")

print("\n== 7. Admin sees pending queue ==")
r = client.get("/api/admin/submissions?status=pending")
show("pending list", r)
check("admin sees 2 pending", r.status_code == 200 and len(r.get_json()) == 2)

print("\n== 8. Approve the raga ==")
r = client.post(f"/api/admin/submissions/{raga_sub_id}/approve",
                json={"note": "Welcome to the library!"})
show("approve raga", r)
check("approve returns 200", r.status_code == 200)
check("status is approved", r.get_json()["submission"]["status"] == "approved")

print("\n== 9. Reject the knowledge article ==")
r = client.post(f"/api/admin/submissions/{know_sub_id}/reject",
                json={"note": "Please add references."})
show("reject knowledge", r)
check("reject returns 200", r.status_code == 200)
check("status is rejected", r.get_json()["submission"]["status"] == "rejected")

print("\n== 10. Public list now contains the approved raga ==")
r = client.get("/api/ragas")
public_ragas = r.get_json()
check("Demo Raga is publicly visible",
      any(x["name"] == "Demo Raga" for x in public_ragas),
      f"({len(public_ragas)} ragas visible)")
r = client.get("/api/knowledge")
public_knowledge = r.get_json()
check("rejected knowledge NOT publicly visible",
      not any(x["title"] == "On the Pakad" for x in public_knowledge))

print("\n== 11. Non-admin cannot access admin endpoint ==")
client.post("/api/auth/logout")
client.post("/api/auth/login", json={"username": "alice", "password": "secret1"})
r = client.get("/api/admin/submissions")
check("non-admin gets 403", r.status_code == 403)
r = client.post(f"/api/admin/submissions/{raga_sub_id}/approve", json={})
check("non-admin approve gets 403", r.status_code == 403)

print("\n== 12. Alice's profile now shows statuses ==")
r = client.get("/api/profile")
profile = r.get_json()
statuses = sorted(s["status"] for s in profile["submissions"])
check("profile statuses are approved+rejected",
      statuses == ["approved", "rejected"],
      f"({statuses})")
for s in profile["submissions"]:
    note = s.get("admin_note", "")
    print(f"     - {s['category']:10s} {s['status']:9s} note='{note}'")

print("\n== 13. Auth-required endpoint ==")
client.post("/api/auth/logout")
r = client.get("/api/profile")
check("anonymous /api/profile returns 401", r.status_code == 401)

print("\nAll flow checks passed.")
