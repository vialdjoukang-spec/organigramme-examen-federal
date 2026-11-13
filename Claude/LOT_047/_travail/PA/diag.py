import re,sys,html
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
h=open('../../LOT_047_Phase_A_V0.html',encoding='utf-8').read()
body=C.SOURCES.sub(' ',h)
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',body,re.S|re.I)
print('paragraphes sans connecteur:')
for p in paras:
    t=C.texte(p)
    if len(t.split())>40 and not C.CONNECT.search(t): print('  -',t[:90])
ph=C.phrases_html(body)
tot=0;con=0;long_=[]
for tag,b,t in ph:
    if tag.lower()=='td': continue
    tot+=1
    if C.CONNECT.search(t): con+=1
    n=len(t.split())
    if n>28: long_.append((n,t[:70]))
print('connecteur',con,tot,round(100*con/tot))
print('phrases >28 mots:',len(long_))
for n,t in long_[:int(sys.argv[1]) if len(sys.argv)>1 else 10]: print('  ',n,t)
