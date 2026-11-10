#!/usr/bin/env python3
"""Préprocesseur local DX.5 : src/pNN.txt -> fragments/pNN.html (macros de citation, fenêtres, tableaux)."""
import re, os, sys, html
D = os.path.dirname(os.path.abspath(__file__))
MAP = dict(WS='wd7036b', CT='w1a65c8', UL='w00f747', HU='wae3eb5', ES='wefeff3', DB='w36d290', CH='w65075b', AV='we0f892',
           DV='we71f2a', LA='wacca11', LO='w68dc92', PC='w8e4b01', SW='wbcff74', RC='w5418cb', KA='w0eb9f4', KB='w9d5455',
           EA='w36b724', US='w24c723', HG='w683c0b', GS='wae7d25', AUG='aips-45674', CIP='aips-56649', MET='aips-55280',
           CEF='aips-68535', PAR='aips-58716')
def cit(m):
    return f'<sup class="r"><a href="#sb-{MAP[m.group(2)]}-{m.group(3)}">{MAP[m.group(2)]}-{m.group(3)}</a></sup>'
def inline(s, n):
    s = re.sub(r'(\s?)\[(' + '|'.join(sorted(MAP, key=len, reverse=True)) + r')(\d+)\]', cit, s)
    s = re.sub(r'\{b:([\w-]+)\|([^}]*)\}', lambda m: f'<button class="w" popovertarget="dx5-p{n}-{m.group(1)}">{m.group(2)}</button>', s)
    return s
def cells(line, tag, n):
    return '<tr>' + ''.join(f'<{tag}>{inline(c.strip(), n)}</{tag}>' for c in line.split('|')) + '</tr>'
def build(n):
    src = open(f'{D}/src/p{n:02d}.txt', encoding='utf-8').read().split('\n')
    out, i, ul, tab, first = [], 0, False, False, True
    def close_ul():
        nonlocal ul
        if ul: out.append('</ul>'); ul = False
    for ln in src:
        if not ln.strip(): continue
        if ul and not ln.startswith('- '): close_ul()
        if tab:
            if ln.strip() == '/T':
                out.append('</table></div>'); tab = False
            else:
                out.append(cells(ln, 'th' if first else 'td', n)); first = False
            continue
        if ln.startswith('P: '): out.append('<div class="p">' + inline(ln[3:], n) + '</div>')
        elif ln.startswith('H: '): out.append('<h4><em>' + inline(ln[3:], n) + '</em></h4>')
        elif ln.startswith('- '):
            if not ul: out.append('<ul>'); ul = True
            out.append('<li>' + inline(ln[2:], n) + '</li>')
        elif ln.strip() == 'T:':
            out.append('<div class="t" style="overflow-x:auto"><table>'); tab = True; first = True
        elif ln.lstrip().startswith('<'): out.append(inline(ln, n))
        elif ln.startswith('{w:'):
            k = re.match(r'\{w:([\w-]+)\}', ln).group(1)
            out.append(f'<div id="dx5-p{n}-{k}" popover class="fenetre">')
        elif ln.strip() == '{/w}': close_ul(); out.append('</div>')
        else: raise SystemExit(f'p{n}: ligne non reconnue: {ln[:80]}')
    close_ul()
    os.makedirs(f'{D}/fragments', exist_ok=True)
    open(f'{D}/fragments/p{n:02d}.html', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    return sum(len(x.encode()) for x in out)
if __name__ == '__main__':
    tot = 0
    for n in range(1, 15):
        if os.path.exists(f'{D}/src/p{n:02d}.txt'):
            b = build(n); tot += b; print(n, b)
    print('total', tot)
