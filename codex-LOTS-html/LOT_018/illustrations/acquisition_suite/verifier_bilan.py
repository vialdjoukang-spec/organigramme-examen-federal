#!/usr/bin/env python3
"""Compare les cellules publiées aux mesures fraîches, sans réécrire de leçon."""
import hashlib
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path
from lxml import html

D = Path(__file__).resolve().parent
B = D.parents[2]
R = B.parent
spec = importlib.util.spec_from_file_location('taille', R / 'harnais/taille_xy.py')
taille = importlib.util.module_from_spec(spec)
spec.loader.exec_module(taille)
data = json.loads((D / 'BILAN_DONNEES.json').read_text())
report = B / 'BILAN_CLICHES_LOT_018.html'
doc = html.document_fromstring(report.read_text())
checks = []


def check(nom, ok):
    checks.append({'controle':nom,'conforme':bool(ok)})


for row in data['lecons']:
    p = B / row['fichier']
    raw = p.read_bytes()
    m = taille.mesurer(raw.decode())
    expected = {'x':m.x[1],'y':m.y[1],'xy':m.x[1]+m.y[1],'html':len(raw)}
    check(row['id']+' empreinte',hashlib.sha256(raw).hexdigest()==row['sha256'])
    tr = doc.xpath('//tr[@data-lecon="'+row['id']+'"]')
    check(row['id']+' ligne unique',len(tr)==1)
    for key, val in expected.items():
        cells = tr[0].xpath('./td[@data-mesure="'+key+'"]') if tr else []
        check(row['id']+' '+key,len(cells)==1 and cells[0].text==f'{val/1000:.3f}' and row[key]==val)
    check(row['id']+' plafond',row['conforme_x'] and expected['x']<=row['plafond_x'])
for a in doc.xpath('//a[@href]'):
    href = a.get('href')
    if href.startswith('#'):
        check('ancre '+href,len(doc.xpath('//*[@id="'+href[1:]+'"]'))==1)
    elif not href.startswith('https://'):
        check('lien local '+href,(B/href).is_file())
before = json.loads((D.parent/'acquisition/LECONS_AVANT.json').read_text())
current = {str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in B.glob('LOT_*/*.html')}
check('244 leçons inchangées',len(current)==244 and current==before)
for p, sha in json.loads((R/'harnais/HARNAIS_MANIFESTE.json').read_text())['fichiers'].items():
    check('harnais '+p,hashlib.sha256((R/p).read_bytes()).hexdigest()==sha)
for s in data['candidats']:
    check('candidat non intégré '+s['id'],not s['inspection_visuelle'] and not s['integre'] and not (B/s['destination']).exists())
    details = doc.xpath('//details[@id="'+s['id']+'"]')
    check('décision visible '+s['id'],len(details)==1 and details[0].get('data-decision')==s['decision'])
sources = []
for parent in [D.parent/'acquisition', D]:
    sources.extend(s for s in json.loads((parent/'CANDIDATS.json').read_text())['candidats'] if s['decision'] in ('retenu_sous_reserve_visuelle','suspendu_provenance'))
check('notices actuelles reproduites exactement',data['candidats']==sources)
for key, decision in [('retenus','retenu_sous_reserve_visuelle'),('suspendus','suspendu_provenance')]:
    expected = sum(s['decision']==decision for s in sources)
    cells = doc.xpath('//*[@data-compte="'+key+'"]')
    check('compte '+key,len(cells)==1 and cells[0].text==str(expected) and data['candidats_'+key]==expected)
rd = doc.xpath('//details[@id="rd-fond-oeil"]')
check('discordance de provenance explicitée',len(rd)==1 and rd[0].get('data-decision')=='suspendu_provenance' and 'organigramme' in rd[0].text_content() and 'Import suspendu' in rd[0].text_content())
result={'date':datetime.now(timezone.utc).isoformat(timespec='seconds'),'reussis':sum(c['conforme'] for c in checks),'total':len(checks),'controles':checks,'portee':'Contrôle du rapport et de l’intégrité, pas validation clinique ni nouvel audit V8 des leçons.'}
(D/'CONTROLE_BILAN.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['reussis','total']}))
raise SystemExit(int(result['reussis']!=result['total']))
