def sub(p,pairs):
    h=open(p).read()
    for a,b in pairs:
        if a not in h: print('MISSING',p,a[:60]); continue
        h=h.replace(a,b,1)
    open(p,'w').write(h)
