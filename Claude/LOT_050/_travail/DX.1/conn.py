import re,sys,glob
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as c
CONN=["En outre","Par ailleurs","Ensuite"]
NOPROPER={'Kennedy','Gaita','Copenhague','Stockholm','Bâle','Holter','Meto','Propranolol','Concor','Lin','Lee','Ataklte','Verdile','Hiss','Kostis','Fisher','ARIC','MRFIT','MonDAFIS','ECTOPIA'}
rot=int(sys.argv[1]) if len(sys.argv)>1 else 0
target=float(sys.argv[2]) if len(sys.argv)>2 else 0.5
def txt(x): return c.texte(re.sub(r'\{[^{}]*\}','',x))
tot=0
for f in sorted(glob.glob('src/p*.txt')):
    s=open(f,encoding='utf-8').read()
    def fix(m):
        global tot,rot
        body=m.group(2)
        # sentences
        parts=re.split(r'(?<=[.!?])(?=\s+[A-ZÀ-Ý«])',body)
        # reattach leading spaces
        out=[]; 
        n=len(parts)
        has=[bool(c.CONNECT.search(txt(p))) for p in parts]
        words=len(txt(body).split())
        need=(words>40 and not any(has)) 
        k=0
        for i,p in enumerate(parts):
            if i>0 and not has[i] and (need or (i%2==1 and sum(has)/n<target)):
                lead=re.match(r'\s*',p).group(0); core=p[len(lead):]
                first=re.match(r"[\wÀ-ÿ'’]+",core)
                fw=first.group(0) if first else ''
                if fw and fw not in NOPROPER and not fw.isupper() and not re.match(r'^\d',fw) and not core.startswith(('<','[','Q','Nœud')) and len(core.split())>5:
                    cn=CONN[rot%len(CONN)]; rot+=1
                    core=cn+", "+core[0].lower()+core[1:]
                    p=lead+core; has[i]=True; need=False; tot+=1
            out.append(p)
        return m.group(1)+''.join(out)+m.group(3)
    s2=re.sub(r'(<div class="p">)(.*?)(</div>)',fix,s,flags=re.S)
    open(f,'w',encoding='utf-8').write(s2)
print('inserted',tot)
