import re, os, glob, sys
sys.path.insert(0, os.environ['OUTILS_REF'])
import controle3 as C
SEG = re.compile(r'((?:[.!?])(?:\[\[[^\]]+\]\])?)(\s+)(?=[A-ZÀ-Ý])')
ORD = ['Par ailleurs, ', 'En outre, ', 'Ainsi, ', 'Ensuite, ']
OK = {'Le','La','Les','Un','Une','Il','Elle','Ces','Cette','Ce','Chez','Pour','Dans'}
def rendered(l):
    t = re.sub(r'\{\{f\d+\|([^}]*)\}\}', r'\1', l); t = re.sub(r'\[\[[^\]]+\]\]', '', t); t = re.sub(r'<[^>]+>', ' ', t)
    return t
tot = 0
for f in sorted(glob.glob('src/p[0-9][0-9].txt')):
    n = int(os.path.basename(f)[1:3])
    if n in (10, 13, 14): continue
    L = open(f, encoding='utf-8').read().split('\n'); O = []
    for l in L:
        if not l.startswith('P ') or len(rendered(l).split()) < 60: O.append(l); continue
        toks = []; pos = 0
        for m in SEG.finditer(l):
            toks.append(l[pos:m.end(1)] + m.group(2)); pos = m.end()
        toks.append(l[pos:])
        if len(toks) < 4: O.append(l); continue
        s = toks[2]; w = re.match(r'([A-Za-zÀ-ÿ\-]+)', s)
        if w and w.group(1) in OK and not C.CONNECT.search(rendered(s)):
            toks[2] = ORD[tot % 4] + s[0].lower() + s[1:]; tot += 1
        O.append(''.join(toks))
    open(f, 'w', encoding='utf-8').write('\n'.join(O))
print(tot)
