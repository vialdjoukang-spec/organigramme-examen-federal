"""Contrôles réels, rapports bruts conservés ; aucune validation clinique."""
from pathlib import Path
import json,subprocess,hashlib,sys
D=Path(__file__).resolve().parents[1];R=D.parents[1]
A=D/'audits'
def run(args,dest):
 p=subprocess.run([sys.executable,*args],cwd=R,text=True,capture_output=True)
 (A/dest).write_text(p.stdout)
 if p.stderr:(A/(dest+'.stderr')).write_text(p.stderr)
 return p.returncode
for f in sorted(D.glob('*.html')):
 subprocess.run([sys.executable,str(R/'harnais/taille_xy.py'),str(f),'--inscrire'],check=True,cwd=R)
 run(['harnais/audit_langue.py',str(f),'--json'],'langue_'+f.stem+'_final.json')
v=run(['codex-LOTS-html/outils/verifier_lot_generique_v8.py',str(D)],'validation_v8.json')
h=run(['harnais/controle_lot.py','verifier',str(D),'--sans-nom','--json'],'harnais_historique.json')
subprocess.run([sys.executable,str(R/'harnais/controle_lot.py'),'manifeste',str(D)],check=True,cwd=R)
checks=[]
for name,sha in json.loads((R/'harnais/HARNAIS_MANIFESTE.json').read_text())['fichiers'].items():
 actual=hashlib.sha256((R/name).read_bytes()).hexdigest();checks.append(dict(fichier=name,attendu=sha,observe=actual,identique=sha==actual))
(A/'harnais_integrite.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
aips=[]
for p in (D/'evidence').glob('AIPS_*.json'):
 m=json.loads(p.read_text());actual=hashlib.sha256((R/m['source']).read_bytes()).hexdigest();aips.append(dict(source=m['source'],attendu=m['sha256'],observe=actual,identique=m['sha256']==actual))
(A/'empreintes_aips.json').write_text(json.dumps(aips,ensure_ascii=False,indent=2)+'\n')
r=json.loads((A/'validation_v8.json').read_text());flat=[c for f in r['fichiers'] for c in f['controles']]
print(json.dumps(dict(v8_code=v,harnais_historique_code=h,controles=len(flat),positifs=sum(c['ok'] for c in flat),citations=sum(c['detail']['citations'] for c in flat if c['controle']=='citations_aips_presentes_dans_fichiers_originaux'),harnais_intact=all(c['identique'] for c in checks),aips_intact=all(c['identique'] for c in aips)),ensure_ascii=False))
assert v==0 and all(c['identique'] for c in checks+aips)
