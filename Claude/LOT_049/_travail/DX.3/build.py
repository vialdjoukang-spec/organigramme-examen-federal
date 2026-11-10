#!/usr/bin/env python3
"""src/pNN.txt -> fragments/pNN.html : [[id,id]] -> citations ; {{b:ID|libellé}} -> bouton fenêtre."""
import re, os, glob
os.makedirs('fragments', exist_ok=True)
def cit(m):
    return ''.join(f'<sup class="r"><a href="#sb-{i.strip()}">{i.strip()}</a></sup>' for i in m.group(1).split(','))
for f in sorted(glob.glob('src/p*.txt')):
    t = open(f, encoding='utf-8').read()
    t = re.sub(r'([.!?])((?:\[\[[^\]]+\]\])+)', r'\2\1', t)
    t = re.sub(r'\[\[([^\]]+)\]\]', cit, t)
    t = re.sub(r'\{\{b:([^|}]+)\|([^}]+)\}\}', lambda m: f'<button class="w" popovertarget="{m.group(1)}">{m.group(2)}</button>', t)
    t = t.replace('<div class="t">','<div class="t" style="overflow-x:auto">')
    open('fragments/' + os.path.basename(f).replace('.txt', '.html'), 'w', encoding='utf-8').write(t)
