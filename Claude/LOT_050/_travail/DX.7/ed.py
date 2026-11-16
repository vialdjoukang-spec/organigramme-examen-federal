import sys,re
def rep(p,pairs):
    t=open(p,encoding='utf-8').read()
    for a,b in pairs:
        if a not in t: print('MANQUE',p,a[:60]); continue
        t=t.replace(a,b,1)
    open(p,'w',encoding='utf-8').write(t)
