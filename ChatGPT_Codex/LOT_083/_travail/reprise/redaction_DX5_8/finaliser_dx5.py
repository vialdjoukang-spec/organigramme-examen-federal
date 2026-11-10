from pathlib import Path
import json,re,hashlib
B=Path(__file__).parent;D=B/'DX.5';P=D/'paquet.json';d=json.loads(P.read_text())
for x in d['passages']:
 if x['id']=='flu-date-2026':
  x['texte_original']=x['texte'];x['texte']=x['texte'].replace('09.2026','09.\n2026');x['normalisation']='Retour de ligne séparant année et jour/mois ; original et empreinte source conservés.'
ids={x['id']:('aips-f5-' if x['id'].startswith('aips') else 'f5-')+str(n+1) for n,x in enumerate(d['passages']) if x['id'] not in ['flu-ssi-alarmes','flu-ssi-tests']}
(D/'paquet_ids_longs.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
for x in d['passages']:
 x['id_original']=x['id'];x['id']=ids.get(x['id'],x['id'])
P.write_text(json.dumps(d,ensure_ascii=False,indent=2))
for f in (D/'fragments').glob('*.html'):
 t=f.read_text()
 for a,b in ids.items():t=t.replace('sb-'+a+'"','sb-'+b+'"')
 f.write_text(t)
