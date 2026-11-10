import sys,json,re,hashlib
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as c
P={x['id']:x['texte'] for x in json.load(open('paquet.json'))['passages']}
SEEN={}
for f in sys.argv[1:]:
    h=open(f'fragments/p{int(f):02d}.html').read()
    ph=c.phrases_html(h); tot=0;conn=0
    for tag,b,t in ph:
        cites=c.CIT.findall(b); nums=c.nombres(c.STRUCT.sub(' ',t))
        for ci in cites:
            if ci not in P: print('INCONNU',ci)
        if nums and not cites and tag!='td': print('SANS CIT',t[:100])
        if cites and nums:
            src=' '.join(P.get(ci,'') for ci in cites)
            m={x for x in nums if x not in c.nombres(src)}
            if m: print('NOMBRE',sorted(m),'::',t[:110])
        if c.DOSE.search(t) and not any(ci.startswith('aips') for ci in cites): print('DOSE',t[:100])
        k=hashlib.sha1(re.sub(r'\W+','',t.lower()).encode()).hexdigest()
        if len(t)>60 and k in SEEN and SEEN[k]!=f: print('DUP',t[:80],SEEN[k])
        SEEN.setdefault(k,f)
        if tag!='td':
            tot+=1; conn+= bool(c.CONNECT.search(t))
            w=len(t.split())
            if w>30: print('LONG',w,t[:80])
            if not c.est_verbale(t): print('NOMIN',t[:80])
    for p in re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S):
        tt=c.texte(p)
        if len(tt.split())>40 and not c.CONNECT.search(tt): print('SANSCONN',len(tt.split()),tt[:90])
    print(f'p{f}: {len(h.encode())} o, phrases {tot}, connecteur {round(100*conn/max(tot,1))}%')
