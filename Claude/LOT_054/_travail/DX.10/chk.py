import sys,json,glob,argparse
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
h='<html><body>'+''.join(open(f,encoding='utf8').read() for f in sorted(glob.glob('fragments/p*.html')))+'<!-- FIN_FICHIER --></body></html>'
open('tmp_all.html','w',encoding='utf8').write(h)
a=argparse.Namespace(points=0,min=0,max=10**9,ex=400,script_ok=False)
P=c.charger_paquet('paquet.json')
j=c.controler('tmp_all.html',P,a,{})
print(j['verdict'],j['octets'],'conn',j['connecteur%'],'sansconn',j['paragraphes_sans_connecteur'],'ph',j['phrases'])
want=sys.argv[1:]
for k,v in j['defauts'].items():
    print('##',k,v['n'])
    for e in v['ex']: print('  -',e)
