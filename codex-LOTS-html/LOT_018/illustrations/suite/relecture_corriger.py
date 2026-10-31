"""Corrections de lisibilité avant rendu : ne pas masquer un signe par son numéro."""
import json,importlib.util
from pathlib import Path
D=Path(__file__).resolve().parent;B=D.parents[2]
spec=importlib.util.spec_from_file_location('dessinateur',B/'outils/dessinateur/dessinateur.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
fix={1:[(i,2,[x,40],[x,60,x,142]) for i,x in enumerate([510,425,610])],3:[(0,0,[540,100],[520,110,454,182])],5:[(0,0,[350,40],[350,60,350,75]),(1,0,[165,55],[185,70,211,89])],9:[(0,1,[530,90],[510,105,474,141])]}
for n,changes in fix.items():
 p=D/f'dx{n}.json';s=json.loads(p.read_text())
 for vi,ri,xy,line in changes:
  v=s['vues'][vi];v['reperes'][ri]['xy']=xy;x1,y1,x2,y2=line;v['formes'].append({'tag':'line','attrs':{'x1':x1,'y1':y1,'x2':x2,'y2':y2,'stroke':'#162c48','stroke-width':2}})
 p.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n');(D/f'dx{n}.html').write_text(m.render(s))
p=D/'dx3.json';s=json.loads(p.read_text());s['vues'][0]['formes'].insert(1,{'tag':'path','attrs':{'d':'M260 210 Q310 155 360 210 Q410 168 455 210 Z','fill':'#e7be45','stroke':'none'}})
for shape in s['vues'][1]['formes']:
 if shape['attrs'].get('fill')=='#b5dff6':shape['attrs']['d']='M250 184 Q355 99 465 184 L465 207 L250 207 Z'
s['vues'][0]['reperes'][0]['definition']='Dépôts jaunes sous la ligne brune de l’épithélium pigmentaire, qu’ils soulèvent. Ils ne suffisent pas à prouver une activité néovasculaire.'
p.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n');(D/'dx3.html').write_text(m.render(s))
p=D/'dx9.json';s=json.loads(p.read_text());s['vues'][0]['reperes'][0]['xy']=[360,210];p.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n');(D/'dx9.html').write_text(m.render(s))
