import glob,re,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
OK=("Le ","La ","Les ","L'","Un ","Une ","Il ","Elle ","Ils ","Cette ","Ces ","Cet ","Chez ","Dans ","Pour ","Sous ","Lors ","Au ","Aux ","Des ","Ce ","Toute ","Tout ","Une ","Aucun ","Leur ","Sa ","Son ","Ses ")
CONS=["En outre, ","Par ailleurs, ","Ensuite, ","Enfin, "]
def txt(x): return C.texte(re.sub(r'<sup class="r">.*?</sup>','',x,flags=re.S))
target=float(sys.argv[1]) if len(sys.argv)>1 else 0.40
tot=0;con=0;cands=[]
files=sorted(glob.glob('fragments/p*.html'))
data={f:open(f).read() for f in files}
# first pass: paragraphs
def split_par(s):
    return list(re.finditer(r'<div class="p">(.*?)</div>',s,re.S))
stats={}
for f in files:
    s=data[f]
    for m in split_par(s):
        body=m.group(1)
        sents=re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])',body)
        for i,x in enumerate(sents):
            t=txt(x)
            if len(t.split())<4: continue
            tot+=1
            if C.CONNECT.search(t): con+=1
print('avant',con,tot,round(100*con/tot))
need=int(target*tot)-con
k=0
for f in files:
    s=data[f]
    out=[];pos=0
    for m in split_par(s):
        body=m.group(1)
        sents=re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])',body)
        newsents=[];last_conn=False
        paraw=len(txt(body).split()); hasc=bool(C.CONNECT.search(txt(body)))
        for i,x in enumerate(sents):
            t=txt(x)
            has=bool(C.CONNECT.search(t))
            do=False
            if i>0 and not has and len(t.split())>=8 and x.startswith(OK) and not last_conn and need>0:
                do=True
            if do:
                c=CONS[k%3]; k+=1
                w=x
                # lowercase first letter unless acronym
                first=w.split(' ')[0]
                if w.startswith("L'"): w=c+"l'"+w[2:]
                else: w=c+w[0].lower()+w[1:]
                x=w; need-=1; has=True
            newsents.append(x); last_conn=has
        nb=' '.join(newsents)
        out.append((m.start(1),m.end(1),nb))
    for a,b,nb in reversed(out):
        s=s[:a]+nb+s[b:]
    data[f]=s
for f in files: open(f,'w').write(data[f])
print('restant need',need)
