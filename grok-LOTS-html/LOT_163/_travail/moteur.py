# -*- coding: utf-8 -*-
"""Assemble une leçon V8. Lecture du CSS de LOT_161, sans modifier ce LOT."""
import html
import re
from pathlib import Path

RACINE = Path("/workspace")
CSS_SRC = RACINE / "grok-LOTS-html/LOT_161/LOT_161_Phase_B_V0_DX.1.html"
LOT = RACINE / "grok-LOTS-html/LOT_163"

GLOSSAIRE = [
    ("Association européenne d'urologie", "EAU"),
    ("Association américaine d'urologie", "AUA"),
    ("Société d'urodynamique, de médecine pelvienne féminine et de reconstruction urogénitale", "SUFU"),
    ("Fédération européenne de chimie clinique et de médecine de laboratoire", "EFLM"),
    ("Confédération européenne de médecine de laboratoire", "ECLM"),
    ("Kidney Disease Improving Global Outcomes", "KDIGO"),
    ("information professionnelle suisse", "AIPS"),
    ("unité formant colonie", "UFC"),
    ("globule rouge", "GR"),
    ("champ à fort grossissement", "HPF"),
    ("nécrose tubulaire aiguë", "NTA"),
    ("insuffisance rénale aiguë", "IRA"),
    ("hypertension artérielle", "HTA"),
    ("anti-inflammatoire non stéroïdien", "AINS"),
    ("inhibiteur de l'enzyme de conversion", "IEC"),
    ("virus de l'immunodéficience humaine", "VIH"),
    ("glucose-6-phosphate déshydrogénase", "G6PD"),
    ("examen cytobactériologique des urines", "ECBU"),
    ("tomodensitométrie", "TDM"),
    ("imagerie par résonance magnétique", "IRM"),
    ("valeur prédictive positive", "VPP"),
    ("valeur prédictive négative", "VPN"),
    ("anticorps anti-cytoplasme des neutrophiles", "ANCA"),
    ("cellule épithéliale tubulaire rénale", "CET"),
    ("intervalle de confiance", "IC"),
]


def css():
    t = CSS_SRC.read_text(encoding="utf-8")
    m = re.search(r"<style>(.*?)</style>", t, re.S)
    if not m:
        raise SystemExit("CSS introuvable")
    return m.group(1)


def p(texte, src=None):
    t = texte.strip()
    if src:
        t += f'<sup class="s">{src}</sup>'
    return f"<p>{t}</p>"


def paras(items):
    out = []
    for it in items:
        if isinstance(it, tuple):
            out.append(p(it[0], it[1] if len(it) > 1 else None))
        else:
            out.append(p(it))
    return "".join(out)


def table(caption, headers, rows):
    th = "".join(f"<th>{html.escape(h)}</th>" for h in headers)
    body = []
    for row in rows:
        tds = "".join(f"<td>{html.escape(c)}</td>" for c in row)
        body.append(f"<tr>{tds}</tr>")
    return (
        f'<div class="tw"><table><caption>{html.escape(caption)}</caption>'
        f"<thead><tr>{th}</tr></thead><tbody>{''.join(body)}</tbody></table></div>"
    )


def glossaire_html():
    lignes = []
    for titre, sigle in GLOSSAIRE:
        lignes.append(
            f'<p>Dans cette leçon, {html.escape(titre)} '
            f'(<abbr title="{html.escape(titre)}">{html.escape(sigle)}</abbr>).</p>'
        )
    return (
        '<div id="w-glossaire" popover class="fenetre"><div class="barre"><span>Sigles de la leçon</span>'
        '<button type="button" popovertarget="w-glossaire" popovertargetaction="hide" aria-label="Fermer">✕</button>'
        f'</div><div class="corps">{"".join(lignes)}</div></div>'
    )


def fenetre(wid, titre, corps):
    return (
        f'<div id="{wid}" popover class="fenetre"><div class="barre"><span>{html.escape(titre)}</span>'
        f'<button type="button" popovertarget="{wid}" popovertargetaction="hide" aria-label="Fermer">✕</button>'
        f'</div><div class="corps">{corps}</div></div>'
    )


def section(n, titre, ile, corps, alterne):
    cl = "c" if alterne else "v"
    wid = f"a-p{n}"
    return (
        f'<section class="ilot {cl}"><h2 id="p{n}">{n}. {html.escape(titre)}</h2>'
        f"{paras(ile)}"
        f'<p>On ouvre <button type="button" class="terme" popovertarget="{wid}">la fenêtre de ce point</button>.</p>'
        f"{fenetre(wid, f'{n}. {titre}', corps)}</section>"
    )


POINTS = [
    (1, "Définition"),
    (2, "Épidémiologie"),
    (3, "Physiopathologie et rappels"),
    (4, "Démarche diagnostique"),
    (5, "Anamnèse et drapeaux rouges"),
    (6, "Examen physique"),
    (7, "Approche syndromique"),
    (8, "Diagnostic positif"),
    (9, "Examens complémentaires"),
    (10, "Arbre décisionnel"),
    (11, "Prise en charge en Suisse"),
    (12, "Prévention"),
    (13, "Points clés"),
    (14, "Pièges d'examen"),
]


def page(fichier_titre, h1, sous, essentiel, contenus, sources, fin):
    """contenus: dict n -> (ile list, corps html str)."""
    som = "".join(f'<li><a href="#p{n}">{n}. {html.escape(titre)}</a></li>' for n, titre in POINTS)
    blocs = []
    for i, (n, titre) in enumerate(POINTS):
        ile, corps = contenus[n]
        blocs.append(section(n, titre, ile, corps, i % 2 == 0))
    src_li = "".join(f"<li>{html.escape(s)}</li>" for s in sources)
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(fichier_titre)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
<style>
{css()}
</style>
</head>
<body>
<main>
<h1 id="titre">{html.escape(h1)}</h1>
<p class="taille" id="taille">Taille : en attente</p>
<p class="sous">{html.escape(sous)}</p>
<section class="ilot c essentiel"><h2 id="ess">L'essentiel</h2>
{paras(essentiel)}
<p>Les sigles s'ouvrent dans <button type="button" class="terme" popovertarget="w-glossaire">la fenêtre des sigles</button>.</p>
{glossaire_html()}
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
{src_li}
</ol>
</section>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</main>
</body>
</html>
<!-- {fin} -->
"""


SOURCES = [
    "Barocas et collaborateurs, guide AUA/SUFU de l'hématurie microscopique, 2020, amendement 2025.",
    "Kouri et collaborateurs, guide EFLM d'analyse d'urine, 2023, publié en 2024.",
    "Guide de l'Association européenne d'urologie sur les infections urologiques, 2024.",
    "Köhler, Wandel et Brunck, Kidney International, 1991.",
    "Muriithi, Nasr et Leung, Clinical Journal of the American Society of Nephrology, 2013.",
    "Perazella et collaborateurs, Clinical Journal of the American Society of Nephrology, 2008.",
    "Cavanaugh et Perazella, American Journal of Kidney Diseases, 2019.",
    "KDIGO, maladies glomérulaires, Kidney International, 2021.",
    "Fosfomycine Sandoz, Swissmedic 66690.",
    "Monuril, Swissmedic 49298.",
    "Nitrofurantoin-Acino 100 retard, Swissmedic 62724.",
    "Bactrim forte, Swissmedic 48306.",
    "Ciproxine, Swissmedic 47795.",
    "Tamsulosine Sandoz eco 0,4 mg, Swissmedic 62112.",
    "Prednisone Streuli, Swissmedic 29349.",
    "Allopurinol Zentiva, Swissmedic 56050.",
    "Ramipril Zentiva, Swissmedic 58159.",
]


def ecrire(nom, html_txt):
    dest = LOT / nom
    dest.write_text(html_txt, encoding="utf-8")
    return dest
