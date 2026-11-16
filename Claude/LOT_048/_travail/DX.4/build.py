#!/usr/bin/env python3
import re,os,glob
D=os.path.dirname(os.path.abspath(__file__))
def cite(m):
    return ''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(','))
for f in sorted(glob.glob(D+'/src/p*.txt')):
    n=int(re.search(r'p(\d+)',os.path.basename(f)).group(1))
    out=[];lis=[]
    def flush():
        global lis
        if lis: out.append('<ul>'+''.join(f'<li>{x}</li>' for x in lis)+'</ul>'); lis=[]
    for line in open(f,encoding='utf-8').read().split('\n'):
        s=line.rstrip()
        if not s: continue
        if s.startswith('LI '): lis.append(s[3:]); continue
        flush()
        if s.startswith('P '): out.append(f'<div class="p">{s[2:]}</div>')
        elif s.startswith('H '): out.append(f'<h4><em>{s[2:]}</em></h4>')
        elif s.startswith('%%/'): out.append('</div>')
        elif s.startswith('%% '): out.append(f'<div id="dx4-p{n}-{s[3:].strip()}" popover class="fenetre">')
        elif s.startswith('PP '): out.append(f'<div class="p">{s[3:]}</div>')
        else: out.append(s)
    flush()
    t='\n'.join(out)
    t=re.sub(r'\^([^^]+)\^',cite,t)
    t=re.sub(r'@@(\w+)\|([^@]+)@@',lambda m:f'<button class="w" popovertarget="dx4-p{n}-{m.group(1)}">{m.group(2)}</button>',t)
    open(f'{D}/fragments/p{n:02d}.html','w',encoding='utf-8').write(t+'\n')
