import re,glob,sys,html
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
exec(open('conv.py').read().split('for f in sorted')[0])
CONN=["En outre, ","Par ailleurs, "]
PROPER=set("GINA HUG SABA ERS ATS Ventolin Atrovent Symbicort Pulmicort Prednisone Prednisolone Cochrane Swissmedic AIPS FeNO VEMS CVF DEP SAPALDIA Gayen Phadiatop ANCA PRAM BPCO LAMA Ligue Solu-Medrol Adrenalin".split())
k=0; tot=0
for f in sorted(glob.glob('src/p*.txt')):
    if f.endswith(('p13.txt',)): continue
    s=open(f).read()
    def fix(m):
        global k,tot
        inner=m.group(1)
        t=C.texte(conv('<P>'+inner+'</P>'))
        if len(t.split())<=40 or C.CONNECT.search(t): return m.group(0)
        sents=re.split(r'(?<=\.)\s+(?=[A-ZÀ-Ý«])',inner)
        if len(sents)<2: return m.group(0)
        # choisir une phrase d'indice >=1 sans bouton ni 'Question'
        for idx in [1,2,3,0]:
            if idx>=len(sents): continue
            st=sents[idx]
            if st.startswith('<B') or 'question' in st[:25].lower(): continue
            w=re.match(r"[\wÀ-ÿ'’®-]+",st)
            if not w: continue
            first=w.group(0)
            low = not (first in PROPER or (first.isupper() and len(first)>1) or '®' in first)
            conn=CONN[k%2]; k+=1; tot+=1
            sents[idx]=conn+(st[0].lower()+st[1:] if low else st)
            return '<P>'+' '.join(sents)+'</P>'
        return m.group(0)
    s2=re.sub(r'<P>(.*?)</P>',fix,s,flags=re.S)
    if s2!=s: open(f,'w').write(s2)
print('insertions',tot)
