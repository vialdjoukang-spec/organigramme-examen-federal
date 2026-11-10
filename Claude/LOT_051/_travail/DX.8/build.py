#!/usr/bin/env python3
# Compile src/pNN.txt (mini-langage) -> fragments/pNN.html
import re, html, os, sys
D = os.path.dirname(os.path.abspath(__file__))
PRE = 'dx8'
def cit(m):
    return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in m.group(1).split())
def inline(t, n):
    t = html.escape(t, quote=False)
    t = re.sub(r'@\(([^)]*)\)', cit, t)
    t = re.sub(r'\[\[([^|\]]+)\|(\d+)\]\]', lambda m: f'<button class="w" popovertarget="{PRE}-p{n}-f{m.group(2)}">{m.group(1)}</button>', t)
    return t
def comp(n):
    src = open(f'{D}/src/p{n:02d}.txt', encoding='utf-8').read()
    out = []; fen = None
    blocs = re.split(r'\n\s*\n', src.strip())
    for b in blocs:
        b = b.strip('\n')
        if not b.strip(): continue
        L = b.split('\n')
        if L[0].startswith('W') and re.fullmatch(r'W\d+', L[0].strip()):
            fen = L[0].strip()[1:]; out.append(f'<div id="{PRE}-p{n}-f{fen}" popover class="fenetre">'); L = L[1:]
            if not L: continue
            b = '\n'.join(L)
        if L[-1].strip() == '/W':
            L = L[:-1]; b = '\n'.join(L); close = True
        else: close = False
        if L and L[0].startswith('## '):
            out.append(f'<h4><em>{inline(L[0][3:], n)}</em></h4>'); L = L[1:]
        if L and L[0].startswith('T|'):
            rows = [[c.strip() for c in l.strip().strip('|').replace('T|', '', 1).split('|')] for l in L if l.startswith('T|')]
            h = '<thead><tr>' + ''.join(f'<th>{inline(c, n)}</th>' for c in rows[0]) + '</tr></thead>'
            bd = '<tbody>' + ''.join('<tr>' + ''.join(f'<td>{inline(c, n)}</td>' for c in r) + '</tr>' for r in rows[1:]) + '</tbody>'
            out.append(f'<div class="t" style="overflow-x:auto"><table>{h}{bd}</table></div>')
        elif L and L[0].startswith('- '):
            out.append('<ul>' + ''.join(f'<li>{inline(l[2:], n)}</li>' for l in L if l.startswith('- ')) + '</ul>')
        elif L and L[0].startswith('!! '):
            out.append(f'<div class="alert alerte"><div class="p">{inline(" ".join(L)[3:], n)}</div></div>')
        elif L and L[0].startswith('KEY '):
            out.append(f'<div class="key"><div class="p">{inline(" ".join(L)[4:], n)}</div></div>')
        elif L:
            for l in L:
                if l.startswith('## '): out.append(f'<h4><em>{inline(l[3:], n)}</em></h4>')
                else: out.append(f'<div class="p">{inline(l, n)}</div>')
        if close: out.append('</div>')
    return '\n'.join(out) + '\n'
os.makedirs(f'{D}/fragments', exist_ok=True)
for n in range(1, 15):
    if os.path.exists(f'{D}/src/p{n:02d}.txt'):
        open(f'{D}/fragments/p{n:02d}.html', 'w', encoding='utf-8').write(comp(n))
