#!/usr/bin/env python3
"""Construit un DX V8 à partir de fenêtres déjà rédigées."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from moteur import A, P, S, W, ecrire, page

SIGLES = W("w-sigles", "Sigles de la fiche", "\n".join([
    P(f"{A('alanine aminotransférase','ALAT')}, {A('aspartate aminotransférase','ASAT')}, "
      f"{A('phosphatase alcaline','PAL')}, {A('gamma-glutamyltransférase','GGT')}, "
      f"{A('limite supérieure de la normale','LSN')}, {A('international normalized ratio','INR')}, "
      f"{A('European Association for the Study of the Liver','EASL')}, "
      f"{A('information professionnelle','AIPS')}, {A('model for end-stage liver disease','MELD')}, "
      f"{A('fibrosis-4 index','FIB')}-4, {A('Roussel Uclaf causality assessment method','RUCAM')}, "
      f"{A('virus de l hépatite B','VHB')}, {A('virus de l hépatite C','VHC')}, "
      f"{A('virus de l hépatite A','VHA')}, {A('virus de l hépatite E','VHE')}, "
      f"{A('acide désoxyribonucléique','ADN')}, {A('acide ribonucléique','ARN')}, "
      f"{A('imagerie par résonance magnétique','IRM')}, {A('unité internationale','UI')}, "
      f"{A('cholangite biliaire primitive','CBP')}, {A('insuffisance hépatique aiguë','IHA')}, "
      f"{A('gène HFE de l hémochromatose','HFE')}, {A('high-density lipoprotein','HDL')}, "
      f"{A('low-density lipoprotein','LDL')}, {A('STeroids Or Pentoxifylline for Alcoholic Hepatitis','STOPAH')}, "
      f"{A('protéine C réactive','CRP')}, {A('European Society for Clinical Nutrition and Metabolism','ESPEN')}."),
]))

# Titres imposés par certitude (le mot-clé doit être dans le h2).
TITRES = [
    (1, "c", "Définition"),
    (2, "v", "Épidémiologie"),
    (3, "c", "Physiopathologie"),
    (4, "v", "Démarche diagnostique"),
    (5, "c", "Anamnèse et drapeaux rouges"),
    (6, "v", "Examen physique"),
    (7, "c", "Approche syndromique"),
    (8, "v", "Diagnostic positif"),
    (9, "c", "Examens complémentaires"),
    (10, "v", "Arbre décisionnel"),
    (11, "c", "Prise en charge en Suisse"),
    (12, "v", "Prévention"),
    (13, "c", "Points clés"),
    (14, "v", "Pièges d'examen"),
]


def construire(num, h1, essentiel_html, sous, fiches, fenetres_par_point, sources):
    """fenetres_par_point : dict point -> liste de HTML de fenêtres."""
    sections = []
    for n, cls, titre in TITRES:
        fiche = fiches.get(n) or P("Le détail de ce point est dans les fenêtres.")
        wins = "".join(fenetres_par_point.get(n, []))
        if n == 1:
            wins = SIGLES + wins
        sections.append((cls, titre, fiche, wins))
    nom = f"LOT_159_Phase_B_V0_DX.{num}"
    html = page(nom, h1, sous, essentiel_html, sections, sources)
    return ecrire(nom + ".html", html)
