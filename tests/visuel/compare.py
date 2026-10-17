#!/usr/bin/env python3
"""Automate Iris · comparaison : écarts de pixels, cliquet d'accessibilité, débordement, polices, CLS.

Usage :
  python tests/visuel/compare.py [--sortie qa/visuel/out]                 # compare et juge (code 1 si échec)
  python tests/visuel/compare.py --sortie <dir> --proposer <dir_ref>      # écrit une référence proposée
La référence engagée vit dans qa/visuel/reference/ (WebP sans perte) et qa/visuel/reference.json.
Elle ne change que par l'étiquette « visuel:nouvelle-reference » suivie d'un commit explicite (skill ssp-qualite-visuelle).
"""
import argparse, collections, json, os, shutil, sys
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CFG = json.load(open(os.path.join(ROOT, 'qa', 'visuel', 'config.json'), encoding='utf-8'))
REF_DIR = os.path.join(ROOT, 'qa', 'visuel', 'reference')
REF_JSON = os.path.join(ROOT, 'qa', 'visuel', 'reference.json')
BLOQ = set(CFG['axe']['impacts_bloquants'])
MARK = '<!-- iris-visuel -->'


def load(p):
    return np.asarray(Image.open(p).convert('RGB')).astype(np.int16)


def a11y_counts(M):
    out = {}
    for k, vs in M.get('axe', {}).items():
        c = collections.Counter()
        for v in vs:
            if v['impact'] in BLOQ:
                c[v['id']] += v['noeuds']
        out[k] = dict(sorted(c.items()))
    return out


def ratio(a, b):
    if a.shape != b.shape:
        return None, None
    m = np.abs(a - b).max(axis=2) > CFG['pixel']['tolerance_canal']
    return float(m.mean()), m


def diff_image(ref, cur, mask, path):
    """Trois volets : référence | actuel | écarts en rouge sur l'actuel grisé."""
    h = max(ref.shape[0], cur.shape[0]); w = ref.shape[1] + cur.shape[1] + cur.shape[1]
    canvas = np.full((h, w, 3), 255, np.uint8)
    canvas[:ref.shape[0], :ref.shape[1]] = ref
    canvas[:cur.shape[0], ref.shape[1]:ref.shape[1] + cur.shape[1]] = cur
    g = (cur.mean(axis=2, keepdims=True) * .35 + 165).astype(np.uint8).repeat(3, 2)
    if mask is not None:
        g[mask] = (220, 20, 60)
    canvas[:cur.shape[0], ref.shape[1] + cur.shape[1]:] = g
    im = Image.fromarray(canvas)
    if im.width > 2400:
        im = im.resize((2400, int(im.height * 2400 / im.width)))
    im.save(path, optimize=True)


def proposer(sortie, dest):
    M = json.load(open(os.path.join(sortie, 'mesures.json'), encoding='utf-8'))
    rd = os.path.join(dest, 'reference'); shutil.rmtree(rd, ignore_errors=True); os.makedirs(rd)
    for k, rel in M['captures'].items():
        Image.open(os.path.join(sortie, rel)).save(os.path.join(rd, k + '.webp'), lossless=True, method=6)
    ref = {'_doc': 'Référence de l’automate Iris. Les nombres sont des plafonds (cliquet) : ils ne peuvent que baisser sans étiquette.',
           'horloge': M['horloge'], 'cls': M['cls'], 'a11y': a11y_counts(M)}
    json.dump(ref, open(os.path.join(dest, 'reference.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'Référence proposée : {len(M["captures"])} captures → {rd}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sortie', default=os.path.join(ROOT, 'qa', 'visuel', 'out'))
    ap.add_argument('--proposer')
    ap.add_argument('--non-bloquant', action='store_true', help='étiquette posée : le titre invite à adopter la référence proposée')
    a = ap.parse_args()
    if a.proposer:
        return proposer(a.sortie, a.proposer)
    M = json.load(open(os.path.join(a.sortie, 'mesures.json'), encoding='utf-8'))
    R = json.load(open(REF_JSON, encoding='utf-8')) if os.path.exists(REF_JSON) else {'cls': {}, 'a11y': {}}
    dd = os.path.join(a.sortie, 'diff'); os.makedirs(dd, exist_ok=True)
    fails, warns, rows, gains = [], [], [], []
    # 1. Pixels
    nchg = 0
    for k, rel in sorted(M['captures'].items()):
        cur = load(os.path.join(a.sortie, rel)); rp = os.path.join(REF_DIR, k + '.webp')
        if not os.path.exists(rp):
            fails.append(f'`{k}` : aucune capture de référence'); rows.append((k, 'référence absente')); continue
        ref = load(rp); r, m = ratio(ref, cur)
        if r is None:
            fails.append(f'`{k}` : dimensions {ref.shape[1]}×{ref.shape[0]} → {cur.shape[1]}×{cur.shape[0]}')
            rows.append((k, 'dimensions changées')); diff_image(ref, cur, None, os.path.join(dd, k + '.png')); nchg += 1; continue
        if r > CFG['pixel']['ratio_max']:
            fails.append(f'`{k}` : {r * 100:.2f} % des pixels changent (seuil {CFG["pixel"]["ratio_max"] * 100:.1f} %)')
            rows.append((k, f'{r * 100:.2f} %')); diff_image(ref, cur, m, os.path.join(dd, k + '.png')); nchg += 1
    # 2. Accessibilité (cliquet) et contraste
    cur_a = a11y_counts(M); ref_a = R.get('a11y', {})
    new_a, contrast = [], collections.Counter()
    for k, c in cur_a.items():
        base = ref_a.get(k)
        for rule, n in c.items():
            if rule == 'color-contrast':
                contrast[k.split('_')[0]] += n
            b = (base or {}).get(rule, 0) if base is not None else None
            if b is None:
                new_a.append(f'`{k}` · {rule} : {n} (aucune référence)')
            elif n > b:
                new_a.append(f'`{k}` · {rule} : {b} → {n}')
        for rule, b in (base or {}).items():
            if c.get(rule, 0) < b:
                gains.append(f'`{k}` · {rule} : {b} → {c.get(rule, 0)}')
    fails += [f'accessibilité, nouveau problème grave : {x}' for x in new_a]
    # 3. Débordement horizontal (bloquant sur mobile)
    for k, d in sorted(M['debordement'].items()):
        if d['deborde']:
            msg = f'`{k}` déborde : {d["largeur_defilement"]} px pour {d["largeur"]} px ({"; ".join(d["fautifs"][:3])})'
            (fails if '_mobile_' in k else warns).append('débordement horizontal ' + msg)
    # 3 bis. Texte coupé sans ellipse ni texte complet (bloquant, ordinateur et mobile)
    ncut = 0
    for k, L in sorted(M.get('texte_coupe', {}).items()):
        for x in L:
            ncut += 1
            fails.append(f'`{k}` : texte coupé ({x["sens"]}) dans {x["el"]} « {x["texte"]} »')
    # 4. Polices
    ext = set()
    for k, f in M['polices'].items():
        if f['echecs']:
            fails.append(f'`{k}` : police non chargée ({", ".join(f["echecs"][:4])})')
        ext.update(f['externes'])
    hl = M.get('hors_ligne', {})
    off = None
    if hl:
        a1, b1 = load(os.path.join(a.sortie, hl['capture'])), load(os.path.join(a.sortie, hl['compare_a']))
        off, mo = ratio(a1, b1)
        if hl.get('erreurs_page'):
            fails.append('hors ligne : erreurs de page ' + '; '.join(hl['erreurs_page'][:3]))
        if off is None or off > CFG['pixel']['ratio_max']:
            msg = (f'hors ligne, le rendu change ({"dimensions" if off is None else f"{off * 100:.2f} % des pixels"}) : '
                   'une ressource externe (CDN de polices) conditionne l’affichage')
            (fails if CFG['polices_externes'] == 'bloquer' else warns).append(msg)
            diff_image(b1, a1, mo, os.path.join(dd, 'hors-ligne.png'))
    if ext:
        msg = 'polices ou feuilles de style chargées depuis le réseau : ' + ', '.join(x.split()[1][:60] for x in sorted(ext)[:3])
        (fails if CFG['polices_externes'] == 'bloquer' else warns).append(msg)
    # 5. Décalage de mise en page (CLS au chargement, cliquet)
    for k, v in M['cls'].items():
        lim = max(CFG['cls_max'], R.get('cls', {}).get(k, 0) + 0.02)
        if v > lim:
            fails.append(f'`{k}` : CLS {v} (plafond {lim:.3f})')
        elif v > CFG['cls_max']:
            warns.append(f'`{k}` : CLS {v} au-dessus de {CFG["cls_max"]} (toléré par la référence)')
    for k, e in M['erreurs_page'].items():
        if e:
            fails.append(f'`{k}` : erreur JavaScript ({e[0]})')
    # Rapport
    ok = not fails
    L = [MARK, f'## Iris · qualité visuelle : {"✅ conforme" if ok else ("🟡 changements à adopter : référence proposée dans l’artefact visuel-reference-proposee" if a.non_bloquant else "❌ régression")}', '',
         '| Contrôle | Résultat |', '|---|---|',
         f'| Captures comparées | {len(M["captures"])} ({len(CFG["variantes"])} variantes × {len(CFG["profils"])} profils × {len(CFG["onglets"]) + len(CFG["etats"])} vues), {nchg} changée(s) |',
         f'| Accessibilité axe-core (graves et critiques) | {sum(sum(c.values()) for c in cur_a.values())} nœuds, {len(new_a)} nouveau(x) |',
         f'| Texte coupé sans ellipse ni texte complet | {ncut} élément(s), {len(M.get("texte_coupe", {}))} vue(s) contrôlée(s) |',
         '| Contraste WCAG AA (color-contrast, nœuds) | ' + (', '.join(f'{v} : {n}' for v, n in sorted(contrast.items())) or 'aucun écart') + ' |',
         f'| Débordement horizontal mobile | {sum(1 for k, d in M["debordement"].items() if d["deborde"] and "_mobile_" in k)} vue(s) |',
         f'| Polices | {sum(len(f["echecs"]) for f in M["polices"].values())} échec(s), {len(ext)} externe(s), rendu hors ligne {"identique" if off is not None and off <= CFG["pixel"]["ratio_max"] else "différent"} |',
         f'| CLS au chargement (max) | {max(M["cls"].values()) if M["cls"] else 0} (seuil {CFG["cls_max"]}) |', '']
    if fails:
        L += ['### Échecs', *[f'- {x}' for x in fails[:60]], '']
    if warns:
        L += ['### Avertissements', *[f'- {x}' for x in warns[:30]], '']
    if gains:
        L += ['### Gains (la référence peut être resserrée)', *[f'- {x}' for x in gains[:30]], '']
    L += ['Les captures, les images d’écart (référence | actuel | écarts en rouge) et la référence proposée sont dans l’artefact **visuel-rapport**.',
          'Pour accepter un changement voulu : étiquette `visuel:nouvelle-reference`, puis `tools/visuel_reference.sh <PR>` (skill ssp-qualite-visuelle).']
    open(os.path.join(a.sortie, 'rapport.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    json.dump({'echecs': fails, 'avertissements': warns, 'gains': gains}, open(os.path.join(a.sortie, 'rapport.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'Iris : {len(fails)} échec(s), {len(warns)} avertissement(s), {nchg} capture(s) changée(s).')
    for x in fails[:20]:
        print('  ÉCHEC', x)
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
