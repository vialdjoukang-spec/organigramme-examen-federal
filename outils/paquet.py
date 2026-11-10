#!/usr/bin/env python3
"""PAQUET — construit gratuitement le paquet de preuves d'une entité (SSP ou DX), point par point.

Entrées (toutes locales, aucune requête modèle) :
  --registres  fichiers JSON/MD de liens déjà validés par Vial (priorité absolue de sélection des sources)
  --textes     extraits déjà lus et datés (evidence/*.txt ; en-tête « URL: » et « Consulté: » recommandé)
  --aips       corpus AipsDownload_*.xml (lu en flux, jamais en entier) + --dci / --autorisation
  --telecharger liste d'URL à rapatrier (cache disque par SHA-256 ; aucune relecture d'une URL déjà en cache)
Sortie : paquet.json = {entite, passages:[{id,source,url,date,texte}], points:{"1":[ids…],…,"14":[…]}}

Usage :
  python3 paquet.py --entite "Ascite de l'hypertension portale" --sortie LOT_166/DX.1/paquet.json \
     --registres data/ck/src.json tools/prevalences/sources_reconnues.json \
     --textes LOT_166/evidence/*.txt --aips AipsDownload_20261008.zip --ham zugelassene_packungen_ham.xlsx \
     --dci spironolact furosemid
"""
import re, os, sys, json, html, hashlib, argparse, datetime, subprocess, urllib.request, collections, math
import zipfile
import xml.etree.ElementTree as ET

CACHE = os.environ.get('PAQUET_CACHE', '.cache/paquet')
# Lexique de sélection par point (nos termes ; enrichissable sans modèle)
POINTS = {
    1: 'définition définit terminologie synonyme classification critères consensus société savante',
    2: 'prévalence incidence épidémiologie suisse OFS Obsan âge sexe mortalité facteurs de risque histoire naturelle',
    3: 'physiopathologie mécanisme cascade lésion perturbation cellule récepteur médiateur',
    4: 'diagnostic différentiel exclure grave urgence red flag drapeau discriminant',
    5: 'anamnèse interrogatoire antécédents symptôme chronologie médicaments drapeaux rouges',
    6: 'examen physique inspection palpation percussion auscultation signe manœuvre sensibilité spécificité',
    7: 'syndrome signes fonctionnels signes physiques tableau clinique',
    8: 'critères diagnostiques majeurs mineurs seuil score stade grade classification',
    9: 'examen complémentaire gold standard référence imagerie biologie échographie scanner IRM ponction interprétation seuil',
    10: 'algorithme arbre décisionnel conduite étape si alors',
    11: 'traitement prise en charge posologie dose mg surveillance urgence grossesse insuffisance rénale hépatique sortie pronostic',
    12: 'prévention dépistage vaccination primaire secondaire tertiaire recommandation',
    13: 'retenir essentiel clé',
    14: 'piège erreur fréquente confusion examen',
}
AIPS_SECTIONS = ('posologie', "mode d'emploi", 'contre-indication', 'mises en garde', 'grossesse', 'allaitement',
                 'interactions', 'effets indésirables', 'surdosage', 'indications')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def html_txt(s):
    s = re.sub(r'<(script|style)\b.*?</\1>', ' ', s, flags=re.S | re.I)
    s = re.sub(r'<(br|/p|/li|/tr|/h\d)\b[^>]*>', '\n', s, flags=re.I)
    return re.sub(r'[ \t]+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()


def telecharger(url):
    """Cache disque (équivalent requests-cache/Hishel, stdlib) : une URL n'est rapatriée qu'une fois."""
    os.makedirs(CACHE, exist_ok=True)
    f = os.path.join(CACHE, sha(url.encode())[:24])
    if os.path.exists(f + '.txt'):
        return open(f + '.txt', encoding='utf-8').read()
    req = urllib.request.Request(url, headers={'User-Agent': 'paquet-medical/1.0 (usage pedagogique)'})
    with urllib.request.urlopen(req, timeout=25) as r:
        brut, typ = r.read(8_000_000), r.headers.get('Content-Type', '')
    open(f + '.raw', 'wb').write(brut)
    if 'pdf' in typ or url.lower().endswith('.pdf'):
        t = subprocess.run(['pdftotext', '-layout', f + '.raw', '-'], capture_output=True, text=True).stdout
    else:
        t = html_txt(brut.decode('utf-8', 'ignore'))
    entete = f'URL: {url}\nConsulté: {datetime.date.today().isoformat()}\nSHA256: {sha(brut)}\n\n'
    open(f + '.txt', 'w', encoding='utf-8').write(entete + t)
    return entete + t


def decouper(texte, stem, source, taille=700):
    url = (re.search(r'^URL:\s*(\S+)', texte, re.M) or [None, ''])[1]
    date = (re.search(r'^Consult[ée]+:\s*(\S+)', texte, re.M) or [None, ''])[1]
    corps = re.sub(r'^(URL|Consult[ée]+|SHA256):.*\n', '', texte, flags=re.M)
    blocs, cur = [], ''
    for para in re.split(r'\n\s*\n|\n(?=[A-ZÀ-Ý0-9•\-])', corps):
        para = re.sub(r'\s+', ' ', para).strip()
        if not para:
            continue
        if len(cur) + len(para) > taille and cur:
            blocs.append(cur)
            cur = ''
        cur = (cur + ' ' + para).strip()
    if cur:
        blocs.append(cur)
    return [{'id': f'{stem}-{i + 1}', 'source': source, 'url': url, 'date': date, 'texte': b} for i, b in enumerate(blocs)]


def ham(xlsx, dcis):
    """Liste Swissmedic HAM (xlsx, lue sans dépendance) : DCI latine/française → numéros d'autorisation (5 chiffres)."""
    z = zipfile.ZipFile(xlsx)
    ss = [html.unescape(re.sub(r'<[^>]+>', '', t)) for t in re.findall(r'<si>(.*?)</si>', z.read('xl/sharedStrings.xml').decode(), re.S)]
    nums = set()
    for row in re.findall(r'<row\b.*?</row>', z.read('xl/worksheets/sheet1.xml').decode(), re.S):
        cel = {}
        for attrs, inner in re.findall(r'<c\b([^>]*)>(.*?)</c>', row, re.S):
            v = re.search(r'<v>(.*?)</v>', inner)
            if v:
                col = re.search(r'r="([A-Z]+)', attrs).group(1)
                cel[col] = ss[int(v.group(1))] if 't="s"' in attrs else v.group(1)
        if any(d.lower() in ' '.join(cel.values()).lower() for d in dcis) and re.fullmatch(r'\d{1,5}', cel.get('A', '')):
            nums.add(cel['A'].zfill(5))  # colonne A = numéro d'autorisation Swissmedic
    return nums


def aips(xml_path, dcis, autorisations, reseau=True):
    """Corpus AIPS = index des informations professionnelles (Type SmPC) : numéro → URL HTML française.
    Lecture en flux ; le texte est ensuite rapatrié (cache) et découpé par rubrique (posologie, grossesse…)."""
    out, cibles, ns = [], [d.lower() for d in dcis], '{https://simisinfo.refdata.ch/MedicinalDocuments/1.0/}'
    if xml_path.endswith('.zip'):  # le zip d'origine se lit en flux, sans extraction sur disque
        z = zipfile.ZipFile(xml_path)
        xml_path = z.open(next(n for n in z.namelist() if n.lower().endswith('.xml')))
    for _, el in ET.iterparse(xml_path, events=('end',)):
        if el.tag != ns + 'MedicinalDocumentsBundle':
            continue
        no = el.findtext(f'{ns}RegulatedAuthorization/{ns}Identifier') or ''
        if el.findtext(ns + 'Type') != 'SmPC':
            el.clear(); continue
        for doc in el.findall(ns + 'AttachedDocument'):
            nom = doc.findtext(ns + 'Description') or ''
            if doc.findtext(ns + 'Language') != 'fr' or not (no in autorisations or any(c in nom.lower() for c in cibles)):
                continue
            url = next((r.findtext(ns + 'Url') for r in doc.findall(ns + 'DocumentReference') if r.findtext(ns + 'ContentType') == 'text/html'), '')
            source = f'AIPS {nom} (Swissmedic {no})'
            out.append({'id': f'aips-{no}-0', 'source': source, 'url': url, 'date': (el.findtext(ns + 'Date') or '')[:10],
                        'texte': f'Information professionnelle {nom}, autorisation Swissmedic {no}.'})
            if reseau and url:
                try:
                    contenu = telecharger(url)
                    k = 0  # compteur unique par document : un ID d'extrait ne se répète jamais entre rubriques
                    for sec in re.split(r'\n(?=(?:' + '|'.join(AIPS_SECTIONS) + r'))', contenu, flags=re.I):
                        if sec.lower().startswith(AIPS_SECTIONS):
                            for p in decouper(sec, f'aips-{no}', source, 900):
                                k += 1
                                p.update(id=f'aips-{no}-{k}', url=url)
                                out.append(p)
                except Exception as e:
                    print(f'AIPS {no} non rapatrié ({e}) : URL consignée, aucune dose écrite sans texte lu', file=sys.stderr)
        el.clear()
    return out


def registres(chemins):
    """Liens validés de Vial : servent d'ordre de priorité (domaines + URL exactes)."""
    urls = []
    for c in chemins:
        s = open(c, encoding='utf-8', errors='ignore').read()
        urls += re.findall(r'https?://[^\s"\'<>)\]]+', s)
    dom = collections.Counter(re.sub(r'^https?://(www\.)?', '', u).split('/')[0] for u in urls)
    return set(urls), dom


def selection(passages, entite, k=8):
    """BM25 allégé (stdlib) : passages les plus pertinents pour chaque point."""
    tok = lambda s: re.findall(r'\w{3,}', s.lower())
    docs = [tok(p['texte']) for p in passages]
    N, df = len(docs) or 1, collections.Counter(w for d in docs for w in set(d))
    moy = sum(map(len, docs)) / N if docs else 1
    out = {}
    for n, mots in POINTS.items():
        q = tok(mots) + tok(entite) * 2
        sc = []
        for i, d in enumerate(docs):
            tf = collections.Counter(d)
            s = sum(math.log(1 + (N - df[w] + .5) / (df[w] + .5)) * tf[w] * 2.2 / (tf[w] + 1.2 * (.25 + .75 * len(d) / moy))
                    for w in q if w in tf)
            if n == 11 and passages[i]['id'].startswith('aips'):
                s *= 2  # le point 11 privilégie l'AIPS
            sc.append((s, passages[i]['id']))
        out[str(n)] = [i for s, i in sorted(sc, reverse=True)[:k] if s > 0]
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--entite', required=True)
    ap.add_argument('--sortie', required=True)
    ap.add_argument('--registres', nargs='*', default=[])
    ap.add_argument('--textes', nargs='*', default=[])
    ap.add_argument('--telecharger', help='fichier texte : une URL par ligne')
    ap.add_argument('--aips')
    ap.add_argument('--dci', nargs='*', default=[])
    ap.add_argument('--autorisation', nargs='*', default=[])
    ap.add_argument('--ham', help='liste Swissmedic HAM .xlsx : traduit --dci en numéros d’autorisation')
    ap.add_argument('--hors-ligne', action='store_true')
    ap.add_argument('--k', type=int, default=8)
    a = ap.parse_args()
    P = []
    for t in a.textes:
        P += decouper(open(t, encoding='utf-8', errors='ignore').read(), os.path.splitext(os.path.basename(t))[0], t)
    valides, domaines = registres(a.registres) if a.registres else (set(), {})
    if a.telecharger:
        for u in [l.strip() for l in open(a.telecharger) if l.strip().startswith('http')]:
            try:
                P += decouper(telecharger(u), 'w' + sha(u.encode())[:6], u)
            except Exception as e:
                print(f'ECHEC {u} : {e}', file=sys.stderr)  # échec dit, jamais contourné
    autor = set(a.autorisation) | (ham(a.ham, a.dci) if a.ham and a.dci else set())
    if a.aips and (a.dci or autor):
        P += aips(a.aips, a.dci, autor, reseau=not a.hors_ligne)
    for p in P:
        d = re.sub(r'^https?://(www\.)?', '', p['url'] or '').split('/')[0]
        p['priorite'] = 2 if p['url'] in valides else (1 if d in domaines else 0)
    P.sort(key=lambda p: -p['priorite'])
    os.makedirs(os.path.dirname(a.sortie) or '.', exist_ok=True)
    json.dump({'entite': a.entite, 'genere': datetime.datetime.now().isoformat(timespec='minutes'),
               'passages': P, 'points': selection(P, a.entite, a.k)}, open(a.sortie, 'w'), ensure_ascii=False, indent=1)
    print(f'{a.sortie} : {len(P)} passages, {sum(p["id"].startswith("aips") for p in P)} AIPS')
