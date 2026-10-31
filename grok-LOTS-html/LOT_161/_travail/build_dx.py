#!/usr/bin/env python3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import specs_suite  # enregistre les DX.2 à DX.10
from dx_commun import ecrire_dx
from gabarit_dx import details, fiches
from gabarit_plus import extra
from specs_dx import SPECS

def main():
    voulu = int(sys.argv[1]) if len(sys.argv) > 1 else None
    for i, s in enumerate(SPECS, start=1):
        if voulu and i != voulu:
            continue
        d = details(s)
        for k in range(1, 15):
            d[k] = d[k] + "\n\n" + extra(s, k)
        ecrire_dx(i, s["nom"], fiches(s), d)

if __name__ == "__main__":
    main()
