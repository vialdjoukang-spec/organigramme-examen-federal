import sys,re,json
sys.path.insert(0,'/home/user/wt/lot-001/Claude/_outils')
import controle3 as c
f='/home/user/wt/lot-001/Claude/LOT_001/LOT_001_Phase_B_V0_DX.5.html'
h=open(f,encoding='utf-8').read()
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',c.SOURCES.sub(' ',h),re.S|re.I)
for p in paras:
    t=c.texte(p)
    if len(t.split())>40 and not c.CONNECT.search(t): print('SANS_CONN:',t[:150])
