import re, sys, os, glob
sys.path.insert(0, os.environ['OUTILS_REF'])
import controle3 as C
SEG = re.compile(r'((?:[.!?])(?:\[\[[^\]]+\]\])?)(\s+)(?=[A-ZÀ-Ý«{<])')
CIT = re.compile(r'\[\[([^\]]+)\]\]')
def words(t):
    t = re.sub(r'\{\{f\d+\|([^}]*)\}\}', r'\1', t); t = re.sub(r'<[^>]+>', ' ', t); t = CIT.sub('', t)
    return len(t.split())
RULES = [(', car ', '. En effet, ', 'car'), (', mais ', '. Cependant, ', 'mais'), (', tandis que ', '. En revanche, ', 'tandis'),
         (', alors que ', '. En revanche, ', 'alors'), (', puis ', '. Ensuite, ', 'puis'), ('; ', '. ', ';'), (', ce qui ', '. Cela ', 'cequi'),
         (', et ', '. De plus, ', 'et'), (' ; ', '. ', ';')]
def split_sentence(s):
    m = CIT.search(s[::-1][:0]) 
    mm = re.match(r'^(.*?)([.!?])((?:\[\[[^\]]+\]\])?)$', s, re.S)
    if not mm: return s
    body, p, cite = mm.groups()
    if words(body) <= 30: return s
    best = None
    for pat, rep, nm in RULES:
        for m in re.finditer(re.escape(pat), body):
            L, R = body[:m.start()], body[m.end():]
            wl, wr = words(L), words(R)
            if wl < 9 or wr < 8 or wl > 29 or wr > 29: continue
            R2 = R[0].upper() + R[1:] if rep.endswith('. ') else R
            right = (rep[2:] + R) if rep != '. ' else (R[0].upper() + R[1:])
            right_txt = re.sub(r'\{\{f\d+\|([^}]*)\}\}', r'\1', re.sub(r'<[^>]+>', ' ', right))
            if not C.est_verbale(re.sub(r'^(En effet|Cependant|En revanche|Ensuite|Cela|De plus), ?', '', right_txt)): continue
            if not C.est_verbale(re.sub(r'<[^>]+>', ' ', L)): continue
            score = abs(wl - wr)
            if best is None or score < best[0]:
                best = (score, L, right)
    if best is None: return s
    _, L, right = best
    if right.startswith('Cela ') is False and right[:1].islower(): pass
    return L + p + cite + ' ' + right + p + cite
def process_line(l):
    if not (l.startswith('P ') or l.startswith('<li>')): return l
    parts = SEG.split(l)
    # parts: text, punct+cite, space, text, ...
    out = []; i = 0
    cur = parts[0]
    res = []
    sents = []
    k = 0
    # rebuild sentences
    toks = []
    pos = 0
    for m in SEG.finditer(l):
        toks.append(l[pos:m.end(1)]); toks.append(m.group(2)); pos = m.end()
    toks.append(l[pos:])
    new = []
    for t in toks:
        if t.strip() == '' : new.append(t); continue
        new.append(split_sentence(t))
    return ''.join(new)
for f in sorted(glob.glob('src/p[0-9][0-9].txt')):
    n = int(os.path.basename(f)[1:3])
    if n in (13, 14): continue
    L = open(f, encoding='utf-8').read().split('\n')
    O = [process_line(l) for l in L]
    open(f, 'w', encoding='utf-8').write('\n'.join(O))
    print(f, sum(1 for a, b in zip(L, O) if a != b))
