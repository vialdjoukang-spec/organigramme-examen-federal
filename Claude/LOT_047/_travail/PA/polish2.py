import re,glob
F={}
for f in glob.glob('src/p*.txt'): F[f]=open(f,encoding='utf-8').read()
miss=[]
def fixx(old,new):
    for f,t in F.items():
        i=t.find(old)
        if i<0: continue
        j=i+len(old)
        m=re.match(r'\s*\[\[([^\]]+)\]\]',t[j:])
        if m: j+=m.end()
        F[f]=t[:i]+new+t[j:]; return
    miss.append(old[:70])
exec(open('fixes2.py',encoding='utf-8').read())
for f,t in F.items(): open(f,'w',encoding='utf-8').write(t)
print('manquants',miss)
