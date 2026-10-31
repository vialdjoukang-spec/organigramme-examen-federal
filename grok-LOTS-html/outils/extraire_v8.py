#!/usr/bin/env python3
"""Extraction des points d'une leçon V8 (<h2 id="pN">).

harnais/controle_lot.py extraire vise le format V0 (<h3> ou <strong> numérotés) et renvoie
0 octet sur les fichiers Grok. Ne pas modifier le harnais : cet outil est la parade (P-21).

  python3 grok-LOTS-html/outils/extraire_v8.py <fichier.html> --points 1,2,3 [--html]

Code 0 si au moins un point demandé est présent, 1 si la sortie est vide, 2 si l'usage est faux.
"""
from __future__ import annotations
import argparse, html, re, sys
from pathlib import Path


def extraire_v8(path, pts, brut_html: bool = False) -> str:
    """Copie adaptable du prototype du bac à sable (31.10.2026). pts : entiers des id pN."""
    t = Path(path).read_text(encoding="utf-8", errors="replace")
    heads = [(m.start(), int(m.group(1))) for m in re.finditer(r'<h2[^>]*\bid="p(\d{1,2})"', t)]
    ends = [m.start() for m in re.finditer(r'<h2[^>]*\bid="sources"', t)]
    out = []
    voulu = set(pts)
    for k, (pos, n) in enumerate(heads):
        if n in voulu:
            fin = heads[k + 1][0] if k + 1 < len(heads) else (ends[0] if ends else len(t))
            seg = t[pos:fin]
            if not brut_html:
                seg = re.sub(r"<(br|/p|/li|/tr|/h\d|/summary)[^>]*>", "\n", seg, flags=re.I)
                seg = html.unescape(re.sub(r"<[^>]+>", " ", seg))
                seg = re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n", seg))
            out.append(f"=== point {n} ===\n{seg.strip()}")
    return "\n".join(out)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fichier")
    ap.add_argument("--points", required=True, help="ex. 1,2,3 ou 2,3,4,8,9,11,12")
    ap.add_argument("--html", action="store_true", help="conserver le HTML du segment")
    a = ap.parse_args(argv)
    try:
        pts = [int(x) for x in a.points.split(",") if x.strip()]
    except ValueError:
        print("points : entiers séparés par des virgules", file=sys.stderr)
        return 2
    if not pts:
        print("aucun point demandé", file=sys.stderr)
        return 2
    p = Path(a.fichier)
    if not p.is_file():
        print(f"fichier absent : {p}", file=sys.stderr)
        return 2
    texte = extraire_v8(p, pts, a.html)
    sys.stdout.write(texte + ("\n" if texte else ""))
    return 0 if texte.strip() else 1


if __name__ == "__main__":
    sys.exit(main())
