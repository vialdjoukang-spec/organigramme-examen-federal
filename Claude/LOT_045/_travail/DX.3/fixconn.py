import re,glob,sys
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as c
COMMON={'Le','La','Les','Un','Une','Il','Elle','Ils','On','Ces','Cette','Ce','Dans','Chez','Pour','En','Des','Du','Sur','Au','Aux','Leur','Son','Sa','Ses','Cela','Ceci','Lorsque','Quand','Selon','Avant','Après','Si','Cet','Tous','Toute','Chaque','Certains','Les','Aucune','Aucun'}
CONN=['Par ailleurs, ','En outre, ','Par ailleurs, ']
k=0
def lower_first(sen):
    m=re.match(r"(L')(\w)",sen)
    if m: return "l'"+sen[2:]
    w=re.match(r"([A-ZÀ-Ý][\wéèêàùûôîç'-]*)",sen)
    if w and w.group(1) in COMMON:
        return sen[0].lower()+sen[1:]
    return sen
def fix_block(m):
    global k
    inner=m.group(2)
    t=c.texte(re.sub(r'\[\[[^\]]*\]\]','',inner))
    if len(t.split())<=40 or c.CONNECT.search(t): return m.group(0)
    if '<button' in inner or '<strong>' in inner: return m.group(0)
    parts=re.split(r'((?:\.|\]\]\.?)\s+)(?=[A-ZÀ-Ý«])',inner)
    # parts: s0,sep,s1,sep,s2...
    if len(parts)<3: return m.group(0)
    idx=2  # second sentence
    s=parts[idx]
    if s.startswith('<'): return m.group(0)
    conn=CONN[k%len(CONN)]; k+=1
    parts[idx]=conn+lower_first(s)
    print('+',conn,s[:60])
    return m.group(1)+''.join(parts)+m.group(3)
for f in sorted(glob.glob('src/p*.src.html')):
    s=open(f).read()
    s2=re.sub(r'(<div class="p">)(.*?)(</div>)',fix_block,s,flags=re.S)
    open(f,'w').write(s2)
