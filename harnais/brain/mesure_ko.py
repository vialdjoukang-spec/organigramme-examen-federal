#!/usr/bin/env python3
"""Mesure en Ko (1 Ko = 1 000 octets) des leçons Flash et verdict de bande (Vial, 28.10.2026).
  python3 harnais/brain/mesure_ko.py <fichier|dossier …> [--json]
Bande Flash : 100 à 298 Ko (jamais 299 ni plus) ; visé 100–200 ; > 200 Ko avertissement ; > 298 Ko BLOQUANT (code 1)."""
import json, sys
from pathlib import Path
KO, MIN, VISE, MAX = 1000, 100, 200, 298
def verdict(o):
    k = o / KO
    return "BLOQUANT" if k > MAX else "AVERTISSEMENT" if k > VISE else "TROP COURT" if k < MIN else "OK"
def main(a):
    fs = []
    for x in [x for x in a if not x.startswith("--")]:
        p = Path(x); fs += sorted(p.rglob("*.html")) if p.is_dir() else [p]
    res = [dict(fichier=str(f), ko=round(f.stat().st_size / KO, 1), verdict=verdict(f.stat().st_size)) for f in fs]
    if "--json" in a: print(json.dumps(res, ensure_ascii=False, indent=1))
    else:
        for r in res: print(f"{r['verdict']:<13} {r['ko']:>7.1f} Ko  {r['fichier']}")
    return 1 if any(r["verdict"] == "BLOQUANT" for r in res) else 0
if __name__ == "__main__": sys.exit(main(sys.argv[1:]))
