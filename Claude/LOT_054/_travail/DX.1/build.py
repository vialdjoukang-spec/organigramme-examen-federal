import re,glob,os,sys
sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C
def words(x): return len(C.texte(x).split())
def split_para(m):
    body=m.group(1)
    sents=re.split(r'(?<=\.)\s+(?=[A-ZÀ-Ý«<])',body)
    out=[];cur=''
    for s in sents:
        cand=(cur+' '+s).strip()
        if not cur or words(cand)<=40 or C.CONNECT.search(C.texte(cand)):
            cur=cand
        else:
            out.append(cur);cur=s
    if cur: out.append(cur)
    return ''.join('<div class="p">%s</div>'%o for o in out)

for f in sorted(glob.glob('src/p*.src')):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'\{([a-z0-9\-,]+)\}',lambda m:''.join('<sup class="r"><a href="#sb-%s">%s</a></sup>'%(i,i) for i in m.group(1).split(',')),t)
    t=re.sub(r'<div class="p">(.*?)</div>',split_para,t,flags=re.S)
    t=t.replace('<div class="t">','<div class="t" style="overflow-x:auto">')
    t='\n'.join(l.rstrip() for l in t.strip().split('\n'))
    open('fragments/'+os.path.basename(f)[:-4]+'.html','w',encoding='utf-8').write(t+'\n')
