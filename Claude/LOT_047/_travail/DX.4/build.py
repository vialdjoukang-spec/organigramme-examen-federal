#!/usr/bin/env python3
"""Convertit src/pNN.txt (DSL court) en fragments/pNN.html pour DX.4."""
import re, os, glob, html
D = os.path.dirname(os.path.abspath(__file__))
def cit(t):
    return re.sub(r'\{\{([\w.\-]+)\}\}', lambda m: f'<sup class="r"><a href="#sb-{m.group(1)}">{m.group(1)}</a></sup>', t)
def btn(t, p):
    return re.sub(r'\[\[(\d+)\|([^\]]+)\]\]', lambda m: f'<button class="w" popovertarget="dx4-p{p}-f{m.group(1)}">{m.group(2)}</button>', t)
def inline(t, p):
    return btn(cit(t), p)
def table(lines, p):
    rows = [[c.strip() for c in l.strip().strip('|').split(' | ')] for l in lines]
    out = ['<div class="t" style="overflow-x:auto"><table>']
    out.append('<tr>' + ''.join(f'<th>{inline(c,p)}</th>' for c in rows[0]) + '</tr>')
    for r in rows[1:]:
        out.append('<tr>' + ''.join(f'<td>{inline(c,p)}</td>' for c in r) + '</tr>')
    out.append('</table></div>')
    return ''.join(out)
def blocks(text, p):
    res = []
    for b in re.split(r'\n\s*\n', text.strip()):
        b = b.strip()
        if not b: continue
        ls = b.split('\n')
        if b.startswith('#h4 '):
            res.append(f'<h4><em>{inline(b[4:], p)}</em></h4>')
        elif ls[0].startswith('|'):
            res.append(table(ls, p))
        elif ls[0].startswith('- '):
            res.append('<ul>' + ''.join(f'<li>{inline(l[2:], p)}</li>' for l in ls) + '</ul>')
        else:
            res.append(f'<div class="p">{inline(" ".join(ls), p)}</div>')
    return ''.join(res)
def convert(src, p):
    # fenêtres : ==N ... ==
    out = []
    parts = re.split(r'(?m)^==(\d*)\s*$', src)
    # parts: texte, num, contenu, '', texte...
    i = 0
    out.append(blocks(parts[0], p))
    i = 1
    while i < len(parts):
        num, content = parts[i], parts[i+1]
        nxt = parts[i+2] if i+2 < len(parts) else ''
        out.append(f'<div id="dx4-p{p}-f{num}" popover class="fenetre">{blocks(content, p)}</div>')
        # parts[i+2] est '' (marqueur fermant), puis texte suivant
        i += 2
        if i < len(parts):
            # marqueur fermant : num vide
            i += 1  # saute le num vide du marqueur de fermeture
            if i < len(parts):
                out.append(blocks(parts[i], p)); i += 1
    return '\n'.join(x for x in out if x)
if __name__ == '__main__':
    os.makedirs(os.path.join(D, 'fragments'), exist_ok=True)
    for f in sorted(glob.glob(os.path.join(D, 'src', 'p*.txt'))):
        n = int(re.search(r'p(\d+)', os.path.basename(f)).group(1))
        h = convert(open(f, encoding='utf8').read(), n)
        open(os.path.join(D, 'fragments', f'p{n:02d}.html'), 'w', encoding='utf8').write(h + '\n')
        print(n, len(h))
