#!/usr/bin/env python3
"""Banc d'essai sur un LOT FICTIF créé dans /tmp (jamais un vrai LOT). Aucun accès réseau."""
import io, contextlib, json, random, shutil, statistics, sys, tempfile, time
from pathlib import Path
C = Path(__file__).resolve().parents[1] / "common"; sys.path.insert(0, str(C)); sys.path.insert(0, str(C / "tests"))
from aides import config_temp
from fabrique_lot import fabriquer
import config as cfgmod, lot_readonly, source_engine, sync_reviewer

def mesure(f, n):
    t = []
    for _ in range(n):
        t0 = time.perf_counter(); f(); t.append((time.perf_counter() - t0) * 1000)
    return round(statistics.median(t), 1), round(max(t), 1)

def main():
    r = Path(tempfile.mkdtemp(prefix="banc_lot_", dir="/tmp")); lot = r / "LOTS" / "LOT_230"
    noms = ["Appel_A_V7_Plan_et_Liste", "Appel_B_V7_Partie_1_DX.1_a_DX.2", "Appel_B_V7_Partie_2_DX.3_a_DX.5", "Appel_B_V7_Partie_3_DX.6_a_DX.7", "Appel_B_V7_Partie_4_DX.8_a_DX.10"]
    fichiers = [fabriquer(lot / f"LOT_230_{n}.html", cible=150_000)[0] for n in noms]
    cfg = cfgmod.charger(config_temp(r, languagetool={"enabled": False})); empreinte0 = lot_readonly.empreintes(lot)
    taille = [round(Path(f).stat().st_size / 1024) for f in fichiers]
    res = {"lot_fictif": str(lot), "tailles_ko": taille}
    rel = sync_reviewer.Relecteur(cfg); f = str(fichiers[2])
    t0 = time.perf_counter(); rel.passage(f, avec_lt=False); res["relecture_froide_ms"] = round((time.perf_counter() - t0) * 1000, 1)
    res["relecture_incrementale_ms_mediane_max"] = mesure(lambda: rel.passage(f, avec_lt=False), 10)
    def lot_complet():
        for g in fichiers: rel.passage(str(g), avec_lt=False)
    res["relecture_lot_complet_5_fichiers_ms"] = mesure(lot_complet, 3)
    with contextlib.redirect_stdout(io.StringIO()):
        res["check_sources_ms"] = mesure(lambda: source_engine.check(cfg, f, "json"), 10)
    res["empreintes_sha256_lot_ms"] = mesure(lambda: lot_readonly.empreintes(lot), 10)
    ix = source_engine.Index(cfg["cache_dir"]); rnd = random.Random(1)
    vocab = "hyponatrémie natrémie traitement prise en charge sepsis pneumonie antibiotique posologie grossesse enfant insuffisance rénale vaccination diabète insuline asthme bronchopneumopathie urgence surveillance critère sortie".split()
    t0 = time.perf_counter()
    for i in range(3000):
        txt = " ".join(rnd.choice(vocab) for _ in range(400))
        ix.c.execute("insert into pages values(?,?,?,?,?,?,?)", (f"https://www.bag.admin.ch/p{i}", "www.bag.admin.ch", rnd.randint(1, 5), f"Page {i} " + rnd.choice(vocab), txt, source_engine.score_pec(txt), "2026-10-24"))
    ix.c.commit(); res["indexation_3000_pages_ms"] = round((time.perf_counter() - t0) * 1000, 1)
    res["recherche_index_3000_pages_ms"] = mesure(lambda: ix.chercher("hyponatrémie traitement grossesse", pec=True), 20)
    res["integrite"] = "LOT fictif inchangé après tous les passages" if lot_readonly.empreintes(lot) == empreinte0 else "MODIFIÉ — ANOMALIE"
    print(json.dumps(res, ensure_ascii=False, indent=1)); shutil.rmtree(r)

if __name__ == "__main__":
    main()
