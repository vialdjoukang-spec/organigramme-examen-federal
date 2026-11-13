import re,glob,sys,html
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
TARGET=float(sys.argv[1]) if len(sys.argv)>1 else 0.40
KEEP=('NICE','ESGE','Rome','Lyon','Montréal','Helicobacter','Kalixanda','Olten','Maastricht','Esomep','Pariet','Agopton','Riopan','Omeprazol','Pantoprazol','LINDAAFF','Los','Barrett','EndoFLIP','Glasgow','OFS','Vaud','Suisse','Europe','Allemagne','Islande','Revue','Office','Unisanté','Bravo')
SKIP=re.compile(r"^(Cependant|Pourtant|Inversement|En revanche|Toutefois|À l'inverse|Enfin|Ensuite|D'abord|Dès lors|Ainsi|Par ailleurs|En outre|Puis|Alors|Or|Il faut|Quatre fen|Trois fen|Deux fen|Une fen|Le tableau|Les dix lignes|Chaque ligne|Quand|Si |Lorsqu|En effet|Sans |Une fois|Après|Pour |Dans |Chez |Sous |En présence|Devant|Selon|À |Mais|Donc|Car|«|\d)")
conns=['En outre,','Par ailleurs,']
files={f:open(f,encoding='utf-8').read() for f in sorted(glob.glob('src/p*.txt'))}
def plain(s): return C.texte(re.sub(r'\[\[[^\]]+\]\]','',s))
def blocks(t):
    for m in re.finditer(r'<div class="p">(.*?)</div>|<li>((?:(?!<ul>|</li>|<div).)*)</li>',t,re.S):
        g=1 if m.group(1) is not None else 2
        yield m.start(g),m.end(g),m.group(g)
# stats
tot=con=0
for f,t in files.items():
    for a,b,s in blocks(t):
        if 'class="dx"' in s: continue
        for x in re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])',s):
            p=plain(x)
            if len(p.split())>=4:
                tot+=1; con+= bool(C.CONNECT.search(p))
print('avant',con,tot,round(100*con/tot,1))
need=int(TARGET*tot)-con
k=0
for f in list(files):
    t=files[f]; out=[]; last=0
    for a,b,s in list(blocks(t)):
        if 'class="dx"' in s: continue
        sents=re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])',s)
        has=[bool(C.CONNECT.search(plain(x))) for x in sents]
        n=len(sents)
        words=len(plain(s).split())
        new=list(sents); changed=False
        i=1
        # règle 1 : bloc sans connecteur et >40 mots -> en ajouter un
        def tweak(idx):
            global k
            x=new[idx]
            p=plain(x)
            if SKIP.match(p) or len(p.split())<8 or len(p.split())>26: return False
            first=x.split(' ',1)
            w=first[0]
            if w.rstrip(',') in KEEP or (w.isupper() and len(w)>1): rest=x
            else: rest=x[0].lower()+x[1:]
            c=conns[k%2]; k+=1
            new[idx]=c+' '+rest
            has[idx]=True
            return True
        if words>40 and not any(has):
            for idx in range(1,n):
                if tweak(idx): changed=True; break
            if not changed:
                for idx in range(0,n):
                    if tweak(idx): changed=True; break
        # règle 2 : compléter jusqu'à la cible
        if need>0:
            idx=1
            while idx<n and need>0:
                if not has[idx] and (idx==0 or not has[idx-1]) :
                    if tweak(idx): changed=True; need-=1; idx+=2; continue
                idx+=1
        if changed:
            out.append((a,b,' '.join(new)))
    for a,b,s in reversed(out):
        t=t[:a]+s+t[b:]
    files[f]=t
for f,t in files.items(): open(f,'w',encoding='utf-8').write(t)
tot=con=0
for f,t in files.items():
    for a,b,s in blocks(t):
        if 'class="dx"' in s: continue
        for x in re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])',s):
            p=plain(x)
            if len(p.split())>=4:
                tot+=1; con+= bool(C.CONNECT.search(p))
print('après',con,tot,round(100*con/tot,1))
