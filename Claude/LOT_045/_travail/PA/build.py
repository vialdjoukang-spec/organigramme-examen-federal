#!/usr/bin/env python3
"""Expanse les macros de src/pNN.src en fragments/pNN.html : [c:SPLF-10,RMS14-4] ; {b:K|libellé} ; {W:K}…{/W}."""
import re, os, sys
ICI = os.path.dirname(os.path.abspath(__file__))
AL = dict(SPLF='w00cff1', RMS14='w32b496', NICE='wc115a2', ERS='wd8e55d', GRACE='w7fdfc0', HEMO='w498289', MASS='w0c7c16',
          MASSAB='wb9ff23', LIEGE='wb847e5', HUG='w2cc29e', SMJ='w91b1da', TA='w726701', TB='w2ceada', LRTI='w20c858',
          RMS25='w1d972f', GLOB='w1825ad', ESCPE='wf4ca70', PLAN='w9a1026')
def cit(m):
    out = ''
    for x in m.group(1).split(','):
        x = x.strip()
        if x.startswith('aips-'): i = x
        else:
            a, n = x.rsplit('-', 1); i = f'{AL.get(a, a)}-{n}'
        out += f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>'
    return out
for n in range(1, 15):
    f = os.path.join(ICI, 'src', f'p{n:02d}.src')
    if not os.path.exists(f): continue
    s = open(f, encoding='utf-8').read()
    s = re.sub(r'\s*\[c:([^\]]+)\]', cit, s)
    s = re.sub(r'\{b:(\w+)\|([^}]+)\}', lambda m: f'<button class="w" popovertarget="pa-p{n}-{m.group(1)}">{m.group(2)}</button>', s)
    s = re.sub(r'\{W:(\w+)\}', lambda m: f'<div id="pa-p{n}-{m.group(1)}" popover class="fenetre">', s)
    s = s.replace('{/W}', '</div>')
    s = s.replace('<div class="t"><table', '<div class="t" style="overflow-x:auto"><table')
    open(os.path.join(ICI, 'fragments', f'p{n:02d}.html'), 'w', encoding='utf-8').write(s)
print('ok')
