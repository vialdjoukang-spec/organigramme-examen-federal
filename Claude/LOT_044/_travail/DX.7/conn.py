import re,sys,os
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as C
CONS=["Par ailleurs, ","Ensuite, ","En outre, ","Enfin, "]
SPL=re.compile(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])')
k=0; single=[]
def conv(s): return re.sub(r'\[\[([^\]]+)\]\]','<sup class="r">x</sup>',s)
for f in sorted(os.listdir('src')):
    if not f.endswith('.txt'): continue
    s=open('src/'+f,encoding='utf-8').read()
    def fix(m):
        global k
        body=m.group(1)
        t=C.texte(re.sub(r'<sup class="r">.*?</sup>','',conv(body),flags=re.S))
        tt=C.texte(conv(body))
        if len(t.split())<=40 or C.CONNECT.search(tt): return m.group(0)
        parts=SPL.split(body)
        if len(parts)<2:
            single.append(f+': '+t[:100]); return m.group(0)
        i=1 if len(parts)<3 else 1
        p=parts[i]
        if p.startswith(('<','{{','%%')) or not p: return m.group(0)
        first=p[0]
        c=CONS[k%len(CONS)]; k+=1
        parts[i]=c+first.lower()+p[1:]
        # reconstruct with original separators
        seps=SPL.findall(body)
        out=parts[0]
        for j in range(1,len(parts)): out+=seps[j-1]+parts[j]
        return '<div class="p">'+out+'</div>'
    s2=re.sub(r'<div class="p">(.*?)</div>',fix,s,flags=re.S)
    open('src/'+f,'w',encoding='utf-8').write(s2)
print('inserted',k); print('\n'.join(single))
