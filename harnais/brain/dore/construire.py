#!/usr/bin/env python3
"""Construit le jeu doré : source.html → arbre rendu (S5) → conversion forme_interactive → corrections S8, S3, S2, S1 → cours_dore.html.
Le jeu doré doit produire ZÉRO doléance (spécificité) ; chaque mutant doit produire la sienne (sensibilité). Déterministe."""
import sys
from pathlib import Path
D = Path(__file__).resolve().parent
sys.path.insert(0, str(D.parent))
import cerveau

if __name__ == "__main__":
    t = cerveau.corriger((D / "source.html").read_text(encoding="utf-8"), convertir=True)
    (D / "cours_dore.html").write_text(t, encoding="utf-8")
    Dl, _ = cerveau.analyser(t, "cours_dore.html", ecrire=False)
    print(f"cours_dore.html : {len(t.encode()) // 1000} Ko · {len(Dl)} doléance(s)")
    for d in Dl: print(f"- {d['severite']} {d['code']} {d['ancre']} : {d['constat']}")
    sys.exit(1 if Dl else 0)
