"""Mise en forme seulement ; faits rédigés depuis le paquet relu."""
from pathlib import Path
from html import escape
import json, re

ROOT = Path(__file__).resolve().parent
ALIASES = json.loads((ROOT/'ALIASES_SOURCES.json').read_text())

class Point:
    def __init__(self, n):
        self.n, self.parts, self.faits, self.fenetres = n, [], 0, 0
    def fait(self, texte, refs):
        refs = [refs] if isinstance(refs, str) else refs
        assert refs and all(r in ALIASES for r in refs), (texte, refs)
        cit = ''.join(f'<sup class="r"><a href="#sb-{ALIASES[r]}">{ALIASES[r]}</a></sup>' for r in refs)
        self.faits += 1
        phrases = re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])', texte)
        contenu = ' '.join(escape(ph)+cit for ph in phrases)
        return f'<div class="p" id="pa-p{self.n}-fait{self.faits}">{contenu}</div>\n'
    def p(self, texte, refs):
        self.parts.append(self.fait(texte, refs))
    def h(self, titre):
        self.parts.append(f'<h4>{escape(titre)}</h4>\n')
    def tableau(self, titres, lignes):
        out = '<div class="t"><table><thead><tr>'+''.join(f'<th>{escape(x)}</th>' for x in titres)+'</tr></thead><tbody>\n'
        for row in lignes:
            assert len(row)==len(titres)
            out += '<tr>'+''.join('<td>'+self.fait(t, refs)+'</td>\n' for t, refs in row)+'</tr>\n'
        self.parts.append(out+'</tbody></table></div>\n')
    def fenetre(self, titre, paragraphes):
        self.fenetres += 1
        ident = f'pa-p{self.n}-fen{self.fenetres}'
        out = f'<h4><button class="w" popovertarget="{ident}">{escape(titre)}</button></h4>\n'
        out += f'<div id="{ident}" popover class="fenetre"><h4>{escape(titre)}</h4>\n'
        out += ''.join(self.fait(t, refs) for t, refs in paragraphes)
        self.parts.append(out+'</div>\n')
    def sauver(self):
        d=ROOT/'fragments';d.mkdir(exist_ok=True)
        dest=d/f'p{self.n:02d}.html'
        assert not dest.exists(), 'Pas de réécriture spontanée d’un fragment reçu'
        s=''.join(self.parts);dest.write_text(s)
        print(self.n,len(s.encode()),self.faits,self.fenetres)
