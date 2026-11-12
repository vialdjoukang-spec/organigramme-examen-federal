#!/usr/bin/env python3
"""RÉSUMEUR — mémoire persistante d'un LOT (zéro modèle). Un agent lit MEMOIRE.md (≈ 3–6 Ko) au lieu de relire
onze cours (≈ 950 Ko), les audits et les sources : état gelé, tailles, verdicts, fiches AIPS, restants d'audit,
sources déjà lues réutilisables, lacunes. Régénéré à chaque commit (gratuit) ; jamais lu en entier par un humain.

Usage : python3 Claude/_harnais/resumeur.py 23 [24 …]      → Claude/LOT_0NN/MEMOIRE.md
        python3 Claude/_harnais/resumeur.py --global        → Claude/_harnais/MEMOIRE_GLOBALE.md (une ligne par LOT)
"""
import re, os, sys, json, glob, html, hashlib, subprocess, collections


def txt(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()


def controle(fichiers):
    try:
        r = subprocess.run([sys.executable, 'Claude/_outils/controle3.py', '--script-ok'] + fichiers,
                           capture_output=True, text=True, timeout=300)
        return {os.path.basename(x['fichier']): (x['verdict'], x['octets']) for x in json.loads(r.stdout)}
    except Exception:
        return {}


def lot(n):
    d = f'Claude/LOT_{n:03d}'
    if not os.path.isdir(d):
        return None
    F = sorted(glob.glob(f'{d}/LOT_{n:03d}_Phase_*.html'), key=lambda f: (('DX.' in f), int(re.search(r'DX\.(\d+)', f).group(1)) if 'DX.' in f else 0))
    C = controle(F)
    o = [f'# Mémoire LOT_{n:03d} (résumeur, {len(F)} fichiers)\n']
    liste = open(f'{d}/LISTE_DX_CANONIQUE.md', encoding='utf-8').read() if os.path.exists(f'{d}/LISTE_DX_CANONIQUE.md') else ''
    o.append('## Liste gelée\n' + '\n'.join(l for l in liste.splitlines() if l.startswith('DX.')) + '\n')
    o.append('## Fichiers\n| Fichier | Titre | Octets | controle3 | Fenêtres | Fiches .mb (AIPS) | Sources | sha8 |\n|---|---|---|---|---|---|---|---|')
    sources = collections.OrderedDict()
    for f in F:
        h = open(f, encoding='utf-8').read()
        mt = re.search(r'<h3[^>]*>\s*(?:<strong>)?\s*DX\.\d+\s*[—-]\s*(.*?)<', h) or re.search(r'class="fm-nom">(.*?)<', h)
        titre = txt(mt.group(1))[:44] if mt else ''
        mb = re.findall(r'<section class="fenetre mb" id="[^"]+"[^>]*aria-label="([^"]+)"', h)
        aips = sorted(set(re.findall(r'id="sb-aips-(\d+)"', h)))
        for sid, corps in re.findall(r'<li id="sb-([\w-]+)">(.*?)</li>', h, re.S):
            u = re.search(r'https?://\S+', txt(corps))
            if u:
                sources.setdefault(u.group(0).rstrip('.'), re.sub(r'^\[[^\]]*\]\s*', '', txt(corps))[:70])
        v, b = C.get(os.path.basename(f), ('?', len(h.encode())))
        o.append(f'| {os.path.basename(f).replace(f"LOT_{n:03d}_", "")} | {titre} | {b} | {v} | {h.count("class=\"fenetre")} | '
                 f'{len(mb)} ({",".join(aips)}) | {len(re.findall(r"<li id=\"sb-", h))} | {hashlib.sha256(h.encode()).hexdigest()[:8]} |')
    o.append('\n## Audits')
    for a in sorted(glob.glob(f'{d}/audits/*.json')):
        try:
            j = json.load(open(a, encoding='utf-8'))
        except Exception:
            continue
        r = j.get('restants') or []
        g = collections.Counter((x.get('gravite') or x.get('classe') or '?') for x in r if isinstance(x, dict))
        o.append(f'- {os.path.basename(a)} : verdict {j.get("verdict")}, {dict(g)}' + (f', seconde passe {j["seconde_passe"].get("verdict")}' if isinstance(j.get('seconde_passe'), dict) else ''))
        for x in r[:12]:
            if isinstance(x, dict) and (x.get('gravite') or '') in ('Critique', 'Grave'):
                o.append(f'  - {x.get("gravite")} · {x.get("fichier", "")} · {txt(str(x.get("constat", "")))[:140]}')
    if os.path.exists(f'{d}/HELP.md'):
        o.append('\n## Lacunes (HELP.md, 8 dernières)\n' + '\n'.join(open(f'{d}/HELP.md', encoding='utf-8').read().strip().splitlines()[-8:]))
    o.append(f'\n## Sources déjà lues dans ce LOT ({len(sources)}) — réutiliser avant toute recherche\n' +
             '\n'.join(f'- {v} — {u}' for u, v in list(sources.items())[:45]) + ('\n- (+ %d autres : grep -h \'<li id="sb-\' dans les cours)' % (len(sources) - 45) if len(sources) > 45 else ''))
    m = '\n'.join(o) + '\n'
    open(f'{d}/MEMOIRE.md', 'w', encoding='utf-8').write(m)
    return n, len(F), sum(1 for v in C.values() if v[0] == 'VERT'), len(m.encode())


if __name__ == '__main__':
    if '--global' in sys.argv:
        lignes = []
        for d in sorted(glob.glob('Claude/LOT_[0-9][0-9][0-9]')):
            n = int(d[-3:]); ca = f'{d}/audits/contre_audit.audit.json'
            v = json.load(open(ca)).get('verdict') if os.path.exists(ca) else '—'
            lignes.append(f'| {n} | {len(glob.glob(d + "/*_Phase_*.html"))} | {"oui" if os.path.exists(d + "/LISTE_DX_CANONIQUE.md") else "non"} | {v} |')
        open('Claude/_harnais/MEMOIRE_GLOBALE.md', 'w').write('# Mémoire globale\n| LOT | fichiers | liste gelée | contre-audit |\n|---|---|---|---|\n' + '\n'.join(lignes) + '\n')
        print(len(lignes), 'LOTs')
    for a in sys.argv[1:]:
        if a.isdigit():
            print(lot(int(a)))
