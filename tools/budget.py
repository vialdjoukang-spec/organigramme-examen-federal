#!/usr/bin/env python3
"""Budgets de taille (Héphaïstos, étendus par Atlas le 17.10.2026 pour le chantier Nerfs crâniens et CK) :
app_v2.html ≤ 6 Mo ; chaque image de assets/ ≤ 200 Ko ; assets/ck/ ≤ 2,5 Mo au total ;
chaque SVG ≤ 120 Ko ; assets/nc/ ≤ 3 Mo au total ; assets/mono/ (monographies, Hygie, chargées à la demande)
≤ 6 Mo au total, budget séparé décidé par Vial le 17.10.2026. Les plafonds se surchargent par variable
d'environnement pour les tests des gardes (APP_MAX_BYTES, CK_MAX_BYTES, SVG_MAX_BYTES, NC_MAX_BYTES, MONO_MAX_BYTES).
"""
import os, sys
if len(sys.argv) > 1 and sys.argv[1] == '--lignes':  # Arsenal : signale une lecture de plus de N lignes.
    n = int(sys.argv[2]); trop = []
    for f in sys.argv[3:]:
        t = open(f, encoding='utf-8', errors='replace').read(); k = max(t.count('\n'), len(t) // 120)  # lignes équivalentes
        if k > n: trop.append(f'{f} ({k} l.)')
    print(('LECTURE TROP LONGUE > %d l. : ' % n + ', '.join(trop) + ' → tools/arsenal/extrait.py ou tools/slim.py') if trop else 'OK lecture')
    sys.exit(1 if trop else 0)
from _app import ROOT, APP
APP_MAX = int(os.environ.get('APP_MAX_BYTES', 6_000_000))
CK_MAX = int(os.environ.get('CK_MAX_BYTES', 2_500_000))
SVG_MAX = int(os.environ.get('SVG_MAX_BYTES', 120 * 1024))
NC_MAX = int(os.environ.get('NC_MAX_BYTES', 3_000_000))
MONO_MAX = int(os.environ.get('MONO_MAX_BYTES', 6_000_000))
TIP_MAX = 12 * 1024 * 1024
IMG_MAX = 200 * 1024
IMG_EXT = {'.webp', '.png', '.jpg', '.jpeg', '.gif', '.avif'}
root = os.environ.get('BUDGET_ROOT', ROOT)
app = os.path.join(root, 'app_v2.html') if 'BUDGET_ROOT' in os.environ else APP


def fmt(n):
    return f'{n:,}'.replace(',', ' ')


def total(d):
    d = os.path.join(root, d)
    return sum(os.path.getsize(os.path.join(a, n)) for a, _, fs in os.walk(d) for n in fs) if os.path.isdir(d) else 0


fails = []
size = os.path.getsize(app)
print(f'app_v2.html : {fmt(size)} octets (budget {fmt(APP_MAX)}).')
if size > APP_MAX:
    fails.append('app_v2.html dépasse le budget')
tip_asset = os.path.join(root, 'assets/config/tip.js')
if os.path.isfile(tip_asset):
    tip_size = os.path.getsize(tip_asset)
    print(f'assets/config/tip.js : {fmt(tip_size)} octets (budget {fmt(TIP_MAX)}).')
    if tip_size > TIP_MAX:
        fails.append('assets/config/tip.js dépasse le budget')
for d, _, files in os.walk(os.path.join(root, 'assets')):
    for n in files:
        p = os.path.join(d, n)
        ext = os.path.splitext(n)[1].lower()
        if ext in IMG_EXT and os.path.getsize(p) > IMG_MAX:
            fails.append(f'{os.path.relpath(p, root)} dépasse 200 Ko')
        if ext == '.svg' and os.path.getsize(p) > SVG_MAX:
            fails.append(f'{os.path.relpath(p, root)} dépasse {fmt(SVG_MAX)} octets (SVG)')
for d, mx in (('assets/ck', CK_MAX), ('assets/nc', NC_MAX), ('assets/mono', MONO_MAX)):
    t = total(d)
    print(f'{d}/ : {fmt(t)} octets (budget {fmt(mx)}).')
    if t > mx:
        fails.append(f'{d}/ dépasse le budget')
for f in fails:
    print('ÉCHEC', f)
sys.exit(1 if fails else 0)
