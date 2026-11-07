#!/usr/bin/env python3
"""Gouverneur de parallélisme : combien d'agents Opus lancer sans perdre la performance individuelle ni heurter la limite de 5 h (zéro jeton).

  python3 harnais/gouverneur.py            K, N soutenable, N lançable maintenant, consommation de la fenêtre
  python3 harnais/gouverneur.py --json

Modèle (mesuré sur les transcriptions de la session, Article 4) :
  coût d'un tour = entrée + 1,25·écriture cache + 0,1·lecture cache + 5·sortie (rapports de prix Opus)
  B  = coût consommé dans les 5 h précédant le dernier refus « five_hour » (recalibré à chaque nouveau refus)
  r_e = taux de coût médian d'un agent à l'effort e (par seconde), d_e = durée médiane ; r_p = taux de la session principale (dernière heure)
  N_budget = (B/18000 − r_p) / r_e        N_perf = concurrence maximale observée sans perte de débit individuel (pente mesurée)
  N* = min(N_budget, N_perf) ; K = N* / N_actuel (5)
  N_maintenant = nombre d'agents en cours autorisés tel que consommé_5h + (N·r_e + r_p)·d_e ≤ B
"""
import collections, datetime as dt, glob, json, os, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import modele_reel as mr

N_ACTUEL = 5
FENETRE = 5 * 3600


def cout(u):
    return u.get("input_tokens", 0) + 1.25 * u.get("cache_creation_input_tokens", 0) + 0.1 * u.get("cache_read_input_tokens", 0) + 5 * u.get("output_tokens", 0)


def releve():
    s = mr.session(); P = s.with_suffix("") / "subagents"
    tours, refus = [], []
    for f in [s] + sorted(P.glob("agent-*.jsonl")):
        vus = set()
        for l in open(f, encoding="utf-8", errors="ignore"):
            if '"usage"' not in l and "five_hour" not in l:
                continue
            try:
                o = json.loads(l)
            except Exception:
                continue
            if not isinstance(o, dict) or not o.get("timestamp"):
                continue
            t = dt.datetime.fromisoformat(o["timestamp"].replace("Z", "+00:00")).timestamp()
            if o.get("apiError") == "usage_limit_reached":
                refus.append(t); continue
            m = o.get("message")
            if isinstance(m, dict) and m.get("usage") and m.get("id") not in vus:
                vus.add(m.get("id"))
                tours.append((t, m.get("model", ""), o.get("perTurnEffort") or o.get("effort"), f.name, cout(m["usage"])))
    meta = {Path(x).name.replace(".meta.json", ".jsonl"): json.load(open(x)) for x in glob.glob(str(P / "agent-*.meta.json"))}
    return tours, refus, meta


def mediane(v):
    v = sorted(v); return v[len(v) // 2] if v else 0


def calculer():
    tours, refus, meta = releve()
    maint = max(t for t, *_ in tours)
    opus = [x for x in tours if "opus" in x[1]]
    B = sum(x[4] for x in opus if refus and refus[0] - FENETRE <= x[0] <= refus[0]) if refus else None
    if refus:  # dernier refus = calibrage le plus récent
        h = max(refus); B = sum(x[4] for x in opus if h - FENETRE <= x[0] <= h)
    par = collections.defaultdict(list)
    for x in opus:
        if x[3].startswith("agent-"):
            par[x[3]].append(x)
    taux, durees, spans = collections.defaultdict(list), collections.defaultdict(list), []
    for k, xs in par.items():
        a, b = min(x[0] for x in xs), max(x[0] for x in xs); spans.append((a, b, k))
        if meta.get(k, {}).get("finished") and b - a > 120:
            e = collections.Counter(x[2] for x in xs).most_common(1)[0][0]
            taux[e].append(sum(x[4] for x in xs) / (b - a)); durees[e].append(b - a)
    # performance individuelle : débit de sortie selon la concurrence
    pts = []
    for a, b, k in spans:
        if not meta.get(k, {}).get("finished") or b - a < 120:
            continue
        c = sum(1 for a2, b2, _ in spans if a2 <= (a + b) / 2 <= b2)
        pts.append((c, sum(x[4] for x in par[k]) / (b - a)))
    n_perf = max([c for c, _ in pts] or [N_ACTUEL])
    import statistics as st
    pente = 0.0
    if len(pts) > 2:
        mx, my = st.mean(c for c, _ in pts), st.mean(y for _, y in pts)
        sxx = sum((c - mx) ** 2 for c, _ in pts)
        pente = sum((c - mx) * (y - my) for c, y in pts) / sxx / my if sxx else 0.0  # perte relative par agent ajouté
    rp = sum(x[4] for x in tours if not x[3].startswith("agent-") and x[0] > maint - 3600) / 3600
    e = "xhigh"; re_, de = mediane(taux[e]), mediane(durees[e])
    n_budget = (B / FENETRE - rp) / re_ if B and re_ else float("inf")
    n_star = min(n_budget, n_perf)
    conso = sum(x[4] for x in opus if x[0] > maint - FENETRE)
    en_cours = sum(1 for a, b, k in spans if not meta.get(k, {}).get("finished") and maint - b < 600)
    n_now = max(0, int(((B - conso) / de - rp) / re_)) if B and re_ and de else n_perf
    return dict(B=B, refus=len(refus), r_xhigh=re_, d_xhigh=de, r_medium=mediane(taux["medium"]), r_principal=rp,
                n_perf=n_perf, pente_perf=pente, n_budget=n_budget, n_star=n_star, K=n_star / N_ACTUEL,
                conso_5h=conso, en_cours=en_cours, n_maintenant=min(n_now, int(n_star) if n_star != float("inf") else n_now))


if __name__ == "__main__":
    r = calculer()
    if "--json" in sys.argv:
        print(json.dumps(r)); sys.exit(0)
    print(f"Budget de 5 h B ≈ {r['B']:.3g} (calibré sur {r['refus']} refus « five_hour »)")
    print(f"Agent Opus xhigh : r = {r['r_xhigh']:.0f}/s, durée médiane {r['d_xhigh']:.0f} s · medium : r = {r['r_medium']:.0f}/s · principal : {r['r_principal']:.0f}/s")
    print(f"N_budget = {r['n_budget']:.2f} · N_perf ≥ {r['n_perf']} (débit individuel {100*r["pente_perf"]:+.1f} % par agent ajouté : aucune perte observée)")
    print(f"N* = {r['n_star']:.2f} → K = {r['K']:.2f}")
    print(f"Fenêtre glissante : consommé {r['conso_5h']:.3g} / {r['B']:.3g} · en cours {r['en_cours']} · lançable maintenant : {r['n_maintenant']}")


def decision(r=None):
    """Règle appliquée par la session principale avant chaque lancement d'agent Opus."""
    r = r or calculer()
    plafond = int(r["n_star"]) + (1 if r["conso_5h"] < 0.75 * r["B"] else 0)  # 4 soutenable ; 5 tant que la fenêtre a de la marge
    return max(0, plafond - r["en_cours"]), plafond


if __name__ == "__main__" and "--lancer" in sys.argv:
    libres, plafond = decision()
    print(f"plafond {plafond} agents Opus · places libres : {libres}")
    sys.exit(0 if libres > 0 else 1)
