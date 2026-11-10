import re,html,sys,glob,os
D=os.path.dirname(os.path.abspath(__file__))
def cit(s):
    return re.sub(r'\s*\{([\w.,\-]+)\}',lambda m:''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in m.group(1).split(',')),s)
def txt(s,n,k):
    s=html.escape(s,quote=False)
    s=re.sub(r'\[\[([\w]+)\|(.*?)\]\]',lambda m:f'<button class="w" popovertarget="pa-p{n}-{m.group(1)}">{m.group(2)}</button>',s)
    s=re.sub(r'\*\*(.*?)\*\*',r'<strong>\1</strong>',s)
    s=re.sub(r'%%(.*?)%%',r'<span class="freq">\1</span>',s)
    s=re.sub(r'@@(E\d)@@',r'<span class="rang">🚩 \1</span>',s)
    return cit(s)
def build(n):
    out=[];pend=[];pops={}
    lines=[l.rstrip('\n') for l in open(f'{D}/src/p{n:02d}.txt',encoding='utf-8') if l.strip() and not l.startswith('#')]
    def flush():
        for k,v in pend:
            paras=''.join(f'<div class="p">{txt(x.strip(),n,k)}</div>' for x in v.split('¶'))
            out.append(f'<div id="pa-p{n}-{k}" popover class="fenetre">{paras}</div>')
        pend.clear()
    for l in lines:
        t,_,r=l.partition(' ')
        if t=='P': flush(); out.append(f'<div class="p">{txt(r,n,"")}</div>')
        elif t=='F':
            k,_,v=r.partition(' '); pend.append((k,v))
        elif t=='H': flush(); out.append(f'<h4><em>{html.escape(r,quote=False)}</em></h4>')
        elif t=='L': flush(); out.append('<ul>'+''.join(f'<li>{txt(x.strip(),n,"")}</li>' for x in r.split(';;'))+'</ul>')
        elif t=='T':
            flush(); rows=[[c.strip() for c in x.split(' | ')] for x in r.split(';;')]
            h='<tr>'+''.join(f'<th>{txt(c,n,"")}</th>' for c in rows[0])+'</tr>'
            b=''.join('<tr>'+''.join(f'<td>{txt(c,n,"")}</td>' for c in x)+'</tr>' for x in rows[1:])
            out.append(f'<div class="t"><table>{h}{b}</table></div>')
        elif t=='R': flush(); out.append(r)
        else: raise SystemExit(f'ligne inconnue p{n}: {l[:60]}')
    flush()
    open(f'{D}/fragments/p{n:02d}.html','w',encoding='utf-8').write('\n'.join(out)+'\n')
for f in sorted(glob.glob(f'{D}/src/p*.txt')): build(int(os.path.basename(f)[1:3]))
