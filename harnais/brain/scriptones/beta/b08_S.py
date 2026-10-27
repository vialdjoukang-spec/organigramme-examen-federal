#!/usr/bin/env python3
"""β8·S — sources du point · point 8 « Diagnostic positif et critères »
Généré par harnais/brain/outils/gabarit.py depuis synapses.json et familles.py : NE PAS ÉDITER À LA MAIN (régénérer).
Codes : BS1 bloc chiffré sans source · BS2 renvoi orphelin · BS3 dose sans source
Entrée : paquet du point 8 (cours HTML) · sortie : contrat brain.scriptone/1 · écrit : rien (lecteur) · jumeau : a08_R."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import bus, familles as F

ID, REGION, VERSION, ZONE, POINT, FAMILLE = "b08_S", "BET", F.VERSION, "beta", 8, "S"
DEPEND = ["familles.py", "synapses.json", "verbes.json"]
analyser = F.analyseur("B", FAMILLE, POINT)
corriger = F.correcteur("B", FAMILLE, POINT)
MUTANTS = F.mutants("B", FAMILLE, POINT)
ECRIT = F.zones("B", FAMILLE, POINT)

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))
