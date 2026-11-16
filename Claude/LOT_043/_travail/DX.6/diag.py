import sys,json,re,collections
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as C
h=open('../../LOT_043_Phase_B_V0_DX.6.html',encoding='utf-8').read()
P={p['id']:p['texte'] for p in json.load(open('paquet.json'))['passages']}
ph=C.phrases_html(C.SOURCES.sub(' ',h))
mode=sys.argv[1] if len(sys.argv)>1 else 'all'
n=0
for tag,b,t in ph:
    cites=C.CIT.findall(b); nums=C.nombres(C.STRUCT.sub(' ',t))
    prob=[]
    if nums and not cites and tag!='td': prob.append('SANSCIT')
    if cites and nums:
        src=' '.join(P.get(c,'') for c in cites); m={x for x in nums if x not in C.nombres(src)}
        if m: prob.append('NUM'+str(sorted(m)))
    if C.DOSE.search(t) and not any(c.lower().startswith('aips') for c in cites): prob.append('DOSE')
    if tag!='td':
        w=len(t.split())
        if w>32: prob.append(f'LONG{w}')
        if not C.est_verbale(t): prob.append('NOMIN')
    if prob: print(prob,'::',t[:150]); n+=1
print(n)
