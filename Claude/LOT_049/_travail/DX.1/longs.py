import re,sys,html
LIM=int(sys.argv[2]) if len(sys.argv)>2 else 28
f=sys.argv[1]
s=open(f).read().replace('</P>','</P>\n').replace('<P>','\n<P>').replace('</W>','</W>\n')
def words(t): return len(re.sub(r'\{[^{}]*\}|<[^>]+>',' ',t).split())
# split like controle3 on src text
for m in re.finditer(r'[^\n]+',s):
    line=m.group(0)
    if line.startswith('<T>') or line.startswith('<tr') or line.startswith('<th') : continue
    for sent in re.split(r'(?<=[.!?])(?:\{[^{}]*\})*\s+(?=[A-ZÀ-Ý«])',line):
        pass
for line in s.split('\n'):
    if re.match(r'\s*<(tr|T|/T|thead|tbody|h4)',line): continue
    parts=re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«<])',line)
    for p in parts:
        w=words(p)
        if w>LIM: print(w,'::',p[:600]); print()
