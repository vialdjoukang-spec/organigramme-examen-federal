#!/usr/bin/env python3
"""Compile src/pNN.txt (balisage compact) en fragments/pNN.html. Local à DX.10."""
import re, os, sys, html
D = os.path.dirname(os.path.abspath(__file__))
PRE = 'dx10'
def cit(s):
    def r(m):
        return ''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(','))
    return re.sub(r'\s*\[\[([^\]]+)\]\]', lambda m: r(m), s)
def btn(n, s):
    return re.sub(r'\{\{w:(\w+)\|([^}]+)\}\}', lambda m: f'<button class="w" popovertarget="{PRE}-p{n}-f{m.group(1)}">{m.group(2)}</button>', s)
def wrap(n, s):
    for m in list(re.finditer(r'\s*\{\{W:(\w+)\|([^}]+)\}\}', s)):
        pass
    while True:
        m = re.search(r'\s*\{\{W:(\w+)\|([^}]+)\}\}', s)
        if not m: return s
        key, term = m.group(1), m.group(2)
        s = s[:m.start()] + s[m.end():]
        i = s.find(term)
        if i < 0: sys.exit(f'terme absent p{n}: {term}')
        s = s[:i] + '{{w:' + key + '|' + term + '}}' + s[i+len(term):]
def inline(n, s):
    return btn(n, cit(wrap(n, s)))
def build(n):
    out = []
    for ln in open(f'{D}/src/p{n:02d}.txt', encoding='utf-8'):
        ln = ln.rstrip('\n')
        if not ln.strip() or ln.startswith('#'): continue
        k, _, body = ln.partition(':')
        body = body.strip()
        if k == 'P':
            out.append(f'<div class="p">{inline(n, body)}</div>')
        elif k == 'H':
            out.append(f'<h4><em>{html.escape(body)}</em></h4>')
        elif k == 'UL':
            out.append('<ul>' + ''.join(f'<li>{inline(n, x.strip())}</li>' for x in body.split(' ;; ')) + '</ul>')
        elif k == 'R':
            out.append(inline(n, body))
        elif k == 'T':
            rows = [r.split('|') for r in body.split(' ;; ')]
            t = '<thead><tr>' + ''.join(f'<th>{inline(n, c.strip())}</th>' for c in rows[0]) + '</tr></thead><tbody>'
            t += '\n'.join('<tr>' + ''.join(f'<td>{inline(n, c.strip())}</td>' for c in r) + '</tr>' for r in rows[1:]) + '</tbody>'
            out.append(f'<div class="t" style="overflow-x:auto"><table>{t}</table></div>')
        elif k.startswith('W'):
            key = k[1:]
            paras = ''.join(f'<div class="p">{inline(n, x.strip())}</div>' for x in body.split(' || '))
            out.append(f'<div id="{PRE}-p{n}-f{key}" popover class="fenetre">{paras}</div>')
        else:
            sys.exit(f'balise inconnue p{n}: {ln[:60]}')
    os.makedirs(f'{D}/fragments', exist_ok=True)
    open(f'{D}/fragments/p{n:02d}.html', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    return sum(len(x.encode()) for x in out)
if __name__ == '__main__':
    tot = 0
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else range(1, 15)):
        if os.path.exists(f'{D}/src/p{n:02d}.txt'):
            b = build(n); tot += b; print(n, b)
    print('total', tot)
