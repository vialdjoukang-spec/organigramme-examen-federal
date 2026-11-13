import sys,re,os,json
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as C
D=os.path.dirname(os.path.abspath(__file__))
for n in range(1,15):
    h=open(f'{D}/fragments/p{n:02d}.html').read()
    e=C.equilibre(h)
    if e: print('BALISES',n,e)
    for tag,b,t in C.phrases_html(h):
        if tag=='td': continue
        w=len(t.split())
        if w>28: print(f'LONG p{n} {w}: {t[:150]}')
        if not C.est_verbale(t): print(f'NOM p{n}: {t}')
    for p in re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S):
        t=C.texte(p)
        if len(t.split())>40 and not C.CONNECT.search(t): print(f'NOCONN p{n}: {t[:110]}')
