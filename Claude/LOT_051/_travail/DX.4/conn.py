import re,glob,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
SAFE={'Le','La','Les','Un','Une','Il','Elle','Dans','Chez','Pour','Cette','Ces','Sa','Son','Ses','En','Au','Aux','Des','Du','On','Ce','Leur','Leurs','Cela'}
CN=["En outre, ","Ensuite, ","Ainsi, ","Par ailleurs, "]
k=0
for f in sorted(glob.glob('src/p*.txt')):
    blocks=open(f).read().split('\n\n'); out=[]
    for b in blocks:
        head=''
        while b.startswith('#'):
            hl,_,b=b.partition('\n'); head+=hl+'\n'
        if b.startswith(('|','-','@@','[[')) or '\n|' in b or '\n- ' in b or b.startswith('@') :
            out.append(head+b);continue
        t=re.sub(r'\{[^}]*\}','',b)
        t=re.sub(r'\[\[(.+?)\|f\d+\]\]',r'\1',t)
        if len(t.split())>40 and not C.CONNECT.search(t):
            parts=re.split(r'(?<=[.!?])(?:\{[^}]*\})?\s+(?=[A-ZÀ-Ý])',b)
            # re-split preserving: simple approach on first boundary
            m=re.search(r'(?<=[.!?])(\{[^}]*\})?\s+(?=[A-ZÀ-Ý])',b)
            if m:
                rest=b[m.end():]; w=re.match(r"[\wÀ-ÿ'’-]+",rest).group(0)
                w2=w.split("'")[0] if "'" in w else w
                if w2 in SAFE or w in SAFE:
                    rest=rest[0].lower()+rest[1:]
                b=b[:m.end()]+CN[k%len(CN)]+rest; k+=1
        out.append(head+b)
    open(f,'w').write('\n\n'.join(out))
print(k)
