import re,glob,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
ART={'Le','La','Les','Un','Une','Chez','Dans','Il','Elle','Elles','Ils','Ce','Cette','Ces','Cet','L\'','Pour','Selon','Après','Avec','Sur','Aux','Des','Du','Lors','Quand','En','À','On','Cela','Leur','Leurs','Son','Sa','Ses','Toute','Tout','Chaque','Certains','Une'}
CONN=['Par ailleurs,','En outre,']
k=0
for f in sorted(glob.glob('src/p*.txt')):
    t=open(f).read()
    def fix(m):
        global k
        raw=m.group(1)
        tx=C.texte(re.sub(r'\[\[[^\]]*\]\]','',raw))
        if len(tx.split())<=40 or C.CONNECT.search(tx): return m.group(0)
        # find sentence boundaries in raw: ". " or "]]. " followed by capital
        pos=[x for x in re.finditer(r'(?<=[.!?])(?:\[\[[^\]]*\]\])*\s+(?=(?:<[^>]+>)*[A-ZÀ-Ý])',raw)]
        # need boundary of the form ".  Next" ; compute candidate insertion at second sentence = first boundary after >=8 words
        for p in pos:
            before=C.texte(re.sub(r'\[\[[^\]]*\]\]','',raw[:p.start()]))
            if len(before.split())>=6:
                i=p.end()
                m2=re.match(r'((?:<[^>]+>)*)([^\s<,]+)',raw[i:])
                w=m2.group(2)
                c=CONN[k%2]; k+=1
                if w in ART or w.rstrip("'") in ART:
                    w2=w[0].lower()+w[1:]
                else: w2=w
                new=raw[:i]+c+' '+m2.group(1)+w2+raw[i+m2.end():]
                return m.group(0).replace(raw,new)
        return m.group(0)
    t2=re.sub(r'<div class="p">(.*?)</div>',fix,t,flags=re.S)
    open(f,'w').write(t2)
print('done',k)
