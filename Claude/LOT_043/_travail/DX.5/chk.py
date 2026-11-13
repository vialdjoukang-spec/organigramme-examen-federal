import sys,re,glob
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as c
for f in sorted(glob.glob('fragments/p*.html')):
    h=open(f).read()
    for p in re.findall(r'<div class="p">(.*?)</div>',h,re.S):
        t=c.texte(p)
        if len(t.split())>40 and not c.CONNECT.search(t): print(f,'SANS_CONN:',t[:100])
    for tag,b,t in c.phrases_html(h):
        if tag=='td': continue
        n=len(t.split())
        if n>32: print(f,'LONG',n,t[:80])
        elif not c.est_verbale(t): print(f,'NOMINAL',t[:80])
