import pathlib,subprocess,json,hashlib
R=pathlib.Path('/workspace/organigramme-examen-federal/work/p1/s4.4-s4.5');T=pathlib.Path('/tmp/p1-179-projection-gardes');O=R/'audit/p1-s4.4-s4.5-reprise-20261020/correctif-acanthosis179';O.mkdir(exist_ok=True)
B='88bcc38ae202af4aef06940fb6f00bbac6517afc';I='2a3d2dc22e6a35b5f633bf9cbadc676947419af0';F='tools/cours/lots/S4.4-S4.5-glo-delta.json'
sha=lambda x:hashlib.sha256(x).hexdigest()
before=json.loads(subprocess.check_output(['git','show',B+':'+F],cwd=R));after=json.load(open(R/F));i=next(i for i,e in enumerate(before['glo_ajouts_proposes']) if e['id']=='acanthosis');a=after['glo_ajouts_proposes'][i];b=before['glo_ajouts_proposes'][i]
expected=json.loads(json.dumps(before));expected['glo_ajouts_proposes'][i]['def']=a['def'];checks={'seule_definition_acanthosis_modifiee':expected==after,'aucun_alias_ajoute':'alias' not in a,'contexte_nigricans_explicite':'nigricans' in a['def'],'projection_definition_identique':next(e for e in json.load(open(T/'data/ck/glo.json')) if e['id']=='acanthosis')==a};hashes={}
files=['data/tip/S4.4.json','data/tip/S4.5.json','tools/cours/lots/S4.4.json','tools/cours/lots/S4.5.json','assets/config/tip.js','tools/cours/lots/S4.4-S4.5-src-delta.json','tools/cours/lots/S4.4-S4.5-domaines-delta.json','data/ck/glo.json','data/ck/src.json','qa/termes-baseline.json','qa/termes_exclus.txt','qa/doses-baseline.json','qa/domaines.yml','tools/lyncee.py','tools/audit/niveau1.py']
for f in files:
 old=subprocess.check_output(['git','show',B+':'+f],cwd=R);new=(R/f).read_bytes();checks[f+'_inchange']=old==new;hashes[f]={'avant':sha(old),'apres':sha(new)}
for f in ['qa/termes-baseline.json','qa/termes_exclus.txt','qa/doses-baseline.json']:
 expected=subprocess.check_output(['git','show',I+':'+f],cwd=R);checks[f+'_projection_inchange']=(T/f).read_bytes()==expected
records=[]
for g in ['G4','G6']:
 cmd=['python3','tools/audit/niveau1.py','--only',g,'--racine',str(T)];p=subprocess.run(cmd,cwd=R,capture_output=True,text=True);records.append({'commande':cmd,'code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
out={'date':'2026-10-20','base_auteur':B,'base_projection':I,'portee':'Vérifications techniques de l’auteur, pas contre-audit indépendant','definition_avant':b,'definition_apres':a,'sha_delta_avant':sha(subprocess.check_output(['git','show',B+':'+F],cwd=R)),'sha_delta_apres':sha((R/F).read_bytes()),'source_relue':{'url':'https://www.nhs.uk/conditions/acanthosis-nigricans/','editeur':'NHS','pays':'GB','date_relecture':'2026-10-20','portee':'Titre ; Symptoms et Causes of acanthosis nigricans ; page revue le 04.07.2024. Description et associations, sans définition générique de toute acanthose.'},'checks':checks,'empreintes':hashes,'commandes':records,'reussi':all(checks.values()) and all(r['code']==0 for r in records)}
(O/'verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'reussi':out['reussi'],'gardes':[{k:r[k] for k in ['commande','code','stdout']} for r in records]},ensure_ascii=False,indent=2));assert out['reussi']
