import re,sys,html
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as C
h=open('/home/user/wt/lot-044/Claude/LOT_044/LOT_044_Phase_B_V0_DX.7.html',encoding='utf-8').read()
h=C.SOURCES.sub(' ',h)
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
n=0
for p in paras:
    t=C.texte(re.sub(r'<sup class="r">.*?</sup>','',p,flags=re.S))
    if len(t.split())>40 and not C.CONNECT.search(C.texte(p)):
        n+=1; print(n,len(t.split()),t[:230])
