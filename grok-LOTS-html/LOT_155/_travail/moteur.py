#!/usr/bin/env python3
"""Assemble une leçon V8 de LOT_155. Les phrases viennent des banques du dossier."""
import html
import re
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
STYLE = (Path(__file__).resolve().parent / "style.css.txt").read_text(encoding="utf-8")
LOT = RACINE / "grok-LOTS-html" / "LOT_155"

SIGLES = {
    "SIADH": "syndrome de sécrétion inappropriée d'hormone antidiurétique",
    "SIAD": "syndrome d'antidiurèse inappropriée",
    "PROFILES": "référentiel suisse des objectifs de formation",
    "UKKA": "association britannique de néphrologie",
    "AIPS": "information professionnelle suisse",
    "SRAA": "système rénine-angiotensine-aldostérone",
    "FGF23": "facteur de croissance des fibroblastes 23",
    "ECG": "électrocardiogramme",
    "SSP": "situation de départ",
    "PTH": "hormone parathyroïdienne",
    "ERC": "Conseil européen de réanimation",
    "IPP": "inhibiteur de la pompe à protons",
    "QT": "intervalle QT de l'électrocardiogramme",
    "DFG": "débit de filtration glomérulaire",
}

MOTS = re.compile(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*")


def mots(phrase: str) -> int:
    return len(MOTS.findall(re.sub(r"«[^»]*»", " ", phrase)))


def wrap_sigles(texte: str) -> str:
    for sigle in sorted(SIGLES, key=len, reverse=True):
        titre = html.escape(SIGLES[sigle], quote=True)
        texte = re.sub(
            rf"\b{sigle}\b",
            f'<abbr title="{titre}">{sigle}</abbr>',
            texte,
        )
    return texte


def inline(texte: str) -> str:
    texte = html.escape(texte, quote=False)
    texte = re.sub(r"\{(\d+)\}", r'<sup class="s">\1</sup>', texte)
    texte = re.sub(
        r"\[\[([^\]|]+)\|([^\]]+)\]\]",
        lambda m: (
            f'<button type="button" class="terme" popovertarget="{m.group(1)}">'
            f"{html.escape(m.group(2))}</button>"
        ),
        texte,
    )
    return wrap_sigles(texte)


def P(texte: str) -> str:
    return f"<p>{inline(texte)}</p>\n"


def fenetre(ident: str, titre: str, phrases: list[str]) -> str:
    corps = "".join(P(x) for x in phrases)
    return (
        f'<div id="{ident}" popover class="fenetre"><div class="barre">'
        f"<span>{html.escape(titre)}</span>"
        f'<button type="button" popovertarget="{ident}" popovertargetaction="hide" '
        f'aria-label="Fermer">✕</button></div><div class="corps">\n{corps}</div></div>'
    )


def verifier_phrases(nom: str, phrases: list[str]) -> None:
    vus = {}
    erreurs = []
    for ph in phrases:
        n = mots(ph)
        if n > 34:
            erreurs.append(f"{nom} : {n} mots : {ph}")
        if ";" in ph:
            erreurs.append(f"{nom} : point-virgule : {ph}")
        if re.search(r"À\s+vérifier|A\s+vérifier|TODO|FIXME|\(\?\)", ph):
            erreurs.append(f"{nom} : marqueur : {ph}")
        cle = re.sub(r"\s+", " ", ph.strip().lower())
        if n >= 8 and cle in vus:
            erreurs.append(f"{nom} : phrase double : {ph}")
        vus[cle] = True
    if erreurs:
        raise SystemExit("\n".join(erreurs[:30]))


def page(meta: dict) -> str:
    toutes = []
    toutes.extend(meta["essentiel"])
    toutes.extend(meta["glossaire"])
    for point in meta["points"]:
        toutes.extend(point["fiche"])
        toutes.extend(point["fenetre"])
        for sous in point.get("sous", []):
            toutes.extend(sous["phrases"])
    toutes.extend(meta.get("extra", []))
    verifier_phrases(meta["fichier"], toutes)

    gloss = fenetre("w-glossaire", "Sigles de la leçon", meta["glossaire"])
    blocs = []
    for i, point in enumerate(meta["points"], start=1):
        couleur = "c" if i % 2 else "v"
        corps = "".join(P(x) for x in point["fiche"])
        if point.get("fenetre"):
            corps += fenetre(f"a-p{i}", point["titre"], point["fenetre"])
        for sous in point.get("sous", []):
            corps += fenetre(sous["id"], sous["titre"], sous["phrases"])
        blocs.append(
            f'<section class="ilot {couleur}"><h2 id="p{i}">{html.escape(point["titre"])}</h2>\n{corps}</section>'
        )
    som = "\n".join(
        f'<li><a href="#p{i}">{html.escape(point["titre"])}</a></li>'
        for i, point in enumerate(meta["points"], start=1)
    )
    sources = "\n".join(f"<li>{html.escape(s)}</li>" for s in meta["sources"])
    ess = "".join(P(x) for x in meta["essentiel"])
    h1 = html.escape(meta["h1"])
    sous = P(meta["sous"])
    dx = f"<h2>{html.escape(meta['h2'])}</h2>\n" if meta.get("h2") else ""
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{h1}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
<style>{STYLE}</style>
</head>
<body>
<main>
<h1 id="titre">{h1}</h1>
<p class="taille" id="taille">Taille : en attente de mesure</p>
{sous}{dx}<section class="ilot c essentiel"><h2 id="ess">L'essentiel</h2>
{ess}{gloss}
</section>
<nav class="ilot v" aria-labelledby="som">
<h2 id="som">Sommaire</h2>
<ol class="som">
{som}
</ol>
<p class="sous">Les mots soulignés ouvrent une fenêtre. Les sources sont à la fin.</p>
</nav>
{''.join(blocs)}
<section class="ilot c"><h2 id="sources">Sources</h2>
<ol class="sources">
{sources}
</ol>
</section>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- FIN_FICHIER {meta["fin"]} -->
"""


def ecrire(meta: dict) -> Path:
    dest = LOT / meta["fichier"]
    dest.write_text(page(meta), encoding="utf-8")
    return dest
