#!/usr/bin/env python3
"""Assemble des phrases citées pour LOT_052. Chaque nombre doit être dans l'extrait cité."""
import html, json, re, sys

NUM = re.compile(r'(?<![\w])(\d+(?:[.,’\' ]\d+)*(?:[.,]\d+)?)(?![\w])')
STRUCT = re.compile(r"\b(?:points?|DX\.?|rangs?|E|étapes?|îlots?|n°|LOT_?|Phase)\s*\d+(?:[.,]\d+)?", re.I)
VERBES = set("""est sont a ont fait font peut peuvent doit doivent reste restent devient deviennent va vont
semble semblent permet permettent signe signent oriente orientent impose imposent confirme confirment élimine
éliminent exclut excluent traite traitent associe associent survient surviennent provoque provoquent entraîne
entraînent exige exigent reçoit reçoivent touche touchent atteint atteignent dépasse dépassent varie varient
augmente augmentent diminue diminuent baisse baissent réduit réduisent favorise favorisent explique expliquent
précède précèdent suit suivent recherche recherchent mesure mesurent montre montrent révèle révèlent
définit définissent correspond correspondent comprend comprennent repose reposent consiste consistent
représente représentent constitue constituent nécessite nécessitent justifie justifient recommande recommandent
indique indiquent prescrit prescrivent administre administrent contre-indique évite évitent limite limitent
dure durent persiste persistent apparaît apparaissent disparaît disparaissent évolue évoluent aggrave aggravent
protège protègent prévient préviennent dépiste dépistent détecte détectent distingue distinguent sépare séparent
conduit conduisent mène mènent aboutit aboutissent cause causent déclenche déclenchent libère libèrent
active activent inhibe inhibent bloque bloquent stimule stimulent fixe fixent lie lient agit agissent
porte portent concerne concernent relève relèvent suffit suffisent vise visent faut était étaient
""".split())
VERBE_RE = re.compile(r"\b(?:\w+(?:ent|ait|aient|era|eront|erait|eraient|ise|isent|it|issent))\b", re.I)
PRONOM = re.compile(r"\b(?:il|elle|ils|elles|on|qui|cela|ce)\s+(?:ne\s+|n'|se\s+|s'|l'|le\s+|la\s+|les\s+|y\s+|en\s+)*\w+", re.I)
DOSE = re.compile(r'\b\d+(?:[.,]\d+)?\s?(?:mg|µg|mcg|UI|g(?=\s?(?:/kg|/j|/jour|par jour|toutes|i\.?v|IV|per os|p\.o)))(?!\s?/\s?(?:l|L|dl|dL|mmol))\b')


def nombres(s):
    out = set()
    for n in NUM.findall(s):
        n = re.sub(r'[’\' ]', '', n).replace(',', '.')
        out.add(re.sub(r'^0+(?=\d)', '', n))
    return out


def verbale(ph):
    mots = {m.lower() for m in re.findall(r"[\w'’-]+", ph)}
    return bool(mots & VERBES or PRONOM.search(ph) or VERBE_RE.search(ph))


class Moteur:
    def __init__(self, paquet_path):
        self.P = {x['id']: x['texte'] for x in json.load(open(paquet_path))['passages']}
        self.parts = {i: [] for i in range(1, 15)}
        self.fen = 0
        self.erreurs = []

    def _err(self, msg):
        self.erreurs.append(msg)

    def _cite(self, ids):
        return ''.join(f'<sup class="r"><a href="#sb-{i}">{i}</a></sup>' for i in ids)

    def _ids(self, texte, hints):
        nums = nombres(STRUCT.sub(' ', texte))
        hints = [h for h in hints if h in self.P]
        if not nums:
            if not hints:
                self._err('phrase factuelle sans extrait: ' + texte)
                return ['MANQUANT']
            return hints[:1]
        def couvre(ids):
            blob = ' '.join(self.P[i] for i in ids)
            return nums <= nombres(blob)
        for h in hints:
            if couvre([h]):
                return [h]
        if hints and couvre(hints):
            return list(hints)
        hits = [i for i, t in self.P.items() if nums <= nombres(t)]
        if hits:
            hits.sort(key=lambda i: (i not in hints, len(self.P[i])))
            return [hits[0]]
        self._err('nombre absent: ' + str(sorted(nums)) + ' :: ' + texte)
        return hints[:1] or ['MANQUANT']

    def S(self, point, texte, *hints):
        texte = re.sub(r'\s+', ' ', texte).strip()
        if not texte.endswith('.'):
            texte += '.'
        n = len(texte[:-1].split()) if False else len(texte.replace('.', '').split())
        # le point final ne compte pas comme mot
        mots = texte[:-1].split() if texte.endswith('.') else texte.split()
        if not 12 <= len(mots) <= 28:
            self._err(f'longueur {len(mots)} p{point}: {texte}')
        if not verbale(texte):
            self._err('non verbale: ' + texte)
        ids = self._ids(texte, hints)
        if DOSE.search(texte) and not any(i.startswith('aips') for i in ids):
            self._err('dose sans aips: ' + texte)
        safe = html.escape(texte[:-1], quote=False) + '.'
        # les boutons sont déjà dans le texte sous forme de marque [[id|libellé]]
        safe = self._boutons(safe)
        self.parts[point].append(f'<div class="p">{safe}{self._cite(ids)}</div>')
        return ids

    def _boutons(self, texte):
        def repl(m):
            return f'<button class="w" popovertarget="{m.group(1)}">{html.escape(m.group(2))}</button>'
        return re.sub(r'\[\[([\w-]+)\|([^\]]+)\]\]', repl, texte)

    def W(self, point, fid, titre, phrases):
        """phrases: list of (texte, *hints). Placée après les phrases du point, appelée explicitement."""
        self.fen += 1
        body = [f'<h4><strong>{html.escape(titre)}</strong></h4>']
        for item in phrases:
            texte, *hints = item
            texte = re.sub(r'\s+', ' ', texte).strip()
            if not texte.endswith('.'):
                texte += '.'
            mots = texte[:-1].split()
            if not 12 <= len(mots) <= 28:
                self._err(f'fenêtre longueur {len(mots)}: {texte}')
            if not verbale(texte):
                self._err('fenêtre non verbale: ' + texte)
            ids = self._ids(texte, hints)
            if DOSE.search(texte) and not any(i.startswith('aips') for i in ids):
                self._err('fenêtre dose sans aips: ' + texte)
            body.append(f'<p>{html.escape(texte[:-1])}{self._cite(ids)}.</p>')
        self.parts[point].append(f'<div id="{fid}" popover class="fenetre">{"".join(body)}</div>')

    def HTML(self, point, fragment):
        self.parts[point].append(fragment)

    def ecrire(self, dossier):
        import os
        os.makedirs(dossier, exist_ok=True)
        for i in range(1, 15):
            if not self.parts[i]:
                self._err(f'point {i} vide')
        if self.erreurs:
            print('\n'.join(self.erreurs))
            print(f'TOTAL {len(self.erreurs)} erreurs')
            raise SystemExit(1)
        for i in range(1, 15):
            open(os.path.join(dossier, f'p{i:02d}.html'), 'w', encoding='utf-8').write('\n'.join(self.parts[i]) + '\n')
        print('fragments', dossier, 'fenêtres', self.fen)
