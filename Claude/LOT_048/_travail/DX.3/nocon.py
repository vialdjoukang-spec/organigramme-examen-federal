import sys,re
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
h=open('/home/user/wt/lot-048/Claude/LOT_048/LOT_048_Phase_B_V0_DX.3.html',encoding='utf-8').read()
h=c.SOURCES.sub(' ',h)
for p in re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S):
    t=c.texte(p)
    if len(t.split())>40 and not c.CONNECT.search(t): print(len(t.split()),t[:100])
