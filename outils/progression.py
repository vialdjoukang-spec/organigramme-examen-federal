#!/usr/bin/env python3
"""PROGRESSION — rend Progression_PR_<IA>.html à partir de la carte de detecteur_lots.py (zéro modèle).
248 LOTs × 11 leçons ; jauge par LOT et par leçon, fluide animé, pourcentage marqué ; filtres par IA.
Le propriétaire de chaque LOT vient d'ATTRIBUTIONS.json (ordre de Vial du 10.11.2026) : un filtre IA n'affiche
que les LOTs dont elle est propriétaire, même si une autre IA y a contribué.

Usage : python3 outils/progression.py --carte carte.json --ia Claude --sortie Claude/Progression_PR_Claude.html
        (--catalogue LOT_Claude_Finaux/CATALOGUE_248.csv par défaut ; noms des SSP)
"""
import os, sys, csv, json, html, argparse, datetime, subprocess, functools

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from attributions import proprietaire, lots_de

LECONS = ['A'] + [f'DX{i}' for i in range(1, 11)]
IAS = ('Claude', 'ChatGPT_Codex', 'Grokbot')


DEPOT = 'vialdjoukang-spec/organigramme-examen-federal'


@functools.lru_cache(maxsize=None)
def _commit(ref):
    if ref in ('origin/main', 'main'):
        return 'main'
    p = subprocess.run(['git', 'rev-parse', ref], capture_output=True, text=True)
    return p.stdout.strip() or ref.replace('origin/', '')


AUDITES = {}  # lot -> réf git de la version auditée (main si fusionnée) ; seuls ces LOTs portent des liens


def lien(r):
    """Lien direct vers le cours audité tel que déposé sur GitHub (rendu HTML via raw.githack, aucune copie)."""
    return f'https://raw.githack.com/{DEPOT}/{_commit(r["ref"])}/{r["chemin"]}'


def lien_audite(lot, l):
    """Lien vers la version auditée d'un LOT de la liste --audites, None sinon."""
    ref = AUDITES.get(lot)
    if not ref:
        return None
    nom = f'LOT_{lot:03d}_Phase_A_V0.html' if l == 'A' else f'LOT_{lot:03d}_Phase_B_V0_DX.{l[2:]}.html'
    return f'https://raw.githack.com/{DEPOT}/{_commit(ref)}/Claude/LOT_{lot:03d}/{nom}'


def teinte_lot(lot):
    """Teinte propre à chaque LOT (angle d'or) : deux LOTs, voisins ou non, n'ont jamais la même couleur."""
    return round((lot * 137.508) % 360, 2)


def jauge(p, grande=False, bloq=False, teinte=None):
    if teinte is None:
        teinte = round(1.35 * p)  # jauges globales : 0 → rouge … 100 → vert d'eau
    return (f'<div class="j{" g" if grande else ""}{" b" if bloq else ""}"><div class="t"><div class="f" '
            f'style="--p:{p}%;--h:{teinte}"></div></div><span>{p} %</span></div>')


def rendre(C, cat, ia_nom, sortie):
    L = C['lecons']
    cartes, tot, parias = [], [], {i: [] for i in IAS}
    for lot in range(1, 249):
        rows = [L.get(f'{lot:03d}:{l}') for l in LECONS]
        p = round(sum(r['score'] if r else 0 for r in rows) / 11)
        tot.append(p)
        prop = proprietaire(lot)
        parias[prop].append(p)
        contrib = sorted({r.get('auteur_ia', r['ia']) for r in rows if r} - {prop, 'inconnu'})
        code, nom = cat.get(lot, ('', ''))
        mini = ''.join(
            f'<div class="l"><b>{(f'<a href="{html.escape(lien_audite(lot, l))}" target="_blank" rel="noopener" title="Ouvrir le cours audité">' if lien_audite(lot, l) else '')}{"Phase A" if l == "A" else "DX." + l[2:]}{" ↗</a>" if lien_audite(lot, l) else ""}</b>{jauge(r["score"] if r else 0, bloq=bool(r and r["bloquant"]), teinte=teinte_lot(lot))}'
            f'<i>{html.escape(r.get("auteur_ia", r["ia"])) if r else "absent"}</i></div>' for l, r in zip(LECONS, rows))
        n = sum(1 for r in rows if r)
        cartes.append(
            f'<article class="c" data-e="{prop}" data-p="{p}"><header><h2>LOT_{lot:03d} <small>{html.escape(code)}</small></h2>'
            f'<p>{html.escape(nom.split("|")[0].strip())}</p>{jauge(p, True, teinte=teinte_lot(lot))}<p class="m">{n}/11 leçons · propriétaire {html.escape(prop)}{(" · contributions " + html.escape(", ".join(contrib))) if contrib else ""}</p></header>'
            f'<details><summary>Leçons</summary><div class="ls">{mini}</div></details></article>')
    if ia_nom in IAS:  # jauge d'une IA : ses seuls LOTs attribués
        tot = [tot[lot - 1] for lot in lots_de(ia_nom)]
    g = round(sum(tot) / len(tot))
    n90, n0 = sum(1 for p in tot if p >= 90), sum(1 for p in tot if p == 0)
    resume = ''.join(f'<div class="ia"><b>{i}</b>{jauge(round(sum(v) / len(v)) if v else 0)}<small>{len(v)} LOTs attribués</small></div>'
                     for i, v in parias.items())
    filtres = ''.join(f'<button data-f="{i}"{" class=on" if i == ia_nom else ""}>{i}</button>' for i in IAS)
    maj = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=1))).strftime('%d.%m.%Y %H:%M')
    doc = f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Progression_PR_{html.escape(ia_nom)}</title><style>
:root{{--fond:#f2f3f5;--carte:#fbfbfc;--encre:#2e3440;--doux:#8a909a;--trait:#dfe2e7;--piste:#e6e8ec}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--fond);color:var(--encre);font:14.5px/1.45 system-ui,-apple-system,"Segoe UI",sans-serif}}
main{{max-width:1240px;margin:0 auto;padding:18px 16px}}h1{{font-size:1.35rem;margin:0 0 4px;letter-spacing:-.01em}}
.top{{background:var(--carte);border:1px solid var(--trait);border-radius:16px;padding:16px 18px;margin-bottom:16px;box-shadow:0 1px 2px rgba(0,0,0,.04),0 8px 24px rgba(30,40,60,.06)}}
.k{{display:flex;gap:26px;flex-wrap:wrap;margin:10px 0 12px}}.k b{{font-size:1.25rem;display:block}}.k small{{color:var(--doux)}}
.ias{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px;margin:12px 0}}.ia{{display:grid;grid-template-columns:110px 1fr;align-items:center;gap:4px 10px}}.ia small{{grid-column:2;color:var(--doux)}}
.fl{{display:flex;gap:6px;flex-wrap:wrap}}.fl button{{border:1px solid var(--trait);background:var(--carte);color:var(--encre);border-radius:999px;padding:5px 12px;cursor:pointer;font:inherit}}
.fl button.on{{background:var(--encre);color:var(--carte);border-color:var(--encre)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:12px}}
.c{{background:var(--carte);border:1px solid var(--trait);border-radius:14px;padding:12px 14px;box-shadow:0 1px 2px rgba(0,0,0,.03),0 6px 16px rgba(30,40,60,.05)}}
.c h2{{font-size:.98rem;margin:0}}.c h2 small{{color:var(--doux);font-weight:500}}.c p{{margin:3px 0 8px;font-size:.84rem}}.m{{color:var(--doux)}}
.j{{display:grid;grid-template-columns:1fr 46px;align-items:center;gap:8px}}.j span{{font-size:.76rem;font-weight:650;text-align:right;font-variant-numeric:tabular-nums}}
.t{{height:8px;background:var(--piste);border-radius:99px;overflow:hidden;box-shadow:inset 0 1px 2px rgba(0,0,0,.08)}}.g .t{{height:13px}}.g span{{font-size:.86rem}}
.f{{height:100%;width:0;border-radius:inherit;position:relative;overflow:hidden;
background:linear-gradient(90deg,hsl(calc(var(--h) - 18) 78% 52%),hsl(var(--h) 80% 48%) 60%,hsl(calc(var(--h) + 14) 85% 56%));
box-shadow:0 0 8px hsl(var(--h) 80% 50% / .35);animation:monte 1.7s cubic-bezier(.2,.8,.2,1) forwards}}
.f::before{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(255,255,255,.45),rgba(255,255,255,0) 60%)}}
.f::after{{content:"";position:absolute;top:0;bottom:0;width:40%;left:-40%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.55),transparent);animation:lueur 2.8s ease-in-out infinite}}
.b .f{{background:linear-gradient(90deg,#c0392b,#e74c3c)}}
@keyframes monte{{to{{width:var(--p)}}}}@keyframes lueur{{0%{{left:-40%}}70%,100%{{left:110%}}}}
@media (prefers-reduced-motion:reduce){{.f{{animation:none;width:var(--p)}}.f::after{{display:none}}}}
details{{margin-top:6px}}summary{{cursor:pointer;font-size:.82rem;color:var(--doux)}}.ls{{display:grid;gap:6px;margin-top:8px}}
.l{{display:grid;grid-template-columns:70px 1fr 92px;gap:8px;align-items:center;font-size:.78rem}}.l a{{color:#2a5d9f;text-decoration:none}}.l a:hover{{text-decoration:underline}}.l i{{color:var(--doux);font-style:normal;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
</style></head><body><main>
<section class="top"><h1>Progression_PR — {html.escape(ia_nom)}</h1>
<div class="k"><div><b>{g} %</b><small>progression globale</small></div><div><b>{n90}</b><small>LOTs ≥ 90 %</small></div>
<div><b>{len(tot) - n90 - n0}</b><small>LOTs en cours</small></div><div><b>{len(tot)}</b><small>LOTs attribués</small></div><div><b>{n0}</b><small>LOTs absents</small></div>
<div><b>{len(L)}/2728</b><small>leçons trouvées</small></div><div><b>{C.get("branches_scannees", "?")}</b><small>branches scannées</small></div>
<div><b>{maj}</b><small>mise à jour (Zurich)</small></div></div>{jauge(g, True)}
<div class="ias">{resume}</div>
<p class="m" style="margin:4px 0 10px">Version la plus avancée de chaque leçon, cherchée sur main et sur toutes les branches. Score : existe 40 · 14 points 20 · bande 100–200 Ko 20 · aucun défaut bloquant 10 · verdict vert 10 ; ancien format multi-DX plafonné à 30. La véracité clinique se contrôle à l'audit.</p>
<div class="fl"><button{' class="on"' if ia_nom not in IAS else ''} data-f="">Tous</button>{filtres}</div></section>
<section class="grid">{''.join(cartes)}</section></main>
<script>
document.querySelectorAll('.fl button').forEach(b=>b.onclick=()=>{{document.querySelectorAll('.fl button').forEach(x=>x.classList.remove('on'));b.classList.add('on');
const f=b.dataset.f;document.querySelectorAll('.c').forEach(c=>c.style.display=(!f||c.dataset.e===f)?'':'none')}});
const d=document.querySelector('.fl button.on');if(d&&d.dataset.f)d.click();
</script></body></html>'''
    os.makedirs(os.path.dirname(sortie) or '.', exist_ok=True)
    open(sortie, 'w').write(doc)
    return g


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--carte', required=True)
    ap.add_argument('--ia', required=True)
    ap.add_argument('--sortie', required=True)
    ap.add_argument('--catalogue', default='LOT_Claude_Finaux/CATALOGUE_248.csv')
    ap.add_argument('--audites', default='', help='LOTs audités et leur réf : 1-4=origin/main,5=origin/claude/lot-005-renfort')
    a = ap.parse_args()
    for part in filter(None, a.audites.split(',')):
        lots, ref = part.split('=')
        x, _, y = lots.partition('-')
        for n in range(int(x), int(y or x) + 1):
            AUDITES[n] = ref
    cat = {}
    if os.path.exists(a.catalogue):
        for r in csv.DictReader(open(a.catalogue, encoding='utf-8')):
            cat[int(r['lot'])] = (r['code'], r['ssp_profiles_2023_fr_en'])
    g = rendre(json.load(open(a.carte)), cat, a.ia, a.sortie)
    print(f'{a.sortie} : progression globale {g} %')
