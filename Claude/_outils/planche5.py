#!/usr/bin/env python3
"""PLANCHE5 — une planche HTML autonome par LOT : 5 captures par cours (capture5.py), réduites en JPEG et intégrées.
Les PNG bruts ne sont pas versés au dépôt (15 Mo par LOT) : la planche (≈ 2–3 Mo) s'envoie à Vial et sert de preuve de forme.
Usage : python3 Claude/_outils/planche5.py Claude/LOT_016 [--sortie /chemin/planche.html] [--largeur 1440]"""
import os, sys, glob, base64, subprocess, tempfile, argparse, html, re

ap = argparse.ArgumentParser(); ap.add_argument('lot'); ap.add_argument('--sortie'); ap.add_argument('--largeur', default='1440')
a = ap.parse_args()
lot = os.path.basename(a.lot.rstrip('/'))
ici = os.path.dirname(os.path.abspath(__file__))
tmp = tempfile.mkdtemp(prefix='planche5_')
fichiers = sorted(glob.glob(os.path.join(a.lot, f'{lot}_Phase_*.html')),
                  key=lambda f: (0, 0) if 'Phase_A' in f else (1, int(re.search(r'DX\.(\d+)', f).group(1))))
subprocess.run([sys.executable, os.path.join(ici, 'capture5.py'), *fichiers, '--sortie', tmp, '--largeur', a.largeur], check=True,
               stdout=subprocess.DEVNULL)
JS = r"""
const { chromium } = require('playwright'); const fs = require('fs');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 720, height: 450 } });
  for (const f of process.argv.slice(2)) { await p.setContent('<body style="margin:0"><img src="file://' + f + '" style="width:720px;display:block">');
    await p.goto('file://' + f); await p.evaluate(() => { document.body.style.margin = 0; const i = document.querySelector('img'); i.style.width = '720px'; i.style.height = 'auto'; });
    await p.locator('img').screenshot({ path: f.replace(/\.png$/, '.jpg'), type: 'jpeg', quality: 62 }); }
  await b.close(); })();
"""
pngs = sorted(glob.glob(os.path.join(tmp, '**', '*.png'), recursive=True))
js = os.path.join(tmp, 'r.js'); open(js, 'w').write(JS)
subprocess.run(['node', js, *pngs], check=True, env={**os.environ, 'NODE_PATH': subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip()})
NOMS = ['1 · début', '2 · fenêtre ouverte', '3 · examens (point 9)', '4 · prise en charge (point 11)', '5 · fin']
blocs = []
for f in fichiers:
    base = os.path.basename(f)[:-5]
    titre = re.search(r'<title>([^<]*)', open(f, encoding='utf-8').read())
    vues = []
    for i in range(1, 6):
        j = glob.glob(os.path.join(tmp, '**', f'{base}_{i}.jpg'), recursive=True)
        vues.append(f'<figure><img alt="{html.escape(base)} vue {i}" src="data:image/jpeg;base64,{base64.b64encode(open(j[0], "rb").read()).decode()}">'
                    f'<figcaption>{NOMS[i - 1]}</figcaption></figure>' if j else f'<figure class="m"><figcaption>{NOMS[i - 1]} : capture absente</figcaption></figure>')
    blocs.append(f'<section><h2>{html.escape(titre.group(1) if titre else base)}</h2><div class="g">{"".join(vues)}</div></section>')
sortie = a.sortie or os.path.join(tmp, f'Planche_{lot}.html')
open(sortie, 'w', encoding='utf-8').write(
    f'<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{lot} — 5 captures par cours</title>'
    '<style>body{margin:0;padding:16px;background:#faf7f2;color:#0b0b0b;font:15px/1.4 system-ui,sans-serif}h1{font-size:1.3rem}h2{font-size:1rem;margin:1.4rem 0 .5rem}'
    '.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:10px}figure{margin:0;background:#fff;border:1px solid #e4dccf;border-radius:8px;overflow:hidden}'
    'img{width:100%;display:block}figcaption{padding:.3rem .5rem;font-size:.8rem}.m{padding:1rem;color:#7f3a20}</style>'
    f'<h1>{lot} — 5 captures par cours ({len(fichiers)} cours)</h1>{"".join(blocs)}</html>')
print(sortie, os.path.getsize(sortie), 'octets')
