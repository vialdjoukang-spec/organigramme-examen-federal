import re,glob,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
CITE=re.compile(r'(?:\[\[[^\]]+\]\])+')
def words(s): return len(re.sub(r'<[^>]+>|\[\[[^\]]+\]\]','',s).split())
SPLITS=[(', alors que ','. En revanche, '),(', tandis que ','. En revanche, '),(', mais ','. Cependant, '),(', car ','. En effet, '),(', puis ','. Ensuite, '),(', ce qui ','. Dès lors, cela ')]
def split_long(sent):
    if words(sent)<=28: return sent
    cites=''.join(CITE.findall(sent))
    body=sent
    best=None
    for pat,rep in SPLITS:
        for m in re.finditer(re.escape(pat),sent):
            a,b=sent[:m.start()],sent[m.end():]
            wa,wb=words(a),words(b)
            if wa>=7 and wb>=7:
                score=abs(wa-wb)
                if best is None or score<best[0]: best=(score,m,rep)
    if not best: return sent
    _,m,rep=best
    a,b=sent[:m.start()],sent[m.end():]
    a=CITE.sub('',a) if False else a
    # a se termine sans cite : on duplique les citations de la phrase
    allc=''.join(CITE.findall(sent))
    b=b.rstrip()
    # b se termine par cites + '.' ; garde tel quel
    return a+allc+rep+b
def process(txt):
    out=[]
    for line in txt.split('\n'):
        if line.startswith('<tr>') or line.startswith('<h4') or not line.strip(): out.append(line); continue
        sents=re.split(r'(?<=\.)\s+(?=[A-ZÀ-Ý«<])',line)
        sents=[split_long(s) for s in sents]
        line=' '.join(sents)
        out.append(line)
    return '\n'.join(out)
for f in sorted(glob.glob('src/p*.txt')):
    t=open(f,encoding='utf-8').read()
    t2=process(t)
    if t2!=t: open(f,'w',encoding='utf-8').write(t2); print('fixed',f)
