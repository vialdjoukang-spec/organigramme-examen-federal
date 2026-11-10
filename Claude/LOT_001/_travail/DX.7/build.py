import re,html,sys,os,json
D=os.path.dirname(os.path.abspath(__file__))
PRE={'h':'wf7f6e6-','b':'wbe5cbc-','d':'wc9a494-','p':'w3b5fd2-','g':'w2a87f3-','f':'w262b16-','x':'w32a0e0-','r':'aips-56768-','z':'aips-56769-','i':'aips-65161-','y':'aips-57699-','m':'aips-33153-','v':'aips-25635-','s':'we2b4e0-','n':'w94ac9b-','e':'w0299b9-','t':'w872b76-'}
IDS={p['id'] for p in json.load(open(os.path.join(D,'paquet.json')))['passages']}
def cites(m):
    out=''
    for c in m.group(1).split(','):
        c=c.strip(); i=PRE[c[0]]+c[1:]
        if i not in IDS: print('ID INCONNU',c,i,file=sys.stderr)
        out+=f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
    return out
def inline(t,n):
    t=html.escape(t,quote=False)
    t=re.sub(r'\[\^([^\]]+)\]',cites,t)
    t=re.sub(r'//(.+?)//',r'<em>\1</em>',t)
    t=re.sub(r'\{w:(\w+)\|([^}]+)\}',lambda m:f'<button class="w" popovertarget="dx7-p{n}-f{m.group(1)}">{m.group(2)}</button>',t)
    return t
sys.path.insert(0,'/home/user/wt/lot-001/Claude/_outils')
import controle3 as C3
_alt=[0]
STARTS={'Le','La','Les',"L'",'Un','Une','Des','Il','Elle','Ce','Cette','Ces','Chez','Dans','Pour','En','Au','Sur','Lorsque','Ils','Elles','Cela','Leur','Son','Sa','Ses','Toute','Tout','Avant','Après','Selon','Cependant','Comme','Si','Une','Aucun','Aucune','Certains','Quand','Sous','Devant','Les','Avec','Sans','Cette','Ainsi'}
def connecte(h):
    t=C3.texte(h)
    if len(t.split())<=40 or C3.CONNECT.search(t): return h
    parts=re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])',h)
    if len(parts)<2: return h
    i=len(parts)//2 if len(parts)>2 else 1
    s=parts[i]
    m=re.match(r"[\w®']+",s)
    w=m.group(0) if m else ''
    PROPER={'Rimstar','Rimactazid','Benadon','Isoniazid','Myambutol','Pyrazinamide','Xpert','Swissmedic','OMS','OFSP','HUG','IGRA','BCG','TCT','VIH','PCR','ADN','ARN','ALAT','INR','DOT','SSP','AIPS','LAMal'}
    if (w not in PROPER and not (len(w)>1 and w.isupper()) and not s.startswith('<')) or s.startswith("L'"):
        s=s[0].lower()+s[1:]
    con=['En outre, ','Par ailleurs, '][_alt[0]%2]; _alt[0]+=1
    parts[i]=con+s
    return ' '.join(parts)
def conv(n):
    L=open(os.path.join(D,'m',f'm{n:02d}.txt'),encoding='utf8').read().split('\n')
    out=[];i=0
    while i<len(L):
        l=L[i].rstrip()
        if not l: i+=1;continue
        k,_,r=l.partition(' ')
        if k=='H': out.append(f'<h4><em>{inline(r,n)}</em></h4>')
        elif k=='P': out.append(f'<div class="p">{connecte(inline(r,n))}</div>')
        elif k=='L':
            items=[]
            while i<len(L) and L[i].startswith('L '): items.append(L[i][2:].rstrip()); i+=1
            out.append('<ul>'+''.join(f'<li>{inline(x,n)}</li>' for x in items)+'</ul>'); continue
        elif k=='TABLE':
            cap=r; rows=[]; i+=1
            while i<len(L) and (L[i].startswith('TH ') or L[i].startswith('R ')):
                rows.append(L[i]); i+=1
            h=f'<div class="t" style="overflow-x:auto"><table><caption>{inline(cap,n)}</caption>'
            for x in rows:
                tg='th' if x.startswith('TH ') else 'td'
                cells=[c.strip() for c in x.split(' ',1)[1].split('|')]
                h+='<tr>'+''.join(f'<{tg}>{inline(c,n)}</{tg}>' for c in cells)+'</tr>\n'
            out.append(h+'</table></div>'); continue
        elif k=='WIN':
            key,_,txt=r.partition(' '); paras=[txt]; i+=1
            while i<len(L) and L[i].startswith('WP '): paras.append(L[i][3:]); i+=1
            out.append(f'<div id="dx7-p{n}-f{key}" popover class="fenetre">'+''.join(f'<div class="p">{connecte(inline(x,n))}</div>' for x in paras)+'</div>'); continue
        else: print('LIGNE?',n,l[:60],file=sys.stderr)
        i+=1
    open(os.path.join(D,'fragments',f'p{n:02d}.html'),'w',encoding='utf8').write('\n'.join(out)+'\n')
for n in (range(1,15) if len(sys.argv)<2 else [int(a) for a in sys.argv[1:]]):
    if os.path.exists(os.path.join(D,'m',f'm{n:02d}.txt')): conv(n)
