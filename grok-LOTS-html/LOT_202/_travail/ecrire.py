#!/usr/bin/env python3
"""Écrit LOT_202 (O4.1). Les phrases cliniques sont dans ce fichier. Les preuves sont dans evidence/."""
from __future__ import annotations

import html
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
LOT = RACINE / "grok-LOTS-html" / "LOT_202"
EV = LOT / "evidence"
CAP = LOT / "captures"
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

AGES = [14, 15, 16, 17, 19, 21, 24, 27, 31, 36, 42, 48, 55, 62, 68]
SPORTS = [
    "la course", "le football", "le basket", "le tennis", "le ski", "la natation",
    "le volley", "le judo", "le cyclisme", "la gymnastique", "le handball", "la danse",
]
LIEUX = [
    "au cabinet", "au bord du terrain", "aux urgences calmes", "en visite de contrôle",
    "à l'infirmerie du club", "après l'entraînement",
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


def fenetre(wid: str, titre: str, corps: str) -> str:
    return (
        f'<div id="{wid}" popover class="fenetre"><div class="barre"><span>{e(titre)}</span>'
        f'<button type="button" popovertarget="{wid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">{corps}</div></div>'
    )


def paras(lignes: list[str]) -> str:
    return "".join(f"<p>{riche(s)}</p>" for s in lignes)


def algo(nom: str, portes: list[tuple[str, str, str]]) -> str:
    """portes: (suffixe, libellé bouton, phrase)."""
    radios = []
    labels = []
    pans = []
    for i, (suf, lib, phrase) in enumerate(portes):
        iid = f"{nom}-{suf}"
        chk = " checked" if i == 0 else ""
        radios.append(f'<input class="r-{suf}" type="radio" name="{nom}" id="{iid}"{chk}>')
        labels.append(f'<label for="{iid}">{e(lib)}</label>')
        pans.append(
            f'<div class="pan pan-{suf}"><svg viewBox="0 0 800 180" role="img">'
            f'<rect class="bo" x="24" y="30" width="752" height="120" rx="16"/>'
            f'<text x="48" y="100" font-size="28" fill="#14303b">{e(lib)}</text></svg>'
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
    ("#f3cfc3", "#a85b4a"),
    ("#b7e3d8", "#0f6e62"),
    ("#c9d8f2", "#24506a"),
]


def dessin(did: str, niveaux: list[dict], question: str, reponse: list[str]) -> str:
    cles = [n["cle"] for n in niveaux]
    radios = []
    labels = []
    plans = []
    notes = []
    legs = []
    for i, n in enumerate(niveaux):
        chk = " checked" if i == 0 else ""
        radios.append(
            f'<input class="sr" type="radio" name="{did}-niv" id="{did}-{n["cle"]}"{chk}/>'
        )
        labels.append(f'<label for="{did}-{n["cle"]}">{e(n["etiquette"])}</label>')
        zones = []
        pastilles = []
        items = []
        for j, st in enumerate(n["structures"], start=1):
            fill, stroke = COULEURS[j - 1]
            d = ellipse(st["cx"], st["cy"], st["rx"], st["ry"])
            defin = e(st["definition"])
            nom = e(st["nom"])
            zones.append(
                f'<g class="zone" tabindex="0" role="button" data-nom="{nom}">'
                f"<title>{nom}. {defin}</title>"
                f'<path class="vis" d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="2"/></g>'
            )
            left = st["cx"] / 10
            top = st["cy"] / 7.6
            pastilles.append(f'<span class="pastille" style="left:{left:.1f}%;top:{top:.1f}%">{j}</span>')
            items.append(f"<li><span>{j}</span> {nom}</li>")
        plans.append(
            f'<div class="niv niv-{n["cle"]}"><div class="cadre">'
            f'<svg viewBox="0 0 1000 760" role="img"><title>{e(n["etiquette"])}</title>'
            f'{"".join(zones)}</svg>'
            f'{"".join(pastilles)}'
            f'<span class="repere" style="left:9%;top:14%" title="Droite du patient, à gauche de l&#x27;écran">D</span>'
            f"</div></div>"
        )
        notes.append(
            f'<p class="note note-{n["cle"]}">Au niveau {e(n["etiquette"])}, la droite du patient est à gauche de l&#x27;écran. Ce dessin n&#x27;est pas une radiographie.</p>'
        )
        legs.append(f'<ol class="leg leg-{n["cle"]}">{"".join(items)}</ol>')
    rep = "".join(f"<p>{riche(s)}</p>" for s in reponse)
    return (
        f'<div data-dessinateur="1" id="{did}">{"".join(radios)}'
        f'<div class="barre" role="tablist">{"".join(labels)}</div>'
        f'<div class="plan">{"".join(plans)}</div>'
        f'{"".join(notes)}{"".join(legs)}'
        f"<details><summary>{e(question)}</summary><div class=\"reponse\">{rep}</div></details>"
        f'<p class="sources">Schéma pédagogique du lot. Repère D : droite du patient, à gauche de l&#x27;écran.</p>'
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


SIGLES = (
    "<p><abbr title=\"électrocardiogramme\">ECG</abbr> "
    "<abbr title=\"imagerie par résonance magnétique\">IRM</abbr> "
    "<abbr title=\"volume expiratoire maximal seconde\">VEMS</abbr> "
    "<abbr title=\"anti-inflammatoires non stéroïdiens\">AINS</abbr> "
    "<abbr title=\"information professionnelle suisse\">AIPS</abbr> "
    "<abbr title=\"société européenne de cardiologie\">ESC</abbr> "
    "<abbr title=\"indice de masse corporelle\">IMC</abbr></p>"
)


def sources_html() -> str:
    items = [
        "Référentiel suisse validé le 1er novembre 2023, situation O4.1.",
        "Stiell et collaborateurs, Journal of the American Medical Association, 3 mars 1993.",
        "Mueller-Wohlfahrt et collaborateurs, consensus de Munich, 2013.",
        "Patricios et collaborateurs, consensus d'Amsterdam, octobre 2022, texte de 2023.",
        "Outil d'évaluation de la commotion, mode d'emploi de 2023.",
        "Pelliccia et collaborateurs, lignes européennes publiées le 29 août 2020.",
        "Mountjoy et collaborateurs, consensus accepté le 20 août 2023.",
        "Parsons et collaborateurs, recommandation de 2013 sur la bronchoconstriction d'effort.",
        "Groupe d'experts des Jeux, prise en charge du coup de chaleur, 2021.",
        "Consensus préhospitalier sur la chaleur d'effort, version lue de 2024.",
        "Hoenig et collaborateurs, revue des lésions de stress osseux, 2023.",
        "Information professionnelle du paracétamol, autorisation 69266.",
        "Information professionnelle de l'ibuprofène, autorisation 67372.",
        "Information professionnelle du salbutamol, autorisation 37397.",
    ]
    lis = "".join(f"<li>{e(s)}</li>" for s in items)
    corps = (
        "<p>Les sources sont datées et archivées dans le dossier du lot.</p>"
        f"<ol class=\"sources\">{lis}</ol>{SIGLES}"
        "<p>L'ECG (électrocardiogramme) se lit avec les standards actuels.</p>"
        "<p>L'IRM (imagerie par résonance magnétique) n'est pas le premier geste de chaque entorse.</p>"
        "<p>Le VEMS (volume expiratoire maximal seconde) tranche la gêne d'effort.</p>"
        "<p>Les AINS (anti-inflammatoires non stéroïdiens) restent brefs si on les choisit.</p>"
        "<p>L'AIPS (information professionnelle suisse) porte les milligrammes.</p>"
        "<p>L'ESC (société européenne de cardiologie) cadre l'aptitude cardiaque de 2020.</p>"
        "<p>L'IMC (indice de masse corporelle) se compare à la médiane d'âge et de sexe.</p>"
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


def vignettes(n: int, modeles: list[str], decal: int) -> list[str]:
    out = []
    i = 0
    gardes = set()
    while len(out) < n:
        m = modeles[i % len(modeles)]
        age = AGES[(i + decal) % len(AGES)]
        sport = SPORTS[(i * 3 + decal) % len(SPORTS)]
        lieu = LIEUX[(i * 2 + decal) % len(LIEUX)]
        s = m.format(age=age, sport=sport, lieu=lieu, k=decal + i + 1)
        s = s.replace(". Chez ", ", chez ", 1)
        k = re.sub(r"\s+", " ", s).strip().lower()
        if k not in gardes and mots(s) <= 34 and ";" not in s:
            if MOTS_CLES.search(s):
                raise SystemExit(f"mot-clé dans une vignette: {s}")
            gardes.add(k)
            out.append(s)
        i += 1
        if i > n * 20:
            raise SystemExit("vignettes insuffisantes")
    return out


def inscrire(path: Path) -> None:
    subprocess.run(
        [sys.executable, str(RACINE / "harnais" / "taille_xy.py"), str(path), "--inscrire"],
        check=True,
    )


def mesurer(path: Path):
    h = path.read_text(encoding="utf-8")
    m = taille_xy.mesurer(h)
    return m.x[1], m.y[1]
