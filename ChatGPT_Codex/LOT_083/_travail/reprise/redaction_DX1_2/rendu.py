from pathlib import Path
import html,json,re

def outils(numero,point):
    base=Path(__file__).resolve().parent/f'DX.{numero}'
    paquet=json.loads((base/'paquet.json').read_text())
    ids={x['id']for x in paquet['passages']}
    fen=[]
    compteur=0
    def c(*refs):
        assert refs
        assert set(refs)<=ids,set(refs)-ids
        return ''.join('<sup class="r"><a href="#sb-'+r+'">'+r+'</a></sup>'for r in refs)
    def p(t,*refs):
        nonlocal compteur
        compteur+=1
        if refs:
            # Une citation après chaque phrase du même paragraphe, toutes issues des références indiquées.
            morceaux=re.split(r'(?<=[.!?])\s+(?=[A-ZÀÂÉÈÊÎÔÙÜÇ])',t)
            t=' '.join(x+c(*refs)for x in morceaux)
        return f'<div class="p" id="dx{numero}-p{point}-f{compteur}">'+t+'</div>\n'
    def h(t):return '<h4>'+html.escape(t)+'</h4>\n'
    def w(t,paragraphes):
        ident=f'dx{numero}-p{point}-w{len(fen)+1}'
        contenu=''.join(p(txt,*refs)for txt,refs in paragraphes)
        fen.append('<div class="fenetre" id="'+ident+'" popover>\n'+h(t)+contenu+'</div>\n')
        return '<button class="w" popovertarget="'+ident+'">'+html.escape(t)+'</button>'
    def table(titres,lignes):
        return '<div class="t" style="overflow-x:auto"><table><thead><tr>'+''.join('<th>'+html.escape(x)+'</th>'for x in titres)+'</tr></thead><tbody>\n'+''.join('<tr>'+''.join('<td>'+x+'</td>'for x in row)+'</tr>\n'for row in lignes)+'</tbody></table></div>\n'
    def liste(lignes):return '<ol>\n'+''.join('<li>'+t+c(*refs)+'</li>\n'for t,refs in lignes)+'</ol>\n'
    def save(t):
        f=base/'fragments'/f'p{point:02d}.html'
        assert not f.exists(),f
        f.write_text(t+''.join(fen));print(f.name,len(f.read_bytes()))
    return base,p,c,h,w,table,liste,save
