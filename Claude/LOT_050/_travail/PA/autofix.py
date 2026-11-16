import re,glob,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
MAC=re.compile(r'\s*\{c:[^}]+\}')
def plain(s): return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',MAC.sub('',re.sub(r'\{w:[^|}]+\|([^}]+)\}',r'\1',s)))).strip()
SPL=[(', et ','En outre, '),(' : ','CAP'),(', avec ','Il y a aussi '),(', en ','Cela se fait en '),(', ou ','Ou bien '),(', car ','En effet, '),(', puisque ','En effet, '),(', alors que ','En revanche, '),(', tandis que ','En revanche, '),(', de sorte que ','Ainsi, '),(', ce qui ','Cela '),(', mais ','Cependant, '),(', parce que ','En effet, '),(' ; ','Ensuite, ')]
def split_sentence(sent):
    # sent: text incl. trailing macro and period
    m=re.search(r'((?:\s*\{c:[^}]+\})?)([.!?])\s*$',sent)
    if not m: return None
    cite=m.group(1); body=sent[:m.start()]; end=m.group(2)
    n=len(plain(body).split())
    if n<=30: return None
    best=None
    for pat,rep in SPL:
        for mm in re.finditer(re.escape(pat),body):
            L=body[:mm.start()]; R=body[mm.end():]
            nl=len(plain(L).split()); nr=len(plain(R).split())
            if nl<8 or nr<6 or nl>31 or nr>31: continue
            if not C.est_verbale(plain(R)) or not C.est_verbale(plain(L)): continue
            if rep in ('Il y a aussi ','Cela se fait en ','Ou bien '): continue
            # right part must contain a verb-ish
            score=abs(nl-nr)
            if best is None or score<best[0]: best=(score,L,R,rep)
    if not best: return None
    _,L,R,rep=best
    # avoid cite macro inside L (mid-sentence cites): fine
    # if L already ends w cite macro, don't duplicate
    Lc=L.rstrip()
    if not re.search(r'\{c:[^}]+\}$',Lc): Lc=Lc+cite
    if rep=='CAP': R2=R[0].upper()+R[1:]
    elif rep=='Cela ': R2='Cela '+R
    else: R2=rep+R
    if rep!='Cela ' and R2[len(rep):len(rep)+1].isupper() is False: pass
    return Lc+'. '+R2+cite+end
PROP=('Zurich','Tours','Toulouse','Weber','Krenosin','Xarelto','Lixiana','Apixaban','Dabigatran','Metoprolol','Bisoprolol','Amiodarone','Holter','Valsalva','Danemark','Suisse','Michigan','Barcelone','Amsterdam','Genève','Liège','Kent','Wolff','Virchow','Europe','REVERT','HASIA','HUG','ECG','TSH','INR','CHA2DS2','HAS','QRS','QT','ST','IRM','ILR','EHRA','ESC','RUP','ELR','AF','Brugada','Mepha','Stada','Sandoz','Devatis','EAST')
def fix_text(t):
    # split each line (paragraph/li) sentences
    out=[]
    for line in t.split('\n'):
        sents=re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])',line)
        # re-merge cite macro cases: sentences end like "...{c:x}." -> fine as split after period
        new=[]
        for s in sents:
            r=split_sentence(s)
            new.append(r if r else s)
        line='  '.join(new) if False else ' '.join(new)
        # connector insertion for paragraphs w/o connector
        pl=plain(line)
        if line.startswith('<div class="p">') and len(pl.split())>40 and not C.CONNECT.search(pl):
            sents=re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])',line)
            for k,conn in ((1,'En outre, '),(2,'Enfin, '),(3,'Par ailleurs, ')):
                if k<len(sents):
                    s=sents[k]
                    w=re.match(r'([A-ZÀ-Ý][\wÀ-ÿ\'’-]*)',s)
                    if w and not w.group(1).startswith(PROP) and w.group(1)[1:].islower() and not s.startswith('<'):
                        sents[k]=conn+s[0].lower()+s[1:]
                        break
            line=' '.join(sents)
        out.append(line)
    return '\n'.join(out)
for f in sorted(glob.glob('src/p*.src')):
    t=open(f,encoding='utf-8').read()
    open(f,'w',encoding='utf-8').write(fix_text(t))
