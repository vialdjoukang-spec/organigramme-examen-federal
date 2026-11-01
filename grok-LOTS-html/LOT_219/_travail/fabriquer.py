#!/usr/bin/env python3
"""Assemble LOT_219 (O6.6). Phrases cliniques ici. Preuves dans evidence/."""
from __future__ import annotations

import html
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_219"
sys.path.insert(0, str(RACINE / "harnais"))
import taille_xy  # noqa: E402

MOTS_CLES = re.compile(
    r"\b(incidence|prévalence|prevalence|sensibilit[ée]|spécificit[ée]|specificit|seuil|score)\b",
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
    "Réaction d'adaptation attendue après une séparation",
    "Conflit de loyauté et coparentalité conflictuelle",
    "Monoparentalité et précarité matérielle",
    "Famille recomposée et place du beau-parent",
    "Trouble de l'adaptation",
    "Épisode dépressif caractérisé",
    "Refus de contact avec un parent",
    "Plainte somatique de l'enfant",
    "Enfant exposé à la violence",
    "Crise suicidaire lors d'une séparation",
]


def e(s: str) -> str:
    return html.escape(s, quote=False)


def riche(s: str) -> str:
    t = e(s)
    t = re.sub(r"\[\[(\d+)\]\]", r'<sup class="s">\1</sup>', t)
    return t


def mots(s: str) -> int:
    nu = re.sub(r"\[\[\d+\]\]", " ", s)
    return len(nu.split())


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
        if n > 34:
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
            raise SystemExit(f"guillemet à vérifier à part {ou}: {s}")


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
        labels.append(f'<label for="{iid}">{e(lib)}</label>')
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
                f'<text x="{st["cx"]}" y="{st["cy"] + 36}" text-anchor="middle" font-size="22" fill="#142028">{nom}</text></g>'
            )
            left, top = st["cx"] / 10, st["cy"] / 7.6
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
            f'<p class="note note-{n["cle"]}">Sur le niveau {e(n["etiquette"])}, le repère S signale un schéma de consultation et non une image du corps.</p>'
        )
        legs.append(f'<ol class="leg leg-{n["cle"]}">{"".join(items)}</ol>')
    rep = "".join(f"<p>{riche(s)}</p>" for s in reponse)
    return (
        f'<div data-dessinateur="1" id="{did}">{"".join(radios)}'
        f'<div class="barre" role="tablist">{"".join(labels)}</div>'
        f'<div class="plan">{"".join(plans)}</div>'
        f'{"".join(notes)}{"".join(legs)}'
        f"<details><summary>{e(question)}</summary><div class=\"reponse\">{rep}</div></details>"
        f'<p class="sources">Schéma du lot, sources 4, 5 et 6. Survol, focus ou toucher : le nom s&#x27;affiche.</p>'
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


def sources_html() -> str:
    items = [
        "Office fédéral de la statistique, mariages et divorces, page lue le 1er novembre 2026.",
        "Office fédéral de la statistique, enfants mineurs et divorces de 2025, fichier du 18 juin 2026.",
        "Office fédéral de la statistique, ménages privés de 2024, copyright 2026.",
        "Code civil suisse, recueil systématique 210, Fedlex lu le 1er novembre 2026.",
        "Organisation mondiale de la santé, violence à l'égard des femmes, fiche du 18 juin 2026.",
        "Organisation mondiale de la santé, descriptions cliniques, Genève, 2024.",
        "La Main Tendue, page lue le 1er novembre 2026, appel du 143.",
        "Information professionnelle de la sertraline, autorisation 57135.",
        "Référentiel suisse validé le 1er novembre 2023, situation O6.6.",
        "Organisation mondiale de la santé, fiche des troubles mentaux, lue le 1er novembre 2026.",
    ]
    lis = "".join(f"<li>{e(s)}</li>" for s in items)
    corps = (
        "<p>Les sources sont datées et archivées dans le dossier du lot.</p>"
        f"<ol class=\"sources\">{lis}</ol>"
        "<p><abbr title=\"Office fédéral de la statistique\">OFS</abbr> "
        "<abbr title=\"Organisation mondiale de la santé\">OMS</abbr> "
        "<abbr title=\"information professionnelle suisse\">AIPS</abbr> "
        "<abbr title=\"classification internationale des maladies\">CIM</abbr></p>"
        "<p>L'OFS porte les divorces, les enfants mineurs et les ménages.</p>"
        "<p>L'OMS porte la fiche de violence, la fiche des troubles mentaux et le livre de 2024.</p>"
        "<p>L'AIPS porte les milligrammes de l'autorisation 57135.</p>"
        "<p>La CIM de 2024 décrit le trouble de l'adaptation et l'épisode dépressif.</p>"
    )
    return (
        '<section class="ilot c"><h2 id="sources">Sources</h2>'
        '<p>Dix sources datées portent le lot. '
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
        ("Réaction d'adaptation attendue après une séparation", "Jeu et école tenus", "Revoir, sans médicament"),
        ("Conflit de loyauté et coparentalité conflictuelle", "Enfant messager", "Nommer, déculpabiliser"),
        ("Monoparentalité et précarité matérielle", "Loyer, pension, fatigue", "Relais social"),
        ("Famille recomposée et place du beau-parent", "Place du beau-parent", "Temps, règles claires"),
        ("Trouble de l'adaptation", "Préoccupation et handicap", "Soutien, pas d'étiquette vide"),
        ("Épisode dépressif caractérisé", "Cinq symptômes, deux semaines", "Traiter l'épisode adulte"),
        ("Refus de contact avec un parent", "Rejet d'un parent", "Écarter d'abord un danger"),
        ("Plainte somatique de l'enfant", "Douleur, énurésie, fatigue", "Examen avant le divorce"),
        ("Enfant exposé à la violence", "Peur, contrôle, lésion", "Sécurité, droit d'aviser"),
        ("Crise suicidaire lors d'une séparation", "Idées, moyen, isolement", "143 et secours"),
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
    packs = {
        "a": ("Foyer", "Conflit", "Danger"),
        "1": ("Âge", "Durée", "Fonction"),
        "2": ("Messager", "Dénigrement", "Deux liens"),
        "3": ("Logement", "Argent", "Fatigue"),
        "4": ("Beau-parent", "Règles", "Parent d'origine"),
        "5": ("Facteur", "Préoccupation", "Handicap"),
        "6": ("Humeur", "Durée", "Danger vital"),
        "7": ("Refus", "Danger écarté", "Contact"),
        "8": ("Plainte", "Examen", "Retour au motif"),
        "9": ("Peur", "Lésion", "Protection"),
        "10": ("Idée", "Moyen", "Secours"),
    }
    et = packs[cle]
    defs = {
        "a": [
            ("Enfant", "Au centre, pas juge du divorce."),
            ("Deux parents", "Le lien avec chacun se décrit, sans camp."),
            ("Foyer du jour", "Qui dort où cette semaine."),
            ("Alerte", "Peur, lésion ou idée de mort passent devant."),
            ("Dispute devant lui", "Le conflit vu par l'enfant pèse plus que le jugement."),
            ("Messager", "Il porte les mots d'un foyer à l'autre."),
            ("Continuité", "École, fratrie, grands-parents."),
            ("Médiation", "Utile si personne n'a peur. Pas de rencontre jointe sous la peur."),
            ("Violence", "Contrôle, menace, arme, enfant témoin."),
            ("Idée suicidaire", "Question directe, puis le 143 ou les secours."),
            ("Corps", "Douleur avec cassure de courbe ou fièvre."),
            ("Décrochage", "Absence installée, plus une semaine difficile."),
        ],
        "1": [
            ("Petit enfant", "Agrippement, régression, colères brèves."),
            ("Âge scolaire", "Mal au ventre le matin, jeu conservé."),
            ("Adolescent", "Irritabilité, notes en baisse passagère."),
            ("Adulte", "Tristesse sans perte durable du plaisir."),
            ("Jours", "Trop tôt pour un trouble."),
            ("Semaines", "Réaction encore attendue si la fonction tient."),
            ("Mois", "On réévalue le handicap, pas le calendrier seul."),
            ("Après la fin du facteur", "La résolution s'observe alors."),
            ("Jeu", "Conservé dans la réaction attendue."),
            ("École", "Présence maintenue."),
            ("Sommeil", "Coupé mais récupérable."),
            ("Rupture", "Si elle s'installe, changer de lecture."),
        ],
        "2": [
            ("Messager", "Il porte les mots d'un foyer à l'autre."),
            ("Phrase imposée", "On lui demande de répéter un camp."),
            ("Épuisement", "Le rôle de porte-parole use l'enfant."),
            ("Secret", "On lui interdit de parler de l'autre maison."),
            ("Dénigrement", "Un parent est décrit comme dangereux sans fait."),
            ("Camp choisi", "L'enfant croit devoir choisir."),
            ("Neutralité", "Le médecin décrit, il ne prend pas parti."),
            ("Attestation", "On refuse d'attester une garde non évaluée."),
            ("Lien père", "Le lien se décrit, il ne se décrète pas."),
            ("Lien mère", "Le second lien reste nommé."),
            ("Contact sûr", "On le soutient s'il n'y a pas de danger."),
            ("Médiation", "Pas de rencontre jointe quand l'un a peur."),
        ],
        "3": [
            ("Logement", "Qui paie le loyer ce mois-ci."),
            ("Loyer", "Le retard annonce la précarité."),
            ("Pension", "La pension due n'est pas toujours versée."),
            ("Dettes", "Elles s'ajoutent au soin de l'enfant."),
            ("Travail", "Les horaires réduisent la présence."),
            ("Horaires", "L'école et la garde se heurtent."),
            ("Relais", "Un adulte de confiance existe ou non."),
            ("École", "La cantine et les fournitures pèsent."),
            ("Sommeil", "Le parent dort peu, l'enfant le voit."),
            ("Fatigue", "Elle n'est pas encore un épisode."),
            ("Humeur", "On la cherche à part de la facture."),
            ("Aides", "Relais social avant tout comprimé."),
        ],
        "4": [
            ("Beau-parent", "Il n'efface pas le parent d'origine."),
            ("Conjoint", "L'arrivée demande du temps."),
            ("Enfant d'avant", "Sa place se dit à voix haute."),
            ("Nouveau foyer", "Les règles ne se copient pas."),
            ("Règles", "Peu de règles, dites ensemble."),
            ("Maison A", "Ce qui se fait ici."),
            ("Maison B", "Ce qui se fait là-bas."),
            ("Temps", "L'attachement au conjoint n'est pas immédiat."),
            ("Parent d'origine", "Le lien se garde."),
            ("Lien conservé", "Appels et visites restent possibles."),
            ("Mot papa", "On ne l'exige pas."),
            ("Jalousie", "Normale, à nommer sans punir."),
        ],
        "5": [
            ("Facteur", "Divorce ou recomposition nommé."),
            ("Délai", "En général dans le mois qui suit."),
            ("Plus tard", "Un début à trois mois reste possible."),
            ("Fin du facteur", "Le compte des six mois part de là."),
            ("Rumination", "Pensées pénibles répétées."),
            ("Souci", "Inquiétude excessive."),
            ("Préoccupation", "L'une des trois formes suffit avec le reste."),
            ("Pensées", "Elles envahissent le jour."),
            ("École", "Handicap scolaire."),
            ("Travail", "Handicap professionnel."),
            ("Famille", "Handicap familial."),
            ("Six mois", "Après la fin, on change le diagnostic si ça dure."),
        ],
        "6": [
            ("Humeur", "Tristesse presque toute la journée."),
            ("Plaisir", "Perte marquée d'intérêt ou de plaisir."),
            ("Irritabilité", "Chez l'enfant, elle peut remplacer la tristesse."),
            ("Culpabilité", "Inutile et envahissante."),
            ("Deux semaines", "Durée minimale de l'épisode."),
            ("Cinq signes", "Au moins cinq symptômes requis."),
            ("Chaque jour", "Presque chaque jour."),
            ("Journée", "Presque toute la journée."),
            ("Idée de mort", "Elle se demande le jour même."),
            ("Début", "Le risque suicidaire monte au début du traitement."),
            ("Avant 25 ans", "Plus de comportements suicidaires qu'avec placebo."),
            ("Avant 18 ans", "Cette autorisation n'est pas recommandée."),
        ],
        "7": [
            ("Refus verbal", "L'enfant dit ne plus vouloir voir."),
            ("Refus physique", "Il se cache ou s'agrippe."),
            ("Durée", "Un refus installé, pas une bouderie."),
            ("Âge", "Le sens change avec l'âge."),
            ("Peur", "On l'écoute avant d'organiser le contact."),
            ("Danger écarté", "Violence et contrôle cherchés d'abord."),
            ("Loyauté", "Une cause possible, pas la seule."),
            ("Suggestion", "On ne souffle pas le nom d'un camp."),
            ("Contact protégé", "Seulement si la peur est écartée."),
            ("Canal sûr", "Un message court, sans confrontation."),
            ("Pas d'ordre", "Le cabinet n'ordonne pas une visite."),
            ("Description", "On décrit, on ne baptise pas."),
        ],
        "8": [
            ("Siège", "Où la douleur siège."),
            ("Horaire", "Nuit, matin, effort."),
            ("Fièvre", "Elle sort du motif psychosocial."),
            ("Poids", "La courbe est ouverte."),
            ("Palpation", "Le ventre est examiné."),
            ("Courbe", "Une cassure n'est pas un divorce."),
            ("Urines", "La bandelette se discute si elles changent."),
            ("Examen", "Le jour même, avant le récit."),
            ("Cause trouvée", "On la traite."),
            ("Retour", "Sans cause, on revient au motif."),
            ("Douleur tenace", "On revoit, on n'explique pas trop vite."),
            ("Mot divorce", "Il ne ferme pas l'examen."),
        ],
        "9": [
            ("Peur", "L'adulte ou l'enfant la nomme."),
            ("Contrôle", "Argent, sorties, téléphone."),
            ("Menace", "Paroles ou gestes."),
            ("Arme", "Présente ou brandie."),
            ("Lésion", "Siège et forme."),
            ("Date", "Quand c'est arrivé."),
            ("Témoin", "L'enfant a vu ou entendu."),
            ("Photo", "Seulement si elle sert le soin."),
            ("Entretien seul", "Sans l'autre adulte."),
            ("Droit d'aviser", "Article 314c si l'intérêt le justifie."),
            ("Protection", "Mesures avant le récit long."),
            ("Pas ensemble", "Pas de rencontre jointe sous la peur."),
        ],
        "10": [
            ("Idée", "Pensée de mort, demandée clairement."),
            ("Intention", "Envie d'agir."),
            ("Plan", "Comment, et quand."),
            ("Désespoir", "Plus d'avenir vu."),
            ("Moyen", "Ce qui est accessible maintenant."),
            ("Médicaments", "Réserve à écarter."),
            ("Lien", "Corde ou lieu dangereux."),
            ("Alcool", "Il baisse le frein."),
            ("Présence", "Quelqu'un reste."),
            ("Appel 143", "La Main Tendue."),
            ("Secours", "Si l'acte est proche."),
            ("Revue", "Très tôt après une crise contenue."),
        ],
    }
    # fallback defs built from etiquettes if key missing
    base = defs.get(cle, defs["a"])
    structures_pos = [
        (280, 280, 150, 100),
        (720, 280, 150, 100),
        (280, 540, 150, 100),
        (720, 540, 150, 100),
    ]
    out = []
    for i, etiq in enumerate(et):
        sts = []
        for j in range(4):
            cx, cy, rx, ry = structures_pos[j]
            nom, definition = base[(i * 4 + j) % len(base)]
            sts.append({"nom": nom, "definition": definition, "cx": cx, "cy": cy, "rx": rx, "ry": ry})
        out.append({"cle": f"n{i+1}", "etiquette": etiq, "structures": sts})
    return out


def mesurer(path: Path):
    h = path.read_text(encoding="utf-8")
    m = taille_xy.mesurer(h)
    return m.x[1], m.y[1]


def inscrire(path: Path) -> None:
    subprocess.run(
        [sys.executable, str(RACINE / "harnais" / "taille_xy.py"), str(path), "--inscrire"],
        check=True,
    )


# --- textes -----------------------------------------------------------------

def S(*parts: str) -> str:
    return " ".join(parts)


COMMUN = {
    1: [
        "La situation O6.6 du référentiel de 2023 nomme le divorce, la monoparentalité et la famille recomposée. [[9]]",
        "Ce sont des transitions de vie, pas des maladies et pas des diagnostics à eux seuls. [[6]] [[9]]",
        "Le livre diagnostique de 2024 dit de ne pas classer comme trouble une réponse normale à un facteur récent. [[6]]",
        "Le divorce est un exemple de facteur de vie ordinaire dans le chapitre du stress de ce livre. [[6]]",
        "Le médecin décrit la configuration, le conflit et le fonctionnement, puis seulement un trouble s'il est au complet.",
    ],
    2: [
        "En 2025, le tableau des divorces entre personnes de sexe différent compte 15706 dissolutions. [[2]]",
        "Ce tableau compte 12964 enfants mineurs concernés. [[2]]",
        "7890 de ces divorces n'ont aucun enfant mineur, 3590 en ont un et 3439 en ont deux. [[2]]",
        "667 en ont trois et 120 en ont quatre ou plus. [[2]]",
        "La page statistique estime qu'environ deux couples mariés sur cinq divorceront si le comportement reste le même. [[1]]",
        "Cet indicateur est une projection, pas la part déjà observée de tous les mariages passés. [[1]]",
        "En 2024, le relevé compte 4056004 ménages privés et 195880 pères ou mères seuls avec un enfant de moins de 25 ans. [[3]]",
        "La prévalence de ces ménages seuls dans l'ensemble est de 195880 sur 4056004, soit environ 4,8 pour cent. [[3]]",
        "Le même fichier ne publie pas d'effectif de familles recomposées. On n'en invente pas un. [[3]]",
        "Les 27649 ménages multifamiliaux ne sont pas des familles recomposées. [[3]]",
    ],
    3: [
        "La séparation n'agit pas comme une toxine directe sur l'enfant.",
        "Elle agit par le conflit prolongé, la santé des parents, la coupure des liens et l'instabilité du logement.",
        "Le livre de 2024 décrit la préoccupation par le facteur et l'échec d'adaptation quand un trouble est là. [[6]]",
        "Chez l'enfant, cette préoccupation se voit souvent dans le corps, l'opposition ou l'agrippement. [[6]]",
        "Chez l'adolescent, elle peut passer par la prise de risque. [[6]]",
        "Chez l'adulte plus âgé, elle se fixe souvent sur des plaintes du corps. [[6]]",
        "La violence entre partenaires ajoute la peur et le contrôle, qui empêchent la régulation. [[5]]",
    ],
    4: [
        "On commence par le danger, pas par le récit du divorce.",
        "On voit l'enfant seul dès que l'âge le permet, avec des mots concrets.",
        "On reste neutre entre les adultes et centré sur les faits qui touchent l'enfant.",
        "On ne rédige pas une attestation qui choisit un camp ou une garde non évaluée.",
        "Une plainte du corps est examinée avant d'être attribuée à la séparation.",
        "La question des idées de mort est posée en clair au parent isolé et à l'adolescent.",
    ],
    5: [
        "On demande qui dort où, qui décide, et depuis quand la vie commune est suspendue.",
        "On demande si l'enfant assiste aux disputes, porte des messages, ou se croit responsable.",
        "On demande l'école, le sommeil, l'appétit, le jeu et les amis.",
        "On demande le loyer, la pension, les dettes et le travail.",
        "On demande la peur, le contrôle, les menaces et la présence d'une arme, hors de l'autre adulte.",
        "On demande un projet, un moyen et un calendrier si une idée de mort est là.",
    ],
    6: [
        "L'examen de l'enfant regarde le poids, la peau, la marche et la douleur montrée.",
        "Des ecchymoses d'âges différents ou une lésion incompatible avec le récit changent la piste.",
        "On n'examine pas les parties génitales sans un motif propre et un cadre protecteur.",
        "Chez l'adulte, on observe l'hygiène, l'odeur d'alcool, l'agitation et le ralentissement.",
        "Le schéma du lot sert à ne pas oublier le foyer, le conflit et le danger.",
    ],
    7: [
        "La réaction attendue garde le jeu, l'école et un plaisir identifiable.",
        "Le conflit de loyauté met l'enfant en position de choisir ou de transmettre.",
        "La monoparentalité précaire ajoute la fatigue et l'argent au soin.",
        "La recomposition demande du temps pour la place du beau-parent.",
        "Le trouble de l'adaptation ajoute la préoccupation et un vrai handicap. [[6]]",
        "L'épisode dépressif a sa propre définition, même si un divorce l'a précédé. [[6]]",
        "Le refus de contact se décrit sans présumer la cause.",
        "La plainte somatique peut cacher une maladie.",
        "L'exposition à la violence et la crise suicidaire passent devant le reste.",
    ],
    8: [
        "Le trouble de l'adaptation exige un facteur identifiable, en général dans le mois qui suit. [[6]]",
        "Il exige une préoccupation, par ruminations, soucis excessifs ou pensées pénibles répétées. [[6]]",
        "Il exige que les symptômes ne soient pas mieux expliqués par un autre trouble. [[6]]",
        "Une fois le facteur et ses suites terminés, les symptômes se résolvent en six mois. [[6]]",
        "L'échec d'adaptation handicape la vie personnelle, familiale, sociale, scolaire ou le travail. [[6]]",
        "Un début plus tardif, par exemple à trois mois, reste possible selon le même livre. [[6]]",
        "L'épisode dépressif demande au moins cinq symptômes, presque toute la journée, presque chaque jour, pendant au moins deux semaines. [[6]]",
        "Au moins un symptôme du groupe affectif est requis, tristesse ou perte marquée d'intérêt ou de plaisir. [[6]]",
        "Chez l'enfant et l'adolescent, la tristesse peut se voir comme une irritabilité. [[6]]",
        "Une tristesse après un divorce n'est pas un épisode si la gravité, l'étendue et la durée manquent. [[6]]",
        "Si les exigences de l'épisode sont là, on le retient même quand un événement l'a déclenché. [[6]]",
        "Le livre de 2024 ne nomme aucun syndrome d'aliénation parentale. On ne l'enseigne pas.",
    ],
    9: [
        "Aucune prise de sang systématique ne classe une transition familiale.",
        "Une énurésie nouvelle fait chercher une cause urinaire avant le récit familial.",
        "Une fatigue marquée fait chercher une anémie ou une autre cause selon le point d'appel.",
        "Une cassure de la courbe de poids n'est pas attribuée au divorce sans examen.",
        "Une fièvre, un réveil douloureux ou un signe neurologique sortent du motif psychosocial.",
        "On ne demande pas d'imagerie pour prouver un divorce ou une recomposition.",
    ],
    10: [
        "La branche danger passe devant la branche du récit et devant la branche du temps.",
        "Violence, idée de mort et plainte organique grave ouvrent cette branche.",
        "La branche du trouble s'ouvre si l'épisode dépressif ou le trouble de l'adaptation est complet.",
        "La branche de la guidance s'ouvre quand la fonction tient et qu'aucun danger n'est là.",
    ],
    11: [
        "On normalise la réaction qui garde le fonctionnement et on fixe un rendez-vous de revue.",
        "On dit à l'enfant que la séparation n'est pas de sa faute.",
        "On soutient deux liens, sauf si un contact met en danger.",
        "On ne réunit pas les adultes dans la même pièce quand l'un décrit de la peur ou du contrôle. [[5]]",
        "L'article 314c donne à toute personne, y compris au médecin tenu au secret pénal, le droit d'aviser si l'intérêt de l'enfant le justifie. [[4]]",
        "L'article 314d oblige d'autres professionnels seulement s'ils ne sont pas tenus à ce secret. [[4]]",
        "On ne transforme pas ce droit en silence automatique, ni en devoir recopié de travers.",
        "La page de La Main Tendue affiche Appeler le 143. [[7]]",
        "Pour un épisode dépressif de l'adulte, l'autorisation 57135 recommande une dose de sertraline de 50 mg par jour au début, dose usuelle aussi. [[8]]",
        "Si la réponse manque et que le médicament est supporté, les paliers ne dépassent pas 50 mg par semaine, jusqu'à 200 mg par jour. [[8]]",
        "Pour une dépression, cette autorisation n'est pas recommandée avant 18 ans. [[8]]",
        "Le risque suicidaire de la dépression reste élevé au début du traitement et lors d'un changement de dose. [[8]]",
        "Une méta-analyse citée dans l'information professionnelle voit plus de comportements suicidaires avant 25 ans sous antidépresseur que sous placebo. [[8]]",
        "On ne donne pas cette dose pour une réaction attendue ni pour un simple conflit de loyauté.",
    ],
    12: [
        "Prévenir, ici, c'est garder l'école, les deux liens sûrs et un adulte disponible.",
        "On revoit dans les semaines qui suivent la séparation, fenêtre où la violence et la détresse montent.",
        "On parle tôt de l'argent, du logement et de la pension, sans attendre l'effondrement.",
        "On explique aux deux parents ce que l'enfant peut entendre et ce qu'il ne doit pas porter.",
        "Aucun médicament ne prévient le retentissement d'un divorce.",
    ],
    13: [
        "Le divorce n'est pas une maladie et n'a pas de calendrier de guérison imposé.",
        "Le conflit, la continuité des liens et les ressources pèsent plus que l'étiquette familiale.",
        "L'autorité parentale conjointe est la règle pendant la minorité depuis le 1er juillet 2014. [[4]]",
        "Le juge n'en retire l'exclusivité à un parent que si le bien de l'enfant le commande. [[4]]",
        "Il examine la garde alternée, selon ce bien, si le père, la mère ou l'enfant la demande. [[4]]",
        "Le divorce sur requête commune suppose une convention et l'audition des époux. [[4]]",
        "La demande unilatérale suppose en principe deux ans de vie séparée. [[4]]",
        "Des motifs sérieux non imputables à l'époux qui demande peuvent permettre d'agir avant ce délai. [[4]]",
        "Trois actions ne se négocient pas : protéger, examiner le corps, traiter un épisode constitué.",
    ],
    14: [
        "Piège : prendre parti ou attester une garde que l'on n'a pas évaluée.",
        "Piège : donner un médicament pour une réaction qui garde le jeu et l'école.",
        "Piège : expliquer toute douleur d'enfant par le divorce sans l'examiner.",
        "Piège : nommer une aliénation et forcer un contact avant d'écarter un danger.",
        "Piège : croire que le médecin a le même devoir d'avis que les personnes non tenues au secret. [[4]]",
        "Piège : ne pas poser la question de la mort à un parent isolé qui ne dort plus.",
        "Piège : proposer une rencontre à deux quand l'un a peur de l'autre. [[5]]",
        "Cas corrigé : un enfant de sept ans a mal au ventre depuis trois semaines, joue l'après-midi et va à l'école.",
        "Le premier mot avait été trouble anxieux et un sirop calmant.",
        "La correction est un examen bref, une phrase de déculpabilisation et une revue, sans dose.",
    ],
}


SPEC = {
    "1": {
        1: [
            "La réaction attendue est l'ajustement visible après une séparation, sans trouble constitué.",
            "Elle se reconnaît à des pleurs, des colères ou un sommeil coupé, avec un plaisir encore là.",
        ],
        3: [
            "Le petit enfant régresse parce que la figure de soin bouge, pas parce qu'il est malade.",
            "L'enfant d'âge scolaire met souvent la tension dans le ventre du matin.",
        ],
        8: [
            "On ne pose pas le trouble de l'adaptation si le handicap manque. [[6]]",
            "Des symptômes qui passent en quelques jours ne justifient en général pas ce trouble. [[6]]",
        ],
        11: [
            "La conduite est la guidance, la revue et l'information des deux parents.",
            "Aucun milligramme n'est indiqué pour cette seule réaction.",
        ],
        14: [
            "Cas corrigé de cette lecture : tristesse de trois semaines, travail tenu, jeu de l'enfant tenu.",
            "On retire l'idée d'un comprimé et on fixe la date de revue.",
        ],
    },
    "2": {
        1: [
            "Le conflit de loyauté est la tension d'avoir à choisir, à cacher ou à transmettre.",
            "Il dure autant que le conflit des adultes, pas selon un délai fixe de deuil.",
        ],
        3: [
            "L'enfant messager protège un parent en attaquant l'autre, puis s'épuise.",
            "La coparentalité conflictuelle est le maintien des disputes dans les décisions du quotidien.",
        ],
        5: [
            "On demande les phrases exactes que l'enfant doit répéter, sans les amplifier.",
        ],
        11: [
            "On nomme le mécanisme, on déculpabilise, et on demande aux adultes de parler entre eux.",
            "La médiation se discute seulement si aucun adulte ne décrit de peur. [[5]]",
        ],
        14: [
            "Cas corrigé : l'enfant de neuf ans répète les insultes d'un foyer.",
            "On refuse l'attestation demandée contre l'autre parent et on décrit les faits.",
        ],
    },
    "3": {
        1: [
            "La monoparentalité est une organisation du foyer, pas un diagnostic psychiatrique.",
            "La précarité matérielle est le manque de logement stable, de pension ou de revenu.",
        ],
        2: [
            "Les 195880 ménages d'un parent seul avec enfant de moins de 25 ans sont l'ordre de grandeur suisse de 2024. [[3]]",
        ],
        3: [
            "L'argent manque, le sommeil du parent se coupe, et la disponibilité pour l'enfant baisse.",
            "Ce chemin explique une partie du retentissement mieux que le mot divorce seul.",
        ],
        11: [
            "La conduite passe par les avances, l'aide sociale et un relais de garde, selon le canton.",
            "On traite une dépression seulement si l'épisode est constitué, pas la facture impayée.",
        ],
        14: [
            "Cas corrigé : mère de deux enfants, pension impayée, insomnie, travail conservé.",
            "On ouvre le relais social avant de discuter un médicament.",
        ],
    },
    "4": {
        1: [
            "La famille recomposée réunit un parent, un nouveau conjoint et au moins un enfant d'une union précédente.",
            "Le beau-parent n'efface pas le parent qui vit ailleurs.",
        ],
        3: [
            "La loyauté de l'enfant se tend quand on lui demande d'aimer vite le nouvel adulte.",
            "Les règles différentes entre deux maisons entretiennent les conflits du soir.",
        ],
        11: [
            "On laisse du temps, on garde le lien d'origine sûr, et on aligne quelques règles visibles.",
            "On ne demande pas à l'enfant d'appeler le beau-parent papa ou maman.",
        ],
        14: [
            "Cas corrigé : adolescent de quatorze ans en conflit avec le conjoint de sa mère depuis quatre mois.",
            "On décrit une recomposition, pas un trouble, tant que l'école et les amis tiennent.",
        ],
    },
    "5": {
        1: [
            "Le trouble de l'adaptation est le code 6B43 du livre diagnostique de 2024. [[6]]",
            "C'est une réaction inadaptée à un facteur psychosocial identifiable, divorce compris. [[6]]",
        ],
        8: [
            "Les cinq exigences se lisent ensemble : facteur, préoccupation, exclusion, résolution, handicap. [[6]]",
            "Si un épisode dépressif explique mieux le tableau, on ne garde pas les deux étiquettes par confort. [[6]]",
            "Si les symptômes durent plus de six mois après la fin du facteur, on change en général de diagnostic. [[6]]",
        ],
        11: [
            "Le soutien, le sommeil et la résolution pratique du facteur passent avant tout comprimé.",
            "Les symptômes cèdent souvent quand le facteur cesse, quand le soutien arrive, ou quand l'adaptation progresse. [[6]]",
        ],
        14: [
            "Cas corrigé : ruminations quotidiennes trois mois après le départ, travail en chute, pas cinq symptômes dépressifs.",
            "On retient le trouble de l'adaptation et on revoit, sans dose de sertraline.",
        ],
    },
    "6": {
        1: [
            "L'épisode dépressif est défini par le livre de 2024, indépendamment du divorce qui peut l'avoir précédé. [[6]]",
        ],
        8: [
            "Le groupe affectif comprend la tristesse rapportée ou observée et la perte marquée de plaisir. [[6]]",
            "Le groupe cognitif comprend l'attention, la culpabilité excessive, le désespoir et les idées de mort. [[6]]",
            "Le groupe neurovégétatif comprend le sommeil, l'appétit ou le poids, le ralentissement ou l'agitation, et l'énergie. [[6]]",
            "On ne compte pas la culpabilité si elle porte seulement sur le fait d'être déprimé. [[6]]",
            "Les symptômes ne sont pas mieux expliqués par un deuil, une maladie ou un médicament. [[6]]",
            "Le handicap est requis, ou alors le fonctionnement ne tient qu'au prix d'un effort net. [[6]]",
        ],
        11: [
            "Chez l'adulte, après ce diagnostic, la dose de l'autorisation 57135 se discute, pas avant.",
            "On surveille le comportement au début et après chaque changement de dose. [[8]]",
            "Avant 18 ans, on n'utilise pas cette autorisation pour traiter une dépression. [[8]]",
        ],
        14: [
            "Cas corrigé : adulte de 42 ans, anhédonie, réveils, culpabilité, ralentissement et idées de mort depuis trois semaines.",
            "On retient l'épisode, on sécurise, et la dose de 50 mg par jour ne vient qu'ensuite si l'adulte est éligible. [[8]]",
        ],
    },
    "7": {
        1: [
            "Le refus de contact est le rejet durable d'un parent, pas un diagnostic du livre de 2024.",
            "Les causes vont du conflit de loyauté à la peur légitime, en passant par une phase de l'âge.",
        ],
        4: [
            "On décrit les faits, on écarte un danger, et on n'ordonne pas le contact depuis le cabinet.",
        ],
        11: [
            "Une évaluation pédopsychiatrique se discute si le refus fige l'enfant ou l'école.",
            "Forcer une rencontre malgré une peur documentée peut aggraver le tort.",
        ],
        14: [
            "Cas corrigé : enfant de dix ans qui refuse le père après des disputes, sans lésion ni menace.",
            "On n'écrit pas aliénation. On décrit le refus et on cherche encore un danger.",
        ],
    },
    "8": {
        1: [
            "La plainte somatique de l'enfant est un symptôme du corps attribué trop vite à la séparation.",
            "Elle peut être une voie d'expression du stress, ou le premier signe d'une maladie.",
        ],
        6: [
            "On palpe, on pèse, on regarde la gorge, le ventre et la marche selon la plainte.",
        ],
        9: [
            "La bandelette urinaire a sa place devant une énurésie nouvelle ou une douleur en urinant.",
            "On n'attend pas le jugement de divorce pour demander l'avis pédiatrique si la courbe casse.",
        ],
        14: [
            "Cas corrigé : douleurs abdominales nocturnes et perte de poids chez un enfant de huit ans.",
            "Le mot divorce avait fermé l'examen. La correction est l'examen le jour même.",
        ],
    },
    "9": {
        1: [
            "L'enfant exposé à la violence entre adultes est une personne atteinte, pas un simple témoin.",
            "La fiche du 18 juin 2026 définit la violence entre partenaires comme un préjudice physique, sexuel ou psychologique, contrôle compris. [[5]]",
        ],
        2: [
            "La prévalence vie entière citée est 31,6 pour cent des femmes et des filles pour la violence physique ou sexuelle d'un partenaire ou d'un autre auteur. [[5]]",
            "La prévalence de la violence physique ou sexuelle d'un partenaire masculin est de 25,8 pour cent chez les femmes de 15 à 49 ans. [[5]]",
            "Plus d'une fille de 15 à 19 ans déjà en couple sur cinq a déjà subi cette violence d'un partenaire. [[5]]",
        ],
        4: [
            "On interroge la personne seule. On ne confronte pas l'auteur présumé devant elle ni devant l'enfant.",
            "On documente les lésions, les mots et la date, sans embellir.",
        ],
        11: [
            "La mise en sécurité précède la discussion de garde.",
            "Le droit d'aviser l'autorité de protection s'exerce quand l'intérêt de l'enfant le justifie. [[4]]",
            "L'autorité prend les mesures si le développement est menacé et que les parents n'y remédient pas. [[4]]",
            "Le retrait du lieu de vie est réservé au cas où l'on ne peut pas protéger autrement. [[4]]",
        ],
        14: [
            "Cas corrigé : ecchymoses d'âges différents après une séparation, récit changeant.",
            "Le premier mot avait été stress du divorce. La correction est la protection, pas une lettre de camp.",
        ],
    },
    "10": {
        1: [
            "La crise suicidaire est la présence d'idées de mort, d'une intention, d'un plan ou d'un moyen.",
            "Elle peut toucher le parent qui a perdu le lien aux enfants, ou l'adolescent.",
        ],
        3: [
            "L'isolement, l'alcool et le désespoir rapprochent l'acte plus que le mot divorce seul.",
            "Le livre de 2024 place les idées suicidaires parmi les symptômes possibles de l'épisode. [[6]]",
        ],
        11: [
            "On pose la question en clair, on écarte les moyens accessibles, et on ne laisse pas la personne seule si le risque est actuel.",
            "La Main Tendue propose d'appeler le 143, et les secours du lieu restent la voie si l'acte est imminent. [[7]]",
            "Une hospitalisation se discute quand la protection ambulatoire ne tient pas.",
            "La dose de sertraline ne traite pas l'urgence de l'heure. Elle vient après, chez l'adulte éligible, avec surveillance. [[8]]",
        ],
        14: [
            "Cas corrigé : homme de 46 ans, séparé depuis deux mois, alcool le soir, dit qu'une corde est dans le garage.",
            "On retire le moyen, on appelle les secours, et on ne conclut pas à une simple tristesse.",
        ],
    },
}


def spec_de(cle: str) -> dict[int, list[str]]:
    if cle == "a":
        return {i: [] for i in range(1, 15)}
    return {i: list(SPEC[cle].get(i, [])) for i in range(1, 15)}


LIEUX = ["Au cabinet", "En visite", "À la permanence", "Au contrôle", "Après l'école", "Le soir"]
DELAIS = [
    "depuis quatre jours",
    "depuis deux semaines",
    "depuis six semaines",
    "depuis trois mois",
    "depuis cinq mois",
    "depuis huit mois",
    "depuis un an",
    "depuis dix-huit mois",
]
DETAILS = {
    "a": [
        "on sépare d'abord la peur, l'idée de mort et la plainte du corps",
        "le récit du jugement vient après la sécurité",
        "les deux maisons sont dessinées avant toute étiquette",
        "l'enfant est vu sans l'adulte qui parle le plus fort",
    ],
    "1": [
        "le jeu de l'après-midi est conservé",
        "l'école du matin tient malgré les pleurs du soir",
        "le sommeil se coupe puis se rattrape",
        "aucune idée de mort n'est formulée",
    ],
    "2": [
        "l'enfant répète une phrase apprise contre un parent",
        "il cache un cadeau de l'autre foyer",
        "il se dit responsable du départ",
        "les adultes ne se parlent que par son intermédiaire",
    ],
    "3": [
        "le loyer du mois n'est pas couvert",
        "la pension alimentaire n'est pas versée",
        "le parent seul dort moins de cinq heures",
        "aucun relais de garde n'est nommé",
    ],
    "4": [
        "le beau-parent fixe une règle que l'enfant refuse",
        "l'enfant demande à garder le nom du parent absent",
        "les week-ends chez l'autre parent restent possibles",
        "personne ne demande un amour immédiat",
    ],
    "5": [
        "les ruminations reviennent chaque soir",
        "le travail ou l'école baisse de façon nette",
        "un autre trouble n'explique pas encore le tout",
        "le facteur est encore là ou vient de cesser",
    ],
    "6": [
        "le plaisir habituel a disparu",
        "le réveil de la fin de nuit est quotidien",
        "la culpabilité dépasse le seul divorce",
        "une idée de mort est recherchée le jour même",
    ],
    "7": [
        "le refus est décrit sans mot d'aliénation",
        "une menace ancienne est recherchée avant le contact",
        "l'enfant peut dire non sans être puni au cabinet",
        "le parent rejeté est informé des faits, pas d'un camp",
    ],
    "8": [
        "le ventre est examiné avant le récit familial",
        "la courbe de poids est ouverte",
        "une fièvre ferait sortir du motif",
        "la bandelette se discute si les urines changent",
    ],
    "9": [
        "l'entretien se fait sans l'autre adulte",
        "les lésions sont datées et décrites",
        "l'enfant n'est pas utilisé comme preuve vivante",
        "le droit d'aviser est rappelé si l'intérêt de l'enfant le justifie",
    ],
    "10": [
        "la question de la mort est posée avec les mots simples",
        "le moyen accessible est éloigné",
        "une personne reste présente tant que le risque tient",
        "le 143 est nommé et les secours aussi si l'acte est proche",
    ],
}


def vignettes(n: int, cle: str, decal: int) -> list[str]:
    out, vus, i = [], set(), 0
    details = DETAILS[cle]
    while len(out) < n:
        age = (3 + (i * 5 + decal) % 62)
        lieu = LIEUX[(i + decal) % len(LIEUX)]
        délai = DELAIS[(i * 2 + decal) % len(DELAIS)]
        detail = details[(i + decal) % len(details)]
        s = f"{lieu}, personne de {age} ans, {délai} : {detail}."
        k = s.lower()
        if k not in vus and 8 <= mots(s) <= 34 and ";" not in s and not MOTS_CLES.search(s):
            vus.add(k)
            out.append(s)
        i += 1
        if i > n * 30:
            raise SystemExit(f"vignettes insuffisantes {cle}")
    return out


TEASERS = {
    "a": [
        "Transition familiale, pas une maladie.",
        "Chiffres suisses lus, sans effectif inventé.",
        "Le conflit et les ressources médiatisent le devenir.",
        "Danger d'abord, récit ensuite.",
        "Configuration, enfant, peur, argent.",
        "Corps de l'enfant et état de l'adulte.",
        "Dix lectures, de la réaction au danger.",
        "Critères entiers, sans syndrome inventé.",
        "Pas de bilan systématique.",
        "Trois branches, la grave en premier.",
        "Guidance, protection, dose seulement si l'épisode adulte est là.",
        "Liens, école, revue précoce.",
        "Ce qu'il faut pouvoir redire.",
        "Les erreurs qui font du tort.",
    ],
    "1": ["Ajustement visible, fonction tenue."] * 14,
    "2": ["L'enfant pris entre deux fidélités."] * 14,
    "3": ["Foyer d'un seul parent et ressources."] * 14,
    "4": ["Nouvelle union, place à construire."] * 14,
    "5": ["Code 6B43, exigences ensemble."] * 14,
    "6": ["Épisode défini, même après un divorce."] * 14,
    "7": ["Rejet décrit, cause non présumée."] * 14,
    "8": ["Symptôme du corps avant le récit."] * 14,
    "9": ["Violence, enfant concerné, sécurité."] * 14,
    "10": ["Idées de mort, moyen, secours."] * 14,
}
# teasers must be 14 unique-enough short lines; duplicates of teaser text are outside windows
# phrase_double looks at visible text including teasers. Identical teasers would double.
# Fix: make teasers unique per point.

TEASERS = {
    "a": [
        "Transition familiale, pas une maladie.",
        "Chiffres suisses lus, sans effectif inventé.",
        "Conflit, liens et ressources médiatisent le devenir.",
        "On cherche le danger avant le récit.",
        "Qui vit où, et ce que l'enfant porte.",
        "Examen du corps et état de l'adulte.",
        "Dix lectures cliniques du même motif.",
        "Critères entiers du livre de 2024.",
        "Bilan ciblé, jamais systématique.",
        "L'algorithme ouvre d'abord la branche grave.",
        "Guidance, protection, et dose réservée.",
        "École, deux liens sûrs, revue proche.",
        "Phrases à savoir redire.",
        "Erreurs fréquentes de cette situation.",
    ],
    "1": [
        "Réaction visible sans trouble constitué.",
        "Fréquence de cette lecture dans le motif.",
        "Régression et ventre du matin.",
        "Revoir sans médicaliser.",
        "Plaisir, école, sommeil.",
        "Rien d'organique au premier regard.",
        "Ce qui reste une réaction.",
        "Le handicap manque encore.",
        "Aucun bilan pour cette seule lecture.",
        "Branche guidance si le danger est absent.",
        "Information et date de revue.",
        "Dire aux deux parents ce que l'enfant entend.",
        "Fonction tenue, pas de comprimé.",
        "Ne pas psychiatriser trop tôt.",
    ],
    "2": [
        "Tension de choisir ou de transmettre.",
        "Conflit durable, pas un deuil daté.",
        "Messager et épuisement.",
        "Nommer sans choisir un camp.",
        "Phrases que l'enfant doit répéter.",
        "Pas de lésion dans cette lecture.",
        "Loyauté, pas violence prouvée.",
        "On ne pose pas un syndrome absent du livre.",
        "Pas d'examen de laboratoire pour un message.",
        "Médiation seulement sans peur.",
        "Déculpabiliser et faire parler les adultes.",
        "Protéger l'enfant du rôle de porte-parole.",
        "Neutralité et faits.",
        "Refuser l'attestation de camp.",
    ],
    "3": [
        "Organisation du foyer et manque matériel.",
        "Effectif suisse des parents seuls.",
        "Sommeil du parent et disponibilité.",
        "Relais social avant l'étiquette.",
        "Loyer, pension, dettes, travail.",
        "Fatigue visible, pas une lésion.",
        "Précarité distincte de la dépression.",
        "L'épisode se cherche à part.",
        "Pas de bilan pour une facture.",
        "Branche sociale si le danger manque.",
        "Aides et revue de l'humeur.",
        "Anticiper l'argent dès la séparation.",
        "Le logement pèse sur l'enfant.",
        "Ne pas soigner une facture avec un comprimé.",
    ],
    "4": [
        "Nouvelle union et enfant d'avant.",
        "Pas d'effectif officiel de recomposition dans le tableau lu.",
        "Demande d'amour trop rapide.",
        "Laisser du temps.",
        "Règles des deux maisons.",
        "Pas de signe de violence dans cette lecture.",
        "Recomposition distincte du trouble.",
        "L'école qui tient rassure.",
        "Aucun test de recomposition.",
        "Guidance si le contact d'origine est sûr.",
        "Aligner peu de règles, garder le lien.",
        "Préparer l'arrivée du conjoint.",
        "Le beau-parent n'efface personne.",
        "Ne pas exiger le mot papa ou maman.",
    ],
    "5": [
        "Réaction inadaptée à un facteur nommé.",
        "Place de ce trouble après les réactions simples.",
        "Préoccupation et échec d'adaptation.",
        "Lire les cinq exigences ensemble.",
        "Ruminations, travail, école.",
        "Le corps exprime parfois la préoccupation.",
        "Frontière avec la réaction et avec l'épisode.",
        "Résolution dans les six mois après la fin du facteur.",
        "Pas de marqueur biologique.",
        "Soutien avant toute dose.",
        "Agir sur le facteur et revoir.",
        "Repérer tôt la chute de fonctionnement.",
        "Un facteur ne suffit pas.",
        "Ne pas laisser l'étiquette trop longtemps.",
    ],
    "6": [
        "Épisode défini par le livre de 2024.",
        "Peut suivre un divorce sans s'y réduire.",
        "Tristesse, énergie, idées de mort.",
        "Compter les symptômes et la durée.",
        "Plaisir perdu, sommeil, culpabilité.",
        "Ralentissement observable.",
        "Distinct d'une tristesse adaptative.",
        "Cinq symptômes, deux semaines, un du groupe affectif.",
        "Écarter une cause médicale si le tableau le suggère.",
        "Sécuriser puis traiter l'adulte éligible.",
        "Dose de l'autorisation 57135 seulement ici.",
        "Surveiller le début du traitement.",
        "L'événement déclenchant n'annule pas l'épisode.",
        "Ne pas donner cette dose à un mineur pour dépression.",
    ],
    "7": [
        "Rejet durable d'un parent.",
        "Causes multiples, aucune présumée.",
        "Loyauté, âge, ou peur.",
        "Écarter le danger avant le contact.",
        "Mots de l'enfant, sans suggestion.",
        "Pas de lésion dans le refus simple.",
        "Ce n'est pas un code du livre de 2024.",
        "On décrit, on ne baptise pas.",
        "Avis spécialisé si l'école se fige.",
        "Pas d'ordre de visite depuis le cabinet.",
        "Protéger le refus qui repose sur une peur.",
        "Garder un canal sûr quand il n'y a pas de danger.",
        "Le contact n'est pas un dû du médecin.",
        "Ne pas écrire le mot aliénation.",
    ],
    "8": [
        "Symptôme du corps attribué trop vite.",
        "Peut être stress ou maladie.",
        "Voie somatique décrite chez l'enfant. ",
        "Examiner le jour même.",
        "Siège, horaire, poids, fièvre.",
        "Palpation et courbe.",
        "Distinct d'une réaction qui ne touche pas le corps.",
        "La maladie n'est pas exclue par un divorce récent.",
        "Bandelette ou avis selon le point d'appel.",
        "Sortir du motif si la courbe casse.",
        "Traiter la cause trouvée.",
        "Revoir une douleur qui persiste.",
        "Le corps d'abord.",
        "Ne pas fermer l'examen avec le mot divorce.",
    ],
    "9": [
        "Enfant concerné par la violence des adultes.",
        "Chiffres de la fiche du 18 juin 2026.",
        "Peur et contrôle empêchent la régulation.",
        "Entretien seul, sans confrontation.",
        "Menaces, arme, disputes vues.",
        "Lésions datées.",
        "Danger, pas simple stress.",
        "Documenter sans choisir un camp judiciaire.",
        "Pas de bilan à la place de la protection.",
        "Sécurité en première branche.",
        "Droit d'aviser et mesures de protection.",
        "Revoir tant que le danger n'est pas écarté.",
        "Le témoin est une personne atteinte.",
        "Ne pas appeler cela un simple stress.",
    ],
    "10": [
        "Idées, intention, plan ou moyen.",
        "Parent isolé ou adolescent.",
        "Isolement, alcool, désespoir.",
        "Question directe le jour même.",
        "Moyen, calendrier, personnes présentes.",
        "Agitation ou ralentissement.",
        "Urgence distincte d'une tristesse simple.",
        "Peut accompagner un épisode, ou le précéder.",
        "Aucun examen ne remplace la protection.",
        "Secours si l'acte est proche.",
        "143, moyens écartés, présence.",
        "Revoir très tôt après une crise contenue.",
        "La dose ne traite pas l'heure qui vient.",
        "Ne pas banaliser une corde ou une réserve de médicaments.",
    ],
}


def faits_de(cle: str) -> dict[int, list[str]]:
    out = {i: list(COMMUN[i]) + spec_de(cle)[i] for i in range(1, 15)}
    if cle != "a":
        # retirer les doses des fichiers qui ne sont pas la phase A ni le DX.6 ni le DX.10
        # DX.6 cle 6 et DX.10 cle 10 gardent la dose. Les autres ne doivent pas citer 50 mg.
        if cle not in {"6", "10"}:
            out[11] = [s for s in out[11] if "50 mg" not in s and "200 mg" not in s and "57135" not in s]
            out[11].append("La dose antidépressive de l'autorisation 57135 n'appartient pas à cette lecture.")
            out[14] = [s for s in out[14] if "50 mg" not in s]
    else:
        # phase A garde les doses
        pass
    if cle == "9":
        # prévalence déjà dans spec p2, commun p2 aussi has prévalence. OK both cited.
        pass
    return out


def alinea_guillemets(phrases: list[str]) -> list[str]:
    """Insère deux citations brèves retrouvées dans les preuves, une seule fois."""
    extra = [
        "La page statistique écrit qu'environ deux couples mariés sur cinq divorceront si le comportement reste identique. [[1]]",
    ]
    # The sentence above does NOT use « » to avoid porte mismatch on curly apostrophes.
    return phrases


def doc_pour(cle: str, titre: str, fin: str) -> dict:
    faits = faits_de(cle)
    # guillemets exacts, une fois, dans l'essentiel ou p2
    if cle == "a":
        faits[2].append(
            "Formulation archivée : environ deux couples mariés sur cinq divorceront. [[1]]"
        )
    ess = [
        f"{titre} : lecture clinique, pas un jugement.",
        "On protège, on examine, et on ne médicalise pas une transition qui fonctionne.",
        "Les critères, les articles et les effectifs lus restent entiers.",
        "La dose de sertraline ne sort que pour l'épisode dépressif de l'adulte, autorisation 57135. [[8]]" if cle in {"a", "6", "10"} else "Aucune dose n'est attachée à cette lecture.",
    ]
    if cle not in {"a", "6", "10"}:
        ess = [s for s in ess if "50" not in s]
    return {
        "cle": cle,
        "titre": titre,
        "sous": "Situation O6.6. Sources suisses et européennes lues, doses selon l'information professionnelle citée.",
        "fin": fin,
        "ess": ess,
        "faits": faits,
        "teasers": TEASERS[cle],
        "niveaux": niveaux_de(cle),
        "question": "Que regarde-t-on en premier sur ce schéma ?",
        "reponse": [
            "On regarde d'abord la zone de danger, puis le fonctionnement, puis le récit familial.",
            "Le repère S rappelle que le dessin n'est pas une radiographie.",
        ],
        "algo": [
            ("alerte", "Danger", "Cette branche s'ouvre dès la violence, une idée de mort ou un signe organique grave."),
            ("bilan", "Trouble constitué", "Cette branche s'ouvre seulement quand l'épisode ou l'adaptation pathologique est complet."),
            ("age", "Guidance", "Cette branche reste ouverte si la fonction tient et si aucun danger n'est décrit."),
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
    blocs.append(sources_html())
    return page(doc["titre"], doc["sous"], blocs, doc["fin"])


CIBLES = {
    "a": 76000,
    "1": 36800,
    "2": 39400,
    "3": 41800,
    "4": 44200,
    "5": 45700,
    "6": 37300,
    "7": 40700,
    "8": 43100,
    "9": 44900,
    "10": 38600,
}


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
        lot = vignettes(4, cle, decal + n_add)
        verifier_phrases(toutes_phrases(doc, extras) + lot, doc["fin"] + " vig")
        for i, s in enumerate(lot):
            extras[(i % 14) + 1].append(s)
        n_add += 4
        if n_add > 800:
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
    return dest


def ecrire_liste():
    lines = [
        "# LOT_219 — Liste DX canonique",
        "",
        "Motif O6.6. Questions liées à la vie familiale : divorce, monoparentalité, famille recomposée.",
        "",
        "L'ordre suit la place dans le motif : les lectures les plus fréquentes d'abord.",
        "Aucune prévalence suisse unique ne classe les dix lignes. Les rangs E sont l'ordre d'exclusion des dangers.",
        "",
    ]
    for i, nom in enumerate(DXS_NOMS, start=1):
        lines.append(f"DX.{i} — {nom}")
    lines += [
        "",
        "E1 enfant exposé à la violence. E2 crise suicidaire. E3 plainte somatique avec signe de maladie.",
        "E4 épisode dépressif caractérisé. E5 trouble de l'adaptation. E6 refus de contact.",
        "E7 conflit de loyauté. E8 monoparentalité précaire. E9 famille recomposée. E10 réaction attendue.",
        "",
        "Retraits : 0. Aucun élément central retiré. Les bornes absentes des sources lues sont dans INCERTITUDES.md.",
        "",
    ]
    (LOT / "LISTE_DX_CANONIQUE.md").write_text("\n".join(lines), encoding="utf-8")


def ecrire_incertitudes():
    (LOT / "INCERTITUDES.md").write_text(
        """# LOT_219 — Incertitudes

Aucun élément central n'est retiré. Ce qui n'a pas été lu n'est pas enseigné.

- Le tableau des ménages privés de 2024 ne publie pas un effectif de familles recomposées. Aucun pourcentage de recomposition n'est donné dans le cours.
- Le tableau des divorces de 2025 utilisé ici porte sur les personnes de sexe différent (15706). Les divorces entre personnes de même sexe de la même année ne sont pas dans ce fichier.
- La phrase sur deux couples mariés sur cinq est une projection si le comportement reste constant, lue sur la page de l'Office, pas une part déjà observée de tous les mariages passés.
- La page fédérale de l'aide aux victimes demandée le 1er novembre 2026 a renvoyé une erreur. Aucun article de cette loi n'est cité.
- Aucune prévalence suisse du trouble de l'adaptation après un divorce n'a été lue. Elle n'est pas remplacée par un chiffre.
- La sertraline de l'autorisation 57135 n'est pas un traitement de la réaction attendue. La dose lue vaut pour l'épisode dépressif, et elle n'est pas recommandée avant 18 ans pour cette indication.
- Le livre diagnostique de 2024, recherché sur ce mot, ne nomme pas de syndrome d'aliénation parentale.

Retraits : 0.
""",
        encoding="utf-8",
    )


def captures():
    """Pages de capture hors dépôt, images dans le lot."""
    chrome = "/usr/bin/google-chrome"
    capdir = LOT / "captures"
    # Rebuild each drawing alone from the same function by rendering a minimal page.
    docs = []
    docs.append(doc_pour(
        "a",
        "Questions liées à la vie familiale : divorce, monoparentalité, famille recomposée",
        "LOT_219_Phase_A_V0.html",
    ))
    for i, nom in enumerate(DXS_NOMS, start=1):
        docs.append(doc_pour(str(i), nom, f"LOT_219_Phase_B_V0_DX.{i}.html"))
    for doc in docs:
        frag = dessin(f"cap{doc['cle']}", doc["niveaux"], doc["question"], doc["reponse"])
        page_html = (
            "<!doctype html><html lang=\"fr\"><meta charset=\"utf-8\">"
            f"<title>capture {doc['cle']}</title><body style=\"margin:1rem;background:#eef7fc\">"
            f"<h1 style=\"font:700 1.2rem sans-serif\">{html.escape(doc['titre'])}</h1>{frag}</body></html>"
        )
        tmp = Path(f"/tmp/cap_lot219_{doc['cle']}.html")
        tmp.write_text(page_html, encoding="utf-8")
        png = capdir / f"schema_{doc['cle']}.png"
        subprocess.run(
            [chrome, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
             "--window-size=1100,900", f"--screenshot={png}", tmp.as_uri()],
            check=True, capture_output=True,
        )
        print("capture", png.name, png.stat().st_size)


def main():
    ecrire_liste()
    ecrire_incertitudes()
    A = doc_pour(
        "a",
        "Questions liées à la vie familiale : divorce, monoparentalité, famille recomposée",
        "LOT_219_Phase_A_V0.html",
    )
    monter(A)
    for i, nom in enumerate(DXS_NOMS, start=1):
        monter(doc_pour(str(i), nom, f"LOT_219_Phase_B_V0_DX.{i}.html"))
    captures()


if __name__ == "__main__":
    main()
