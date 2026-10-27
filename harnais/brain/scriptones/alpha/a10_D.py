#!/usr/bin/env python3
"""α10·D — termes dédiés et absence de méta-conception · point 10 « Arbre décisionnel »
Généré par harnais/brain/outils/gabarit.py depuis synapses.json et familles.py : NE PAS ÉDITER À LA MAIN (régénérer).
Codes : AD1 mention de conception · AD2 termes cliquables insuffisants · AD3 fenêtre qui coupe une phrase porteuse · AD4 mot cliquable dans le titre
Entrée : paquet du point 10 (cours HTML) · sortie : contrat brain.scriptone/1 · écrit : rien (lecteur) · jumeau : b10_L."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import bus, familles as F

ID, REGION, VERSION, ZONE, POINT, FAMILLE = "a10_D", "ALP", F.VERSION, "alpha", 10, "D"
DEPEND = ["familles.py", "synapses.json", "verbes.json"]
analyser = F.analyseur("A", FAMILLE, POINT)
corriger = F.correcteur("A", FAMILLE, POINT)
MUTANTS = F.mutants("A", FAMILLE, POINT)
ECRIT = F.zones("A", FAMILLE, POINT)

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))
