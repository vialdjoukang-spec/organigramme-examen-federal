#!/usr/bin/env python3
"""CONTROLE3 — contrôle gratuit (zéro modèle) des 3 axes d'un HTML de cours.

  A. VÉRACITÉ : tout nombre d'une phrase citée figure mot pour mot dans l'extrait cité ;
                toute phrase chiffrée porte une citation ; toute citation existe dans le paquet ;
                toute phrase de dose cite un extrait AIPS.
  B. LANGUE   : phrase verbale (verbe conjugué), connecteur logique par paragraphe, 8–32 mots,
                zéro phrase dupliquée (dans le fichier et entre fichiers du même lot).
  C. FORME    : points attendus présents, FIN_FICHIER, aucun title=, aucun <script>, tableaux enveloppés,
                balises équilibrées, bande d'octets.

Usage :
  python3 controle3.py FICHIER.html [FICHIER2.html ...] --paquet paquet.json [--points 14] [--min 100000 --max 200000]
Sortie : JSON par fichier (verdict VERT/ORANGE/ROUGE + défauts localisés) ; code 0 si aucun ROUGE.
"""
import re, sys, json, html, hashlib, argparse, collections

CIT = re.compile(r'<sup class="r"><a href="#sb-([\w.\-:]+)">')
NUM = re.compile(r'(?<![\w])(\d+(?:[.,’\' ]\d+)*(?:[.,]\d+)?)(?![\w])')
DOSE = re.compile(r'\b\d+(?:[.,]\d+)?\s?(?:mg|µg|mcg|UI|g(?=\s?(?:/kg|/j|/jour|par jour|toutes|i\.?v|IV|per os|p\.o)))(?!\s?/\s?(?:l|L|dl|dL|mmol))\b')
CONNECT = re.compile(r"\b(car|donc|or|ainsi|puis|alors|parce que|puisque|lorsque|quand|si|tandis que|alors que|"
                     r"afin de|afin que|pour que|de sorte que|c'est pourquoi|en effet|cependant|toutefois|"
                     r"néanmoins|par conséquent|dès lors|ensuite|enfin|d'abord|en revanche|ce qui|"
                     r"grâce à|à cause de|en raison de|si bien que|de ce fait|par ailleurs|en outre|"
                     r"autrement dit|c'est-à-dire|d'où|puisqu'|lorsqu'|qu'il)\b", re.I)
# Formes verbales conjuguées fréquentes en rédaction médicale (3e pers., présent/futur/passé composé)
VERBES = set("""propose proposent recommande recommandent conseille conseillent mentionne mentionnent contient contiennent figure figurent résulte résultent ajoute ajoutent dépend dépendent rassemble rassemblent résume résument précise précisent indique indiquent décrit décrivent est sont a ont fait font peut peuvent doit doivent reste restent devient deviennent va vont
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
s'accompagne s'accompagnent s'associe s'explique s'élève se manifeste se manifestent se traduit se traduisent
se définit se recherche se mesure se prescrit se discute se pose s'impose s'observe s'installe se complique
remplace remplacent précise précisent compte comptent atteste attestent rappelle rappellent signale signalent
pose posent écarte écartent retient retiennent ordonne ordonnent adapte adaptent surveille surveillent
contrôle contrôlent corrige corrigent restaure restaurent normalise normalise prolonge prolongent
était étaient avait avaient sera seront aura auront serait seraient pourrait pourraient devrait devraient
faut suffit suffisent vise visent cible ciblent porte portent concerne concernent relève relèvent
""".split())
VERBE_RE = re.compile(r"\b(?:\w+(?:ent|ait|aient|era|eront|erait|eraient|ise|isent|it|issent))\b", re.I)
PRONOM_VERBE = re.compile(r"\b(?:il|elle|ils|elles|on|qui|cela|ce|celle-ci|celui-ci)\s+(?:ne\s+|n'|se\s+|s'|l'|le\s+|la\s+|les\s+|y\s+|en\s+)*\w+", re.I)
STRUCT = re.compile(r"\b(?:points?|DX\.?|rangs?|E|étapes?|îlots?|n°|LOT_?|Phase)\s*\d+(?:[.,]\d+)?|\b[A-Z]\d{2}(?:\.\d{1,2})?\b|\bCIM-1[01]\b|\b(?:le|au|du|appeler le)\s+14[0-9]\b|\binterleukine[- ]\d+\b|\bIL-\d+\b", re.I)
SOURCES = re.compile(r'<section\b[^>]*id="[\w-]*sources"[^>]*>.*?</section>|<details\b[^>]*class="refs"[^>]*>.*?</details>', re.S | re.I)
TAG_SS = re.compile(r'<(script|style)\b[^>]*>.*?</\1>', re.S | re.I)
VIDES = {'br', 'hr', 'img', 'meta', 'link', 'input', 'source', 'col', 'wbr', 'area', 'base', 'embed', 'track', 'param'}


def texte(fragment):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', fragment))).strip()


def nombres(s):
    out = set()
    for n in NUM.findall(s):
        n = re.sub(r'[’\' ]', '', n).replace(',', '.')
        out.add(re.sub(r'^0+(?=\d)', '', n))  # « 07 » et « 7 » désignent le même nombre
    return out


def nombres_source(s):
    """Correctif local (Claude/_outils) : dans un extrait, des nombres de colonnes voisines séparés par une espace
    (« 0 0.35 0.21 », « 98 8.1 ») sont fusionnés par NUM ; on ajoute aussi chaque nombre pris isolément. Le contrôle
    reste strict : le nombre de la phrase doit figurer tel quel dans l'extrait cité."""
    out = nombres(s)
    for tok in re.split(r'[\s\u00a0\u202f]+', s):
        out |= nombres(tok)
    for n in re.findall(r'\b\d{1,3}(?:,\d{3})+\b', s):  # séparateur de milliers anglais (« 149,238 »)
        out.add(n.replace(',', ''))
    for n in re.findall(r'\b\d+\u00b7\d+\b', s):  # point médian décimal du Lancet (« 70·8 »)
        out |= nombres(' ' + n.replace('\u00b7', ',') + ' ') | nombres(' ' + n.replace('\u00b7', '.') + ' ')
    for n in re.findall(r'\d+(?:[.,]\d+)?', s):  # nombres collés à un glyphe OCR (« >_80 », « e8.5 »)
        out |= nombres(' ' + n + ' ')
    return out


def est_verbale(ph):
    mots = {m.lower() for m in re.findall(r"[\w'’-]+", ph)}
    return bool(mots & VERBES or PRONOM_VERBE.search(ph) or VERBE_RE.search(ph))


def phrases_html(h):
    """Découpe les blocs textuels (p, li, td, div.p, dd) en phrases ; conserve le HTML brut pour les citations."""
    blocs = re.findall(r'<(p|li|td|dd|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|li|td|dd|div)>', h, re.S | re.I)
    out = []
    for tag, b in blocs:
        for brut in re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])', b):
            t = texte(re.sub(r'<sup class="r">.*?</sup>', '', brut, flags=re.S))  # l'étiquette de citation n'est pas du texte
            if len(t.split()) >= 4:
                out.append((tag, brut, t))
    return out


def equilibre(h):
    pile = []
    for ferme, nom in re.findall(r'<(/?)([a-zA-Z][\w-]*)\b[^>]*?(?<!/)>', TAG_SS.sub('', h)):
        nom = nom.lower()
        if nom in VIDES:
            continue
        if not ferme:
            pile.append(nom)
        elif pile and pile[-1] == nom:
            pile.pop()
        elif nom in pile:
            return f'fermeture </{nom}> mal placée'
    return None if not pile else f'non fermées: {pile[-5:]}'


def controler(chemin, paquet, a, vus_lot):
    brut = open(chemin, 'rb').read()
    h = brut.decode('utf-8', 'ignore')
    d = collections.defaultdict(list)
    ph = phrases_html(SOURCES.sub(' ', h))  # la section Sources (générée, identique partout) n'entre pas dans l'analyse
    # A — véracité
    for tag, b, t in ph:
        cites = CIT.findall(b)
        nums = nombres(STRUCT.sub(' ', t))  # seuls les libellés structurels (point 3, DX.4, rang 2…) sont exemptés
        if nums and not cites and tag.lower() != 'td':
            d['A_chiffre_sans_citation'].append(t[:140])
        for c in cites if paquet else []:
            if c not in paquet:
                d['A_citation_inconnue'].append(c)
        if paquet and cites and nums:
            source = ' '.join(paquet.get(c, '') for c in cites)
            ns = nombres_source(source)
            manq = {n for n in nums if n not in ns}
            if manq:
                d['A_nombre_absent_de_l_extrait'].append(f'{sorted(manq)} :: {t[:120]}')
        if DOSE.search(t) and not any(c.lower().startswith('aips') for c in cites):
            d['A_dose_sans_AIPS'].append(t[:140])
    # B — langue
    paras = re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>', h, re.S | re.I)
    sans_conn = sum(1 for p in paras if len(texte(p).split()) > 40 and not CONNECT.search(texte(p)))
    for tag, b, t in ph:
        if tag.lower() in ('td',):
            continue
        n = len(t.split())
        if not est_verbale(t):
            d['B_phrase_nominale'].append(t[:120])
        if n > 32:
            d['B_phrase_longue'].append(f'{n} mots :: {t[:90]}')
        k = hashlib.sha1(re.sub(r'\W+', '', t.lower()).encode()).hexdigest()
        if len(t) > 60:
            if k in vus_lot and vus_lot[k] != chemin:
                d['B_phrase_partagee_entre_fichiers'].append(t[:120])
            elif k in vus_lot.get('_local_' + chemin, set()):
                d['B_phrase_dupliquee'].append(t[:120])
            vus_lot.setdefault(k, chemin)
            vus_lot.setdefault('_local_' + chemin, set()).add(k)
    nph = max(1, len([1 for tg, _, _ in ph if tg.lower() != 'td']))
    conn = sum(1 for tg, _, t in ph if tg.lower() != 'td' and CONNECT.search(t))
    # C — forme
    if a.points:
        manquants = [i for i in range(1, a.points + 1) if not re.search(rf'id="[\w-]*p{i}"', h)]
        if manquants:
            d['C_points_manquants'].append(str(manquants))
    if 'FIN_FICHIER' not in h[-400:]:
        d['C_FIN_FICHIER_absent'].append('-')
    if re.search(r'\stitle=', h):
        d['C_title_interdit'].append(str(len(re.findall(r'\stitle=', h))))
    if re.search(r'<script\b', h, re.I) and not a.script_ok:
        d['C_script_interdit'].append('-')
    nus = len(re.findall(r'<table\b', h)) - len(re.findall(r'overflow-x:\s*auto[^>]*>\s*<table', h))
    if nus > 0:
        d['C_tableau_non_enveloppe'].append(str(nus))
    e = equilibre(h)
    if e:
        d['C_balises'].append(e)
    if not (a.min <= len(brut) <= a.max):
        d['C_taille_hors_bande'].append(f'{len(brut)} o (bande {a.min}–{a.max})')
    rouge = [k for k in d if k.startswith(('A_nombre', 'A_citation', 'A_dose', 'C_points', 'C_FIN', 'C_balises', 'B_phrase_partagee'))]
    verdict = 'ROUGE' if rouge else ('ORANGE' if d else 'VERT')
    return {'fichier': chemin, 'octets': len(brut), 'sha256': hashlib.sha256(brut).hexdigest()[:16],
            'verdict': verdict, 'phrases': nph, 'connecteur%': round(100 * conn / nph),
            'paragraphes_sans_connecteur': sans_conn,
            'defauts': {k: {'n': len(v), 'ex': v[:a.ex]} for k, v in d.items()}}


def charger_paquet(p):
    if not p:
        return {}
    j = json.load(open(p))
    return {x['id']: x['texte'] for x in j['passages']} if isinstance(j, dict) else {x['id']: x['texte'] for x in j}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('fichiers', nargs='+')
    ap.add_argument('--paquet')
    ap.add_argument('--points', type=int, default=14)
    ap.add_argument('--min', type=int, default=100_000)
    ap.add_argument('--max', type=int, default=200_000)
    ap.add_argument('--ex', type=int, default=3, help='exemples par défaut (concision du rapport)')
    ap.add_argument('--script-ok', action='store_true')
    a = ap.parse_args()
    P = charger_paquet(a.paquet)
    vus = {}
    R = [controler(f, P, a, vus) for f in a.fichiers]
    print(json.dumps(R, ensure_ascii=False, indent=1))
    sys.exit(1 if any(r['verdict'] == 'ROUGE' for r in R) else 0)
