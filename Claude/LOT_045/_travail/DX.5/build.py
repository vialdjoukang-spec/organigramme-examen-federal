import re,glob,os,html
PRE='dx5'
def conv(txt):
    out=[];lines=txt.split('\n');i=0;ul=False;tb=False
    def cite(s):
        s=re.sub(r' ?\[\[([^\]]+)\]\]',lambda m:''.join('<sup class="r"><a href="#sb-%s">%s</a></sup>'%(x.strip(),x.strip()) for x in m.group(1).split(',')),s)
        s=re.sub(r'\{\{w:([\w-]+)\|([^}]+)\}\}',lambda m:'<button class="w" popovertarget="%s-%s">%s</button>'%(PRE,m.group(1),m.group(2)),s)
        return s
    for l in lines:
        l=l.rstrip()
        if ul and not l.startswith('LI: '): out.append('</ul>');ul=False
        if not l: continue
        if tb:
            if l=='/T': out.append('</table></div>');tb=False
            else:
                cells=[c.strip() for c in l[3:].split(' | ')]
                tag='th' if l.startswith('h: ') else 'td'
                out.append('<tr>'+''.join('<%s>%s</%s>'%(tag,cite(c),tag) for c in cells)+'</tr>')
            continue
        if l=='T:': out.append('<div class="t" style="overflow-x:auto"><table>');tb=True
        elif l.startswith('P: '): out.append('<div class="p">'+cite(l[3:])+'</div>')
        elif l.startswith('H: '): out.append('<h4><em>'+l[3:]+'</em></h4>')
        elif l.startswith('LI: '):
            if not ul: out.append('<ul>');ul=True
            out.append('<li>'+cite(l[4:])+'</li>')
        elif l.startswith('@@win '): out.append('<div id="%s-%s" popover class="fenetre">'%(PRE,l[6:].strip()))
        elif l=='@@end': out.append('</div>')
        else: raise SystemExit('ligne inconnue: '+l[:60])
    if ul: out.append('</ul>')
    return '\n'.join(out)+'\n'
for f in sorted(glob.glob('src/p*.txt')):
    n=os.path.basename(f)[:-4]
    open('fragments/%s.html'%n,'w').write(conv(open(f).read()))
