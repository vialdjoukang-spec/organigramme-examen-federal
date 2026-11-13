import re,glob,sys,json
def plain(s): return re.sub(r'\{\{f\d+\|([^}]+)\}\}',r'\1',re.sub(r'\[\[.+?\]\]','',s))
SPL=re.compile(r'.*?(?:[.!?](?:\[\[.+?\]\])?(?:\s+(?=[A-ZÀ-Ý«])|$))',re.S)
def sents(rest):
    parts=[m.group(0) for m in SPL.finditer(rest)]
    tail=rest[len(''.join(parts)):]
    if tail: parts.append(tail)
    return parts
def tok(p):
    cites=re.findall(r'\[\[.+?\]\]',p)
    t=p
    for i,c in enumerate(cites,1): t=t.replace(c,f'@{i}',1)
    return t,cites
if sys.argv[1]=='list':
    lo,hi=int(sys.argv[2]),int(sys.argv[3]); k=0
    for f in sorted(glob.glob('src/p*.txt')):
        for ln,l in enumerate(open(f,encoding='utf-8').read().split('\n')):
            kind,_,rest=l.partition(' ')
            if kind not in('P','L','L2'): continue
            for i,p in enumerate(sents(rest)):
                n=len(plain(p).split())
                if n>32:
                    k+=1
                    if lo<=k<=hi:
                        t,c=tok(p); print(f'{f}|{ln}|{i}|{n}\n{t.strip()}\n')
else:
    # apply: patchfile lines "f|ln|i|newtext"
    P={}
    for l in open(sys.argv[2],encoding='utf-8'):
        l=l.rstrip('\n')
        if not l.strip(): continue
        f,ln,i,new=l.split('|',3); P.setdefault(f,{})[(int(ln),int(i))]=new
    for f,d in P.items():
        lines=open(f,encoding='utf-8').read().split('\n')
        for (ln,i),new in sorted(d.items(),reverse=True):
            kind,_,rest=lines[ln].partition(' ')
            ps=sents(rest)
            _,cites=tok(ps[i])
            trail=' ' if ps[i].endswith(' ') else ''
            new2=re.sub(r'@(\d)',lambda m:cites[int(m.group(1))-1],new)
            ps[i]=new2+trail
            lines[ln]=kind+' '+''.join(ps)
        open(f,'w',encoding='utf-8').write('\n'.join(lines))
