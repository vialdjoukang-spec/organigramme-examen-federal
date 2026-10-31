#!/usr/bin/env python3
"""Assemble une leçon V8. Le style est copié du modèle déjà validé sur cette branche."""
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]
STYLE = Path(RACINE / "grok-LOTS-html/LOT_162/LOT_162_Phase_B_V0_DX.4.html").read_text(encoding="utf-8")
STYLE = STYLE.split("<style>", 1)[1].split("</style>", 1)[0]

SIGLES = [
    ("G6PD", "glucose-6-phosphate déshydrogénase"),
    ("ADAMTS13", "désintégrine et métalloprotéase à motifs thrombospondine, membre 13"),
    ("PROFILES", "Principal Relevant Objectives and Framework for Integrated Learning and Education in Switzerland"),
    ("CIVD", "coagulation intravasculaire disséminée"),
    ("SHU", "syndrome hémolytique et urémique"),
    ("PTT", "purpura thrombotique thrombocytopénique"),
    ("AIPS", "information professionnelle suisse"),
    ("OMS", "Organisation mondiale de la Santé"),
    ("BSG", "British Society of Gastroenterology"),
    ("BSH", "British Society for Haematology"),
    ("NICE", "National Institute for Health and Care Excellence"),
    ("ECCO", "European Crohn's and Colitis Organisation"),
    ("ESC", "European Society of Cardiology"),
    ("VGM", "volume globulaire moyen"),
    ("NFS", "numération formule sanguine"),
    ("LDH", "lactate déshydrogénase"),
    ("MAT", "microangiopathie thrombotique"),
    ("CRP", "protéine C réactive"),
    ("EPO", "érythropoïétine"),
    ("ECG", "électrocardiogramme"),
    ("IRM", "imagerie par résonance magnétique"),
    ("DAT", "test direct à l'antiglobuline"),
    ("MMA", "acide méthylmalonique"),
    ("ADN", "acide désoxyribonucléique"),
    ("VIH", "virus de l'immunodéficience humaine"),
    ("ABO", "système de groupes sanguins ABO"),
    ("UI", "unité internationale"),
    ("GBD", "Global Burden of Disease"),
]


def esc(t: str) -> str:
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def abbr_texte(t: str) -> str:
    t = esc(t)
    for sig, titre in SIGLES:
        t = t.replace(sig, f'<abbr title="{esc(titre)}">{sig}</abbr>')
    return t


def sups(nums) -> str:
    return "".join(f'<sup class="s">{n}</sup>' for n in nums)


def P(texte: str, sources) -> str:
    return f"<p>{abbr_texte(texte)}{sups(sources)}</p>"


def fenetre(wid: str, titre: str, corps: str) -> str:
    return (
        f'<div id="{wid}" popover class="fenetre"><div class="barre"><span>{esc(titre)}</span>'
        f'<button type="button" popovertarget="{wid}" popovertargetaction="hide" aria-label="Fermer">✕</button>'
        f'</div><div class="corps">{corps}</div></div>'
    )


def table(caption: str, headers, rows) -> str:
    h = "".join(f"<th>{esc(x)}</th>" for x in headers)
    body = []
    for r in rows:
        body.append("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>")
    return (
        f'<div class="tw"><table><caption>{esc(caption)}</caption><thead><tr>{h}</tr></thead>'
        f'<tbody>{"".join(body)}</tbody></table></div>'
    )


def page(*, chemin: Path, titre: str, sous: str, essentiel: str, sommaire_note: str,
         points: list, sources_ol: str, fin: str, glossaire: str) -> None:
    """points : liste de 14 tuples (titre_h2, fiche_html, fenetre_html)."""
    ilots = []
    ilots.append(
        f'<section class="ilot c essentiel" aria-labelledby="ess"><h2 id="ess">L\'essentiel</h2>'
        f'{essentiel}{glossaire}</section>'
    )
    items = "".join(f'<li><a href="#p{i}">{esc(points[i-1][0])}</a></li>' for i in range(1, 15))
    ilots.append(
        f'<nav class="ilot v" aria-labelledby="som"><h2 id="som">Sommaire</h2><ol class="som">{items}</ol>'
        f'<p class="sous">{esc(sommaire_note)}</p></nav>'
    )
    for i, (h2, fiche, fen) in enumerate(points, start=1):
        cls = "c" if i % 2 else "v"
        wid = f"w{i}"
        bouton = f'<button type="button" class="terme" popovertarget="{wid}">Détail</button>'
        ilots.append(
            f'<section class="ilot {cls}"><h2 id="p{i}">{i}. {esc(h2)}</h2>{fiche}{bouton}'
            f'{fenetre(wid, h2, fen)}</section>'
        )
    html = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titre)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
<style>{STYLE}</style>
</head>
<body>
<main>
<h1 id="titre">{esc(titre)}</h1>
<p class="taille" id="taille">Taille : en attente de mesure</p>
<p class="sous">{esc(sous)}</p>
{''.join(ilots)}
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
<section class="ilot c"><h2 id="sources">Sources</h2>
<ol class="sources">
{sources_ol}
</ol>
</section>
</main>
</body>
</html>
<!-- {fin} -->
'''
    chemin.write_text(html, encoding="utf-8")
