import sys,re,glob
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
h=C.SOURCES.sub('',open('/home/user/wt/lot-051/Claude/LOT_051/LOT_051_Phase_B_V0_DX.4.html').read())
for tag,b,t in C.phrases_html(h):
    if tag.lower()=='td': continue
    if not C.est_verbale(t): print('NOM |',t)
    elif len(t.split())>32: print('LONG',len(t.split()),'|',t)
print('--- paragraphes sans connecteur')
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
for p in paras:
    t=C.texte(p)
    if len(t.split())>40 and not C.CONNECT.search(t): print(len(t.split()),'|',t[:160])
