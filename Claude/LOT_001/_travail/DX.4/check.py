import sys,json,types,glob
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
P=C.charger_paquet('paquet.json')
files=sys.argv[1:] or sorted(glob.glob('fragments/p*.html'))
for f in files:
    h='<section class="ilot" id="dx4-p1">'+open(f).read()+'</section>'
    open('/tmp/claude-0/chk.html','w').write(h+'\n<!-- FIN_FICHIER -->')
    a=types.SimpleNamespace(points=0,min=0,max=10**9,script_ok=False,ex=8)
    r=C.controler('/tmp/claude-0/chk.html',P,a,{})
    print(f,r['octets'],r['verdict'],r['connecteur%'],'sansconn',r['paragraphes_sans_connecteur'])
    for k,v in r['defauts'].items(): print('  ',k,v['n'],' || '.join(v['ex']))

    import re
    for p in re.findall(r'<div class="p">(.*?)</div>',h,re.S):
        t=C.texte(p)
        if len(t.split())>40 and not C.CONNECT.search(t): print('   SANSCONN:',t[:100])
