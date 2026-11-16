import re,sys,html
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as C
h=open('/home/user/wt/lot-043/Claude/LOT_043/LOT_043_Phase_B_V0_DX.2.html').read()
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
for p in paras:
    t=C.texte(p)
    if len(t.split())>40 and not C.CONNECT.search(t): print('SANS CONNECTEUR:',t[:100])
