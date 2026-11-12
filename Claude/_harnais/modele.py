#!/usr/bin/env python3
"""MODÈLE — prévision multivariée de la consommation (zéro modèle de langage ; numpy seulement).

1. Identité mécanique, vérifiée sur chaque agent :  coût ≈ 0,1·Σ contexte lu + 1,25·cache écrit + 5·sortie,
   avec Σ contexte lu ≈ T·(C0 + g·T/2) : T tours, C0 contexte de départ, g croissance du contexte par tour.
2. Régression log-linéaire a priori (connue avant le lancement) : log(coût) ~ type de tâche + nombre de DX,
   intervalles par bootstrap (2 000 tirages) et intervalle de prédiction par résidus.
3. Monte-Carlo d'un LOT standard (Phase A, P1, 5 agents × 2 DX, 2 audits, 2 corrections, contre-audit, audits
   de Phase A) : médiane, IC 80 % et 95 % ; puis scénarios du harnais (leviers chiffrés, hypothèses explicites).
Entrée : Claude/_harnais/donnees/agents.jsonl (suivi.py) + journaux pour la trajectoire de contexte.
Sortie : Claude/_harnais/donnees/modele.json
"""
import os, sys, json, os, glob, re, sys, math, random
import numpy as np

random.seed(7); np.random.seed(7)
PROJ = os.path.expanduser('~/.claude/projects')


def trajectoire(aid):
    f = glob.glob(os.path.join(PROJ, '*', '*', 'subagents', f'agent-{aid}.jsonl'))
    if not f:
        return None
    ctx = []
    for l in open(f[0], encoding='utf-8', errors='ignore'):
        try:
            d = json.loads(l)
        except Exception:
            continue
        u = (d.get('message') or {}).get('usage') if d.get('type') == 'assistant' else None
        if u:
            ctx.append((u.get('cache_read_input_tokens') or 0) + (u.get('cache_creation_input_tokens') or 0) + (u.get('input_tokens') or 0))
    if len(ctx) < 6:
        return None
    T = len(ctx); x = np.arange(T)
    g = float(np.polyfit(x, ctx, 1)[0])
    return dict(T=T, C0=float(np.mean(ctx[:3])), Cfin=float(np.mean(ctx[-3:])), g=g, Cmoy=float(np.mean(ctx)))


A = [json.loads(l) for l in open('Claude/_harnais/donnees/agents.jsonl', encoding='utf-8')]
A = [a for a in A if a['type'] != 'principal' and a['tours'] > 5 and a.get('fini')]
# Trajectoires conservées dans le dépôt : une machine vierge (journaux locaux absents) garde l'historique.
FT = 'Claude/_harnais/donnees/trajectoires.json'
TR = json.load(open(FT, encoding='utf-8')) if os.path.exists(FT) else {}
for a in A:
    a['traj'] = trajectoire(a['id']) or TR.get(a['id'])
    if a['traj']: TR[a['id']] = a['traj']
    a['ndx'] = 2 if a['type'] == 'redaction_2DX' else 1
json.dump(TR, open(FT, 'w', encoding='utf-8'))
A = [a for a in A if a['traj']]
if len(A) < 20:
    print(f'Données insuffisantes ({len(A)} agents avec trajectoire) : modele.json conservé tel quel.'); sys.exit(0)
# 1. identité mécanique
pred = [0.1 * a['traj']['T'] * a['traj']['Cmoy'] + 1.25 * a['cache_creation_input_tokens'] + 5 * a['output_tokens'] for a in A]
obs = [a['cout'] for a in A]
r2_id = 1 - sum((o - p) ** 2 for o, p in zip(obs, pred)) / sum((o - np.mean(obs)) ** 2 for o in obs)
# 2. régression log-linéaire
types = sorted({a['type'] for a in A})
def X(a):
    return [1.0] + [1.0 if a['type'] == t else 0.0 for t in types[1:]]
Xm = np.array([X(a) for a in A]); y = np.log([a['cout'] for a in A])
beta, *_ = np.linalg.lstsq(Xm, y, rcond=None)
res = y - Xm @ beta; s = float(np.std(res, ddof=Xm.shape[1]))
r2 = 1 - float(np.sum(res ** 2) / np.sum((y - y.mean()) ** 2))
boot = []
for _ in range(2000):
    i = np.random.randint(0, len(A), len(A))
    b, *_ = np.linalg.lstsq(Xm[i], y[i], rcond=None); boot.append(b)
boot = np.array(boot)
def pred_type(t):
    v = np.array(X(dict(type=t)))
    m = float(v @ beta); lo, hi = np.percentile(boot @ v, [2.5, 97.5])
    return dict(mediane=math.exp(m) / 1e6, ic95_moyenne=[math.exp(lo) / 1e6, math.exp(hi) / 1e6],
                ip95_agent=[math.exp(m - 1.96 * s) / 1e6, math.exp(m + 1.96 * s) / 1e6])
parType = {t: pred_type(t) for t in types}
stats = {}
for t in types:
    L = [a for a in A if a['type'] == t]
    stats[t] = dict(n=len(L), T=float(np.median([a['traj']['T'] for a in L])), C0=float(np.median([a['traj']['C0'] for a in L])),
                    Cfin=float(np.median([a['traj']['Cfin'] for a in L])), g=float(np.median([a['traj']['g'] for a in L])),
                    sortie=float(np.median([a['output_tokens'] for a in L])), cout=float(np.median([a['cout'] for a in L])) / 1e6,
                    web=float(np.median([a['outils'].get('_web', 0) for a in L])), aips=float(np.median([a['outils'].get('_aips', 0) for a in L])),
                    lectures=float(np.median([a['outils'].get('_lectures', 0) for a in L])))
# 3. Monte-Carlo d'un LOT standard, puis scénarios mécaniques : chaque agent tiré est recalculé avec l'identité (1),
#    leviers du harnais tirés dans des plages prudentes (incertitude propagée dans l'intervalle).
LOT = {'redaction_2DX': 5, 'audit': 4, 'correction': 2, 'contre_audit': 2, 'gel_P1': 1, 'recherche': 2}
LEV = dict(C0=(0.08, 0.15),   # socle : dépôt MEDINA hors session (CLAUDE.md 28 Ko ≈ 9 k tokens) + brief compact
           T=(0.15, 0.35),    # tours : appels groupés, rédaction par générateur (contenu.py → gen.py), portes avant audit
           g=(0.15, 0.35))    # croissance du contexte : MEMOIRE.md, fiches AIPS compactes, sources_cache
def recalc(a, lc, lt, lg):
    t = a['traj']; T, C0, g = t['T'], t['C0'], max(t['g'], 0)
    k = a['cache_read_input_tokens'] / max(1.0, T * C0 + g * T * T / 2)
    T2, C02, g2 = T * (1 - lt), C0 * (1 - lc), g * (1 - lg)
    cr2 = k * (T2 * C02 + g2 * T2 * T2 / 2)
    return (0.1 * cr2 + 1.25 * a['cache_creation_input_tokens'] * (1 - lt) + 5 * a['output_tokens'] + a['input_tokens']) / 1e6
par = {t: [a for a in A if a['type'] == t] for t in types}
def tirage_lot(harnais):
    tot = 0.0
    lc, lt, lg = (random.uniform(*LEV['C0']), random.uniform(*LEV['T']), random.uniform(*LEV['g'])) if harnais else (0, 0, 0)
    for t, n in LOT.items():
        for _ in range(n):
            if par.get(t):
                tot += recalc(random.choice(par[t]), lc, lt, lg)
    return tot
base = sorted(tirage_lot(False) for _ in range(20000))
harn = sorted(tirage_lot(True) for _ in range(20000))
def q(v, p): return v[int(p * (len(v) - 1))]
principal_par_lot = 15.0  # M éq. ; boucle principale : 121 M sur environ 8 LOTs
out = dict(n_agents=len(A), r2_identite=r2_id, r2_regression=r2, sigma_log=s, types=types, beta=beta.tolist(),
           par_type=parType, stats=stats, lot_standard=LOT, principal_par_lot=principal_par_lot,
           leviers=LEV, lot_actuel=dict(mediane=q(base, .5), ic80=[q(base, .1), q(base, .9)], ic95=[q(base, .025), q(base, .975)]),
           lot_harnais=dict(mediane=q(harn, .5), ic80=[q(harn, .1), q(harn, .9)], ic95=[q(harn, .025), q(harn, .975)]))
# Validation croisée « un LOT laissé de côté » : prévision du coût réel des LOT 021 à 024 sans leurs propres agents
valid = {}
for L in (21, 22, 23, 24):
    reels = [a for a in A if a.get('lot') == L]
    if not reels: continue
    autres = {t: [a for a in A if a['type'] == t and a.get('lot') != L] for t in types}
    comp = {}
    for a in reels: comp[a['type']] = comp.get(a['type'], 0) + 1
    sims = []
    for _ in range(5000):
        sims.append(sum(recalc(random.choice(autres[t]), 0, 0, 0) for t, n in comp.items() for _ in range(n) if autres.get(t)))
    sims.sort()
    valid[L] = dict(reel=sum(a['cout'] for a in reels) / 1e6, mediane=q(sims, .5), ic95=[q(sims, .025), q(sims, .975)], composition=comp)
out['validation'] = valid
# Effet LOT (difficulté commune aux agents d'un même LOT) : calibré sur les LOT de composition propre (021–023)
lr = [math.log(v['reel'] / v['mediane']) for L, v in valid.items() if L in (21, 22, 23)]
mu, sd = float(np.mean(lr)), float(np.std(lr, ddof=1)) if len(lr) > 1 else 0.15
def calib(v):
    w = sorted(x * math.exp(random.gauss(mu, sd)) for x in v)
    return dict(mediane=q(w, .5), ic80=[q(w, .1), q(w, .9)], ic95=[q(w, .025), q(w, .975)])
out['effet_lot'] = dict(mu=mu, sd=sd, ratios=[math.exp(x) for x in lr])
out['lot_actuel_calibre'] = calib(base); out['lot_harnais_calibre'] = calib(harn)
out['economie_mediane_pct'] = 100 * (1 - out['lot_harnais']['mediane'] / out['lot_actuel']['mediane'])
# Mesure réelle des économies : agents lancés sous harnais (description préfixée « [H] ») contre agents antérieurs
H = [a for a in A if (a.get('desc') or '').startswith('[H]')]
mes = {}
for t in types:
    h = [a['cout'] for a in H if a['type'] == t]; b = [a['cout'] for a in A if a['type'] == t and a not in H]
    if len(h) >= 3 and len(b) >= 3:
        d = float(np.mean(np.log(h)) - np.mean(np.log(b)))
        se = float(math.sqrt(np.var(np.log(h), ddof=1) / len(h) + np.var(np.log(b), ddof=1) / len(b)))
        mes[t] = dict(n_harnais=len(h), economie_pct=100 * (1 - math.exp(d)), ic95_pct=[100 * (1 - math.exp(d + 1.96 * se)), 100 * (1 - math.exp(d - 1.96 * se))])
out['economies_mesurees'] = mes or 'aucun agent [H] encore : mesure automatique dès la reprise'
json.dump(out, open('Claude/_harnais/donnees/modele.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps({k: out[k] for k in ('n_agents', 'r2_identite', 'r2_regression', 'sigma_log', 'lot_actuel', 'lot_harnais', 'economie_mediane_pct')}, indent=1))
for t in types: print(t, {k: round(v, 2) if isinstance(v, float) else v for k, v in stats[t].items()})
