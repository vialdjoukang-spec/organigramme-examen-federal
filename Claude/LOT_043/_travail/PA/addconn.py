import re, os, glob, sys
sys.path.insert(0, os.environ['OUTILS_REF'])
import controle3 as C
SEG = re.compile(r'((?:[.!?])(?:\[\[[^\]]+\]\])?)(\s+)(?=[A-ZÀ-Ý])')
SKIP = {'NICE','HUG','Revue','Société','Verdon','Bösner','Haasenritter','Nitroglycerin','Heparin-Na','Morphini','Paracétamol','Selon','Dans','En','Chez','Pour','Si','Lorsque','Ainsi','Cependant','Cela','De','Un','Une','Le','La','Les','L','Il','Elle','Ces','Cette','Ce','Aucun','Aucune'}
ORD = ['Ensuite, ', 'Par ailleurs, ', 'En outre, ', 'Enfin, ']
def rendered(l):
    t = re.sub(r'\{\{f\d+\|([^}]*)\}\}', r'\1', l); t = re.sub(r'\[\[[^\]]+\]\]', '', t); t = re.sub(r'<[^>]+>', ' ', t)
    return t
def fix(l, which):
    if not (l.startswith('P ') or l.startswith('<li>')): return l
    t = rendered(l)
    if len(t.split()) <= 38 or C.CONNECT.search(t): return l
    toks = []; pos = 0
    for m in SEG.finditer(l):
        toks.append(l[pos:m.end(1)] + m.group(2)); pos = m.end()
    toks.append(l[pos:])
    k = 0; out = []
    for i, s in enumerate(toks):
        if i in which and i < len(toks):
            w = re.match(r'([A-Za-zÀ-ÿ\-]+)', s)
            if w and w.group(1) in {'Le','La','Les','Un','Une','Il','Elle','Ces','Cette','Ce','Aucun','Aucune','Chez','Pour','Dans','Selon'} and not C.CONNECT.search(rendered(s)):
                s = ORD[k % 4] + s[0].lower() + s[1:]; k += 1
        out.append(s)
    return ''.join(out)
for f in sorted(glob.glob('src/p[0-9][0-9].txt')):
    n = int(os.path.basename(f)[1:3])
    if n in (13, 14): continue
    L = open(f, encoding='utf-8').read().split('\n')
    O = [fix(l, {1, 3}) for l in L]
    open(f, 'w', encoding='utf-8').write('\n'.join(O))
    print(f, sum(1 for a, b in zip(L, O) if a != b))
