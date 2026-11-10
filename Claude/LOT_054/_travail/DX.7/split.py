import re,glob,sys
TOK=[(', car ','. En effet, '),(', mais ','. Cependant, '),(' alors que ','. En revanche, '),(' tandis que ','. En revanche, '),(', ce qui ','. Cela '),(', puisque ','. En effet, '),(' parce que ','. En effet, ')]
def words(s): return len(re.sub(r'\[\[[^\]]*\]\]|<[^>]+>','',s).split())
for f in sorted(glob.glob('src/p*.src')):
    out=[]; n=0
    for line in open(f).read().split('\n'):
        if not re.match(r'\s*<(div class="p"|li|p)',line) :
            out.append(line); continue
        parts=re.split(r'(?<=\.)(?=\s+[A-ZÀ-Ý«])|(?<=\.)(?=<)',line)
        res=[]
        for s in parts:
            if words(s)>30:
                m=re.search(r'(\[\[[^\]]*\]\])\.?(</div>|</li>|</p>)?\s*$',s)
                cite=m.group(1) if m else ''
                best=None
                for tok,rep in TOK:
                    for mm in re.finditer(re.escape(tok),s):
                        a,b=s[:mm.start()],s[mm.end():]
                        if words(a)>=8 and words(b)>=8:
                            sc=abs(words(a)-words(b))
                            if best is None or sc<best[0]: best=(sc,mm,tok,rep)
                if best:
                    _,mm,tok,rep=best
                    a=s[:mm.start()]; b=s[mm.end():]
                    if cite and not re.search(r'\[\[[^\]]*\]\]\s*$',a): a=a+cite
                    s=a+rep+b[0].upper()+b[1:] if rep.endswith(', ') is False else a+rep+b
                    n+=1
            res.append(s)
        out.append(''.join(res))
    open(f,'w').write('\n'.join(out))
    print(f,n)
