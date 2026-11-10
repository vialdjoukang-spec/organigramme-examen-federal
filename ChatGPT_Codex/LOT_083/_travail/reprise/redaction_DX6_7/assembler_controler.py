from pathlib import Path
import sys, os, subprocess, json, re, hashlib
B=Path(__file__).resolve().parent;ROOT=B.parents[4];n=int(sys.argv[1]);D=B/f'DX.{n}';env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
subprocess.run([sys.executable,str(B/f'rediger_DX{n}.py')],check=True,env=env)
C=json.loads((D/'contrat.json').read_text());name=f'LOT_083_Phase_B_V0_DX.{n}';F=D/(name+'.html')
subprocess.run([sys.executable,str(ROOT/'outils/assembler.py'),'--fragments',str(D/'fragments'),'--paquet',str(D/'paquet.json'),'--contrat',str(D/'contrat.json'),'--titre',f'DX.{n} — '+C['ENTITE'],'--sortie',str(F)],check=True,env=env)
h=F.read_text();h=re.sub(r'</(section|div|table|thead|tbody|tr|td|th|h2|h3|h4|ol|li|blockquote)>',r'</\1>\n',h);F.write_text(h);raw=F.read_bytes();sha=hashlib.sha256(raw).hexdigest()
cmd=[sys.executable,str(ROOT/'outils/controle3.py'),str(F),'--paquet',str(D/'paquet.json'),'--points','14','--min','100000','--max','200000','--ex','100'];r=subprocess.run(cmd,capture_output=True,text=True,env=env);(D/'controle.json').write_text(r.stdout);ct=json.loads(r.stdout)[0]
q='Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ?';ids=re.findall(r'\bid="([^"]+)"',h);targets=re.findall(r'popovertarget="([^"]+)"',h)
v={'octets':len(raw),'sha256':sha,'points':len(re.findall(fr'id="dx{n}-p\d+"',h)),'question_exacte':h.count(q),'ligne_max':max(map(len,h.splitlines())),'ids_total':len(ids),'ids_uniques':len(set(ids)),'ids_dupliques':sorted({x for x in ids if ids.count(x)>1}),'cibles_absentes':sorted(set(targets)-set(ids)),'fin_exacte':h.rstrip().endswith(f'<!-- FIN_FICHIER {name} -->'),'controle_original':ct['verdict'],'images':'Différées selon Vial','autoaudit':False}
(D/'MANIFESTE.json').write_text(json.dumps({F.name:{'octets':len(raw),'sha256':sha}},ensure_ascii=False,indent=2)+'\n');(D/'VERIFICATIONS_TECHNIQUES.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n');print(json.dumps(v,ensure_ascii=False));print(json.dumps(ct['defauts'],ensure_ascii=False,indent=2))
assert v['points']==14 and v['question_exacte']==1 and v['ligne_max']<3000 and not v['ids_dupliques']and not v['cibles_absentes']and v['fin_exacte']
raise SystemExit(r.returncode)
