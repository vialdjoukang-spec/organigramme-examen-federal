import sys,re,json
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
h=open('/home/user/wt/lot-052/Claude/LOT_052/LOT_052_Phase_B_V0_DX.8.html').read()
ph=C.phrases_html(C.SOURCES.sub(' ',h))
mode=sys.argv[1]
if mode=='nom':
    for tag,b,t in ph:
        if tag.lower()!='td' and not C.est_verbale(t): print('NOM|',t)
elif mode=='long':
    for tag,b,t in ph:
        if tag.lower()!='td' and len(t.split())>32: print(len(t.split()),'|',t)
elif mode=='conn':
    paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
    for p in paras:
        t=C.texte(p)
        if len(t.split())>40 and not C.CONNECT.search(t): print(len(t.split()),'|',t)
