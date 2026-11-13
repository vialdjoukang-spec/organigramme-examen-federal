import re,os
D='/home/user/wt/lot-052/Claude/LOT_052/_travail/DX.2/fragments/'
def cit(s):
    s=re.sub(r'([.!?])(\[\[[\w.\-]+\]\])', r'\2\1', s)
    return re.sub(r'\[\[([\w.\-]+)\]\]', r'<sup class="r"><a href="#sb-\1">\1</a></sup>', s)
class Cnt: cnt=0
CON=re.compile(r"\b(car|donc|or|ainsi|puis|alors|parce que|puisque|lorsque|quand|si|tandis que|alors que|afin de|afin que|pour que|de sorte que|c'est pourquoi|en effet|cependant|toutefois|néanmoins|par conséquent|dès lors|ensuite|enfin|d'abord|en revanche|ce qui|grâce à|à cause de|en raison de|si bien que|de ce fait|par ailleurs|en outre|autrement dit|c'est-à-dire|d'où|puisqu'|lorsqu'|qu'il)\b",re.I)
SAFE=('Le ','La ','Les ','Un ','Une ','Cette ','Ce ','Ces ','Il ','Elle ',"L'")
def liaison(t,pt):
    # insère un connecteur additif dans une phrase sur deux sans connecteur (hors première phrase)
    parts=re.split(r'(?<=[.!?\]])\s+(?=[A-ZÀ-Ý«])',t)
    if len(parts)<2: return t
    out=[parts[0]]; prev=bool(CON.search(parts[0])); k=0
    for i,x in enumerate(parts[1:],1):
        has=bool(CON.search(x))
        if not has and not prev and x.startswith(SAFE) and not re.match(r'(Le|La|Les|Un|Une) (WSES|NICE|ESGE|HUG|TG|CRP|ASA|Murphy)',x):
            mot=["En outre, ","Par ailleurs, "][Cnt.cnt%2]; Cnt.cnt+=1
            x=mot+x[0].lower()+x[1:]; has=True
        out.append(x); prev=has
    return ' '.join(out)
class Pt:
    def __init__(s,n): s.n=n; s.o=[]; s.k=0
    def h(s,t): s.o.append(f'<h4><em>{t}</em></h4>')
    def p(s,t,*wins):
        t=liaison(t,s)
        ws=[]
        for lab,body in wins:
            s.k+=1; i=f'dx2-p{s.n}-f{s.k}'
            t=t.replace('@@',f'<button class="w" popovertarget="{i}">{lab}</button>',1)
            ws.append(f'<div id="{i}" popover class="fenetre">{cit(body)}</div>')
        s.o.append(f'<div class="p">{cit(t)}</div>')
        s.o+=ws
    def ul(s,items): s.o.append('<ul>'+''.join(f'<li>{cit(i)}</li>' for i in items)+'</ul>')
    def t(s,head,rows):
        r='<div class="t" style="overflow-x:auto"><table><thead><tr>'+''.join(f'<th>{h}</th>' for h in head)+'</tr></thead><tbody>'
        r+=''.join('<tr>'+''.join(f'<td>{cit(c)}</td>' for c in row)+'</tr>' for row in rows)+'</tbody></table></div>'
        s.o.append(r)
    def save(s): open(D+f'p{s.n:02d}.html','w',encoding='utf-8').write('\n'.join(s.o)+'\n')
def W(*paras): return ''.join(f'<div class="p">{x}</div>' if not x.startswith('<') else x for x in paras)
