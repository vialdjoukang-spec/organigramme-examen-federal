#!/usr/bin/env python3
"""Compile src_txt/pNN.txt (mini-DSL) en fragments/pNN.html. Usage: python3 mk.py [NN ...]"""
import re, sys, html, os, glob
D = os.path.dirname(os.path.abspath(__file__))
PRE = 'dx10'

def cite(m):
    ids = [i.strip() for i in m.group(1).split(',')]
    return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)

def inline(s, n, wins, used):
    s = html.escape(s, quote=False)
    s = re.sub(r'\{([\w.\-:, ]+)\}', cite, s)
    def btn(m):
        k, lab = m.group(1), m.group(2)
        used.append(k)
        if k not in wins: raise SystemExit(f'fenetre inconnue {k} (point {n})')
        return f'<button class="w" popovertarget="{PRE}-p{n}-f{k}">{lab}</button>'
    s = re.sub(r'@(\w+):([^@]+)@', btn, s)
    return s

def para(s, n, wins, used):
    return f'<div class="p">{inline(s, n, wins, used)}</div>'

def win_html(k, content, n, wins):
    parts = [x.strip() for x in content.split('//') if x.strip()]
    body = ''
    for x in parts:
        if x.startswith('- '):
            body += '<ul>' + ''.join(f'<li>{inline(i.strip(), n, wins, [])}</li>' for i in x.split(' - ') if i.strip()).replace('<li>- ', '<li>') + '</ul>'
        elif x.startswith('H '):
            body += f'<h4><em>{inline(x[2:], n, wins, [])}</em></h4>'
        else:
            body += para(x, n, wins, [])
    return f'<div id="{PRE}-p{n}-f{k}" popover class="fenetre">{body}</div>'

def build(n):
    src = open(f'{D}/src_txt/p{n:02d}.txt', encoding='utf-8').read()
    blocks = [b for b in re.split(r'\n\s*\n', src.strip()) if b.strip() and not b.startswith('#')]
    wins = {}
    # pre-pass: collect windows
    for b in blocks:
        for line in b.split('\n'):
            if line.startswith('W '):
                k, c = line[2:].split(' ¦ ', 1)
                wins[k.strip()] = c.strip()
    out, pend = [], []
    for b in blocks:
        lines = [l for l in b.split('\n') if l.strip()]
        head = lines[0]
        if head.startswith('W '):
            continue
        used = []
        if head.startswith('P '):
            out.append(para(' '.join(l.strip() for l in lines)[2:], n, wins, used))
        elif head.startswith('H '):
            out.append(f'<h4><em>{inline(head[2:], n, wins, used)}</em></h4>')
        elif head.startswith('L'):
            items = [l[2:].strip() for l in lines[1:] if l.startswith('- ')]
            if head.strip() != 'L': out.append(para(head[2:], n, wins, used))
            out.append('<ul>\n' + '\n'.join(f'<li>{inline(i, n, wins, used)}</li>' for i in items) + '\n</ul>')
        elif head.strip() == 'N':
            h2='<ul style="list-style:none;padding-left:0">'
            for l in lines[1:]:
                ind=(len(l)-len(l.lstrip()))//2
                h2+=f'<li style="margin-left:{ind*1.6}em">'+inline(l.strip()[2:],n,wins,used)+'</li>'
            out.append(h2+'</ul>')
        elif head.strip() == 'T':
            rows = [[c.strip() for c in l.split(' ¦ ')] for l in lines[1:]]
            t = '<div class="t" style="overflow-x:auto"><table><tr>' + ''.join(f'<th>{inline(c, n, wins, used)}</th>' for c in rows[0]) + '</tr>'
            for r in rows[1:]:
                t += '<tr>' + ''.join(f'<td>{inline(c, n, wins, used)}</td>' for c in r) + '</tr>'
            out.append(t + '</table></div>')
        else:
            raise SystemExit(f'bloc inconnu point {n}: {head[:60]}')
        for k in used:
            out.append(win_html(k, wins[k], n, wins))
    h = '\n'.join(out) + '\n'
    open(f'{D}/fragments/p{n:02d}.html', 'w', encoding='utf-8').write(h)
    return len(h.encode())

if __name__ == '__main__':
    ns = [int(a) for a in sys.argv[1:]] or [int(re.search(r'p(\d+)', f).group(1)) for f in sorted(glob.glob(f'{D}/src_txt/p*.txt'))]
    tot = 0
    for n in ns:
        sz = build(n); tot += sz; print(f'p{n:02d}: {sz} o')
