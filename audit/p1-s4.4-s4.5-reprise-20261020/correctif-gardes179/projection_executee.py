import pathlib,subprocess,tarfile,io,json,shutil,sys,hashlib
R=pathlib.Path('/workspace/organigramme-examen-federal/work/p1/s4.4-s4.5');B='2a3d2dc22e6a35b5f633bf9cbadc676947419af0';T=pathlib.Path('/tmp/p1-179-projection-gardes')
if not T.exists():
 T.mkdir();raw=subprocess.check_output(['git','archive',B],cwd=R);tarfile.open(fileobj=io.BytesIO(raw)).extractall(T,filter='data')
# Repartir des catalogues du commit d’intégration connu à chaque projection.
for name in ['glo','src']:
 (T/'data/ck'/f'{name}.json').write_bytes(subprocess.check_output(['git','show',B+':data/ck/'+name+'.json'],cwd=R))
gd=json.load(open(R/'tools/cours/lots/S4.4-S4.5-glo-delta.json'));gdold=json.loads(subprocess.check_output(['git','show','a19ade11:tools/cours/lots/S4.4-S4.5-glo-delta.json'],cwd=R))
g=json.load(open(T/'data/ck/glo.json'));own={e['id'] for e in gdold['glo_ajouts_proposes']};g=[e for e in g if e['id'] not in own];ids={e['id'] for e in g}
for e in gd['glo_ajouts_proposes']:
 assert e['id'] not in ids,('Collision projection',e['id']);g.append(e);ids.add(e['id'])
for u in gd['glo_mises_a_jour_proposees']:g=[u['apres'] if e['id']==u['id'] else e for e in g]
(T/'data/ck/glo.json').write_text(json.dumps(g,ensure_ascii=False,indent=1)+'\n')
sd=json.load(open(R/'tools/cours/lots/S4.4-S4.5-src-delta.json'));sdold=json.loads(subprocess.check_output(['git','show','a19ade11:tools/cours/lots/S4.4-S4.5-src-delta.json'],cwd=R));sources=json.load(open(T/'data/ck/src.json'));oldids={s['id'] for s in sdold};sources=[s for s in sources if s['id'] not in oldids]+sd
assert len({s['id'] for s in sources})==len(sources)
(T/'data/ck/src.json').write_text(json.dumps(sources,ensure_ascii=False,indent=1)+'\n')
for c in ['S4.4','S4.5']:shutil.copyfile(R/'data/tip'/f'{c}.json',T/'data/tip'/f'{c}.json')
sys.path.insert(0,str(T/'tools'));from tip_data import build;build(T)
# Règles nouvelles seulement si nécessaires ; aucune baseline/exclusion n’est éditée.
import yaml
D=yaml.safe_load((T/'qa/domaines.yml').read_text());dd=json.load(open(R/'tools/cours/lots/S4.4-S4.5-domaines-delta.json'))
for e in dd['ajouts_proposes']:
 if e['domaine'] not in D[e['liste']]:D[e['liste']].append(e['domaine'])
# Le coordinateur les a déjà intégrées dans2a3d ; écrire uniquement si un futur ajout ciblé apparaît.
if D!=yaml.safe_load((T/'qa/domaines.yml').read_text()):(T/'qa/domaines.yml').write_text(yaml.safe_dump(D,allow_unicode=True))
for name in ['termes-baseline.json','termes_exclus.txt']:
 expected=subprocess.check_output(['git','show',B+':qa/'+name],cwd=R);assert (T/'qa'/name).read_bytes()==expected
cmds=[['python3','tools/ck_build.py','--racine',str(T)],['python3','tools/lyncee.py','--racine',str(T)],['python3','tools/audit/niveau1.py','--only','G6','--racine',str(T)]]
# niveau1 utilise --root, son schéma exact est lu avant appel si nécessaire.
for cmd in cmds:
 p=subprocess.run(cmd,cwd=T,capture_output=True,text=True);print('CMD',' '.join(cmd),'EXIT',p.returncode);print((p.stdout+p.stderr)[-15000:])
