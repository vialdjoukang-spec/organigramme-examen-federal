"""Copie une remise relue, actualise les empreintes ; Git reste une action séparée."""
from pathlib import Path
import argparse, hashlib, json, re
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
j=root.parent/'JOURNAL_NUIT.md';s=j.read_text();last=s[s.rfind('LOTs livrés :'):]
delivered=re.search(r'LOTs livrés : (\d+)/23',last)
assert delivered, 'Dernière ligne de bilan absente'
blocks=last.split('blocages : ',1)[1].strip()
s=s[:s.rfind('LOTs livrés :')]
s+=v.note+'\n\n'+f'LOTs livrés : {delivered.group(1)}/23 ; leçons poussées : {v.total}/253 après poussée de ce commit, 858 existantes consolidées ; blocages : {blocks}\n'
j.write_text(s)
print(source.name,len(data),v.sha)
