import re,glob,sys,itertools
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as C
CON=itertools.cycle(["Par ailleurs, ","En outre, ","Ensuite, "])
COMMON={'Le','La','Les','Un','Une','Il','Elle','Ils','Ces','Cette','Dans','Pour','Chez','Cela','Ce','Sa','Son','Leur','Leurs','Après','Selon','Sans','Quand','Lorsque','Devant','Plus','Une','Ses','Cependant','En','Au','Aux','Des','Du','Sur','Toute','Tout','Chaque'}
def txt(s): return C.texte(re.sub(r'\[\[[^\]]+\]\]','',s))
def fix(par):
    t=txt(par)
    extra=sum(len(m.split(',')) for m in re.findall(r'\[\[([^\]]+)\]\]',par))
    if len(t.split())+extra<=36 or C.CONNECT.search(t): return par
    parts=re.split(r'(?<=[.!?])((?:\[\[[^\]]+\]\])?)\s+(?=[A-ZÀ-Ý«])',par)
    # parts: [s1, cites1, s2, cites2, ...] -> rebuild
    if len(parts)<3: return par
    # insert at 2nd sentence
    s2=parts[2]
    w=s2.split(' ',1)[0]
    if w in COMMON: s2=s2[0].lower()+s2[1:]
    parts[2]=next(CON)+s2
    out=parts[0]
    for i in range(1,len(parts),2):
        out+=parts[i]+' '+parts[i+1] if i+1<len(parts) else parts[i]
    return out
for f in sorted(glob.glob('src/p*.txt')):
    L=open(f).read().split('\n'); new=[]
    for l in L:
        if l.startswith('P '):
            l='P '+fix(l[2:])
        elif l.startswith('WIN '):
            k,_,body=l[4:].partition(' ')
            body=' ¶ '.join(fix(x.strip()) for x in body.split('¶'))
            l=f'WIN {k} {body}'
        new.append(l)
    open(f,'w').write('\n'.join(new))
