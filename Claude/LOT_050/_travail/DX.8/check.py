import sys,re,importlib.util,json
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
h=open('/home/user/wt/lot-050/Claude/LOT_050/LOT_050_Phase_B_V0_DX.8.html',encoding='utf-8').read()
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
print('PARAS SANS CONNECTEUR:')
for p in paras:
    t=c.texte(p)
    if len(t.split())>40 and not c.CONNECT.search(t): print('  ',len(t.split()),t[:110])
ph=c.phrases_html(c.SOURCES.sub(' ',h))
print('SANS CONNECTEUR (phrases):',sum(1 for tg,_,t in ph if tg!='td' and not c.CONNECT.search(t)),'/',sum(1 for tg,_,t in ph if tg!='td'))
if len(sys.argv)>1:
    for tg,b,t in ph:
        if tg!='td' and not c.CONNECT.search(t): print('   -',t[:100])
