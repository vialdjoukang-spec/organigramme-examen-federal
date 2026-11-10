import re,sys,glob
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
for f in sorted(glob.glob('src/p*.txt')):
    for i,l in enumerate(open(f,encoding='utf8')):
        if not l.startswith('P: '): continue
        t=re.sub(r'<<([^|>]+)\|[^|>]*\|[^>]+>>',r'\1',l[3:]); t=re.sub(r'\[\[[^\]]+\]\]','',t)
        if len(t.split())>40 and not c.CONNECT.search(t): print(f'{f}:{i+1}: {len(t.split())} mots :: {t[:110]}')
