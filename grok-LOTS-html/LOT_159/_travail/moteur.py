#!/usr/bin/env python3
"""Assembleur V8 du LOT_159. Le texte médical est dans les modules voisins."""
from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MODELE = ROOT / "harnais/modele_lecon/MODELE_DD_V8.html"
LOT = ROOT / "grok-LOTS-html/LOT_159"


def css() -> str:
    brut = MODELE.read_text(encoding="utf-8")
    m = re.search(r"<style>.*?</style>", brut, re.S)
    if not m:
        raise SystemExit("style du modèle V8 introuvable")
    return m.group(0)


def A(titre: str, texte: str) -> str:
    return f'<abbr title="{html.escape(titre, quote=True)}">{texte}</abbr>'


def S(*nums: int) -> str:
    return '<sup class="s">' + ",".join(str(n) for n in nums) + "</sup>"


def P(texte: str, *nums: int) -> str:
    return f"<p>{texte}{S(*nums) if nums else ''}</p>"


def B(cible: str, mot: str) -> str:
    return f'<button type="button" class="terme" popovertarget="{cible}">{mot}</button>'


def W(ident: str, titre: str, corps: str, sous: bool = False) -> str:
    cls = "fenetre sousf" if sous else "fenetre"
    return (
        f'<div id="{ident}" popover class="{cls}">'
        f'<div class="barre"><span>{titre}</span>'
        f'<button type="button" popovertarget="{ident}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">\n{corps}\n</div></div>'
    )


def table(legende: str, entetes: list[str], lignes: list[list[str]]) -> str:
    head = "".join(f"<th>{h}</th>" for h in entetes)
    body = []
    for ligne in lignes:
        cells = "".join(f"<td>{c}</td>" for c in ligne)
        body.append(f"<tr>{cells}</tr>")
    return (
        f'<div class="tw"><table><caption>{legende}</caption><thead><tr>{head}</tr></thead>'
        f"<tbody>\n" + "\n".join(body) + "\n</tbody></table></div>"
    )


def page(nom: str, h1: str, sous: str, essentiel: str, sections: list[tuple], sources: list[str]) -> str:
    """sections : (id, classe c|v, titre h2, fiche html, fenetres html)."""
    nav = ['<ol class="som">']
    for i, (_c, titre, _f, _w) in enumerate(sections, start=1):
        nav.append(f'<li><a href="#p{i}">{titre}</a></li>')
    nav.append("</ol>")
    nav.append('<p class="sous">Les mots ⧉ ouvrent une fenêtre. Les <a href="#sources">sources</a> sont à la fin.</p>')
    blocs = []
    for i, (cls, titre, fiche, wins) in enumerate(sections, start=1):
        blocs.append(f'<section class="ilot {cls}"><h2 id="p{i}">{i}. {titre}</h2>\n{fiche}\n{wins}\n</section>')
    lis = "\n".join(f"<li>{s}</li>" for s in sources)
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(h1)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
{css()}
</head>
<body>
<main>
<h1 id="titre">{h1}</h1>
<p class="taille" id="taille">Taille inscrite après mesure.</p>
<p class="sous">{sous}</p>
<section class="ilot c essentiel" aria-labelledby="ess">
<h2 id="ess">L'essentiel</h2>
{essentiel}
</section>
<nav class="ilot v" aria-labelledby="som">
<h2 id="som">Sommaire</h2>
{''.join(nav)}
</nav>
{''.join(blocs)}
<section class="ilot c">
<h2 id="sources">Sources</h2>
<ol class="sources">
{lis}
</ol>
</section>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- FIN_FICHIER {nom} -->
"""


def ecrire(nom: str, contenu: str) -> Path:
    dest = LOT / nom
    dest.write_text(contenu, encoding="utf-8")
    return dest
