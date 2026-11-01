# -*- coding: utf-8 -*-
"""Habillage V8 du LOT_232. Fenêtres, dual-vue, Atkinson. Pas de script."""

CSS = """
:root{--fond:#eef7fc;--page:#ffffff;--texte:#1d2a30;--doux:#4f5f66;--lien:#0b5d86;--titre:#14303b;--trait:#cfe3ec;--encadre:#f5f7f9;--bord:#1a7a50;--vert:#1a7a50;--ciel:#176fa0;--alerte:#a1262f;--ombre:rgb(15 60 90 / .28);--voile:rgb(10 30 45 / .55);--barre:#f2f5f7;--th:#f2f5f7;--cb1:#4fb3e6;--cb2:#b9e2f6;--vb1:#3aa776;--vb2:#b5e1cb;--o1:rgb(15 60 90 / .07);--o2:rgb(15 60 90 / .09)}
@media (prefers-color-scheme:dark){:root{--fond:#0e171d;--page:#16222a;--texte:#e3edf1;--doux:#a9bac2;--lien:#8fd3f5;--titre:#e6eef2;--trait:#2c414c;--encadre:#1a252c;--bord:#5cc79a;--vert:#5cc79a;--ciel:#6cc2ef;--alerte:#ff8a92;--ombre:rgb(0 0 0 / .6);--voile:rgb(0 0 0 / .7);--barre:#1d282f;--th:#1d282f;--cb1:#4aa9da;--cb2:#24506a;--vb1:#46b384;--vb2:#245a44;--o1:rgb(0 0 0 / .35);--o2:rgb(0 0 0 / .3)}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--fond);color:var(--texte);font:1rem/1.45 "Atkinson Hyperlegible",Verdana,sans-serif;overflow-wrap:break-word;hyphens:manual}
main{max-width:72ch;margin:0 auto;padding:1rem 1rem 2rem}
h1,h2,h3,.barre,summary,nav,caption,th{font-family:"Atkinson Hyperlegible",Verdana,sans-serif}
h1{font-size:1.75rem;line-height:1.25;color:var(--titre);margin:0 0 .4rem}
h2{font-size:1.3rem;line-height:1.3;color:var(--titre);margin:0 0 .45rem}
h3{font-size:1.05rem;color:var(--titre);margin:.8rem 0 .3rem}
p{margin:0 0 .55rem}.sous{color:var(--doux);font-size:.95rem}
a{color:var(--lien)}
.ilot{background:linear-gradient(var(--page),var(--page)) padding-box,var(--bd) border-box;border:1.5px solid transparent;border-radius:12px;padding:.85rem 1rem .6rem;margin:0 0 .7rem;box-shadow:0 1px 2px var(--o1),0 6px 16px var(--o2)}
.ilot.c{--bd:linear-gradient(135deg,var(--cb1),var(--cb2))}
.ilot.v{--bd:linear-gradient(135deg,var(--vb1),var(--vb2))}
button.terme{all:unset;cursor:pointer;color:var(--lien);text-decoration:underline dotted 1.5px;text-underline-offset:3px}
button.terme::after{content:" ⧉";font-size:.75em;vertical-align:.15em}
button.terme:focus-visible{outline:2px solid var(--lien);outline-offset:2px}
.fenetre{position:fixed;inset:0;margin:auto;width:min(92vw,46rem);max-height:86vh;overflow:auto;padding:0;border:1px solid var(--trait);border-radius:12px;background:var(--page);color:var(--texte);box-shadow:0 18px 50px var(--ombre)}
.fenetre::backdrop{background:var(--voile)}
.barre{position:sticky;top:0;z-index:1;display:flex;align-items:center;justify-content:space-between;gap:.8rem;padding:.55rem .6rem .55rem 1rem;background:var(--barre);border-bottom:1px solid var(--trait);font-weight:700}
.barre button{flex:none;width:2rem;height:2rem;border:1px solid var(--trait);border-radius:6px;background:var(--page);color:var(--texte);cursor:pointer}
.corps{padding:1rem 1.2rem 1.2rem}
.tw{overflow-x:auto;margin:.6rem 0 1rem}
table{border-collapse:collapse;width:100%;font-size:.92rem;line-height:1.4}
th,td{border:1px solid var(--trait);padding:.35rem .45rem;vertical-align:top;text-align:left}
th{background:var(--th)}
caption{text-align:left;font-weight:700;padding:.2rem 0 .4rem}
nav ol{padding-left:1.2rem;margin:.2rem 0}
.som{columns:2;column-gap:1.2rem}.som li{break-inside:avoid}
.urgence{border:2px solid var(--alerte);border-radius:8px;padding:.7rem .9rem;margin:.7rem 0;background:var(--page)}
.urgence strong{color:var(--alerte)}
figure{margin:.6rem 0}figure svg{width:100%;height:auto;display:block}
figcaption{font-size:.88rem;color:var(--doux);margin-top:.3rem}
.sources{font-size:.86rem}.sources li{margin:.35rem 0}
.mention{font-style:italic;color:var(--doux)}
.taille{font-size:.85rem;color:var(--doux)}
sup.s{font-size:.66em;font-weight:700;color:#1a3a6b}
.cliche{text-decoration:underline dotted;text-underline-offset:3px}
abbr[title]{text-decoration:underline dotted 1px;cursor:help}
.schema .etape rect{fill:var(--page);stroke:var(--ciel);stroke-width:1.6}
.schema .etape:hover rect,.schema .etape:focus rect,.schema .etape:target rect{stroke:var(--alerte);stroke-width:3}
.schema text{fill:var(--texte);font-family:"Atkinson Hyperlegible",Verdana,sans-serif}
@media (max-width:480px){h1{font-size:1.45rem}.som{columns:1}}
"""

TITRES = [
    (1, "Définition"),
    (2, "Épidémiologie"),
    (3, "Physiopathologie"),
    (4, "Démarche diagnostique"),
    (5, "Anamnèse et drapeaux rouges"),
    (6, "Examen clinique"),
    (7, "Approche syndromique"),
    (8, "Diagnostic positif"),
    (9, "Examens complémentaires"),
    (10, "Arbre décisionnel"),
    (11, "Prise en charge en Suisse"),
    (12, "Prévention"),
    (13, "Points clés"),
    (14, "Pièges d'examen"),
]


def fenetre(wid, titre, corps):
    return (
        f'<div id="{wid}" popover class="fenetre"><div class="barre"><span>{titre}</span>'
        f'<button type="button" popovertarget="{wid}" popovertargetaction="hide" aria-label="Fermer">✕</button>'
        f'</div><div class="corps">{corps}</div></div>'
    )


def bouton(wid, libelle):
    return f'<button type="button" class="terme" popovertarget="{wid}">{libelle}</button>'


def page(nom_fichier, titre_onglet, h1, sous, essentiel, sections, sources_html, fin):
    """sections : liste de (num, carte_html, liste de fenetres html)."""
    liens = "\n".join(
        f'<li><a href="#p{n}">{lib}</a></li>' for n, lib in TITRES
    )
    blocs = []
    for i, (n, carte, wins) in enumerate(sections):
        lib = TITRES[n - 1][1]
        cls = "c" if i % 2 == 0 else "v"
        blocs.append(
            f'<section class="ilot {cls}"><h2 id="p{n}">{n}. {lib}</h2>\n{carte}\n'
            + "\n".join(wins)
            + "\n</section>"
        )
    corps = "\n".join(blocs)
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre_onglet}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
<style>
{CSS}
</style>
</head>
<body>
<main>
<h1 id="titre">{h1}</h1>
<p class="taille" id="taille">Taille : en cours de mesure</p>
<p class="sous">{sous}</p>
<section class="ilot c essentiel" aria-labelledby="ess">
<h2 id="ess">L'essentiel</h2>
{essentiel}
</section>
<nav class="ilot v" aria-labelledby="som">
<h2 id="som">Sommaire</h2>
<ol class="som">
{liens}
</ol>
<p class="sous">Les mots ⧉ ouvrent une fenêtre. Les sources sont à la fin.</p>
</nav>
{corps}
<section class="ilot c">
<h2 id="sources">Sources</h2>
<ol class="sources">
{sources_html}
</ol>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>
</section>
</main>
</body>
</html>
<!-- FIN_FICHIER {fin} -->
"""
