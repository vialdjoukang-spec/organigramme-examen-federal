import re,glob,sys
sys.path.insert(0,'/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils')
import controle3 as C
SAFE=('Le ','La ','Les ','Un ','Une ','Il ','Elle ','Ces ','Cette ','Ce ','Aucun ','Chez ','Dans ','Pour ','Sur ','Lors ','Parmi ','Chaque ','Le<','La<')
ins=0
for f in sorted(glob.glob('src/p*.txt')):
    t=open(f,encoding='utf-8').read()
    def fix(m):
        global ins
        body=m.group(1)
        tt=C.texte(re.sub(r'\[\[[^\]]*\]\]','',re.sub(r'<[^>]+>',' ',body)))
        if len(tt.split())<=40 or C.CONNECT.search(tt): return m.group(0)
        # phrases: coupe après [[...]]. ou . + espace + Majuscule
        parts=re.split(r'(?<=[.!?])(?:\[\[[^\]]*\]\])?\s+(?=[A-ZÀ-Ý«])',body)
        # reconstruire en gardant les séparateurs : utiliser finditer
        idx=[m2.end() for m2 in re.finditer(r'[.!?](?:\[\[[^\]]*\]\])?\s+(?=[A-ZÀ-Ý«])',body)]
        for pos in idx:
            rest=body[pos:]
            if rest.startswith(SAFE):
                w=rest.split(' ',1)
                new=body[:pos]+'En outre, '+w[0][0].lower()+rest[1:]
                ins+=1
                return '<div class="p">'+new+'</div>'
        return m.group(0)
    t2=re.sub(r'<div class="p">(.*?)</div>',fix,t,flags=re.S)
    open(f,'w',encoding='utf-8').write(t2)
print('inserted',ins)
