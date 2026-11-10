#!/usr/bin/env python3
"""Convertit src/pNN.txt (mini-balisage) en fragments/pNN.html. Aucun contenu : mise en forme seulement.
  paragraphe = bloc séparé par ligne vide ; '## t' = sous-titre ; '- x' = liste ; '{id,id}' = citation ;
  '<<libellé|fK>>' = bouton de fenêtre ; '@w fK' ... '@end' = fenêtre ; '@t' ... '@end' = tableau (1re ligne = en-tête, cellules séparées par ' | ')."""
import re, os, sys, html
D = os.path.dirname(os.path.abspath(__file__))
PRE = 'dx1'
def cit(s):
    s = re.sub(r'([.!?])((?:\{[\w.\-:, ]+\})+)', r'\2\1', s)
    def r(m):
        return ''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(','))
    return re.sub(r'\{([\w.\-:, ]+)\}', r, s)
def inline(s, n):
    s = cit(html.escape(s, quote=False))
    s = re.sub(r'&lt;&lt;(.+?)\|(f\d+)&gt;&gt;', lambda m: f'<button class="w" popovertarget="{PRE}-p{n}-{m.group(2)}">{m.group(1)}</button>', s)
    return s
def conv(n):
    src = open(os.path.join(D, 'src', f'p{n:02d}.txt'), encoding='utf-8').read().split('\n')
    out, i, wins, buf = [], 0, [], []
    def flush_p(lines):
        if lines:
            out.append(f'<div class="p">{inline(" ".join(lines), n)}</div>')
    para = []
    while i < len(src):
        l = src[i].rstrip()
        if l.startswith('@t'):
            flush_p(para); para = []
            rows = []; i += 1
            while not src[i].startswith('@end'):
                if src[i].strip(): rows.append([c.strip() for c in src[i].split(' | ')])
                i += 1
            h = '<tr>' + ''.join(f'<th>{inline(c, n)}</th>' for c in rows[0]) + '</tr>'
            b = ''.join('<tr>' + ''.join(f'<td>{inline(c, n)}</td>' for c in r) + '</tr>' for r in rows[1:])
            out.append(f'<div class="t" style="overflow-x:auto"><table>{h}{b}</table></div>')
        elif l.startswith('@w '):
            flush_p(para); para = []
            fid = l.split()[1]; body = []; i += 1
            while not src[i].startswith('@end'):
                body.append(src[i]); i += 1
            ps = [x.strip() for x in '\n'.join(body).split('\n\n') if x.strip()]
            wins.append(f'<div id="{PRE}-p{n}-{fid}" popover class="fenetre">' + ''.join(f'<div class="p">{inline(p.replace(chr(10), " "), n)}</div>' for p in ps) + '</div>')
        elif l.startswith('### '):
            flush_p(para); para = []
            out.append(f'<h4><em>{html.escape(l[4:])}</em></h4>')
        elif l.startswith('## '):
            flush_p(para); para = []
            out.append(f'<h4><em>{html.escape(l[3:])}</em></h4>')
        elif l.startswith('- '):
            flush_p(para); para = []
            items = []
            while i < len(src) and src[i].startswith('- '):
                items.append(src[i][2:]); i += 1
            out.append('<ul>' + ''.join(f'<li>{inline(x, n)}</li>' for x in items) + '</ul>')
            continue
        elif not l.strip():
            flush_p(para); para = []
            out.extend(wins); wins = []
        else:
            para.append(l)
        i += 1
    flush_p(para); out.extend(wins)
    os.makedirs(os.path.join(D, 'fragments'), exist_ok=True)
    open(os.path.join(D, 'fragments', f'p{n:02d}.html'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
for n in range(1, 15):
    if os.path.exists(os.path.join(D, 'src', f'p{n:02d}.txt')): conv(n)
