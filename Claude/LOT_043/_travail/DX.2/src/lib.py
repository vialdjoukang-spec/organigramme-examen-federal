import re, os, html as H
FR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'fragments')
CITE = re.compile(r'\[((?:w[0-9a-f]{5,6}|aips)-\d+(?:-\d+)?)\]')
def c(t):
    return CITE.sub(lambda m: f'<sup class="r"><a href="#sb-{m.group(1)}">{m.group(1)}</a></sup>', t)
DROP = {'hormones et attaques de panique','locus coeruleus','probabilité d\'infarctus selon la description de la douleur','signes vitaux et signaux d\'alarme','hyperventilation','critères du DSM-5 pour le trouble panique','prévalence selon le lieu de soins','scores de dépistage de la panique aux urgences','vignette de Monsieur D. aux HUG','agoraphobie','critères cognitifs qui orientent vers la panique'}
class Pt:
    def __init__(self, n):
        self.n = n; self.out = []; self.k = 0
    def p(self, text, *fens):
        """text contient {0},{1}... : boutons ; fens = [(label, [phrases...] ou html)]"""
        btns = []; pops = []
        for lab, body in fens:
            if lab in DROP:
                btns.append(lab); continue
            self.k += 1
            i = f'dx2-p{self.n}-f{self.k}'
            btns.append(f'<button class="w" popovertarget="{i}">{lab}</button>')
            if isinstance(body, (list, tuple)):
                body = '\n'.join(x if x.startswith('<') else f'<div class="p">{c(x)}</div>' for x in body)
            pops.append(f'<div id="{i}" popover class="fenetre">{body}</div>')
        t = c(text)
        for j, b in enumerate(btns): t = t.replace('{%d}' % j, b)
        self.out.append(f'<div class="p">{t}</div>' + ''.join('\n' + x for x in pops))
    def h(self, t): self.out.append(f'<h4><em>{t}</em></h4>')
    def ul(self, items): self.out.append('<ul>\n' + '\n'.join(f'<li>{c(x)}</li>' for x in items) + '\n</ul>')
    def raw(self, t): self.out.append(c(t))
    def table(self, head, rows):
        s = '<div class="t" style="overflow-x:auto"><table><thead><tr>' + ''.join(f'<th>{c(x)}</th>' for x in head) + '</tr></thead><tbody>'
        for r in rows: s += '\n<tr>' + ''.join(f'<td>{c(x)}</td>' for x in r) + '</tr>'
        self.out.append(s + '</tbody></table></div>')
    def save(self):
        os.makedirs(FR, exist_ok=True)
        open(os.path.join(FR, f'p{self.n:02d}.html'), 'w', encoding='utf-8').write('\n'.join(self.out) + '\n')
