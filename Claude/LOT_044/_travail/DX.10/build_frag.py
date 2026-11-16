#!/usr/bin/env python3
"""Convertit src/pNN.txt (balisage compact) en fragments/pNN.html. Usage: build_frag.py"""
import re, os, html, glob
D = os.path.dirname(os.path.abspath(__file__))

import json
PAQ = json.load(open(os.path.join(D, 'paquet.json')))['passages']
ALIAS = {'smw':'w640bc0','esc':'esc2024aorte','jac':'w3d9b96','ccr':'w5aebf3','life':'wb8e178','chuv':'wf33277','herz':'w0da615','com':'w902ef3','rcm':'w606bef','hug':'wfba9d7','crev':'w930c2f','esc1':'w0095f9','smwab':'w79a30c','tra':'aips-41529','esm':'aips-65741','ura':'aips-66012','kap':'aips-53842','gen':'esc2024aorte_gen'}
def norm(t): return re.sub(r'\s+', ' ', re.sub('\u00ad\\s*','',t).replace('\u2019',"'").replace('\u2010','-')).lower()
NP = [(q['id'], norm(q['texte'])) for q in PAQ]
ERR = []
def resolve(spec):
    ids = []
    spec = html.unescape(spec)
    for part in spec.split(';;'):
        a, _, sn = part.partition(':')
        pre = ALIAS[a.strip()]; sn = norm(sn.strip())
        hit = [i for i, t in NP if i.startswith(pre + '-') and sn in t]
        if not hit:
            ERR.append(f'p?: {part}'); continue
        ids.append(hit[0])
    return list(dict.fromkeys(ids))
def esc(s): return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
def inline(s, n):
    s = esc(s)
    s = re.sub(r'\[\[(.+?)\]\]', lambda m: ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in resolve(m.group(1))), s)
    s = re.sub(r'\{\{(f\d+)\|([^}]+)\}\}', lambda m: f'<button class="w" popovertarget="dx10-p{n}-{m.group(1)}">{m.group(2)}</button>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'__([^_]+)__', r'<em>\1</em>', s)
    return s
def block(lines, n):
    out, ul, tb = [], False, False
    sub = False
    def close():
        nonlocal ul, tb, sub
        if sub: out.append('</ul></li>'); sub = False
        if ul: out.append('</ul>'); ul = False
        if tb: out.append('</table></div>'); tb = False
    for ln in lines:
        if not ln.strip(): continue
        k, _, rest = ln.partition(' ')
        if k == 'L2':
            if not sub:
                out[-1] = out[-1][:-5]; out.append('<ul>'); sub = True
            out.append(f'<li>{inline(rest, n)}</li>'); continue
        if k == 'L':
            if tb: close()
            if sub: out.append('</ul></li>'); sub = False
            if not ul: out.append('<ul>'); ul = True
            out.append(f'<li><p>{inline(rest, n)}</p></li>' if n == 10 else f'<li>{inline(rest, n)}</li>'); continue
        if k in ('T', 'R'):
            if ul: close()
            if not tb: out.append('<div class="t" style="overflow-x:auto"><table>'); tb = True
            cells = [c.strip() for c in rest.strip().strip('|').split('|')]
            tag = 'th' if k == 'T' else 'td'
            out.append('<tr>' + ''.join(f'<{tag}>{inline(c, n)}</{tag}>' for c in cells) + '</tr>'); continue
        close()
        if k == 'P': out.append(f'<div class="p">{inline(rest, n)}</div>')
        elif k == 'H': out.append(f'<h4><em>{inline(rest, n)}</em></h4>')
        else: raise SystemExit(f'ligne inconnue: {ln[:60]}')
    close()
    return ''.join(out)
for f in sorted(glob.glob(os.path.join(D, 'src', 'p*.txt'))):
    n = int(re.search(r'p(\d+)\.txt', f).group(1))
    main, wins, cur = [], [], None
    for ln in open(f, encoding='utf-8').read().split('\n'):
        if ln.startswith('F '):
            cur = [ln[2:].strip(), []]; continue
        if ln.strip() == '/F':
            wins.append(cur); cur = None; continue
        (cur[1] if cur else main).append(ln)
    # les fenêtres sont placées après le paragraphe qui les appelle
    body, pend = [], []
    wd = {w[0]: w for w in wins}
    html_out = ''
    # regroupe par paragraphe : on rend ligne à ligne puis insère les fenêtres appelées après le bloc contenant le bouton
    chunks, buf = [], []
    for ln in main:
        buf.append(ln)
    out = []
    i = 0
    rendered = block(main, n)
    # insertion: après chaque élément fermé contenant un bouton, ajouter ses fenêtres
    def win_html(wid):
        w = wd[wid]
        return f'<div id="dx10-p{n}-{wid}" popover class="fenetre">{block(w[1], n)}</div>'
    parts = re.split(r'(?<=</div>)|(?<=</ul>)|(?<=</li>)', rendered)
    # simple : on repère les boutons dans le HTML rendu élément par élément
    elems = re.findall(r'<div class="p">.*?</div>|<h4>.*?</h4>|<ul>.*</ul>(?=<div|<h4|$)|<div class="t".*?</table></div>', rendered, re.S)
    res = ''
    for e in elems:
        res += e
        for wid in re.findall(r'popovertarget="dx10-p%d-(f\d+)"' % n, e):
            res += win_html(wid)
    open(os.path.join(D, 'fragments', f'p{n:02d}.html'), 'w', encoding='utf-8').write(res)
    unused = [w for w in wd if f'popovertarget="dx10-p{n}-{w}"' not in res]
    if unused: print('fenêtres non appelées', n, unused)
print('ok'); 
if ERR:
    print('\n'.join(ERR)); raise SystemExit(1)
