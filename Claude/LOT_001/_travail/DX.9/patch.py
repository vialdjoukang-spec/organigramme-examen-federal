import sys
def P(f,pairs):
    p=f'/home/user/wt/lot-001/Claude/LOT_001/_travail/DX.9/s/{f}.html'
    t=open(p,encoding='utf-8').read()
    for a,b in pairs:
        n=t.count(a)
        if n!=1: print('!!',f,n,a[:60]); continue
        t=t.replace(a,b)
    open(p,'w',encoding='utf-8').write(t)
