#!/usr/bin/env python3
"""Convertit src/pNN.txt (mini-balisage) en fragments/pNN.html pour DX.7."""
import re, os, sys, html
D = os.path.dirname(os.path.abspath(__file__))
def cit(m):
    return ''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(','))
def inline(s):
    s = s.replace('&', '&amp;') if '&amp;' not in s else s
    s = re.sub(r'\[\[([\w\-]+)\|([^\]]+)\]\]', r'<button class="w" popovertarget="\1">\2</button>', s)
    s = re.sub(r'\{([\w\-,\s]+)\}', cit, s)
    return s
def reorder(txt):
    L=txt.split('\n'); wins={}; rest=[]; i=0
    while i<len(L):
        if L[i].startswith('W '):
            wid=L[i][2:].strip(); j=i
            while L[j]!='ENDW': j+=1
            wins[wid]=L[i:j+1]; i=j+1
        else: rest.append(L[i]); i+=1
    out=[]
    for l in rest:
        out.append(l)
        for m in re.findall(r'\[\[([\w\-]+)\|',l):
            if m in wins: out+=wins.pop(m)
    for w in wins.values(): out+=w
    return '\n'.join(out)
def conv(txt):
    txt=reorder(txt)
    out, ul, tab, win = [], [], [], False
    def flush():
        nonlocal ul, tab
        if ul:
            out.append('<ul>' + ''.join(f'<li>{inline(x)}</li>' for x in ul) + '</ul>'); ul = []
        if tab:
            h = ''.join(f'<th>{inline(c)}</th>' for c in tab[0])
            r = ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in row) + '</tr>' for row in tab[1:])
            out.append(f'<div class="t" style="overflow-x:auto"><table><tr>{h}</tr>{r}</table></div>'); tab = []
    for ln in txt.split('\n'):
        ln = ln.rstrip()
        if not ln.strip(): continue
        k, _, rest = ln.partition(' ')
        if k == 'UL': ul.append(rest); continue
        if k == 'T': tab.append([c.strip() for c in rest.split(' | ')]); continue
        flush()
        if k == 'P': out.append(f'<div class="p">{inline(rest)}</div>')
        elif k == 'H': out.append(f'<h4><em>{inline(rest)}</em></h4>')
        elif k == 'W': out.append(f'<div id="{rest.strip()}" popover class="fenetre">'); win = True
        elif k == 'ENDW': out.append('</div>'); win = False
        else: sys.exit(f'ligne inconnue: {ln[:80]}')
    flush()
    return '\n'.join(out) + '\n'
os.makedirs(f'{D}/fragments', exist_ok=True)
for f in sorted(os.listdir(f'{D}/src')):
    if f.endswith('.txt'):
        h = conv(open(f'{D}/src/{f}', encoding='utf-8').read())
        open(f'{D}/fragments/{f[:-4]}.html', 'w', encoding='utf-8').write(h)
        print(f, len(h.encode()))
