#!/usr/bin/env python3
"""Hermès · compile chaque schéma de nerf en chaîne JS insérable, pour que les couches fonctionnent aussi en file://.

assets/nc/ncXX-<vue>.svg  →  assets/nc/ncXX.js : (window.CK_SVG=window.CK_SVG||{})["assets/nc/ncXX-<vue>.svg"]="<svg…>";
L'application charge ncXX.js au premier affichage du schéma (<script src>, compatible file://) ; sans ce fichier, elle
affiche le SVG par <img> et désactive les couches. Sortie stable (tri, JSON compact) : rejouer donne le même octet.
Usage : python3 tools/nc_svg_js.py [--src assets/nc] [--check]
"""
import argparse, glob, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def build(src):
    out = {}
    for f in sorted(glob.glob(os.path.join(src, '*.svg'))):
        m = re.match(r'^([a-zA-Z]+\d*[A-Za-z]?)-[^/]+\.svg$', os.path.basename(f))
        if not m:
            continue
        rel = os.path.relpath(f, ROOT).replace(os.sep, '/')
        txt = open(f, encoding='utf-8').read().strip()
        assert '<script' not in txt.lower(), f'{rel} : balise script interdite'
        out.setdefault(m.group(1), []).append((rel, txt))
    return {os.path.join(src, k + '.js'): '/* Généré par tools/nc_svg_js.py : ne pas modifier à la main. */\n' + ''.join(
        f'(window.CK_SVG=window.CK_SVG||{{}})[{json.dumps(r)}]={json.dumps(t, ensure_ascii=False)};\n' for r, t in v) for k, v in out.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', default=os.path.join(ROOT, 'assets', 'nc'))
    ap.add_argument('--check', action='store_true', help='échoue si un fichier JS manque ou diffère')
    a = ap.parse_args()
    if not os.path.isdir(a.src):
        print(f'Aucun dossier {a.src} : rien à compiler.'); return 0
    bad = 0
    for p, js in build(os.path.abspath(a.src)).items():
        cur = open(p, encoding='utf-8').read() if os.path.exists(p) else None
        if cur == js:
            continue
        if a.check:
            print(f'ÉCHEC : {os.path.relpath(p, ROOT)} est absent ou périmé (lancez tools/nc_svg_js.py).'); bad += 1
        else:
            open(p, 'w', encoding='utf-8').write(js); print(f'écrit : {os.path.relpath(p, ROOT)}')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
