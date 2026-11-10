"""Rendu de fragments ; aucune génération de faits ni notation clinique."""
from html import escape
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


class Point:
    def __init__(self, numero):
        self.numero = numero
        self.texte = []
        self.faits = 0
        self.fenetres = 0
        self.ids_sources = {x['id'] for x in json.loads((ROOT / 'paquet.json').read_text())['passages']}

    def fait(self, texte, refs):
        if isinstance(refs, str):
            refs = [refs]
        assert refs and set(refs) <= self.ids_sources, (texte, refs)
        self.faits += 1
        citations = ''.join(f'<sup class="r"><a href="#sb-{escape(x)}">{escape(x)}</a></sup>' for x in refs)
        return f'<div class="p" id="pa-p{self.numero}-fait{self.faits}">{escape(texte)}{citations}</div>\n'

    def p(self, texte, refs):
        self.texte.append(self.fait(texte, refs))

    def h(self, texte):
        self.texte.append(f'<h4>{escape(texte)}</h4>\n')

    def tableau(self, titres, lignes):
        out = '<div class="t"><table><thead><tr>'
        out += ''.join(f'<th>{escape(x)}</th>' for x in titres) + '</tr></thead><tbody>'
        for ligne in lignes:
            assert len(ligne) == len(titres)
            out += '<tr>' + ''.join('<td>' + self.fait(t, r) + '</td>' for t, r in ligne) + '</tr>\n'
        self.texte.append(out + '</tbody></table></div>\n')

    def fenetre(self, titre, paragraphes):
        self.fenetres += 1
        ident = f'pa-p{self.numero}-fen{self.fenetres}'
        out = f'<h4><button class="w" popovertarget="{ident}">{escape(titre)}</button></h4>\n'
        out += f'<div id="{ident}" popover class="fenetre"><h4>{escape(titre)}</h4>\n'
        out += ''.join(self.fait(t, r) for t, r in paragraphes)
        self.texte.append(out + '</div>\n')

    def sauver(self):
        dest = ROOT / 'fragments'
        dest.mkdir(exist_ok=True)
        (dest / f'p{self.numero:02d}.html').write_text(''.join(self.texte))
        print(self.numero, self.faits, self.fenetres, len(''.join(self.texte).encode()))
