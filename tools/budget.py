#!/usr/bin/env python3
"""Budgets : app_v2.html ≤ 6 Mo ; chaque image de assets/ ≤ 200 Ko."""
import os, sys
from _app import ROOT, APP
APP_MAX = int(os.environ.get('APP_MAX_BYTES', 6_000_000))
IMG_MAX = 200 * 1024
IMG_EXT = {'.webp', '.png', '.jpg', '.jpeg', '.gif', '.avif'}

fails = []
size = os.path.getsize(APP)
print(f'app_v2.html : {size:,} octets (budget {APP_MAX:,}).'.replace(',', ' '))
if size > APP_MAX:
    fails.append('app_v2.html dépasse le budget')
for d, _, files in os.walk(os.path.join(ROOT, 'assets')):
    for n in files:
        p = os.path.join(d, n)
        if os.path.splitext(n)[1].lower() in IMG_EXT and os.path.getsize(p) > IMG_MAX:
            fails.append(f'{os.path.relpath(p, ROOT)} dépasse 200 Ko')
for f in fails:
    print('ÉCHEC', f)
sys.exit(1 if fails else 0)
