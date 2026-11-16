#!/usr/bin/env python3
"""Compile src_txt/pNN.txt (mini-balisage) -> fragments/pNN.html pour DX.9."""
import re, os, sys, html
D = os.path.dirname(os.path.abspath(__file__))
PRE = 'dx9'
MAP = {'F':'wda45ff','V':'wfbafca','B':'w26fe26','J':'w2a2fbf','W':'w257597','G':'w794e8a','H':'wf38a30','N':'wbe6886',
       'R':'wbe4079','AD':'w783af6','PH':'wb630cd','K':'w5146e9','S':'wc5f842','O':'w5bdf05','Q':'w762f21','D1':'w6b43e7','D2':'w677780','D3':'w96f255','D4':'w38bf2d',
       'D5':'wde0698','D6':'w052a32','X':'aips-58728','E':'aips-61549','L':'aips-65149','C':'aips-49456','Hp':'aips-46613','A':'aips-48313'}
def cite(m):
    out = ''
    for tok in m.group(1).split(','):
        tok = tok.strip(); k, n = tok.rsplit('-', 1); i = f'{MAP[k]}-{n}'
        out += f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
    return out
def inline(t, n, wins):
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'\[\[(.+?)\]\]', cite, t)
    t = re.sub(r'\{\{(.+?)\|(\w+)\}\}', lambda m: f'<button class="w" popovertarget="{PRE}-p{n}-f{m.group(2)}">{m.group(1)}</button>', t)
    return t
def comp(n):
    src = open(os.path.join(D, 'src_txt', f'p{n:02d}.txt'), encoding='utf-8').read().split('\n')
    out = []; ul = []; tb = []
    def flush():
        nonlocal ul, tb
        if ul:
            h = ''; cur = 0
            for (lv, x) in ul:
                if lv > cur:
                    h += '<ul>' * (lv - cur) if cur else '<ul>' * lv
                elif lv < cur:
                    h += '</li>' + '</ul></li>' * (cur - lv)
                elif cur:
                    h += '</li>'
                h += f'\n<li>{x}'; cur = lv
            h += '</li>' + '</ul></li>' * (cur - 1) + '</ul>'
            out.append(h); ul = []
        if tb:
            rows = []
            for i, r in enumerate(tb):
                tag = 'th' if i == 0 else 'td'
                rows.append('<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in r) + '</tr>')
            out.append('<div class="t" style="overflow-x:auto"><table>\n' + '\n'.join(rows) + '\n</table></div>'); tb = []
    for ln in src:
        if not ln.strip() or ln.startswith('#'): continue
        k, _, rest = ln.partition(' ')
        if not k.startswith('L'):
            if ul: flush()
        if k != 'T':
            if tb: flush()
        if k == 'P': out.append(f'<div class="p">{inline(rest, n, None)}</div>')
        elif k == 'H': out.append(f'<h4><em>{inline(rest, n, None)}</em></h4>')
        elif k.startswith('L'): ul.append((int(k[1:] or 1), inline(rest, n, None)))
        elif k == 'T': tb.append([inline(c.strip(), n, None) for c in rest.split(' | ')])
        elif k == 'W':
            wid, _, body = rest.partition(': ')
            paras = ''.join(f'<div class="p">{inline(x.strip(), n, None)}</div>' for x in body.split(' ¶ '))
            out.append(f'<div id="{PRE}-p{n}-f{wid}" popover class="fenetre">{paras}</div>')
        else: raise SystemExit(f'p{n}: balise inconnue {k}')
    flush()
    os.makedirs(os.path.join(D, 'fragments'), exist_ok=True)
    open(os.path.join(D, 'fragments', f'p{n:02d}.html'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
if __name__ == '__main__':
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else range(1, 15)):
        if os.path.exists(os.path.join(D, 'src_txt', f'p{n:02d}.txt')): comp(n)
