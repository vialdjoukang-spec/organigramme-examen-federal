import re,sys
def rsent(f,start,new,cnt=1):
    s=open(f,encoding='utf-8').read()
    n=s.count(start)
    assert n>=1,(f,start[:60])
    assert n==1,(f,'multi',start[:60],n)
    i=s.index(start)
    m=re.compile(r'\.(?=\s|$)').search(s,i)
    j=m.end()
    s=s[:i]+new+s[j:]
    open(f,'w',encoding='utf-8').write(s)
