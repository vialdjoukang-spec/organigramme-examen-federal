#!/usr/bin/env python3
"""Expansion des fragments source (src/pNN.txt) en fragments HTML.
[[id id]] -> citations ; {{fK|libellé}} -> bouton fenêtre ; lignes 'P ' -> div.p ; blocs '@@fK' ... '@@end' -> fenêtre."""
import re, os, glob
D = os.path.dirname(os.path.abspath(__file__))
def cit(m):
    return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in m.group(1).split())
for f in sorted(glob.glob(D + '/src/p[0-9][0-9].txt')):
    n = int(os.path.basename(f)[1:3])
    out, fen = [], None
    for l in open(f, encoding='utf-8').read().split('\n'):
        if fen is not None:
            if l.strip() == '@@end':
                out.append(f'<div id="dx6-p{n}-{fen[0]}" popover class="fenetre">' + '\n'.join(fen[1]) + '</div>')
                fen = None
            else:
                fen[1].append('<div class="p">' + l[2:] + '</div>' if l.startswith('P ') else l)
            continue
        m = re.match(r'@@(f\d+)\s*$', l.strip())
        if m:
            fen = (m.group(1), [])
            continue
        if not l.strip():
            continue
        if l.startswith('P '):
            l = '<div class="p">' + l[2:] + '</div>'
        out.append(l)
    t = '\n'.join(out)
    t = re.sub(r'([.!?])((?:\[\[[^\]]+\]\])+)', r'\2\1', t)
    t = t.replace('<div class="t">','<div class="t" style="overflow-x:auto">')
    t = re.sub(r'\[\[([^\]]+)\]\]', cit, t)
    t = re.sub(r'\{\{(f\d+)\|([^}]+)\}\}', lambda m: f'<button class="w" popovertarget="dx6-p{n}-{m.group(1)}">{m.group(2)}</button>', t)
    open(D + f'/fragments/p{n:02d}.html', 'w', encoding='utf-8').write(t + '\n')
    print(n, len(t.encode()))
