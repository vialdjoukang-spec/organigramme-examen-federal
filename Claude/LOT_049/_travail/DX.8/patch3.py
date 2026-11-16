import re,glob,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
def clean(s): return re.sub(r'\[@[^\]]*\]|\{\{\d+\|([^}]*)\}\}',r'\1',s)
cnt=0; skipped=[]
for f in sorted(glob.glob('src/p*.txt')):
    out=[]
    for blk in re.split(r'(\n\s*\n)',open(f,encoding='utf-8').read()):
        if not blk.strip() or blk.lstrip().startswith(('|','- ','#')):
            out.append(blk); continue
        lines=blk.split('\n'); new=[]
        for l in lines:
            pre=''
            body=l
            m=re.match(r'^(>>\s*\d+\s*\|\s*)(.*)$',l)
            if m: pre,body=m.group(1),m.group(2)
            t=clean(body)
            if len(t.split())>40 and not C.CONNECT.search(t):
                ss=re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])',body)
                done=False
                for i in range(1,len(ss)):
                    s=ss[i]
                    if re.match(r'^(Réponse|Q\d|Étape|Ce sont)',s): continue
                    w='En outre' if cnt%2==0 else 'Par ailleurs'
                    ss[i]=f'{w}, '+s[0].lower()+s[1:]
                    if re.match(r'^(Le|La|Les|Un|Une)\b',s) is None and not re.match(r"^(Elle|Il|Ils|L'|Dans|Pour|Chez|En|Sur|Lors|Les|Des|Cette|Ce|Au|À)",s):
                        ss[i]=s  # revert (unknown start)
                        continue
                    done=True; cnt+=1; break
                if not done: skipped.append((f,t[:80]))
                body=' '.join(ss)
            new.append(pre+body)
        out.append('\n'.join(new))
    open(f,'w',encoding='utf-8').write(''.join(out))
print(cnt); [print(s) for s in skipped]
