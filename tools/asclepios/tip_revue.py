"""Asclépios · applique au champ 5 de TIP (data/TIP.json) : 15 champs écrits (tip_nouveaux.py, sources tip_sources.py)
et la revue des blocs « Autres éléments ciblés » (tip_autres_a/b/c.py). Rejouable : part de data/TIP.json extrait de main.
Usage : python3 tools/json_inject.py extract TIP && python3 tools/asclepios/tip_revue.py && python3 tools/json_inject.py inject TIP"""
import json,sys,os
sys.path.insert(0,os.path.dirname(__file__))
from tip_nouveaux import NEW
from tip_sources import SRC
from tip_autres_a import AUT as A
from tip_autres_b import AUT as B
from tip_autres_c import AUT as C
AUT={**A,**B,**C}
ORDER=['constantes','peau','tete-cou','ganglions','thorax','coeur-vaisseaux','vasc','seins','abdomen','tr-genital','rachis','membres','epaule','coude-main','hanche','genou','cheville-pied','neuro','neuro-nc','neuro-moteur','meninge-gcs','psychiatrie','pediatrie','geriatrie','autres']
DEF='0M123456N';SEQ={'abdomen':'0M1432 56N'.replace(' ','')}
def parse(s):
  B=[];cur=None;ph='0'
  for l in s.split('\n'):
    if not l.strip():continue
    c=l[0]
    if c=='§':cur={'r':l[1:].strip(),'it':[],'ch':[]};B.append(cur);ph='0'
    elif c=='¶':ph=l[1:].strip()
    elif c=='@':cur['ch']+=[x for x in l[1:].split() if x not in cur['ch']]
    elif l.startswith('• '):cur['it'].append((ph,l[2:]))
    else:raise ValueError('ligne inattendue : '+l[:60])
  return B
def build(B):
  key=lambda b:(ORDER.index(b['r']) if b['r'] in ORDER else len(ORDER))
  out=[]
  for b in sorted(B,key=key):
    seq=SEQ.get(b['r'],DEF);L=sorted(b['it'],key=lambda e:seq.index(e[0]));cur=None
    out.append('§'+b['r'])
    for ph,t in L:
      if ph!=cur:out.append('¶'+ph);cur=ph
      out.append('• '+t)
    if b['ch']:out.append('@'+' '.join(b['ch']))
  return '\n'.join(out)
def merge(B,new):
  for nb in new:
    old=next((b for b in B if b['r']==nb['r']),None)
    if old:
      seen=set();it=[]
      for e in old['it']+nb['it']:
        k=e[1].strip().rstrip('.').lower()
        if k not in seen:seen.add(k);it.append(e)
      st['doublons']+=len(old['it'])+len(nb['it'])-len(it);old['it']=it;old['ch']+=[x for x in nb['ch'] if x not in old['ch']]
    else:B.append(nb)
  return B
T=json.load(open('data/TIP.json'))
st=dict(ecrits=0,blocs=0,elements_avant=0,elements_apres=0,sources=0,doublons=0)
for sid,txt in NEW.items():
  c=T[sid]['c'];assert c[5].startswith('À compléter'),sid
  c[5]=build(parse(txt));st['ecrits']+=1
  v=T[sid].setdefault('v',{'S':[],'c':[None]*len(c),'d':[None]*len(T[sid].get('d',[]))})
  ids=[]
  for s in SRC[sid]:
    if isinstance(s,int):ids.append(s);continue
    i=max([x['id'] for x in v['S']]+[0])+1;v['S'].append({'id':i,**s});ids.append(i);st['sources']+=1
  v['c'][5]=['complété',ids]
miss=[]
for sid,x in T.items():
  c=x['c']
  if len(c)<6 or '§autres' not in c[5] or sid in NEW:continue
  if sid not in AUT:miss.append(sid);continue
  B=parse(c[5]);old=[b for b in B if b['r']=='autres'];st['elements_avant']+=sum(len(b['it']) for b in old)
  B=[b for b in B if b['r']!='autres'];nw=parse(AUT[sid]);st['elements_apres']+=sum(len(b['it']) for b in nw)
  c[5]=build(merge(B,nw));st['blocs']+=1
if miss:sys.exit('blocs non revus : '+' '.join(miss))
extra=set(AUT)-{k for k in T if k in AUT}
json.dump(T,open('data/TIP.json','w'),ensure_ascii=False,separators=(',',':'))
print(st,'inconnus:',extra or 0)
