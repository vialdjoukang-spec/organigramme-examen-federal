import re,glob,sys
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as C
def plain(s): return re.sub(r'\{\{f\d+\|([^}]+)\}\}',r'\1',re.sub(r'\[\[.+?\]\]','',s))
mode=sys.argv[1]
for f in sorted(glob.glob('src/p*.txt')):
    for ln_no,ln in enumerate(open(f,encoding='utf-8').read().split('\n')):
        k,_,rest=ln.partition(' ')
        if k not in('P','L','L2'): continue
        sents=re.split(r'(?<=[.!?])(?:\[\[.+?\]\])?\s+(?=[A-ZÀ-Ý«])',rest)
        # more faithful: split on plain
        parts=[];buf=''
        for m in re.finditer(r'.*?(?:[.!?](?:\[\[.+?\]\])?(?:\s+(?=[A-ZÀ-Ý«])|$))',rest,re.S): parts.append(m.group(0))
        if not parts: parts=[rest]
        for p in parts:
            t=plain(p).strip(); n=len(t.split())
            if mode=='long' and n>32: print(f'{f}:{ln_no} [{n}] {p.strip()}\n')
            if mode=='nom' and n>=4 and not C.est_verbale(t): print(f'{f}:{ln_no} NOM {p.strip()}\n')
        if mode=='conn' and k=='P':
            t=plain(rest)
            if len(t.split())>40 and not C.CONNECT.search(t): print(f'{f}:{ln_no} CONN {t[:140]}\n')
