import sys
def fx(n,R):
    f=f'src_txt/p{n:02d}.txt'; s=open(f).read()
    for a,b in R:
        if a not in s: print('ABSENT',n,a[:50]); continue
        s=s.replace(a,b)
    open(f,'w').write(s)
