#!/usr/bin/env python3
"""Compile src/pNN.txt (mini-langage) en fragments/pNN.html. Aucun contenu médical ici."""
import re, os, glob, sys
D = os.path.dirname(os.path.abspath(__file__))
PRE = {  # alias -> identifiant de source du paquet
 'eu': 'w06ef11', 'u': 'w3bd653', 'j': 'aips-66999', 'd': 'aips-66649', 'nx': 'aips-55609', 'a': 'w2aac93',
 'r': 'w81dc83', 's': 'w79d85d', 'h': 'w793a21', 'c': 'w2356b3', 'f': 'w3bd1ac', 'v': 'w716208', 'm': 'w5c3b07',
 't': 'w1575d8', 'e': 'w37d3cc', 'o': 'waa837e', 'g': 'w2df0cf', 'ac': 'w6e934f', 'n': 'w7e05da',
 'vd': 'wccae35', 'dl': 'wcc015a', 'im': 'w0f5495', 'pp': 'w21619c', 'bo': 'wdf8b7a', 'bm': 'w9e125a',
 'du': 'wb864a3', 'dn': 'w9bb45e', 'rm': 'wfe8689', 'zk': 'w3828cc', 'ps': 'w587d73', 'es': 'w395dcb',
 'ug': 'we8cc9f', 'ge': 'w6e934f', 'ro': 'w7e05da',
}
def ident(tok):
    tok = tok.strip()
    if '-' in tok:
        return tok
    m = re.fullmatch(r'([a-z]+)(\d+)', tok)
    if not m or m.group(1) not in PRE:
        sys.exit(f'alias inconnu : {tok}')
    return f'{PRE[m.group(1)]}-{m.group(2)}'
def cite(m):
    return ''.join(f'<sup class="r"><a href="#sb-{ident(i)}">{ident(i)}</a></sup>' for i in m.group(1).split(','))
def compile_point(n, txt):
    out, lis, intable = [], [], False
    def flush():
        nonlocal lis
        if lis:
            out.append('<ul>' + ''.join(f'<li>{x}</li>' for x in lis) + '</ul>'); lis = []
    for line in txt.split('\n'):
        s = line.rstrip()
        if not s or s.startswith('#'):
            continue
        if s.startswith('LI '):
            lis.append(s[3:]); continue
        flush()
        if s.startswith('P '): out.append(f'<div class="p">{s[2:]}</div>')
        elif s.startswith('H '): out.append(f'<h4><em>{s[2:]}</em></h4>')
        elif s == 'T': out.append('<div class="t" style="overflow-x:auto"><table>')
        elif s == 'T/': out.append('</table></div>')
        elif s.startswith('RH '):
            out.append('<tr>' + ''.join(f'<th>{c.strip()}</th>' for c in s[3:].split(' | ')) + '</tr>')
        elif s.startswith('R '):
            out.append('<tr>' + ''.join(f'<td>{c.strip()}</td>' for c in s[2:].split(' | ')) + '</tr>')
        elif s.startswith('%%/'): out.append('</div>')
        elif s.startswith('%% '): out.append(f'<div id="dx3-p{n}-{s[3:].strip()}" popover class="fenetre">')
        else: sys.exit(f'ligne non reconnue (p{n}) : {s[:60]}')
    flush()
    t = '\n'.join(out)
    t = re.sub(r'\^([^^]+)\^', cite, t)
    t = re.sub(r'@@(\w+)\|([^@]+)@@', lambda m: f'<button class="w" popovertarget="dx3-p{n}-{m.group(1)}">{m.group(2)}</button>', t)
    return t + '\n'
os.makedirs(D + '/fragments', exist_ok=True)
for f in sorted(glob.glob(D + '/src/p*.txt')):
    n = int(re.search(r'p(\d+)', os.path.basename(f)).group(1))
    open(f'{D}/fragments/p{n:02d}.html', 'w', encoding='utf-8').write(compile_point(n, open(f, encoding='utf-8').read()))
