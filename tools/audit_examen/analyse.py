import json,re,collections,difflib,unicodedata,sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from _app import span
from tip_data import load
app = (ROOT / 'app_v2.html').read_text(encoding='utf-8')
a, b = span(app, 'GES'); g=json.loads(app[a:b]); t=load(ROOT, app)
def nz(s):return unicodedata.normalize('NFD',s.lower()).encode('ascii','ignore').decode()
ORD={'Inspection':1,'Palpation':2,'Percussion':3,'Auscultation':4,'Mobilisation':5,'Tests spéciaux':6}
ABD={'Inspection':1,'Auscultation':2,'Percussion':3,'Palpation':4,'Tests spéciaux':6}
SYS={'CV':'cardi|pouls|souffle|jugul|arter|veine|oedem|pression arter|tension|vascul|capillaire|doppler|ips|carotid|aort',
'RESP':'poumon|respir|pulmon|thorax|plevr|crepit|sibil|murmure|vibration|saturation|spo2|tirage|dyspn',
'DIG':'abdom|foie|hepat|rate|splen|intestin|anal|rect|digest|murphy|mcburney|blumberg|ascite|hernie',
'URO-GEN':'rein|lombaire|giordano|testic|scrot|penis|prostat|vagin|vulv|uter|gyneco|genit|vessie|urin',
'NEURO':'neuro|reflex|force|sensib|nerf|crani|pupill|coordin|marche|romberg|babinski|lasegue|glasgow|mening|conscien|tonus|dermatome',
'LOCO':'articul|muscul|tendon|ligament|mobilis|amplitude|rachis|epaule|genou|hanche|coude|poignet|cheville|menisq|tiroir|epineuse',
'PEAU':'peau|cutan|lesion|eruption|phaner|ongle|cheveu|muqueuse|purpura|ictere|cyanose|paleur|derm',
'LYMPH-ENDO':'ganglion|adenopath|lymph|thyro|goitre|sein',
'ORL-OPH':'oreille|otoscop|tympan|nez|gorge|pharyn|amygdal|oeil|yeux|fond d|acuite|visuel|conjonct|bouche|dent|langue|sinus',
'PSY':'humeur|psych|suicid|delire|halluc|cognit|orientation|mmse|moca|anxi|thymie'}
SYSre={k:re.compile(v) for k,v in SYS.items()}
rows=[];mat={};viol=[];allitems=[]
for r in g:
  cnt=collections.Counter()
  for i in r['items']:
    txt=nz(i['s']+' '+i['g'])
    ss=[k for k,v in SYSre.items() if v.search(txt)] or ['—']
    for s in ss:cnt[s]+=1
    allitems.append((r['id'],i['p'],i['s']))
  mat[r['id']]=cnt
  o=ABD if r['id']=='abdomen' else ORD
  seq=[(k,i['p'],i['s']) for k,i in enumerate(r['items']) if i['p'] in o]
  mx=0;prev=None
  for k,p,s in seq:
    if o[p]<mx: viol.append((r['id'],k+1,p,s,prev))
    if o[p]>=mx: mx=o[p];prev=p
  rows.append((r['id'],r['r'],len(r['items']),collections.Counter(i['p'] for i in r['items'])))
# redundancy: similar item titles across different regions
red=[]
for a in range(len(allitems)):
  for b in range(a+1,len(allitems)):
    A,B=allitems[a],allitems[b]
    if A[0]==B[0]:continue
    x,y=nz(A[2]),nz(B[2])
    if difflib.SequenceMatcher(None,x,y).ratio()>=0.8: red.append((A,B))
# TIP c[5]
empty=[k for k,v in t.items() if len(v['c'])<6 or not re.sub('<[^>]+>','',v['c'][5]).strip()]
tipviol=[];heads=collections.Counter();nohead=[]
for k,v in t.items():
  if k in empty:continue
  s=v['c'][5];hs=re.findall(r'^<b>([^<]{2,70})</b>\s*$',s,re.M)
  if not hs:nohead.append(k)
  for h in hs:heads[h]+=1
  for blk in re.split(r'^<b>[^<]{2,70}</b>\s*$',s,flags=re.M):
    b=nz(re.sub('<[^>]+>','',blk))
    pos=[(b.find(w),n) for w,n in [('inspect',1),('palp',2),('percu',3),('auscult',4)] if b.find(w)>=0]
    pos.sort();ns=[n for _,n in pos]
    if 'abdo' in b[:200] and ns[:2]==[1,4]:continue
    if ns!=sorted(ns):tipviol.append(k)
tipviol=sorted(set(tipviol))
output = ROOT / '.cache/audit_examen/stats.json'
output.parent.mkdir(parents=True, exist_ok=True)
json.dump(dict(rows=[(a,b,c,dict(d)) for a,b,c,d in rows],mat={k:dict(v) for k,v in mat.items()},viol=viol,red=red,empty=empty,nohead=nohead,tipviol=tipviol,nheads=len(heads),heads=heads.most_common(30)),output.open('w', encoding='utf-8'),ensure_ascii=False,indent=0)
print(len(viol),len(red),len(empty),len(nohead),len(tipviol),len(heads))
for v in viol:print(v)
for a,b in red:print(a,'<>',b)
