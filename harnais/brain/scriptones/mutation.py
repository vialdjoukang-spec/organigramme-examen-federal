#!/usr/bin/env python3
"""Test par mutation des 160 scriptones (registre) sur leurs jeux dorés (gratuit, déterministe).
  python3 harnais/brain/scriptones/mutation.py [--n 25] [--json] [--ids s1_police,a02_R,…] [--zone alpha|beta|transversal]
1. Spécificité : chaque jeu doré (cours_dore.html, journal_dore.jsonl, brief_dore.md, SHA256SUMS, cumul) ne produit AUCUNE doléance.
2. Sensibilité : chaque mutant (erreur connue injectée, paramètres tirés par graine, contexte varié par une variation neutre) doit produire
   le code attendu ; sinon « évasion ». Un mutant peut aussi être une panne injectée (couple texte, options).
3. Idempotence : corriger(corriger(x)) == corriger(x) sur le doré et sur les premiers mutants ; dry-run : aucun fichier écrit.
Taux d'évasion : borne supérieure à 95 % (règle de trois si aucune évasion : 3/N) ; 99,99 % de détection exige N ≥ 29 958 mutants distincts sans évasion."""
import json, random, re, sys, time
from pathlib import Path
D = Path(__file__).resolve().parent
sys.path.insert(0, str(D))
import bus, reseau

DORE = D.parent / "dore/cours_dore.html"
NOMS = [e["id"] for e in reseau.registre()["scriptones"] if e["langage"] == "python"]
_DORES = {}


def dore(m):
    p = Path(getattr(m, "DORE", DORE))
    if p not in _DORES: _DORES[p] = p.read_text(encoding="utf-8")
    return _DORES[p], p == DORE


def borne(n, k):
    """Borne supérieure à 95 % du taux d'évasion (Wilson ; règle de trois si k = 0)."""
    if n == 0: return 1.0
    if k == 0: return 3 / n
    z = 1.96; p = k / n; c = (p + z * z / (2 * n) + z * ((p * (1 - p) + z * z / (4 * n)) / n) ** .5) / (1 + z * z / n)
    return min(1.0, c)


BRUIT = [["chez le sujet âgé,", "chez l'enfant,", "en montagne,", "en milieu urbain,", "pendant le transport,", "à l'arrivée aux urgences,"],
         ["la surveillance continue", "la mesure répétée", "la documentation précise", "la transmission entre équipes", "l'évaluation initiale", "la réévaluation horaire"],
         ["améliore la sécurité du patient", "réduit les erreurs de tri", "limite les retards de traitement", "facilite la décision médicale", "guide le choix du transfert", "évite les gestes inutiles"],
         ["car les signes évoluent vite", "parce que l'état change sans bruit", "donc chaque valeur compte", "ainsi le risque baisse", "car le froid cache la gravité", "puisque le temps presse"]]


def neutre(g, r):
    """Variation neutre du contexte : une phrase verbale neutre ajoutée à un paragraphe des points 3 à 14, et les nombres UNIQUES de ce paragraphe
    tirés au hasard (un nombre repris ailleurs — seuil, stade — n'est jamais touché, pour ne pas créer de vraie incohérence)."""
    S = bus.sections(g); n = r.choice([k for k in S if k >= 3]); B = [b for b in bus.blocs(g, *S[n], ("p",)) if not re.search(r"(?i)<(?:p|li)\b", b[2])]
    if not B: return g
    pa, pf, _ = r.choice(B); seg = g[pa:pf]
    phrase = " ".join(r.choice(x) for x in BRUIT) + "."
    seg = seg[:-4] + " " + phrase[0].upper() + phrase[1:] + seg[-4:]
    vis = bus.texte(g); compte = {}
    for x in re.findall(r"\d+", vis): compte[x] = compte.get(x, 0) + 1
    def rep(d):
        x = d.group(0)
        if compte.get(x, 0) != 1 or len(x) > 6: return x
        return str(r.randint(10 ** (len(x) - 1) if len(x) > 1 else 2, 10 ** len(x) - 1))
    seg = re.sub(r">([^<]*)<", lambda m: ">" + re.sub(r"(?<![\d,.·])\d+(?![\d,.·])", rep, m.group(1)) + "<", seg)
    return g[:pa] + seg + g[pf:]


def lancer(n=25, noms=None, rapide=False):
    t0 = time.time(); rap = dict(faux_positifs={}, mutants={}, evasions=[], idempotence_ko=[], par_scriptone={})
    total = det = 0; vus = set(); dist = dist_det = 0
    for nm in noms or NOMS:
        m = reseau.module(nm); g, cours = dore(m)
        Dg, _ = m.analyser(g, "dore", {})
        if Dg: rap["faux_positifs"][nm] = [f"{d['code']} {d['constat'][:80]}" for d in Dg]
        if hasattr(m, "corriger"):
            c = m.corriger(g, {})
            if c != g and nm not in ("s14_journal",): rap["idempotence_ko"].append(f"{nm} : le doré n'est pas un point fixe")
            if m.corriger(c, {}) != c: rap["idempotence_ko"].append(f"{nm} : doré")
        k = min(n, getattr(m, "COUT_MUTATION", n)); ok_s = tot_s = 0
        for nom_m, fn, code in m.MUTANTS:
            ok = 0
            for s in range(k):
                r = random.Random(f"{nm}|{nom_m}|{s}"); g2 = neutre(g, r) if (s and cours) else g
                if s and s < 3 and cours and m.analyser(g2, "neutre", {})[0]: rap["faux_positifs"].setdefault(nm, []).append(f"variation neutre graine {s}")
                try: x = fn(g2, r)
                except Exception as e: rap["evasions"].append(f"{nm} · {nom_m} · graine {s} : mutant inapplicable ({type(e).__name__} {e})"); total += 1; tot_s += 1; continue
                x, opt = x if isinstance(x, tuple) else (x, {})
                if x == g2 and not opt: rap["evasions"].append(f"{nm} · {nom_m} · graine {s} : mutant identique au doré"); total += 1; tot_s += 1; continue
                Dx, _ = m.analyser(x, "mutant", opt); total += 1; tot_s += 1
                h = bus.sha(x + json.dumps(opt, sort_keys=True, default=str) + nm); neuf = h not in vus; vus.add(h); dist += neuf
                if any(d["code"] == code for d in Dx): ok += 1; det += 1; dist_det += neuf; ok_s += 1
                else: rap["evasions"].append(f"{nm} · {nom_m} · graine {s} : {code} attendu, obtenu {sorted({d['code'] for d in Dx})}")
                if s < (1 if rapide else 2) and hasattr(m, "corriger") and not opt:
                    cx = m.corriger(x, {})
                    if m.corriger(cx, {}) != cx: rap["idempotence_ko"].append(f"{nm} · {nom_m} · graine {s}")
            rap["mutants"][f"{nm} · {nom_m} → {code}"] = f"{ok}/{k}"
        rap["par_scriptone"][nm] = f"{ok_s}/{tot_s}"
    rap.update(scriptones=len(noms or NOMS), total=total, detectes=det, distincts=dist, taux_detection=round(det / max(1, total), 6),
               borne_evasion_95=round(borne(dist, dist - dist_det), 6), duree_s=round(time.time() - t0, 1))
    rap["vert"] = not rap["faux_positifs"] and not rap["evasions"] and not rap["idempotence_ko"]
    return rap


if __name__ == "__main__":
    a = sys.argv
    n = int(a[a.index("--n") + 1]) if "--n" in a else 25
    noms = a[a.index("--ids") + 1].split(",") if "--ids" in a else None
    if "--zone" in a: noms = [e["id"] for e in reseau.registre()["scriptones"] if e["langage"] == "python" and e["zone"] == a[a.index("--zone") + 1]]
    r = lancer(n, noms)
    if "--json" in a: print(json.dumps(r, ensure_ascii=False, indent=1))
    else:
        ko = [k for k, v in r["mutants"].items() if v.split("/")[0] != v.split("/")[1]]
        print(f"{len(r['mutants'])} classes de mutants · {len(ko)} incomplètes" + "".join(f"\n  KO {k} : {r['mutants'][k]}" for k in ko[:20]))
        print(f"faux positifs : {r['faux_positifs'] or 'aucun'} · idempotence : {r['idempotence_ko'] or 'OK'}")
        print(f"MUTATION : {r['scriptones']} scriptones · {r['detectes']}/{r['total']} détectés ({r['distincts']} mutants distincts) · taux {r['taux_detection'] * 100:.4f} % · "
              f"borne d'évasion 95 % (distincts) ≤ {r['borne_evasion_95'] * 100:.4f} % · {r['duree_s']} s")
        for e in r["evasions"][:15]: print("  ÉVASION", e)
    sys.exit(0 if r["vert"] else 1)
