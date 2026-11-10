import re,os,html,sys
D=os.path.dirname(os.path.abspath(__file__))
PRE={'A':'w9d5693','P':'w3ea599','K':'wcd89b3','G':'w0fafdd','T':'wa2f885','N':'w04607f','B':'w48d02f','E':'w0e502d','R':'w89197e'}
def cit(m):
    k,n=m.group(1),m.group(2)
    i=f'aips-{n}' if k=='S' else f'{PRE[k]}-{n}'
    return f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
def inline(s):
    s=re.sub(r'\[\[([A-Z])(\d+(?:-\d+)?)\]\]',cit,s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
    s=re.sub(r'__(.+?)__',r'<em>\1</em>',s)
    return s
def build(n):
    src=open(f'{D}/src/p{n:02d}.txt',encoding='utf8').read().split('\n')
    out=[];k=0;mode=None;wins=[]
    def close():
        nonlocal mode
        if mode=='ul': out.append('</ul>')
        if mode=='tb': out.append('</table></div>')
        mode=None
    for ln in src:
        if not ln.strip() or ln.startswith('#'): continue
        tag,_,body=ln.partition(' ')
        if tag=='L':
            if mode!='ul': close(); out.append('<ul>'); mode='ul'
            out.append(f'<li>{inline(body)}</li>'); continue
        if tag in('TH','TR'):
            if mode!='tb': close(); out.append('<div class="t" style="overflow-x:auto"><table>'); mode='tb'
            cells=[c.strip() for c in body.split('|')]
            c='th' if tag=='TH' else 'td'
            out.append('<tr>'+''.join(f'<{c}>{inline(x)}</{c}>' for x in cells)+'</tr>'); continue
        close()
        if tag=='H': out.append(f'<h4><em>{inline(body)}</em></h4>'); continue
        if tag=='P':
            wins=[]
            def w(m):
                nonlocal k
                k+=1; wid=f'dx4-p{n}-f{k}'
                wins.append(f'<div id="{wid}" popover class="fenetre">'+''.join(f'<div class="p">{inline(x.strip())}</div>' for x in m.group(2).split('¶'))+'</div>')
                return f'<button class="w" popovertarget="{wid}">{m.group(1)}</button>'
            b=re.sub(r'\{\{(.+?)\|(.+?)\}\}',w,body)
            out.append(f'<div class="p">{inline(b)}</div>'); out+=wins; continue
        raise SystemExit(f'ligne inconnue p{n}: {ln[:60]}')
    close()
    open(f'{D}/fragments/p{n:02d}.html','w',encoding='utf8').write('\n'.join(out)+'\n')
for n in range(1,15):
    if os.path.exists(f'{D}/src/p{n:02d}.txt'): build(n)
