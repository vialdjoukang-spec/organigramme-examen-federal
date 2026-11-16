import sys,re,glob
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
tot=0;con=0
for f in sorted(glob.glob('fragments/p*.html')):
    h=open(f).read()
    for m in re.finditer(r'<div class="p">(.*?)</div>',h,re.S):
        b=m.group(1)
        phs=[c.texte(re.sub(r'<sup class="r">.*?</sup>','',p,flags=re.S)) for p in re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])',b)]
        phs=[p for p in phs if len(p.split())>=4]
        t=' '.join(phs); n=len(t.split())
        hc=[bool(c.CONNECT.search(p)) for p in phs]
        tot+=len(phs);con+=sum(hc)
        full=c.texte(b)
        if len(full.split())>40 and not c.CONNECT.search(full): print(f,'SANS CONNECTEUR:',t[:90])
        for p in phs:
            w=len(p.split())
            if w>28: print(f,'LONG',w,p[:80])
            if not c.est_verbale(p): print(f,'NOMINALE',p[:80])
print('connecteur %',round(100*con/max(tot,1)),tot)
