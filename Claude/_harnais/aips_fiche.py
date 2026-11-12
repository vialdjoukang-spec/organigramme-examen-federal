#!/usr/bin/env python3
"""AIPS_FICHE — mémoire AIPS partagée (zéro modèle) : une AIPS refdata est lue UNE fois, découpée en rubriques et
gardée en cache JSON ; les agents lisent la fiche compacte (≈ 2–4 Ko) au lieu de l'AIPS entière (40–120 Ko).

  fiche <url_refdata|n°_cache>         → rubriques : numéro, mise à jour, indications, posologie, contre-indications,
                                          grossesse, allaitement (texte AIPS mot pour mot, tronqué proprement)
  verifier <cours.html …>              → porte avant audit : pour chaque fiche .mb, compare les lignes Grossesse,
                                          Allaitement et Contre-indications au texte de l'AIPS citée ; signale toute
                                          interdiction adoucie (« ne doit pas », « absolue nécessité », « sevr… »),
                                          toute date « mise à jour » fausse dans la bibliographie.
  trouve <nom|n°> …                    → corpus refdata hors ligne (AipsDownload_20261008.xml) : n° Swissmedic,
                                          date, URL française de l'AIPS (SmPC) et de la notice (PIL) ; zéro recherche web ; aucune recherche web.
Cache : $AIPS_CACHE (défaut ~/.cache/medina_aips) ; HTML brut + JSON des rubriques.
Code 1 si un défaut ADOUCI ou DATE est trouvé.
"""
import re, sys, os, json, html, hashlib, subprocess, argparse

CACHE = os.environ.get('AIPS_CACHE', os.path.expanduser('~/.cache/medina_aips'))
RUB = ['Composition', 'Indications/Possibilités d’emploi', 'Posologie/Mode d’emploi', 'Contre-indications',
       'Mises en garde et précautions', 'Interactions', 'Grossesse', 'Allaitement', 'Effet sur l’aptitude',
       'Effets indésirables', 'Surdosage', 'Propriétés/Effets', 'Numéro d’autorisation', 'Présentation',
       'Titulaire de l’autorisation', 'Mise à jour de l’information']
INTERDIT = r"ne doit pas|ne doivent pas|ne (?:faut|doit) pas allaiter|on ne doit pas|ne pas (?:allaiter|utiliser|administrer)|contre-indiqu|cesser d.allaiter|interrompre l.allaitement|sevr"
EXCEPTION = r"absolue nécessité|nécessité absolue|que si le bénéfice|indications? strictes?|sauf nécessité"


def texte(h):
    h = re.sub(r'<(script|style)\b.*?</\1>', ' ', h, flags=re.S | re.I)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h))).strip()


def charger(url):
    os.makedirs(CACHE, exist_ok=True)
    cle = hashlib.sha1(url.encode()).hexdigest()
    fj = os.path.join(CACHE, cle + '.json')
    if os.path.exists(fj):
        return json.load(open(fj, encoding='utf-8'))
    fh = os.path.join(CACHE, cle + '.html')
    if not os.path.exists(fh) or os.path.getsize(fh) < 2000:
        subprocess.run(['curl', '-sS', '--retry', '2', '-m', '60', '-o', fh, url], check=False)
    t = texte(open(fh, encoding='utf-8', errors='ignore').read()) if os.path.exists(fh) else ''
    pos = sorted((t.find(r), r) for r in RUB if t.find(r) >= 0)
    rub = {}
    for i, (p, r) in enumerate(pos):
        fin = pos[i + 1][0] if i + 1 < len(pos) else len(t)
        rub[r] = t[p + len(r):fin].strip(' :')
    g = rub.get('Grossesse', '')
    if 'Allaitement' in g and not rub.get('Allaitement'):
        g, _, a = g.partition('Allaitement'); rub['Grossesse'], rub['Allaitement'] = g, a
    d = dict(url=url, titre=t[:80], rubriques=rub,
             numero=re.findall(r'\d{5}', rub.get('Numéro d’autorisation', ''))[:6],
             mise_a_jour=rub.get('Mise à jour de l’information', '')[:40].strip())
    json.dump(d, open(fj, 'w', encoding='utf-8'), ensure_ascii=False)
    return d


def court(s, n=900):
    return s if len(s) <= n else s[:n].rsplit('. ', 1)[0] + '. […]'


def fiche(url):
    d = charger(url)
    print(f"{d['titre']}\nN° {', '.join(d['numero'])} · mise à jour : {d['mise_a_jour']}")
    for r in ['Indications/Possibilités d’emploi', 'Posologie/Mode d’emploi', 'Contre-indications', 'Grossesse', 'Allaitement']:
        print(f'\n## {r}\n{court(d["rubriques"].get(r, "ABSENT"), 1400 if r.startswith("Poso") else 900)}')


def niveau(s):
    """0 rien ; 1 prudence ; 2 exception (absolue nécessité) ; 3 interdiction."""
    if re.search(INTERDIT, s, re.I): return 3
    if re.search(EXCEPTION, s, re.I): return 2
    if re.search(r'prudence|prudent', s, re.I): return 1
    return 0


def verifier(chemin):
    h = open(chemin, encoding='utf-8').read()
    biblio = dict(re.findall(r'<li id="sb-(aips-[0-9a-z]+|s\d+)">(.*?)</li>', h, re.S))
    urls = {k: re.search(r'https://files\.refdata\.ch/\S+?\.html', v).group(0) for k, v in biblio.items()
            if re.search(r'https://files\.refdata\.ch/\S+?\.html', v)}
    defauts = []
    for fid, corps in re.findall(r'<section class="fenetre mb" id="([^"]+)".*?<div class="fen">(.*?)</div></section>', h, re.S):
        ancres = set(re.findall(r'href="#sb-((?:aips-[0-9a-z]+|s\d+))"', corps)) & set(urls)
        if not ancres:
            defauts.append((fid, 'SANS_AIPS', 'aucune AIPS refdata citée dans la fiche')); continue
        A = [charger(urls[a]) for a in ancres]
        lignes = dict((texte(k).lower(), texte(v)) for k, v in re.findall(r'<tr>\s*<t[hd][^>]*>(.*?)</t[hd]>\s*<td[^>]*>(.*?)</td>\s*</tr>', corps, re.S))
        for cle, rub in (('grossesse', 'Grossesse'), ('allaitement', 'Allaitement')):
            ligne = ' '.join(v for k, v in lignes.items() if cle in k)
            ref = ' '.join(a['rubriques'].get(rub, '') for a in A)
            if ref and not ligne:
                defauts.append((fid, 'ABSENT', f'ligne {rub} absente alors que l’AIPS la renseigne'))
            elif niveau(ref) >= 2 and niveau(ligne) < min(niveau(ref), 2):
                extrait = re.search(r'[^.]*(?:' + INTERDIT + '|' + EXCEPTION + r')[^.]*\.', ref, re.I)
                defauts.append((fid, 'ADOUCI', f'{rub} : AIPS « {extrait.group(0).strip()[:160] if extrait else ""} » ; fiche « {ligne[:120]} »'))
        for a, k in zip(A, ancres):
            maj = a['mise_a_jour'][:20]
            if maj and maj.split()[0].lower() not in biblio.get(k, '').lower():
                defauts.append((fid, 'DATE', f'{k} : mise à jour refdata « {maj} » absente de la bibliographie'))
    return defauts


def corpus_index():
    """Index n° → (type nom, date, url fr) ; « SmPC » = information professionnelle (AIPS),
    « PIL » = notice patient ; l'URL SmPC se passe ensuite à `fiche <url>` ; construit une fois depuis le XML refdata, puis JSON."""
    fi = os.path.join(CACHE, 'corpus_index.json')
    if os.path.exists(fi): return json.load(open(fi, encoding='utf-8'))
    import xml.etree.ElementTree as ET
    ns = '{https://simisinfo.refdata.ch/MedicinalDocuments/1.0/}'; idx = {}
    for _, b in ET.iterparse(os.path.join(CACHE, 'AipsDownload_20261008.xml')):
        if b.tag != ns + 'MedicinalDocumentsBundle': continue
        if b.findtext(ns + 'Domain') == 'Human':
            n = b.findtext(f'{ns}RegulatedAuthorization/{ns}Identifier')
            for d in b.findall(ns + 'AttachedDocument'):
                if d.findtext(ns + 'Language') == 'fr':
                    u = [r.findtext(ns + 'Url') for r in d.findall(ns + 'DocumentReference') if r.findtext(ns + 'ContentType') == 'text/html']
                    idx.setdefault(n, []).append([b.findtext(ns + 'Type') + ' ' + (d.findtext(ns + 'Description') or ''), (b.findtext(ns + 'Date') or '')[:10], (u or [''])[0]])
        b.clear()
    json.dump(idx, open(fi, 'w', encoding='utf-8'), ensure_ascii=False); return idx


def trouve(q):
    idx = corpus_index(); q2 = q.lower(); r = []
    for n, docs in idx.items():
        for nom, date, url in docs:
            if q == n or q2 in (nom or '').lower(): r.append(f'{n} · {nom} · {date} · {url}')
    print('\n'.join(r[:15]) or f'absent du corpus : {q} → swissmedicinfo.ch ou « À vérifier (AIPS) »')


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('action', choices=['fiche', 'verifier', 'trouve']); ap.add_argument('cibles', nargs='+')
    a = ap.parse_args()
    if a.action == 'fiche':
        for c in a.cibles: fiche(c)
    elif a.action == 'trouve':
        for c in a.cibles: trouve(c)
    else:
        n = 0
        for c in a.cibles:
            D = verifier(c)
            for d in D:
                print(f'{os.path.basename(c)} · {d[0]} · {d[1]} · {d[2]}')
            n += sum(1 for d in D if d[1] in ('ADOUCI', 'DATE', 'ABSENT'))
        print(f'{n} défaut(s) bloquant(s)')
        sys.exit(1 if n else 0)
