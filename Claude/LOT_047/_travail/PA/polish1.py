import re,glob,sys
F={}
for f in glob.glob('src/p*.txt'): F[f]=open(f,encoding='utf-8').read()
miss=[]
def fix(old,new):
    for f,t in F.items():
        i=t.find(old)
        if i<0: continue
        j=i+len(old)
        m=re.match(r'\s*\[\[([^\]]+)\]\]',t[j:])
        if m:
            c=' [['+m.group(1)+']]'
            repl=new.replace('{C}',c)+c
            t=t[:i]+repl+t[j+m.end():]
        else:
            t=t[:i]+new.replace('{C}','')+t[j:]
        F[f]=t; return
    miss.append(old[:60])
exec(open('fixes1.py',encoding='utf-8').read())
for f,t in F.items(): open(f,'w',encoding='utf-8').write(t)
print('manquants',miss)
