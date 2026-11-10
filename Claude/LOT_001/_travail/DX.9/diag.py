import re,sys,json
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
h=open('/home/user/wt/lot-001/Claude/LOT_001/LOT_001_Phase_B_V0_DX.9.html',encoding='utf-8').read()
h=C.SOURCES.sub(' ',h)
ph=[x for x in C.phrases_html(h) if x[0].lower()!='td']
print('phrases',len(ph),'avec connecteur',sum(1 for x in ph if C.CONNECT.search(x[2])))
mode=sys.argv[1] if len(sys.argv)>1 else 'para'
if mode=='para':
    paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
    for p in paras:
        t=C.texte(p)
        if len(t.split())>40 and not C.CONNECT.search(t): print('-',t[:110].replace('\n',' '),'|',len(t.split()))
else:
    for tg,b,t in ph:
        if not C.CONNECT.search(t): print('*',t[:150])
