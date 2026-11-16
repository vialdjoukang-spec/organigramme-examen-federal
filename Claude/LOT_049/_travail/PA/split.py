import re,glob,sys
MAP=[(", tandis qu'","En revanche, "),(", tandis que ","En revanche, "),(", alors que ","En revanche, "),(", alors qu'","En revanche, "),(", car ","En effet, "),(", ce qui ","Cela "),(", mais ","Cependant, "),(", puis ","Ensuite, "),(" ; ","")]
def wc(s):
    s=re.sub(r'\{[^}]*\}','',s); s=re.sub(r'\[\[\w+\|(.*?)\]\]',r'\1',s); return len(s.split())
def fix_sentence(s):
    m=re.match(r'^(.*?)((?: \{[\w.,\-]+\})?)\.$',s,re.S)
    if not m: return s
    body,cite=m.group(1),m.group(2)
    if wc(body)<=28: return s
    best=None
    n=len(body.split())
    for mk,rep in MAP:
        for mm in re.finditer(re.escape(mk),body):
            a=body[:mm.start()]; b=body[mm.end():]
            if wc(a)<8 or wc(b)<6: continue
            sc=abs(wc(a)-wc(b))
            if best is None or sc<best[0]: best=(sc,a,b,rep)
    if not best: return s
    _,a,b,rep=best
    b2=(rep+b) if rep else b
    if rep=="" : b2=b[0].upper()+b[1:]
    elif rep.endswith(' ') and rep[0].isupper(): b2=rep+b
    first=fix_sentence(a+cite+'.') if wc(a)>28 else a+cite+'.'
    second=fix_sentence(b2[0].upper()+b2[1:]+cite+'.') if wc(b2)>28 else b2[0].upper()+b2[1:]+cite+'.'
    return first+' '+second
def para(t):
    parts=re.split(r'(?<=\.)\s+(?=[A-ZÀ-ÝÉ«\[])',t)
    return ' '.join(fix_sentence(p) for p in parts)
for f in sorted(glob.glob('p*.txt')):
    L=open(f,encoding='utf-8').read().split('\n'); out=[]
    for l in L:
        if l.startswith('P '): l='P '+para(l[2:])
        elif l.startswith('F '):
            k,_,v=l[2:].partition(' '); l='F '+k+' '+' ¶ '.join(para(x.strip()) for x in v.split('¶'))
        out.append(l)
    open(f,'w',encoding='utf-8').write('\n'.join(out))
