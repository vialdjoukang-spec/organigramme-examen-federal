import json, re, tempfile, time, unittest
from pathlib import Path
from aides import config_temp, PROMPT
from fabrique_lot import fabriquer
import config as cfgmod, sync_reviewer, v7_rules

class TestRelecteur(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.r = Path(self.tmp.name)
        self.cfg = cfgmod.charger(config_temp(self.r, languagetool={"url": "http://127.0.0.1:9/v2/check", "timeout_s": 2}))
    def tearDown(self): self.tmp.cleanup()

    def test_prompt_14_points(self):
        p = v7_rules.charger(PROMPT)
        self.assertEqual([n for n, _ in p["points"]], list(range(1, 15)))
        for s in ("§6.1", "§6.2", "§6.3", "§7.2", "§8.1", "§8.5", "§9.5", "§16", "§4.10"): self.assertIn(s, p["refs"])

    def test_regles_toutes_referencees(self):
        p = v7_rules.charger(PROMPT)
        for cat, r in sync_reviewer.REGLES.items():
            if not cat.startswith("_"): self.assertIn(r["section"], p["refs"], cat)

    def test_fichier_conforme_sans_p1(self):
        f, _ = fabriquer(self.r / "LOT_230" / "LOT_230_y.html")
        r = sync_reviewer.Relecteur(self.cfg).passage(str(f), avec_lt=False)
        self.assertEqual(r["compte"]["P1"], 0, [x for x in r["items"] if x["gravite"] == "P1"][:3])

    def test_defauts_detectes(self):
        f, _ = fabriquer(self.r / "LOT_230" / "LOT_230_y.html", defauts=("volume", "vague", "point_manquant", "pec_sans_source"))
        r = sync_reviewer.Relecteur(self.cfg).passage(str(f), avec_lt=False)
        t = json.dumps(r["items"], ensure_ascii=False)
        self.assertIn("points absents : 12", t)
        self.assertTrue(any(x["section"] == "§7.2" and "phrases" in x["message"] for x in r["items"]))
        self.assertIn("souvent", t); self.assertIn("il est important de noter que", t); self.assertIn("monitoring", t)
        self.assertTrue(any(x["section"] == "§4.1" for x in r["items"]))
        self.assertEqual(r["code"], 1)
        for x in r["items"]: self.assertLessEqual(len(x["message"].split()), 26)

    def test_languagetool_indisponible_non_bloquant(self):
        f, _ = fabriquer(self.r / "LOT_230" / "LOT_230_y.html")
        t0 = time.time(); r = sync_reviewer.Relecteur(self.cfg).passage(str(f), avec_lt=True)
        self.assertEqual(r["languagetool"]["statut"], "NON VÉRIFIÉ"); self.assertLess(time.time() - t0, 10)
        self.assertIn("NON VÉRIFIÉ", (Path(self.cfg["output_dir"]) / "LOT_230" / "LOT_230_y.retours.md").read_text())

    def test_incremental(self):
        f, _ = fabriquer(self.r / "LOT_230" / "LOT_230_y.html")
        rel = sync_reviewer.Relecteur(self.cfg); rel.passage(str(f), avec_lt=False)
        r2 = rel.passage(str(f), avec_lt=False)
        self.assertEqual(r2["segments_evites"], r2["monographies"])

    def test_coherence_dx(self):
        a = "<p>DX.1 — Hyponatrémie de type 1</p><p>DX.2 — SIADH</p>"
        b = "<summary>DX.1 — Hyponatrémie de type 1</summary><summary>DX.2 — Potomanie</summary>"
        it = sync_reviewer.coherence_dx(b, a)
        self.assertEqual(len(it), 1); self.assertEqual(it[0]["section"], "§9.5")

if __name__ == "__main__":
    unittest.main()
