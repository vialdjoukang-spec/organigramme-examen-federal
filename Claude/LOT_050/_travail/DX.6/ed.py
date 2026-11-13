import sys
def rep(f,pairs):
    t=open('src/'+f,encoding='utf-8').read()
    for a,b in pairs:
        if a not in t: print('MISS',f,a[:70]); continue
        t=t.replace(a,b,1)
    open('src/'+f,'w',encoding='utf-8').write(t)
