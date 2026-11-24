"""
Run this script ONCE to copy your uploaded collage photo as the hero background.

Usage:
  1. Save your collage photo (the instrument grid image) anywhere on your computer.
  2. Run:  python _save_hero.py path\to\your\photo.jpg
  3. The script copies it to backend/images/hero-bg.jpg and the site picks it up.

If you don't have the file handy, the script can also download a matching
high-quality placeholder from Unsplash until you replace it.
"""
import sys
import shutil
from pathlib import Path

DEST = Path(__file__).parent / "images" / "hero-bg.jpg"
DEST.parent.mkdir(exist_ok=True)

if len(sys.argv) > 1:
    src = Path(sys.argv[1])
    if not src.exists():
        print(f"ERROR: file not found: {src}")
        sys.exit(1)
    shutil.copy2(src, DEST)
    print(f"Saved hero background → {DEST}")
else:
    # Download a verified Indian classical music collage from Wikimedia
    try:
        import urllib.request
        url = (
            "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/"
            "Indian_string_instruments_-_Saravati_vina%2C_Bin_or_Rudra_veena%2C_Esraj_or_Diltuba%2C"
            "Tambura%2C_Fiddle_or_Violin%2C_Sitar%2C_Surbahar%2C_Sarangi%2C_Tambura_-_Harmonium%2C"
            "Tabla_-_MIM_Brussels_%282018-05-26_10.41.21_by_Miguel_Discart_%40Flickr_46273431562%29.jpg/"
            "1280px-thumbnail.jpg"
        )
        req = urllib.request.Request(url, headers={"User-Agent": "ClassicalVerse/1.0"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            DEST.write_bytes(resp.read())
        print(f"Saved hero background → {DEST}")
        print("Replace it later with your own photo using:  python _save_hero.py your_photo.jpg")
    except Exception as e:
        print(f"Download failed: {e}")
        print("Please manually copy your photo to:  backend/images/hero-bg.jpg")
