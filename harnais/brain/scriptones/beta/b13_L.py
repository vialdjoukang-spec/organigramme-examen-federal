#!/usr/bin/env python3
"""β13·L — langue adverse (lexique, anglicismes, typographie) · point 13 « Points clés »
Généré par harnais/brain/outils/gabarit.py depuis synapses.json et familles.py : NE PAS ÉDITER À LA MAIN (régénérer).
Codes : BL1 nuance vague sans chiffre · BL2 anglicisme · BL3 typographie française · BL4 mot doublé
Entrée : paquet du point 13 (cours HTML) · sortie : contrat brain.scriptone/1 · écrit : P13:typo-texte · jumeau : a13_H."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import bus, familles as F

ID, REGION, VERSION, ZONE, POINT, FAMILLE = "b13_L", "BET", F.VERSION, "beta", 13, "L"
DEPEND = ["familles.py", "synapses.json", "verbes.json"]
analyser = F.analyseur("B", FAMILLE, POINT)
corriger = F.correcteur("B", FAMILLE, POINT)
MUTANTS = F.mutants("B", FAMILLE, POINT)
ECRIT = F.zones("B", FAMILLE, POINT)

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))
