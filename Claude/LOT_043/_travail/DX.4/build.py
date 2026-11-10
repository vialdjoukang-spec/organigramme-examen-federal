#!/usr/bin/env python3
"""Compile src/pNN.txt (mini-balisage) en fragments/pNN.html pour DX.4."""
import re, os, sys, html
D = os.path.dirname(os.path.abspath(__file__))
PFX = 'dx4'

def inline(s):
    s = re.sub(r'([.!?])((?:\[\[[\w.\-:, ]+\]\])+)', r'\2\1', s)
    s = s.replace('&', '&amp;').replace('<', '&lt;')
    s = re.sub(r'\[\[([\w.\-:, ]+)\]\]', lambda m: ''.join(
        f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(',')), s)
    s = re.sub(r'\{\{([\w\-]+)\|([^}]+)\}\}', lambda m: f'<button class="w" popovertarget="{PFX}-{m.group(1)}">{m.group(2)}</button>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    return s

def block(b):
    lines = b.strip('\n').split('\n')
    h = lines[0]
    if h.startswith('# '):
        return f'<h4><em>{inline(h[2:])}</em></h4>'
    if h.startswith('TABLE'):
        rows = [[c.strip() for c in l.split(' | ')] for l in lines[1:] if l.strip()]
        out = '<div class="t" style="overflow-x:auto"><table>'
        for k, r in enumerate(rows):
            tag = 'th' if k == 0 else 'td'
            out += '<tr>' + ''.join(f'<{tag}>{inline(c)}</{tag}>' for c in r) + '</tr>'
        return out + '</table></div>'
    if h.startswith('- '):
        out = '<ul>'
        for l in lines:
            m = re.match(r'(-+) (.*)', l)
            if m:
                d = len(m.group(1))
                st = '' if d == 1 else f' style="margin-left:{1.4 * (d - 1):.1f}em;list-style:circle"'
                out += f'<li{st}>{inline(m.group(2))}</li>'
        return out + '</ul>'
    return f'<div class="p">{inline(" ".join(lines))}</div>'

def compile_(txt):
    out, inwin, win = [], None, []
    for b in re.split(r'\n\s*\n', txt):
        b = b.strip('\n')
        if not b.strip():
            continue
        first = b.split('\n')[0]
        if first.startswith('WIN '):
            inwin = first[4:].strip(); win = []
            rest = '\n'.join(b.split('\n')[1:])
            if rest.strip():
                win.append(block(rest))
            continue
        if first.strip() == 'ENDWIN':
            out.append(f'<div id="{PFX}-{inwin}" popover class="fenetre">' + ''.join(win) + '</div>')
            inwin = None
            continue
        (win if inwin else out).append(block(b))
    return '\n'.join(out) + '\n'

if __name__ == '__main__':
    os.makedirs(f'{D}/fragments', exist_ok=True)
    for f in sorted(os.listdir(f'{D}/src')):
        if f.endswith('.txt'):
            n = f[:-4]
            open(f'{D}/fragments/{n}.html', 'w').write(compile_(open(f'{D}/src/{f}').read()))
    print('ok')
