import re,sys,os,html
D=os.path.dirname(os.path.abspath(__file__))
def cites(s):
    s=re.sub(r'([.!?])((?:\[\[[^\]]+\]\])+)',lambda m:m.group(2)+m.group(1),s)
    def f(m):
        return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in m.group(1).split())
    s=re.sub(r'\[\[([^\]]+)\]\]',f,s)
    s=re.sub(r'\{\{(dx6-p\d+-f\d+)\|([^}]+)\}\}',lambda m:f'<button class="w" popovertarget="{m.group(1)}">{m.group(2)}</button>',s)
    return s
def conv(txt):
    out=[];mode=None;win=False
    def close():
        nonlocal mode
        if mode=='ul': out.append('</ul>')
        if mode=='tab': out.append('</table></div>')
        mode=None
    for line in txt.split('\n'):
        line=line.rstrip()
        if not line: continue
        k,_,r=line.partition(' ')
        r=cites(r)
        if k=='L':
            if mode!='ul': close(); out.append('<ul>'); mode='ul'
            out.append(f'<li>{r}</li>'); continue
        if k in('T','R'):
            if mode!='tab': close(); out.append('<div class="t" style="overflow-x:auto"><table>'); mode='tab'
            tag='th' if k=='T' else 'td'
            out.append('<tr>'+''.join(f'<{tag}>{c.strip()}</{tag}>' for c in r.split('|'))+'</tr>'); continue
        if k=='RAW': out.append(r); continue
        close()
        if k=='P': out.append(f'<div class="p">{r}</div>')
        elif k=='Q': out.append(f'<p>{r}</p>')
        elif k=='H': out.append(f'<h4><em>{r}</em></h4>')
        elif k=='WIN': out.append(f'<div id="{r}" popover class="fenetre">')
        elif k=='END': out.append('</div>')
        else: raise SystemExit('ligne inconnue: '+line[:80])
    close()
    return '\n'.join(out)
os.makedirs(D+'/fragments',exist_ok=True)
for n in range(1,15):
    f=f'{D}/src/p{n:02d}.txt'
    if os.path.exists(f):
        open(f'{D}/fragments/p{n:02d}.html','w').write(conv(open(f).read())+'\n')
