import sys
def sub(f,pairs):
    t=open(f,encoding='utf-8').read()
    for a,b in pairs:
        if a not in t: print('MISS',f,a[:60]); continue
        t=t.replace(a,b)
    open(f,'w',encoding='utf-8').write(t)
