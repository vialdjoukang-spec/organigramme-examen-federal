"""Liste des clichés à réunir (normal + pathologique) par diagnostic ; régénérable : python3 liste_images.py."""
import json, glob, os, html
d = json.load(open('recensement.json', encoding='utf-8'))
R = {r['code']: r['nom'] for r in d['regions']}
enr = {}
for f in glob.glob('enrichi/[!_]*.json'):
    try: enr.update(json.load(open(f, encoding='utf-8')))
    except Exception: pass
E = html.escape
lignes, n_ok = [], 0
for x in d['imagerie']:
    t = x['techniques'][0]
    g = enr.get(x['id'], {}).get('gold', {}).get('examen')
    im = enr.get(x['id'], {}).get('images', {})
    ac = im.get('a_chercher') or {}
    cl = (f"<b>Normal :</b> {E(ac.get('normal','(normal trouvé)'))}<br><b>Pathologique :</b> {E(ac['patho'])}" if ac.get('patho')
          else E(g or f"{t['tech']} — {t['detail'].split(',')[0].strip()}"))
    st = 'trouvé' if im.get('patho') else ('manque' if im.get('manque') else 'à chercher')
    n_ok += st == 'trouvé'
    lignes.append(f"<tr class='{st.replace(' ','_').replace('é','e')}'><td>{x['id']}</td><td>{E(R[x['region']])}</td><td>{E(x['systeme'])}</td><td>{E(x['diagnostic'])}</td><td>{'MIN' if x['niveau']=='M' else 'CIBLE'}</td><td>{cl}</td><td><code>{x['id']}_normal.jpg</code><br><code>{x['id']}_patho.jpg</code></td><td>{st}</td></tr>")
n = len(d['imagerie'])
page = f"""<!doctype html><html lang=fr><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>Clichés à réunir</title>
<style>body{{background:#fff;color:#000;font:15px/1.4 system-ui;margin:16px}}h1{{background:#bcd0f7;padding:6px 10px;border-radius:6px}}
.w{{overflow-x:auto}}table{{border-collapse:collapse;min-width:900px}}th,td{{border-bottom:1px solid #ddd;padding:5px 8px;text-align:left;vertical-align:top}}
th{{border-bottom:2px solid #000;position:sticky;top:0;background:#fff}}tr.trouve td:last-child{{font-weight:800}}tr.manque td:last-child{{text-decoration:underline}}</style>
<h1>Clichés à réunir : {n} diagnostics × 2 images</h1>
<p>Pour chaque diagnostic, il faut un cliché <b>normal</b> et un cliché <b>pathologique</b> de même technique et même plan, où la lésion se voit. Nomme le fichier comme indiqué, puis dépose-le ; je pose les flèches numérotées. Déjà trouvés : <b>{n_ok}</b> / {n}.</p>
<div class=w><table><tr><th>Id</th><th>Région</th><th>Système</th><th>Diagnostic</th><th>Niveau</th><th>Cliché demandé</th><th>Noms de fichiers</th><th>Statut</th></tr>{''.join(lignes)}</table></div>"""
open('LISTE_IMAGES.html', 'w', encoding='utf-8').write(page)
print(n, n_ok)
