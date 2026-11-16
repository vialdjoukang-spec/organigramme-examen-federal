import re,glob,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
SAFE=("La ","Le ","Les ","L'","Un ","Une ","Elle ","Elles ","Il ","Ils ","Cette ","Ce ","Ces ","Dans ","Pour ","Sous ","En ","Chez ","Avec ","Selon ","Après ","Avant ","Par ","Sur ","Lorsque ")
SENT=re.compile(r'.+?[.!?](?:\[\[[^\]]*\]\])?(?=\s+[A-ZÀ-Ý«<]|\s*$)',re.S)
def has_conn(s):
    plain=re.sub(r'\[\[.*?\]\]','',s); plain=re.sub(r'<[^>]+>',' ',plain)
    return bool(C.CONNECT.search(plain))
def fix_para(m):
    body=m.group(2)
    if '<table' in body or '<button' in body and False: return m.group(0)
    sents=SENT.findall(body)
    if len(sents)<2 or ''.join(sents).strip()!=body.strip().replace('\n',''): 
        # rebuild safe: only proceed if splitting is exact modulo whitespace
        rest=re.sub(r'\s+','',''.join(sents))
        if rest!=re.sub(r'\s+','',body): return m.group(0)
    seps=re.split(r'(?<=[.!?])(?:\[\[[^\]]*\]\])?',body)  # unused
    # reconstruct with original whitespace
    out=[];pos=0;idxs=[]
    for mm in SENT.finditer(body): idxs.append((mm.start(),mm.end()))
    parts=[]; last=0
    for s,e in idxs:
        parts.append((body[last:s],body[s:e])); last=e
    tail=body[last:]
    n=len(parts); k=0
    new=[]
    for i,(pre,s) in enumerate(parts):
        ws=len(s)-len(s.lstrip()); pre=pre+s[:ws]; s=s[ws:]
        if i in (1,3,5) and not has_conn(s) and s.startswith(SAFE) and i<n:
            first=s.split(' ',1)[0]
            conn=["Par ailleurs, ","En outre, "][k%2]; k+=1
            if s.startswith("L'") : s2=s[0].lower()+s[1:]
            else: s2=s[0].lower()+s[1:]
            s=conn+s2
        new.append(pre+s)
    return m.group(1)+''.join(new)+tail+m.group(3)
for f in sorted(glob.glob('src/p*.txt')):
    if f.endswith(('p13.txt','p10.txt')): continue
    t=open(f).read()
    t2=re.sub(r'(<div class="p">)(.*?)(</div>)',fix_para,t,flags=re.S)
    open(f,'w').write(t2)
