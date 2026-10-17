#!/usr/bin/env python3
"""Janus · contrôle des schémas de nerfs crâniens (assets/nc/*.svg) pour Dédale.

Chaque SVG : XML valide ; couches nommées obligatoires <g id="trait">, <g id="nerf">, <g id="legendes">
(facultatives : noyaux, foramens, territoires, lesions) ; aucun <script>, aucun gestionnaire on…,
aucune ressource externe (href http, compatible file:// et hors ligne) ; poids ≤ 120 Ko (tools/budget.py) ;
une entrée dans assets/nc/credits.json (source, auteur, licence admise, url, derive).
Sans aucun SVG, le contrôle réussit (NC-0).
"""
import argparse, json, os, re, sys
import xml.etree.ElementTree as ET
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COUCHES = ('trait', 'nerf', 'legendes')
FACULTATIVES = ('noyaux', 'foramens', 'territoires', 'lesions')
LICENCES = re.compile(r'^(CC BY(-SA)? [0-9.]+|CC0 1\.0|Domaine public|PD)$')
MAX = 120 * 1024


def check(root):
    d = os.path.join(root, 'assets', 'nc')
    errs = []
    if not os.path.isdir(d):
        return errs, 0
    svgs = sorted(n for n in os.listdir(d) if n.endswith('.svg'))
    cred = {}
    cp = os.path.join(d, 'credits.json')
    if svgs:
        if not os.path.exists(cp):
            return [f'assets/nc/credits.json absent ({len(svgs)} SVG)'], len(svgs)
        cred = {c.get('fichier'): c for c in json.load(open(cp, encoding='utf-8'))}
    for n in svgs:
        p = os.path.join(d, n)
        raw = open(p, encoding='utf-8').read()
        if os.path.getsize(p) > MAX:
            errs.append(f'{n} : {os.path.getsize(p)} octets, au-delà de 120 Ko')
        try:
            t = ET.fromstring(raw)
        except ET.ParseError as e:
            errs.append(f'{n} : XML invalide ({e})')
            continue
        ids = {el.get('id') for el in t.iter() if el.tag.endswith('}g') or el.tag == 'g'}
        for c in COUCHES:
            if c not in ids:
                errs.append(f'{n} : couche <g id="{c}"> absente')
        if re.search(r'<script\b|\son[a-z]+\s*=', raw, re.I):
            errs.append(f'{n} : script ou gestionnaire d’événement interdit')
        if re.search(r'(?:xlink:)?href\s*=\s*["\']https?:', raw, re.I):
            errs.append(f'{n} : ressource externe interdite (hors ligne)')
        c = cred.get(n)
        if not c:
            errs.append(f'{n} : aucune entrée dans assets/nc/credits.json')
            continue
        for k in ('source', 'auteur', 'licence', 'url', 'derive'):
            if k not in c:
                errs.append(f'{n} : crédit sans champ {k}')
        if c.get('licence') and not LICENCES.match(c['licence']):
            errs.append(f'{n} : licence « {c["licence"]} » non admise (CC BY, CC BY-SA, CC0, domaine public)')
        if c.get('derive') and not str(c.get('licence_derivee', '')).startswith('CC BY-SA'):
            errs.append(f'{n} : vue dérivée sans licence_derivee CC BY-SA (décision du 17.10.2026)')
    return errs, len(svgs)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--racine', default=ROOT)
    a = ap.parse_args(argv)
    errs, n = check(a.racine)
    for e in errs:
        print('ÉCHEC', e)
    print(f'Schémas des nerfs : {n} SVG, {"conformes" if not errs else f"{len(errs)} échec(s)"}.')
    return 1 if errs else 0


if __name__ == '__main__':
    sys.exit(main())
