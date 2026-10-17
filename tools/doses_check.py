#!/usr/bin/env python3
"""Pharmakon · contrôle de la table suisse des doses (data/ck/doses_ch.json), zéro jeton.

Chaque ligne doit porter :
  - aips_extrait : au moins un extrait VERBATIM de l'information professionnelle suisse (rubrique + texte) ;
  - url (swissmedicinfo, AIPS) et url_texte (texte officiel publié par Refdata, files.refdata.ch) ;
  - aips_version (date « Mise à jour de l'information » du texte) et aips_publie (date ISO de publication) ;
  - lu_le (date ISO, au plus aujourd'hui) ;
  - chaque nombre des champs dérivés (dose, intervalle, duree, population) présent dans les extraits.
Code de sortie 1 au premier manquement, avec la ligne fautive.
"""
import datetime, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISO = re.compile(r'^20\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$')
NUM = re.compile(r'\d+(?:[.,]\d+)?')
DERIVES = ('dose', 'intervalle', 'duree', 'population')


def norm(t):
    t = re.sub(r'(?<=\d)[ \u00a0\u202f\u2009’\']+(?=\d{3}\b)', '', t)  # 10 000, 1'500 → 10000, 1500
    return t.replace(',', '.')


def nombres(t):
    return {re.sub(r'\.0+$', '', n) for n in NUM.findall(norm(t))}


def check(rows, today=None):
    today = today or datetime.date.today().isoformat()
    errs = []
    for r in rows:
        rid = r.get('id', '?')
        ex = r.get('aips_extrait')
        if not isinstance(ex, list) or not ex or not all(isinstance(e, dict) and e.get('rubrique') and
                                                           isinstance(e.get('texte'), str) and len(e['texte']) >= 20 for e in ex):
            errs.append(f'{rid} : aips_extrait verbatim manquant ou vide')
            continue
        if not re.match(r'^https://(www\.)?(swissmedicinfo\.ch|swissmedicinfo-pro\.ch)/', r.get('url', '')):
            errs.append(f'{rid} : url AIPS (swissmedicinfo) manquante')
        if not r.get('url_texte', '').startswith('https://files.refdata.ch/'):
            errs.append(f'{rid} : url_texte (texte officiel Refdata) manquante')
        if not r.get('aips_version'):
            errs.append(f'{rid} : aips_version (mise à jour de l’information) manquante')
        for k in ('aips_publie', 'lu_le'):
            v = r.get(k, '')
            if not ISO.match(v) or v > today:
                errs.append(f'{rid} : {k} « {v} » n’est pas une date ISO passée')
        texte = ' '.join(e['texte'] for e in ex)
        dispo = nombres(texte)
        for k in DERIVES:
            manque = sorted(nombres(r.get(k, '')) - dispo)
            if manque:
                errs.append(f'{rid} : {k} cite {", ".join(manque)}, absent des extraits verbatim')
    return errs


if __name__ == '__main__':
    p = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'data', 'ck', 'doses_ch.json')
    rows = json.load(open(p, encoding='utf-8'))
    errs = check(rows)
    for e in errs:
        print('ÉCHEC', e)
    print(f'doses_ch : {len(rows)} lignes, {len(errs)} manquement(s).')
    sys.exit(1 if errs else 0)
