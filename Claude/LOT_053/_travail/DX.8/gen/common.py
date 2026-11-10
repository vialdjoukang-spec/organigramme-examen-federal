import re,os
OUT='/home/user/wt/lot-053/Claude/LOT_053/_travail/DX.8/fragments'
def S(m):
    ids=m.group(1).split()
    return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)
def cite(t): return re.sub(r'\{([a-z0-9\- ]+)\}',S,t)
class Pt:
    def __init__(s,n): s.n=n; s.out=[]
    def P(s,text,wins=None):
        t=cite(text.strip())
        pops=[]
        if wins:
            for k,(lab,content) in wins.items():
                fid=f'dx8-p{s.n}-f{k}'
                t=t.replace(f'[[{k}]]',f'<button class="w" popovertarget="{fid}">{lab}</button>')
                pops.append(f'<div id="{fid}" popover class="fenetre">{cite(content.strip())}</div>')
        s.out.append(f'<div class="p">{t}</div>'+''.join(pops))
    def H(s,t): s.out.append(f'<h4><em>{t}</em></h4>')
    def UL(s,items):
        s.out.append('<ul>'+''.join(f'<li>{cite(i.strip())}</li>' for i in items)+'</ul>')
    def T(s,head,rows):
        h=''.join(f'<th>{x}</th>' for x in head)
        r=''.join('<tr>'+''.join(f'<td>{cite(c)}</td>' for c in row)+'</tr>' for row in rows)
        s.out.append(f'<div class="t" style="overflow-x:auto;"><table><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>')
    def save(s):
        os.makedirs(OUT,exist_ok=True)
        open(f'{OUT}/p{s.n:02d}.html','w').write('\n'.join(s.out)+'\n')
