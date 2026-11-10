import sys,re,glob,importlib.util
spec=importlib.util.spec_from_file_location('c3','/home/user/organigramme-examen-federal/Claude/_outils/controle3.py'); c3=importlib.util.module_from_spec(spec); spec.loader.exec_module(c3)
mode=sys.argv[1]
for f in sorted(glob.glob('fragments/p*.html')):
    h=open(f).read()
    for tag,b,t in c3.phrases_html(h):
        if tag.lower()=='td': continue
        n=len(t.split())
        if mode=='long' and n>32: print(f[-8:-5],n,'|',t)
        if mode=='nom' and not c3.est_verbale(t): print(f[-8:-5],n,'|',t)
    if mode=='para':
        for p in re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>',h,re.S|re.I):
            tx=c3.texte(p)
            if len(tx.split())>40 and not c3.CONNECT.search(tx): print(f[-8:-5],len(tx.split()),'|',tx[:200])
