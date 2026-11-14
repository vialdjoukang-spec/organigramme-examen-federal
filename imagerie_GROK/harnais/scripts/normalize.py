#!/usr/bin/env python3
"""normalize.py — JPEG, long side <= 1024 px, quality 85, EXIF/metadata stripped, RGB.
CLI:  python3 scripts/normalize.py <src> <dest.jpg> [--max 1024]
      python3 scripts/normalize.py --inplace <file.jpg> [...]
"""
import sys, io
from PIL import Image, ImageOps

def normalize(src, dest, maxside=1024, quality=85):
    im = Image.open(src)
    try:
        im = ImageOps.exif_transpose(im)
    except Exception:
        pass
    if getattr(im, "n_frames", 1) > 1:
        im.seek(0)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (0, 0, 0))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    elif im.mode in ("I;16", "I", "F"):
        im = ImageOps.autocontrast(im.convert("L"))
    if im.mode != "RGB":
        im = im.convert("RGB")
    w, h = im.size
    s = min(1.0, maxside / max(w, h))
    if s < 1.0:
        im = im.resize((max(1, round(w * s)), max(1, round(h * s))), Image.LANCZOS)
    clean = Image.new("RGB", im.size)
    clean = Image.frombytes("RGB", im.size, im.tobytes())  # drops all metadata
    clean.save(dest, "JPEG", quality=quality, optimize=True, progressive=True)
    return clean.size

if __name__ == "__main__":
    a = sys.argv[1:]
    mx = 1024
    if "--max" in a:
        i = a.index("--max"); mx = int(a[i + 1]); del a[i:i + 2]
    if not a:
        print(__doc__); sys.exit(1)
    if a[0] == "--inplace":
        for f in a[1:]:
            print(f, normalize(f, f, mx))
    else:
        print(a[1], normalize(a[0], a[1], mx))
