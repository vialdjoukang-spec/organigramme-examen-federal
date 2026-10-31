#!/usr/bin/env python3
"""COÛTS RELATIFS — une ligne par passe de modèle, bilan par LOT (Python standard, zéro jeton, aucun tarif réel lu).

  python3 grok-LOTS-html/outils/couts.py noter LOT_134 <poste> [--modele grok-4.6] [--effort xhigh]
          (--jetons-entree N --jetons-sortie N [--jetons-cache N] | --ko-entree K --ko-sortie K [--ko-cache K])
          [--tours N] [--fichier NOM] [--note "texte"]
  python3 grok-LOTS-html/outils/couts.py bilan [LOT_XXX] [--json]
  python3 grok-LOTS-html/outils/couts.py tarifs

Unité : 1 u = 1 000 000 jetons d'entrée du modèle de référence, sans cache (grok-LOTS-html/connaissance/TARIFS_RELATIFS.json).
Coût d'une passe : u = prix_entrée(modèle) × [entrée_neuve + lecture_cache_relative × entrée_cache + rapport_sortie × sortie] / 1e6
                   × prime_rapide si l'effort est « fast ». Octets → jetons : 1 jeton ≈ 3,2 octets (hypothèse).
Si --modele / --effort manquent : lus dans ROUTAGE_GROK.json pour le poste (reasoning_effort, + « fast » si le poste est rapide). Écrit UNIQUEMENT dans connaissance/COUTS.jsonl (--sortie pour ailleurs).
Les barèmes sont des HYPOTHÈSES tant que Vial n'a pas remplacé TARIFS_RELATIFS.json par les valeurs de son abonnement : le bilan sert à comparer
(S1 contre S2, poste contre poste), pas à prédire une facture.
"""
from __future__ import annotations
import argparse, datetime, json, sys
from collections import defaultdict
from pathlib import Path

D = Path(__file__).resolve().parent.parent            # grok-LOTS-html/
VAULT = D / "connaissance"
OCTETS_PAR_JETON = 3.2
ZH = datetime.timezone(datetime.timedelta(hours=1))
POSTES = ("redacteur-phase-a", "redacteur", "auditeur-medical", "auditeur-conformite", "transversale", "mecanique")


def charger_json(p, defaut=None):
    try:
        return json.loads(Path(p).read_text(encoding="utf-8"))
    except Exception:
        return defaut


def tarifs():
    return charger_json(VAULT / "TARIFS_RELATIFS.json", {"prix_entree_relatif": {"grok-4.7": 1.0, "grok-4.6": 0.6, "grok-4.5": 0.25},
                                                       "rapport_sortie_sur_entree": 5.0, "lecture_cache_relative": 0.1, "prime_mode_rapide": 1.5})


def routage(poste):
    c = charger_json(D / "ROUTAGE_GROK.json", {}) or {}
    t = c.get("postes", c)
    e = t.get(poste, {}) if isinstance(t, dict) else {}
    if isinstance(e, dict):
        eff = e.get("reasoning_effort") or e.get("effort")
        return e.get("modele") or e.get("model"), (str(eff) + " fast") if e.get("fast") else eff
    return None, None


def cout(modele, effort, entree, sortie, cache, T):
    prix = T["prix_entree_relatif"].get(modele)
    if prix is None:
        raise SystemExit(f"modèle inconnu du barème : {modele} (connus : {', '.join(T['prix_entree_relatif'])})")
    u = prix * (entree + T["lecture_cache_relative"] * cache + T["rapport_sortie_sur_entree"] * sortie) / 1e6
    if effort and "fast" in str(effort).lower():                  # « low fast » = mode rapide (prime)
        u *= T["prime_mode_rapide"]
    return u


def noter(a):
    T = tarifs()
    modele, effort = a.modele, a.effort
    if not modele or not effort:
        m, e = routage(a.poste)
        modele, effort = modele or m, effort or e
    if not modele:
        raise SystemExit("modèle introuvable : passez --modele (ROUTAGE_GROK.json n'a pas pu être lu pour ce poste)")
    k = 1000 / OCTETS_PAR_JETON
    ent = a.jetons_entree if a.jetons_entree is not None else (a.ko_entree or 0) * k
    sor = a.jetons_sortie if a.jetons_sortie is not None else (a.ko_sortie or 0) * k
    cac = a.jetons_cache if a.jetons_cache is not None else (a.ko_cache or 0) * k
    u = cout(modele, effort, ent, sor, cac, T)
    ligne = {"horodatage": datetime.datetime.now(ZH).isoformat(timespec="seconds"), "lot": a.lot, "poste": a.poste, "fichier": a.fichier,
             "modele": modele, "effort": effort, "tours": a.tours, "jetons_entree": round(ent), "jetons_cache": round(cac), "jetons_sortie": round(sor),
             "cout_u": round(u, 4), "bareme": "hypothese" if "_avertissement" in T else "reel", "note": a.note}
    sortie = Path(a.sortie) if a.sortie else VAULT / "COUTS.jsonl"
    sortie.parent.mkdir(parents=True, exist_ok=True)
    with sortie.open("a", encoding="utf-8") as f:
        f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    print(f"{a.lot} {a.poste} {modele}/{effort} : {u:.3f} u  → {sortie}")
    return 0


def lire(sortie=None):
    p = Path(sortie) if sortie else VAULT / "COUTS.jsonl"
    out = []
    if p.exists():
        for l in p.read_text(encoding="utf-8").splitlines():
            try: out.append(json.loads(l))
            except Exception: pass
    return out


def bilan(a):
    L = [l for l in lire(a.sortie) if not a.lot or l.get("lot") == a.lot]
    par_lot, par_poste = defaultdict(float), defaultdict(float)
    for l in L:
        par_lot[l["lot"]] += l["cout_u"]; par_poste[l["poste"]] += l["cout_u"]
    n = len(par_lot)
    res = {"lignes": len(L), "lots": n, "total_u": round(sum(par_lot.values()), 3), "moyenne_u_par_lot": round(sum(par_lot.values()) / n, 3) if n else None,
           "par_poste_u": {k: round(v, 3) for k, v in sorted(par_poste.items())}, "par_lot_u": {k: round(v, 3) for k, v in sorted(par_lot.items())}}
    prev = charger_json(VAULT / "PREVISION_SIMULATION.json")
    if prev and n:
        res["prevision_simulation_u_par_lot"] = {k: prev.get(k) for k in ("S1", "S2")}
        res["avertissement"] = "prévision = HYPOTHÈSES de sim_duo.py ; comparer seulement quand COUTS.jsonl porte des jetons réels et un barème réel"
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=1))
    else:
        print(f"{res['lignes']} passe(s), {n} LOT(s), total {res['total_u']} u" + (f", moyenne {res['moyenne_u_par_lot']} u/LOT" if n else ""))
        for k, v in res["par_poste_u"].items(): print(f"  {k:22s} {v:9.3f} u")
        if "prevision_simulation_u_par_lot" in res: print("  prévision simulation (hypothèse) :", res["prevision_simulation_u_par_lot"])
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=("noter", "bilan", "tarifs"))
    ap.add_argument("lot", nargs="?"); ap.add_argument("poste", nargs="?")
    ap.add_argument("--modele"); ap.add_argument("--effort")
    ap.add_argument("--jetons-entree", type=float); ap.add_argument("--jetons-sortie", type=float); ap.add_argument("--jetons-cache", type=float)
    ap.add_argument("--ko-entree", type=float); ap.add_argument("--ko-sortie", type=float); ap.add_argument("--ko-cache", type=float)
    ap.add_argument("--tours", type=int); ap.add_argument("--fichier"); ap.add_argument("--note"); ap.add_argument("--sortie"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    if a.cmd == "tarifs":
        print(json.dumps(tarifs(), ensure_ascii=False, indent=1)); return 0
    if a.cmd == "bilan":
        return bilan(a)
    if not a.lot or not a.poste or a.poste not in POSTES:
        ap.print_usage(sys.stderr); print("poste attendu parmi :", ", ".join(POSTES), file=sys.stderr); return 2
    if all(v is None for v in (a.jetons_entree, a.jetons_sortie, a.ko_entree, a.ko_sortie)):
        print("indiquez les volumes (--jetons-… ou --ko-…)", file=sys.stderr); return 2
    return noter(a)


if __name__ == "__main__":
    sys.exit(main())
