#!/usr/bin/env python3
"""Diagnostics de LOT_164. Chaque fenêtre détaille un seul mécanisme."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from moteur import P, page

OUT = Path(__file__).resolve().parents[1]
S = lambda *n: n

SOURCES = """
<li>Organisation mondiale de la Santé, seuils d'hémoglobine, 2024.</li>
<li>Organisation mondiale de la Santé, ferritine, 2020.</li>
<li>Snook et al., Gut, 2021.</li>
<li>Ligne directrice de transfusion, 2015.</li>
<li>Devalia et al., British Journal of Haematology, 2014.</li>
<li>Scully et al., British Journal of Haematology, 2023.</li>
<li>Hill et al., British Journal of Haematology, 2016.</li>
<li>Best Practice, évaluation de l'anémie, preuves relues en 2026.</li>
<li>Doig, Journal of Applied Laboratory Medicine, 2024.</li>
<li>McDonagh et Macdougall, European Journal of Heart Failure, 2018.</li>
<li>Dignass et al., Journal of Crohn's and Colitis, 2015.</li>
<li>Ferinject, numéro 57851.</li>
<li>Maltofer, numéro 30124.</li>
<li>Venofer, numéro 15398.</li>
<li>Tardyferon, numéro 37448.</li>
<li>Ferro-Gradumet, numéro 31644.</li>
<li>Ferrum Hausmann, numéro 35102.</li>
<li>Vitarubine, numéro 21672.</li>
<li>Vitarubine Dépôt, numéro 33584.</li>
<li>Vitarubine Oral, numéro 68216.</li>
<li>Prednisone Streuli, numéro 29349.</li>
<li>Eprex, numéro 49078.</li>
<li>Aranesp, numéro 55725.</li>
<li>Cablivi, numéro 66792.</li>
<li>Hydroxycarbamide Devatis, numéro 67491.</li>
<li>Acidum folicum Hänseler, numéro 55746.</li>
<li>AndreaFol, numéro 54718.</li>
<li>Maltofer Fol, numéro 46538.</li>
<li>Acidum folicum Streuli, numéro 36752.</li>
<li>Catalogue des situations, F2.16, 2026.</li>
<li>Qureshi et al., British Journal of Haematology, 2018.</li>
"""

TITRES = [
    "Définition", "Épidémiologie", "Physiopathologie", "Démarche diagnostique",
    "Anamnèse et drapeaux rouges", "Examen physique", "Approche syndromique",
    "Diagnostic positif", "Examens complémentaires", "Arbre décisionnel",
    "Prise en charge", "Prévention", "Points clés", "Pièges et cas",
]


def ecrire(n, titre, essentiel, fiche, wins):
    assert len(fiche) == 14 and len(wins) == 14
    points = [(TITRES[i], fiche[i], wins[i]) for i in range(14)]
    page(
        chemin=OUT / f"LOT_164_Phase_B_V0_DX.{n}.html",
        titre=titre,
        sous=f"DX.{n} de F2.16. {titre}. Texte du 31 octobre 2026.",
        essentiel=essentiel,
        sommaire_note="Les seuils communs du cours F2.16 ne sont pas recopiés. La fenêtre donne le détail de ce diagnostic.",
        points=points,
        sources_ol=SOURCES,
        fin=f"FIN_FICHIER LOT_164_Phase_B_V0_DX.{n}",
        glossaire="",
    )


def W(*paras):
    return "".join(P(t, src) for t, src in paras)
