#!/usr/bin/env python3
"""Construit un DX V8 à partir d'îlots (texte court) et de fenêtres (texte long)."""
from pathlib import Path
from moteur import page, SIGLES, btn

def ecrire(numero, h1, sous_extra, essentiel, ilots, sources_html=None):
    nom = f"LOT_162_Phase_B_V0_DX.{numero}"
    ilots = dict(ilots)
    ile, fens = ilots["p1"]
    if "Sigles de la leçon" not in ile:
        ilots["p1"] = (ile + SIGLES, fens)
    html = page(
        nom,
        h1,
        f"DX.{numero} de F2.14. {sous_extra} Texte du 31 octobre 2026.",
        essentiel,
        "Les mots soulignés ouvrent une fenêtre. Les sources sont en bas de la leçon.",
        ilots,
        sources_html or SOURCES,
    )
    dest = Path(__file__).resolve().parents[1] / f"{nom}.html"
    dest.write_text(html, encoding="utf-8")
    return dest

SOURCES = """
<ol class="sources">
<li>Wuerzner et al., Revue Médicale Suisse, 2010.</li>
<li>Ross et al., Thyroid, 2016.</li>
<li>Jonklaas et al., Thyroid, 2014.</li>
<li>Bartalena et al., European Thyroid Journal, 2018.</li>
<li>Satoh et al., Endocrine Journal, 2016.</li>
<li>Tessler et al., Journal of the American College of Radiology, 2017.</li>
<li>Medical Journal of Australia, 2016, biotine.</li>
<li>Néo-Mercazole, numéro 21037.</li>
<li>Euthyrox, numéro 54949.</li>
<li>Propranolol Zentiva, numéro 47025.</li>
<li>Solu-CORTEF, numéro 23533.</li>
<li>Iodure de potassium axapharm, numéro 67017.</li>
<li>Prednisone Streuli, numéro 29349.</li>
<li>Cordarone comprimés, numéro 33393.</li>
<li>Eltroxine-LF, numéro 29812.</li>
<li>Hydrocortisone Galepharm, numéro 57970.</li>
<li>Catalogue PROFILES, F2.14, 2026 pour la lecture du catalogue.</li>
</ol>
"""
