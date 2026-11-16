#!/usr/bin/env python3
"""Expanseur local : src/pNN.txt (mini-balisage) -> fragments/pNN.html. Écrit uniquement dans _travail/DX.2/."""
import re, os, sys, html
D = os.path.dirname(os.path.abspath(__file__))
PRE = 'dx2'
def cit(t):
    return re.sub(r'\{([\w.\-]+)\}', lambda m: f'<sup class="r"><a href="#sb-{m.group(1)}">{m.group(1)}</a></sup>', t)
def btn(t, n):
    return re.sub(r'\[\[(f\d+)\|([^\]]+)\]\]', lambda m: f'<button class="w" popovertarget="{PRE}-p{n}-{m.group(1)}">{m.group(2)}</button>', t)
def inline(t, n):
    return btn(cit(t), n)
def conv(src, n):
    out, ul, tab = [], False, None
    nested = False
    def closeul():
        nonlocal ul
        if ul: out.append('</ul>'); ul = False
    def closetab():
        nonlocal tab
        if tab is not None:
            out.append('<div class="t" style="overflow-x:auto"><table>' + ''.join(tab) + '</table></div>'); tab = None
    for ln in src.split('\n'):
        ln = ln.rstrip()
        if not ln: continue
        if ln.startswith('  - '):
            if not nested:
                out[-1] = out[-1][:-5] + '<ul>'; nested = True
            out.append('<li>' + inline(ln[4:], n) + '</li>'); continue
        if nested:
            out.append('</ul></li>'); nested = False
        if ln.startswith('- '):
            closetab()
            if not ul: out.append('<ul>'); ul = True
            out.append('<li>' + inline(ln[2:], n) + '</li>'); continue
        closeul()
        if ln.startswith('T: ') or ln.startswith('R: '):
            cells = [c.strip() for c in ln[3:].split('|')]
            if tab is None: tab = []
            tag = 'th' if ln.startswith('T: ') else 'td'
            tab.append('<tr>' + ''.join(f'<{tag}>{inline(c, n)}</{tag}>' for c in cells) + '</tr>'); continue
        closetab()
        if ln.startswith('H: '):
            out.append(f'<h4><em>{html.escape(ln[3:])}</em></h4>')
        elif ln.startswith('P: '):
            out.append('<div class="p">' + inline(ln[3:], n) + '</div>')
        elif ln.startswith('W: '):
            k, body = ln[3:].split('|', 1)
            paras = ''.join('<div class="p">' + inline(x.strip(), n) + '</div>' for x in body.split('¶'))
            out.append(f'<div id="{PRE}-p{n}-{k.strip()}" popover class="fenetre">{paras}</div>')
        else:
            raise SystemExit(f'ligne non reconnue p{n}: {ln[:60]}')
    if nested: out.append('</ul></li>')
    closeul(); closetab()
    return '\n'.join(out) + '\n'
for n in range(1, 15):
    f = os.path.join(D, 'src', f'p{n:02d}.txt')
    if os.path.exists(f):
        open(os.path.join(D, 'fragments', f'p{n:02d}.html'), 'w', encoding='utf-8').write(conv(open(f, encoding='utf-8').read(), n))
