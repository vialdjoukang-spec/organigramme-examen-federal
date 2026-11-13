import sys,re
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as C
h=open('/home/user/wt/lot-045/Claude/LOT_045/LOT_045_Phase_B_V0_DX.5.html').read()
h2=C.SOURCES.sub(' ',h)
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
for p in paras:
    t=C.texte(p)
    if len(t.split())>40 and not C.CONNECT.search(t): print('PARA:',t[:200])
ph=[(tg,b,t) for tg,b,t in C.phrases_html(h2) if tg.lower()!='td']
n=len(ph);k=sum(1 for _,_,t in ph if C.CONNECT.search(t))
print(n,k,round(100*k/n))
