import re,glob,sys
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
from controle3 import nombres, STRUCT, DOSE
n=0
for f in sorted(glob.glob('src/p*.txt')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'([.!?])((?:\[\[[^\]]+\]\])+)',r'\2\1',t)
    parts=re.split(r'(?<=[.!?])(\s+)(?=[A-ZÀ-Ý])',t)
    for i in range(0,len(parts)-2,2):
        s=parts[i]; nxt=parts[i+2]
        if '[[' in s: continue
        plain=re.sub(r'<[^>]+>',' ',s)
        if (nombres(STRUCT.sub(' ',plain)) or DOSE.search(plain)) :
            m=re.match(r'^[^<\[]*?((?:\[\[[^\]]+\]\])+)[.!?]',nxt)
            m=re.search(r'((?:\[\[[^\]]+\]\])+)[.!?](?:\s|$|<)',nxt)
            if m:
                tok=m.group(1)
                parts[i]=re.sub(r'([.!?])$',tok+r'\1',s,count=1); n+=1
    open(f,'w',encoding='utf-8').write(''.join(parts))
print(n)
