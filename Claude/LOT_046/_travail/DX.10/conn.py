import sys,re,glob
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as C
OK={'Le','La','Les','Il','Elle','Ce','Cette','Ces','Un','Une','Dans','Chez','Selon','Sa','Son','Ses','Cet','Pour','Après'}
conn=['Par ailleurs, ','En outre, ']
n=0
for f in sorted(glob.glob('src/p*.src.html')):
    s=open(f).read()
    def fix(m):
        global n
        b=m.group(1)
        t=C.texte(re.sub(r'⟦.*?⟧','',re.sub(r'<button[^>]*>|</button>','',b)))
        if len(t.split())<=40 or C.CONNECT.search(t): return m.group(0)
        pos=0
        for mm in re.finditer(r'([.!?](?:⟦[^⟧]*⟧)*)\s+([A-ZÀ-Ý][\wéèêàç\']*)',b):
            if mm.group(2) in OK and mm.start()>20:
                c=conn[n%2]; n+=1
                w=mm.group(2)
                b=b[:mm.start()]+mm.group(1)+' '+c+w[0].lower()+w[1:]+b[mm.end():]
                return '<div class="p">'+b+'</div>'
        return m.group(0)
    s2=re.sub(r'<div class="p">(.*?)</div>',fix,s,flags=re.S)
    open(f,'w').write(s2)
print(n)
