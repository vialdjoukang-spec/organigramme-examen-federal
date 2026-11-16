import re,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
f=sys.argv[1]
h=open(f,encoding='utf-8').read()
paras=re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I)
for p in paras:
    t=c.texte(p)
    if len(t.split())>40 and not c.CONNECT.search(t): print(len(t.split()),t[:260].replace('\n',' '));print()
