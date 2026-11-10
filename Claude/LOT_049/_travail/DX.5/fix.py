import sys
def sub(f,pairs):
    t=open(f).read()
    for a,b in pairs:
        if a not in t: print('MISSING',f,'|',a[:70]); continue
        t=t.replace(a,b)
    open(f,'w').write(t)
