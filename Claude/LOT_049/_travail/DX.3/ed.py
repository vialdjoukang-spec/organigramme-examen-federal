import sys
def sub(f,a,b):
    p=open(f,encoding='utf-8').read()
    if a not in p: print('MISSING:',a[:70]); return
    open(f,'w',encoding='utf-8').write(p.replace(a,b,1))
