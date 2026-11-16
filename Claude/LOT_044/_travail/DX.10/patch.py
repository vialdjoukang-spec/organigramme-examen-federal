import sys
def P(f,a,b):
    s=open(f,encoding='utf-8').read()
    if a not in s: print('ABSENT',f,a[:60]); return
    open(f,'w',encoding='utf-8').write(s.replace(a,b,1))
