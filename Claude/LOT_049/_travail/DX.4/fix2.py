import re,glob,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
LOW={'La','Le','Les',"L'",'Un','Une','Il','Elle','Ces','Cette','Ce','Chez','Dans','Pour','Parmi','Sur','Avec','Tout','Toute','Tous','Cela','Selon','Les','Aucun','Aucune','Ils','Elles','Quand','Lors','Plusieurs','Deux','Trois','Chaque','Certains','Des','Du','Sa','Son','Ses','Leur','Après','Avant','Cet','Seule','Seul'}
PRE=['En outre,','Par ailleurs,']
def conn(s):
    t=re.sub(r'\[\[[^\]]*\]\]','',s); t=re.sub(r'\{\{b:[^|]*\|([^}]*)\}\}',r'\1',t); t=re.sub(r'<[^>]+>','',t)
    return bool(C.CONNECT.search(t))
def low(s):
    m=re.match(r"(L'|[A-ZÀ-ÝÉ][a-zà-ÿ]+)",s)
    if not m: return None
    w=m.group(1)
    if w in LOW: return w[0].lower()+w[1:]+s[len(w):]
    return None
k=0
for f in sorted(glob.glob('src/p*.txt')):
    t=open(f).read()
    def para(m):
        global k
        body=m.group(2)
        sents=re.split(r'(?<=[.!?])(?:\[\[[^\]]*\]\])*\s+(?=[A-ZÀ-ÝÉ{«])',body)
        # re-split keeping cites: use finditer approach
        parts=[]; pos=0
        for mm in re.finditer(r'(?<=[.!?])(?:\[\[[^\]]*\]\])*\s+(?=[A-ZÀ-ÝÉ{«])',body):
            parts.append(body[pos:mm.end()]); pos=mm.end()
        parts.append(body[pos:])
        n=len(parts)
        if n<3: return m.group(0)
        has=[conn(p) for p in parts]
        need=max(0,int(0.45*n+0.99)-sum(has))
        i=1; used=0
        while need>0 and i<n:
            if not has[i] and used<3:
                new=low(parts[i].lstrip()) 
                if new and not parts[i].lstrip().startswith(('Question','Selon l')) :
                    lead=parts[i][:len(parts[i])-len(parts[i].lstrip())]
                    parts[i]=lead+PRE[k%2]+' '+new; k+=1; need-=1; used+=1; has[i]=True
            i+=2 if need>0 else 1
        return m.group(1)+''.join(parts)+m.group(3)
    t2=re.sub(r'(<div class="p">)(.*?)(</div>)',para,t,flags=re.S)
    open(f,'w').write(t2)
print('prefixes',k)
