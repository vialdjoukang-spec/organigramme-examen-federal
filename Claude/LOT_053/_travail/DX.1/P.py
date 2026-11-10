import sys
def patch(f,pairs):
    p='/home/user/wt/lot-053/Claude/LOT_053/_travail/DX.1/fragments/'+f
    s=open(p,encoding='utf8').read()
    for a,b in pairs:
        if a not in s: print('MISS',f,a[:70]); continue
        s=s.replace(a,b)
    open(p,'w',encoding='utf8').write(s)
