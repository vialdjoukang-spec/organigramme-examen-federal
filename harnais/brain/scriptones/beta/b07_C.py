#!/usr/bin/env python3
"""β7·C — cohérence chiffrée et unités · point 7 « Approche syndromique »
Généré par harnais/brain/outils/gabarit.py depuis synapses.json et familles.py : NE PAS ÉDITER À LA MAIN (régénérer).
Codes : BC1 point médian décimal · BC2 décimale à point · BC3 chiffre des points clés absent du corps · BC4 unité non SI · BC5 comparateur ASCII · BC6 espace avant %
Entrée : paquet du point 7 (cours HTML) · sortie : contrat brain.scriptone/1 · écrit : P7:typo-chiffres · jumeau : a07_S."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import bus, familles as F

ID, REGION, VERSION, ZONE, POINT, FAMILLE = "b07_C", "BET", F.VERSION, "beta", 7, "C"
DEPEND = ["familles.py", "synapses.json", "verbes.json"]
analyser = F.analyseur("B", FAMILLE, POINT)
corriger = F.correcteur("B", FAMILLE, POINT)
MUTANTS = F.mutants("B", FAMILLE, POINT)
ECRIT = F.zones("B", FAMILLE, POINT)

if __name__ == "__main__":
    sys.exit(bus.cli(sys.modules[__name__]))
