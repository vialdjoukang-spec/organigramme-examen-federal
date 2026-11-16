import re,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
h=open('/home/user/wt/lot-049/Claude/LOT_049/LOT_049_Phase_B_V0_DX.7.html').read()

paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
n=0
for p in paras:
    t=C.texte(p)
    if len(t.split())>40 and not C.CONNECT.search(t):
        n+=1; print(n,len(t.split()),t[:110])
