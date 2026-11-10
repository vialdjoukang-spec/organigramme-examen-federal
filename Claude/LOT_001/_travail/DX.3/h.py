# Aides de rédaction DX.3 : citations, paragraphes, fenêtres, tableaux. Aucun contenu médical ici.
import html as _h

def c(*ids):
    return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)

def S(txt, *ids):
    """Phrase : texte + citation(s) + point final (la citation précède le point)."""
    end = '' if txt[-1] in '.!?' else '.'
    return txt + c(*ids) + end

class Pt:
    def __init__(self, n):
        self.n = n
        self.k = 0
        self.pending = []

    def w(self, label, *paras):
        """Bouton de fenêtre à insérer dans une phrase ; paras = liste de <div class="p">."""
        self.k += 1
        i = f'dx3-p{self.n}-f{self.k}'
        self.pending.append(f'<div id="{i}" popover class="fenetre">' + ''.join(paras) + '</div>')
        return f'<button class="w" popovertarget="{i}">{label}</button>'

    def P(self, *ph):
        out = '<div class="p">' + ' '.join(ph) + '</div>'
        if self.pending:
            out += ''.join(self.pending)
            self.pending = []
        return out

def fp(*ph):
    """Paragraphe pour l'intérieur d'une fenêtre."""
    return '<div class="p">' + ' '.join(ph) + '</div>'

def H4(t):
    return f'<h4><em>{t}</em></h4>'

def UL(*items):
    return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'

def T(heads, rows):
    h = '<tr>' + ''.join(f'<th>{x}</th>' for x in heads) + '</tr>'
    r = ''.join('<tr>' + ''.join(f'<td>{x}</td>' for x in row) + '</tr>' for row in rows)
    return f'<div class="t" style="overflow-x:auto"><table>{h}{r}</table></div>'
