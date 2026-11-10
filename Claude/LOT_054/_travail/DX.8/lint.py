import re,sys,glob,html
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
h=open('tmp/t.html',encoding='utf-8').read()
body=C.SOURCES.sub(' ',h)
ph=C.phrases_html(body)
def where(t):
    k=t[:35]
    for f in sorted(glob.glob('src/p*.txt')):
        s=html.unescape(open(f).read())
        s=re.sub(r'\{\{[^}]*\}\}','',s)
        if k in s: return f[-6:-4]
    return '??'
mode=sys.argv[1]
for tag,b,t in ph:
    if tag=='td': continue
    n=len(t.split())
    if mode=='nom' and not C.est_verbale(t): print(where(t),'|',t)
    if mode=='long' and n>32: print(where(t),n,'|',t)
if mode=='conn':
    paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',body,re.S|re.I)
    for p in paras:
        tx=C.texte(re.sub(r'<sup class="r">.*?</sup>','',p))
        if len(tx.split())>40 and not C.CONNECT.search(tx): print(where(tx),'|',tx[:110])
if mode=='noconn':
    for tag,b,t in ph:
        if tag!='td' and not C.CONNECT.search(t): print(where(t),'|',t)
