import re,glob
def rs(start,new,files=None):
    for f in sorted(glob.glob('src/p*.txt')):
        s=open(f,encoding='utf-8').read()
        i=s.find(start)
        if i<0: continue
        m=re.compile(r'\]\]\.(?=\s|<|$)|(?<![\]A-Z])\.(?=\s|<|$)').search(s,i+len(start)-1)
        j=m.end()
        s=s[:i]+new+s[j:]
        open(f,'w',encoding='utf-8').write(s); return f
    raise SystemExit('NOT FOUND: '+start[:60])
