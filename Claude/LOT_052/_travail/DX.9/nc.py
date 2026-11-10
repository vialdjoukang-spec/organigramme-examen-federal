import re,sys,html
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
for f in sys.argv[1:]:
    h=open(f).read()
    for p in re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S):
        t=C.texte(p)
        if len(t.split())>40 and not C.CONNECT.search(t): print(f[-8:],'PARA SANS CONN:',t[:90])
