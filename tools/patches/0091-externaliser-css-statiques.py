#!/usr/bin/env python3
"""Déplacer deux feuilles statiques, octet pour octet et au même ordre cascade."""
import os,re,hashlib
from pathlib import Path
STYLE_SHA256 = ['fcfc4c90133daaf0a27589d82713bf9e77de87728ce80ddf7dfceac9d25b8194', '5a3263e92c982ff9832c6fe753f7fc45b99887bbadfec382c5aa63a4d11ab239']

def appliquer(source, destination):
    styles=list(re.finditer(r'<style\b([^>]*)>(.*?)</style>',source,re.S))
    assert len(styles)==5, 'Cinq feuilles inline attendues avant ce patch'
    for ordinal,index in reversed(list(enumerate((0,4),1))):
        match=styles[index];assert not match[1].strip(), 'Seulement les feuilles anonymes statiques'
        css=match[2];assert hashlib.sha256(css.encode()).hexdigest()==STYLE_SHA256[ordinal-1]
        assert source.count(match[0])==1 and not re.search(r'url\s*\(',css,re.I)
        path=destination/('app-'+str(ordinal)+'.css');path.parent.mkdir(parents=True,exist_ok=True);path.write_text(css)
        source=source[:match.start()]+'<link rel="stylesheet" href="assets/style/'+path.name+'">'+source[match.end():]
    return source

if __name__=='__main__':
    path=Path(os.environ.get('APP_FILE','app_v2.html'))
    path.write_text(appliquer(path.read_text(),path.parent/'assets/style'))
