# -*- coding: utf-8 -*-
"""Moteur V8 du LOT_171. Style repris du modèle de leçon, pas du fond clinique."""
from pathlib import Path

STYLE = Path(__file__).with_name("style.cssfrag").read_text(encoding="utf-8")

def e(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def paras(items):
    out = []
    for it in items:
        if not it:
            continue
        if isinstance(it, tuple) and it[0] == "h":
            out.append(it[1])
        else:
            out.append(f"<p>{e(it)}</p>")
    return "".join(out)

def fen(fid, libelle, titre, items):
    return (
        f'<p><button type="button" class="terme" popovertarget="{fid}">{e(libelle)}</button></p>'
        f'<div id="{fid}" popover class="fenetre"><div class="barre"><span>{e(titre)}</span>'
        f'<button type="button" popovertarget="{fid}" popovertargetaction="hide" aria-label="Fermer">✕</button></div>'
        f'<div class="corps">{paras(items)}</div></div>'
    )

def section(sid, cls, titre, accroches, fenetres):
    acc = "".join(f"<p>{e(a)}</p>" for a in accroches)
    return f'<section class="ilot {cls}"><h2 id="{sid}">{titre}</h2>{acc}{"".join(fenetres)}</section>'

SIGLES = (
    '<p>Sigles développés pour toute la leçon. '
    '<abbr title="information professionnelle suisse">AIPS</abbr> '
    '<abbr title="International Myeloma Working Group">IMWG</abbr> '
    '<abbr title="gammapathie monoclonale de signification indéterminée">MGUS</abbr> '
    '<abbr title="calcium, rein, anémie, os">CRAB</abbr> '
    '<abbr title="Kidney Disease: Improving Global Outcomes">KDIGO</abbr> '
    '<abbr title="european association for the study of the liver">EASL</abbr> '
    '<abbr title="American Association for the Study of Liver Diseases">AASLD</abbr> '
    '<abbr title="chaînes légères libres sériques">FLC</abbr> '
    '<abbr title="protéine C réactive">CRP</abbr> '
    '<abbr title="rapport international normalisé">INR</abbr> '
    '<abbr title="imagerie par résonance magnétique">IRM</abbr> '
    '<abbr title="tomodensitométrie">TDM</abbr> '
    '<abbr title="tomographie par émission de positons">TEP</abbr> '
    '<abbr title="vert de bromocrésol">BCG</abbr> '
    '<abbr title="pourpre de bromocrésol">BCP</abbr> '
    '<abbr title="gradient d&#x27;albumine entre le sérum et l&#x27;ascite">SAAG</abbr> '
    '<abbr title="péritonite bactérienne spontanée">SBP</abbr> '
    '<abbr title="syndrome hépatorénal">HRS</abbr> '
    '<abbr title="acute kidney injury, insuffisance rénale aiguë">AKI</abbr> '
    '<abbr title="Model for End-stage Liver Disease">MELD</abbr> '
    '<abbr title="transjugular intrahepatic portosystemic shunt, dérivation portosystémique intrahépatique">TIPS</abbr> '
    '<abbr title="amylose à chaînes légères">AL</abbr> '
    '<abbr title="amylose de la protéine amyloïde A">AA</abbr> '
    '<abbr title="gène MYD88, mutation L265P">MYD88</abbr> '
    '<abbr title="récepteur de la phospholipase A2 de type M">PLA2R</abbr> '
    '<abbr title="gammapathie monoclonale de signification rénale">MGRS</abbr> '
    '<abbr title="Organisation mondiale de la santé">OMS</abbr> '
    '<abbr title="Principal Relevant Objectives and Framework for Integrated Learning and Education in Switzerland">PROFILES</abbr> '
    '<abbr title="hyalinose segmentaire et focale">HSF</abbr> '
    '<abbr title="peptide natriurétique de type B, fraction N-terminale">BNP</abbr> '
    '<abbr title="Association for Clinical Biochemistry">ACB</abbr> '
    '<abbr title="ARUP Laboratories, répertoire d&#x27;analyses">ARUP</abbr>.'
    "</p>"
)

SOM = """<ol class="som">
<li><a href="#p1">1. Définition</a></li>
<li><a href="#p2">2. Épidémiologie</a></li>
<li><a href="#p3">3. Physiopathologie</a></li>
<li><a href="#p4">4. Démarche diagnostique</a></li>
<li><a href="#p5">5. Anamnèse et drapeaux rouges</a></li>
<li><a href="#p6">6. Examen physique</a></li>
<li><a href="#p7">7. Approche syndromique</a></li>
<li><a href="#p8">8. Diagnostic positif</a></li>
<li><a href="#p9">9. Examens complémentaires</a></li>
<li><a href="#p10">10. Arbre décisionnel</a></li>
<li><a href="#p11">11. Prise en charge en Suisse</a></li>
<li><a href="#p12">12. Prévention</a></li>
<li><a href="#p13">13. Points clés</a></li>
<li><a href="#p14">14. Pièges d'examen</a></li>
</ol>
<p class="sous">Les mots ⧉ ouvrent une fenêtre. Les sources sont à la fin.</p>"""

SOURCES = """<ol class="sources">
<li>Catalogue ACB, protéines totales, intervalle adulte 60 à 80 g/l. PDF lu le 31 octobre 2026.</li>
<li>Khumalo et collaborateurs, trou protéique, 2025. Albumine de laboratoire 35 à 52 g/l.</li>
<li>ARUP et Mayo, fractions de l'électrophorèse, pages lues le 31 octobre 2026.</li>
<li>Kyle et collaborateurs, New England Journal of Medicine, 2006. Prévalence du MGUS.</li>
<li>Rajkumar et collaborateurs, Blood, 2005. Risque Mayo et rapport 0,26 à 1,65.</li>
<li>Rajkumar, Hematology, 2015, critères IMWG 2014. CRAB et biomarqueurs.</li>
<li>KDIGO, maladies glomérulaires, 2021. Syndrome néphrotique et anticoagulation.</li>
<li>EASL, cirrhose décompensée, Journal of Hepatology, 2018. Albumine, ascite, SBP, HRS.</li>
<li>Biggins et collaborateurs, Hepatology, 2021. Six à huit grammes par litre après grande ponction.</li>
<li>Figge et collaborateurs, Critical Care Medicine, 1998. Trou anionique et albumine.</li>
<li>Payne et collaborateurs, British Medical Journal, 1973. Calcémie et albumine.</li>
<li>Pugh et collaborateurs, British Journal of Surgery, 1973. Score entier.</li>
<li>AIPS albumine 65562 et 58155, spironolactone 27257, furosémide 30629. Corpus lu le 31 octobre 2026.</li>
</ol>
<p class="mention">Contenu établi à partir des sources citées ; non validé cliniquement par un médecin.</p>"""


def page(nom_fichier, h1, sous, essentiel, sections, fin):
    corps = "\n".join(sections)
    html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(h1)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap">
{STYLE}
</head>
<body>
<main>
<h1 id="titre">{e(h1)}</h1>
<p class="taille" id="taille">Taille : en attente</p>
<p class="sous">{sous}</p>
<section class="ilot c essentiel" aria-labelledby="ess">
<h2 id="ess">L'essentiel</h2>
{essentiel}
</section>
<nav class="ilot v" aria-labelledby="som">
<h2 id="som">Sommaire</h2>
{SOM}
</nav>
{corps}
<section class="ilot c">
<h2 id="sources">Sources</h2>
{SOURCES}
</section>
</main>
</body>
</html>
<!-- FIN_FICHIER {fin} -->
"""
    return html


def svg_electrophorese():
    """Six tracés. Le survol du nom montre la lecture. Le clic ouvre la définition."""
    traces = [
        ("n", "Normal", "62,78 92,78 108,22 128,78 150,70 168,48 186,62 210,40 250,78",
         "Vallées nettes"),
        ("i", "Inflammatoire", "62,70 100,55 118,28 132,40 150,18 168,38 190,48 220,30 250,55",
         "Alpha 1 et 2 hautes"),
        ("c", "Cirrhose", "62,78 108,48 140,62 168,58 190,50 220,46 250,52",
         "Bloc bêta-gamma"),
        ("s", "Néphrotique", "62,78 108,62 150,16 168,55 210,70 250,78",
         "Alpha-2 haute"),
        ("m", "Monoclonal", "62,78 108,24 140,78 168,55 200,18 214,55 250,78",
         "Bande étroite"),
        ("h", "Hypogamma", "62,78 108,22 140,78 168,58 220,74 250,78",
         "Gamma plat"),
    ]
    cols = []
    for i, (k, nom, pts, tip) in enumerate(traces):
        origin = 20 + i * 148
        seq = []
        for j, pair in enumerate(pts.split()):
            px, py = pair.split(",")
            xx = origin + (int(px) - 60) * 120 / 190
            seq.append(("M" if j == 0 else "L") + f"{xx:.1f},{py}")
        d = " ".join(seq)
        cols.append(f'''<g class="hot" tabindex="0">
<path d="{d}" fill="none" stroke="currentColor" stroke-width="2.4" />
<text x="{origin+68}" y="108" text-anchor="middle" font-size="13" font-weight="700">{nom}</text>
<g class="tip"><rect x="{origin}" y="116" width="136" height="28" rx="6" fill="var(--page)" stroke="var(--trait)"/>
<text x="{origin+68}" y="135" text-anchor="middle" font-size="12">{tip}</text></g>
</g>''')
    return f'''<figure class="schema"><svg viewBox="0 0 900 190" role="img" aria-labelledby="elTit elDesc">
<title id="elTit">Six électrophorèses comparées</title>
<desc id="elDesc">Normal, inflammatoire, cirrhose avec bloc bêta-gamma, syndrome néphrotique, pic monoclonal, hypogammaglobulinémie. Le survol d'un nom affiche la lecture.</desc>
<line x1="12" y1="96" x2="888" y2="96" stroke="var(--trait)"/>
{''.join(cols)}
</svg>
<figcaption>Six tracés. Survoler un nom. La définition de chaque profil s'ouvre au clic des boutons sous la figure.</figcaption>
</figure>
<style>
figure.schema .hot .tip{{display:none}}
figure.schema .hot:hover .tip,figure.schema .hot:focus .tip,figure.schema.montre .hot .tip{{display:block}}
</style>'''


def svg_hypo():
    etapes = [
        (40, "1. Albumine basse", "Unité et méthode"),
        (100, "2. Protéinurie", "Grammes par jour"),
        (160, "3. Foie et ascite", "Bilirubine et INR"),
        (220, "4. Selles et tube", "Perte digestive"),
        (280, "5. CRP et apport", "Inflammation ou jeûne"),
    ]
    g = []
    for y, nom, tip in etapes:
        g.append(f'''<g class="hot" tabindex="0">
<rect x="180" y="{y}" width="280" height="44" rx="8" fill="var(--encadre)" stroke="currentColor"/>
<text x="320" y="{y+27}" text-anchor="middle" font-size="15" font-weight="700">{nom}</text>
<g class="tip"><rect x="470" y="{y}" width="250" height="44" rx="6" fill="var(--page)" stroke="var(--trait)"/>
<text x="482" y="{y+27}" font-size="13">{tip}</text></g>
</g>''')
        if y < 280:
            g.append(f'<line x1="320" y1="{y+44}" x2="320" y2="{y+56}" stroke="currentColor"/>')
    return f'''<figure class="schema"><svg viewBox="0 0 760 350" role="img" aria-labelledby="hyTit">
<title id="hyTit">Algorithme devant une hypoalbuminémie</title>
{''.join(g)}
</svg>
<figcaption>Ordre de lecture devant une albumine basse. Survoler une étape.</figcaption>
</figure>'''


def svg_clone():
    boxes = [
        (24, "MGUS", "Pas de CRAB"),
        (168, "Myélome", "CRAB ou SLiM"),
        (312, "Waldenström", "IgM, moelle"),
        (456, "Amylose AL", "Rouge Congo"),
    ]
    g = []
    for x, nom, tip in boxes:
        g.append(f'''<g class="hot" tabindex="0">
<rect x="{x}" y="70" width="130" height="70" rx="8" fill="var(--encadre)" stroke="currentColor"/>
<text x="{x+65}" y="112" text-anchor="middle" font-size="13" font-weight="700">{nom}</text>
<g class="tip"><rect x="{x}" y="148" width="130" height="32" rx="6" fill="var(--page)" stroke="var(--trait)"/>
<text x="{x+65}" y="169" text-anchor="middle" font-size="12">{tip}</text></g>
</g>''')
    return f'''<figure class="schema"><svg viewBox="0 0 620 240" role="img" aria-labelledby="clTit">
<title id="clTit">Quatre clones à ne pas confondre</title>
<text x="310" y="36" text-anchor="middle" font-size="15" font-weight="700">Pic ou chaîne légère</text>
<line x1="310" y1="44" x2="310" y2="70" stroke="currentColor"/>
{''.join(g)}
</svg>
<figcaption>Quatre diagnostics. Survoler le nom. Le détail s'ouvre au clic.</figcaption>
</figure>'''


def stand(titre, svg, montre=False):
    cls = "schema montre" if montre else "schema"
    svg2 = svg.replace('class="schema"', f'class="{cls}"', 1)
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>{e(titre)}</title>
{STYLE}</head><body style="background:#fff"><main>{svg2}</main></body></html>"""
