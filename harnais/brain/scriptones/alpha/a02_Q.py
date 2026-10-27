#!/usr/bin/env python3
"""α2·Q — continuité du texte (bloc, lignes séparées, nombre de phrases) · point 2 « Épidémiologie (Suisse, puis Europe) »
Généré par harnais/brain/outils/gabarit.py depuis synapses.json et familles.py : NE PAS ÉDITER À LA MAIN (régénérer).
Codes : AQ1 lignes séparées (bloc exigé) · AQ2 étiquette en tête de phrase · AQ3 nombre de phrases hors bornes · AQ4 texte haché
Entrée : paquet du point 2 (cours HTML) · sortie : contrat brain.scriptone/1 · écrit : P2:blocs · jumeau : b02_X."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import bus, familles as F

ID, REGION, VERSION, ZONE, POINT, FAMILLE = "a02_Q", "ALP", F.VERSION, "alpha", 2, "Q"
DEPEND = ["familles.py", "synapses.json", "verbes.json"]
analyser = F.analyseur("A", FAMILLE, POINT)
corriger = F.correcteur("A", FAMILLE, POINT)
MUTANTS = F.mutants("A", FAMILLE, POINT)
ECRIT = F.zones("A", FAMILLE, POINT)

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))
