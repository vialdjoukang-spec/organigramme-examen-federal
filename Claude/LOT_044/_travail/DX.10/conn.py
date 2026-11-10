import re,glob,sys
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as C
def plain(s): return re.sub(r'\{\{f\d+\|([^}]+)\}\}',r'\1',re.sub(r'\[\[.+?\]\]','',s))
KEEP=re.compile(r"^(ESC|IRM|ECG|ADD-RS|ADD|IRAD|Trandate|Esmolol|Urapidil|L'Urapidil|Kapanol|Le Trandate|Swiss|Marfan|TEM|ADvISED|DISSECT|GERAADA|FAST|HUG|TEVAR|AIPS|MMP)")
n=0
for f in sorted(glob.glob('src/p*.txt')):
    lines=open(f,encoding='utf-8').read().split('\n'); out=[]
    for ln in lines:
        if ln.startswith('P '):
            rest=ln[2:]; t=plain(rest)
            if len(t.split())>40 and not C.CONNECT.search(t):
                parts=[m.group(0) for m in re.finditer(r'.*?(?:[.!?](?:\[\[.+?\]\])?(?:\s+(?=[A-ZÀ-Ý«])|$))',rest,re.S)]
                if len(parts)>=2:
                    conn=['En effet, ','Ainsi, '][n%2]; n+=1
                    p2=parts[1]
                    w=p2.split(' ')[0]
                    if not KEEP.match(p2) and not re.search(r'\d',w) and w[0].isupper() and not w.isupper():
                        p2=p2[0].lower()+p2[1:]
                    parts[1]=conn+p2
                    ln='P '+''.join(parts)+rest[len(''.join(parts)):]
        out.append(ln)
    open(f,'w',encoding='utf-8').write('\n'.join(out))
print(n)
