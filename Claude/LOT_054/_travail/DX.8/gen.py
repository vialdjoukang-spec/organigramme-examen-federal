import re,sys,html,os
PRE='dx8'
BT=re.compile(r'\(\(([\w-]+)\)\)')
def esc(t):
    t=html.escape(t,quote=False)
    t=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',t)
    t=re.sub(r'\{\{([^}]+)\}\}',lambda m:''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(',')),t)
    return t
def build(n):
    L=open(f'src/p{n:02d}.txt',encoding='utf-8').read().split('\n')
    wins={};order=[];i=0;main=[]
    # first pass: separate window defs
    cur=None
    for ln in L:
        if ln.startswith('W '):
            fid,lab=[x.strip() for x in ln[2:].split('|',1)];cur=fid;wins[fid]={'label':lab,'lines':[]}
        elif ln.startswith(' ') and cur and ln.strip():
            wins[cur]['lines'].append(ln.strip())
        else:
            cur=None
            main.append(ln)
    fnum={}
    def btn(m):
        fid=m.group(1)
        if fid not in wins: raise SystemExit(f'p{n}: fenetre inconnue {fid}')
        if fid not in fnum: fnum[fid]=len(fnum)+1
        return f'<button class="w" popovertarget="{PRE}-p{n}-f{fnum[fid]}">{html.escape(wins[fid]["label"],quote=False)}</button>'
    def render_lines(lines,inwin=False):
        out=[];k=0;pend=[]
        def refs(txt):
            return re.findall(r'\(\(([\w-]+)\)\)',txt)
        def flush_wins(txts):
            for t in txts:
                for fid in refs(t):
                    if fid in emitted: continue
                    emitted.add(fid)
                    body=render_lines(wins[fid]['lines'],True)
                    num=fnum.get(fid) or fnum.setdefault(fid,len(fnum)+1)
                    out.append(f'<div id="{PRE}-p{n}-f{num}" popover class="fenetre">{body}</div>')
        while k<len(lines):
            ln=lines[k]
            if not ln.strip(): k+=1; continue
            if ln.startswith('H:'):
                out.append(f'<h4><em>{esc(ln[2:].strip())}</em></h4>');k+=1
            elif ln.startswith('P:'):
                txt=ln[2:].strip();k+=1
                while k<len(lines) and lines[k].startswith('  '): txt+=' '+lines[k].strip();k+=1
                out.append('<div class="p">'+re.sub(r'\(\(([\w-]+)\)\)',btn,esc(txt))+'</div>')
                if not inwin: flush_wins([txt])
            elif ln.startswith('- ') or ln.startswith('U:'):
                items=[]
                if ln.startswith('U:'): k+=1
                while k<len(lines) and lines[k].startswith('- '):
                    t=lines[k][2:].strip();k+=1
                    while k<len(lines) and lines[k].startswith('  '): t+=' '+lines[k].strip();k+=1
                    items.append(t)
                out.append('<ul>'+''.join('<li>'+re.sub(r'\(\(([\w-]+)\)\)',btn,esc(t))+'</li>' for t in items)+'</ul>')
                if not inwin: flush_wins(items)
            elif ln.startswith('T:') or ln.startswith('R:'):
                if ln.startswith('T:'): k+=1
                rows=[]
                while k<len(lines) and lines[k].startswith('R:'):
                    rows.append([c.strip() for c in lines[k][2:].split('|')]);k+=1
                h='<div class="t" style="overflow-x:auto"><table>'
                for ri,r in enumerate(rows):
                    tag='th' if ri==0 else 'td'
                    h+='<tr>'+''.join('<%s>%s</%s>'%(tag,BT.sub(btn,esc(c)),tag) for c in r)+'</tr>'
                out.append(h+'</table></div>')
                if not inwin: flush_wins([c for r in rows for c in r])
            else:
                raise SystemExit(f'p{n}: ligne inconnue: {ln[:60]}')
        return ''.join(out)
    emitted=set()
    return render_lines(main)
if __name__=='__main__':
    os.makedirs('fragments',exist_ok=True)
    for n in range(1,15):
        if os.path.exists(f'src/p{n:02d}.txt'):
            h=build(n);open(f'fragments/p{n:02d}.html','w',encoding='utf-8').write(h);print(n,len(h.encode()))
