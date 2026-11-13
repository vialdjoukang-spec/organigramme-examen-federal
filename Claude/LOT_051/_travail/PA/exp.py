import re, os, sys, html
D = os.path.dirname(os.path.abspath(__file__))
def cit(m):
    return ''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(','))
def inline(s, n):
    s = re.sub(r'\s*\{([\w\-, ]+)\}', cit, s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'\[\[(f\d+)\|(.+?)\]\]', lambda m: f'<button class="w" popovertarget="pa-p{n}-{m.group(1)}">{m.group(2)}</button>', s)
    return s
def nest(L, n):
    h = ''; cur = -1
    for l in L:
        d = (len(l) - len(l.lstrip())) // 2
        txt = inline(l.strip()[2:].strip(), n)
        if d > cur:
            h += '<ul><li>' * (d - cur) if cur >= 0 else '<ul>' * (d + 1) + '<li>'
            if cur >= 0: pass
        elif d == cur:
            h += '</li><li>'
        else:
            h += '</li></ul>' * (cur - d) + '</li><li>'
        h += txt; cur = d
    return h + '</li></ul>' * (cur + 1)
def conv(n):
    src = open(f'{D}/src/p{n:02d}.txt', encoding='utf-8').read()
    out = []
    for blk in re.split(r'\n\s*\n', src.strip()):
        L = blk.strip().split('\n')
        if L[0].startswith('# '):
            out.append(f'<h4><em>{html.escape(L[0][2:])}</em></h4>')
            L = L[1:]
            if not L: continue
        if L[0].startswith('@@'):
            m = re.match(r'@@(f\d+)\s+(.*)', ' '.join(L), re.S)
            paras = m.group(2).split('¶')
            out.append(f'<div id="pa-p{n}-{m.group(1)}" popover class="fenetre">' + ''.join(f'<div class="p">{inline(p.strip(), n)}</div>' for p in paras) + '</div>')
        elif L[0].startswith('* '):
            out.append(nest(L, n))
        elif L[0].startswith('|'):
            rows = [[c.strip() for c in l.strip().strip('|').split('|')] for l in L]
            t = '<div class="t" style="overflow-x:auto"><table><thead><tr>' + ''.join(f'<th>{inline(c, n)}</th>' for c in rows[0]) + '</tr></thead><tbody>'
            for r in rows[1:]:
                t += '<tr>' + ''.join(f'<td>{inline(c, n)}</td>' for c in r) + '</tr>'
            out.append(t + '</tbody></table></div>')
        else:
            out.append(f'<div class="p">{inline(" ".join(L), n)}</div>')
    open(f'{D}/fragments/p{n:02d}.html', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
for n in range(1, 15):
    if os.path.exists(f'{D}/src/p{n:02d}.txt'): conv(n)
