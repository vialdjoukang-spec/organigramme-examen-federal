#!/usr/bin/env python3
"""α8·S — structure du point · point 8 « Diagnostic positif et critères »
Généré par harnais/brain/outils/gabarit.py depuis synapses.json et familles.py : NE PAS ÉDITER À LA MAIN (régénérer).
Codes : AS1 absent · AS2 titre sans gras · AS3 doublon · AS4 élément requis absent · AS5 ordre
Entrée : paquet du point 8 (cours HTML) · sortie : contrat brain.scriptone/1 · écrit : P8:titre · jumeau : b08_X."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import bus, familles as F

ID, REGION, VERSION, ZONE, POINT, FAMILLE = "a08_S", "ALP", F.VERSION, "alpha", 8, "S"
DEPEND = ["familles.py", "synapses.json", "verbes.json"]
analyser = F.analyseur("A", FAMILLE, POINT)
corriger = F.correcteur("A", FAMILLE, POINT)
MUTANTS = F.mutants("A", FAMILLE, POINT)
ECRIT = F.zones("A", FAMILLE, POINT)

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))
