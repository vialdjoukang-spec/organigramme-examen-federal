#!/usr/bin/env python3
"""Assemble les 11 HTML, la liste canonique et le contrôle des chiffres."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fabriquer import DX, ROOT, ecrire_un, nombres_ok
from contenu import rendre, urgence
from banque import dx1
from banque2 import dx2
from banque3 import dx3, dx4
from banque4 import dx5, dx6
from banque5 import dx7, dx8, dx9, dx10
from phase_a import spec as spec_a, liste_html

FNS = {1: dx1, 2: dx2, 3: dx3, 4: dx4, 5: dx5, 6: dx6, 7: dx7, 8: dx8, 9: dx9, 10: dx10}
E_H2 = {8: " E3", 9: " E1", 10: " E2"}

def main() -> int:
    (ROOT / "LISTE_DX_CANONIQUE.md").write_text(
        "# LOT_130 — liste canonique gelée\n\n"
        "Gel après établissement des dix diagnostics du SSP F1.1, le 9 novembre 2026. "
        "Justification dans LISTE_DX_JUSTIFICATION.md.\n\n"
        + "\n".join(f"DX.{i} — {nom}" for i, nom, _e in DX)
        + "\n",
        encoding="utf-8",
    )
    erreurs = []
    secs = rendre("ssp", spec_a())
    p = ecrire_un("LOT_130_Phase_A_V0.html", "Phase A — Pression artérielle anormale (F1.1)", "ssp", secs,
                  "<!-- FIN_FICHIER LOT_130_PHASE_A -->", extra=liste_html())
    err = nombres_ok(p.read_text(encoding="utf-8"))
    print(f"Phase A {p.stat().st_size} o, nombres {len(err)}")
    erreurs += [("A", e) for e in err]
    for i, nom, _e in DX:
        sections = rendre(f"dx{i}", FNS[i]())
        if i == 1 and "p11-urgence" not in sections[10]:
            sections[10] += urgence("dx1", [
                ("On cherche d'abord une atteinte aiguë d'organe si la pression est très haute.", ["ESCURG"]),
                ("On n'abaisse pas cette pression de façon rapide et non contrôlée.", ["ESCVIT"]),
                ("On n'utilise pas le ramipril pendant la grossesse.", ["AIPSCI"]),
            ])
        h2 = f"DX.{i} — {nom}{E_H2.get(i, '')}"
        path = ecrire_un(f"LOT_130_Phase_B_V0_DX.{i}.html", h2, f"dx{i}", sections,
                         f"<!-- FIN_FICHIER LOT_130_PHASE_B_DX.{i} -->")
        err = nombres_ok(path.read_text(encoding="utf-8"))
        print(f"DX.{i} {path.stat().st_size} o, nombres {len(err)}")
        for e in err[:12]:
            print("  ", e[:200])
        erreurs += [(f"DX.{i}", e) for e in err]
    print("TOTAL erreurs", len(erreurs))
    return 1 if erreurs else 0

if __name__ == "__main__":
    raise SystemExit(main())
