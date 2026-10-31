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
    body = "\n".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return (
        f'<div class="tw"><table><caption>{caption}</caption><thead>\n<tr>{th}</tr></thead>\n'
        f"<tbody>\n{body}\n</tbody></table></div>"
    )


def p(texte, ref=None):
    sup = f'<sup class="s">{ref}</sup>' if ref else ""
    return f"<p>{texte}{sup}</p>"


def page(nom_fichier, h1, sous, essentiel, ilots, sources_html, h2_dx=None):
    nav = "".join(f'<li><a href="#{ident}">{titre.split(". ", 1)[1]}</a></li>' for _n, ident, titre in POINTS)
    sections = []
    for i, (_n, ident, titre) in enumerate(POINTS):
        ile, fens = ilots[ident]
        col = "c" if i % 2 == 0 else "v"
        sections.append(
            f'<section class="ilot {col}"><h2 id="{ident}">{titre}</h2>{ile}{"".join(fens)}</section>'
        )
    extra = f"<h2>{h2_dx}</h2>\n" if h2_dx else ""
    return f"""<!doctype html>
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
{extra}<section class="ilot c essentiel" aria-labelledby="ess">
<h2 id="ess">L'essentiel</h2>
{essentiel}
</section>
<nav class="ilot v" aria-labelledby="som">
<h2 id="som">Sommaire</h2>
<ol class="som">
{nav}
</ol>
<p class="sous">Les mots ⧉ ouvrent une fenêtre. Les sources sont à la fin.</p>
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
