import re,glob,importlib.util,itertools
spec=importlib.util.spec_from_file_location('c3','/home/user/organigramme-examen-federal/Claude/_outils/controle3.py'); C=importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
CIT=re.compile(r'\[\[[\w\-|]+\]\]')
LOW={'Le','La','Les',"L'",'Un','Une','Des','Elle','Il','Ils','Elles','Ce','Cette','Ces','Cela','Dans','Chez','Pour','Lorsque','Si','Après','Avant','En','Selon','Chaque','Aucun','Son','Sa','Ses','Leur','Deux','Quatre','Trois'}
PREF=itertools.cycle(['En outre, ','Par ailleurs, ','Dès lors, ','Ainsi, '])
BAD=re.compile(r"^(Le premier|Le deuxième|Le troisième|Le quatrième|La première|La deuxième|La troisième|Question|Non,|Oui,|Cela|D'abord|Ensuite|Enfin|Pourtant|En revanche|De plus|Cependant)")
def addconn(p,k=1):
    # p: paragraph inner text; add connective to k-th eligible sentence
    parts=re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«<])',p)
    done=0
    for i in range(1,len(parts)):
        s=parts[i]
        if s.startswith('<') or BAD.match(s) or C.CONNECT.search(C.texte(CIT.sub('',s))): continue
        w=re.match(r"([A-Za-zÀ-ÿ']+)",s)
        first=w.group(1) if w else ''
        pre=next(PREF)
        if first in LOW or first.rstrip("'")+"'" in LOW: s=s[0].lower()+s[1:]
        parts[i]=pre+s; done+=1
        if done>=k: break
    return ' '.join(parts),done
tot=0
for f in sorted(glob.glob('src/p*.txt')):
    lines=open(f,encoding='utf-8').read().split('\n'); ch=False
    for n,l in enumerate(lines):
        m=re.match(r'^(<div class="p">)(.*)(</div>)$',l)
        if not m: continue
        t=C.texte(CIT.sub('',m.group(2)))
        if len(t.split())>40 and not C.CONNECT.search(t):
            new,d=addconn(m.group(2),1)
            if d: lines[n]=m.group(1)+new+m.group(3); ch=True; tot+=1
    if ch: open(f,'w',encoding='utf-8').write('\n'.join(lines))
print(tot)
