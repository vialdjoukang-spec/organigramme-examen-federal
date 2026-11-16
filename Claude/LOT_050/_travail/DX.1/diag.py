import sys,re
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
h=open('/home/user/wt/lot-050/Claude/LOT_050/LOT_050_Phase_B_V0_DX.1.html',encoding='utf-8').read()
h2=c.SOURCES.sub(' ',h)
ph=c.phrases_html(h2)
mode=sys.argv[1]
if mode=='long':
    for tag,b,t in ph:
        if tag!='td' and len(t.split())>28: print(len(t.split()),'|',t,'\n')
elif mode=='nom':
    for tag,b,t in ph:
        if tag!='td' and not c.est_verbale(t): print(t,'\n')
elif mode=='para':
    paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h2,re.S|re.I)
    for p in paras:
        t=c.texte(re.sub(r'<sup class="r">.*?</sup>','',p,flags=re.S))
        if len(t.split())>40 and not c.CONNECT.search(t): print(len(t.split()),'|',t,'\n')
elif mode=='noconn':
    for tag,b,t in ph:
        if tag!='td' and not c.CONNECT.search(t): print(t[:150])
