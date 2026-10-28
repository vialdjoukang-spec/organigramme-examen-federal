#!/usr/bin/env python3
"""α6·H — phrases verbales et longueur · point 6 « Examen physique ciblé, région par région »
Généré par harnais/brain/outils/gabarit.py depuis synapses.json et familles.py : NE PAS ÉDITER À LA MAIN (régénérer).
Codes : AH1 phrase nominale · AH2 phrase de plus de 35 mots
Entrée : paquet du point 6 (cours HTML) · sortie : contrat brain.scriptone/1 · écrit : rien (lecteur) · jumeau : b06_L."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import bus, familles as F

ID, REGION, VERSION, ZONE, POINT, FAMILLE = "a06_H", "ALP", F.VERSION, "alpha", 6, "H"
DEPEND = ["familles.py", "synapses.json", "verbes.json"]
analyser = F.analyseur("A", FAMILLE, POINT)
corriger = F.correcteur("A", FAMILLE, POINT)
MUTANTS = F.mutants("A", FAMILLE, POINT)
ECRIT = F.zones("A", FAMILLE, POINT)

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))
