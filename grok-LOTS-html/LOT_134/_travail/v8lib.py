#!/usr/bin/env python3
"""Assemblage V8 pour LOT_134. N'écrit que sous grok-LOTS-html/LOT_134/."""
from pathlib import Path

ROOT = Path("/workspace")
MODELE = ROOT / "harnais/modele_lecon/MODELE_DD_V8.html"
LOT = ROOT / "grok-LOTS-html/LOT_134"


def feuille():
    html = MODELE.read_text(encoding="utf-8")
    css = html[html.find("<style>") + 7:html.find("</style>")].strip()
    parts, buf = [], ""
    for chunk in css.split("}"):
        if not chunk.strip():
            continue
        piece = chunk + "}"
        if buf and len(buf) + len(piece) > 1400:
            parts.append(buf)
            buf = piece
        else:
            buf += piece
    if buf:
        parts.append(buf)
    return "\n".join(parts)


def abbr(sigle, definition):
    return f'<abbr title="{definition}">{sigle}</abbr>'


def sup(*nums):
    return "<sup class=\"s\">" + ",".join(str(n) for n in nums) + "</sup>"


def bouton(cible, libelle):
    return f'<button type="button" class="terme" popovertarget="{cible}">{libelle}</button>'


def fenetre(ident, titre, corps, sous=False):
    classe = "fenetre sousf" if sous else "fenetre"
    return (
        f'<div id="{ident}" popover class="{classe}">'
        f'<div class="barre"><span>{titre}</span>'
        f'<button type="button" popovertarget="{ident}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">\n{corps}\n</div></div>'
    )


def ilot(numero, titre, paragraphe, fenetres="", essentiel=False):
    couleur = "c" if (numero or 0) % 2 else "v"
    if essentiel:
        ident, h = "ess", "L'essentiel"
        couleur = "c"
        classe = f"ilot {couleur} essentiel"
    elif numero == 0:
        ident, h = "som", titre
        classe = "ilot v"
    else:
        ident, h = f"p{numero}", f"{numero}. {titre}"
        classe = f"ilot {couleur}"
    return f'<section class="{classe}"><h2 id="{ident}">{h}</h2>\n<p>{paragraphe}</p>\n{fenetres}</section>\n'


def page(titre_doc, h1, sous, blocs, fin):
    css = feuille()
    corps = "\n".join(blocs)
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre_doc}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
<style>
{css}
</style>
</head>
<body>
<main>
<h1 id="titre">{h1}</h1>
<p class="taille" id="taille">Taille : en cours de mesure</p>
<p class="sous">{sous}</p>
{corps}
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- {fin} -->
"""


def ecrire(nom, texte):
    dest = LOT / nom
    dest.write_text(texte, encoding="utf-8")
    return dest
