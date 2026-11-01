#!/usr/bin/env python3
"""Habillage V8 de LOT_145. Le texte vient des modules de leçon, pas d'une boucle d'angles."""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_145"
STYLE = (LOT / "_travail" / "style_v8.css").read_text(encoding="utf-8")
sys.path.insert(0, str(RACINE / "harnais"))
import taille_xy  # noqa: E402

MOT = re.compile(r"[\wÀ-ÿŒœ]+(?:['’\-][\wÀ-ÿŒœ]+)*")
FIN_PHRASE = re.compile(r"(?<=[.!?…])\s+(?=[A-ZÀ-Ý«])")
CLES = re.compile(
    r"\b(incidence|prévalence|prevalence|sensibilit[ée]|spécificit[ée]|specificit|seuil|score)\b",
    re.I,
)
ANNEES_INDEX = {"2002", "2003", "2012", "2020", "2021", "2026"}


def e(s: str) -> str:
    return html.escape(s, quote=True)


def sup(n: int) -> str:
    return f'<sup class="s">{n}</sup>'


def abbr(sigle: str, titre: str) -> str:
    return f'<abbr title="{e(titre)}">{e(sigle)}</abbr>'


def cliche(ancre: str, mot: str) -> str:
    return f'<span class="cliche" data-cliche="{e(ancre)}">{mot}</span>'


def phrases(texte: str) -> list[str]:
    brut = re.sub(r"<[^>]+>", " ", texte)
    brut = html.unescape(brut)
    return [p.strip() for p in FIN_PHRASE.split(brut) if p.strip()]


def nb_mots(phrase: str) -> int:
    return len(MOT.findall(re.sub(r"«[^»]*»", " ", phrase)))


def cle(phrase: str) -> str:
    return re.sub(r"[^a-z0-9àâäçéèêëîïôöùûüœ]+", " ", phrase.lower()).strip()


def controle_texte(fragments: list[str]) -> list[str]:
    erreurs = []
    vus: dict[str, str] = {}
    for frag in fragments:
        if frag.lstrip().startswith("<"):
            continue
        for ph in phrases(frag):
            n = nb_mots(ph)
            if n > 35:
                erreurs.append(f"phrase longue ({n} mots) : {ph[:180]}")
            if ";" in ph:
                erreurs.append(f"point-virgule : {ph[:140]}")
            if n >= 8:
                k = cle(ph)
                if k in vus:
                    erreurs.append(f"phrase double : {ph[:140]}")
                else:
                    vus[k] = ph
        visible = html.unescape(re.sub(r"<[^>]+>", " ", frag))
        if CLES.search(visible) and re.search(r"\d", visible):
            annees = set(re.findall(r"\b(?:19|20)\d{2}\b", visible))
            if not (annees & ANNEES_INDEX) and "<sup" not in frag:
                erreurs.append(f"chiffre-clé sans année ni appel : {visible[:160]}")
        if re.search(r"\b(TODO|FIXME|À vérifier|A vérifier)\b|\(\?\)", visible):
            erreurs.append("marqueur d'incertitude dans le cours")
        if re.search(r", repère \d+\.", visible):
            erreurs.append("gabarit repère encore présent")
    return erreurs


def fenetre(fid: str, titre: str, paragraphes: list[str]) -> str:
    morceaux = []
    for p in paragraphes:
        morceaux.append(p if p.lstrip().startswith("<") else f"<p>{p}</p>")
    corps = "".join(morceaux)
    return (
        f'<div id="{fid}" popover class="fenetre"><div class="barre"><span>{e(titre)}</span>'
        f'<button type="button" popovertarget="{fid}" popovertargetaction="hide" aria-label="Fermer">✕</button>'
        f'</div><div class="corps">{corps}</div></div>'
    )


def bouton(fid: str, mot: str) -> str:
    return f'<button type="button" class="terme" popovertarget="{fid}">{mot}</button>'


def schema(prefix: str, onglets: list[tuple[str, str]]) -> str:
    lettres = "abcd"
    radios, labels, pans = [], [], []
    for i, (lib, inner) in enumerate(onglets):
        let = lettres[i]
        fid = f"{prefix}-{let}"
        chk = " checked" if i == 0 else ""
        radios.append(f'<input type="radio" name="{prefix}" id="{fid}"{chk}>')
        labels.append(f'<label for="{fid}">{e(lib)}</label>')
        pans.append(f'<div class="pan p{let}">{inner}</div>')
    return (
        '<div class="sch">'
        + "".join(radios)
        + '<div class="cmds">'
        + "".join(labels)
        + "</div>"
        + "".join(pans)
        + "</div>"
    )


def svg_boite(titre: str, lignes: list[str], fond: str, trait: str) -> str:
    y = 78
    texts = [f'<text x="210" y="42" text-anchor="middle" font-size="18" font-weight="700">{e(titre)}</text>']
    for i, ligne in enumerate(lignes):
        texts.append(
            f'<text x="210" y="{y + i * 28}" text-anchor="middle" font-size="15">{e(ligne)}</text>'
        )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 220" role="img">'
        f'<rect width="420" height="220" rx="12" fill="{fond}" stroke="{trait}" stroke-width="2"/>'
        + "".join(texts)
        + "</svg>"
    )


def page(lecon: dict) -> str:
    fragments = []
    points_html = []
    for pt in lecon["points"]:
        fiche = pt["fiche"]
        fens = "".join(fenetre(f["id"], f["titre"], f["paragraphes"]) for f in pt["fenetres"])
        fragments.append(fiche)
        for f in pt["fenetres"]:
            fragments.extend(f["paragraphes"])
        points_html.append(
            f'<section class="ilot {pt["classe"]}"><h2 id="{pt["id"]}">{pt["titre"]}</h2>'
            f"<p>{fiche}</p>{fens}</section>"
        )
    if lecon.get("essentiel"):
        fragments.extend(lecon["essentiel"])
    if lecon.get("urgence"):
        fragments.append(lecon["urgence"])
    err = controle_texte(fragments)
    if err:
        raise SystemExit("HABILLAGE REFUSÉ\n" + "\n".join(err[:30]))
    essentiel = "".join(f"<p>{p}</p>" for p in lecon["essentiel"])
    urgence = ""
    if lecon.get("urgence"):
        urgence = f'<div class="urgence"><p>{lecon["urgence"]}</p></div>'
        fragments.append(lecon["urgence"])
    sources = "".join(f"<li>{s}</li>" for s in lecon["sources"])
    som = "".join(f'<li><a href="#{pt["id"]}">{e(pt["sommaire"])}</a></li>' for pt in lecon["points"])
    html_doc = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(lecon["title"])}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
<style>{STYLE}</style>
</head>
<body>
<main>
<h1 id="titre">{e(lecon["h1"])}</h1>
<p class="taille" id="taille">Taille : en attente</p>
<p class="sous">{lecon["sous"]}</p>
<section class="ilot c essentiel" aria-labelledby="ess">
<h2 id="ess">L'essentiel</h2>
{essentiel}
</section>
{urgence}
<nav class="ilot v" aria-labelledby="som">
<h2 id="som">Sommaire</h2>
<ol class="som">
{som}
</ol>
<p class="sous">Les mots soulignés ouvrent une fenêtre. Les sources sont en bas de la leçon.</p>
</nav>
{''.join(points_html)}
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
<section class="ilot c"><h2 id="sources">Sources</h2>
<ol class="sources">
{sources}
</ol>
</section>
</main>
</body>
</html>
<!-- FIN_FICHIER {lecon["fin"]} -->
"""
    m = taille_xy.mesurer(html_doc)
    lib = (
        f"Taille : T = {m.x[1]/1000:.1f} Ko (+ {m.y[1]/1000:.1f} Ko) · "
        f"lecture de la fiche ≈ {max(1, round(m.x[0]/180))} min · {m.fen} fenêtres, {m.dep} dépliants"
    )
    html_doc = html_doc.replace("Taille : en attente", lib, 1)
    return html_doc


def ecrire(lecon: dict) -> Path:
    dest = LOT / lecon["fichier"]
    dest.write_text(page(lecon), encoding="utf-8")
    print(dest.name, "écrit")
    return dest
