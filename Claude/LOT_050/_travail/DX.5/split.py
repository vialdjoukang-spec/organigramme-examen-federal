import re,glob,html
def wc(s): return len(re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>|\^[\w.\-:,]+\^',' ',s))).split())
CANDS=[(r'; ',None),(r', car ','En effet, '),(r', puisque ','En effet, '),(r', alors que ','En revanche, '),(r', tandis que ','En revanche, '),(r', mais ','Cependant, '),(r', ce qui ','Cela '),(r', si bien que ','Ainsi, '),(r', de sorte que ','Ainsi, ')]
def split_sentence(s):
    n=wc(s)
    if n<=28: return [s]
    best=None
    for pat,rep in CANDS:
        for m in re.finditer(pat,s):
            a,b=s[:m.start()],s[m.end():]
            if wc(a)>=8 and wc(b)>=6 and a.count('(')==a.count(')') and not re.search(r'^(Phase|Posologie|Classe|Contre)',a):
                score=abs(wc(a)-wc(b))
                if pat in (r' : ',r'; '): score+=3
                if best is None or score<best[0]: best=(score,m,rep)
    if not best: return [s]
    _,m,rep=best
    a,b=s[:m.start()],s[m.end():]
    if rep is None: nb=b[0].upper()+b[1:]
    elif rep=='Cela concerne ': nb='Cela concerne '+b
    elif rep=='Cela ': nb='Cela '+b
    else: nb=rep+b
    first=a.rstrip()
    if not first.endswith('.'): first+='.'
    parts=[first]+split_sentence(nb)
    return parts
for f in sorted(glob.glob('src/p0[1-9].txt')+glob.glob('src/p1[01].txt')):
    out=[]
    for line in open(f,encoding='utf-8'):
        l=line.rstrip('\n')
        if l.startswith('<div class="p">') and l.endswith('</div>') and '<table' not in l:
            body=l[len('<div class="p">'):-6]
            sents=re.split(r'(?<=[.!?])(?:(?:\^[\w.\-:,]+\^)?)\s+(?=[A-ZÀ-Ý«<])',body)
            # keep cites attached: re-split carefully
            sents=re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])',body)
            new=[]
            for s in sents:
                # s may end with period; strip final period for processing
                end=''
                m=re.search(r'(\.|\?|!)$',s)
                if m: end=m.group(1); s=s[:-1]
                parts=split_sentence(s)
                cs=re.findall(r'\^[\w.\-:,]+\^',s)
                if cs and len(parts)>1:
                    ids=','.join(dict.fromkeys(x.strip('^') for x in cs)); parts=[p if '^' in p else p.rstrip('.')+'^'+ids+'^'+('.' if p.endswith('.') else '') for p in parts]
                new.append(' '.join(parts[:-1]+[parts[-1]+end]) if len(parts)>1 else parts[0]+end)
            l='<div class="p">'+' '.join(new)+'</div>'
        out.append(l)
    open(f,'w',encoding='utf-8').write('\n'.join(out)+'\n')
