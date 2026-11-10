#!/usr/bin/env python3
"""gen.py : src/pNN.txt (mini-DSL) -> fragments/pNN.html. Travail propre à DX.5."""
import re, html, os, sys
D = os.path.dirname(os.path.abspath(__file__))
PRE = 'dx5'

def cite(s):
    def r(m):
        ids = [i for i in m.group(1).split(',') if i]
        return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids) + (m.group(2) or '')
    return re.sub(r'\s\^([\w\-:,]+)(\.|(?=\s|$|<))', lambda m: r(m), s)

def inline(s, n):
    s = html.escape(s, quote=False)
    s = re.sub(r'\[\[(.+?)\|(f\d+)\]\]', lambda m: f'<button class="w" popovertarget="{PRE}-p{n}-{m.group(2)}">{m.group(1)}</button>', s)
    return cite(s)

def build(n):
    src = open(os.path.join(D, 'src', f'p{n:02d}.txt'), encoding='utf-8').read().split('\n')
    out, wins, i = [], {}, 0
    def flush():
        for k in sorted(wins, key=lambda x: int(x[1:])):
            out.append(f'<div id="{PRE}-p{n}-{k}" popover class="fenetre">' + ''.join(wins[k]) + '</div>')
        wins.clear()
    while i < len(src):
        l = src[i].rstrip()
        if not l.strip() or l.startswith('#'):
            i += 1; continue
        if l.startswith('p: '):
            flush(); out.append('<div class="p">' + inline(l[3:], n) + '</div>'); i += 1
        elif l.startswith('h: '):
            flush(); out.append('<h4><em>' + html.escape(l[3:], quote=False) + '</em></h4>'); i += 1
        elif l.startswith('win '):
            m = re.match(r'win (f\d+): (.*)', l)
            k, t = m.group(1), m.group(2)
            if ' :: ' in t:
                ti, t = t.split(' :: ', 1)
                wins.setdefault(k, []).append('<h4><em>' + html.escape(ti, quote=False) + '</em></h4>')
            wins.setdefault(k, []).append('<div class="p">' + inline(t, n) + '</div>'); i += 1
        elif l.startswith('ul:'):
            flush(); i += 1; items = []
            while i < len(src) and re.match(r'\s*- ', src[i]):
                lv = (len(src[i]) - len(src[i].lstrip())) // 2
                items.append((lv, inline(src[i].strip()[2:], n))); i += 1
            h, cur = '', 0
            for idx, (lv, t) in enumerate(items):
                nxt = items[idx + 1][0] if idx + 1 < len(items) else 0
                if nxt > lv: h += '<li><p>' + t + '</p><ul>'
                else:
                    h += '<li>' + t
                    h += '</li>' + '</ul></li>' * (lv - nxt)
            out.append('<ul>' + h + '</ul>')
        elif l.startswith('table: '):
            flush(); cap = html.escape(l[7:], quote=False); i += 1; rows = []
            while i < len(src) and src[i].startswith('|'):
                rows.append([c.strip() for c in src[i].strip().strip('|').split(' | ')]); i += 1
            h = '<div class="t" style="overflow-x:auto"><table><caption>' + cap + '</caption>'
            h += '<tr>' + ''.join(f'<th>{inline(c, n)}</th>' for c in rows[0]) + '</tr>'
            for r in rows[1:]:
                h += '<tr>' + ''.join(f'<td>{inline(c, n)}</td>' for c in r) + '</tr>'
            out.append(h + '</table></div>')
        else:
            sys.exit(f'p{n:02d} ligne {i+1} non reconnue : {l[:60]}')
    flush()
    open(os.path.join(D, 'fragments', f'p{n:02d}.html'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')

for n in range(1, 15):
    if os.path.exists(os.path.join(D, 'src', f'p{n:02d}.txt')):
        build(n)
