import re,sys,os,html
D=os.path.dirname(os.path.abspath(__file__))
def inline(s,keys,n):
    s=re.sub(r'\{([\w.\-]+)\}',lambda m:f'<sup class="r"><a href="#sb-{m.group(1)}">{m.group(1)}</a></sup>',s)
    s=re.sub(r'\[\[(.+?)::(\w+)\]\]',lambda m:f'<button class="w" popovertarget="dx8-p{n}-f{keys[m.group(2)]}">{m.group(1)}</button>',s)
    return s
def blocks(lines,keys,n):
    out=[];i=0;ul=[]
    def flush():
        nonlocal ul
        if ul: out.append('<ul>'+''.join(f'<li>{x}</li>' for x in ul)+'</ul>'); ul=[]
    while i<len(lines):
        l=lines[i].rstrip()
        if not l.strip(): flush(); i+=1; continue
        if l.startswith('- '): ul.append(inline(l[2:],keys,n)); i+=1; continue
        flush()
        if l.startswith('## '): out.append(f'<h4><em>{inline(l[3:],keys,n)}</em></h4>')
        elif l=='TABLE':
            rows=[];i+=1
            while lines[i].strip()!='ENDTABLE': rows.append(lines[i].rstrip()); i+=1
            t='<div class="t"><table>'
            for k,r in enumerate(rows):
                c=[inline(x.strip(),keys,n) for x in r.split('|')]
                tag='th' if k==0 else 'td'
                t+='<tr>'+''.join(f'<{tag}>{x}</{tag}>' for x in c)+'</tr>'
            out.append(t+'</table></div>')
        elif l.startswith('<'): out.append(inline(l,keys,n))
        else: out.append(f'<div class="p">{inline(l,keys,n)}</div>')
        i+=1
    flush(); return out
def conv(n):
    src=open(f'{D}/src/p{n:02d}.txt',encoding='utf-8').read().split('\n')
    keys={};k=0
    for l in src:
        m=re.match(r'@@(\w+)\s*$',l)
        if m: k+=1; keys[m.group(1)]=k
    out=[];main=[];i=0
    while i<len(src):
        m=re.match(r'@@(\w+)\s*$',src[i])
        if m:
            body=[];i+=1
            while src[i].strip()!='@@': body.append(src[i]); i+=1
            main_html=blocks(main,keys,n); main=[]
            out+=main_html
            out.append(f'<div id="dx8-p{n}-f{keys[m.group(1)]}" popover class="fenetre">'+''.join(blocks(body,keys,n))+'</div>')
        else: main.append(src[i])
        i+=1
    out+=blocks(main,keys,n)
    open(f'{D}/fragments/p{n:02d}.html','w',encoding='utf-8').write('\n'.join(out)+'\n')
for n in (range(1,15) if len(sys.argv)<2 else [int(x) for x in sys.argv[1:]]):
    if os.path.exists(f'{D}/src/p{n:02d}.txt'): conv(n)
