import re,glob,os,html
D=os.path.dirname(os.path.abspath(__file__))
def cite(s):
    s=re.sub(r'([.?!])((?:\{[\w.\-]+\})+)',r'\2\1',s)
    return re.sub(r'\{([\w.\-]+)\}',lambda m:f'<sup class="r"><a href="#sb-{m.group(1)}">{m.group(1)}</a></sup>',s)
def inline(s):
    s=cite(s)
    s=re.sub(r'\[\[b:([\w\-]+)\|([^\]]+)\]\]',lambda m:f'<button class="w" popovertarget="{m.group(1)}">{m.group(2)}</button>',s)
    return s
def render(lines):
    out=[];ul=[];tb=[]
    def fl():
        nonlocal ul,tb
        if ul: out.append('<ul>'+''.join(f'<li>{inline(x)}</li>' for x in ul)+'</ul>'); ul=[]
        if tb:
            h=tb[0];rows=tb[1:]
            t='<div class="t" style="overflow-x:auto"><table><thead><tr>'+''.join(f'<th>{inline(c.strip())}</th>' for c in h)+'</tr></thead><tbody>'
            for r in rows: t+='<tr>'+''.join(f'<td>{inline(c.strip())}</td>' for c in r)+'</tr>'
            out.append(t+'</tbody></table></div>'); tb=[]
    for l in lines:
        l=l.rstrip('\n')
        if not l.strip(): continue
        if l.startswith('L '): 
            if tb: fl()
            ul.append(l[2:]); continue
        if l.startswith('T '):
            if ul: fl()
            tb.append(l[2:].split(' | ')); continue
        fl()
        if l.startswith('P '): out.append(f'<div class="p">{inline(l[2:])}</div>')
        elif l.startswith('H '): out.append(f'<h4><em>{l[2:]}</em></h4>')
        elif l.startswith('R '): out.append(inline(l[2:]))
        elif l.startswith('F '):
            out.append(f'<div id="{l[2:].strip()}" popover class="fenetre">')
        elif l.startswith('/F'): out.append('</div>')
        else: raise SystemExit('ligne inconnue: '+l[:60])
    fl(); return '\n'.join(out)+'\n'
for f in sorted(glob.glob(D+'/src/p*.txt')):
    n=os.path.basename(f)[1:-4]
    open(f'{D}/fragments/p{n}.html','w').write(render(open(f).read().split('\n')))
print('ok')
