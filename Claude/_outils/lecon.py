#!/usr/bin/env python3
"""LECON — enveloppe Claude des outils de référence (outils/ de reference/prompts-9.11.26), zéro modèle.

  prep     : contrat.json (14 points µ3) + paquet.json (URL rapatriées en cache, textes evidence, AIPS par DCI)
  finir    : assembler.py puis controle3.py (avec le paquet), résumé compact ; code 1 si ROUGE
  extraire : texte des passages d'un paquet (id + texte), filtrable par motif, pour lecture ciblée

Correctif local (sans toucher outils/) : dans paquet.py, les rubriques AIPS ne sont pas découpées car chaque
ligne du texte rapatrié commence par une espace ; on retire cette espace avant le découpage.
Chaque DCI garde au plus --aips-max documents (le premier est la préparation originale quand elle existe).

Exemples :
  python3 Claude/_outils/lecon.py prep --lot 043 --cible DX.3 --entite "Péricardite aiguë" --urls urls.txt --dci colchicin ibuprofen
  python3 Claude/_outils/lecon.py finir --lot 043 --cible DX.3 --titre "DX.3 — Péricardite aiguë"
  python3 Claude/_outils/lecon.py extraire --lot 043 --cible DX.3 --motif "colchicine|posologie"
"""
import os, re, sys, json, argparse, subprocess, collections

ICI = os.path.dirname(os.path.abspath(__file__))
REF = os.environ.get('OUTILS_REF', os.path.join(ICI, '..', '..', 'outils'))
sys.path.insert(0, REF)
os.environ.setdefault('PAQUET_CACHE', '/tmp/claude_paquet_cache')
AIPS_ZIP = os.environ.get('AIPS_ZIP', '/home/user/Medina/AipsDownload_20261008.zip')
_D = '/home/user/Medina/docs/collaboration/references/medicaments-suisses-vial-2026-10-11/'
# erweiterte_ham_ind couvre les monopréparations courantes (Dafalgan 46206…) absentes de zugelassene_packungen_ham
HAMS = os.environ.get('HAM_XLSX', _D + 'erweiterte_ham_ind.xlsx:' + _D + 'zugelassene_packungen_ham.xlsx').split(':')

POINTS = [
 ("Définition et sémantique", 5000, "Définition exacte de la société savante, nommée et datée ; synonymes admis et termes à éviter ; ce que l'entité est, ce qu'elle n'est pas et ce qui s'en approche."),
 ("Épidémiologie (Suisse, puis Europe)", 7000, "Prévalence et incidence chiffrées, sourcées et datées ; âge, sexe, groupes à risque et mortalité ; histoire naturelle ; enjeux de santé publique. Tableau chiffre/population/année/source si ≥ 3 chiffres."),
 ("Physiopathologie", 12000, "Chaîne moléculaire → cellulaire → tissulaire → clinique ; chaque perturbation reliée à l'examen qui la montre et au traitement qui la corrige. Tableau de corrélation perturbation → exploration → thérapeutique."),
 ("Démarche diagnostique", 8000, "Les graves d'abord (E1, E2 avec 🚩), puis les fréquents ; trois ou quatre DX discriminants avec signe ou examen qui tranche, piège, conduite si positif. Tableau DX/élément qui tranche/piège/conduite."),
 ("Anamnèse ciblée et drapeaux rouges", 8000, "Chaque question porte sa raison physiopathologique ; chronologie, déclencheurs, comorbidités, médicaments ; tableau drapeau rouge/signification/action immédiate."),
 ("Examen physique ciblé, région par région", 10000, "Le normal puis le pathologique ; technique du geste ; valeur diagnostique et piège d'interprétation."),
 ("Approche syndromique", 10000, "Syndromes numérotés 7.1, 7.2…, chacun éclaté en signes fonctionnels et physiques ; définition en fenêtre, geste de recherche, mécanisme. Tableau syndrome/signes fonctionnels/signes physiques."),
 ("Diagnostic positif et critères", 8000, "Critères de la société savante avec leur année (majeurs, mineurs, seuils, durée, exclusions) ; ce qui suffit et ce qui ne suffit pas ; scores et stades avec leur usage. Tableau des critères."),
 ("Examens complémentaires", 16000, "9.a gold standard ; 9.b première intention ; 9.c alternatives (grossesse, enfant, DFGe < 30, allergie iode, IRM impossible) ; 9.d deuxième intention ; indication, prescription exacte, interprétation. Tableau résultat/signification/conduite, valeurs normales SI."),
 ("Arbre décisionnel", 6000, "Embranchements « si X → Y » en liste imbriquée ; graves d'abord ; chaque nœud = signe, examen ou action."),
 ("Prise en charge selon les recommandations suisses", 20000, "11.A but chiffré ; 11.B moyens : urgences chronologiques (fenêtre « Urgence — conduite chronologique »), ordre du traitement, pharmacologie AIPS (spécialité ®, dose, voie, durée, n° Swissmedic), non pharmacologique, situations spéciales, social et assurances ; 11.C surveillance ; 11.D pronostic, guérison, critères de sortie. Tableau médicaments."),
 ("Prévention", 6000, "Primaire, secondaire, tertiaire avec recommandation suisse (organisme, année) ; gestes, populations cibles, seuils."),
 ("Points clés", 2000, "Trois à six phrases verbales intactes, mémorisables, sans fenêtre."),
 ("Pièges et questions fréquentes à l'examen fédéral suisse", 6000, "Chaque piège en question d'examen, réponse et raison ; tableau question/réponse/raison."),
]
SQ = {9: "<h4><em>9.a Gold standard</em></h4>…<h4><em>9.b Première intention</em></h4>…<h4><em>9.c Alternatives</em></h4>…<h4><em>9.d Deuxième intention</em></h4>…",
      11: "<h4><em>11.A But</em></h4>…<h4><em>11.B Moyens</em></h4>…<h4><em>11.C Surveillance</em></h4>…<h4><em>11.D Pronostic et sortie</em></h4>…"}


def dossier(lot, cible):
    racine = os.path.join('Claude', f'LOT_{int(lot):03d}')
    return racine, os.path.join(racine, '_travail', 'PA' if cible in ('A', 'PA') else cible)


def prep(a):
    import paquet as PQ
    orig = PQ.html_txt
    PQ.html_txt = lambda s: '\n'.join(l.strip() for l in orig(s).split('\n'))
    racine, d = dossier(a.lot, a.cible)
    os.makedirs(d, exist_ok=True)
    pre = 'pa' if a.cible in ('A', 'PA') else 'dx' + a.cible.split('.')[-1]
    C = {'LOT': f'{int(a.lot):03d}', 'CODE_SSP': a.ssp or '', 'ENTITE': a.entite, 'PREFIX': pre, 'SECURITE': a.securite or '',
         'points': {str(i + 1): {'titre': t, 'octets': o, 'exige': e, 'squelette': SQ.get(i + 1, '')} for i, (t, o, e) in enumerate(POINTS)}}
    json.dump(C, open(os.path.join(d, 'contrat.json'), 'w'), ensure_ascii=False, indent=1)
    P = []
    for t in a.textes or []:
        P += PQ.decouper(open(t, encoding='utf-8', errors='ignore').read(), os.path.splitext(os.path.basename(t))[0], t)
    echecs = []
    if a.urls:
        for u in [l.strip() for l in open(a.urls) if l.strip().startswith('http')]:
            try:
                t = PQ.telecharger(u)
                if re.search(r'recaptcha|captcha|are you a robot|verify you are human|Access Denied|Just a moment', t[:4000], re.I) and len(t) < 20000:
                    f = os.path.join(os.environ['PAQUET_CACHE'], PQ.sha(u.encode())[:24])
                    for ext in ('.txt', '.raw'):
                        if os.path.exists(f + ext):
                            os.remove(f + ext)
                    raise RuntimeError('page anti-robot (captcha) : non citable, retirée du cache')
                P += PQ.decouper(t, 'w' + PQ.sha(u.encode())[:6], u)
            except Exception as e:
                echecs.append(f'{u} : {e}')
    if a.dci or a.autorisation:
        autor = set(a.autorisation)
        for h in HAMS:
            autor |= PQ.ham(h, a.dci)
        no_prio = lambda no: 0 if no in a.autorisation else 1
        A = PQ.aips(AIPS_ZIP, a.dci, autor)
        par_doc = collections.OrderedDict()
        for p in A:
            par_doc.setdefault(p['id'].split('-')[1], []).append(p)
        garde, compte = [], collections.Counter()

        def actifs(ps):
            """Nombre de principes actifs (noms latins en -um) de la rubrique Composition : 1 = monopréparation."""
            comp = next((q['texte'] for q in ps if re.search(r'Principes? actifs?', q['texte'])), '')
            m = re.search(r'Principes? actifs?\s*:?\s*(.{0,300}?)(Excipients|$)', comp)
            return len(set(re.findall(r'\b[A-Z]?[a-z]+(?:um|i|ae)\b', m.group(1)))) if m else 9

        def rubriques(ps):
            return sum(bool(re.match(r'(Posologie|Grossesse|Contre-indications)', q['texte'])) for q in ps)
        # monopréparations lisibles d'abord (Posologie + Grossesse découpées), puis volume de texte
        COMBI = re.compile(r'\b(plus|comp|duo|grippe|combi|forte?|cold|rhume|night|day)\b|[/+]|co-|\bet\b', re.I)
        ENFANT = re.compile(r'enfant|sirop|suspension|junior|b[ée]b[ée]|p[ée]diatr|gouttes|suppositoire', re.I)

        def cle(kv):
            nom = kv[1][0]['source']
            return (no_prio(kv[0]), bool(COMBI.search(nom)), bool(ENFANT.search(nom)), -rubriques(kv[1]), -len(kv[1]))
        for no, ps in sorted(par_doc.items(), key=cle):
            nom = ps[0]['source'].lower()
            dci = next((x for x in a.dci if x.lower() in nom), None) or next((x for x in a.dci if any(x.lower() in q['texte'].lower() for q in ps)), a.dci[0])
            if no in a.autorisation or (compte[dci] < a.aips_max and len(ps) > 1):
                compte[dci] += 1
                garde += ps
        P += garde
    old = os.path.join(d, 'paquet.json')
    if a.ajouter and os.path.exists(old):
        anciens = json.load(open(old))['passages']
        ids = {p['id'] for p in P}
        P = [p for p in anciens if p['id'] not in ids] + P
    for p in P:
        p.setdefault('priorite', 0)
    json.dump({'entite': a.entite, 'passages': P, 'points': PQ.selection(P, a.entite, 8)}, open(old, 'w'), ensure_ascii=False, indent=1)
    n_aips = sum(p['id'].startswith('aips') for p in P)
    docs = sorted({p['source'] for p in P if p['id'].startswith('aips')})
    print(f'{old} : {len(P)} passages, {n_aips} AIPS ; documents AIPS : {docs}')
    for e in echecs:
        print('ECHEC', e)


def lignes(sortie):
    """µ7 : aucune ligne > 3 000 caractères — la liste Sources de l'assembleur passe à une ligne par source ; MANIFESTE resigné."""
    import hashlib
    h = open(sortie, encoding='utf-8').read()
    h2 = h.replace('</li><li id="sb-', '</li>\n<li id="sb-').replace('<ol><li id="sb-', '<ol>\n<li id="sb-')
    if h2 != h:
        open(sortie, 'w', encoding='utf-8').write(h2)
        man = os.path.join(os.path.dirname(sortie), 'MANIFESTE.json')
        m = json.load(open(man)) if os.path.exists(man) else {}
        b = h2.encode()
        m[os.path.basename(sortie)] = {'octets': len(b), 'sha256': hashlib.sha256(b).hexdigest()}
        json.dump(m, open(man, 'w'), ensure_ascii=False, indent=1)


def finir(a):
    racine, d = dossier(a.lot, a.cible)
    nom = f'LOT_{int(a.lot):03d}_Phase_A_V0.html' if a.cible in ('A', 'PA') else f'LOT_{int(a.lot):03d}_Phase_B_V0_{a.cible}.html'
    sortie = os.path.join(racine, nom)
    r = subprocess.run([sys.executable, os.path.join(REF, 'assembler.py'), '--fragments', os.path.join(d, 'fragments'),
                        '--paquet', os.path.join(d, 'paquet.json'), '--contrat', os.path.join(d, 'contrat.json'),
                        '--titre', a.titre, '--sortie', sortie], capture_output=True, text=True)
    print(r.stdout.strip(), r.stderr.strip()[-500:])
    lignes(sortie)
    r = subprocess.run([sys.executable, os.path.join(REF, 'controle3.py'), sortie, '--paquet', os.path.join(d, 'paquet.json'), '--ex', str(a.ex)],
                       capture_output=True, text=True)
    open(os.path.join(d, 'controle.json'), 'w').write(r.stdout)
    R = json.loads(r.stdout)[0]
    print(json.dumps({k: R[k] for k in ('verdict', 'octets', 'connecteur%', 'paragraphes_sans_connecteur')}, ensure_ascii=False))
    for k, v in R['defauts'].items():
        print(f"  {k} ({v['n']}) :", ' || '.join(v['ex']))
    sys.exit(1 if R['verdict'] == 'ROUGE' else 0)


def extraire(a):
    _, d = dossier(a.lot, a.cible)
    P = json.load(open(os.path.join(d, 'paquet.json')))['passages']
    m = re.compile(a.motif, re.I) if a.motif else None
    for p in P:
        if (not m or m.search(p['texte']) or m.search(p['id'])) and (not a.prefixe or p['id'].startswith(a.prefixe)):
            print(f"[{p['id']}] ({p['source'][:70]}, {p.get('date','')}) {p['texte'] if not a.court else p['texte'][:200]}\n")


def manifeste(a):
    """Recalcule MANIFESTE.json du LOT et coupe les lignes trop longues des 11 HTML (avant PR)."""
    import glob
    racine, _ = dossier(a.lot, 'PA')
    for f in sorted(glob.glob(os.path.join(racine, 'LOT_*_Phase_*.html'))):
        lignes(f)
        h = open(f, 'rb').read()
        if any(len(l) > 3000 for l in h.decode('utf-8', 'ignore').split('\n')):
            print('LIGNE > 3000 :', f)
    import hashlib
    m = {os.path.basename(f): {'octets': len(open(f, 'rb').read()), 'sha256': hashlib.sha256(open(f, 'rb').read()).hexdigest()}
         for f in sorted(glob.glob(os.path.join(racine, 'LOT_*_Phase_*.html')))}
    json.dump(m, open(os.path.join(racine, 'MANIFESTE.json'), 'w'), ensure_ascii=False, indent=1)
    print(len(m), 'fichiers au MANIFESTE')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    s = ap.add_subparsers(dest='cmd', required=True)
    p = s.add_parser('prep'); p.add_argument('--lot', required=True); p.add_argument('--cible', required=True)
    p.add_argument('--entite', required=True); p.add_argument('--ssp'); p.add_argument('--securite')
    p.add_argument('--urls'); p.add_argument('--textes', nargs='*'); p.add_argument('--dci', nargs='*', default=[])
    p.add_argument('--aips-max', type=int, default=2); p.add_argument('--autorisation', nargs='*', default=[], help='n° Swissmedic à inclure d\'office'); p.add_argument('--ajouter', action='store_true')
    f = s.add_parser('finir'); f.add_argument('--lot', required=True); f.add_argument('--cible', required=True)
    f.add_argument('--titre', required=True); f.add_argument('--ex', type=int, default=4)
    e = s.add_parser('extraire'); e.add_argument('--lot', required=True); e.add_argument('--cible', required=True)
    e.add_argument('--motif'); e.add_argument('--prefixe'); e.add_argument('--court', action='store_true')
    m = s.add_parser('manifeste'); m.add_argument('--lot', required=True)
    a = ap.parse_args()
    {'prep': prep, 'finir': finir, 'extraire': extraire, 'manifeste': manifeste}[a.cmd](a)
