#!/usr/bin/env python3
"""Externaliser trois constantes JSON pures d’interface, sans modifier leurs valeurs."""
import os,json,hashlib,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from _app import span
SHA256 = {'SESSION': '46238e121d462ee7544739a596187a774823cc7bb9d8690ee085f9b68d484080', 'EXI': '9bb24be63d5ee719663a0ac6c4b7d988dcb76c8a7dded883ba98927457473692', 'ATT': '81914d1fb6f03a5e21d7e78024d1d01abe96b8554a27a1494df736fe744aaa46'}
ANCHOR='<script>\nconst SSP='
TAG='<script src="assets/config/interface.js"></script>\n'

def appliquer(source,destination):
    assert source.count(ANCHOR)==1 and TAG not in source, 'Ancrage principal unique attendu'
    declarations=[]
    for name,digest in SHA256.items():
        a,b=span(source,name);value=source[a:b]
        json.loads(value)
        assert hashlib.sha256(value.encode()).hexdigest()==digest, 'Valeur attendue différente : '+name
        declaration='const '+name+'='+value+';'
        assert source.count(declaration)==1 and source[b:b+1]==';'
        declarations.append(declaration)
        source=source.replace(declaration,'',1)
    destination.parent.mkdir(parents=True,exist_ok=True)
    assert not destination.exists(), 'Ne pas écraser un fichier existant'
    destination.write_text('\n'+'\n'.join(declarations)+'\n')
    return source.replace(ANCHOR,TAG+ANCHOR,1)

if __name__=='__main__':
    target=Path(os.environ.get('APP_FILE','app_v2.html'))
    target.write_text(appliquer(target.read_text(),target.parent/'assets/config/interface.js'))
