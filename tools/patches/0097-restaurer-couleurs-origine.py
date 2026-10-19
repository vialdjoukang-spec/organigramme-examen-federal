#!/usr/bin/env python3
"""Restaurer les couleurs d’origine, avant les demandes de fond bleu et de palette."""
import os,re,hashlib
from pathlib import Path
SCOPES='\n/* Fonds des zones de lecture : seuls les arrière-plans changent. */\n@media (prefers-color-scheme:light){\n:root:not([data-theme="dark"]) :is(.panel,#tip,#qp){--reading-bg:#eaf7fd}\n:root:not([data-theme="dark"]) .panel .m-it{background:var(--reading-bg)}\n}\n:root[data-theme="light"] :is(.panel,#tip,#qp){--reading-bg:#eaf7fd}\n:root[data-theme="light"] .panel .m-it{background:var(--reading-bg)}\n'
EXPECTED={'app-1.css': '26ba0fc7fa44e795fe6c812cfe2fdf5b8867c589e985fdb2530f99bd723a564a', 'app-2.css': '2ceb2b0fab015df9995db8fc28183756eb7d82fc074eb0b7c2e9e7b0216eb48e'}

def appliquer(css,name):
    assert hashlib.sha256(css.encode()).hexdigest()==EXPECTED[name]
    rules=re.findall(r'[^{}]*\{[^{}]*background:var\(--reading-bg,var\(--paper\)\)[^{}]*\}',css)
    assert len(rules)==(4 if name=='app-1.css' else 9)
    for rule in rules:
        assert css.count(rule)==1 and rule.count('background:var(--reading-bg,var(--paper))')==1
        css=css.replace(rule,rule.replace('background:var(--reading-bg,var(--paper))','background:var(--paper)',1),1)
    if name=='app-2.css':
        assert css.count(SCOPES)==1;css=css.replace(SCOPES,'',1)
        for a,b in [(':root{--bg:#eaf7fd;--paper:#ffffff;',':root{--bg:#fbfbf8;--paper:#ffffff;'),(':root{--bg:#eaf7fd}\n',':root{--bg:#fbfbf8} \n')]:
            assert css.count(a)==1;css=css.replace(a,b,1)
    return css

if __name__=='__main__':
    folder=Path(os.environ.get('STYLE_DIR','assets/style'))
    modified={name:appliquer((folder/name).read_text(),name) for name in EXPECTED}
    for name,css in modified.items():(folder/name).write_text(css)
