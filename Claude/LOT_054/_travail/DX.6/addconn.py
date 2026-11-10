import re,glob,sys,itertools
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
SAFE={'Le','La','Les','Un','Une','Il','Elle','Cette','Ce','Chez','Dans','Pour','Sous','Après','Cet','Ces','Chaque','Sa','Son','Ses'}
CONN=itertools.cycle(['En outre,','Par ailleurs,','Ainsi,','Dès lors,'])
MINW=int(sys.argv[1]); MODE=sys.argv[2]  # MODE: 'noconn' = only paragraphs without connector; 'all' = add to paragraphs with <2 connector sentences
n=0
for f in sorted(glob.glob('src/p*.html')):
    s=open(f,encoding='utf-8').read()
    def para(m):
        global n
        body=m.group(2)
        parts=re.split(r'(?<=\.)((?:\{\{[^}]+\}\})?)\s+(?=[A-ZÉÀ])',body)
        sents=[parts[0]]+[parts[i+1] for i in range(1,len(parts)-1,2)]
        plains=[C.texte(re.sub(r'\{\{[^}]+\}\}','',x)) for x in sents]
        if sum(len(p.split()) for p in plains)<MINW: return m.group(0)
        have=sum(1 for p in plains if C.CONNECT.search(p))
        if MODE=='noconn' and have>0: return m.group(0)
        if MODE=='all' and have*2>=len(plains): return m.group(0)
        for idx in range(1,len(sents)):
            w=sents[idx].split(' ',1)[0]
            if (not C.CONNECT.search(plains[idx])) and w in SAFE and len(plains[idx].split())>=6:
                c=next(CONN)
                sents[idx]=c+' '+w[0].lower()+w[1:]+sents[idx][len(w):]
                n+=1
                break
        out=[sents[0]]
        for i in range(1,len(sents)):
            out.append(parts[2*i-1]); out.append(' '+sents[i])
        return m.group(1)+''.join(out)+m.group(3)
    s2=re.sub(r'(<div class="p">)(.*?)(</div>)',para,s,flags=re.S)
    open(f,'w',encoding='utf-8').write(s2)
print('inserted',n)
