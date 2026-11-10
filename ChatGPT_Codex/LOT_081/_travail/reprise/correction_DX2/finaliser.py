from pathlib import Path
import subprocess,sys,hashlib,json,re,os
D=Path(__file__).resolve().parent
O=D.parents[3]/'_outils'
f=D/'LOT_081_Phase_B_V0_DX.2.html'
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
subprocess.run([sys.executable,str(O/'assembler.py'),'--fragments',str(D/'fragments'),'--paquet',str(D/'paquet.json'),'--contrat',str(D/'contrat.json'),'--titre','DX.2 — Hernie discale lombaire avec radiculopathie','--sortie',str(f)],check=True,env=env)
h=f.read_text();h=re.sub(r'>(?=<)', '>\n',h);h=re.sub(r'(<sup class="r">)\s+(<a)',r'\1\2',h);f.write_text(h);b=f.read_bytes()
(D/'MANIFESTE.json').write_text(json.dumps({f.name:{'octets':len(b),'sha256':hashlib.sha256(b).hexdigest()}},ensure_ascii=False,indent=2)+'\n')
r=subprocess.run([sys.executable,str(O/'controle3.py'),str(f),'--paquet',str(D/'paquet.json'),'--ex','100'],capture_output=True,text=True,env=env)
(D/'CONTROLE3.json').write_text(r.stdout);print(r.stdout)
q='Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ?'
ids=re.findall(r'\bid="([^"]+)"',h);targets=re.findall(r'popovertarget="([^"]+)"',h)
print('SHA',hashlib.sha256(b).hexdigest(),'OCTETS',len(b),'MAX_LIGNE',max(map(len,h.splitlines())),'QUESTION',h.count(q),'DOUBLONS_IDS',[x for x in set(ids)if ids.count(x)>1],'CIBLES_MANQUANTES',sorted(set(targets)-set(ids)))
