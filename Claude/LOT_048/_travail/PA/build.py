#!/usr/bin/env python3
"""Préprocesseur LOT_048 PA : src/pNN.txt (mini-balisage) -> fragments/pNN.html.
Lignes : P texte | H4 texte | LI texte | SUB texte | TB / TH a|b / TR a|b / TE | WIN k texte (¶ sépare des paragraphes)
Citations : [[U127,U129]] ; fenêtre : <<k:libellé>> ; alias dans ALIAS."""
import re, os, sys, html

ALIAS = {'U': 'w2aac93-', 'A': 'w6e934f-', 'T': 'w3bd653-', 'E': 'w06ef11-', 'G': 'w2df0cf-', 'O': 'wc83488-', 'S': 'w30ee9d-',
         'K': 'w0a1251-', 'D': 'w7e05da-', 'L': 'wd122d9-', 'W': 'w745ce5-', 'Z': 'w3828cc-', 'Y': 'w587d73-', 'H': 'wda5da9-',
         'X': 'aips-55609-', 'J': 'aips-66999-', 'F': 'aips-49503-', 'C': 'aips-53668-', 'M': 'aips-56313-', 'P': 'aips-59834-',
         'B': 'aips-65165-', 'V': 'aips-57386-', 'Q': 'w395dcb-', 'N': 'wd1395b-', 'R': 'w96f064-', 'EE': 'w0cbb91-', 'I': 'w6e934f-'}
KEYS = sorted(ALIAS, key=len, reverse=True)
D = os.path.dirname(os.path.abspath(__file__))


def ident(tok):
    for k in KEYS:
        if tok.startswith(k) and tok[len(k):].isdigit():
            return ALIAS[k] + tok[len(k):]
    raise SystemExit('alias inconnu : ' + tok)


def cites(txt):
    def rep(m):
        return ''.join(f'<sup class="r"><a href="#sb-{ident(t)}">{ident(t)}</a></sup>' for t in m.group(1).split(','))
    return re.sub(r'\[\[([^\]]+)\]\]', rep, txt)


def build(n):
    src = open(os.path.join(D, 'src', f'p{n:02d}.txt'), encoding='utf-8').read().split('\n')
    out, wins, ul, sub, tb = [], [], False, False, False
    pre = f'pa-p{n}-f'

    def close_lists():
        nonlocal ul, sub
        if sub:
            out.append('</ul>'); sub = False
        if ul:
            out.append('</ul>'); ul = False

    def flush():
        nonlocal wins
        for w in wins:
            out.append(w)
        wins = []

    for raw in src:
        l = raw.rstrip()
        if not l or l.startswith('#'):
            continue
        tag, _, rest = l.partition(' ')
        rest = rest.strip()
        if tag in ('P', 'H4', 'TB', 'TE') or tag == 'TH' or tag == 'TR':
            pass
        if tag == 'LI':
            if sub:
                out.append('</ul>'); sub = False
            elif ul:
                pass
            if not ul:
                flush(); out.append('<ul>'); ul = True
            else:
                out.append('')
            out.append(f'<li>{cites(rest)}')
            # fermeture différée : on met </li> si le suivant n'est pas SUB
            out.append('@@LI')
            continue
        if tag == 'SUB':
            # supprime le marqueur @@LI précédent (li reste ouvert)
            if not sub:
                out.append('<ul>'); sub = True
            out.append(f'<li>{cites(rest)}</li>')
            continue
        # tout autre marqueur ferme les listes
        if ul or sub:
            if sub:
                out.append('</ul>'); sub = False
            else:
                pass
            if ul:
                out.append('</ul>'); ul = False
        if tag == 'P':
            out.append(f'<div class="p">{cites(rest)}</div>')
            flush()
        elif tag == 'H4':
            out.append(f'<h4><em>{rest}</em></h4>')
        elif tag == 'TB':
            out.append('<div class="t" style="overflow-x:auto"><table>')
        elif tag == 'TH':
            out.append('<tr>' + ''.join(f'<th>{cites(c.strip())}</th>' for c in rest.split('|')) + '</tr>')
        elif tag == 'TR':
            out.append('<tr>' + ''.join(f'<td>{cites(c.strip())}</td>' for c in rest.split('|')) + '</tr>')
        elif tag == 'TE':
            out.append('</table></div>')
        elif tag == 'WIN':
            k, _, body = rest.partition(' ')
            paras = ''.join(f'<div class="p">{cites(x.strip())}</div>' for x in body.split('¶'))
            wins.append(f'<div id="{pre}{k}" popover class="fenetre">{paras}</div>')
        else:
            raise SystemExit(f'p{n}: marqueur inconnu {tag!r} dans {l[:60]}')
    if sub:
        out.append('</ul>')
    if ul:
        out.append('</ul>')
    flush()
    txt = '\n'.join(x for x in out if x != '')
    # fermeture des li laissés sans sous-liste
    txt = re.sub(r'@@LI\n?', '</li>\n', txt)
    # boutons de fenêtre
    txt = re.sub(r'<<(\w+):([^>]+)>>', lambda m: f'<button class="w" popovertarget="{pre}{m.group(1)}">{m.group(2)}</button>', txt)
    # une ligne ne dépasse pas 3000 caractères
    assert all(len(x) < 3000 for x in txt.split('\n')), f'p{n}: ligne > 3000'
    os.makedirs(os.path.join(D, 'fragments'), exist_ok=True)
    open(os.path.join(D, 'fragments', f'p{n:02d}.html'), 'w', encoding='utf-8').write(txt + '\n')
    return len(txt.encode())


if __name__ == '__main__':
    tot = 0
    for n in range(1, 15):
        if os.path.exists(os.path.join(D, 'src', f'p{n:02d}.txt')):
            b = build(n); tot += b
            print(f'p{n:02d}: {b} o')
    print('total fragments', tot)
