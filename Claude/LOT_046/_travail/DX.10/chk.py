import sys,re
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as C
h=open('../../LOT_046_Phase_B_V0_DX.10.html').read()
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
for p in paras:
    t=C.texte(p)
    if len(t.split())>40 and not C.CONNECT.search(t): print('SANS CONN:',t[:110])
tot=0;ok=0
for tag,b,t in C.phrases_html(C.SOURCES.sub(' ',h)):
    if tag=='td':continue
    tot+=1; ok+= bool(C.CONNECT.search(t))
    if len(t.split())>28: print('LONG',len(t.split()),t[:80])
print(ok,tot,round(100*ok/max(tot,1)))
