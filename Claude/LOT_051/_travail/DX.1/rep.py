import sys
def rep(f,R):
    s=open(f).read()
    for a,b in R:
        if a not in s: print('MISSING',f,a[:60]); continue
        s=s.replace(a,b)
    open(f,'w').write(s)
