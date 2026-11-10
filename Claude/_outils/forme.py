#!/usr/bin/env python3
"""FORME — correction automatique de la forme des cours (ordre de Vial du 10.11.2026), zéro modèle, idempotent.

1. Police obligatoire : Atkinson Hyperlegible, chargée depuis Claude/_polices/ (fichiers partagés, aucun octet
   ajouté à la leçon hormis ~1 Ko de CSS ; la bande 100–200 Ko reste respectée).
2. Mise en page : texte courant justifié avec césure, interligne réduit (1,4), marges de paragraphe resserrées ;
   titres, tableaux, figures et listes de navigation restent alignés à gauche.
3. Espaces inutiles : lignes vides multiples, paragraphes vides, espaces doubles dans le texte, espace avant
   « . » ou « , ». Les blocs <script>, <style>, <pre>, <svg> et les attributs ne sont jamais touchés.

Usage : python3 Claude/_outils/forme.py Claude/LOT_00X/*.html   (--verifier : code 1 si un fichier changerait)
"""
import re, sys

POLICES = '../_polices/atkinson-hyperlegible-latin-'
FACES = ''.join(
    f"@font-face{{font-family:'Atkinson Hyperlegible';font-style:{st};font-weight:{w};font-display:swap;"
    f"src:url('{POLICES}{w}-{st}.woff2') format('woff2')}}"
    for w in (400, 700) for st in ('normal', 'italic'))
CSS = (FACES +
       "html,body,p,li,td,th,dd,dt,div,span,figcaption,summary,details,button,input,select{"
       "font-family:'Atkinson Hyperlegible',Verdana,'Segoe UI',system-ui,sans-serif!important}"
       "body{line-height:1.4!important}"
       "p,.p,li,dd,blockquote,.df{text-align:justify;hyphens:auto;-webkit-hyphens:auto}"
       "p,.p{margin:.35em 0}li{margin:.15em 0}"
       "h1,h2,h3,h4,h5,h6,td,th,caption,figcaption,nav li,.ls li{text-align:left;hyphens:manual}"
       "h1,h2,h3,h4{line-height:1.2;margin:.8em 0 .35em}")
BLOC = f'<style id="forme-vial">{CSS}</style>'
RE_BLOC = re.compile(r'<style id="forme-vial">.*?</style>', re.S)
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
    if '</head>' in h:
        h = h.replace('</head>', BLOC + '</head>', 1)
    else:
        h = BLOC + h
    return h


if __name__ == '__main__':
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
