#!/usr/bin/env python3
"""GLOSSAIRE — porte des sigles et des scores (ordre de Vial du 13.11.2026), zéro modèle. Code 1 en cas d'échec.

Tout sigle (2 à 6 majuscules ou chiffres, commençant par une lettre) et tout score cité dans une fiche remplie doit
exister dans Claude/_progression/glossaire.json : « abreviations » (sigle → définition développée) et « scores »
(nom → définition, cotation item par item, interprétation, source). La page (outils/receptacle.py) enveloppe chaque
sigle d'un survol <abbr> et ouvre chaque score dans une fenêtre au clic ; elle applique la même détection.
Ne sont pas des sigles : chiffres romains, codes de système (S1–S12), lettre + chiffres (vitamine B12, J7, C3, F20),
identifiants de fiches et champs bibliographiques (« sources », « source » : initiales d'auteurs).
Sigles à casse mixte (PaO2, IgE, COHb, HbA1c, eGFR, hCG, NT-proBNP…) : tout segment qui mêle minuscules et au moins
deux majuscules, ou une majuscule après la première lettre. Un mot composé par tirets (anti-HBc, TnI-hs, NT-proBNP) est
lu de gauche à droite en prenant à chaque position la plus longue suite de segments présente au glossaire ; un segment
à casse mixte qui ne s'y trouve pas est signalé. Unités (mL, kPa, mmHg, mU, mOsm…) exclues.
Un score est cité par son nom ou ses alias, ou par « score (de) Nom » : le nom doit exister dans « scores ».
Usage : python3 Claude/_progression/glossaire.py [--contexte]     (controle.py appelle aussi cette porte)
"""
import glob, json, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
DON = os.path.join(ICI, 'donnees')
GLO = os.path.join(ICI, 'glossaire.json')
V = '—'
# Sigle = mot de 2 à 9 signes portant au moins deux capitales : capitales seules (HUG), casse mixte (sTfR, PcP, HBs)
# ou capitales collées à un chiffre (ADAMTS13) ; audit verbal_vv_s10, restant 12.
SIGLE = re.compile(r'(?<![0-9A-Za-zÀ-ÖØ-öø-ÿ_])((?=[0-9A-Za-zÀ-ÖØ-öø-ÿ]*[A-ZÀ-ÖØ-Þ][0-9a-zß-öø-ÿ]*[A-ZÀ-ÖØ-Þ])'
                   r'[A-Za-zÀ-ÖØ-öø-ÿ][0-9A-Za-zÀ-ÖØ-öø-ÿ]{1,8})(?![0-9A-Za-zÀ-ÖØ-öø-ÿ_])')
NON_SIGLE = re.compile(r'^(?:[IVXL]+|S1[0-2]|S\d|[A-Z]\d{1,3}|EX|PH|PS|SF)$')
ID = re.compile(r'^(?:EX-\d|PH|PS|SF)-[A-Za-z0-9.-]+$')
MOT = re.compile(r'(?<![0-9A-Za-zÀ-ÖØ-öø-ÿ_-])([A-Za-z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)+|[A-Za-z][A-Za-z0-9]*)(?![0-9A-Za-zÀ-ÖØ-öø-ÿ_])')
MIXTE = re.compile(r'^(?=.*[a-z])(?:.+[A-Z]|[A-Z].*[A-Z])')
UNITE = re.compile(r'^(?:[mµnpfkcd]?(?:L|Pa|U|UA|UI|IU|Eq|Osm|Da|Hz|Hg|mHg|H2O|gH2O|gH))$|^(?:mmHg|cmH2O|kgH|kgH2O|mosmol|kDa)$')
URL = re.compile(r'https?://\S+')
META = {'id', 'module', 'type', 'titre', 'systeme', 'etiquettes', 'passerelles', 'sous_onglet', 'entree_primaire', 'axe_secondaire',
        'classe', 'sous_classe', 'bloc', 'code_cim10', 'sources', 'source'}


def textes(x, cle=''):
    """Chaînes affichées d'une fiche, hors métadonnées, identifiants et champs bibliographiques."""
    if isinstance(x, dict):
        for k, v in x.items():
            if k not in META:
                yield from textes(v, k)
    elif isinstance(x, list):
        for v in x:
            yield from textes(v, cle)
    elif isinstance(x, str) and x.strip() != V and not ID.match(x):
        yield URL.sub(' ', x)


def mixte(p):
    return bool(MIXTE.match(p)) and not UNITE.match(p) and not NON_SIGLE.match(p)


def sigles(t, connus=frozenset()):
    """Sigles en majuscules, puis sigles à casse mixte (seuls ou dans un mot composé par tirets)."""
    r = [m.group(1) for m in SIGLE.finditer(t) if not NON_SIGLE.match(m.group(1))]
    for m in MOT.finditer(t):
        p, i = m.group(1).split('-'), 0
        while i < len(p):
            j = next((j for j in range(len(p), i, -1) if '-'.join(p[i:j]) in connus), None)
            if j and (j - i > 1 or mixte(p[i])):
                r.append('-'.join(p[i:j]))
                i = j
                continue
            if mixte(p[i]):
                r.append(p[i])
            i += 1
    return r


SCORE_CITE = re.compile(r"\b[Ss]cores? (?:de |du |d'|des )?([A-Z0-9][\w-]*)")


def noms_scores(sc):
    """Noms affichables d'un score : sa clé et ses alias (« Glasgow » pour GCS)."""
    return {n: k for k, v in sc.items() for n in [k] + v.get('alias', [])}

def remplie(f):
    return any(True for _ in textes(f))


def fiches():
    for p in sorted(glob.glob(os.path.join(DON, '*', '*.json'))):
        f = json.load(open(p, encoding='utf-8'))
        if remplie(f):
            yield f


def verifier(don=DON, glo=GLO):
    """Erreurs de la porte (liste de chaînes) et nombre de fiches remplies."""
    global DON
    DON = don
    g = json.load(open(glo, encoding='utf-8')) if os.path.exists(glo) else {}
    ab, sc, hors = g.get('abreviations', {}), g.get('scores', {}), g.get('hors_sigles', {})
    noms = noms_scores(sc)
    connus = frozenset(ab) | frozenset(noms) | frozenset(hors)
    err, manq, n = [], {}, 0
    for k, s in sc.items():
        for c in ('definition', 'cotation', 'interpretation', 'source'):
            if not s.get(c) or s.get(c) == V:
                err.append(f'glossaire : score {k}, champ « {c} » vide')
        for c in s.get('cotation', []):
            if not (isinstance(c, dict) and c.get('item') and c.get('points') not in (None, '')):
                err.append(f'glossaire : score {k}, ligne de cotation sans item ou points')
        for c in s.get('interpretation', []):
            if not (isinstance(c, dict) and c.get('plage') and c.get('sens')):
                err.append(f'glossaire : score {k}, interprétation sans plage ou sens')
    for k, d in ab.items():
        if not d or d == V:
            err.append(f'glossaire : sigle {k}, définition vide')
    for f in fiches():
        n += 1
        for t in textes(f):
            for s in sigles(t, connus):
                if s not in ab and s not in noms and s not in hors:
                    manq.setdefault(s, []).append((f['id'], t))
            for m in SCORE_CITE.finditer(t):
                w = m.group(1)
                if not any(x == w or x.split()[0] == w for x in noms):
                    manq.setdefault('score ' + w, []).append((f['id'], t))
    for s, l in sorted(manq.items()):
        err.append(f'glossaire : {s} absent ({l[0][0]}, {len(l)} occurrence(s))')
    return err, n, manq, len(ab), len(sc)


def main():
    err, n, manq, nab, nsc = verifier()
    if '--contexte' in sys.argv:
        for s, l in sorted(manq.items()):
            i, t = l[0]
            print(f'{s}\t{len(l)}\t{i}\t{t[:120]}')
        return 0
    print(f'GLOSSAIRE · {n} fiches remplies · {nab} sigles · {nsc} scores')
    for m in err[:18]:
        print('  ✗', m)
    if len(err) > 18:
        print(f'  … {len(err) - 18} autres échecs')
    print('VERT' if not err else f'ROUGE : {len(err)} échec(s)')
    return 1 if err else 0


if __name__ == '__main__':
    sys.exit(main())
