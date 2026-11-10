"""Copie une remise relue, actualise les empreintes ; Git reste une action séparée."""
from pathlib import Path
import argparse, hashlib, json
a=argparse.ArgumentParser()
a.add_argument('source');a.add_argument('sha');a.add_argument('total',type=int);a.add_argument('note')
v=a.parse_args();root=Path(__file__).resolve().parents[2]
source=Path(v.source).resolve();assert root in source.parents
data=source.read_bytes();assert hashlib.sha256(data).hexdigest()==v.sha
assert 100000<=len(data)<=200000
(root/source.name).write_bytes(data)
m=json.loads((root/'MANIFESTE.json').read_text());m[source.name]={'octets':len(data),'sha256':v.sha}
(root/'MANIFESTE.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
e=json.loads((root/'ETAT_FILE.json').read_text())
if source.name not in e['html_produits']:e['html_produits'].append(source.name)
(root/'ETAT_FILE.json').write_text(json.dumps(e,ensure_ascii=False,indent=2)+'\n')
j=root.parent/'JOURNAL_NUIT.md';s=j.read_text();s=s[:s.rfind('LOTs livrés :')]
s+=v.note+'\n\n'+f'LOTs livrés : 0/23 ; leçons poussées : {v.total}/253 après poussée de ce commit, 858 existantes consolidées ; blocages : LOT080 DX5 et DX6 REFUSE P3 ; LOT081 PR567 CI/fusion en cours ; LOT082 production/audits en cours ; LOT083–102 à produire.\n'
j.write_text(s)
print(source.name,len(data),v.sha)
