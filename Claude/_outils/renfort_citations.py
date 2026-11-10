#!/usr/bin/env python3
"""RENFORT_CITATIONS — met une leçon ancienne (citations [Sx] par paragraphe) au format de citation par phrase, sans rien réécrire.
Chaque phrase chiffrée du bloc reçoit les sources que l'auteur citait déjà pour ce bloc (ou, à défaut, pour le bloc précédent
du même point) ; une phrase de dose reçoit les seules sources AIPS du bloc ou, à défaut, l'AIPS de la bibliographie qui nomme la
molécule. La bibliographie reçoit des ancres sb-<id> (aips-<n° Swissmedic> pour une AIPS, S<k> sinon). Mécanique, idempotent.
Usage : python3 renfort_citations.py fichier.html [...]"""
import re, sys, html as H
sys.path.insert(0, __import__('os').path.dirname(__file__))
from controle3 import nombres, STRUCT, DOSE, texte

BLOC = re.compile(r'<(p|li|td|dd|div class="p")((?:\s[^>]*)?)>(.*?)</(p|li|td|dd|div)>', re.S | re.I)
LAB = re.compile(r'href="#source-(S\d+)"')
SPLIT = re.compile(r'(?<=[.!?])(\s+)(?=[A-ZÀ-Ý«])')


def biblio(h):
    ids, noms = {}, {}
    for m in re.finditer(r'<li id="source-(S\d+)">(.*?)</li>', h, re.S):
        t = texte(m.group(2))
        a = re.search(r'(?:autorisation|n°|Swissmedic)\s*(?:n°\s*|Swissmedic\s*)?(\d{5})', t)
        if 'AIPS' in t and a:
            ids[m.group(1)] = f'aips-{a.group(1)}'
            noms[m.group(1)] = t.lower()
        else:
            ids[m.group(1)] = m.group(1)
    return ids, noms


def sup(i, lab):
    return f'<sup class="r"><a href="#sb-{i}">{lab}</a></sup>'


CITID = re.compile(r'<sup class="r"><a href="#sb-([\w.\-:]+)">')


def biblio_sb(h):
    """Format « sb-N » : renomme les ancres AIPS en sb-aips-<n°> (préfixe exigé pour une dose) ; renvoie le HTML et les noms AIPS."""
    noms, ren = {}, {}
    for m in re.finditer(r'<div class="sb" id="sb-(\d+)">(.*?)</div>', h, re.S):
        t = texte(m.group(2))
        a = re.search(r'(?:n°|autorisation)\s*(\d{5})', t)
        if a and re.search(r'AIPS|Swissmedic|swissmedicinfo|information professionnelle', t, re.I):
            nid = f'aips-{a.group(1)}'
            while nid in ren.values():
                nid += 'b'
            ren[m.group(1)] = nid
            noms[nid] = t.lower()
    for old, new in ren.items():
        h = re.sub(rf'(["#])sb-{old}(?=")', rf'\1sb-{new}', h)
        h = re.sub(rf'(<a href="#sb-{new}">){old}(</a>)', rf'\g<1>{old}\2', h)
    return h, noms


def traiter(h):
    ids, noms = biblio(h)
    if not ids and 'id="sb-' in h:
        h, noms_sb = biblio_sb(h)
        return traiter_sb(h, noms_sb)
    if not ids:
        return h, 0
    avant = [None]  # sources du dernier bloc cité (repli pour un bloc sans source dans le même point)
    n = [0]

    def bloc(m):
        tag, attrs, corps, fin = m.groups()
        if 'class="r"' in corps or 'id="source-' in corps:
            return m.group(0)
        labs = list(dict.fromkeys(LAB.findall(corps)))
        if 'class="point"' in attrs:
            avant[0] = None
        if labs:
            avant[0] = labs
        labs = labs or avant[0] or []
        if not labs:
            return m.group(0)
        morceaux = SPLIT.split(corps)
        for k in range(0, len(morceaux), 2):
            p = morceaux[k]
            t = texte(re.sub(r'<span class="sources">.*?</span>', '', p, flags=re.S))
            if len(t.split()) < 4 or not nombres(STRUCT.sub(' ', t)):
                continue
            if DOSE.search(t):
                choix = [l for l in labs if ids.get(l, '').startswith('aips')]
                if not choix:
                    mots = {w.lower() for w in re.findall(r'[A-Za-zÀ-ÿ]{5,}', t)}
                    choix = [l for l, nm in noms.items() if any(w in nm for w in mots)][:2]
                choix = choix or labs
            else:
                choix = labs
            c = ''.join(sup(ids.get(l, l), l) for l in choix)
            mm = re.search(r'([.!?])(\s*(?:</[^>]+>\s*)*)$', p)
            morceaux[k] = p[:mm.start()] + c + p[mm.start():] if mm else p + c
            n[0] += 1
        return f'<{tag}{attrs}>{"".join(morceaux)}</{fin}>'

    h = BLOC.sub(bloc, h)
    for s, i in ids.items():  # ancres de bibliographie
        h = h.replace(f'<li id="source-{s}">', f'<li id="source-{s}"><span id="sb-{i}"></span>', 1) if f'id="sb-{i}"' not in h else h
    return h, n[0]


def traiter_sb(h, noms):
    n = [0]
    avant = [None]

    def bloc(m):
        tag, attrs, corps, fin = m.groups()
        if 'class="sb"' in attrs:
            return m.group(0)
        labs = list(dict.fromkeys(CITID.findall(corps)))
        if labs:
            avant[0] = labs
        labs = labs or avant[0] or []
        if not labs:
            return m.group(0)
        morceaux = SPLIT.split(corps)
        for k in range(0, len(morceaux), 2):
            p = morceaux[k]
            if CITID.search(p):
                if not DOSE.search(texte(p)) or any(c.startswith('aips') for c in CITID.findall(p)):
                    continue
            t = texte(re.sub(r'<sup class="r">.*?</sup>', '', p, flags=re.S))
            if len(t.split()) < 4 or not nombres(STRUCT.sub(' ', t)):
                continue
            if DOSE.search(t):
                choix = [l for l in labs if l.startswith('aips')]
                if not choix:
                    mots = {w.lower() for w in re.findall(r'[A-Za-zÀ-ÿ]{5,}', t)}
                    choix = [i for i, nm in noms.items() if any(w in nm for w in mots)][:2]
                if not choix:
                    continue
            else:
                choix = labs
            c = ''.join(f'<sup class="r"><a href="#sb-{i}">{i.split("-")[-1]}</a></sup>' for i in choix if i not in CITID.findall(p))
            mm = re.search(r'([.!?])(\s*(?:</[^>]+>\s*)*)$', p)
            morceaux[k] = p[:mm.start()] + c + p[mm.start():] if mm else p + c
            n[0] += 1
        return f'<{tag}{attrs}>{"".join(morceaux)}</{fin}>'

    return BLOC.sub(bloc, h), n[0]


if __name__ == '__main__':
    for f in sys.argv[1:]:
        h, n = traiter(open(f, encoding='utf-8').read())
        open(f, 'w', encoding='utf-8').write(h)
        print(f, n, 'phrases citées')
