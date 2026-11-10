#!/usr/bin/env python3
"""MIGRER_L1 — passe mécanique d'une leçon G vers le prompt L1 (ordre de Vial du 10.11.2026), idempotent, zéro modèle.

1. Supprime l'arbre CIM emboîté (« Où se situe le problème ? »), architecture interdite.
2. Point 1 : « Définition et sémantique » devient « Définition ».
3. Supprime les volets « Notions voisines » (span.dx ou details), interdits au point 1.
4. Transforme chaque fenêtre dépliante (details.fenetre, details.f, span.dx) en fenêtre centrale occultante :
   le résumé devient un lien <a class="ouvre" href="#f-…"> dans la phrase ; le contenu devient
   <section class="fenetre" id="f-…" role="dialog"> placée en fin de <main> (CSS :target, sans script).
Le fond médical n'est jamais réécrit : les phrases, sources et tableaux sont déplacés tels quels.

Usage : python3 Claude/_outils/migrer_l1.py Claude/LOT_00X/LOT_*Phase_*.html
"""
import html as H
import re
import sys


def fin_balise(h, i, tag):
    """Indice juste après la balise fermante correspondant à l'ouvrante <tag située en i (imbrication comprise)."""
    pat = re.compile(rf'<(/?){tag}\b[^>]*>', re.I)
    prof = 0
    for m in pat.finditer(h, i):
        if m.group(0).endswith('/>'):
            continue
        prof += -1 if m.group(1) else 1
        if prof == 0:
            return m.end()
    return -1


def texte(s):
    return H.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s))).strip()


def supprimer_bloc(h, ouvre_re, tag):
    while True:
        m = re.search(ouvre_re, h, re.S)
        if not m:
            return h
        j = fin_balise(h, m.start(), tag)
        if j < 0:
            return h
        h = h[:m.start()] + h[j:]


RE_FEN = re.compile(r'<details\b[^>]*class=["\']?(?:fenetre|f)\b[^>]*>|<span class="dx">')


def migrer(h, prefixe):
    # 1. arbre CIM
    h = supprimer_bloc(h, r'<div class="arb"[^>]*>', 'div')
    h = supprimer_bloc(h, r'<details class="arbre"[^>]*>', 'details')
    # 2. titre du point 1
    h = re.sub(r'Définition et sémantique', 'Définition', h)
    # 3. notions voisines
    while True:
        m = re.search(r'<span class="dx"><input[^>]*><label[^>]*>\s*Notions voisines', h)
        tag = 'span'
        if not m:
            m = re.search(r'<details\b[^>]*>\s*<summary>[^<]*Notions voisines', h)
            tag = 'details'
        if not m:
            m = re.search(r'<span class="tm"[^>]*>\s*Notions voisines', h)
            tag = 'span'
        if not m:
            break
        j = fin_balise(h, m.start(), tag)
        if j < 0:
            break
        h = h[:m.start()] + h[j:]
    h = re.sub(r'<p(?: class="li")?>\s*(?:Détails\s*:)?\s*</p>', '', h)
    # 4. fenêtres centrales, de l'intérieur vers l'extérieur
    fenetres = []
    n = len(re.findall(r'id="f-' + prefixe + r'-\d+"', h))
    while True:
        cand = list(RE_FEN.finditer(h))
        choix = None
        for m in reversed(cand):
            tag = 'span' if m.group(0).startswith('<span') else 'details'
            j = fin_balise(h, m.start(), tag)
            if j > 0 and not RE_FEN.search(h, m.end(), j):
                choix = (m, tag, j)
                break
        if not choix:
            break
        m, tag, j = choix
        bloc = h[m.start():j]
        if tag == 'details':
            s = re.search(r'<summary[^>]*>(.*?)</summary>', bloc, re.S)
            titre = s.group(1).strip() if s else 'Détail'
            corps = bloc[s.end():bloc.rfind('</details>')] if s else bloc
        else:
            s = re.search(r'<label[^>]*>(.*?)</label>', bloc, re.S)
            titre = s.group(1).strip() if s else 'Détail'
            c = re.search(r'<span class="dxc">', bloc)
            corps = bloc[c.end():bloc.rfind('</span>', 0, bloc.rfind('</span>'))] if c else bloc
        n += 1
        fid = f'f-{prefixe}-{n}'
        lien = f'<a class="ouvre" href="#{fid}">{titre}</a>'
        sec = (f'<section class="fenetre" id="{fid}" role="dialog" aria-label="{H.escape(texte(titre), quote=True)}">'
               f'<div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>'
               f'<h4>{titre}</h4>\n{corps}\n</div></section>')
        h = h[:m.start()] + lien + h[j:]
        fenetres.append(sec)
    if fenetres:
        bloc = '\n<!-- fenêtres centrales L1 -->\n' + '\n'.join(fenetres) + '\n'
        k = h.rfind('</main>')
        if k < 0:
            k = h.rfind('</body>')
        h = h[:k] + bloc + h[k:] if k >= 0 else h + bloc
    return h


if __name__ == '__main__':
    for f in sys.argv[1:]:
        h = open(f, encoding='utf-8').read()
        pre = re.sub(r'\W', '', re.search(r'(DX\.\d+|Phase_A)', f).group(1).lower()) if re.search(r'(DX\.\d+|Phase_A)', f) else 'x'
        n = migrer(h, pre)
        if n != h:
            open(f, 'w', encoding='utf-8').write(n)
        print(f"{f.split('/')[-1]} {len(h.encode())}→{len(n.encode())} o, fenêtres {n.count('class=\"fenetre\" id=')}")
