"""Checkpoint partiel : ne transforme pas un lot incomplet en succès."""
from pathlib import Path
import subprocess,sys,json,hashlib
D=Path(__file__).resolve().parents[1];R=D.parents[1];A=D/'audits'
for f in sorted(D.glob('*.html')):
 subprocess.run([sys.executable,str(R/'harnais/taille_xy.py'),str(f),'--inscrire'],check=True,cwd=R)
 p=subprocess.run([sys.executable,str(R/'harnais/audit_langue.py'),str(f),'--json'],text=True,capture_output=True,cwd=R)
 (A/('langue_'+f.stem+'_checkpoint.json')).write_text(p.stdout)
for args,name in [(['codex-LOTS-html/outils/verifier_lot_generique_v8.py',str(D)],'validation_v8_partielle.json'),(['harnais/controle_lot.py','verifier',str(D),'--sans-nom','--json'],'harnais_historique_partiel.json')]:
 p=subprocess.run([sys.executable,*args],cwd=R,text=True,capture_output=True);(A/name).write_text(p.stdout)
 if p.stderr:(A/(name+'.stderr')).write_text(p.stderr)
 print(name,'code',p.returncode)
subprocess.run([sys.executable,str(R/'harnais/controle_lot.py'),'manifeste',str(D)],cwd=R,check=True)
check=[]
for f,expected in json.loads((R/'harnais/HARNAIS_MANIFESTE.json').read_text())['fichiers'].items():
 actual=hashlib.sha256((R/f).read_bytes()).hexdigest();check.append(dict(fichier=f,attendu=expected,observe=actual,identique=actual==expected))
(A/'harnais_integrite.json').write_text(json.dumps(check,ensure_ascii=False,indent=2)+'\n');assert all(x['identique'] for x in check)
v=json.loads((A/'validation_v8_partielle.json').read_text());checks=[c for f in v['fichiers'] for c in f['controles']]
print(json.dumps(dict(fichiers=len(v['fichiers']),controles=len(checks),positifs=sum(x['ok'] for x in checks),echecs=[x for x in checks if not x['ok']],lot_complet=v['onze_fichiers_et_dix_diagnostics']),ensure_ascii=False))
