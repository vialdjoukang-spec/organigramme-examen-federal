import re,os,html,sys
D=os.path.dirname(os.path.abspath(__file__))
PRE='dx8'
def cites(s):
    return re.sub(r'\[@([\w.\-,:]+)\]',lambda m:''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in m.group(1).split(',')),s)
def inline(s,n):
    s=cites(s)
    s=re.sub(r'\{\{(\d+)\|([^}]+)\}\}',lambda m:f'<button class="w" popovertarget="{PRE}-p{n}-f{m.group(1)}">{m.group(2)}</button>',s)
    return s
def conv(n):
    t=open(f'{D}/src/p{n:02d}.txt',encoding='utf-8').read()
    out=[]
    for blk in re.split(r'\n\s*\n',t.strip()):
        L=[l for l in blk.split('\n') if l.strip()]
        if not L: continue
        if L[0].startswith('## '):
            out.append(f'<h5>{inline(L[0][3:],n)}</h5>'); L=L[1:]
            if not L: continue
        elif L[0].startswith('# '):
            out.append(f'<h4><em>{inline(L[0][2:],n)}</em></h4>'); L=L[1:]
            if not L: continue
        if L[0].startswith('|'):
            rows=[[c.strip() for c in l.strip().strip('|').split('|')] for l in L]
            h='<div class="t" style="overflow-x:auto"><table>'
            h+='<tr>'+''.join(f'<th>{inline(c,n)}</th>' for c in rows[0])+'</tr>\n'
            for r in rows[1:]: h+='<tr>'+''.join(f'<td>{inline(c,n)}</td>' for c in r)+'</tr>\n'
            out.append(h+'</table></div>'); continue
        if L[0].startswith('- '):
            out.append('<ul>'+''.join(f'<li>{inline(l[2:],n)}</li>' for l in L)+'</ul>'); continue
        if L[0].startswith('>>'):
            for l in L:
                k,tx=l[2:].split('|',1)
                out.append(f'<div id="{PRE}-p{n}-f{k.strip()}" popover class="fenetre"><div class="p">{inline(tx.strip(),n)}</div></div>')
            continue
        # paragraphe ; lignes '>>' finales = fenêtres
        par=[l for l in L if not l.startswith('>>')]; win=[l for l in L if l.startswith('>>')]
        out.append(f'<div class="p">{inline(" ".join(par),n)}</div>')
        for l in win:
            k,tx=l[2:].split('|',1)
            out.append(f'<div id="{PRE}-p{n}-f{k.strip()}" popover class="fenetre"><div class="p">{inline(tx.strip(),n)}</div></div>')
    open(f'{D}/fragments/p{n:02d}.html','w',encoding='utf-8').write('\n'.join(out)+'\n')
for n in range(1,15):
    if os.path.exists(f'{D}/src/p{n:02d}.txt'): conv(n)
