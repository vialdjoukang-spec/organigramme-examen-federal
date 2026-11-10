import sys,re
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
h=open('/tmp/w47x8/test.html',encoding='utf-8').read()
h=C.SOURCES.sub(' ',h)
for m in re.finditer(r'<div class="p">(.*?)</div>',h,re.S):
    t=C.texte(re.sub(r'<sup class="r">.*?</sup>','',m.group(1),flags=re.S))
    if len(t.split())>40 and not C.CONNECT.search(t): print('SANS CONN:',len(t.split()),t[:110])
