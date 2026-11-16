import re,sys,glob,os
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as c
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mode=sys.argv[1]
for f in sorted(glob.glob(D+'/fragments/p*.html')):
    h=open(f).read()
    name=os.path.basename(f)
    if mode=='long':
        for tag,b,t in c.phrases_html(h):
            if tag=='td': continue
            n=len(t.split())
            if n>28: print(name,n,'|',t[:400]); 
    elif mode=='conn':
        for p in re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I):
            t=c.texte(p)
            if len(t.split())>40 and not c.CONNECT.search(t): print(name,len(t.split()),'|',t[:160])
    elif mode=='nom':
        for tag,b,t in c.phrases_html(h):
            if tag=='td': continue
            if not c.est_verbale(t): print(name,'NOM |',t[:200])
