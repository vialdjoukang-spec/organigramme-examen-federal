#!/usr/bin/env python3
"""α9·R — récit négatif interdit · point 9 « Examens complémentaires »
Généré par harnais/brain/outils/gabarit.py depuis synapses.json et familles.py : NE PAS ÉDITER À LA MAIN (régénérer).
Codes : AR1 phrase d'absence pure (supprimée par script) · AR2 phrase mixte · AR3 dose « à vérifier » · AR4 dans une fenêtre
Entrée : paquet du point 9 (cours HTML) · sortie : contrat brain.scriptone/1 · écrit : P9:absence · jumeau : b09_S."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import bus, familles as F

ID, REGION, VERSION, ZONE, POINT, FAMILLE = "a09_R", "ALP", F.VERSION, "alpha", 9, "R"
DEPEND = ["familles.py", "synapses.json", "verbes.json"]
analyser = F.analyseur("A", FAMILLE, POINT)
corriger = F.correcteur("A", FAMILLE, POINT)
MUTANTS = F.mutants("A", FAMILLE, POINT)
ECRIT = F.zones("A", FAMILLE, POINT)

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))
