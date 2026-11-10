import re,os,sys,glob
D=os.path.dirname(os.path.abspath(__file__))
def cit(m):
    return ''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(','))
def expand(txt,n):
    txt=re.sub(r'\{\{([^}]+)\}\}',cit,txt)
    txt=re.sub(r'⟦(\w+)\|([^⟧]+)⟧',lambda m:f'<button class="w" popovertarget="pa-p{n}-f{m.group(1)}">{m.group(2)}</button>',txt)
    txt=txt.replace('<div class="t">','<div class="t" style="overflow-x:auto">')
    return txt

sys.path.insert(0,'/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as C3
def w2(x): return len(re.sub(r'\{\{[^}]*\}\}','',re.sub(r'⟦\w+\|([^⟧]*)⟧',r'\1',x)).split())
CIT_RE=re.compile(r'\{\{[^}]*\}\}')
DELIMS=[(' ; ','. ',0),(', alors que ','. En revanche, ',0),(', tandis que ','. En revanche, ',0),(', mais ','. Cependant, ',0),(', car ','. En effet, ',0),(', ce qui ','. Cela ',0),(' : ','. ',0),(', puis ','. Ensuite, ',0),(', et ','. ',1),(', où ','. ',9)]
def cap(x): return x[:1].upper()+x[1:]
def split1(sent):
    if w2(sent)<=29: return [sent]
    body=sent.rstrip()
    end='.' if body.endswith('.') else ''
    if end: body=body[:-1]
    best=None
    for d,rep,chk in DELIMS:
        if chk==9: continue
        pos=[m.start() for m in re.finditer(re.escape(d),body)]
        for p in pos:
            a,b=body[:p],body[p+len(d):]
            if '{{' in a and a.count('{{')!=a.count('}}'): continue
            if w2(a)<8 or w2(b)<8: continue
            if chk and not C3.est_verbale(CIT_RE.sub('',b)): continue
            score=abs(w2(a)-w2(b))
            if best is None or score<best[0]: best=(score,a,b,rep)
        if best: break
    if not best: return [sent]
    _,a,b,rep=best
    ca,cb=CIT_RE.findall(a),CIT_RE.findall(b)
    if not ca and cb and re.search(r'\d',a): a=a+''.join(cb[-1:])
    if not cb and ca and re.search(r'\d',b): b=b+''.join(ca[-1:])
    lead=rep.split('. ')[1] if rep.count('. ')>0 and rep.split('. ')[1] else ''
    first=a+'.'
    second=(lead+b if lead else cap(b))+end
    if lead=='' : second=cap(b)+end
    return split1(first)+split1(second)
def splitlong(t):
    sents=re.split(r'(?<=\.)\s+(?=[A-ZÀ-Ý«(])',t)
    out=[]
    for x in sents: out+=split1(x)
    return ' '.join(out)
def wc(x): return len(re.sub(r'<[^>]+>',' ',x).split())
def chunks(t):
    sents=re.split(r'(?<=\.)\s+(?=[A-ZÀ-Ý«(])',t)
    groups=[];cur=''
    for x in sents:
        if cur and wc(cur)+wc(x)>38:
            groups.append(cur);cur=x
        else: cur=(cur+' '+x).strip()
    if cur: groups.append(cur)
    return ['<div class="p">'+g+'</div>' for g in groups]
def build(n):
    src=open(f'{D}/src/p{n:02d}.txt',encoding='utf-8').read().split('\n')
    out=[];infen=False
    for l in src:
        l=l.rstrip()
        if not l: continue
        if l.startswith('§F '):
            out.append(f'<div id="pa-p{n}-f{l[3:].strip()}" popover class="fenetre">');infen=True;continue
        if l.startswith('§E'):
            out.append('</div>');infen=False;continue
        if l.startswith('P: '): out.extend(chunks(expand(splitlong(l[3:]),n)))
        elif l.startswith('H: '): out.append('<h4><em>'+expand(l[3:],n)+'</em></h4>')
        else: out.append(expand(l,n))
    open(f'{D}/fragments/p{n:02d}.html','w',encoding='utf-8').write('\n'.join(out)+'\n')
for n in range(1,15):
    if os.path.exists(f'{D}/src/p{n:02d}.txt'): build(n)
