"""BESOINS_IMAGES.html : tout ce qu'il faut en images (imagerie + explorations fonctionnelles). Régénérable : python3 besoins_images.py"""
import json, glob, html
E = html.escape
d = json.load(open('recensement.json', encoding='utf-8'))
R = {r['code']: r['nom'] for r in d['regions']}
TI = {t['code']: t['nom'] for t in d['technologies_imagerie']}
TE = {t['code']: t['nom'] for t in d['technologies_explorations']}
enr = {}
for f in glob.glob('enrichi/[!_]*.json'):
    try: enr.update(json.load(open(f, encoding='utf-8')))
    except Exception: pass
# Explorations : qui fournit ? Tracé réel souhaité, ou schéma que je dessine moi-même (courbes théoriques, sans droits).
SCHEMA = {'VENT', 'DYN'}
def niv(x): return 'MIN' if x.get('niveau') == 'M' else 'CIBLE'
def table(entetes, lignes):
    return ('<div class=w><table><tr>' + ''.join(f'<th>{h}</th>' for h in entetes) + '</tr>' + ''.join(lignes) + '</table></div>')
# A. Diagnostics d'imagerie
la, a_ok = [], 0
for x in d['imagerie']:
    e = enr.get(x['id'], {}); im = e.get('images', {}); ac = im.get('a_chercher') or {}
    if im.get('patho'): st = 'TROUVÉ'; a_ok += 1
    elif im.get('manque'): st = 'introuvable en libre'
    else: st = 'à fournir'
    t = x['techniques'][0]
    norm = ac.get('normal') or f"{TI.get(t['tech'], t['tech'])} normal, même plan ({t['detail']})"
    pat = ac.get('patho') or f"{TI.get(t['tech'], t['tech'])} ({t['detail']}) montrant : {x['diagnostic']}"
    la.append(f"<tr class='{'ok' if st=='TROUVÉ' else ''}'><td>{x['id']}</td><td>{niv(x)}</td><td>{E(R[x['region']])} · {E(x['systeme'])}</td><td><b>{E(x['diagnostic'])}</b></td>"
              f"<td><b>Normal :</b> {E(norm)}<br><b>Pathologique :</b> {E(pat)}</td><td><code>{x['id']}_normal.jpg</code><br><code>{x['id']}_patho.jpg</code></td><td>{st}</td></tr>")
# B. Fiches de technique d'imagerie : une illustration normale de référence
lb = [f"<tr><td>{x['id']}</td><td>{niv(x)}</td><td>{E(TI.get(x['tech'], x['tech']))}</td><td><b>{E(x['titre'])}</b></td><td>Un cliché normal de référence qui illustre la notion (ex. : les cinq densités sur une radiographie du thorax).</td><td><code>{x['id']}.jpg</code></td><td>à fournir</td></tr>" for x in d['fiches_technique_imagerie']]
# C. Explorations : tracé normal + tracé pathologique
lc, c_reel = [], 0
for x in d['explorations']:
    t = x['explorations'][0]; sch = t['tech'] in SCHEMA
    c_reel += not sch
    qui = 'je le dessine (schéma)' if sch else 'tracé réel à fournir'
    lc.append(f"<tr><td>{x['id']}</td><td>{niv(x)}</td><td>{E(R[x['region']])} · {E(x['systeme'])}</td><td><b>{E(x['diagnostic'])}</b></td>"
              f"<td>{E(TE.get(t['tech'], t['tech']))} — {E(t['detail'])}<br><b>Normal :</b> tracé normal de cet examen<br><b>Pathologique :</b> {E(x['anomalie'])}</td>"
              f"<td><code>{x['id']}_normal.jpg</code><br><code>{x['id']}_patho.jpg</code></td><td>{qui}</td></tr>")
# D. Fiches de technique des explorations : un tracé normal annoté
ld = [f"<tr><td>{x['id']}</td><td>{niv(x)}</td><td>{E(TE.get(x['tech'], x['tech']))}</td><td><b>{E(x['titre'])}</b></td><td>Un tracé normal complet, lisible, qui sert de référence de lecture.</td><td><code>{x['id']}.jpg</code></td><td>{'je le dessine (schéma)' if x['tech'] in SCHEMA else 'tracé réel à fournir'}</td></tr>" for x in d['fiches_technique_explorations']]
nI, nE = len(d['imagerie']), len(d['explorations'])
nB, nD = len(lb), len(ld)
dD = sum(x['tech'] not in SCHEMA for x in d['fiches_technique_explorations'])
total_vial = 2 * (nI - a_ok) + nB + 2 * c_reel + dD
page = f"""<!doctype html><html lang=fr><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>Besoins en images</title>
<style>:root{{--n1:#bcd0f7;--n2:#f9dcae;--n3:#cfeedd}}body{{background:#fff;color:#000;font:15px/1.45 system-ui,sans-serif;margin:16px;max-width:1500px}}
h1{{background:var(--n1);padding:8px 12px;border-radius:6px;margin:0 0 12px}}h2{{background:var(--n2);padding:6px 12px;border-radius:6px;margin:28px 0 8px}}
nav a{{display:inline-block;border:2px solid #000;border-radius:999px;padding:4px 12px;margin:0 6px 6px 0;color:#000;text-decoration:none;font-weight:700}}
.w{{overflow-x:auto}}table{{border-collapse:collapse;min-width:1000px}}th,td{{border-bottom:1px solid #ddd;padding:6px 8px;text-align:left;vertical-align:top}}
th{{border-bottom:2px solid #000;position:sticky;top:0;background:#fff}}tr.ok td{{background:var(--n3)}}code{{font-size:.85em}}
.reg{{border:1px solid #999;border-radius:8px;padding:10px 14px}}.reg li{{margin:3px 0}}table.s{{min-width:0}}</style>
<h1>Besoins en images : imagerie et explorations fonctionnelles</h1>
<div class=reg><b>Règles pour chaque image fournie</b><ul>
<li>Envoie une paire : un cliché <b>normal</b> et un cliché <b>pathologique</b>, de même technique, même plan et même séquence ; la lésion doit se voir.</li>
<li>Anonymise totalement : aucun nom, date de naissance, numéro ni hôpital ne doit rester sur l'image.</li>
<li>Nomme le fichier comme dans la colonne « Fichiers » ; je pose ensuite les flèches numérotées, je vérifie leur position et je rédige les légendes.</li>
<li>Dis-moi la source : image personnelle, ou image dont tu as les droits. Le dépôt et la page sont publics.</li>
<li>Commence par les lignes <b>MIN</b> : elles forment le minimum indispensable de l'examen fédéral.</li></ul></div>
<h2>Bilan</h2><div class=w><table class=s><tr><th>Bloc</th><th>Éléments</th><th>Images par élément</th><th>Déjà trouvées</th><th>À fournir par toi</th></tr>
<tr><td>A. Diagnostics d'imagerie</td><td>{nI}</td><td>2 (normal + patho)</td><td>{2*a_ok}</td><td>{2*(nI-a_ok)}</td></tr>
<tr><td>B. Fiches de technique d'imagerie</td><td>{nB}</td><td>1</td><td>0</td><td>{nB}</td></tr>
<tr><td>C. Explorations fonctionnelles</td><td>{nE}</td><td>2 (tracé normal + patho)</td><td>0</td><td>{2*c_reel} (les {2*(nE-c_reel)} autres : je les dessine)</td></tr>
<tr><td>D. Fiches de technique des explorations</td><td>{nD}</td><td>1</td><td>0</td><td>{dD} (les {nD-dD} autres : je les dessine)</td></tr>
<tr><td><b>Total</b></td><td></td><td></td><td>{2*a_ok}</td><td><b>{total_vial}</b></td></tr></table></div>
<p>Je dessine moi-même, sans droits à acquérir, les courbes des explorations ventilatoires (spirométrie, boucles débit-volume) et des tests dynamiques et métaboliques (cinétiques de glycémie, de cortisol…), car ce sont des schémas théoriques.</p>
<nav><a href="#A">A. Imagerie</a><a href="#B">B. Techniques d'imagerie</a><a href="#C">C. Explorations</a><a href="#D">D. Techniques des explorations</a></nav>
<h2 id=A>A. Diagnostics d'imagerie ({nI})</h2>{table(['Id','Niveau','Région · système','Diagnostic','Clichés attendus','Fichiers','Statut'], la)}
<h2 id=B>B. Fiches de technique d'imagerie ({nB})</h2>{table(['Id','Niveau','Technologie','Fiche','Image attendue','Fichier','Statut'], lb)}
<h2 id=C>C. Explorations fonctionnelles ({nE})</h2>{table(['Id','Niveau','Région · système','Diagnostic','Tracés attendus','Fichiers','Qui fournit'], lc)}
<h2 id=D>D. Fiches de technique des explorations ({nD})</h2>{table(['Id','Niveau','Technologie','Fiche','Tracé attendu','Fichier','Qui fournit'], ld)}
"""
open('BESOINS_IMAGES.html', 'w', encoding='utf-8').write(page)
print(nI, a_ok, nB, nE, c_reel, nD, dD, total_vial)
