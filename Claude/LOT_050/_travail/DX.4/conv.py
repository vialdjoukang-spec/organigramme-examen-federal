import re,sys,glob,html,os
M='w9b2b4d'
def cites(s):
    def f(m):
        ids=[x.strip() for x in m.group(1).split(';')]
        ids=[(M+i) if re.fullmatch(r'-\d+',i) else i for i in ids]
        return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)
    return re.sub(r'\s*\{([^{}]+)\}',lambda m:f(m),s)
def inline(s,n):
    s=re.sub(r'\[\[(f\d+)\|([^\]]+)\]\]',lambda m:f'<button class="w" popovertarget="dx4-p{n}-{m.group(1)}">{m.group(2)}</button>',s)
    return cites(s)
def conv(path):
    n=int(re.search(r'p(\d+)',os.path.basename(path)).group(1))
    out=[];lines=open(path,encoding='utf-8').read().split('\n');i=0
    while i<len(lines):
        l=lines[i]
        if not l.strip(): i+=1;continue
        if l.startswith('p: '): out.append(f'<div class="p">{inline(l[3:],n)}</div>')
        elif l.startswith('h: '): out.append(f'<h4><em>{l[3:]}</em></h4>')
        elif l.startswith('- '):
            items=[]
            while i<len(lines) and lines[i].startswith('- '): items.append(f'<li>{inline(lines[i][2:],n)}</li>'); i+=1
            out.append('<ul>'+''.join(items)+'</ul>'); continue
        elif l.startswith('| '):
            rows=[]
            while i<len(lines) and lines[i].startswith('| '): rows.append([c.strip() for c in lines[i][2:].rstrip('|').split('|')]); i+=1
            t='<div class="t" style="overflow-x:auto"><table>'
            t+='<tr>'+''.join(f'<th>{c}</th>' for c in rows[0])+'</tr>'
            for r in rows[1:]: t+='<tr>'+''.join(f'<td>{inline(c,n)}</td>' for c in r)+'</tr>'
            out.append(t+'</table></div>'); continue
        elif l.startswith('win '):
            m=re.match(r'win (f\d+): (.*)',l)
            body=[f'<div class="p">{inline(m.group(2),n)}</div>']
            i+=1
            while i<len(lines) and lines[i].startswith('  '):
                body.append(f'<div class="p">{inline(lines[i].strip(),n)}</div>'); i+=1
            out.append(f'<div id="dx4-p{n}-{m.group(1)}" popover class="fenetre">'+''.join(body)+'</div>'); continue
        else: raise SystemExit(f'ligne inconnue {path}: {l[:60]}')
        i+=1
    open(f'fragments/p{n:02d}.html','w',encoding='utf-8').write('\n'.join(out)+'\n')
for f in sorted(glob.glob('src/p*.txt')): conv(f)
