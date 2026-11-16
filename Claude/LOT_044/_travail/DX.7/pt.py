import sys
def patch(f,R):
    p=open(f).read()
    for a,b in R:
        assert a in p,('MISSING',a[:60]); p=p.replace(a,b)
    open(f,'w').write(p)
