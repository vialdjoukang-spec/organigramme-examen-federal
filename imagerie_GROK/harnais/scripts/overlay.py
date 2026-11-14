#!/usr/bin/env python3
"""overlay.py — superpose flèches et contours d'un manifeste sur l'image pathologique.
Usage : python3 scripts/overlay.py manifest/IMG-344.json [/tmp/IMG-344_overlay.png]
Le fichier produit sert au contrôle visuel (Read). Il ne remplace pas le jugement.
"""
import json, os, sys
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COL = {
    "principale": (255, 212, 0),
    "associee": (0, 229, 255),
    "secondaire": (124, 255, 79),
    "complication": (255, 59, 107),
}

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    src = sys.argv[1]
    if not os.path.isabs(src):
        src = os.path.join(ROOT, src)
    m = json.load(open(src, encoding="utf-8"))
    rel = (m.get("patho") or {}).get("file")
    if not rel:
        print("pas d'image pathologique")
        sys.exit(1)
    img_path = rel if os.path.isabs(rel) else os.path.join(ROOT, rel)
    im = Image.open(img_path).convert("RGB")
    W, H = im.size
    dr = ImageDraw.Draw(im)
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(img_path)[0] + "_overlay.png"
    for i, a in enumerate((m.get("patho") or {}).get("arrows") or [], 1):
        col = COL.get(a.get("role"), COL["principale"])
        pts = a.get("contour") or []
        if len(pts) >= 2:
            xy = [(p[0] * W, p[1] * H) for p in pts]
            dr.line(xy, fill=(6, 16, 24), width=5)
            dr.line(xy, fill=col, width=2)
        tip, fr = a.get("tip"), a.get("from")
        if tip and fr:
            x1, y1, x2, y2 = fr[0] * W, fr[1] * H, tip[0] * W, tip[1] * H
            dr.line([(x1, y1), (x2, y2)], fill=(6, 16, 24), width=4)
            dr.line([(x1, y1), (x2, y2)], fill=col, width=2)
            r = 11
            dr.ellipse([x1 - r, y1 - r, x1 + r, y1 + r], fill=col, outline=(6, 16, 24))
            dr.text((x1 - 4, y1 - 6), str(i), fill=(6, 16, 24))
    im.save(out, "PNG")
    print(out)

if __name__ == "__main__":
    main()
