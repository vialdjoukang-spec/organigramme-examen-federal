#!/usr/bin/env python3
"""Surveillance locale du contrat ; ne rédige pas et ne simule pas un agent."""
import datetime, hashlib, json, os, sys, time, subprocess
from pathlib import Path
D=Path(__file__).resolve().parents[1];R=D.parent
LOCK=D/'_cache'/'production.lock'; ETAT=D/'ETAT_CONTINUITE.json'
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
def lire(p):return json.loads(p.read_text())
def controler():
 e=lire(ETAT);res=lire(R/'IA_RESERVATIONS.json')['codex']; errors=[]
 branch=subprocess.check_output(['git','branch','--show-current'],cwd=R,text=True).strip()
 if branch!=res['branche']:errors.append('Branche non autorisée')
 n=e['prochain_lot']
 if not res['plage'][0]<=n<=res['plage'][1]:errors.append('Prochain lot hors plage')
 if e['statut'] not in ('actif','termine'):errors.append('Contrat en pause : aucune reprise autorisée')
 for f,h in lire(R/'harnais/HARNAIS_MANIFESTE.json')['fichiers'].items():
  if not (R/f).exists() or hashlib.sha256((R/f).read_bytes()).hexdigest()!=h:errors.append('Harnais altéré : '+f)
 for line in subprocess.check_output(['git','status','--porcelain','--untracked-files=all'],cwd=R,text=True).splitlines():
  if not line[3:].startswith('codex-LOTS-html/'):errors.append('Modification hors périmètre : '+line[3:])
 p=D/f'LOT_{n:03}'
 report={'controle_le':now(),'erreurs':errors,'prochain_lot':n,'html_presents':len(list(p.glob('*.html'))),'verrou_local':LOCK.exists(),'portee':'Contrôle de contrat, pas une preuve de rédaction ni une validation médicale.'}
 tmp=D/'CONTROLE_CONTINUITE.json.tmp';tmp.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');tmp.replace(D/'CONTROLE_CONTINUITE.json')
 return report
cmd=sys.argv[1] if len(sys.argv)>1 else 'controler'
if cmd=='prendre':
 LOCK.parent.mkdir(exist_ok=True)
 try:
  with LOCK.open('x') as f:f.write(json.dumps({'pris_le':now(),'hote':os.uname().nodename,'responsable':'session principale ; vérifier activité avant récupération'}))
 except FileExistsError:sys.exit('Production déjà verrouillée ; ne pas lancer de second producteur.')
 print('Verrou local acquis')
elif cmd=='liberer':
 LOCK.unlink(missing_ok=True);print('Verrou local libéré')
elif cmd=='controler':
 r=controler();print(json.dumps(r,ensure_ascii=False));sys.exit(bool(r['erreurs']))
elif cmd=='surveiller':
 while True:
  try:
   r=controler()
   with (D/'VEILLE_CONTRAT.jsonl').open('a') as f:f.write(json.dumps(r,ensure_ascii=False)+'\n')
  except Exception as e:
   with (D/'VEILLE_CONTRAT.jsonl').open('a') as f:f.write(json.dumps({'controle_le':now(),'erreur':str(e)})+'\n')
  time.sleep(60)
else:sys.exit('Commande inconnue')
