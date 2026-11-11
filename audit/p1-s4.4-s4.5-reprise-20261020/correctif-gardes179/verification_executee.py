import pathlib,subprocess,json,hashlib,sys,os,copy
R=pathlib.Path('.').resolve();T=pathlib.Path('/tmp/p1-179-projection-gardes');B='2a3d2dc22e6a35b5f633bf9cbadc676947419af0';H='9fc53c972ecd66a5ed2cf4ecb4a1167bcddcfe2a';O=R/'audit/p1-s4.4-s4.5-reprise-20261020/correctif-gardes179';O.mkdir(exist_ok=True)
sha=lambda b:hashlib.sha256(b).hexdigest();records=[]
# Reconstruire la projection définitive par le script local déjà utilisé ; consigner sa sortie exacte.
p=subprocess.run(['python3','/tmp/p1_179_projection.py'],cwd=R,capture_output=True,text=True);records.append({'commande':['python3','/tmp/p1_179_projection.py'],'code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
cmds=[(['python3','tools/audit/niveau1.py','--racine',str(T),'--sortie',str(O/'signalements-projection.json')],R),(['python3','tools/tip_data.py'],R),(['python3','tools/arsenal/lot.py','cours','S4.4','S4.5','-v'],R),(['python3','tools/cours/controler.py'],R),(['python3','-m','unittest','discover','-s','tests','-p','test_cours_ssp.py'],R),(['python3','-m','unittest','discover','-s','tests','-p','test_tip_asset.py'],R),(['python3','-m','unittest','discover','-s','tests','-p','test_arsenal.py'],R)]
for cmd,cwd in cmds:
 p=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,env={**os.environ,'PYTHONWARNINGS':'ignore::ResourceWarning'});records.append({'commande':cmd,'code':p.returncode,'stdout':p.stdout,'stderr':p.stderr});print(p.returncode,' '.join(cmd))
checks={};hashes={}
for f in ['qa/termes-baseline.json','qa/termes_exclus.txt','qa/doses-baseline.json']:
 actual=(T/f).read_bytes();expected=subprocess.check_output(['git','show',B+':'+f],cwd=R);own=(R/f).read_bytes();ownbefore=subprocess.check_output(['git','show',H+':'+f],cwd=R)
 checks[f+'_projection_inchange']=actual==expected;checks[f+'_branche_inchange']=own==ownbefore;hashes[f]={'integration':sha(expected),'projection':sha(actual),'branche_avant':sha(ownbefore),'branche_apres':sha(own)}
for c in ['S4.4','S4.5']:
 old=json.loads(subprocess.check_output(['git','show',H+':data/tip/'+c+'.json'],cwd=R));new=json.load(open(R/'data/tip'/f'{c}.json'));lot=json.load(open(R/'tools/cours/lots'/f'{c}.json'))
 checks[c+'_DD_f_s_fs_intacts']=all(old[k]==new[k] for k in ['d','f','s','fs'])
 checks[c+'_visa_DD_intact']=old.get('v',{}).get('d')==new.get('v',{}).get('d')
 checks[c+'_lots_14_et_empreintes']=len(new['c'])==14 and new['c']==lot['parties'] and lot['avant_gel_9fc53c9_sha256']==[sha(t.encode()) for t in old['c']] and lot['apres_sha256']==[sha(t.encode()) for t in new['c']]
 hashes[c]={'avant_9fc':lot['avant_gel_9fc53c9_sha256'],'apres':lot['apres_sha256']}
# Vérifier littéralement les quatre précisions médicales du correctif9fc.
a=json.load(open(R/'data/tip/S4.4.json'))['c'];b=json.load(open(R/'data/tip/S4.5.json'))['c']
checks['9fc_post_coital']=all('test post-coïtal' in a[i] for i in [8,13]);checks['9fc_CFTR_couple']='chez l’homme et sa partenaire' in a[8] and 'sans anomalie rénale' in a[8];checks['9fc_serologie_attribuee']='l’ESHRE permet conditionnellement' in a[8] and 'CNGOF 2024' in a[8];checks['9fc_iop_non_iatrogene']='IOP non iatrogène' in b[1];checks['9fc_coeliaque']='maladie cœliaque' in b[4]
for f in ['app_v2.html','tools/lyncee.py','tools/audit/niveau1.py']:
 checks[f+'_inchange']=sha((R/f).read_bytes())==sha(subprocess.check_output(['git','show',H+':'+f],cwd=R))
report=pathlib.Path('/workspace/organigramme-examen-federal/work/p1/integration-s4.4-s4.5/audit/P1-GARDES-INITIAL-S4.4-S4.5-20261020.json');checks['43_signalements_initiaux_conserves']=len(json.load(open(report)))==43
out={'date':'2026-10-20','base_projection':B,'base_auteur':H,'projection_locale':str(T),'scope':'Vérifications techniques de l’auteur ; aucune attestation indépendante','checks':checks,'empreintes':hashes,'rapport_initial_sha256':sha(report.read_bytes()),'commandes':records,'signalements_finaux':json.load(open(O/'signalements-projection.json')),'reussi':all(checks.values()) and all(r['code']==0 for r in records)}
(O/'verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('RESULTAT',out['reussi'],len(out['signalements_finaux']))
