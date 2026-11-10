#!/usr/bin/env python3
"""PROGRESSION — génère Progression_PR.html : 248 LOTs × 11 leçons (Phase A + DX.1 à DX.10), sans modèle.

Pour chaque leçon, la version retenue est la meilleure trouvée sur main puis sur les branches récentes
(lecture git sans checkout). Score d'une leçon (contrôle structurel, sans paquet) :
  existe 40 · 14 points 20 · bande 100–200 Ko 20 · aucun défaut bloquant 10 · verdict VERT 10
Couleurs admises : vert, rouge, jaune, gris, noir pâle.

Usage : python3 progression.py <depot> --sortie Progression_PR.html [--jours 30] [--rafraichir]
"""
import os, re, sys, csv, io, json, html, time, argparse, subprocess, datetime
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle3

RE_LECON = re.compile(r'LOT_(\d{3})_Phase_(A|B)_V\d+(?:_DX\.(\d{1,2}))?\.html$')
DOSSIERS = {'LOT_Claude_Finaux': 'LOT_Claude_Finaux', 'grok-LOTS-html': 'grok-LOTS-html', 'codex-LOTS-html': 'codex-LOTS-html'}
BLOQUANTS = ('C_points_manquants', 'C_FIN_FICHIER_absent', 'C_balises', 'B_phrase_partagee_entre_fichiers')


def git(d, *a, t=900):
    return subprocess.run(['git', '-C', d, *a], capture_output=True, text=True, errors='ignore', timeout=t).stdout


def rafraichir(d, jours):
    git(d, 'fetch', '-q', '--depth=1', '--filter=tree:0', 'origin', '+refs/heads/*:refs/remotes/origin/*')
    seuil = time.time() - jours * 86400
    refs = [l.split()[1] for l in git(d, 'for-each-ref', '--format=%(committerdate:unix) %(refname:short)', 'refs/remotes').splitlines()
            if l and int(l.split()[0]) >= seuil and l.split()[1] != 'origin/HEAD']
    specs = [f'+refs/heads/{r[7:]}:refs/remotes/{r}' for r in refs if r.startswith('origin/')]
    for i in range(0, len(specs), 40):
        git(d, 'fetch', '-q', '--depth=1', 'origin', *specs[i:i + 40])


def refs_recentes(d, jours):
    seuil = time.time() - jours * 86400
    out = []
    for l in git(d, 'for-each-ref', '--sort=-committerdate', '--format=%(committerdate:unix) %(refname:short)', 'refs/remotes').splitlines():
        ts, r = l.split()
        if r != 'origin/HEAD' and (r == 'origin/main' or int(ts) >= seuil):
            out.append(r)
    return ['origin/main'] + [r for r in out if r != 'origin/main']


def mesurer(args):
    d, ref, chemin = args
    brut = subprocess.run(['git', '-C', d, 'show', f'{ref}:{chemin}'], capture_output=True, timeout=120).stdout
    tmp = f'/tmp/prog_{os.getpid()}.html'
    open(tmp, 'wb').write(brut)

    class A:
        points, min, max, ex, script_ok = 14, 100_000, 200_000, 1, False
    r = controle3.controler(tmp, {}, A, {})
    defs = set(r['defauts'])
    s = 40
    s += 0 if 'C_points_manquants' in defs else 20
    s += 0 if 'C_taille_hors_bande' in defs else 20
    bloq = bool(defs & set(BLOQUANTS))
    s += 0 if bloq else 10
    s += 10 if not defs else 0
    return {'ref': ref, 'chemin': chemin, 'score': s, 'bloquant': bloq, 'octets': len(brut),
            'connect': r['connecteur%'], 'defauts': sorted(defs)}


def collecter(d, jours):
    cand = {}
    for ref in refs_recentes(d, jours):
        for f in git(d, 'ls-tree', '-r', '--name-only', ref).splitlines():
            m = RE_LECON.search(f)
            if not m or f.startswith(('audit', 'qa', '_OBSOLETES')) or '_OBSOLETE' in f:
                continue
            lot, ph, dx = int(m.group(1)), m.group(2), m.group(3)
            lec = 'A' if ph == 'A' else f'DX{int(dx)}'
            cand.setdefault((lot, lec), []).append((ref, f))
    taches = [(d, ref, f) for v in cand.values() for ref, f in v[:3]]  # au plus 3 versions par leçon
    with ProcessPoolExecutor() as ex:
        res = list(ex.map(mesurer, taches, chunksize=8))
    meilleur = {}
    for (dd, ref, f), r in zip(taches, res):
        m = RE_LECON.search(f)
        lot = int(m.group(1)); lec = 'A' if m.group(2) == 'A' else f'DX{int(m.group(3))}'
        cle = (lot, lec)
        r['main'] = ref == 'origin/main'
        if cle not in meilleur or (r['score'], r['main']) > (meilleur[cle]['score'], meilleur[cle]['main']):
            meilleur[cle] = r
    return meilleur


COUL = {'vert': '#2f8f46', 'vert_c': '#cfe8d3', 'rouge': '#b23a3a', 'rouge_c': '#f1d3d3', 'jaune': '#d9a91a',
        'jaune_c': '#f6e7b8', 'gris': '#9a9a9a', 'gris_c': '#e3e3e3', 'gris_f': '#efefef', 'noir': '#3d3d3d'}


def teinte(p, bloq):
    if p == 0:
        return 'gris'
    if bloq:
        return 'rouge'
    return 'vert' if p >= 90 else 'jaune'


def jauge(p, bloq, grande=False):
    t = teinte(p, bloq)
    return (f'<div class="j{" g" if grande else ""}"><div class="f {t}" style="--p:{p}%"></div>'
            f'<span>{p} %</span></div>')


def rendre(meilleur, catalogue, plages, sortie):
    lecons = ['A'] + [f'DX{i}' for i in range(1, 11)]
    cartes, tot = [], []
    for lot in range(1, 249):
        rows = [meilleur.get((lot, l)) for l in lecons]
        sc = [r['score'] if r else 0 for r in rows]
        p = round(sum(sc) / 11)
        tot.append(p)
        bloq_lot = any(r and r['bloquant'] for r in rows)
        code, nom = catalogue.get(lot, ('', ''))
        equipe = next((n for n, (a, b) in plages.items() if a <= lot <= b), '')
        sur_main = sum(1 for r in rows if r and r['main'])
        mini = ''.join(
            f'<div class="l"><b>{"Phase A" if l == "A" else l.replace("DX", "DX.")}</b>{jauge(r["score"] if r else 0, bool(r and r["bloquant"]))}'
            f'<i>{"main" if r and r["main"] else ("branche" if r else "—")}</i></div>' for l, r in zip(lecons, rows))
        cartes.append(
            f'<article class="c" data-e="{html.escape(equipe)}" data-p="{p}"><header><h2>LOT_{lot:03d} <small>{html.escape(code)}</small></h2>'
            f'<p>{html.escape(nom.split("|")[0].strip())}</p>{jauge(p, bloq_lot, True)}'
            f'<p class="m">{sur_main}/11 leçons sur main{" · " + html.escape(equipe) if equipe else ""}</p></header>'
            f'<details><summary>11 leçons</summary><div class="ls">{mini}</div></details></article>')
    g = round(sum(tot) / len(tot))
    n100 = sum(1 for p in tot if p >= 90)
    n0 = sum(1 for p in tot if p == 0)
    filtres = ''.join(f'<button data-f="{html.escape(n)}">{html.escape(n)} ({a}–{b})</button>' for n, (a, b) in plages.items())
    maj = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=1))).strftime('%d.%m.%Y %H:%M')
    doc = f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Progression_PR</title><style>
:root{{--vert:{COUL['vert']};--rouge:{COUL['rouge']};--jaune:{COUL['jaune']};--gris:{COUL['gris']};--noir:{COUL['noir']}}}
*{{box-sizing:border-box}}body{{margin:0;background:{COUL['gris_f']};color:var(--noir);font:15px/1.45 system-ui,sans-serif}}
main{{max-width:1200px;margin:0 auto;padding:16px}}h1{{font-size:1.4rem;margin:0 0 6px}}
.top .j{{background:{COUL['gris_f']}}}.top{{background:{COUL['gris_c']};border:1px solid var(--gris);border-radius:12px;padding:14px;margin-bottom:14px}}
.k{{display:flex;gap:18px;flex-wrap:wrap;margin:8px 0}}.k b{{font-size:1.3rem}}
.fl{{display:flex;gap:6px;flex-wrap:wrap}}.fl button{{border:1px solid var(--gris);background:{COUL['gris_f']};color:var(--noir);border-radius:8px;padding:5px 10px;cursor:pointer}}
.fl button.on{{background:var(--noir);color:{COUL['gris_f']}}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px}}
.c{{background:{COUL['gris_f']};border:1px solid var(--gris);border-radius:12px;padding:12px;box-shadow:3px 4px 0 {COUL['gris_c']}}}
.c h2{{font-size:1.02rem;margin:0}}.c h2 small{{color:var(--gris)}}.c p{{margin:3px 0 8px;font-size:.86rem}}.m{{color:var(--gris)}}
.j{{position:relative;height:16px;background:{COUL['gris_c']};border-radius:9px;overflow:hidden}}.j.g{{height:26px;border-radius:13px}}
.j span{{position:absolute;inset:0;display:grid;place-items:center;font-size:.78rem;font-weight:700;color:var(--noir)}}
.f{{height:100%;width:0;border-radius:inherit;position:relative;overflow:hidden;animation:monte 1.6s ease-out forwards}}
.f::after{{content:"";position:absolute;inset:-60% -100%;background:repeating-linear-gradient(110deg,rgba(255,255,255,.0) 0 14px,rgba(255,255,255,.28) 14px 26px);animation:flot 2.6s linear infinite}}
.f.vert{{background:var(--vert)}}.f.rouge{{background:var(--rouge)}}.f.jaune{{background:var(--jaune)}}.f.gris{{background:var(--gris)}}
@keyframes monte{{to{{width:var(--p)}}}}@keyframes flot{{to{{transform:translateX(52px)}}}}
@media (prefers-reduced-motion:reduce){{.f{{animation:none;width:var(--p)}}.f::after{{animation:none}}}}
details{{margin-top:8px}}summary{{cursor:pointer;font-size:.85rem}}.ls{{display:grid;gap:5px;margin-top:6px}}
.l{{display:grid;grid-template-columns:62px 1fr 52px;gap:6px;align-items:center;font-size:.8rem}}.l i{{color:var(--gris);font-style:normal}}
.leg{{display:flex;gap:12px;flex-wrap:wrap;font-size:.82rem}}.leg span::before{{content:"";display:inline-block;width:11px;height:11px;border-radius:3px;margin-right:4px;vertical-align:-1px;background:var(--x)}}
</style></head><body><main>
<section class="top"><h1>Progression_PR — 248 LOTs</h1><div class="k"><div><b>{g} %</b><br>progression globale</div>
<div><b>{n100}</b><br>LOTs ≥ 90 %</div><div><b>{248 - n100 - n0}</b><br>LOTs en cours</div><div><b>{n0}</b><br>LOTs absents</div>
<div><b>{maj}</b><br>mise à jour (Zurich)</div></div>{jauge(g, False, True)}
<div class="leg" style="margin-top:8px"><span style="--x:var(--vert)">≥ 90 %</span><span style="--x:var(--jaune)">en cours</span>
<span style="--x:var(--rouge)">défaut bloquant</span><span style="--x:var(--gris)">absent</span></div>
<p class="m" style="margin:6px 0 0">Score d'une leçon : existe 40 · 14 points 20 · bande 100–200 Ko 20 · aucun défaut bloquant 10 · verdict vert 10. La véracité clinique se contrôle à l'audit.</p>
<div class="fl" style="margin-top:10px"><button class="on" data-f="">Tous</button>{filtres}</div></section>
<section class="grid">{''.join(cartes)}</section></main>
<script>
document.querySelectorAll('.fl button').forEach(b=>b.onclick=()=>{{document.querySelectorAll('.fl button').forEach(x=>x.classList.remove('on'));b.classList.add('on');
const f=b.dataset.f;document.querySelectorAll('.c').forEach(c=>c.style.display=(!f||c.dataset.e===f)?'':'none')}});
</script></body></html>'''
    open(sortie, 'w').write(doc)
    return g


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('depot')
    ap.add_argument('--sortie', default='Progression_PR.html')
    ap.add_argument('--jours', type=int, default=30)
    ap.add_argument('--rafraichir', action='store_true')
    ap.add_argument('--plages', default='Claude:18-40,Codex:41-80,Grok:100-120')
    a = ap.parse_args()
    d = os.path.abspath(a.depot)
    if a.rafraichir:
        rafraichir(d, a.jours)
    cat = {}
    for r in csv.DictReader(io.StringIO(git(d, 'show', 'origin/main:LOT_Claude_Finaux/CATALOGUE_248.csv'))):
        cat[int(r['lot'])] = (r['code'], r['ssp_profiles_2023_fr_en'])
    plages = {}
    for x in a.plages.split(','):
        n, _, r = x.partition(':')
        lo, _, hi = r.partition('-')
        plages[n] = (int(lo), int(hi))
    M = collecter(d, a.jours)
    json.dump({f'{k[0]:03d}:{k[1]}': v for k, v in sorted(M.items())}, open(os.path.splitext(a.sortie)[0] + '.json', 'w'), ensure_ascii=False)
    g = rendre(M, cat, plages, a.sortie)
    print(f'{a.sortie} : progression globale {g} %, {len(M)} leçons trouvées')
