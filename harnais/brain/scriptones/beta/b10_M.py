#!/usr/bin/env python3
"""β10·M — contre-épreuve par mutation (sentinelle sur le fichier réel) · point 10 « Arbre décisionnel »
Généré par harnais/brain/outils/gabarit.py depuis synapses.json et familles.py : NE PAS ÉDITER À LA MAIN (régénérer).
Codes : BM1 synapse α aveugle sur ce fichier
Entrée : paquet du point 10 (cours HTML) · sortie : contrat brain.scriptone/1 · écrit : rien (lecteur) · jumeau : a10_S."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import bus, familles as F

ID, REGION, VERSION, ZONE, POINT, FAMILLE = "b10_M", "BET", F.VERSION, "beta", 10, "M"
DEPEND = ["familles.py", "synapses.json", "verbes.json"]
analyser = F.analyseur("B", FAMILLE, POINT)
corriger = F.correcteur("B", FAMILLE, POINT)
MUTANTS = F.mutants("B", FAMILLE, POINT)
ECRIT = F.zones("B", FAMILLE, POINT)

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))
