"""Garde de production et veille locale : aucun appel modèle, aucun score médical."""
from pathlib import Path
import json,hashlib,subprocess,datetime,sys,time,os
from zoneinfo import ZoneInfo
D=Path(__file__).resolve().parent;B=D.parent;R=B.parent

def controle():
 errors=[];branch=subprocess.check_output(['git','branch','--show-current'],cwd=R,text=True).strip()
 res=json.loads((R/'IA_RESERVATIONS.json').read_text())['codex'];lo,hi=res['plage']
 if branch!=res['branche']:errors.append('branche')
 for p,h in json.loads((R/'harnais/HARNAIS_MANIFESTE.json').read_text())['fichiers'].items():
  if hashlib.sha256((R/p).read_bytes()).hexdigest()!=h:errors.append('commun:'+p)
 for row in subprocess.check_output(['git','status','--porcelain','--untracked-files=all'],cwd=R,text=True).splitlines():
  if not row[3:].startswith('codex-LOTS-html/'):errors.append('hors-perimetre:'+row[3:])
 for p in (R/'harnais/controle_lot.py',R/'harnais/scinder_1_10.py'):compile(p.read_text(),str(p),'exec')
 state=json.loads((B/'ETAT_CONTINUITE.json').read_text())
 if state['statut'] not in ('actif','termine'):errors.append('contrat-pause')
 if not lo<=state['prochain_lot']<=hi:errors.append('lot-actif-hors-borne')
 files=[]
 for p in sorted(B.glob('LOT_*/*.html')):
  n=int(p.parent.name[4:])
  if not lo<=n<=hi:errors.append('borne:'+str(n))
  files.append({'fichier':str(p.relative_to(B)),'octets':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
 out={'date':datetime.datetime.now(datetime.timezone.utc).isoformat(),'branche':branch,'borne':[lo,hi],'erreurs':errors,'pret_infrastructure':not errors,'verrou_present':(B/'_cache/production.lock').exists(),'date_zurich':datetime.datetime.now(ZoneInfo('Europe/Zurich')).isoformat(),'fichiers':files,'portee':'Contrôle infrastructure et empreintes ; aucune validation médicale ni complétude déduite.'}
 tmp=D/f'ACTIVITE.{os.getpid()}.tmp';tmp.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');tmp.replace(D/'ACTIVITE.json');return out

def bracelet(task):
 p=subprocess.run([sys.executable,'-B',str(D/'bracelet/bracelet_suggest.py'),task],capture_output=True,text=True)
 with (D/'PREUVE_EMBOITEMENT.jsonl').open('a') as f:f.write(json.dumps({'date':datetime.datetime.now(datetime.timezone.utc).isoformat(),'date_zurich':datetime.datetime.now(ZoneInfo('Europe/Zurich')).isoformat(),'tache':task,'sortie_exacte':p.stdout,'stderr':p.stderr,'code_sortie':p.returncode,'ARSENAL_lu':True,'HARNAIS_lu':True,'producteur':'codex'},ensure_ascii=False)+'\n')
 print(p.stdout);return p.returncode
if __name__=='__main__':
 if len(sys.argv)>1 and sys.argv[1] in ('--help','-h'):
  print('Usage: controler.py [controle | veille | bracelet TACHE]. Controle ne valide pas le contenu médical.');sys.exit(0)
 if len(sys.argv)>1 and sys.argv[1] not in ('controle','veille','bracelet'):sys.exit('Commande inconnue')
 if len(sys.argv)>1 and sys.argv[1]=='bracelet':sys.exit(bracelet(' '.join(sys.argv[2:])))
 if len(sys.argv)>1 and sys.argv[1]=='veille':
  lock=D/'veille.lock'
  try:
   fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY);os.write(fd,str(os.getpid()).encode());os.close(fd)
  except FileExistsError:sys.exit('Veille déjà enregistrée ; contrôler le PID avant reprise.')
  try:
   while True:controle();time.sleep(60)
  finally:lock.unlink(missing_ok=True)
 else:
  r=controle();print(json.dumps({k:v for k,v in r.items() if k!='fichiers'},ensure_ascii=False));sys.exit(bool(r['erreurs']))
