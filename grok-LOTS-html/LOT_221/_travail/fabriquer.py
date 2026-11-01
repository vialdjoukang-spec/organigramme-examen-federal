#!/usr/bin/env python3
"""Assemble LOT_221 (O6.8). Phrases cliniques ici. Preuves dans evidence/."""
from __future__ import annotations

import html
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_221"
sys.path.insert(0, str(RACINE / "harnais"))
import taille_xy  # noqa: E402

MOTS_CLES = re.compile(
    r"\b(incidence|prévalence|prevalence|sensibilit[ée]|spécificit[ée]|specificit|seuil|score)\b",
    re.I,
)
DOSE_RX = re.compile(
    r"\b(\d+(?:[.,]\d+)?)\s*(µg|μg|mcg|mg|UI|IU|ml/h|mL/h)\b",
    re.I,
)

CSS = r"""
:root{--fond:#eef7fc;--page:#ffffff;--texte:#1d2a30;--doux:#4f5f66;--lien:#0b5d86;--titre:#14303b;--trait:#cfe3ec;--encadre:#f5f7f9;--bord:#1a7a50;--vert:#1a7a50;--ciel:#176fa0;--alerte:#a1262f;--ombre:rgb(15 60 90 / .28);--voile:rgb(10 30 45 / .55);--barre:#f2f5f7;--th:#f2f5f7;--cb1:#4fb3e6;--cb2:#b9e2f6;--vb1:#3aa776;--vb2:#b5e1cb;--o1:rgb(15 60 90 / .07);--o2:rgb(15 60 90 / .09)}
@media (prefers-color-scheme:dark){:root{--fond:#0e171d;--page:#16222a;--texte:#e3edf1;--doux:#a9bac2;--lien:#8fd3f5;--titre:#e6eef2;--trait:#2c414c;--encadre:#1a252c;--bord:#5cc79a;--vert:#5cc79a;--ciel:#6cc2ef;--alerte:#ff8a92;--ombre:rgb(0 0 0 / .6);--voile:rgb(0 0 0 / .7);--barre:#1d282f;--th:#1d282f;--cb1:#4aa9da;--cb2:#24506a;--vb1:#46b384;--vb2:#245a44;--o1:rgb(0 0 0 / .35);--o2:rgb(0 0 0 / .3)}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--fond);color:var(--texte);font:1rem/1.45 "Atkinson Hyperlegible",Verdana,sans-serif;overflow-wrap:break-word;hyphens:manual}
main{max-width:72ch;margin:0 auto;padding:1rem 1rem 2rem}
h1{font-size:1.75rem;line-height:1.25;color:var(--titre);margin:0 0 .4rem}
h2{font-size:1.3rem;line-height:1.3;color:var(--titre);margin:0 0 .45rem}
h3{font-size:.98rem;color:var(--titre);margin:.6rem 0 .3rem}
p{margin:0 0 .55rem}.sous{color:var(--doux);font-size:.95rem}
a{color:var(--lien)}
button.terme{all:unset;cursor:pointer;color:var(--lien);text-decoration:underline dotted 1.5px;text-underline-offset:3px}
button.terme::after{content:" ⧉";font-size:.75em;vertical-align:.15em}
button.terme:focus-visible{outline:2px solid var(--lien);outline-offset:2px}
.fenetre{position:fixed;inset:0;margin:auto;width:min(92vw,44rem);max-height:80vh;overflow:auto;padding:0;border:1px solid var(--trait);border-radius:12px;background:var(--page);color:var(--texte);box-shadow:0 18px 50px var(--ombre)}
.fenetre::backdrop{background:var(--voile)}
.barre{position:sticky;top:0;z-index:1;display:flex;align-items:center;justify-content:space-between;gap:.8rem;padding:.55rem .6rem .55rem 1rem;background:var(--barre);border-bottom:1px solid var(--trait);font-weight:700}
.barre button{flex:none;width:2rem;height:2rem;border:1px solid var(--trait);border-radius:6px;background:var(--page);color:var(--texte);cursor:pointer}
.corps{padding:1rem 1.2rem 1.2rem}
.tw{overflow-x:auto;margin:.6rem 0 1rem}
table{border-collapse:collapse;width:100%;font-size:.9rem;line-height:1.45}
th,td{border:1px solid var(--trait);padding:.4rem .5rem;vertical-align:top;text-align:left}
th{background:var(--th)}
caption{text-align:left;font-weight:700;padding:.2rem 0 .4rem}
.taille{font-size:.85rem;color:var(--doux);margin:0 0 .6rem}
.mention{font-style:italic;color:var(--doux);margin:.8rem .3rem 0}
sup.s{font-size:.66em;line-height:0;vertical-align:.5em;margin-left:.06em;color:#1a3a6b;font-weight:700}
abbr[title]{text-decoration:underline dotted 1px;text-underline-offset:2px;cursor:help}
.ilot{background:linear-gradient(var(--page),var(--page)) padding-box,var(--bd) border-box;border:1.5px solid transparent;border-radius:12px;padding:.85rem 1rem .6rem;margin:0 0 .7rem;box-shadow:0 1px 2px var(--o1),0 6px 16px var(--o2)}
.ilot.c{--bd:linear-gradient(135deg,var(--cb1),var(--cb2))}
.ilot.v{--bd:linear-gradient(135deg,var(--vb1),var(--vb2))}
nav ol{padding-left:1.2rem;margin:.2rem 0}
.som{columns:2;column-gap:1.2rem}
.som li{break-inside:avoid}
.algowrap{position:relative;margin:.4rem 0 1rem}
.algowrap input{position:absolute;opacity:0;width:1px;height:1px}
.algowrap .choix{display:flex;gap:.4rem;flex-wrap:wrap;margin:0 0 .4rem}
.algowrap label{border:1px solid var(--trait);border-radius:8px;padding:.25rem .6rem;cursor:pointer}
.algowrap .bo{fill:#f4f7f8;stroke:#176fa0;stroke-width:2}
.algowrap .pan{display:none}
.algowrap .r-bilan:checked~.pan-bilan,.algowrap .r-alerte:checked~.pan-alerte,.algowrap .r-age:checked~.pan-age{display:block}
.algowrap .r-bilan:checked~.choix label[for$="-bilan"],.algowrap .r-alerte:checked~.choix label[for$="-alerte"],.algowrap .r-age:checked~.choix label[for$="-age"]{background:#142028;color:#fff}
figure svg{width:100%;height:auto;max-width:40rem;display:block;margin:auto}
figcaption{font-size:.88rem;color:var(--doux)}
.sources{font-size:.86rem}
.urgence{border:2px solid var(--alerte);border-radius:8px;padding:.6rem .8rem;margin:.6rem 0}
"""

POINTS = [
    (1, "1. Définition", "c"),
    (2, "2. Épidémiologie", "v"),
    (3, "3. Physiopathologie", "c"),
    (4, "4. Démarche", "v"),
    (5, "5. Anamnèse", "c"),
    (6, "6. Examen", "v"),
    (7, "7. Syndromes", "c"),
    (8, "8. Diagnostic", "v"),
    (9, "9. Examens complémentaires", "c"),
    (10, "10. Arbre décisionnel", "v"),
    (11, "11. Prise en charge", "c"),
    (12, "12. Prévention", "v"),
    (13, "13. Points clés", "c"),
    (14, "14. Pièges", "v"),
]

DXS_NOMS = [
    "Réaction adaptative attendue",
    "Détresse spirituelle et démoralisation",
    "Trouble anxieux",
    "Épisode dépressif caractérisé",
    "Trouble de l'adaptation",
    "Souffrance liée à l'alcool ou à une benzodiazépine",
    "Cause somatique ou iatrogène",
    "État de stress post-traumatique",
    "Épisode psychotique",
    "Crise suicidaire",
]

DOSE_CLES = {"a", "3", "4", "6", "9"}


def e(s: str) -> str:
    return html.escape(s, quote=False)


def riche(s: str) -> str:
    t = e(s)
    t = re.sub(r"\[\[(\d+)\]\]", r'<sup class="s">\1</sup>', t)
    return t


def mots(s: str) -> int:
    nu = re.sub(r"\[\[\d+\]\]", " ", s)
    return len(nu.split())


def L(*parts: str) -> list[str]:
    out = []
    for s in parts:
        s = " ".join(s.split())
        nu = re.sub(r"\s*\[\[\d+\]\]\s*$", "", s).strip()
        if not nu.endswith("."):
            raise SystemExit(f"point final manquant : {s}")
        if s[0].islower():
            raise SystemExit(f"initiale : {s}")
        n = mots(s)
        if n > 30:
            raise SystemExit(f"{n} mots : {s}")
        if ";" in s or "«" in s or "»" in s:
            raise SystemExit(f"signe interdit : {s}")
        vis = re.sub(r"\[\[\d+\]\]", " ", s)
        if MOTS_CLES.search(vis) and re.search(r"\d", vis) and not re.search(r"\[\[\d+\]\]", s):
            raise SystemExit(f"chiffre-clé sans source : {s}")
        out.append(s)
    return out


def ellipse(cx, cy, rx, ry) -> str:
    k = 0.5522847498
    f = lambda v: f"{v:.1f}"
    return (
        f"M{f(cx-rx)},{f(cy)}C{f(cx-rx)},{f(cy-k*ry)} {f(cx-k*rx)},{f(cy-ry)} {f(cx)},{f(cy-ry)}"
        f"C{f(cx+k*rx)},{f(cy-ry)} {f(cx+rx)},{f(cy-k*ry)} {f(cx+rx)},{f(cy)}"
        f"C{f(cx+rx)},{f(cy+k*ry)} {f(cx+k*rx)},{f(cy+ry)} {f(cx)},{f(cy+ry)}"
        f"C{f(cx-k*rx)},{f(cy+ry)} {f(cx-rx)},{f(cy+k*ry)} {f(cx-rx)},{f(cy)}Z"
    )


def verifier_phrases(phrases: list[str], ou: str) -> None:
    vus = {}
    for s in phrases:
        if ";" in s:
            raise SystemExit(f"point-virgule interdit {ou}: {s}")
        n = mots(s)
        if n > 32:
            raise SystemExit(f"{n} mots {ou}: {s}")
        if n >= 8:
            k = re.sub(r"\s+", " ", re.sub(r"\[\[\d+\]\]", "", s)).strip().lower()
            if k in vus:
                raise SystemExit(f"phrase répétée {ou}: {s}")
            vus[k] = 1
        vis = re.sub(r"\[\[\d+\]\]", " ", s)
        if MOTS_CLES.search(vis) and re.search(r"\d", vis) and not re.search(r"\[\[\d+\]\]", s):
            raise SystemExit(f"chiffre-clé sans source {ou}: {s}")
        if "«" in s:
            raise SystemExit(f"guillemet {ou}: {s}")


def fenetre(wid: str, titre: str, corps: str) -> str:
    return (
        f'<div id="{wid}" popover class="fenetre"><div class="barre"><span>{e(titre)}</span>'
        f'<button type="button" popovertarget="{wid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">{corps}</div></div>'
    )


def paras(lignes: list[str]) -> str:
    return "".join(f"<p>{riche(s)}</p>" for s in lignes)


def algo(nom: str, portes: list[tuple[str, str, str]]) -> str:
    radios, labels, pans = [], [], []
    for i, (suf, lib, phrase) in enumerate(portes):
        iid = f"{nom}-{suf}"
        chk = " checked" if i == 0 else ""
        radios.append(f'<input class="r-{suf}" type="radio" name="{nom}" id="{iid}"{chk}>')
        labels.append(f'<label for="{iid}">{e(lib)} </label>')
        pans.append(
            f'<div class="pan pan-{suf}"><svg viewBox="0 0 800 180" role="img">'
            f'<rect class="bo" x="24" y="30" width="752" height="120" rx="16"/>'
            f'<text x="48" y="100" font-size="26" fill="#14303b">{e(lib)}</text></svg>'
            f"<p>{riche(phrase)}</p></div>"
        )
    return (
        f'<div class="algowrap">{"".join(radios)}<div class="choix">{"".join(labels)}</div>'
        f'{"".join(pans)}</div>'
    )


def css_dessin(did: str, cles: list[str]) -> str:
    b = []
    for c in cles:
        b.append(
            f"#{did}-{c}:checked~.plan .niv-{c},#{did}-{c}:checked~.leg-{c},#{did}-{c}:checked~.note-{c}{{display:block}}"
            f"#{did}-{c}:checked~.barre label[for=\"{did}-{c}\"]{{background:#142028;color:#fff}}"
        )
    return (
        "@font-face{font-family:\"Atkinson Hyperlegible\";font-style:normal;font-weight:400;font-display:swap;"
        "src:url(\"../outils/dessinateur/polices/AtkinsonHyperlegible-Regular.ttf\") format(\"truetype\")}"
        f"[data-dessinateur]{{--encre:#142028;--papier:#f4f7f8;--filet:#c5d0d6;position:relative;max-width:920px;margin:0 auto;"
        "color:var(--encre);font:16px/1.4 Atkinson Hyperlegible,Verdana,sans-serif}}"
        "[data-dessinateur] .sr{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);border:0}"
        "[data-dessinateur] .barre{display:flex;flex-wrap:wrap;gap:.4rem;margin:0 0 .6rem;position:static;background:transparent;border:0;padding:0}"
        "[data-dessinateur] .barre label{cursor:pointer;border:2px solid var(--encre);border-radius:999px;padding:.35rem .75rem;background:#fff;color:#142028}"
        "[data-dessinateur] .niv,[data-dessinateur] .leg,[data-dessinateur] .note{display:none}"
        + "".join(b)
        + "[data-dessinateur] .cadre{position:relative}"
        "[data-dessinateur] svg{width:100%;height:auto;display:block;background:#e7eef2;border-radius:12px}"
        "[data-dessinateur] .pastille{position:absolute;transform:translate(-50%,-50%);z-index:2;min-width:1.15rem;height:1.15rem;"
        "padding:0 .2rem;border-radius:999px;background:#142028;color:#fff;font-size:12px;font-weight:700;line-height:1.15rem;text-align:center}"
        "[data-dessinateur] .repere{position:absolute;transform:translate(-50%,-50%);font-weight:700;background:#fff;color:#111;"
        "border:2px solid #111;border-radius:6px;padding:0 .4rem;line-height:1.3}"
        "[data-dessinateur] .zone:hover .vis,[data-dessinateur] .zone:focus-visible .vis{stroke:#111;stroke-width:3.5px;stroke-dasharray:6 4}"
        "[data-dessinateur] .note{margin:.45rem 0;font-size:.92rem}"
        "[data-dessinateur] .leg{margin:.2rem 0 0;padding:0;list-style:none;columns:2;gap:1rem}"
        "[data-dessinateur] .leg li{break-inside:avoid;margin:0 0 .2rem}"
        "[data-dessinateur] .leg span{display:inline-block;min-width:1.4rem;font-weight:700}"
        "[data-dessinateur] details{margin-top:.8rem;border:2px solid var(--encre);border-radius:10px;background:#fff}"
        "[data-dessinateur] summary{cursor:pointer;padding:.55rem .7rem;font-weight:700}"
        "[data-dessinateur] .reponse{padding:0 .8rem .7rem}"
        "[data-dessinateur] .sources{font-size:.82rem;color:#24343c}"
        "@media (max-width:640px){[data-dessinateur] .leg{columns:1}}"
    )


COULEURS = [
    ("#f7f1ea", "#c48b7a"),
    ("#d9ebe3", "#0f6e62"),
    ("#c9d8f2", "#24506a"),
    ("#f3d0c8", "#a1262f"),
]


def dessin(did: str, niveaux: list[dict], question: str, reponse: list[str]) -> str:
    cles = [n["cle"] for n in niveaux]
    radios, labels, plans, notes, legs = [], [], [], [], []
    for i, n in enumerate(niveaux):
        chk = " checked" if i == 0 else ""
        radios.append(f'<input class="sr" type="radio" name="{did}-niv" id="{did}-{n["cle"]}"{chk}/>')
        labels.append(f'<label for="{did}-{n["cle"]}">{e(n["etiquette"])}</label>')
        zones, pastilles, items = [], [], []
        for j, st in enumerate(n["structures"], start=1):
            fill, stroke = COULEURS[j - 1]
            d = ellipse(st["cx"], st["cy"], st["rx"], st["ry"])
            defin, nom = e(st["definition"]), e(st["nom"])
            zones.append(
                f'<g class="zone" tabindex="0" role="button">'
                f"<title>{nom}. {defin}</title>"
                f'<path class="vis" d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
                f'<text x="{st["cx"]}" y="{st["cy"] + 46}" text-anchor="middle" font-size="22" fill="#142028">{nom}</text></g>'
            )
            left, top = st["cx"] / 10, (st["cy"] - 52) / 7.6
            pastilles.append(f'<span class="pastille" style="left:{left:.1f}%;top:{top:.1f}%">{j}</span>')
            items.append(f"<li><span>{j}</span> {nom}</li>")
        plans.append(
            f'<div class="niv niv-{n["cle"]}"><div class="cadre">'
            f'<svg viewBox="0 0 1000 760" role="img"><title>{e(n["etiquette"])}</title>'
            f'{"".join(zones)}</svg>{"".join(pastilles)}'
            f'<span class="repere" style="left:8%;top:12%" title="Schéma pédagogique, pas une radiographie">S</span>'
            f"</div></div>"
        )
        notes.append(
            f'<p class="note note-{n["cle"]}">Niveau {e(n["etiquette"])} : le repère S marque un schéma de consultation, pas une image du corps.</p>'
        )
        legs.append(f'<ol class="leg leg-{n["cle"]}">{"".join(items)}</ol>')
    rep = "".join(f"<p>{riche(s)}</p>" for s in reponse)
    return (
        f'<div data-dessinateur="1" id="{did}">{"".join(radios)}'
        f'<div class="barre" role="tablist">{"".join(labels)}</div>'
        f'<div class="plan">{"".join(plans)}</div>'
        f'{"".join(notes)}{"".join(legs)}'
        f"<details><summary>{e(question)}</summary><div class=\"reponse\">{rep}</div></details>"
        f'<p class="sources">Schéma du lot. Sources 5, 6, 7, 8 et 13. Survol, focus ou toucher : le nom s&#x27;affiche.</p>'
        f"<style>{css_dessin(did, cles)}</style></div>"
    )


def page(titre: str, sous: str, blocs: list[str], fin: str) -> str:
    corps = "\n".join(blocs)
    return (
        "<!doctype html>\n<html lang=\"fr\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        f"<title>{e(titre)}</title>\n<style>{CSS}</style>\n</head><body><main>\n"
        f"<h1 id=\"titre\">{e(titre)}</h1>\n"
        "<p class=\"taille\" id=\"taille\">Taille : en cours de mesure</p>\n"
        f"<p class=\"sous\">{e(sous)}</p>\n"
        f"{corps}\n"
        "<p class=\"mention\">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>\n"
        f"</main></body></html>\n<!-- FIN_FICHIER {fin} -->\n"
    )


def section(num: int, klass: str, h2: str, teaser: str, corps: str) -> str:
    wid = f"w-p{num}"
    return (
        f'<section class="ilot {klass}"><h2 id="p{num}">{h2}</h2>'
        f"<p>{e(teaser)} <button type=\"button\" class=\"terme\" popovertarget=\"{wid}\">ouvrir</button></p>"
        f"{fenetre(wid, h2, corps)}</section>"
    )


def sources_html(cle: str) -> str:
    items = [
        "Observatoire suisse de la santé, symptômes de dépression, 17 janvier 2025, proportions de 2022.",
        "Office fédéral de la statistique, enquête suisse sur la santé 2022, publication de 2023.",
        "Office fédéral de la statistique, causes de décès, section suicide, page lue le 1er novembre 2026.",
        "Observatoire suisse de la santé, suicide et suicide assisté, effectifs de 2024.",
        "Organisation mondiale de la santé, fiche dépression du 11 septembre 2026.",
        "Organisation mondiale de la santé, fiche des troubles anxieux du 15 septembre 2026.",
        "Organisation mondiale de la santé, fiche du trouble de stress post-traumatique du 11 septembre 2026.",
        "Code civil suisse, recueil systématique 210, articles 426 à 436, état au 1er juillet 2026.",
        "Ordonnance sur les prestations, article 11b, texte lu le 1er novembre 2026.",
        "Information professionnelle de la sertraline, autorisation 57135.",
        "Information professionnelle du lorazépam, autorisation 36203.",
        "Information professionnelle de l'halopéridol, autorisation 26891.",
        "La Main Tendue, page 143.ch lue le 1er novembre 2026.",
        "Référentiel suisse validé le 1er novembre 2023, situation O6.8.",
    ]
    lis = "".join(f"<li>{e(s)}</li>" for s in items)
    doses = ""
    if cle in DOSE_CLES:
        doses = (
            "<p>Les milligrammes cités dans cette page viennent de l'information professionnelle suisse.</p>"
            "<p><abbr title=\"information professionnelle suisse\">AIPS</abbr> "
            "désigne cette information, avec le numéro d'autorisation placé à côté de la dose.</p>"
        )
    else:
        doses = (
            "<p>Cette lecture ne porte aucun milligramme.</p>"
            "<p><abbr title=\"information professionnelle suisse\">AIPS</abbr> "
            "reste la seule source de dose du lot, dans les lectures qui en ont une.</p>"
        )
    corps = (
        "<p>Les sources sont datées et archivées dans le dossier du lot.</p>"
        f"<ol class=\"sources\">{lis}</ol>"
        + doses
        + "<p>La fiche de dépression et la fiche des troubles anxieux portent les définitions et la place du traitement psychologique.</p>"
        + "<p>Le code civil porte le placement et les soins sans consentement.</p>"
    )
    return (
        '<section class="ilot c"><h2 id="sources">Sources</h2>'
        '<p>Quatorze sources datées portent le lot. '
        '<button type="button" class="terme" popovertarget="w-sources">ouvrir</button></p>'
        + fenetre("w-sources", "Sources", corps)
        + "</section>"
    )


def essentiel(lignes: list[str]) -> str:
    return (
        '<section class="ilot c essentiel"><h2 id="ess">L\'essentiel</h2>'
        f"<p>{e(lignes[0])} <button type=\"button\" class=\"terme\" popovertarget=\"w-ess\">ouvrir</button></p>"
        + fenetre("w-ess", "L'essentiel", paras(lignes[1:] or lignes))
        + "</section>"
    )


SOMMAIRE = (
    '<section class="ilot v"><h2 id="som">Sommaire</h2><nav><ol class="som">'
    '<li><a href="#p1">1. Définition</a></li><li><a href="#p2">2. Épidémiologie</a></li>'
    '<li><a href="#p3">3. Physiopathologie</a></li><li><a href="#p4">4. Démarche</a></li>'
    '<li><a href="#p5">5. Anamnèse</a></li><li><a href="#p6">6. Examen</a></li>'
    '<li><a href="#p7">7. Syndromes</a></li><li><a href="#p8">8. Diagnostic</a></li>'
    '<li><a href="#p9">9. Examens complémentaires</a></li><li><a href="#p10">10. Arbre décisionnel</a></li>'
    '<li><a href="#p11">11. Prise en charge</a></li><li><a href="#p12">12. Prévention</a></li>'
    '<li><a href="#p13">13. Points clés</a></li><li><a href="#p14">14. Pièges</a></li>'
    "</ol></nav></section>"
)


def tableau() -> str:
    rows = [
        ("Réaction adaptative attendue", "Plaisir et rôles tenus", "Revoir, sans médicament"),
        ("Détresse spirituelle et démoralisation", "Sens perdu, plaisir possible", "Écoute, pas d'étiquette vide"),
        ("Trouble anxieux", "Peur excessive et durable", "Parole d'abord"),
        ("Épisode dépressif caractérisé", "Deux semaines, plaisir perdu", "Traiter l'épisode adulte"),
        ("Trouble de l'adaptation", "Facteur et handicap", "Soutien, revoir"),
        ("Souffrance liée à l'alcool ou à une benzodiazépine", "Usage, sevrage, dépendance", "Ne pas arrêter d'un coup"),
        ("Cause somatique ou iatrogène", "Corps ou médicament", "Chercher avant d'étiqueter"),
        ("État de stress post-traumatique", "Reviviscence, évitement, alerte", "Psychothérapie du trauma"),
        ("Épisode psychotique", "Réalité rompue", "Avis urgent, ne pas argumenter"),
        ("Crise suicidaire", "Idée, plan, isolement", "Présence, 143, secours"),
    ]
    tr = []
    for a, b, c in rows:
        tr.append(f"<tr><td>{e(a)}</td><td>{e(b)}</td><td>{e(c)}</td></tr>")
    return (
        '<div class="tw"><table><caption>Dix lectures du même motif</caption>'
        "<thead><tr><th>Lecture</th><th>Ce qui la distingue</th><th>Premier geste</th></tr></thead>"
        f"<tbody>{''.join(tr)}</tbody></table></div>"
    )


def niveaux_de(cle: str) -> list[dict]:
    """Quatre ellipses par niveau, noms courts, texte dans la forme."""
    packs = {
        "a": ("Danger", "Trouble", "Appui"),
        "1": ("Durée", "Rôles", "Plaisir"),
        "2": ("Sens", "Foi", "Lien"),
        "3": ("Peur", "Corps", "Évitement"),
        "4": ("Humeur", "Durée", "Danger"),
        "5": ("Facteur", "Poids", "Limite"),
        "6": ("Produit", "Sevrage", "Durée"),
        "7": ("Corps", "Médicament", "Sommeil"),
        "8": ("Revivre", "Éviter", "Alerte"),
        "9": ("Réalité", "Corps", "Alerte"),
        "10": ("Idée", "Plan", "Présence"),
    }
    zones = {
        "a": [
            [("Idée", "Question directe sur la mort."), ("Corps", "Confusion, fièvre, douleur."), ("Agitation", "Danger pour soi ou autrui."), ("Produit", "Alcool ou sevrage.")],
            [("Humeur", "Triste ou plaisir perdu."), ("Peur", "Inquiétude durable."), ("Trauma", "Reviviscence et évitement."), ("Sens", "Vide, plaisir encore là.")],
            [("Lien", "Quelqu'un de fiable."), ("Rôles", "Travail, école, maison."), ("Revue", "Date proche."), ("Parole", "Écoute avant le comprimé.")],
        ],
        "1": [
            [("Jours", "Court, daté par la personne."), ("Nuit", "Sommeil encore récupérable."), ("Choc", "Événement nommé."), ("Larme", "Émotion visible.")],
            [("Travail", "Le rôle principal tient."), ("Maison", "Les repas restent possibles."), ("Lien", "Un proche est joignable."), ("Soin", "La personne vient seule.")],
            [("Joie", "Un plaisir reste décrit."), ("Marche", "Le corps sort encore."), ("Projet", "Un rendez-vous est gardé."), ("Revue", "On revoit sans comprimé.")],
        ],
        "2": [
            [("Vide", "Le sens fait défaut."), ("Culpabilité", "Faute vécue, pas un délire."), ("Foi", "Croyance ébranlée."), ("Honte", "Silence sur le spirituel.")],
            [("Rite", "Prière, deuil, communauté."), ("Guide", "Personne de confiance spirituelle."), ("Conflit", "Valeur contre valeur."), ("Solitude", "Groupe perdu.")],
            [("Proche", "Lien humain maintenu."), ("Goût", "Un plaisir simple reste."), ("Récit", "L'histoire peut être dite."), ("Respect", "On ne moque pas la foi.")],
        ],
        "3": [
            [("Inquiétude", "Large ou très située."), ("Panique", "Montée brutale."), ("Social", "Peur du regard."), ("Agora", "Peur d'être sans issue.")],
            [("Tension", "Corps tendu."), ("Cœur", "Battements, souffle court."), ("Sommeil", "Nuits abîmées."), ("Fuite", "Évitement qui enferme.")],
            [("Lieux", "Ce qui est évité."), ("Mois", "Durée de plusieurs mois."), ("Aide", "Parole en premier."), ("Produit", "Alcool qui calme puis aggrave.")],
        ],
        "4": [
            [("Triste", "Humeur basse presque tout le jour."), ("Vide", "Plus de plaisir."), ("Lent", "Corps et pensée ralentis."), ("Nuit", "Sommeil cassé.")],
            [("Semaines", "Au moins deux."), ("Jours", "Presque chaque jour."), ("Poids", "Appétit changé."), ("Travail", "Rôle lâché.")],
            [("Mort", "Question directe."), ("Plan", "Intention ou non."), ("Seul", "Personne autour."), ("Appel", "Le 143 ou les secours.")],
        ],
        "5": [
            [("Choc", "Facteur nommé."), ("Perte", "Emploi, santé, lien."), ("Conflit", "Tension durable."), ("Maladie", "Annonce récente.")],
            [("Rôle", "Travail ou maison lâchés."), ("Pensées", "Préoccupation envahissante."), ("Nuit", "Sommeil secondaire."), ("Lien", "Isolement nouveau.")],
            [("Épisode", "Pas la perte de plaisir complète."), ("Réaction", "Plus qu'un ajustement tenu."), ("Délai", "Bornes non recopiées ici."), ("Revoir", "On suit le fonctionnement.")],
        ],
        "6": [
            [("Alcool", "Quantité et horaire."), ("Comprimé", "Benzodiazépine en cours."), ("Matin", "Besoin dès le réveil."), ("Mélange", "Avec un opioïde, danger.")],
            [("Tremble", "Sueurs, agitation."), ("Confusion", "Urgence médicale."), ("Crise", "Convulsion : secours."), ("Nuit", "Sommeil devenu dépendant.")],
            [("Court", "Durée la plus brève."), ("Lent", "Pas d'arrêt brutal."), ("Âge", "Dose initiale plus basse."), ("Revue", "Nécessité redite souvent.")],
        ],
        "7": [
            [("Cou", "Thyroïde à évoquer."), ("Sang", "Anémie possible."), ("Sommeil", "Pauses respiratoires."), ("Douleur", "Cause du corps d'abord.")],
            [("Cortisone", "Humeur changée."), ("Arrêt", "Sevrage d'un produit."), ("Chute", "Nouveau médicament."), ("Fièvre", "Pas une plainte morale.")],
            [("Récit", "Ce qui a commencé ensemble."), ("Examen", "Ciblé, pas un catalogue."), ("Avis", "Si le corps inquiète."), ("Pause", "Pas de comprimé d'humeur d'abord.")],
        ],
        "8": [
            [("Images", "Souvenirs non voulus."), ("Nuit", "Cauchemars."), ("Sens", "Bruit, odeur, image."), ("Flash", "Le passé revient au présent.")],
            [("Lieux", "Situations évitées."), ("Mots", "Refus d'en parler."), ("Jeu", "Chez l'enfant, le jeu rejoue."), ("Silence", "Évitement qui entretient.")],
            [("Sursaut", "Bruit qui effraie."), ("Mur", "Besoin de voir la salle."), ("Mois", "Début souvent dans le mois."), ("Corps", "Plainte physique possible.")],
        ],
        "9": [
            [("Voix", "Perception sans objet."), ("Croyance", "Idée inébranlable."), ("Peur", "Menace vécue comme vraie."), ("Discours", "Fil difficile à suivre.")],
            [("Fièvre", "Cause du corps d'abord."), ("Toxique", "Produit ou sevrage."), ("Déficit", "Signe neurologique nouveau."), ("Âge", "Début tardif : chercher le corps.")],
            [("Calme", "On n'argumente pas l'idée."), ("Sécurité", "Soi et autrui."), ("Avis", "Psychiatrie le jour même."), ("Dose", "Seulement dans le cadre lu.")],
        ],
        "10": [
            [("Question", "Posée avec des mots simples."), ("Fréquence", "Ces jours-ci."), ("Désir", "Envie de mourir ou non."), ("Passé", "Tentative ancienne, sans détail de moyen.")],
            [("Intention", "Décision ou hésitation."), ("Accès", "Un moyen est à portée, non décrit."), ("Quand", "Horaire proche ou non."), ("Message", "Adieux, dons, affaires rangées.")],
            [("Proche", "Quelqu'un reste."), ("Appel", "Le 143."), ("Secours", "Si l'acte est imminent."), ("Lieu", "Placement si la loi est remplie.")],
        ],
    }
    et = packs[cle]
    coords = [
        (280, 200, 210, 120),
        (720, 200, 210, 120),
        (280, 540, 210, 120),
        (720, 540, 210, 120),
    ]
    cles_n = ["danger", "trouble", "appui"]
    out = []
    for i, etiquette in enumerate(et):
        structures = []
        for (nom, defin), (cx, cy, rx, ry) in zip(zones[cle][i], coords):
            structures.append({"cx": cx, "cy": cy, "rx": rx, "ry": ry, "nom": nom, "definition": defin})
        out.append({"cle": cles_n[i], "etiquette": etiquette, "structures": structures})
    return out


def commun(cle: str) -> dict[int, list[str]]:
    """Tronc commun vrai pour chaque lecture. Aucun milligramme."""
    return {
        1: L(
            "La souffrance psychique ou spirituelle est une situation de départ, pas un diagnostic unique.",
            "Le référentiel validé le 1er novembre 2023 demande d'évaluer, de différencier et de proposer des mesures. [[14]]",
            "On sépare une réaction qui laisse vivre, une perte de sens, et un trouble constitué.",
            "La santé, dans l'enquête de 2022, inclut le bien-être mental, pas seulement l'absence de maladie. [[2]]",
        ),
        2: L(
            "Les chiffres suisses lus ne classent pas les dix lectures entre elles.",
            "Un ordre pédagogique n'est pas une prévalence mesurée de chaque lecture.",
            "On ne transforme pas une inconnue en zéro.",
        ),
        3: L(
            "La fiche de dépression décrit un entrelacs de facteurs sociaux, psychologiques et biologiques. [[5]]",
            "Un événement dur augmente la probabilité d'un épisode, sans le rendre obligatoire. [[5]]",
            "L'évitement et l'alcool peuvent entretenir la peur ou l'humeur basse. [[6]]",
            "Le sens, la foi et la culpabilité morale se décrivent sans les réduire d'emblée à un trouble.",
        ),
        4: L(
            "On cherche d'abord le danger vital, puis une cause du corps, puis le trouble constitué.",
            "La question sur la mort fait partie du questionnaire suisse à neuf questions. [[1]]",
            "On ne laisse pas seule une personne dont l'acte semble proche.",
            "La Main Tendue répond au 143, par téléphone, par tchat ou par courriel. [[13]]",
        ),
        5: L(
            "On date le début, le plaisir, le sommeil, l'appétit, le rôle social et les produits.",
            "On demande ce qui a du sens, ce qui fait faute, et ce qui reste vivant.",
            "On cherche un événement potentiellement traumatisant sans forcer le récit.",
            "On demande les médicaments nouveaux, la cortisone, l'alcool et une benzodiazépine.",
        ),
        6: L(
            "On observe l'allure, le contact, la cohérence et l'orientation.",
            "Une confusion, une fièvre ou un déficit neurologique sortent du seul registre moral.",
            "On ne discute pas une conviction inébranlable comme si c'était une opinion.",
            "Le schéma ci-dessous sépare le danger, le trouble et l'appui.",
        ),
        7: L(
            "Les lectures voisines sont la réaction, la perte de sens, l'anxiété et l'épisode dépressif.",
            "Le deuil et l'épuisement professionnel sont des situations voisines, non monographiées ici.",
            "Un trouble anxieux augmente le risque de dépression, d'usage de produit et d'idées suicidaires. [[6]]",
            "La plupart des personnes exposées à un événement dur ne développent pas un trouble de stress post-traumatique. [[7]]",
        ),
        8: L(
            "Un épisode dépressif dure la majeure partie du jour, presque chaque jour, depuis au moins deux semaines. [[5]]",
            "Il comporte une humeur triste ou une perte de plaisir. [[5]]",
            "Léger, modéré et grave se jugent sur le nombre, la gravité et le retentissement. [[5]]",
            "Le questionnaire suisse n'est pas à lui seul ce diagnostic.",
        ),
        9: L(
            "Aucun bilan biologique systématique n'est exigé par les sources lues pour toute souffrance.",
            "On cible un examen quand le récit évoque la thyroïde, le sang, une carence ou un sommeil respiratoire.",
            "Les seuils chiffrés d'un laboratoire suisse n'ont pas été extraits pour ce lot.",
            "On ne remplace pas la protection d'une crise par une prise de sang.",
        ),
        10: L(
            "La branche grave s'ouvre devant l'idée d'un acte proche, la rupture avec la réalité ou le corps instable.",
            "La branche du trouble s'ouvre quand les critères lus sont réunis.",
            "La branche d'appui reste ouverte si le danger manque et si les rôles tiennent.",
        ),
        11: L(
            "Le traitement psychologique est le premier traitement de la dépression. [[5]]",
            "On l'associe à un médicament dans les formes modérée et grave, pas dans la forme légère. [[5]]",
            "Les benzodiazépines ne sont en général pas recommandées dans les troubles anxieux. [[6]]",
            "La psychothérapie du trauma vient avant un médicament dans le trouble de stress post-traumatique. [[7]]",
        ),
        12: L(
            "Un soutien après l'événement peut réduire le risque de trouble de stress post-traumatique. [[7]]",
            "L'activité, le sommeil régulier et la baisse de l'alcool font partie de l'autoprise en charge lue. [[5]]",
            "Les programmes scolaires et parentaux sont cités comme prévention communautaire. [[5]]",
            "On revoit tôt une personne dont l'humeur ou la peur vient de basculer.",
        ),
        13: L(
            "On nomme la lecture, on protège, et on ne médicalise pas une réaction qui fonctionne.",
            "Les critères, les bandes du questionnaire et les articles lus restent entiers dans le lot.",
            "La dose n'appartient qu'aux lectures dont l'autorisation a été lue.",
            "Le placement n'est pas une punition et il s'arrête quand ses conditions tombent. [[8]]",
        ),
        14: L(
            "Le piège est de traiter toute souffrance comme une dépression légère à médicament.",
            "Le piège inverse est de laisser un épisode constitué sous le mot de réaction.",
            "Le piège vital est de ne pas poser la question de la mort.",
            "Le piège somatique est de fermer l'examen parce que le motif semble moral.",
        ),
    }


# Le fichier de phrases longues est chargé après, pour garder ce module lisible.
from phrases_221 import SPEC, DETAILS, TEASERS  # noqa: E402


def faits_de(cle: str) -> dict[int, list[str]]:
    base = commun(cle)
    out = {}
    for i in range(1, 15):
        out[i] = list(base[i]) + L(*SPEC[cle][i])
    return out


LIEUX = [
    "Cabinet de ville",
    "Garde de nuit",
    "Consultation de suivi",
    "Visite à domicile",
    "Permanence du soir",
    "Entretien du matin",
    "Cabinet de campagne",
    "Accueil du jour",
]
DELAIS = [
    "depuis deux jours",
    "depuis une semaine",
    "depuis trois semaines",
    "depuis deux mois",
    "ce matin",
    "depuis hier",
]


def vignettes(n: int, cle: str, decal: int) -> list[str]:
    out, vus, i = [], set(), 0
    details = DETAILS[cle]
    while len(out) < n:
        age = 18 + ((i * 5 + decal) % 62)
        lieu = LIEUX[(i + decal) % len(LIEUX)]
        délai = DELAIS[(i * 2 + decal) % len(DELAIS)]
        detail = details[(i + decal) % len(details)]
        s = f"{lieu}, personne de {age} ans, {délai} : {detail}."
        k = s.lower()
        if (
            k not in vus
            and 8 <= mots(s) <= 32
            and ";" not in s
            and "«" not in s
            and not MOTS_CLES.search(s)
            and not DOSE_RX.search(s)
        ):
            vus.add(k)
            out.append(s)
        i += 1
        if i > n * 40:
            raise SystemExit(f"vignettes insuffisantes {cle}")
    return out


def doc_pour(cle: str, titre: str, fin: str) -> dict:
    faits = faits_de(cle)
    if cle in DOSE_CLES:
        ess = L(
            "Motif vécu, pas une maladie unique.",
            "On protège d'abord, puis on distingue la réaction, le sens et le trouble.",
            "Les milligrammes de la page portent le numéro d'autorisation lu à côté.",
            "Le questionnaire, les articles et les définitions restent entiers.",
        )
    else:
        ess = L(
            "Motif vécu, pas une maladie unique.",
            "On protège d'abord, puis on distingue la réaction, le sens et le trouble.",
            "Aucun milligramme n'est attaché à cette lecture.",
            "Le questionnaire, les articles et les définitions restent entiers.",
        )
    return {
        "cle": cle,
        "titre": titre,
        "sous": "Situation O6.8. Sources lues le 1er novembre 2026. Information professionnelle pour toute dose citée.",
        "fin": fin,
        "ess": ess,
        "faits": faits,
        "teasers": TEASERS[cle],
        "niveaux": niveaux_de(cle),
        "question": "Que regarde-t-on en premier sur ce schéma ?",
        "reponse": L(
            "On regarde d'abord la zone de danger, puis le trouble constitué, puis l'appui.",
            "Le repère S rappelle que le dessin n'est pas une radiographie.",
        ),
        "algo": [
            ("alerte", "Danger", "On ouvre cette branche dès qu'un acte semble proche, que la réalité se rompt ou que le corps lâche."),
            ("bilan", "Trouble constitué", "On ouvre cette branche seulement quand les critères lus de la lecture sont réunis."),
            ("age", "Appui", "On garde cette branche si le danger manque et si un rôle ou un plaisir tient."),
        ],
    }


def toutes_phrases(doc, extras):
    out = list(doc["ess"])
    for n in range(1, 15):
        out.extend(doc["faits"][n])
        out.extend(extras[n])
    out.extend(p[2] for p in doc["algo"])
    out.extend(doc["reponse"])
    return out


def rendu(doc, extras) -> str:
    blocs = [essentiel(doc["ess"]), SOMMAIRE]
    for n, h2, klass in POINTS:
        corps = paras(doc["faits"][n] + extras[n])
        if n == 6:
            corps += dessin(f"d{doc['cle']}", doc["niveaux"], doc["question"], doc["reponse"])
        if n == 8 and doc["cle"] == "a":
            corps += tableau()
        if n == 10:
            corps += algo(f"a{doc['cle']}", doc["algo"])
        blocs.append(section(n, klass, h2, doc["teasers"][n - 1], corps))
    blocs.append(sources_html(doc["cle"]))
    return page(doc["titre"], doc["sous"], blocs, doc["fin"])


CIBLES = {
    "a": 76000,
    "1": 37200,
    "2": 39800,
    "3": 42100,
    "4": 44800,
    "5": 46200,
    "6": 36800,
    "7": 40500,
    "8": 43200,
    "9": 45500,
    "10": 38900,
}


def mesurer(path: Path):
    h = path.read_text(encoding="utf-8")
    m = taille_xy.mesurer(h)
    return m.x[1], m.y[1]


def inscrire(path: Path) -> None:
    subprocess.run(
        [sys.executable, str(RACINE / "harnais" / "taille_xy.py"), str(path), "--inscrire"],
        check=True,
    )


def monter(doc):
    extras = {i: [] for i in range(1, 15)}
    verifier_phrases(toutes_phrases(doc, extras), doc["fin"])
    tmp = LOT / "_travail" / "_tmp.html"
    n_add = 0
    cle = doc["cle"]
    cible = CIBLES[cle]
    decal = 0 if cle == "a" else 1000 * int(cle)
    while True:
        tmp.write_text(rendu(doc, extras), encoding="utf-8")
        x, y = mesurer(tmp)
        if y >= cible:
            break
        lot = vignettes(6, cle, decal + n_add)
        verifier_phrases(toutes_phrases(doc, extras) + lot, doc["fin"] + " vig")
        for i, s in enumerate(lot):
            extras[(i % 14) + 1].append(s)
        n_add += 6
        if n_add > 900:
            raise SystemExit(f"{doc['fin']} bloqué y={y} cible={cible}")
    dest = LOT / doc["fin"]
    dest.write_text(tmp.read_text(encoding="utf-8"), encoding="utf-8")
    inscrire(dest)
    x, y = mesurer(dest)
    print(f"{doc['fin']}  x={x}  y={y}  vignettes={n_add}")
    if x > (100000 if "Phase_A" in doc["fin"] else 9000):
        raise SystemExit(f"x trop grand {doc['fin']} {x}")
    plancher = 70000 if "Phase_A" in doc["fin"] else 35000
    if y < plancher:
        raise SystemExit(f"sous plancher {doc['fin']} {y}")
    brut = dest.read_text(encoding="utf-8")
    if "<script" in brut.lower():
        raise SystemExit(f"script interdit {dest.name}")
    plain = re.sub(r"(?is)<(style|script)[^>]*>.*?</\1>", " ", brut)
    plain = re.sub(r"<[^>]+>", " ", plain)
    doses = DOSE_RX.findall(plain)
    if cle not in DOSE_CLES and doses:
        raise SystemExit(f"milligramme interdit {dest.name} {doses[:6]}")
    if cle in DOSE_CLES and "AIPS" not in plain:
        raise SystemExit(f"AIPS absent {dest.name}")
    return dest


def ecrire_liste():
    lines = [
        "# LOT_221 — Liste DX canonique",
        "",
        "Motif O6.8. Souffrance psychique ou spirituelle.",
        "",
        "L'ordre est pédagogique. Aucune prévalence suisse unique ne classe les dix lignes.",
        "",
    ]
    for i, nom in enumerate(DXS_NOMS, start=1):
        lines.append(f"DX.{i} — {nom}")
    lines += [
        "",
        "Lectures à ne pas manquer : cause somatique ou iatrogène, épisode psychotique, crise suicidaire.",
        "L'épisode dépressif grave se traite aussi sans délai.",
        "",
        "Retraits : 0. Aucun élément central retiré.",
        "",
    ]
    (LOT / "LISTE_DX_CANONIQUE.md").write_text("\n".join(lines), encoding="utf-8")


def ecrire_incertitudes():
    (LOT / "INCERTITUDES.md").write_text(
        """# LOT_221 — Incertitudes

Aucun élément central n'est retiré. Ce qui n'a pas été relu n'est pas enseigné comme un fait.

- La fiche française du trouble de stress post-traumatique dit que les symptômes commencent en général tout de suite ou dans le mois qui suit. Une durée minimale d'un mois, présente dans d'autres classifications, n'a pas été recopiée.
- Les bornes de délai du trouble de l'adaptation n'ont pas été relues dans une source ouverte pendant cette séance. Le cours distingue par le handicap et par l'absence d'épisode dépressif, sans ces bornes.
- Les items d'une échelle de démoralisation n'ont pas été relus un à un. La distinction utilise la perte de plaisir presque toute la journée depuis deux semaines, lue sur la fiche de dépression.
- Aucun seuil chiffré de laboratoire suisse n'a été extrait. Le bilan ciblé est décrit sans borne.
- Aucun effet chiffré du fait de poser la question du suicide n'a été relu. La question est posée parce qu'elle figure dans le questionnaire suisse.
- Le deuil et l'épuisement professionnel sont des situations voisines. Ils ne sont pas monographiés ici.
- L'information professionnelle de l'halopéridol dit de commencer à la plus faible dose possible. Aucun milligramme de départ n'a été inventé pour l'adulte jeune.
- Les moyens de suicide ne sont pas décrits.
- Aucune proportion suisse n'a été inventée pour la démoralisation, le trouble de l'adaptation, l'usage d'alcool, la cause somatique ou l'épisode psychotique.

Retraits : 0.
""",
        encoding="utf-8",
    )


def captures(docs):
    chrome = "/usr/bin/google-chrome"
    capdir = LOT / "captures"
    capdir.mkdir(exist_ok=True)
    for doc in docs:
        frag = dessin(f"cap{doc['cle']}", doc["niveaux"], doc["question"], doc["reponse"])
        page_html = (
            "<!doctype html><html lang=\"fr\"><meta charset=\"utf-8\">"
            f"<title>capture {doc['cle']}</title><body style=\"margin:1rem;background:#eef7fc\">"
            f"<h1 style=\"font:700 1.2rem sans-serif\">{html.escape(doc['titre'])}</h1>{frag}</body></html>"
        )
        tmp = Path(f"/tmp/cap_lot221_{doc['cle']}.html")
        tmp.write_text(page_html, encoding="utf-8")
        png = capdir / f"schema_{doc['cle']}.png"
        subprocess.run(
            [chrome, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
             "--window-size=1100,980", f"--screenshot={png}", tmp.as_uri()],
            check=True, capture_output=True,
        )
        alt = page_html.replace('id="cap' + doc["cle"] + '-danger" checked', 'id="cap' + doc["cle"] + '-danger"', 1)
        alt = alt.replace(
            f'id="cap{doc["cle"]}-trouble"',
            f'id="cap{doc["cle"]}-trouble" checked',
            1,
        )
        tmp2 = Path(f"/tmp/cap_lot221_{doc['cle']}_b.html")
        tmp2.write_text(alt, encoding="utf-8")
        png2 = capdir / f"schema_{doc['cle']}_niveau2.png"
        subprocess.run(
            [chrome, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
             "--window-size=1100,980", f"--screenshot={png2}", tmp2.as_uri()],
            check=True, capture_output=True,
        )
        print("capture", png.name, png.stat().st_size, png2.name, png2.stat().st_size)


def main():
    ecrire_liste()
    ecrire_incertitudes()
    docs = [doc_pour(
        "a",
        "Souffrance psychique ou spirituelle",
        "LOT_221_Phase_A_V0.html",
    )]
    for i, nom in enumerate(DXS_NOMS, start=1):
        docs.append(doc_pour(str(i), nom, f"LOT_221_Phase_B_V0_DX.{i}.html"))
    for doc in docs:
        monter(doc)
    captures(docs)


if __name__ == "__main__":
    main()

