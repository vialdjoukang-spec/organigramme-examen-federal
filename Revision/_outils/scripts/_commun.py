# -*- coding: utf-8 -*-
"""Fonctions partagées des scripts Revision (chemins, MAP, lecture LISTE_DX, JSON SSP)."""
import json, os, re, glob
REV = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
GROK = os.path.dirname(REV)
MAP_PATH = os.path.join(REV, '_index', 'MAP_G1_G16.json')

def load_map():
    return json.load(open(MAP_PATH, encoding='utf-8'))

def ssp_entry(code):
    code = code.upper().replace('G0', 'G') if re.fullmatch(r'G0\d', code.upper()) else code.upper()
    for s in load_map()['ssp']:
        if s['code'] == code: return s
    raise SystemExit(f"SSP inconnu dans MAP : {code}")

def entry_for_dir(d):
    d = os.path.abspath(d)
    for s in load_map()['ssp']:
        if os.path.abspath(os.path.join(REV, s['dossier'])) == d: return s
    raise SystemExit(f"Dossier hors MAP : {d}")

def ssp_dir(s): return os.path.join(REV, s['dossier'])

def lot_dir(s): return os.path.join(GROK, s['source'])

def liste_dx(s):
    """Lit LISTE_DX_CANONIQUE.md du LOT source → [(id, nom)]."""
    t = open(os.path.join(lot_dir(s), 'LISTE_DX_CANONIQUE.md'), encoding='utf-8').read()
    return [(m.group(1), m.group(2).strip()) for m in re.finditer(r'^(DX\.\d+)\s*[—-]\s*(.+)$', t, re.M)]

def ssp_json(s):
    p = glob.glob(os.path.join(ssp_dir(s), 'LOT_*_TypeA_Reflexe.json'))
    return json.load(open(p[0], encoding='utf-8')) if p else None

def dx_ids(dx):
    out = []
    for m in re.findall(r'DX\.(\d+)', dx or ''):
        k = 'DX.' + m
        if k not in out: out.append(k)
    return out
