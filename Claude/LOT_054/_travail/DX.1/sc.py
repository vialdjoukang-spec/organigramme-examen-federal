import re,sys,glob
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
h=open('../../LOT_054_Phase_B_V0_DX.1.html',encoding='utf-8').read()
h=C.SOURCES.sub(' ',h)
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
n=0
for p in paras:
    t=C.texte(p)
    if len(t.split())>40 and not C.CONNECT.search(t):
        n+=1; print('--',len(t.split()),t[:200])
print(n)
