import re,sys
def patch(f,prefix,new):
    p=f'src/{f}.txt'; s=open(p,encoding='utf-8').read()
    i=s.find(prefix)
    if i<0: print('MISS',f,prefix[:50]); return
    if s.find(prefix,i+1)>=0: print('DUP',f,prefix[:50])
    m=re.compile(r'\.(?=\s|<|$)').search(s,i+len(prefix)-1) if not prefix.endswith('.') else None
    # find sentence end from i
    j=i
    while True:
        k=s.find('.',j)
        if k<0: print('NOEND',prefix[:40]); return
        nxt=s[k+1:k+2]
        if nxt=='' or nxt in ' \n<':
            break
        j=k+1
    s=s[:i]+new+s[k+1:]
    open(p,'w',encoding='utf-8').write(s)
