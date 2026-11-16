import sys
def sub(f,R):
    p=open(f).read()
    for a,b in R:
        if a not in p: print('MISSING',f,a[:60]); continue
        p=p.replace(a,b,1)
    open(f,'w').write(p)
