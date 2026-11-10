import sys
def rep(f,pairs):
    s=open(f).read()
    for o,n in pairs:
        if o not in s: print('MISS',f,o[:60]); continue
        s=s.replace(o,n)
    open(f,'w').write(s)
