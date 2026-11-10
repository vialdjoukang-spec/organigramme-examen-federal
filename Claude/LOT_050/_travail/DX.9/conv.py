import re,sys,os,glob,html
D=os.path.dirname(os.path.abspath(__file__))
CIT=re.compile(r'\s?\[((?:w[0-9a-f]{5,6}|aips)-?[\w]*-\d+)\]')
def cit(s):
    return CIT.sub(lambda m:'<sup class="r"><a href="#sb-%s">%s</a></sup>'%(m.group(1),m.group(1)),s)
def conv(txt):
    out=[]
    for blk in re.split(r'\n\s*\n',txt.strip()):
        b=blk.strip()
        if not b: continue
        if b.startswith('## '): out.append('<h4><em>%s</em></h4>'%b[3:]); continue
        if b.startswith('<'): out.append(cit(b)); continue
        lines=b.split('\n')
        if all(l.startswith('- ') for l in lines):
            out.append('<ul>'+''.join('<li>%s</li>'%cit(l[2:]) for l in lines)+'</ul>'); continue
        if all(l.startswith('|') for l in lines):
            rows=[[c.strip() for c in l.strip().strip('|').split('|')] for l in lines]
            t='<div class="t" style="overflow-x:auto"><table><thead><tr>'+''.join('<th>%s</th>'%c for c in rows[0])+'</tr></thead><tbody>'
            for r in rows[1:]: t+='<tr>'+''.join('<td>%s</td>'%cit(c) for c in r)+'</tr>'
            out.append(t+'</tbody></table></div>'); continue
        out.append('<div class="p">%s</div>'%cit(' '.join(lines)))
    return '\n'.join(out)+'\n'
for f in sorted(glob.glob(D+'/src/p*.txt')):
    n=os.path.basename(f)[:-4]
    open(D+'/fragments/%s.html'%n,'w').write(conv(open(f).read()))
print('ok')
