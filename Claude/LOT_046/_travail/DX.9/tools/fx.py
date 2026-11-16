import re,glob,os,sys
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/src'
TOK=r'((?:\{[A-Z0-9]+:\d+\})*)'
def fix(old,new,files=None,count=None):
    pat=re.compile(re.escape(old.rstrip('.'))+TOK+r'(\.?)')
    n=0
    for f in sorted(glob.glob(D+'/p*.html')):
        t=open(f).read()
        def r(m):
            nonlocal n
            n+=1
            if '<T>' in new: return new.replace('<T>',m.group(1))
            if '{' in new: return new
            return new.rstrip('.')+m.group(1)+(m.group(2) or '.')
        t2=pat.sub(r,t)
        if t2!=t: open(f,'w').write(t2)
    if n==0: print('NON TROUVÉ:',old[:80])
    return n
