#!/usr/bin/env python3
"""Colorer les fonds de lecture, en préservant l’en-tête, la sauvegarde et les caractères."""
import hashlib,os,re
from pathlib import Path
EXPECTED={'app-1.css':'fcfc4c90133daaf0a27589d82713bf9e77de87728ce80ddf7dfceac9d25b8194','app-2.css':'6cbc95a99ac059f2b4f20feade1c63a6555faab57e46ea8221986d06411f7efe'}
SCOPES='''
/* Fonds des zones de lecture : seuls les arrière-plans changent. */
@media (prefers-color-scheme:light){
:root:not([data-theme="dark"]) :is(.panel,#tip,#qp){--reading-bg:#eaf7fd}
:root:not([data-theme="dark"]) .panel .m-it{background:var(--reading-bg)}
}
:root[data-theme="light"] :is(.panel,#tip,#qp){--reading-bg:#eaf7fd}
:root[data-theme="light"] .panel .m-it{background:var(--reading-bg)}
'''

def appliquer(css,name):
    assert hashlib.sha256(css.encode()).hexdigest()==EXPECTED[name], 'Feuille source inattendue'
    rules=re.findall(r'[^{}]*\{[^{}]*background:var\(--paper\)[^{}]*\}',css)
    assert rules and all(css.count(rule)==1 and rule.count('background:var(--paper)')==1 for rule in rules)
    for rule in rules:
        css=css.replace(rule,rule.replace('background:var(--paper)','background:var(--reading-bg,var(--paper))',1),1)
    assert 'background:var(--paper)' not in css
    return css+(SCOPES if name=='app-2.css' else '')

if __name__=='__main__':
    folder=Path(os.environ.get('STYLE_DIR','assets/style'))
    modified={name:appliquer((folder/name).read_text(),name) for name in EXPECTED}
    for name,css in modified.items():(folder/name).write_text(css)
