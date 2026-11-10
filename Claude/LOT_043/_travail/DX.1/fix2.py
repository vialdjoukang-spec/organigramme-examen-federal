import re,glob,sys
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
from controle3 import CONNECT, texte
cyc=['Par ailleurs, ','En outre, ']
k=0; n=0
SKIP=re.compile(r"^(NICE|Verdon|Bösner|Marburg|Ronga|Haasenritter|Heberden|Bass|Genève|HUG|SAPHO|Tietze|Cyriax|[A-Z]{2,}|Lausanne|Pendant|Dans une|Dans la)")
for f in sorted(glob.glob('src/p*.txt')):
    t=open(f,encoding='utf-8').read()
    def fix(m):
        global k,n
        body=m.group(1)
        tx=texte(re.sub(r'\[\[[^\]]+\]\]','',body))
        if len(tx.split())<=40 or CONNECT.search(tx): return m.group(0)
        parts=re.split(r'((?:\.\[\[[^\]]+\]\]|\.)\s+)(?=[A-ZÀ-Ý])',body)
        # parts: s0, sep0, s1, sep1, ...
        for i in range(2,len(parts),2):
            s=parts[i]
            if SKIP.match(s) or s.startswith('<'): continue
            c=cyc[k%2]; k+=1
            parts[i]=c+s[0].lower()+s[1:]
            n+=1
            return '<div class="p">'+''.join(parts)+'</div>'
        return m.group(0)
    t2=re.sub(r'<div class="p">(.*?)</div>',fix,t,flags=re.S)
    open(f,'w',encoding='utf-8').write(t2)
print(n)
