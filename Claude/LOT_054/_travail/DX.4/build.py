#!/usr/bin/env python3
"""Convertit src/pNN.txt (mini-balisage) en fragments/pNN.html pour DX.4."""
import re, os, sys, html
ICI = os.path.dirname(os.path.abspath(__file__))
AL = {'X':'w0e3adc','U':'wc98211','Ua':'we7bdc5','T':'w983d6e','Tm':'wc18734','Th':'wea1c3f','Ts':'weef5c3','G':'w8818ba',
      'A':'w73e3ee','J':'w2f8271','H':'w726084','D':'w7c5ff4','N':'w05e6f4','E':'wb2b33d','Es':'wee3ff9','S':'wf62797',
      'L':'w1f3d24','I':'wf6f45c','K':'wc1104a','P':'w6b8b39','Q':'w080a44','Z':'wa8a90e','R':'w11a3a4','C':'w33edcd'}
def cid(x):
    x = x.strip()
    if x.startswith('aips'): return x
    a, n = x.rsplit('-', 1)
    return f'{AL[a]}-{n}'
def cites(s):
    def f(m):
        return ''.join(f'<sup class="r"><a href="#sb-{cid(i)}">{cid(i)}</a></sup>' for i in re.split(r'[ ,]+', m.group(1).strip()) if i)
    return re.sub(r'\[\[(.*?)\]\]', f, s)
def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
def inline(s):
    s = esc(s)
    s = s.replace('&lt;em&gt;', '<em>').replace('&lt;/em&gt;', '</em>').replace('&lt;b&gt;', '<b>').replace('&lt;/b&gt;', '</b>')
    return cites(s)
def para(txt, pre, n, k):
    wins = []
    def w(m):
        k[0] += 1
        wid = f'{pre}-p{n}-f{k[0]}'
        body = ''.join(f'<div class="p">{inline(p.strip())}</div>' for p in m.group(2).split('¶') if p.strip())
        wins.append(f'<div id="{wid}" popover class="fenetre">{body}</div>')
        return f'<button class="w" popovertarget="{wid}">{esc(m.group(1))}</button>'
    t = re.sub(r'\{\{(.*?)::(.*?)\}\}', w, txt, flags=re.S)
    # séparer le texte hors boutons
    parts = re.split(r'(<button.*?</button>)', t)
    t = ''.join(p if p.startswith('<button') else inline(p) for p in parts)
    return f'<div class="p">{t}</div>' + ''.join(wins)
def conv(src, pre, n):
    out, k = [], [0]
    blocs = re.split(r'\n\s*\n', src.strip())
    for b in blocs:
        L = b.strip().split('\n')
        if L[0].startswith('## '):
            out.append(f'<h4><em>{inline(L[0][3:])}</em></h4>')
            rest = '\n'.join(L[1:]).strip()
            if rest: out.append(conv(rest, pre, n))
        elif L[0].startswith('# '):
            out.append(f'<h4><em>{inline(L[0][2:])}</em></h4>')
            rest = '\n'.join(L[1:]).strip()
            if rest: out.append(conv(rest, pre, n))
        elif L[0].startswith('|'):
            rows = [[c.strip() for c in r.strip().strip('|').split('|')] for r in L]
            h = '<tr>' + ''.join(f'<th>{inline(c)}</th>' for c in rows[0]) + '</tr>'
            body = ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>' for r in rows[1:])
            out.append(f'<div class="t" style="overflow-x:auto"><table>{h}{body}</table></div>')
        elif L[0].startswith('- ') or L[0].startswith('  - '):
            out.append(lst(L, pre, n, k))
        else:
            out.append(para(' '.join(l.strip() for l in L), pre, n, k))
    return '\n'.join(out)
def lst(L, pre, n, k):
    # liste à deux niveaux : "- " et "  - "
    html_, stack_open = '<ul>', False
    i = 0
    items = []
    for l in L:
        if l.startswith('  - '): items[-1][1].append(l[4:])
        else: items.append([l[2:], []])
    res = '<ul>'
    for t, subs in items:
        if subs: res += '<li><p>' + inline(t) + '</p>\n<ul>' + ''.join('<li>' + inline(s) + '</li>' for s in subs) + '</ul>'
        else: res += '<li>' + inline(t)
        res += '</li>\n'
    return res + '</ul>'
if __name__ == '__main__':
    os.makedirs(os.path.join(ICI, 'fragments'), exist_ok=True)
    for f in sorted(os.listdir(os.path.join(ICI, 'src'))):
        if not f.endswith('.txt'): continue
        n = int(f[1:3])
        src = open(os.path.join(ICI, 'src', f), encoding='utf-8').read()
        open(os.path.join(ICI, 'fragments', f'p{n:02d}.html'), 'w', encoding='utf-8').write(conv(src, 'dx4', n) + '\n')
