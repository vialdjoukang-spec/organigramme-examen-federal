import sys
def patch(fn,pairs):
    s=open('/home/user/wt/lot-050/Claude/LOT_050/_travail/DX.8/src/'+fn,encoding='utf-8').read()
    bad=[]
    for a,b in pairs:
        if a in s: s=s.replace(a,b)
        else: bad.append(a[:70])
    open('/home/user/wt/lot-050/Claude/LOT_050/_travail/DX.8/src/'+fn,'w',encoding='utf-8').write(s)
    for b in bad: print('NOT FOUND',fn,b)
