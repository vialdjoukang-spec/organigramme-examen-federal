import re,sys,glob,os,html
D=os.path.dirname(os.path.abspath(__file__))
def cit(s):
    return re.sub(r'\{([\w\-,.]+)\}',lambda m:''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in m.group(1).split(',')),s)
def inline(s,n):
    s=re.sub(r'\[\[(.+?)\|(f\d+)\]\]',lambda m:f'<button class="w" popovertarget="dx1-p{n}-{m.group(2)}">{m.group(1)}</button>',s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
    return cit(s)
def conv(txt,n):
    out=[];lines=txt.split('\n');i=0;para=[]
    def flush():
        nonlocal para
        if para: out.append('<div class="p">'+inline(' '.join(para),n)+'</div>'); para=[]
    while i<len(lines):
        l=lines[i].rstrip()
        if not l: flush()
        elif l.startswith('#### '): flush(); out.append('<h4><em>'+l[5:]+'</em></h4>')
        elif l.startswith('@@ '):
            flush(); fid=l[3:].strip(); body=[];i+=1
            while lines[i].strip()!='@@@': body.append(lines[i]); i+=1
            out.append(f'<div id="dx1-p{n}-{fid}" popover class="fenetre">'+conv('\n'.join(body),n)+'</div>')
        elif l.startswith('|'):
            flush(); rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                rows.append(lines[i]);i+=1
            i-=1
            t='<div class="t" style="overflow-x:auto"><table>'
            for k,r in enumerate(rows):
                hd=r.startswith('||'); cells=[c.strip() for c in r.lstrip('|').split('|')]
                tag='th' if hd else 'td'
                t+=('<thead>' if hd else '')+'<tr>'+''.join(f'<{tag}>{inline(c,n)}</{tag}>' for c in cells)+'</tr>'+('</thead><tbody>' if hd else '')
            out.append(t+'</tbody></table></div>')
        elif re.match(r'^\s*- ',l):
            flush(); its=[]
            while i<len(lines) and re.match(r'^\s*- ',lines[i]):
                m=re.match(r'^(\s*)- (.*)$',lines[i]); its.append((len(m.group(1))//2,m.group(2)));i+=1
            i-=1
            h='<ul>';cur=0
            for k,(lv,tx) in enumerate(its):
                if k>0: h+='</li>'
                if lv>cur: h+='<li><ul>'*(lv-cur); cur=lv
                elif lv<cur:
                    while cur>lv: h+='</ul></li>'; cur-=1
                h+='<li>'+inline(tx,n)
            h+='</li>'
            while cur>0: h+='</ul></li>'; cur-=1
            h+='</ul>'
            out.append(h)
        else: para.append(l)
        i+=1
    flush()
    return '\n'.join(out)
for f in sorted(glob.glob(D+'/src/p*.txt')):
    n=int(re.search(r'p(\d+)',os.path.basename(f)).group(1))
    open(f'{D}/fragments/p{n:02d}.html','w').write(conv(open(f).read(),n)+'\n')
    print(f'p{n:02d}',os.path.getsize(f'{D}/fragments/p{n:02d}.html'))
