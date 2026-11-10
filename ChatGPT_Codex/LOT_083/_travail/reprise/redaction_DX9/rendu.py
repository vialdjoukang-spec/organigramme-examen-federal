from pathlib import Path
import json,html
BASE=Path(__file__).resolve().parent/'DX.9'
P={x['id']:x for x in json.loads((BASE/'paquet.json').read_text())['passages']}
def outils(n):
    fen=[];compteur=0
    def c(*ids):
        assert all(i in P for i in ids),ids
        return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)
    def p(t,*ids): return '<p class="p">'+t+c(*ids)+'</p>\n'
    def h(t): return '<h4>'+t+'</h4>\n'
    def w(t,paragraphes):
        nonlocal compteur
        compteur+=1;i=f'dx9-p{n}-w{compteur}'
        fen.append(f'<div class="fenetre" id="{i}" popover>\n'+h(t)+''.join(p(a,*b) for a,b in paragraphes)+'</div>\n')
        return f'<button class="w" popovertarget="{i}">{t}</button>'
    def table(entetes,lignes):
        return '<div style="overflow-x:auto">\n<table>\n<thead><tr>'+''.join('<th>'+t+'</th>' for t in entetes)+'</tr></thead>\n<tbody>\n'+''.join('<tr>\n'+''.join('<td>'+t+'</td>\n' for t in l)+'</tr>\n' for l in lignes)+'</tbody>\n</table>\n</div>\n'
    def liste(items):return '<ul>\n'+''.join('<li>'+t+'</li>\n' for t in items)+'</ul>\n'
    def save(s):
        f=BASE/'fragments'/f'p{n:02d}.html'
        assert not f.exists(),f
        f.write_text(s+'\n'+''.join(fen))
        print(f'{f.name}: {f.stat().st_size} octets')
    return p,c,h,w,table,liste,save
