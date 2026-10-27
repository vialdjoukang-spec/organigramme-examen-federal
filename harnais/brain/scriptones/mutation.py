#!/usr/bin/env python3
"""Test par mutation des scriptones sur le jeu doré (gratuit, déterministe).
  python3 harnais/brain/scriptones/mutation.py [--n 25] [--json]
1. Spécificité : le jeu doré (dore/cours_dore.html) ne produit AUCUNE doléance.
2. Sensibilité : chaque mutant (erreur connue injectée, paramètres tirés par graine) doit produire le code attendu ; sinon « évasion ».
3. Idempotence : corriger(corriger(x)) == corriger(x) sur le doré et sur chaque mutant ; dry-run : le fichier n'est jamais écrit.
Taux d'évasion : borne supérieure à 95 % (règle de trois si aucune évasion : 3/N) ; 99,99 % de détection exige N ≥ 29 958 sans évasion."""
import importlib, json, random, sys, time
from pathlib import Path
D = Path(__file__).resolve().parent
sys.path.insert(0, str(D))
import bus

NOMS = ["s1_police", "s2_rythme", "s3_concision", "s4_budget", "s5_arbre", "s8_tableaux"]
DORE = D.parent / "dore/cours_dore.html"


def borne(n, k):
    """Borne supérieure à 95 % du taux d'évasion (Wilson ; règle de trois si k = 0)."""
    if n == 0: return 1.0
    if k == 0: return 3 / n
    z = 1.96; p = k / n; c = (p + z * z / (2 * n) + z * ((p * (1 - p) + z * z / (4 * n)) / n) ** .5) / (1 + z * z / n)
    return min(1.0, c)


BRUIT = [["chez le sujet âgé,", "chez l'enfant,", "en montagne,", "en milieu urbain,", "pendant le transport,", "à l'arrivée aux urgences,"],
         ["la surveillance continue", "la mesure répétée", "la documentation précise", "la transmission entre équipes", "l'évaluation initiale", "la réévaluation horaire"],
         ["améliore la sécurité du patient", "réduit les erreurs de tri", "limite les retards de traitement", "facilite la décision médicale", "guide le choix du transfert", "évite les gestes inutiles"],
         ["car les signes évoluent vite", "parce que l'état change sans bruit", "donc chaque valeur compte", "ainsi le risque baisse", "car le froid masque la gravité", "puisque le temps presse"]]


def neutre(g, r):
    """Variation neutre du contexte (chiffres d'un paragraphe des points 3 à 14 remplacés, hors balises) : le doré varié ne doit produire
    aucune doléance, et l'erreur injectée doit rester détectée quel que soit le contexte. Multiplie les mutants distincts."""
    import re
    S = bus.sections(g); n = r.choice([k for k in S if k >= 3]); B = bus.blocs(g, *S[n], ("p",))
    if not B: return g
    pa, pf, _ = r.choice(B); seg = g[pa:pf]
    phrase = " ".join(r.choice(x) for x in BRUIT) + "."
    seg = seg[:-4] + " " + phrase[0].upper() + phrase[1:] + seg[-4:]
    seg = re.sub(r">([^<]*)<", lambda m: ">" + re.sub(r"\d+", lambda d: str(r.randint(10 ** (len(d.group(0)) - 1) if len(d.group(0)) > 1 else 1, 10 ** len(d.group(0)) - 1)), m.group(1)) + "<", seg)
    return g[:pa] + seg + g[pf:]


def lancer(n=25, noms=NOMS):
    t0 = time.time(); g = DORE.read_text(encoding="utf-8"); rap = dict(faux_positifs={}, mutants={}, evasions=[], idempotence_ko=[])
    total = det = 0; vus = set(); dist = dist_det = 0
    for nm in noms:
        m = importlib.import_module(nm)
        Dg, _ = m.analyser(g, "dore", {})
        if Dg: rap["faux_positifs"][nm] = [f"{d['code']} {d['constat'][:80]}" for d in Dg]
        c = m.corriger(g, {})
        if m.corriger(c, {}) != c: rap["idempotence_ko"].append(f"{nm} : doré")
        for nom_m, fn, code in m.MUTANTS:
            ok = 0
            for s in range(n):
                r = random.Random(f"{nm}|{nom_m}|{s}"); g2 = neutre(g, r) if s else g
                if s < 5 and m.analyser(g2, "neutre", {})[0]: rap["faux_positifs"].setdefault(nm, []).append(f"variation neutre graine {s}")
                x = fn(g2, r)
                if x == g2: rap["evasions"].append(f"{nm} · {nom_m} · graine {s} : mutant identique au doré"); total += 1; continue
                Dx, _ = m.analyser(x, "mutant", {}); total += 1; h = bus.sha(x); neuf = h not in vus; vus.add(h); dist += neuf
                if any(d["code"] == code for d in Dx): ok += 1; det += 1; dist_det += neuf
                else: rap["evasions"].append(f"{nm} · {nom_m} · graine {s} : {code} attendu, obtenu {sorted({d['code'] for d in Dx})}")
                if s < 3:
                    cx = m.corriger(x, {})
                    if m.corriger(cx, {}) != cx: rap["idempotence_ko"].append(f"{nm} · {nom_m} · graine {s}")
            rap["mutants"][f"{nm} · {nom_m} → {code}"] = f"{ok}/{n}"
    rap.update(total=total, detectes=det, distincts=dist, taux_detection=round(det / max(1, total), 6), borne_evasion_95=round(borne(dist, dist - dist_det), 6),
               duree_s=round(time.time() - t0, 1))
    rap["vert"] = not rap["faux_positifs"] and not rap["evasions"] and not rap["idempotence_ko"]
    return rap


if __name__ == "__main__":
    n = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 25
    r = lancer(n)
    if "--json" in sys.argv: print(json.dumps(r, ensure_ascii=False, indent=1))
    else:
        for k, v in r["mutants"].items(): print(f"{'OK' if v.split('/')[0] == v.split('/')[1] else 'KO'}  {k} : {v}")
        print(f"faux positifs du doré : {r['faux_positifs'] or 'aucun'} · idempotence : {r['idempotence_ko'] or 'OK'}")
        print(f"MUTATION : {r['detectes']}/{r['total']} détectés ({r['distincts']} mutants distincts) · taux {r['taux_detection'] * 100:.4f} % · borne d'évasion 95 % (distincts) ≤ {r['borne_evasion_95'] * 100:.4f} % · {r['duree_s']} s")
        for e in r["evasions"][:10]: print("  ÉVASION", e)
    sys.exit(0 if r["vert"] else 1)
