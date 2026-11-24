import json, sys, urllib.request
BASE = "http://127.0.0.1:5000"
PATHS = [
    "/api/bandishes/piya-bawari",
    "/api/taals/teentaal",
    "/api/artists/ravi-shankar",
    "/api/gurus/guruji-anand",
    "/api/concerts/sawai-gandharva",
    "/api/courses/khayal-craft",
    "/api/community/samay-relevance",
    "/api/archives/all-india-radio-1955",
]
ok = 0
for p in PATHS:
    try:
        with urllib.request.urlopen(BASE + p, timeout=5) as r:
            data = json.loads(r.read())
            if p == "/api/bandishes/piya-bawari":
                b = data["bandish"]
                print(f"OK {p} -> {b['title']} | YT={bool(b.get('youtube'))} SP={bool(b.get('spotify'))} | related raga={data['raga']['name']}")
            elif p == "/api/taals/teentaal":
                t = data["taal"]
                print(f"OK {p} -> {t['name']} {t['beats']}b | YT={bool(t.get('youtube'))} SP={bool(t.get('spotify'))} | related bandishes={len(data['bandishes'])}")
            elif p == "/api/archives/all-india-radio-1955":
                a = data["archive"]
                print(f"OK {p} -> {a['title']} {a['year']} | YT={bool(a.get('youtube'))} SP={bool(a.get('spotify'))}")
            else:
                k = list(data.keys())[0]
                print(f"OK {p} -> {data[k].get('title') or data[k].get('name')}")
            ok += 1
    except Exception as e:
        print(f"FAIL {p}: {e}", file=sys.stderr)
print(f"\n{ok}/{len(PATHS)} endpoints OK")
sys.exit(0 if ok == len(PATHS) else 1)
