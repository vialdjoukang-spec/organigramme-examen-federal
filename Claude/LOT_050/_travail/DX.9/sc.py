import re,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
h=open('/home/user/wt/lot-050/Claude/LOT_050/LOT_050_Phase_B_V0_DX.9.html').read()
for p in re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S):
    t=c.texte(p)
    if len(t.split())>40 and not c.CONNECT.search(t): print('SANSCONN:',t[:110])
