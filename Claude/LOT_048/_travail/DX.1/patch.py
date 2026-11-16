import sys,re
def patch(f,pairs):
    s=open('src/'+f).read()
    for a,b in pairs:
        if a not in s: print('MISS',f,a[:70]); continue
        if s.count(a)>1: print('MULTI',f,a[:70])
        s=s.replace(a,b,1)
    open('src/'+f,'w').write(s)
