"""Insertion idempotente dans la fenêtre d'examen ; fiche de base intacte."""
import hashlib,json,re,gzip,subprocess
from pathlib import Path
BASE=Path(__file__).resolve().parents[2];D=Path(__file__).resolve().parent;LOT=D.parent
mapping={'LOT_018_Phase_A_V0.html':('a-explorations',['optique','retine']),'LOT_018_Phase_B_V0_DX.7.html':('dx7-detail9',['retine']),'LOT_018_Phase_B_V0_DX.8.html':('dx8-detail9',['optique'])}
for name,(target,items) in mapping.items():
 p=LOT/name; text=p.read_text()
 backup=D/(name+'.avant.gz')
 if not backup.exists():backup.write_bytes(gzip.compress(text.encode(),mtime=0))
 text=re.sub(r'<!-- ILLUSTRATIONS_018_DEBUT -->.*?<!-- ILLUSTRATIONS_018_FIN -->','',text,flags=re.S)
 pattern=r'(<div id="'+target+r'" popover class="fenetre">.*?<div class="corps">)'
 body='<!-- ILLUSTRATIONS_018_DEBUT -->'+''.join((D/(i+'.html')).read_text() for i in items)+'<!-- ILLUSTRATIONS_018_FIN -->'
 text,n=re.subn(pattern,lambda m:m[1]+body,text,count=1,flags=re.S)
 if n!=1:raise RuntimeError('Fenêtre introuvable : '+name)
 p.write_text(text)
 subprocess.run(['python3','-B','harnais/taille_xy.py',str(p),'--inscrire'],check=True)
manifest=json.loads((LOT/'MANIFESTE.json').read_text())
for row in manifest['fichiers']:
 p=LOT/row['fichier'];row['octets']=p.stat().st_size;row['sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
(LOT/'MANIFESTE.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=1)+'\n')
