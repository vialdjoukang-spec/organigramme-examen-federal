#!/usr/bin/env python3
import re,sys,html,glob,os
AL={'U':'w83e157-','H':'w39de5c-','R':'w7a9169-','A':'wf82810-','D':'w2525fb-','T':'w3e0084-','Z':'wbf7aee-','N':'w5f0cb9-','C':'wc8fed2-','AX':'aips-69243-','BO':'aips-52433-','DY':'aips-55057-','OX':'w2413c5-','LA':'w50e187-','W':'w8deb59-'}
def cit(m):
    ids=[]
    for x in m.group(1).split(','):
        x=x.strip(); k=re.match(r'[A-Z]+',x).group(0); ids.append(AL[k]+x[len(k):])
    return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)
def inl(s):
    s=re.sub(r'\[\[([^\]]+)\]\]',cit,s)
    s=re.sub(r'\{\{([\w-]+)\|([^}]+)\}\}',lambda m:f'<button class="w" popovertarget="{m.group(1)}">{m.group(2)}</button>',s)
    return s
def conv(path):
    out=[];ul=[];tb=[]
    def flush():
        nonlocal ul,tb
        if ul: out.append('<ul>'+''.join(f'<li>{inl(x)}</li>' for x in ul)+'</ul>'); ul=[]
        if tb:
            r=''.join('<tr>'+''.join((f'<th>{c}</th>' if i==0 else f'<td>{c}</td>') for c in row)+'</tr>' for i,row in enumerate(tb))
            out.append(f'<div class="t" style="overflow-x:auto"><table>{r}</table></div>'); tb=[]
    for l in open(path,encoding='utf-8').read().split('\n'):
        l=l.rstrip()
        if not l: continue
        k,_,v=l.partition(': ')
        if k!='L': 
            if ul: flush()
        if k!='T':
            if tb: flush()
        if k=='P': out.append(f'<div class="p">{inl(v)}</div>')
        elif k=='RAW': out.append(inl(v))
        elif k=='H': out.append(f'<h4><em>{v}</em></h4>')
        elif k=='L': ul.append(v)
        elif k=='T': tb.append([inl(c.strip()) for c in v.split('|')])
        elif k=='F':
            i,_,t=v.partition(' | ')
            out.append(f'<div id="{i}" popover class="fenetre"><div class="p">{inl(t)}</div></div>')
        else: raise SystemExit('ligne inconnue: '+l[:50])
    flush()
    return '\n'.join(out)+'\n'
for f in sorted(glob.glob('src/p*.txt')):
    open('fragments/'+os.path.basename(f).replace('.txt','.html'),'w',encoding='utf-8').write(conv(f))
