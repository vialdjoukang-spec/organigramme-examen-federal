from pathlib import Path
import json,re,hashlib,os,subprocess
B=Path(__file__).parent;D=B/"DX.5"
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1');f=D/'LOT_083_Phase_B_V0_DX.5.html';subprocess.run(['python3','outils/assembler.py','--fragments',str(D/'fragments'),'--paquet',str(D/'paquet.json'),'--contrat',str(D/'contrat.json'),'--titre','LOT 083 — DX.5 — Grippe saisonnière','--sortie',str(f)],env=env,check=True)
t=f.read_text();m=re.search(r'<div class="p">Ce cours, lu seul.*?</div>',t);t=t[:m.start()]+t[m.end():];t=t.replace('</main>',m[0]+'\n</main>')
for tag in ['</li>','</tr>','</section>']:t=t.replace(tag,tag+'\n')
f.write_text(t);sha=hashlib.sha256(f.read_bytes()).hexdigest();(D/'MANIFESTE.json').write_text(json.dumps({f.name:dict(octets=f.stat().st_size,sha256=sha)},indent=2))
with (D/'CONTROLE3.json').open('w') as out:subprocess.run(['python3','outils/controle3.py',str(f),'--paquet',str(D/'paquet.json'),'--points','14','--min','100000','--max','200000'],stdout=out,env=env)
print(f.stat().st_size,sha)
