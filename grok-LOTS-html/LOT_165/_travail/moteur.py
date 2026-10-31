# -*- coding: utf-8 -*-
"""Assemble une leçon V8 du LOT_165. Lit le CSS de LOT_161, sans le modifier."""
import html
import re
from pathlib import Path

RACINE = Path("/workspace")
CSS_SRC = RACINE / "grok-LOTS-html/LOT_161/LOT_161_Phase_B_V0_DX.1.html"
LOT = RACINE / "grok-LOTS-html/LOT_165"

GLOSSAIRE = [
    ("système de groupes sanguins ABO", "ABO"),
    ("transfusion-related acute lung injury, insuffisance pulmonaire aiguë post-transfusionnelle", "TRALI"),
    ("transfusion-associated circulatory overload, surcharge volémique associée à la transfusion", "TACO"),
    ("International Society of Blood Transfusion", "ISBT"),
    ("réaction transfusionnelle fébrile non hémolytique", "RTFNH"),
    ("réaction transfusionnelle hémolytique", "RTH"),
    ("purpura post-transfusionnel", "PTP"),
    ("human leukocyte antigen, antigène d'histocompatibilité", "HLA"),
    ("human neutrophil antigen, antigène des neutrophiles", "HNA"),
    ("human platelet antigen, antigène plaquettaire", "HPA"),
    ("transfusion-associated dyspnoea, dyspnée associée à une transfusion", "TAD"),
    ("transfusion-transmitted infection, infection transmise par transfusion", "TTI"),
    ("information professionnelle suisse", "AIPS"),
    ("lactate déshydrogénase", "LDH"),
    ("aspartate aminotransférase", "ASAT"),
    ("peptide natriurétique de type B", "BNP"),
    ("coagulation intravasculaire disséminée", "CID"),
    ("hémorragie fœto-maternelle", "HFM"),
    ("fetomaternal haemorrhage, hémorragie fœto-maternelle", "FMH"),
    ("unité internationale", "UI"),
    ("virus de l'immunodéficience humaine", "VIH"),
    ("virus de l'hépatite B", "VHB"),
    ("virus de l'hépatite C", "VHC"),
    ("Office fédéral de la santé publique", "OFSP"),
    ("concentré érythrocytaire", "CE"),
    ("plasma frais congelé", "PFC"),
    ("concentré plaquettaire", "CP"),
    ("recherche d'anticorps irréguliers", "RAI"),
    ("cytomégalovirus", "CMV"),
    ("Association for the Advancement of Blood and Biotherapies", "AABB"),
    ("International Haemovigilance Network", "IHN"),
    ("British Committee for Standards in Haematology", "BCSH"),
    ("Hôpitaux universitaires de Genève", "HUG"),
    ("laboratoire d'immunologie transfusionnelle", "LIHT"),
    ("produit sanguin labile", "PSL"),
    ("personne responsable de l'hémovigilance", "PRHv"),
    ("groupe sanguin AB, antigènes A et B sans anticorps ABO naturels", "AB"),
    ("segment du numéro d'aide-mémoire I-310.AA.01", "AA"),
]


def css():
    t = CSS_SRC.read_text(encoding="utf-8")
    m = re.search(r"<style>(.*?)</style>", t, re.S)
    if not m:
        raise SystemExit("CSS introuvable")
    extra = """
svg .cell{cursor:help}
svg .cell:hover rect{stroke:#14303b;stroke-width:3px}
svg .ok{fill:#1a7a50}
svg .non{fill:#a1262f}
svg .soi{fill:#0b5d86}
svg .entete{fill:#14303b}
svg text{font-family:Verdana,sans-serif;font-size:13px}
svg .lbl{fill:#ffffff;font-weight:700}
svg .petit{fill:#ffffff;font-size:11px}
svg .titre-svg{fill:#14303b;font-size:15px;font-weight:700}
"""
    return m.group(1) + extra


def p(texte, src=None):
    t = texte.strip()
    if src:
        if isinstance(src, (list, tuple)):
            t += "".join(f'<sup class="s">{s}</sup>' for s in src)
        else:
            t += f'<sup class="s">{src}</sup>'
    return f"<p>{t}</p>"


def paras(items):
    out = []
    for it in items:
        if isinstance(it, tuple):
            out.append(p(it[0], it[1] if len(it) > 1 else None))
        else:
            out.append(it if it.startswith("<") else p(it))
    return "".join(out)


def table(caption, headers, rows):
    th = "".join(f"<th>{html.escape(h)}</th>" for h in headers)
    body = []
    for row in rows:
        tds = "".join(f"<td>{c if '<' in c else html.escape(c)}</td>" for c in row)
        body.append(f"<tr>{tds}</tr>")
    return (
        '<div class="tw"><table><caption>' + html.escape(caption) + "</caption>"
        + "<thead><tr>" + th + "</tr></thead><tbody>\n"
        + "\n".join(body)
        + "\n</tbody></table></div>"
    )


def glossaire_html():
    lignes = []
    for titre, sigle in GLOSSAIRE:
        lignes.append(
            f"<p>Dans cette leçon, {html.escape(titre)} "
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

SOURCES = [
    "Swissmedic, Hémovigilance, rapport annuel 2024.",
    "Swissmedic, aide-mémoire I-310.AA.01-A01f, 09.08.2024.",
    "Swissmedic, Guide d'assurance-qualité dans la pratique transfusionnelle, édition 2026.",
    "Rhophylac 300, information professionnelle, Swissmedic 53609.",
    "Adrenalin Sintetica 1 mg/ml, information professionnelle, Swissmedic 56551.",
    "Lasix solution injectable, information professionnelle, Swissmedic 30630.",
    "Tavegyl solution pour injection, information professionnelle, Swissmedic 35501.",
    "Qureshi et collaborateurs, guide BCSH de l'immunoglobuline anti-D, Transfusion Medicine, 2014.",
    "Hôpitaux universitaires de Genève, safety-card AB, approuvé le 15.02.2024.",
    "ISBT, IHN et AABB, définitions de surveillance 2013 et définition révisée de la surcharge volémique 2018, citées par Swissmedic en 2024.",
]


def page(fichier_titre, h1, sous, essentiel, contenus, fin, sources=None):
    som = "".join(f'<li><a href="#p{n}">{n}. {html.escape(titre)}</a></li>' for n, titre in POINTS)
    blocs = []
    for i, (n, titre) in enumerate(POINTS):
        ile, corps = contenus[n]
        blocs.append(section(n, titre, ile, corps, i % 2 == 0))
    src_li = "".join(f"<li>{html.escape(s)}</li>" for s in (sources or SOURCES))
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


def ecrire(nom, html_texte):
    chemin = LOT / nom
    chemin.write_text(html_texte, encoding="utf-8")
    return chemin
