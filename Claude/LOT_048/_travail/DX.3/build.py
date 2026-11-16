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

sys.path.insert(0, '/home/user/organigramme-examen-federal/Claude/_outils')
import controle3 as _c
def _plain(x):
    return _c.texte(re.sub(r'\^([^^]+)\^', lambda m: ' ' + ' '.join(m.group(1).split(',')) + ' ', x))
def _mots(x):
    return len(_plain(x).split())
def decouper(par):
    """Un paragraphe de plus de 40 mots sans connecteur est coupé en paragraphes plus courts (mise en forme seule)."""
    if _mots(par) <= 40 or _c.CONNECT.search(_plain(par)):
        return [par]
    ph = re.split(r'(?<=[.!?\^])\s+(?=[A-ZÀ-Ý«])', par)
    out, cur = [], ''
    for s in ph:
        if cur and _mots(cur + ' ' + s) > 40:
            out.append(cur); cur = s
        else:
            cur = (cur + ' ' + s).strip()
    if cur: out.append(cur)
    return out
def compile_point(n, txt):
    out, lis, intable = [], [], False
    def flush():
        nonlocal lis
        if lis:
            h, lvl = '', 0
            for i_, (l_, x_) in enumerate(lis):
                if i_ == 0:
                    h += '<ul>' * l_; lvl = l_
                else:
                    h += '</li>'
                    while lvl < l_: h += '<li style="list-style:none"><ul>'; lvl += 1
                    while lvl > l_: h += '</ul></li>'; lvl -= 1
                h += f'<li>{x_}'
            h += '</li>'
            while lvl > 1: h += '</ul></li>'; lvl -= 1
            h += '</ul>'
            out.append(h); lis = []
    for line in txt.split('\n'):
        s = line.rstrip()
        if not s or s.startswith('#'):
            continue
        m_ = re.match(r'LI(\d?) ', s)
        if m_:
            lis.append((int(m_.group(1) or 1), s[len(m_.group(0)):])); continue
        flush()
        if s.startswith('P '): out.extend(f'<div class="p">{x}</div>' for x in decouper(s[2:]))
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
