#!/usr/bin/env python3
# Convertit src/pNN.txt (macros [[ALIAS.n]], <<k|libellé>>, @@k corps @@) en fragments/pNN.html
import re, os, sys
A = dict(R14='w32b496', R26='w74d830', R23='w86b96b', R25='w1d972f', E20='wd8e55d', CV='w522ffd', NB='w2de1ee',
         RT='wc8a97f', CO='w9c2a0a', MK='w2f3e3e', MB='wc1814e', FN='w975f25', MC='w9c9190', G22='w4f25d2', G24='we048d4',
         SY='aips-55568', FO='aips-66747', LU='aips-59341', MM='aips-62361', PR='aips-69640', SP='w00cff1', NI='wc115a2')
D = os.path.dirname(os.path.abspath(__file__))
os.makedirs(f'{D}/fragments', exist_ok=True)
for n in range(1, 15):
    f = f'{D}/src/p{n:02d}.txt'
    if not os.path.exists(f): continue
    s = open(f, encoding='utf-8').read()
    s = re.sub(r'([.!?])((?:\[\[[A-Z0-9]+\.\d+\]\])+)', r'\2\1', s)
    s = re.sub(r'\[\[([A-Z0-9]+)\.(\d+)\]\]', lambda m: f'<sup class="r"><a href="#sb-{A[m.group(1)]}-{m.group(2)}">{A[m.group(1)]}-{m.group(2)}</a></sup>', s)
    s = re.sub(r'<<(\w+)\|(.*?)>>', lambda m: f'<button class="w" popovertarget="dx4-p{n}-f{m.group(1)}">{m.group(2)}</button>', s)
    s = re.sub(r'@@(\w+)\s(.*?)@@', lambda m: f'<div id="dx4-p{n}-f{m.group(1)}" popover class="fenetre">{m.group(2).strip()}</div>', s, flags=re.S)
    s = re.sub(r'[ \t]*\n[ \t]*', '\n', s).strip() + '\n'
    open(f'{D}/fragments/p{n:02d}.html', 'w', encoding='utf-8').write(s)
