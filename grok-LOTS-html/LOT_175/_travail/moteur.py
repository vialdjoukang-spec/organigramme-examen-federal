#!/usr/bin/env python3
"""Moteur V8 du LOT_175. Phrases courtes, fenêtres popover, aucune balise script."""
from __future__ import annotations

import html
import re
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
STYLE = (RACINE / "harnais/modele_lecon/style_lecon.css").read_text(encoding="utf-8")
DEST = RACINE / "grok-LOTS-html/LOT_175"

# Sigles développés à la première occurrence visible de chaque fichier.
SIGLES: dict[str, tuple[str, str]] = {}


def reset_sigles() -> None:
    SIGLES.clear()


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def sigle(code: str, titre: str, minus: str) -> str:
    if code not in SIGLES:
        SIGLES[code] = (titre, minus)
        return f'<abbr title="{esc(titre)}">{code}</abbr> ({esc(minus)})'
    return f'<abbr title="{esc(titre)}">{code}</abbr>'


def sref(n: int) -> str:
    return f'<sup class="s">{n}</sup>'


def P(texte: str, sources: str) -> str:
    """Paragraphe. `sources` est une liste de numéros, par exemple '1' ou '1,7'."""
    corps = texte.strip()
    if re.search(r"\d", corps):
        corps += sref(sources if isinstance(sources, str) else str(sources))
    return f"<p>{corps}</p>"


def LI(texte: str, sources: str) -> str:
    corps = texte.strip()
    if re.search(r"\d", corps):
        corps += sref(sources)
    return f"<li>{corps}</li>"


def fenetre(fid: str, titre: str, corps: str, sous: bool = False) -> str:
    classe = "fenetre sousf" if sous else "fenetre"
    return (
        f'<div id="{fid}" popover class="{classe}"><div class="barre"><span>{titre}</span>'
        f'<button type="button" popovertarget="{fid}" popovertargetaction="hide" aria-label="Fermer">✕</button>'
        f'</div><div class="corps">{corps}</div></div>'
    )


def bouton(fid: str, mot: str) -> str:
    return f'<button type="button" class="terme" popovertarget="{fid}">{mot}</button>'


def tableau(caption: str, entetes: list[str], lignes: list[list[str]]) -> str:
    th = "".join(f"<th>{e}</th>" for e in entetes)
    body = []
    for ligne in lignes:
        tds = "".join(f"<td>{c}</td>" for c in ligne)
        body.append(f"<tr>{tds}</tr>")
    return (
        f'<div class="tw"><table><caption>{caption}</caption><thead><tr>{th}</tr></thead>'
        f'<tbody>{"".join(body)}</tbody></table></div>'
    )


def mots_de(phrase: str) -> int:
    brut = re.sub(r"<[^>]+>", " ", phrase)
    brut = brut.replace("U.I.", "UI")
    return len(re.findall(r"[A-Za-zÀ-ÿ0-9]+", brut))


def controler_phrases(nom: str, html_texte: str) -> list[str]:
    """Contrôle local avant la porte : longueur, point-virgule, doublon, marqueur."""
    from html.parser import HTMLParser

    class T(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.parts: list[str] = []
            self.skip = 0

        def handle_starttag(self, tag, attrs):
            if tag in ("script", "style"):
                self.skip += 1

        def handle_endtag(self, tag):
            if tag in ("script", "style") and self.skip:
                self.skip -= 1

        def handle_data(self, data):
            if not self.skip:
                self.parts.append(data)

    t = T()
    t.feed(html_texte)
    texte = " ".join(t.parts)
    erreurs = []
    if re.search(r"À\s+vérifier|A\s+vérifier|\bTODO\b|\bFIXME\b|\(\?\)", texte):
        erreurs.append("marqueur d'incertitude")
    if re.search(r"\bi\.\s?v\.|\bi\.\s?m\.|\bs\.\s?c\.|\bp\.\s?ex\.|\bcf\.|\betc\.", texte):
        erreurs.append("abréviation interdite")
    propre = texte.replace("U.I.", "UI")
    phrases = re.split(r"(?<=[.!?])\s+", propre)
    vus = {}
    for ph in phrases:
        ph = ph.strip()
        if "non validé cliniquement" in ph:
            continue
        n = mots_de(ph)
        if ";" in ph:
            erreurs.append("point-virgule: " + ph[:80])
        if n > 35:
            erreurs.append(f"{n} mots: {ph[:140]}")
        if n >= 8:
            if ph in vus:
                erreurs.append("doublon: " + ph[:100])
            vus[ph] = 1
    return erreurs


def page(nom_fichier: str, titre_page: str, h1: str, sous: str, essentiel: str, sections: list[tuple[str, str, str, str]], sources_html: str) -> str:
    """sections: (id, classe c|v, titre h2, html intérieur). Les sigles sont déjà posés."""
    nav = []
    blocs = []
    for i, (ident, classe, titre, corps) in enumerate(sections):
        nav.append(f'<li><a href="#{ident}">{esc(re.sub(r"^\\d+\\.\\s*", "", titre))}</a></li>')
        blocs.append(f'<section class="ilot {classe}"><h2 id="{ident}">{titre}</h2>{corps}</section>')
    # Réinjecter les sigles : le corps a été construit AVANT reset si l'appelant a déjà émis les abbr.
    # L'appelant construit le corps après son propre reset. Ici on ne reset pas une seconde fois
    # si l'appelant a déjà rempli SIGLES. On ne touche pas au corps.
    html_out = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titre_page)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
<style>
{STYLE}
</style>
</head>
<body>
<main>
<h1 id="titre">{h1}</h1>
<p class="taille" id="taille">Taille : en cours de mesure.</p>
<p class="sous">{sous}</p>
<section class="ilot c essentiel" aria-labelledby="ess">
<h2 id="ess">L'essentiel</h2>
{essentiel}
</section>
<nav class="ilot v" aria-labelledby="som">
<h2 id="som">Sommaire</h2>
<ol class="som">
{''.join(nav)}
</ol>
<p class="sous">Les mots ⧉ ouvrent une fenêtre. Les sources sont à la fin.</p>
</nav>
{''.join(blocs)}
<section class="ilot c" aria-labelledby="sources">
<h2 id="sources">Sources</h2>
<ol class="sources">
{sources_html}
</ol>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</section>
</main>
</body>
</html>
<!-- FIN_FICHIER {nom_fichier} -->
"""
    return html_out


SOURCES = """
<li>Organisation mondiale de la santé. Soins pendant le travail pour une expérience positive. Résumé, 2018.</li>
<li>Ayres-de-Campos et collaborateurs. Classification du cardiotocogramme. FIGO, 2015.</li>
<li>National Institute for Health and Care Excellence. Soins postnataux NG194, 2021, mis à jour en 2026.</li>
<li>National Institute for Health and Care Excellence. Santé mentale périnatale CG192, 2014.</li>
<li>SIGN 169. Dépistage dépressif par l'échelle d'Édimbourg, page lue en 2026.</li>
<li>Gynécologie suisse. Avis d'experts 77 sur l'anémie, texte relu en 2026.</li>
<li>Information professionnelle Syntocinon, autorisation 22114, lue le 31 octobre 2026.</li>
<li>Information professionnelle Pabal, autorisation 58079, texte d'octobre 2023.</li>
<li>Information professionnelle Méthergin, autorisation 12730, lue le 31 octobre 2026.</li>
<li>Information professionnelle Rhophylac, autorisation 53609, lue le 31 octobre 2026.</li>
<li>Information professionnelle Konakion MM paediatric, autorisation 48112021, lue le 31 octobre 2026.</li>
<li>Information professionnelle Dafalgan, autorisation 47503, lue le 31 octobre 2026.</li>
<li>Information professionnelle Nalador, autorisation 43642, lue le 31 octobre 2026.</li>
<li>Information professionnelle Cytotec, autorisation 46945, indication des ulcères, lue le 31 octobre 2026.</li>
<li>Information professionnelle Cyklokapron oral, autorisation 33741, lue le 31 octobre 2026.</li>
<li>Apgar, 1953. Issue inférieure à 7 à cinq minutes dans la revue de 2018.</li>
"""


SCHEMA_TRAVAIL = """
<figure class="schema"><svg viewBox="0 0 640 220" role="img" aria-label="Trois temps du travail eutocique">
<rect x="16" y="40" width="180" height="120" rx="10" fill="#d5e8f5" stroke="#176fa0"/>
<rect x="230" y="40" width="180" height="120" rx="10" fill="#b5e1cb" stroke="#1a7a50"/>
<rect x="444" y="40" width="180" height="120" rx="10" fill="#f3cfc3" stroke="#a1262f"/>
<text x="106" y="78" text-anchor="middle" font-size="15" fill="#14303b">Latence</text>
<text x="106" y="104" text-anchor="middle" font-size="13" fill="#14303b">jusqu'à 5 cm</text>
<text x="106" y="128" text-anchor="middle" font-size="12" fill="#14303b">durée non normée</text>
<text x="320" y="78" text-anchor="middle" font-size="15" fill="#14303b">Phase active</text>
<text x="320" y="104" text-anchor="middle" font-size="13" fill="#14303b">de 5 cm à complet</text>
<text x="320" y="128" text-anchor="middle" font-size="12" fill="#14303b">souvent moins de 12 h</text>
<text x="534" y="78" text-anchor="middle" font-size="15" fill="#14303b">Deuxième temps</text>
<text x="534" y="104" text-anchor="middle" font-size="13" fill="#14303b">poussée jusqu'à l'enfant</text>
<text x="534" y="128" text-anchor="middle" font-size="12" fill="#14303b">souvent moins de 3 h</text>
<path d="M196 100 H230" stroke="#14303b" marker-end="url(#fl175)"/>
<path d="M410 100 H444" stroke="#14303b"/>
<defs><marker id="fl175" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#14303b"/></marker></defs>
</svg>
<figcaption>Repères de durée de la recommandation de 2018 pour un premier travail. Le chiffre de un centimètre par heure n'est pas un seuil d'intervention.</figcaption>
</figure>
"""
