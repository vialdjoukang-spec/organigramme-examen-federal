import sys,json,glob,os,types
sys.path.insert(0,'/home/user/wt/lot-001/Claude/_outils')
import controle3 as C
D='/home/user/wt/lot-001/Claude/LOT_001/_travail/DX.10/'
P=C.charger_paquet(D+'paquet.json')
a=types.SimpleNamespace(points=0,min=0,max=10**9,ex=40,script_ok=False)
sel=sys.argv[1:] 
for f in sorted(glob.glob(D+'fragments/p*.html')):
    if sel and os.path.basename(f)[:3] not in sel: continue
    body=open(f).read()
    tmp='/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/_t.html'
    open(tmp,'w').write('<main>'+body+'</main>\nFIN_FICHIER')
    r=C.controler(tmp,P,a,{})
    print(os.path.basename(f),len(body),r['verdict'],'conn%',r['connecteur%'],'sansconn',r['paragraphes_sans_connecteur'])
    import re
    for p in re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',body,re.S):
        t=C.texte(p)
        if len(t.split())>40 and not C.CONNECT.search(t): print('   SANSCONN:',t[:90])
    for k,v in r['defauts'].items():
        if k.startswith('C_'): continue
        print('  ',k,v['n']); [print('      ',x) for x in v['ex']]
