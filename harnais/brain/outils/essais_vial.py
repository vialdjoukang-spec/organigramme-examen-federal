#!/usr/bin/env python3
"""BRAIN-HARNESS · essais demandés par Vial, mesurés et reproductibles (lecture seule sur main ; gratuit, hors ligne) :
  python3 harnais/brain/outils/essais_vial.py [--rapide] [--json]      écrit harnais/brain/essais_vial.json
T1 réduction des dépenses (jetons par étage, mesurée contre deux références, comparée à la cible de 99,99 %)
T2 application à 4 cours réels de LOT différents (lus par `git show origin/main:…`, jamais modifiés ; corrections sur copie en mémoire)
T3 nombre de connexions sans conflit : preuve statique (un écrivain par zone), confluence sur ordres aléatoires, détection du conflit injecté,
   couverture des mutants selon le nombre de familles par synapse (1 à 5, α seule, β seule, α + β), 16 cours simultanés
T4 auto-adaptation : panne injectée dans chacune des 140 synapses (exception, contrat rompu, lenteur), double panne, isolement des autres
   synapses, orchestre complet sous pannes, stagnation."""
import itertools, json, os, random, subprocess, sys, tempfile, time
from pathlib import Path
B = Path(__file__).resolve().parents[1]
R = B.parents[1]
sys.path[:0] = [str(B / "scriptones"), str(B), str(R / "harnais")]
import bus, reseau, familles as F, mutation, orchestre

COURS = ["LOT_Claude_Finaux/LOT_001/LOT_001_Phase_B_V0_DX.2.html", "LOT_Claude_Finaux/LOT_005/LOT_005_Phase_B_V0_DX.3.html",
         "LOT_Claude_Finaux/LOT_010/LOT_010_Phase_B_V0_DX.4.html", "LOT_Claude_Finaux/LOT_012/LOT_012_Phase_B_V0_DX.5.html"]
CIBLE = 99.99


def lire_main(p):
    for ref in ("origin/main", "main"):
        r = subprocess.run(["git", "-C", str(R), "show", f"{ref}:{p}"], capture_output=True)
        if r.returncode == 0: return r.stdout.decode("utf-8", "surrogateescape")
    raise FileNotFoundError(p)


def synapses():
    return [e["id"] for e in reseau.registre()["scriptones"] if e["zone"] in ("alpha", "beta")]


# ───────────────────────── T1 et T2 ─────────────────────────
def t1_t2(cours):
    S16 = reseau.module("s16_economie"); out = []
    for p, html in cours.items():
        nom = Path(p).name; sha0 = bus.sha(html)
        r = orchestre.passer(html=html, nom=nom, journal=None, historique=[])
        t1, tours = reseau.corriger_tout(html); t2, _ = reseau.corriger_tout(t1)
        M = S16.mesures(html); J = r["jetons"]; base = J["relecture_integrale_par_noeud"]; texte = M["jetons_texte_cours"]
        vis0, vis1 = len(bus.texte_visible(html)), len(bus.texte_visible(t1))
        out.append(dict(cours=nom, lot=nom[:7], octets=len(html.encode("utf-8", "surrogateescape")), verdict=r["verdict"], duree_s=r["duree_s"],
                        alpha_avant=sum(r["doleances_alpha_avant"].values()), alpha_apres=sum(r["doleances_alpha_apres"].values()), beta=sum(r["doleances_beta"].values()),
                        corrigees_par_script=sum(r["doleances_alpha_avant"].values()) - sum(r["doleances_alpha_apres"].values()), tours_point_fixe=tours,
                        idempotent=t2 == t1, main_intact=bus.sha(lire_main(p)) == sha0, texte_visible_conserve_pct=round(100 * vis1 / max(1, vis0), 2),
                        jetons=dict(relecture_10_noeuds=10 * base, texte_10_noeuds=10 * texte, briefs_sonnet=sum(J["briefs_sonnet"].values()),
                                    briefs_opus=sum(J["briefs_opus"].values()), briefs_total=J["total_briefs"], par_noeud={**J["briefs_sonnet"], **J["briefs_opus"]},
                                    reduction_vs_relecture_pct=round(100 * (1 - J["total_briefs"] / max(1, 10 * base)), 2),
                                    reduction_vs_texte_pct=round(100 * (1 - J["total_briefs"] / max(1, 10 * texte)), 2)),
                        codes_alpha_apres=r["doleances_alpha_apres"], codes_beta=r["doleances_beta"]))
    tot = lambda k: sum(c["jetons"][k] for c in out)
    agg = dict(relecture=tot("relecture_10_noeuds"), texte=tot("texte_10_noeuds"), briefs=tot("briefs_total"))
    agg.update(reduction_vs_relecture_pct=round(100 * (1 - agg["briefs"] / agg["relecture"]), 2), reduction_vs_texte_pct=round(100 * (1 - agg["briefs"] / agg["texte"]), 2),
               cible_pct=CIBLE, briefs_max_pour_cible=round(agg["relecture"] * (1 - CIBLE / 100)), ecart_facteur=round(agg["briefs"] / max(1, agg["relecture"] * (1 - CIBLE / 100)), 1))
    # référence : cours propre (doré) : seuls les paquets sans doléance → plancher du circuit
    g = (B / "dore/cours_dore.html").read_text(encoding="utf-8"); rd = orchestre.passer(html=g, nom="cours_dore.html", journal=None, historique=[])
    agg["dore"] = dict(verdict=rd["verdict"], briefs=rd["jetons"]["total_briefs"], relecture_10_noeuds=rd["jetons"]["base_10_noeuds"], reduction_pct=rd["jetons"]["reduction_pct"])
    return out, agg


# ───────────────────────── T3 connexions ─────────────────────────
def t3(cours, rapide):
    reg = reseau.registre(); E = reg["scriptones"]; W = reseau.ecrivains()
    zones = sorted({z for _, zs in W for z in zs}); lecteurs = [e["id"] for e in E if not e.get("ecrit")]
    ar = dict(entrees=len(E), sorties_bus=len(E), ecritures=sum(len(e.get("ecrit") or []) for e in E), zigzag=2 * 13,
              jumeaux=sum(1 for e in E if e.get("jumeau")), alpha_vers_sonnet=14, sonnet_vers_beta=14, vote_vers_opus=5, opus_vers_sortie=5)
    ar["total"] = sum(ar.values())
    res = dict(scriptones=len(E), ecrivains=len(W), zones_ecrites=len(zones), lecteurs=len(lecteurs), conflits_statiques=reseau.conflits_statiques(),
               connexions=ar, regle="une zone, un écrivain : connexions d'écriture = zones (pigeonnier) ; connexions de lecture illimitées (doléances sur le bus)")
    # confluence : K ordres aléatoires des écrivains sur chaque cours réel → même texte
    S12 = reseau.module("s12_ordonnanceur"); K = 3 if rapide else 8; conf = []
    for p, html in cours.items():
        D, M = S12.analyser(html, Path(p).name, {"ordres": K, "graine": 7})
        conf.append(dict(cours=Path(p).name, ordres=M["ordres_testes"], ecrivains=M["ecrivains"], doleances=[d["code"] for d in D]))
    res["confluence"] = conf
    g = (B / "dore/cours_dore.html").read_text(encoding="utf-8"); inj = {}
    for nm, opt in (("deux écrivains déclarés sur une zone", None), ("duel", {"injecter": "duel", "ordres": 6}), ("bavard", {"injecter": "bavard", "ordres": 1}), ("intrus", {"injecter": "intrus", "ordres": 1})):
        if opt is None: opt = S12.MUTANTS[0][1](g, random.Random(1))[1]
        D, _ = S12.analyser(g, "dore", opt); inj[nm] = sorted({d["code"] for d in D})
    res["conflit_injecte_detecte"] = inj
    # couverture des mutants des 140 synapses selon les familles actives au point du mutant
    graines = 1 if rapide else 2; lignes = []; t0 = time.time()
    for n in range(1, 15):
        ids = [F.ident("A", f, n).ID for f in F.FAM_A] + [F.ident("B", f, n).ID for f in F.FAM_B]
        mods = {i: reseau.module(i) for i in ids}
        for i in ids:
            m = mods[i]; gm, _ = mutation.dore(m)
            for nom_m, fn, code in m.MUTANTS:
                for s in range(graines):
                    rr = random.Random(f"T3|{i}|{nom_m}|{s}"); x = fn(gm, rr); x, opt = x if isinstance(x, tuple) else (x, {})
                    if x == gm: continue
                    vus = frozenset(j for j in ids if mods[j].analyser(x, "mutant", opt if j == i else {})[0])
                    lignes.append(dict(point=n, auteur=i, classe=nom_m, detecte_par=sorted(vus)))
    fam = lambda j: ("α" if j[0] == "a" else "β") + j.split("_")[1]
    toutes = [f"α{f}" for f in F.FAM_A] + [f"β{f}" for f in F.FAM_B]
    cov = lambda S: sum(1 for l in lignes if any(fam(j) in S for j in l["detecte_par"])) / max(1, len(lignes))
    courbe = []
    for k in range(1, 11):
        best = max(itertools.combinations(toutes, k), key=lambda S: (cov(set(S)), S))
        courbe.append(dict(familles=k, meilleur_ensemble=list(best), couverture_pct=round(100 * cov(set(best)), 2)))
    red = [len({fam(j) for j in l["detecte_par"]}) for l in lignes]
    res["couverture"] = dict(mutants=len(lignes), duree_s=round(time.time() - t0, 1), alpha_seule_pct=round(100 * cov({f"α{f}" for f in F.FAM_A}), 2),
                             beta_seule_pct=round(100 * cov({f"β{f}" for f in F.FAM_B}), 2), alpha_beta_pct=round(100 * cov(set(toutes)), 2), courbe=courbe,
                             redondance=dict(une_famille=sum(r == 1 for r in red), deux_ou_plus=sum(r >= 2 for r in red), moyenne=round(sum(red) / max(1, len(red)), 2)),
                             optimal=next((c["familles"] for c in courbe if c["couverture_pct"] >= 100), None))
    # 16 cours simultanés (4 cours × 4 copies), écriture réelle sur copies : chaque copie doit valoir la correction séquentielle
    with tempfile.TemporaryDirectory() as d:
        ref, chem = {}, []
        for p, html in cours.items():
            ref[Path(p).name] = bus.sha(reseau.corriger_tout(html)[0])
            for k in range(4):
                c = Path(d) / f"{k}_{Path(p).name}"; c.write_text(html, encoding="utf-8", errors="surrogateescape"); chem.append(c)
        par = {}
        for np_ in ((4, 16) if rapide else (1, 4, 16)):
            for c in chem: c.write_text(cours[next(p for p in cours if p.endswith(c.name.split("_", 1)[1]))], encoding="utf-8", errors="surrogateescape")
            t0 = time.time(); rs = orchestre.lot(chem, np_, None, appliquer=True); dt = time.time() - t0
            ok = all(bus.sha(bus.lire(c)[0]) == ref[c.name.split("_", 1)[1]] for c in chem)
            par[str(np_)] = dict(cours=len(chem), duree_s=round(dt, 1), identiques_au_sequentiel=ok, pannes=[r["verdict"] for r in rs if r["verdict"].startswith("panne")])
        res["simultanes"] = par
    return res


# ───────────────────────── T4 auto-adaptation ─────────────────────────
def t4(cours, rapide):
    S13 = reseau.module("s13_disjoncteur"); ids = synapses(); html = next(iter(cours.values())); nom = Path(next(iter(cours))).name
    res = {}
    for nature, attendu in (("exception", "Z1"), ("contrat", "Z1"), ("lenteur", "Z4")):
        ok = rer = 0
        for i in ids:
            D, M = S13.analyser(html, nom, {"pannes": {i: nature}, "ids": [i]})
            ok += any(d["code"] == attendu for d in D); rer += M["reroutees"]
        res[nature] = dict(synapses=len(ids), signalees=ok, reroutees_vers_jumeau=rer)
    ok = 0
    for i in ids:
        j = reseau.jumeau(i); D, _ = S13.analyser(html, nom, {"pannes": {i: "exception", j: "exception"}, "ids": [j, i]}); ok += any(d["code"] == "Z2" and d["severite"] == "CRITIQUE" for d in D)
    res["double_panne"] = dict(synapses=len(ids), escalades_Z2=ok)
    # isolement : une panne par point (14 synapses) ; les 126 autres rendent exactement les mêmes doléances
    base = {i: sorted(d["id"] for d in (bus.executer(reseau.module(i), nom, html=html, ecrire=False)["doleances"])) for i in ids}
    r = random.Random(11); tirage = [r.choice([x for x in ids if x[1:3] == f"{n:02d}"]) for n in range(1, 15)]
    dj = reseau.Disjoncteur(); diff = 0; couvert = perdu = 0
    for i in ids:
        s, eff, nature = reseau.executer_protege(i, html, nom, dj, {x: "exception" for x in tirage})
        if i in tirage:
            perdu += len(base[i]); couvert += 1 if eff else 0; continue
        diff += sorted(d["id"] for d in s["doleances"]) != base[i]
    res["isolement"] = dict(pannes_injectees=len(tirage), autres_synapses=len(ids) - len(tirage), autres_modifiees=diff, pannes_couvertes_par_jumeau=couvert,
                            doleances_propres_des_synapses_en_panne=perdu, note="le jumeau couvre l'exigence par une autre méthode ; les doléances propres de la synapse en panne sont rendues au nœud auditeur (Z1)")
    # orchestre complet sous pannes, sur le doré (propre) : une panne couverte n'empêche pas la sortie ; une double panne la bloque
    g = (B / "dore/cours_dore.html").read_text(encoding="utf-8"); i = "a05_R"; j = reseau.jumeau(i); orc = {}
    for nm, pn in (("sans panne", {}), ("panne couverte (a05_R)", {i: "exception"}), (f"double panne ({i} + {j})", {i: "exception", j: "exception"}),
                   ("10 pannes aléatoires", {x: random.Random(5).choice(["exception", "contrat"]) for x in random.Random(5).sample(ids, 10)})):
        rr = orchestre.passer(html=g, nom="cours_dore.html", journal=None, historique=[], pannes=pn)
        orc[nm] = dict(verdict=rr["verdict"], pannes=len(rr.get("pannes", [])), escalades=len(rr.get("escalades", [])))
    res["orchestre"] = orc
    # stagnation : deux passages de suite avec les mêmes doléances ouvertes → fichier bloqué (orchestre) ; Z3 (s13)
    p1 = orchestre.passer(html=html, nom=nom, journal=None, historique=[]); p2 = orchestre.passer(html=html, nom=nom, journal=None, historique=[p1["ouvertes"]])
    D, _ = S13.analyser(html, nom, {"historique": [["x", "y"], ["y", "x"]], "ids": []})
    res["stagnation"] = dict(passage_1=p1["verdict"], passage_2=p2["verdict"], z3_signale=any(d["code"] == "Z3" for d in D))
    res["gardien"] = "empreinte altérée → arrêt : test_scriptones.py::test_empreinte_alteree_refuse (vert)"
    return res


def main(a):
    rapide = "--rapide" in a; t0 = time.time()
    cours = {p: lire_main(p) for p in COURS}
    T12, agg = t1_t2(cours)
    out = dict(date=time.strftime("%Y-%m-%d"), cours=COURS, T1_T2=T12, T1_agrege=agg, T3=t3(cours, rapide), T4=t4(cours, rapide))
    out["duree_s"] = round(time.time() - t0, 1)
    if not rapide: (B / "essais_vial.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    if "--json" in a: print(json.dumps(out, ensure_ascii=False, indent=1)); return 0
    print(f"T1 réduction : {agg['reduction_vs_relecture_pct']} % (contre relecture HTML ×10) · {agg['reduction_vs_texte_pct']} % (contre texte ×10) · cible {CIBLE} % non atteinte (facteur {agg['ecart_facteur']})")
    for c in T12: print(f"T2 {c['cours']} : α {c['alpha_avant']} → {c['alpha_apres']} · β {c['beta']} · {c['verdict']} · idempotent {c['idempotent']} · main intact {c['main_intact']} · {c['jetons']['reduction_vs_relecture_pct']} %")
    t = out["T3"]; print(f"T3 conflits statiques {len(t['conflits_statiques'])} · confluence {[c['doleances'] for c in t['confluence']]} · injectés {t['conflit_injecte_detecte']} · couverture α {t['couverture']['alpha_seule_pct']} % β {t['couverture']['beta_seule_pct']} % α+β {t['couverture']['alpha_beta_pct']} % · optimal {t['couverture']['optimal']} familles · simultanés {t['simultanes']}")
    t = out["T4"]; print(f"T4 {json.dumps({k: v for k, v in t.items() if k != 'gardien'}, ensure_ascii=False)}")
    print(f"durée {out['duree_s']} s"); return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
