#!/usr/bin/env python3
"""Assemble une leçon V8. Le style vient du modèle validé, non modifié."""
from pathlib import Path
import re

RACINE = Path(__file__).resolve().parents[3]
MODELE = (RACINE / "harnais/modele_lecon/MODELE_DD_V8.html").read_text(encoding="utf-8")
STYLE = re.search(r"<style>.*?</style>", MODELE, re.S).group(0)
FONT = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">'
)

POINTS = [
    (1, "p1", "1. Définition"),
    (2, "p2", "2. Épidémiologie"),
    (3, "p3", "3. Physiopathologie"),
    (4, "p4", "4. Démarche diagnostique"),
    (5, "p5", "5. Anamnèse et drapeaux rouges"),
    (6, "p6", "6. Examen physique"),
    (7, "p7", "7. Approche syndromique"),
    (8, "p8", "8. Diagnostic positif"),
    (9, "p9", "9. Examens complémentaires"),
    (10, "p10", "10. Arbre décisionnel"),
    (11, "p11", "11. Prise en charge"),
    (12, "p12", "12. Prévention"),
    (13, "p13", "13. Points clés"),
    (14, "p14", "14. Pièges et cas"),
]


def fen(wid, titre, corps, sous=False):
    cls = "fenetre sousf" if sous else "fenetre"
    return (
        f'<div id="{wid}" popover class="{cls}"><div class="barre"><span>{titre}</span>'
        f'<button type="button" popovertarget="{wid}" popovertargetaction="hide" aria-label="Fermer">✕</button>'
        f'</div><div class="corps">{corps}</div></div>'
    )


def btn(wid, mot):
    return f'<button type="button" class="terme" popovertarget="{wid}">{mot}</button>'


def table(caption, headers, rows):
    th = "".join(f"<th>{h}</th>" for h in headers)
    body = []
    for r in rows:
        tds = "".join(f"<td>{c}</td>" for c in r)
        body.append(f"<tr>{tds}</tr>")
    return (
        f'<div class="tw"><table><caption>{caption}</caption><thead><tr>{th}</tr></thead>'
        f'<tbody>{"".join(body)}</tbody></table></div>'
    )


def page(nom_fichier, h1, sous, essentiel, sommaire_note, ilots, sources_html):
    nav = []
    for _n, ident, titre in POINTS:
        nav.append(f'<li><a href="#{ident}">{titre.split(". ", 1)[1]}</a></li>')
    sections = []
    colors = ["c", "v"]
    for i, (_n, ident, titre) in enumerate(POINTS):
        ile, fens = ilots[ident]
        col = colors[i % 2]
        sections.append(
            f'<section class="ilot {col}"><h2 id="{ident}">{titre}</h2>{ile}{"".join(fens)}</section>'
        )
    html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{h1}</title>
{FONT}
{STYLE}
</head>
<body>
<main>
<h1 id="titre">{h1}</h1>
<p class="taille" id="taille">Taille : en attente de mesure.</p>
<p class="sous">{sous}</p>
<section class="ilot c essentiel" aria-labelledby="ess">
<h2 id="ess">L'essentiel</h2>
{essentiel}
</section>
<nav class="ilot v" aria-labelledby="som">
<h2 id="som">Sommaire</h2>
<ol class="som">
{"".join(nav)}
</ol>
<p class="sous">{sommaire_note}</p>
</nav>
{"".join(sections)}
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
<section class="ilot c"><h2 id="sources">Sources</h2>
{sources_html}
</section>
</main>
</body>
</html>
<!-- FIN_FICHIER {nom_fichier} -->
"""
    return html


SIGLES = (
    '<p>Sigles de la leçon : <abbr title="thyréostimuline">TSH</abbr>, '
    '<abbr title="triiodothyronine">T3</abbr>, '
    '<abbr title="American Thyroid Association">ATA</abbr>, '
    '<abbr title="European Thyroid Association">ETA</abbr>, '
    '<abbr title="Japan Thyroid Association">JTA</abbr>, '
    '<abbr title="American College of Radiology">ACR</abbr>, '
    '<abbr title="Thyroid Imaging">TI</abbr>, '
    '<abbr title="Reporting and Data System">RADS</abbr>, '
    '<abbr title="information professionnelle suisse">AIPS</abbr>, '
    '<abbr title="Centre hospitalier universitaire vaudois">CHUV</abbr>, '
    '<abbr title="anticorps anti-récepteur de la TSH">TRAb</abbr>, '
    '<abbr title="thyroperoxydase">TPO</abbr>, '
    '<abbr title="Burch-Wartofsky Point Scale">BWPS</abbr>, '
    '<abbr title="thyrotoxicose induite par l\'amiodarone">AIT</abbr>, '
    '<abbr title="hypothyroïdie induite par l\'amiodarone">AIH</abbr>, '
    '<abbr title="crise thyréotoxique certaine, critère japonais">TS1</abbr>, '
    '<abbr title="crise thyréotoxique suspectée, critère japonais">TS2</abbr>, '
    '<abbr title="intraveineuse">IV</abbr>, '
    '<abbr title="électrocardiogramme">ECG</abbr>, '
    '<abbr title="imagerie par résonance magnétique">IRM</abbr>, '
    '<abbr title="anticorps anti-cytoplasme des polynucléaires neutrophiles">ANCA</abbr>, '
    '<abbr title="National Health and Nutrition Examination Survey">NHANES</abbr>, '
    '<abbr title="échelle de coma de Glasgow">GCS</abbr>, '
    '<abbr title="New York Heart Association">NYHA</abbr>, '
    '<abbr title="Principal Relevant Objectives and Framework for Integrated Learning and Education in Switzerland">PROFILES</abbr>, '
    '<abbr title="catégorie 1, bénigne, du système échographique">TR1</abbr>, '
    '<abbr title="catégorie 2, non suspecte">TR2</abbr>, '
    '<abbr title="catégorie 3, peu suspecte">TR3</abbr>, '
    '<abbr title="catégorie 4, moyennement suspecte">TR4</abbr>, '
    '<abbr title="catégorie 5, très suspecte">TR5</abbr>, '
    '<abbr title="deuxième partie du nom commercial de l\'hydrocortisone injectable">CORTEF</abbr>, '
    '<abbr title="forme d\'Eltroxine mentionnée dans l\'information professionnelle">LF</abbr>.'
    '</p>'
)
