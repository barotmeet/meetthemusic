"""Download verified Indian classical music images for ClassicalVerse."""
import sys
import time
import urllib.request
from pathlib import Path

IMAGES_DIR = Path(__file__).parent / "images"
IMAGES_DIR.mkdir(exist_ok=True)

# Verified via Wikimedia Commons API (2026-06)
DOWNLOADS = {
    "hero-bg.jpg": (
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/"
        "Indian_string_instruments_-_Saravati_vina%2C_Bin_or_Rudra_veena%2C_Esraj_or_Diltuba%2C"
        "Tambura%2C_Fiddle_or_Violin%2C_Sitar%2C_Surbahar%2C_Sarangi%2C_Tambura_-_Harmonium%2C"
        "Tabla_-_MIM_Brussels_%282018-05-26_10.41.21_by_Miguel_Discart_%40Flickr_46273431562%29.jpg/"
        "1280px-thumbnail.jpg"
    ),
    "tabla.jpg": (
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Tabla.jpg/960px-Tabla.jpg"
    ),
    "sitar.jpg": "https://upload.wikimedia.org/wikipedia/commons/b/ba/Sitar_full.jpg",
    "performance.jpg": (
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/"
        "An_Indian_classical_music_performance.jpg/960px-An_Indian_classical_music_performance.jpg"
    ),
}


def download(name: str, url: str) -> None:
    dest = IMAGES_DIR / name
    print(f"Downloading {name}...")
    req = urllib.request.Request(url, headers={"User-Agent": "ClassicalVerse/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    if len(data) < 5000:
        raise RuntimeError(f"{name}: response too small ({len(data)} bytes)")
    dest.write_bytes(data)
    print(f"  Saved {dest} ({len(data):,} bytes)")


def main() -> int:
    failed = []
    for i, (name, url) in enumerate(DOWNLOADS.items()):
        if i:
            time.sleep(3)
        try:
            download(name, url)
        except Exception as exc:
            print(f"  ERROR {name}: {exc}", file=sys.stderr)
            failed.append(name)

    if failed:
        print(f"\nFailed: {', '.join(failed)}", file=sys.stderr)
        return 1
    print("\nAll images ready in backend/images/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
