#!/usr/bin/env python3
"""FORME — correction automatique de la forme des cours (ordre de Vial du 10.11.2026), zéro modèle, idempotent.

1. Police obligatoire : Atkinson Hyperlegible, chargée depuis Claude/_polices/ (fichiers partagés, feuille commune
   Claude/_polices/forme.css, ~70 octets ajoutés par leçon ; la bande 100–200 Ko reste respectée).
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
CSS = (FACES +
       "html,body,body *:not(code):not(pre):not(kbd):not(samp){"
       "font-family:'Atkinson Hyperlegible',Verdana,'Segoe UI',system-ui,sans-serif!important}"
       "body{line-height:1.4!important}"
       "p,.p,li,dd,blockquote,.df{text-align:justify;hyphens:auto;-webkit-hyphens:auto}"
       "p,.p{margin:.35em 0}li{margin:.15em 0}"
       "h1,h2,h3,h4,h5,h6,td,th,caption,figcaption,nav li,.ls li{text-align:left;hyphens:manual}"
       "h1,h2,h3,h4{line-height:1.2;margin:.8em 0 .35em}"
       # Palette chaude (ordre de Vial : aucun bleu ni teinte apparentée) et mise en page large
       ":root{--fm-fond:#fbf6ee;--fm-encre:#2a211c;--fm-terre:#b4532a;--fm-ambre:#c9861a;--fm-olive:#5f7a35;"
       "--fm-vin:#8a2c35;--fm-bord:#e7d9c6;--fm-menu:#2f221b;--fm-menu-txt:#f5e7d3}"
       "html,body{background:var(--fm-fond)!important;color:var(--fm-encre)}"
       "a{color:var(--fm-terre)}a:visited{color:var(--fm-vin)}"
       "main,article,.wrap,.page,.contenu,body>section{max-width:none!important;width:auto!important}"
       "body{margin:0!important;padding:0 2.4vw 3rem 312px!important;max-width:none!important}"
       "main *:not(img):not(svg):not(video):not(image),article *:not(img):not(svg):not(video):not(image),body>section *:not(img):not(svg){max-width:none!important}"
       "img,svg,video{max-width:100%!important;height:auto}"
       "main,article{margin:0 auto!important;padding:1.2rem 0!important;max-width:min(1500px,100%)!important}"
       "#brain-barre14{position:fixed!important;top:0!important;left:0!important;right:auto!important;bottom:0!important;width:276px!important;display:flex!important;flex-direction:column!important;flex-wrap:nowrap!important;align-items:stretch!important;justify-content:flex-start!important;gap:2px!important;overflow-y:auto!important;overflow-x:hidden!important;z-index:95!important;"
       "background:var(--fm-menu)!important;color:var(--fm-menu-txt);padding:18px 12px 24px!important;box-shadow:2px 0 14px rgba(0,0,0,.22)!important}""#brain-barre14::before{content:\"Parties du cours\";font-weight:700;font-size:15px;margin:0 8px 12px;color:#f9d9a8}"
                            "#brain-barre14 a{display:flex!important;gap:10px!important;align-items:center!important;padding:7px 10px!important;border-radius:9px!important;min-height:0!important;white-space:normal!important;"
       "color:var(--fm-menu-txt)!important;background:transparent!important;text-decoration:none;font:500 14px/1.3 'Atkinson Hyperlegible',Verdana,sans-serif!important;outline:0!important}"
       "#brain-barre14 a b{background:#e9a54b!important;color:#2f221b!important;min-width:24px!important;height:24px!important;border-radius:12px!important;font-size:12px!important}"
       "#brain-barre14 a:hover,#brain-barre14 a:focus-visible{background:var(--fm-terre)!important;color:#fff!important}"
                     "[id]{scroll-margin-top:14px}"
       "table{border-collapse:collapse}th{background:var(--fm-terre)!important;color:#fff!important}"
       "td,th{border-color:var(--fm-bord)!important}"
       "h2{color:var(--fm-vin)}h3{color:var(--fm-terre)}"
       "@media (max-width:900px){body{padding:64px 14px 3rem!important}"
       "#brain-barre14{bottom:auto!important;right:0!important;width:auto!important;flex-direction:row!important;overflow-x:auto!important;padding:8px!important}"
       "#brain-barre14::before{display:none}#brain-barre14 a{white-space:nowrap!important}}")
BLOC = '<link id="forme-vial" rel="stylesheet" href="../_polices/forme.css">'  # aucun script : contrat C_script_interdit  # feuille partagée : ~70 octets par leçon
RE_BLOC = re.compile(r'<style id="forme-vial">.*?</style>|<link id="forme-vial"[^>]*>|<script id="forme-vial-js"[^>]*></script>', re.S)
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
    """Teinte bleue à violette (165–305°) → terre cuite à ambre (14–40°), luminosité et saturation gardées."""
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    deg = h * 360
    if s < 0.12 or not 165 <= deg <= 305:
        return None
    nh = (14 + (deg - 165) / 140 * 26) / 360
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
    if len(liens) < 3:
        return h
    nav = '<nav id="brain-barre14" aria-label="Parties du cours">' + ''.join(
        f'<a href="#{i}"><b>{k}</b>{re.sub(r"^[0-9.\s]+", "", lib)[:60]}</a>' for k, (i, lib) in enumerate(liens, 1)) + '</nav>'
    return re.sub(r'(<body\b[^>]*>)', lambda m: m.group(1) + nav, h2, count=1)


def corriger(h):
    h = RE_BLOC.sub('', h)
    parts = PROTEGES.split(h)
    out = []
    i = 0
    while i < len(parts):
        out.append(nettoyer_texte(parts[i]))
        if i + 1 < len(parts):
            out.append(parts[i + 1])  # bloc protégé intact
        i += 3
    h = ''.join(out)
    h = recolorer(ajouter_menu(h))
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
        n = corriger(h)
        if n != h:
            change += 1
            if not verif:
                open(f, 'w', encoding='utf-8').write(n)
        print(f"{f.split('/')[-1]} {'à corriger' if verif and n != h else ('corrigé' if n != h else 'conforme')} "
              f"{len(h.encode())}→{len(n.encode())} o")
    sys.exit(1 if verif and change else 0)
