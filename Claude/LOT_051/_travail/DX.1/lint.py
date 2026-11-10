import sys,re
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
h=open('/home/user/wt/lot-051/Claude/LOT_051/LOT_051_Phase_B_V0_DX.1.html',encoding='utf-8').read()
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
for p in paras:
    t=c.texte(re.sub(r'<sup class="r">.*?</sup>','',p))
    if len(t.split())>40 and not c.CONNECT.search(t): print('SANS CONN >40 :',t[:90])
ph=c.phrases_html(c.SOURCES.sub(' ',h))
ns=[t for tg,_,t in ph if tg.lower()!='td']
nc=[t for t in ns if not c.CONNECT.search(t)]
print('phrases',len(ns),'sans connecteur',len(nc),'%',round(100*(len(ns)-len(nc))/len(ns)))
if len(sys.argv)>1:
    for t in nc[:int(sys.argv[1])]: print(' -',t[:110])
