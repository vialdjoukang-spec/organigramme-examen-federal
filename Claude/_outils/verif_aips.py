#!/usr/bin/env python3
"""VERIF_AIPS — porte mécanique avant tout audit (protocole Fable, 11.11.2026), zéro modèle.

Pour chaque leçon :
  1. chaque ancre `#sb-aips-<n°>` citée a une entrée de bibliographie `<li id="sb-aips-<n°>">` avec une URL refdata ;
  2. chaque citation entre guillemets « … » suivie, dans la même phrase, d'une ancre AIPS figure mot pour mot
     dans le texte de CETTE information professionnelle (rapatriée de refdata, mise en cache) ;
  3. chaque phrase de dose (mg, µg, UI, mmol) qui cite une ancre AIPS sans dire « hors AIPS » ni écrire une divergence
     a ses nombres de dose dans le texte de l'AIPS citée ; sinon « dose absente de l'AIPS citée » (à relire à la main :
     soit la mauvaise AIPS est collée, soit la dose vient d'une recommandation et la phrase doit le dire).

Usage : python3 Claude/_outils/verif_aips.py Claude/LOT_0XX/*.html [--cache DIR] [--json]
Code de sortie 1 si un défaut 1 ou 2 existe, ou si une AIPS citée n'a pas pu être lue (une vérification non faite
n'est jamais un succès). Les défauts 3 sont des alertes à relire.
"""
import re, sys, os, html, json, hashlib, subprocess, argparse

GUILL = re.compile(r'«\s*(.+?)\s*»', re.S)
ANCRE = re.compile(r'href="#sb-aips-([0-9a-z]+)"')
DOSE = re.compile(r"(\d{1,3}(?:[ '’\u00a0\u202f]\d{3})+|\d+(?:[.,]\d+)?)\s?(?:mg|µg|mcg|UI|mmol)\b")
HORS = re.compile(r"hors (?:AIPS|information professionnelle)|ne (?:chiffre|donne|fixe|porte|décrit) pas|diverge|"
                  r"alors que l'AIPS|absente? de l'AIPS|recommandation|consensus|propose|selon (?:l'|la |le )", re.I)


def norm(s):
    s = html.unescape(s).replace(' ', ' ').replace(' ', ' ').replace(' ', ' ')
    s = s.replace('’', "'").replace('ʼ', "'").replace('‑', '-').replace('–', '-').replace('−', '-')
    s = re.sub(r"(?<=\d)['’ ](?=\d{3})", '', s)  # 1'000 → 1000
    s = re.sub(r'\s+', ' ', s).lower()
    return re.sub(r'\s*([.,;:!?()«»"])\s*', r'\1', s).strip(' .;,')


def texte(h, colle=False):
    # colle=True : balises en ligne retirées sans espace, car refdata découpe parfois un mot en plusieurs <span> (« allait|e|ment »)
    if colle:
        h = re.sub(r'</?(?:span|b|i|em|strong|u|font)\b[^>]*>', '', h)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h)))


def aips(url, cache):
    f = os.path.join(cache, hashlib.sha1(url.encode()).hexdigest() + '.html')
    if not os.path.exists(f) or os.path.getsize(f) < 2000:
        subprocess.run(['curl', '-sS', '--retry', '2', '-m', '60', '-o', f, url], check=False)
    try:
        h = open(f, encoding='utf-8', errors='ignore').read()
        return norm(texte(h)) + ' ¦ ' + norm(texte(h, colle=True))  # citation admise si présente dans l'une des deux lectures
    except OSError:
        return ''


def verifier(chemin, cache):
    h = open(chemin, encoding='utf-8').read()
    biblio = {m.group(1): m.group(2) for m in re.finditer(r'<li id="sb-aips-([0-9a-z]+)">(.*?)</li>', h, re.S)}
    urls = {k: (re.search(r'https://files\.refdata\.ch/[^\s<"]+?\.html', v) or [None])[0] for k, v in biblio.items()}
    d = {'ancre_sans_biblio': [], 'biblio_sans_url': [], 'citation_absente': [], 'dose_absente': [], 'aips_illisible': []}
    cites = set(ANCRE.findall(h))
    d['ancre_sans_biblio'] = sorted(cites - set(biblio))
    d['biblio_sans_url'] = sorted(k for k in cites & set(biblio) if not urls.get(k))
    T = {}
    for k in cites:
        if urls.get(k):
            T[k] = aips(urls[k], cache)
            if len(T[k]) < 1500:
                d['aips_illisible'].append(k)
    corps = h.split('id="sb-aips-')[0] if 'id="sb-aips-' in h else h
    # unités de texte : paragraphe, cellule, puce ; puis phrases closes par une citation
    for bloc in re.findall(r'<(?:p|li|td|th|caption)\b[^>]*>(.*?)</(?:p|li|td|th|caption)>', corps, re.S):
        for ph in re.split(r'(?<=</sup>)\s*[.;]\s+', bloc):
            anc = [a for a in ANCRE.findall(ph) if a in T and a not in d['aips_illisible']]
            if not anc:
                continue
            brut = texte(re.sub(r'<sup.*?</sup>', ' ', ph, flags=re.S))
            for q in GUILL.findall(brut):
                n = norm(q)
                if len(n) >= 12 and not any(n in T[a] for a in anc):
                    d['citation_absente'].append({'aips': anc, 'citation': q[:160]})
            if DOSE.search(brut) and not HORS.search(brut) and '«' not in brut:
                manq = [x for x in (re.sub(r"[ '’\u00a0\u202f]", '', y) for y in DOSE.findall(brut))
                        if not any(re.search(r'(?<![\d.,])' + re.escape(x.replace('.', ',')).replace(',', '[.,]') + r'(?![\d])', T[a]) for a in anc)]
                if manq:
                    d['dose_absente'].append({'aips': anc, 'nombres': manq, 'phrase': brut.strip()[:200]})
    return {'fichier': os.path.basename(chemin), 'aips_citees': len(cites),
            'bloquant': bool(d['ancre_sans_biblio'] or d['biblio_sans_url'] or d['citation_absente'] or d['aips_illisible']),
            'defauts': {k: v for k, v in d.items() if v}}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('fichiers', nargs='+')
    ap.add_argument('--cache', default=os.environ.get('AIPS_CACHE', '/tmp/aips_cache'))
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args()
    os.makedirs(a.cache, exist_ok=True)
    R = [verifier(f, a.cache) for f in a.fichiers]
    if a.json:
        print(json.dumps(R, ensure_ascii=False, indent=1))
    else:
        for r in R:
            print(f"{r['fichier']} : {'BLOQUANT' if r['bloquant'] else 'OK'} · {r['aips_citees']} AIPS citées · "
                  + ', '.join(f'{k}={len(v)}' for k, v in r['defauts'].items()))
            for k, v in r['defauts'].items():
                for x in v[:8]:
                    print('   ', k, '::', json.dumps(x, ensure_ascii=False)[:260])
    sys.exit(1 if any(r['bloquant'] for r in R) else 0)
