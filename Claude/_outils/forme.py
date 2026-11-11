#!/usr/bin/env python3
"""FORME — correction automatique de la forme des cours (ordre de Vial du 10.11.2026), zéro modèle, idempotent.

1. Police obligatoire : Atkinson Hyperlegible, chargée depuis Claude/_polices/ (fichiers partagés, feuille commune
   Claude/_polices/forme.css, ~70 octets ajoutés par leçon ; la bande L1 de 80–150 Ko, images exclues, reste respectée).
2. Mise en page : texte courant justifié avec césure, interligne réduit (1,4), marges de paragraphe resserrées ;
   titres, tableaux, figures et listes de navigation restent alignés à gauche.
3. Espaces inutiles : lignes vides multiples, paragraphes vides, espaces doubles dans le texte, espace avant
   « . » ou « , ». Les blocs <script>, <style>, <pre>, <svg> et les attributs ne sont jamais touchés.

Usage : python3 Claude/_outils/forme.py Claude/LOT_00X/*.html   (--verifier : code 1 si un fichier changerait)
"""
import re, sys

POLICES = 'atkinson-hyperlegible-latin-'  # relatif à Claude/_polices/forme.css
FACES = ''.join(
    f"@font-face{{font-family:'Atkinson Hyperlegible';font-style:{st};font-weight:{w};font-display:swap;"
    f"src:url('{POLICES}{w}-{st}.woff2') format('woff2')}}"
    for w in (400, 700) for st in ('normal', 'italic'))
# Feuille commune (ordre de Vial du 10.11.2026, révisé) : lisibilité d'abord — encre quasi noire sur blanc pur,
# gras 700 nettement distinct, fonds chauds très pâles, accents chauds sombres (contraste AA), aucun bleu ni violet,
# colonne de texte ≈ 60 % de la page centrée à droite d'un menu latéral clair. Aucun script.
CSS_LISIBLE = """
:root{--fm-fond:#fff;--fm-encre:#0b0b0b;--fm-noir:#000;--fm-doux:#33291f;--fm-terre:#7f3a20;--fm-vin:#5f2129;
--fm-ambre:#624512;--fm-olive:#3c4d22;--fm-bord:#e4dccf;--fm-pale:#faf7f2;--fm-zebre:#fbfaf7;--fm-tete:#f2ece3;
--fm-menu:#faf8f5;--fm-menu-bord:#e4d5c0;--fm-menu-txt:#140f0b;--fm-col:min(60vw,100%)}
html,body,body *:not(code):not(pre):not(kbd):not(samp){font-family:'Atkinson Hyperlegible',Verdana,'Segoe UI',system-ui,sans-serif!important}
html{scroll-behavior:auto;-webkit-text-size-adjust:100%}
html,body{background:var(--fm-fond)!important;color:var(--fm-encre)!important}
body{margin:0!important;padding:0 24px 4rem 300px!important;max-width:none!important;width:auto!important;
font-size:17px;font-weight:400;line-height:1.42!important;text-rendering:optimizeLegibility;font-kerning:normal}
body>*:not(#brain-barre14):not([popover]):not(script):not(style){box-sizing:border-box;max-width:var(--fm-col)!important;
width:auto!important;margin-left:auto!important;margin-right:auto!important}
main,article,.wrap,.page,.contenu,.monographie,.monograph,body>section{max-width:none!important;width:auto!important;
background:transparent!important;box-shadow:none!important}
main,article{padding:.4rem 0 2rem!important}
img,svg,video{max-width:100%!important;height:auto}
p,.p,li,dd,dt,blockquote,figcaption,caption,td,label{color:var(--fm-encre)!important}
p,.p,li,dd,blockquote,.df{text-align:justify;hyphens:auto;-webkit-hyphens:auto}
p,.p{margin:.4em 0!important}li{margin:.18em 0}ul,ol{padding-left:1.35em}
b,strong{font-weight:700!important}
p b,p strong,.p b,.p strong,li b,li strong,td b,td strong,dd b,dd strong,blockquote b{color:var(--fm-noir)!important}
em,i{font-style:italic}
h1,h2,h3,h4,h5,h6,td,th,caption,figcaption,nav li,.ls li{text-align:left;hyphens:manual}
h1,h2,h3,h4,h5{font-weight:700!important;line-height:1.22;letter-spacing:-.005em}
h1{color:#0f0b08;font-size:2.05em;margin:.5em 0 .45em}
h2{color:var(--fm-vin);font-size:1.5em;margin:1.5em 0 .5em;padding-bottom:.28em;border-bottom:2px solid var(--fm-bord)}
h3{color:var(--fm-terre);font-size:1.22em;margin:1.25em 0 .4em}
h4{color:var(--fm-ambre);font-size:1.06em;margin:1em 0 .3em}
h5,h6{color:var(--fm-doux);font-size:1em;margin:.9em 0 .3em}
a{color:var(--fm-terre);text-decoration-thickness:1px;text-underline-offset:2px}a:visited{color:var(--fm-vin)}
a:hover{color:var(--fm-vin)}
[id]{scroll-margin-top:16px}
hr{border:0;border-top:1px solid var(--fm-bord);margin:1.4em 0}
nav[aria-label="Plan"],nav[aria-label="Navigation"]{display:none!important}
#brain-barre14{box-sizing:border-box!important;position:fixed!important;top:0!important;left:0!important;right:auto!important;bottom:0!important;width:268px!important;
max-width:none!important;margin:0!important;display:flex!important;flex-direction:column!important;flex-wrap:nowrap!important;
align-items:stretch!important;justify-content:flex-start!important;gap:1px!important;overflow-y:auto!important;overflow-x:hidden!important;
z-index:95!important;background:var(--fm-menu)!important;color:var(--fm-menu-txt)!important;padding:20px 12px 28px!important;
border-right:1px solid var(--fm-menu-bord)!important;box-shadow:none!important;scrollbar-width:thin;scrollbar-color:#d9c6ab transparent}
#brain-barre14::before{content:"Parties du cours";display:block;font:700 12px/1.2 'Atkinson Hyperlegible',Verdana,sans-serif;
letter-spacing:.12em;text-transform:uppercase;color:var(--fm-a,#7c2431);margin:0 10px 12px;padding-bottom:10px;border-bottom:2px solid var(--fm-a-doux,#ead7bb)}
#brain-barre14 a{display:flex!important;flex:0 0 auto!important;gap:11px!important;align-items:center!important;padding:6px 10px 6px 8px!important;
margin:0!important;border:0!important;border-left:3px solid transparent!important;border-radius:0 8px 8px 0!important;min-height:0!important;
white-space:normal!important;color:var(--fm-menu-txt)!important;background:transparent!important;text-decoration:none!important;
font:400 14.5px/1.28 'Atkinson Hyperlegible',Verdana,sans-serif!important;outline:0!important;box-shadow:none!important;text-align:left!important}
#brain-barre14 a b{display:inline-flex!important;align-items:center!important;justify-content:center!important;flex:0 0 27px!important;
width:27px!important;min-width:27px!important;height:27px!important;padding:0!important;margin:0!important;border-radius:50%!important;
background:var(--fm-a-pale,#f1e0c6)!important;color:var(--fm-a,#6b3412)!important;font:700 12px/1 'Atkinson Hyperlegible',Verdana,sans-serif!important;
letter-spacing:-.03em!important;font-variant-numeric:tabular-nums;overflow:hidden;white-space:nowrap!important;box-shadow:inset 0 0 0 1px var(--fm-a-doux,#e2c9a5)}
#brain-barre14 a:hover,#brain-barre14 a:focus-visible{background:var(--fm-a-pale)!important;border-left-color:var(--fm-a-mid)!important;color:#000!important}
#brain-barre14 a:hover b,#brain-barre14 a:focus-visible b{background:var(--fm-a-doux)!important;color:var(--fm-a)!important}
#brain-barre14 a:focus-visible{outline:2px solid var(--fm-a)!important;outline-offset:-2px!important}
#brain-barre14 a.fm-actif,#brain-barre14 a[aria-current]{background:var(--fm-a-doux)!important;border-left-color:var(--fm-a)!important;color:#000!important;font-weight:700!important}
#brain-barre14 a.fm-actif b,#brain-barre14 a[aria-current] b{background:var(--fm-a)!important;color:#fff!important;box-shadow:none!important}
#brain-barre14 a:target{background:var(--fm-a-pale)!important}
#brain-barre14.fm-dyn{background-image:linear-gradient(var(--fm-a-mid),var(--fm-a-mid))!important;background-repeat:no-repeat!important;
background-size:3px calc(var(--fm-prog,0)*100%)!important;background-position:right top!important}
#fm-bandeau{position:relative;margin-top:0!important;margin-bottom:1.1rem!important;padding:30px 34px 24px!important;background:var(--fm-a-pale)!important;
border-left:7px solid var(--fm-a)!important;border-radius:0 0 18px 18px;box-shadow:0 1px 0 var(--fm-a-doux)}
#fm-bandeau .fm-code{display:flex;flex-wrap:wrap;gap:6px 14px;align-items:baseline;margin:0 0 .5em!important;text-align:left!important;color:var(--fm-a)!important;
font-size:13px!important;font-weight:700!important;letter-spacing:.13em;text-transform:uppercase}
#fm-bandeau .fm-phase{font-weight:400;letter-spacing:.04em;text-transform:none;color:#241d18;font-size:14px}
#fm-bandeau .fm-nom{margin:0!important;color:#111!important;font-size:clamp(1.9rem,2.7vw,2.75rem)!important;font-weight:700!important;line-height:1.1!important;
text-align:left!important;hyphens:manual!important;letter-spacing:-.012em}
.fm-double{display:none!important}
table{border-collapse:separate!important;border-spacing:0!important;width:100%;background:#fff!important;border:1px solid var(--fm-bord)!important;
border-radius:10px;overflow:hidden;margin:.7em 0 1.1em;font-size:.95em;line-height:1.38}
th{background:var(--fm-tete)!important;color:#140b06!important;font-weight:700!important;text-align:left;vertical-align:bottom;
padding:.55em .75em!important;border:0!important;border-bottom:2px solid #dcc09b!important;border-right:1px solid #ecdcc4!important}
td{padding:.5em .75em!important;vertical-align:top;border:0!important;border-top:1px solid #efe4d5!important;border-right:1px solid #f3eadd!important}
th:last-child,td:last-child{border-right:0!important}
tr:first-child>td{border-top:0!important}
tbody tr:nth-child(even)>td{background-color:var(--fm-zebre)}
tbody tr:hover>td{background-color:#f7f2ea}
caption{caption-side:top;text-align:left;font-weight:700;color:var(--fm-vin)!important;padding:.2em 0 .5em}
sup.r{line-height:0;white-space:nowrap}
sup.r{font-size:.74em!important;vertical-align:super}
sup.r a,.r a{display:inline-block;font-size:.92em!important;line-height:1.3;font-weight:700;padding:0 .3em!important;margin-left:2px;
border-radius:4px;background:#f3ede4!important;color:#6a2e15!important;text-decoration:none!important;vertical-align:baseline}
sup.r a:hover,.r a:hover{background:var(--fm-terre)!important;color:#fff!important}
.tm{color:#6a2e15;border-bottom:1.5px dotted #a4785a;text-decoration:none}
.tm.med{background:#f7f1ea!important;color:#5f2a12!important;border-bottom:1.5px solid #a6704f!important}
.tm .df,.tm.med .df{background:#fffaf2!important;color:var(--fm-encre)!important;border:1px solid #e6d2b6!important;border-left:4px solid var(--fm-terre)!important;
border-radius:10px!important;padding:10px 14px!important;box-shadow:0 14px 34px -10px rgba(70,38,14,.35)!important;line-height:1.45!important;
font-size:.9em!important;font-weight:400!important;text-align:left!important}
.tm .df *{color:inherit}
.tm .df b,.tm .df strong{color:#000!important}
.tm .df .tm{color:#8a3512!important}
button.w{color:var(--fm-terre)!important;border-bottom:1.5px dotted var(--fm-terre)!important;cursor:pointer}
button.w:hover{background:#fbefe2!important}
[popover].fenetre{background:#fff!important;color:var(--fm-encre)!important;border:1px solid #e3cfb2!important;border-top:5px solid var(--fm-terre)!important;
border-radius:14px!important;box-shadow:0 24px 60px -12px rgba(50,26,10,.45)!important;padding:18px 22px!important;line-height:1.45}
.fenetre::backdrop{background:rgba(42,24,12,.32)!important}
details{margin:.55em 0}
details.fenetre>summary{color:var(--fm-olive)!important;font-weight:700}
details.fenetre[open]{background:var(--fm-pale);border-left:4px solid var(--fm-a-mid,#c27a3a);padding:.5em 1em;border-radius:0 10px 10px 0;margin:.5em 0}
details.fenetre[open]>summary{display:block!important;margin-bottom:.3em}
details>div,details>p,details>ul,details>ol{color:var(--fm-encre)}
#fm-bandeau~header h1,#fm-bandeau~h1,#fm-bandeau~* header h1{font-size:1.2em!important;color:var(--fm-doux)!important;margin:.6em 0 .4em!important}
details:not([class]){border:1px solid var(--fm-bord);border-radius:10px;background:var(--fm-pale);padding:.45em .95em}
details:not([class])>summary{cursor:pointer;font-weight:700;color:var(--fm-vin)}
details:not([class])[open]>summary{margin-bottom:.35em;padding-bottom:.35em;border-bottom:1px solid var(--fm-bord)}
figure.cliche-guide,.cliche-guide{background:var(--fm-pale)!important;border:1px solid var(--fm-bord)!important;border-radius:12px!important;
padding:12px 16px!important;margin:1em 0!important}
.cliche-guide img{border-radius:8px;background:#fff}
.cliche-guide figcaption{font-size:.88em!important;color:var(--fm-doux)!important;margin-top:.5em;line-height:1.38}
blockquote{border-left:4px solid #e2bf8f;background:var(--fm-pale);margin:.8em 0;padding:.5em 1em;border-radius:0 8px 8px 0}
.alert{background:#fbf5f2!important;border-left:4px solid var(--fm-vin)!important;color:var(--fm-encre)!important}
.key{background:var(--fm-pale)!important;border-left:4px solid var(--fm-ambre)!important;color:var(--fm-encre)!important}
.cible,.arbn.cible,li.cible{background:#fbe7cc!important;border-color:#d9a25e!important;color:#161616!important}
.cible b,.cible .dfn,.cible li,.cible .tm,.cible summary,.cible>summary::before{color:#161616!important}
.cible>b,.cible>summary b{color:#000!important}
#__tabs a{color:#5a2a0e!important;background:#faf1e4!important}
#__tabs a.on{background:#f3dcbc!important;color:#000!important}
.n{color:#2d643a!important}
@media (max-width:900px){
:root{--fm-col:100%}
body{padding:62px 16px 3rem!important;font-size:16.5px}
#fm-bandeau{padding:20px 18px 16px!important;border-radius:0 0 12px 12px}
#brain-barre14.fm-dyn{background-size:calc(var(--fm-prog,0)*100%) 3px!important;background-position:left bottom!important}
#brain-barre14{bottom:auto!important;right:0!important;width:auto!important;height:auto!important;flex-direction:row!important;
gap:6px!important;overflow-x:auto!important;overflow-y:hidden!important;padding:8px 10px!important;border-right:0!important;
border-bottom:1px solid var(--fm-menu-bord)!important;scrollbar-width:none}
#brain-barre14::before{display:none}
#brain-barre14 a{white-space:nowrap!important;border-left:0!important;border-radius:999px!important;padding:4px 12px 4px 4px!important;
background:#fff!important;box-shadow:inset 0 0 0 1px var(--fm-menu-bord)!important;font-size:14px!important;gap:7px!important}
#brain-barre14 a b{flex-basis:24px!important;width:24px!important;min-width:24px!important;height:24px!important;font-size:11px!important}
[id]{scroll-margin-top:66px}
table{font-size:.9em}}
@media print{#brain-barre14{display:none!important}body{padding:0!important}body>*{max-width:none!important}}
"""
CSS = FACES + re.sub(r'\n', '', CSS_LISIBLE) + (
    # L1 (10.11.2026) : fenêtre centrale occultante ouverte au clic d'un mot, sans script (:target)
    "section.fenetre{display:none}"
    "section.fenetre:target{display:flex!important;flex-direction:column;position:fixed!important;inset:0!important;z-index:200;overflow:auto;padding:4vh 4vw;background:rgba(20,16,12,.62)!important;max-width:none!important;max-height:none!important;width:auto!important;height:auto!important;margin:0!important;border:0!important;border-radius:0!important;box-shadow:none!important;transform:none!important}"
    "section.fenetre:target>*{margin-top:auto!important;margin-bottom:auto!important;flex:none;width:100%;max-width:min(1100px,94vw);margin:0 auto;background:#fff;color:#161616;padding:6px 28px}"
    "section.fenetre:target>*:first-child{border-radius:14px 14px 0 0;padding-top:22px}"
    "section.fenetre:target>*:last-child{border-radius:0 0 14px 14px;padding-bottom:22px}"
    "section.fenetre a.fermer{float:right;font-weight:700;text-decoration:none}"
    "a.ouvre{font-weight:600;text-decoration:underline dotted;text-underline-offset:3px;cursor:zoom-in;hyphens:manual;-webkit-hyphens:manual}")
# Feuille partagée + unique script externe autorisé (menu dynamique ; ordre de Vial du 10.11.2026, toléré par controle3.py)
BLOC = '<link id="forme-vial" rel="stylesheet" href="../_polices/forme.css"><script src="../_polices/forme.js" defer></script>'
RE_BLOC = re.compile(r'<style id="forme-vial">.*?</style>|<link id="forme-vial"[^>]*>|<script id="forme-vial-js"[^>]*></script>'
                     r'|<script src="\.\./_polices/forme\.js" defer></script>', re.S)
PROTEGES = re.compile(r'(<(script|style|pre|svg|textarea)\b.*?</\2>)', re.S | re.I)


def nettoyer_texte(seg):
    # seg : HTML sans bloc protégé ; on ne touche qu'aux nœuds texte (entre > et <)
    def texte(m):
        t = m.group(1)
        t = re.sub(r'[ \t ]{2,}', ' ', t)
        t = re.sub(r'(?<=\S) +(?=[.,](?:\s|$|<))', '', t)
        return '>' + t + '<'
    seg = re.sub(r'>([^<>]+)<', texte, seg)
    seg = re.sub(r'<p(\s[^>]*)?>\s*</p>', '', seg)
    seg = re.sub(r'\n[ \t]*(?:\n[ \t]*)+', '\n', seg)
    return seg


import colorsys

RE_HEX = re.compile(r'#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b')
RE_RGB = re.compile(r'rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)((?:[,\s/]+[\d.]+%?)?)\s*\)')


def chaud(r, g, b):
    """Sarcelle (150–178°) → olive ; bleu à violet (178–305°) → terre cuite à ambre (14–40°) ; luminosité gardée."""
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    deg = h * 360
    if s < 0.12 or not 150 <= deg <= 305:
        return None
    if deg < 178:  # vert d'eau, sarcelle → olive (aucune teinte apparentée au bleu)
        r2, g2, b2 = colorsys.hls_to_rgb(84 / 360, l, min(0.6, s))
        return round(r2 * 255), round(g2 * 255), round(b2 * 255)
    nh = (14 + (deg - 178) / 127 * 26) / 360
    r2, g2, b2 = colorsys.hls_to_rgb(nh, l, min(0.78, max(s, 0.35)))
    return round(r2 * 255), round(g2 * 255), round(b2 * 255)


def sans_bleu(css):
    def hx(m):
        v = m.group(1)
        if len(v) == 3:
            v = ''.join(c * 2 for c in v)
        n = chaud(int(v[0:2], 16), int(v[2:4], 16), int(v[4:6], 16))
        return m.group(0) if n is None else '#%02x%02x%02x' % n
    def rg(m):
        n = chaud(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        if n is None:
            return m.group(0)
        a = m.group(4)
        return f"rgba({n[0]},{n[1]},{n[2]}{',' + a.strip(' ,/') if a.strip(' ,/') else ''})" if a.strip() else f"rgb({n[0]},{n[1]},{n[2]})"
    return RE_RGB.sub(rg, RE_HEX.sub(hx, css))


def recolorer(h):
    h = re.sub(r'(<style\b[^>]*>)(.*?)(</style>)', lambda m: m.group(1) + sans_bleu(m.group(2)) + m.group(3), h, flags=re.S | re.I)
    h = re.sub(r'(\sstyle=")([^"]*)(")', lambda m: m.group(1) + sans_bleu(m.group(2)) + m.group(3), h)
    h = re.sub(r'(\s(?:fill|stroke|color|bgcolor)=")([^"]*)(")', lambda m: m.group(1) + sans_bleu(m.group(2)) + m.group(3), h)
    return h


def ajouter_menu(h):
    """Menu des parties : si la leçon n'a pas de #brain-barre14, il est construit à partir des titres h2."""
    if 'id="brain-barre14"' in h:
        return h
    liens, n = [], [0]
    def ident(m):
        attrs, txt = m.group(1), m.group(2)
        lib = re.sub(r'<[^>]+>', '', txt).strip()
        if not lib:
            return m.group(0)
        mid = re.search(r'\sid="([^"]+)"', attrs)
        if not mid:
            n[0] += 1
            i = f'fm-{n[0]}'
            attrs += f' id="{i}"'
        else:
            i = mid.group(1)
        liens.append((i, lib))
        return f'<h2{attrs}>{txt}</h2>'
    h2 = re.sub(r'<h2((?:\s[^>]*)?)>(.*?)</h2>', ident, h, flags=re.S)
    if len(liens) < 5:  # leçons dont les parties numérotées « 1. … 14. » sont en h3
        liens.clear(); n[0] = 0
        def ident3(m):
            attrs, txt = m.group(1), m.group(2)
            lib = re.sub(r'<[^>]+>', '', txt).strip()
            if not re.match(r'^(?:\d{1,2}\.|Sources|Bibliographie)', lib):
                return m.group(0)
            mid = re.search(r'\sid="([^"]+)"', attrs)
            if not mid:
                n[0] += 1; i = f'fm-{n[0]}'; attrs += f' id="{i}"'
            else:
                i = mid.group(1)
            liens.append((i, lib))
            return f'<h3{attrs}>{txt}</h3>'
        h2 = re.sub(r'<h3((?:\s[^>]*)?)>(.*?)</h3>', ident3, h, flags=re.S)
    if len(liens) < 3:
        return h
    nav = '<nav id="brain-barre14" aria-label="Parties du cours">' + ''.join(
        f'<a href="#{i}"><b>{k}</b>{re.sub(r"^[0-9.\s]+", "", lib)[:60]}</a>' for k, (i, lib) in enumerate(liens, 1)) + '</nav>'
    return re.sub(r'(<body\b[^>]*>)', lambda m: m.group(1) + nav, h2, count=1)


def _fin_bloc(h, debut, nom):
    """Position juste après la balise fermante appariée de <nom> ouverte en `debut` (imbrication comprise)."""
    prof = 0
    for m in re.finditer(rf'<(/?){nom}\b[^>]*>', h[debut:], re.I):
        prof += -1 if m.group(1) else 1
        if prof == 0:
            return debut + m.end()
    return -1


def retirer_sommaire(h):
    """Ordre de Vial : aucun sommaire interne en boutons ou pastilles en haut du cours ; seul le menu latéral reste.
    Repère, avant le corps du cours, un bloc nav/div/ul/ol/p fait presque uniquement de liens internes vers les parties.
    Les liens qu'il est seul à porter (Bloc 2, Tableau, Algorithme…) rejoignent le menu latéral avant d'être retirés."""
    mm = re.search(r'<nav id="brain-barre14".*?</nav>', h, re.S)
    if not mm:
        return h
    lim = re.search(r'id="[\w-]*p2"', h[mm.end():])
    limite = mm.end() + (lim.start() if lim else len(h) * 3 // 10)
    pos = mm.end()
    while True:
        m = re.compile(r'<(nav|div|ul|ol|p)\b([^>]*)>', re.I).search(h, pos, limite)
        if not m:
            return h
        nom = m.group(1).lower()
        fin = _fin_bloc(h, m.start(), nom)
        if fin < 0:
            pos = m.end(); continue
        bloc = h[m.start():fin]
        liens = re.findall(r'<a\b[^>]*href="#([^"]+)"[^>]*>(.*?)</a>', bloc, re.S)
        hors = re.sub(r'<a\b.*?</a>', '', bloc, flags=re.S)
        hors = re.sub(r'<[^>]+>', '', hors)
        hors = re.sub(r'[\s·•|,;–—\-/]+', '', hors)
        if (len(liens) >= 5 and len(hors) <= 15 and 'class="r"' not in bloc and 'class="tm' not in bloc
                and all(re.search(rf'id="{re.escape(i)}"', h) for i, _ in liens)):
            menu = mm.group(0)
            if len(re.findall(r'<a\b', menu)) < 6:  # menu construit faute de mieux : on le refait depuis le sommaire
                menu = re.sub(r'<a\b.*?</a>', '', menu, flags=re.S)
            deja = set(re.findall(r'href="#([^"]+)"', menu))
            ajout = ''
            for i, txt in liens:
                if i in deja or (re.sub(r'<[^>]+>', '', txt).strip().lower().startswith('source') and '<b>§</b>' in menu):
                    continue
                lib = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', txt)).strip()
                t = re.search(rf'<(h[1-4])\b[^>]*id="{re.escape(i)}"[^>]*>(.*?)</\1>', h, re.S)
                if t:
                    lib = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', t.group(2))).strip() or lib
                num = re.match(r'(\d{1,2})[.)]?\s+', lib)
                marque = num.group(1) if num else ('§' if lib.lower().startswith(('source', 'bibli', 'référ')) else '◆')
                lib = lib[num.end():] if num else lib
                ajout += f'<a href="#{i}"><b>{marque}</b>{lib}</a>'
                deja.add(i)
            if ajout:
                k = menu.rfind('<a href="#', 0, menu.rfind('</nav>'))
                dernier_src = re.search(r'<b>§</b>', menu[k:])
                pos_ins = k if dernier_src else menu.rfind('</nav>')
                menu = menu[:pos_ins] + ajout + menu[pos_ins:]
            h = h[:mm.start()] + menu + h[mm.end():m.start()] + h[fin:]
            return retirer_sommaire(h)
        pos = m.end()


def teinte(nom):
    """Couleur d'accent propre à chaque leçon, déterministe : angle d'or sur un hachage du nom de fichier,
    dans les 175° autorisés (0–150° et 335–360° : jamais de bleu, cyan, indigo, violet ni mauve)."""
    import zlib
    k = zlib.crc32(nom.encode('utf-8'))
    a = (k * 137.50776405) % 175
    h = a if a < 150 else a + 185
    def hx(l, s):
        r, g, b = colorsys.hls_to_rgb(h / 360, l, s)
        return '#%02x%02x%02x' % (round(r * 255), round(g * 255), round(b * 255))
    return hx(.27, .42), hx(.46, .34), hx(.965, .40), hx(.915, .34)


def _texte(x):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', x)).replace('&amp;', '&').strip()


def bandeau(h, nom):
    """En-tête : le nom du diagnostic (DX) ou du SSP (Phase A), en grand, le code en petit ; accent propre à la leçon.
    Le titre d'origine identique est conservé dans le fichier mais masqué (classe fm-double) pour éviter le doublon."""
    h = re.sub(r'<header id="fm-bandeau".*?</header>', '', h, flags=re.S)
    h = re.sub(r'(<h[1-3]\b[^>]*?) class="fm-double"', r'\1', h).replace('class="fm-double ', 'class="')
    a, m, p, p2 = teinte(nom)
    h = re.sub(r'<body\b[^>]*>', f'<body style="--fm-a:{a};--fm-a-mid:{m};--fm-a-pale:{p};--fm-a-doux:{p2}">', h, count=1)
    lot = re.match(r'(LOT_\d+)', nom)
    lot = lot.group(1) if lot else ''
    dx = re.search(r'DX\.(\d+)', nom)
    titre = None
    if dx:
        for t in re.finditer(r'<(h[1-3])\b([^>]*)>(.*?)</\1>', h, re.S):
            tx = _texte(t.group(3))
            mm = re.match(rf'DX\.{dx.group(1)}\s*[—–:-]\s*(.+)', tx)
            if mm:
                titre, cible = mm.group(1), t
                break
        code, phase = f'{lot} · DX.{dx.group(1)}', 'Phase B · diagnostic différentiel'
    else:
        cible = re.search(r'<(h1)\b([^>]*)>(.*?)</\1>', h, re.S)
        titre = _texte(cible.group(3)) if cible else None
        g = re.search(r'<title>[^<]*?\b(G\d+)\b', h)
        code, phase = f'{lot} · SSP {g.group(1)}' if g else lot, 'Phase A · situation clinique de départ'
    if not titre:
        t = re.search(r'<title>([^<]+)</title>', h)
        titre, cible = (_texte(t.group(1)) if t else nom), None
    if cible is not None:
        balise = cible.group(0)
        n = re.sub(r'^<(h[1-3])\b', r'<\1 class="fm-double"', balise) if 'class=' not in balise.split('>')[0] else \
            re.sub(r'class="', 'class="fm-double ', balise, count=1)
        h = h.replace(balise, n, 1)
    bloc = (f'<header id="fm-bandeau"><div class="fm-code"><span>{code}</span><span class="fm-phase">{phase}</span></div>'
            f'<div class="fm-nom">{titre}</div></header>')
    mm = re.search(r'<nav id="brain-barre14".*?</nav>', h, re.S)
    if mm:
        return h[:mm.end()] + bloc + h[mm.end():]
    return re.sub(r'(<body\b[^>]*>)', lambda x: x.group(1) + bloc, h, count=1)


def corriger(h, nom=''):
    h = retirer_sommaire(ajouter_menu(RE_BLOC.sub('', h)))
    parts = PROTEGES.split(h)
    out = []
    i = 0
    while i < len(parts):
        out.append(nettoyer_texte(parts[i]))
        if i + 1 < len(parts):
            out.append(parts[i + 1])  # bloc protégé intact
        i += 3
    h = ''.join(out)
    h = recolorer(h)
    h = bandeau(h, nom)
    if '</head>' in h:
        h = h.replace('</head>', BLOC + '</head>', 1)
    else:
        h = BLOC + h
    return h


def ecrire_css(dossier):
    import os
    open(os.path.join(dossier, 'forme.css'), 'w', encoding='utf-8').write(CSS + '\n')


if __name__ == '__main__':
    import os
    ecrire_css(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '_polices'))
    verif = '--verifier' in sys.argv
    fichiers = [a for a in sys.argv[1:] if not a.startswith('--')]
    change = 0
    for f in fichiers:
        h = open(f, encoding='utf-8').read()
        n = corriger(h, os.path.basename(f))
        if n != h:
            change += 1
            if not verif:
                open(f, 'w', encoding='utf-8').write(n)
        print(f"{f.split('/')[-1]} {'à corriger' if verif and n != h else ('corrigé' if n != h else 'conforme')} "
              f"{len(h.encode())}→{len(n.encode())} o")
    sys.exit(1 if verif and change else 0)
