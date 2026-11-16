import re,sys,html
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
from controle3 import CONNECT, texte
SAFE=('Le','La','Les','Un','Une','Des','Dans','Pour','Chez','Il','Elle','Ils','On','Ce','Cette','Ces','Cela','Lors','Sous','Après','Avant','Selon')
CONS=['En outre,','Par ailleurs,']
def lower(s):
    m=re.match(r"(L'|[A-ZÀ-Ý][a-zà-ÿ]+)",s)
    if not m: return None
    w=m.group(1)
    base=w if w!="L'" else "L'"
    if w!="L'" and w not in SAFE: return None
    return s[0].lower()+s[1:]
def proc(t, target):
    k=[0]
    def blk(m):
        b=m.group(2)
        sents=re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])',b)
        has=[bool(CONNECT.search(texte(re.sub(r'<sup class="r">.*?</sup>','',s)))) for s in sents]
        n=len(sents); c=sum(has)
        need_para = (len(texte(b).split())>40 and c==0)
        for i in range(1,n):
            if has[i]: continue
            if i>0 and has[i-1]: continue
            if not (need_para or (c/n<target)): break
            if sents[i].startswith('<'): continue
            lw=lower(sents[i])
            if lw is None: continue
            sents[i]=CONS[k[0]%2]+' '+lw; k[0]+=1; has[i]=True; c+=1; need_para=False
        return m.group(1)+' '.join(sents)+m.group(3)
    return re.sub(r'(<div class="p">)(.*?)(</div>)',blk,t,flags=re.S)
for f in sys.argv[2:]:
    t=open(f).read(); t2=proc(t,float(sys.argv[1])); open(f,'w').write(t2)
