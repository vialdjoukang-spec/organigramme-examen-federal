"""Normaliseur numérique robuste (FR/DE/EN) + comparaison à arrondi près.
Corrige le bug historique « 0,4 » lu « .4 » : la virgule décimale n'est jamais un séparateur de token."""
import re, unicodedata
from dataclasses import dataclass, field

ESP = '\u00a0\u202f\u2009\u2007 '
UNITES = [  # (regex, unité canonique, facteur vers l'unité canonique)
    (r'(?:/|pour|par|per)\s*100[\s\'’.,\u00a0\u202f]*000\b', 'pour 100 000', 1.0),
    (r'(?:/|pour|par|per)\s*10[\s\'’.,\u00a0\u202f]*000\b', 'pour 100 000', 10.0),
    (r'(?:/|pour|par|per)\s*1[\s\'’.,\u00a0\u202f]*000(?!\s*000)\b', 'pour 100 000', 100.0),
    (r'‰', 'pour 100 000', 100.0),
    (r'%|pour\s*cent|pourcent', '%', 1.0),
]

@dataclass
class Valeur:
    bas: float
    haut: float
    unite: str = ''
    qualif: str = ''          # '~', '<', '>', '≤', '≥', ''
    decimales: int = 0
    brut: str = ''
    def tol(self):
        """Tolérance d'arrondi : une demi-unité de la dernière décimale affichée."""
        return 0.5 * 10 ** (-self.decimales)

NUM = r'\d{1,3}(?:[\s\'’\u00a0\u202f\u2009](?=\d{3}\b)\d{3})+(?:[.,]\d+)?|\d+(?:[.,]\d+)?'

def _num(tok):
    """'17 690' -> (17690,0) ; '0,4' -> (0.4,1) ; "1'240" -> (1240,0) ; '2.5' -> (2.5,1)."""
    t = re.sub(f'[{ESP}\'’]', '', tok)
    if ',' in t and '.' in t:                      # 1.234,5 ou 1,234.5
        if t.rfind(',') > t.rfind('.'): t = t.replace('.', '').replace(',', '.')
        else: t = t.replace(',', '')
    elif ',' in t:
        ent, dec = t.split(',', 1)
        t = ent + '.' + dec if len(dec) != 3 or ent == '0' else ent + dec   # « 0,400 » reste décimal
    elif '.' in t:
        ent, dec = t.split('.', 1)
        if len(dec) == 3 and ent != '0' and len(ent) <= 3 and re.search(r'\.\d{3}\.', tok + '.') is None and False:
            t = ent + dec
    dec = len(t.split('.')[1]) if '.' in t else 0
    return float(t), dec

def parse(s):
    """Retourne une Valeur ou None. Gère fourchettes (« 30 à 40 % », « 3–10 »), ~ < > ≤ ≥, unités."""
    if s is None: return None
    s0 = unicodedata.normalize('NFC', str(s)).strip()
    s1 = s0.replace('−', '-').replace('–', '-').replace('—', '-')
    q = ''
    m = re.match(r'\s*(~|≈|env\.?|environ|ca\.?|<|>|≤|≥|<=|>=|moins de|plus de)\s*', s1, re.I)
    if m:
        k = m.group(1).lower()
        q = {'≈': '~', 'env': '~', 'env.': '~', 'environ': '~', 'ca': '~', 'ca.': '~', '<=': '≤', '>=': '≥',
             'moins de': '<', 'plus de': '>'}.get(k, k)
        s1 = s1[m.end():]
    nums = list(re.finditer(NUM, s1))
    if not nums: return None
    a, da = _num(nums[0].group())
    b, db = a, da
    if len(nums) > 1:
        entre = s1[nums[0].end():nums[1].start()]
        if re.fullmatch(r'\s*(-|à|a|to|bis|et)\s*', entre, re.I):
            b, db = _num(nums[1].group())
    reste = s1[nums[0].end():]
    unite, f = '', 1.0
    for rx, u, fac in UNITES:
        if re.search(rx, reste, re.I): unite, f = u, fac; break
    return Valeur(a * f, b * f, unite, q, max(da, db), s0)

def concorde(ref, obs, tol_rel=0.0):
    """ref, obs : Valeur. Concordant si unités compatibles et intervalles (élargis de la tolérance d'arrondi) se recoupent."""
    if ref is None or obs is None: return None
    if ref.unite and obs.unite and ref.unite != obs.unite: return False
    t = max(ref.tol(), obs.tol()) + tol_rel * max(abs(ref.haut), abs(obs.haut))
    if ref.qualif == '<': return obs.haut < ref.bas + t
    if ref.qualif == '>': return obs.bas > ref.haut - t
    return not (obs.bas > ref.haut + t or obs.haut < ref.bas - t)

def nombres(texte):
    """Tous les nombres d'un texte, sans casser « 0,4 » ni « 17 690 »."""
    return [(_num(m.group())[0], m.start()) for m in re.finditer(NUM, texte)]
