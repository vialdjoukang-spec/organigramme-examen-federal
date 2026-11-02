#!/usr/bin/env python3
"""Bilan de mesures réelles. Aucun verdict médical ni clôture automatique."""
import argparse,datetime,hashlib,html,json,re,sys
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE.parent/'harnais'))
import taille_xy
p=argparse.ArgumentParser();p.add_argument('lot',type=int);a=p.parse_args()
D=BASE/f'LOT_{a.lot:03}';manifest=json.loads((D/'MANIFESTE.json').read_text())
rows=[]
for r in sorted(manifest['fichiers'],key=lambda x:x.get('dx',0)):
 f=D/r['fichier']
 if f.parent!=D or not f.is_file():raise ValueError('Chemin de manifeste invalide')
 raw=f.read_bytes()
 if hashlib.sha256(raw).hexdigest()!=r['sha256']:raise ValueError('Manifeste périmé : '+f.name)
 m=taille_xy.mesurer(raw.decode());n=len(raw);label='Phase A' if '_Phase_A_' in f.name else 'DX'+str(r['dx'])
 titre=re.search(r'<main>\s*<h[12][^>]*>(.*?)</h[12]>',raw.decode(),re.S)
 if titre: label=html.unescape(re.sub(r'<[^>]+>','',titre.group(1)))
 limite=100000 if '_Phase_A_' in f.name else 9000
 rows.append(f'<tr><td><a href="{D.name}/{html.escape(f.name)}">{html.escape(label)}</a></td><td>{n/1000:.3f}</td><td>{m.x[1]/1000:.3f}</td><td>{m.y[1]/1000:.3f}</td><td>{"Oui" if m.x[1]<=limite else "Non"}</td><td>{"Oui" if 100000<=n<=200000 else "Non"}</td></tr>')
links=[]
for f in sorted((D/'audits').glob('SYNTHESE*.json')):links.append(f'<li><a href="{D.name}/audits/{f.name}">{f.name}</a></li>')
for pattern in ('COUVERTURE*.json', 'AUDIT_COUVERTURE*.md'):
 for f in sorted((D/'audits').glob(pattern)):links.append(f'<li><a href="{D.name}/audits/{f.name}">{f.name}</a></li>')
for pattern in ('PLAN_ICONOGRAPHIQUE*.json', 'IMAGES_*.json'):
 for f in sorted((D/'evidence').glob(pattern)):links.append(f'<li><a href="{D.name}/evidence/{f.name}">{f.name}</a></li>')
body='''<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Bilan LOT</title><style>body{font:16px system-ui;max-width:1100px;margin:2rem auto;padding:1rem;color:#172536}table{border-collapse:collapse;width:100%}td,th{border:1px solid #c8d0da;padding:.6rem;text-align:left}a{color:#1556a0}</style>'''
body+=f'<h1>LOT {a.lot} — mesures vérifiées</h1><p>{html.escape(manifest["statut"])}</p><p>Mesuré le {datetime.datetime.now(datetime.timezone.utc).isoformat()}. 1 Ko = 1 000 octets. HTML : fichier complet. Base et fenêtres : texte mesuré par taille_xy. Les fenêtres illustrées sont exemptées du plafond : le poids HTML et la bande historique sont informatifs. Ces mesures ne valent pas validation médicale.</p><table><tr><th>Leçon</th><th>HTML Ko</th><th>Texte base Ko</th><th>Texte fenêtres Ko</th><th>Base conforme (Phase A ≤100 Ko ; DD ≤9 Ko)</th><th>Bande historique100–200 Ko</th></tr>'+''.join(rows)+'</table>'
body+='<h2>Preuves et limites</h2><p>Les synthèses ci-dessous distinguent audits, tests, réserves et statut préparatoire. Une date de consultation ne garantit pas la dernière version du registre. Aucun cliché absent ne doit être réputé acquis. La veille locale contrôle le contrat ; elle ne rédige pas et ne garantit pas la persistance du runtime.</p><ul>'+''.join(links)+'</ul></html>'
(BASE/f'BILAN_LOT_{a.lot:03}.html').write_text(body)
print(json.dumps({'fichier':f'BILAN_LOT_{a.lot:03}.html','html_mesures':len(rows),'validation_clinique':False}))
