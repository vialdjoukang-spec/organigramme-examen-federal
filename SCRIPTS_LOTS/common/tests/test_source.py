import json, tempfile, time, unittest
from pathlib import Path
from aides import config_temp
from fabrique_lot import fabriquer
import config as cfgmod, source_engine
from netutil import ErreurSource, ListeBlanche

class TestSource(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.r = Path(self.tmp.name)
        self.cfg = cfgmod.charger(config_temp(self.r))
    def tearDown(self): self.tmp.cleanup()

    def test_check_bloque_affirmation_sans_source(self):
        f, _ = fabriquer(self.r / "LOT_230" / "LOT_230_x.html", defauts=("pec_sans_source",))
        self.assertEqual(source_engine.check(self.cfg, str(f), "json"), 1)
        pb, st = source_engine.verifier_sources(Path(f).read_text())
        self.assertTrue(any(x["section"] == "§4.1" and x["point"] == 11 for x in pb))

    def test_check_fichier_source_passe(self):
        f, _ = fabriquer(self.r / "LOT_230" / "LOT_230_x.html")
        self.assertEqual(source_engine.check(self.cfg, str(f), "json"), 0)

    def test_check_reference_absente_et_source_sans_date(self):
        html = "<p>La dose atteint 5 mg/kg [S9].</p><h2>Sources</h2><ol><li>[S1] https://www.bag.admin.ch/ sans date</li></ol>"
        pb, st = source_engine.verifier_sources(html)
        msgs = " ".join(x["message"] for x in pb)
        self.assertIn("[S9] cité mais absent", msgs); self.assertIn("sans date", msgs)

    def test_check_pec_sources_niveau4_seulement(self):
        html = ("<p><strong>11. Prise en charge</strong></p><p>La dose atteint 5 mg/kg [S1].</p>"
                "<h2>Sources</h2><ol><li>[S1] IDSA https://www.idsociety.org/ consulté le 2026-10-24</li></ol>")
        pb, _ = source_engine.verifier_sources(html)
        self.assertTrue(any(x["section"] == "§4.2" and x["point"] == 11 for x in pb))

    def test_check_refuse_lot_autre_agent(self):
        f, _ = fabriquer(self.r / "LOT_240" / "LOT_240_x.html", lot=240)
        self.assertEqual(source_engine.check(self.cfg, str(f), "json"), 2)

    def test_liste_blanche(self):
        lb = ListeBlanche()
        self.assertEqual(lb.niveau("https://www.bag.admin.ch/fr/x"), 1)
        self.assertEqual(lb.niveau("https://www.sgaim.ch/"), 2)
        self.assertEqual(lb.niveau("https://www.escardio.org/"), 3)
        self.assertEqual(lb.niveau("https://www.who.int/"), 4)
        for u in ("https://exemple.com/", "http://www.bag.admin.ch/", "https://www.ssai-sgai.ch/"):
            with self.assertRaises(ErreurSource): lb.autoriser(u)
        with self.assertRaises(ErreurSource) as e: lb.autoriser("https://www.cdc.gov/")
        self.assertEqual(e.exception.code, "BLOQUE_ROBOTS")

    def test_classement_niveau_puis_pec(self):
        ix = source_engine.Index(self.cfg["cache_dir"]); d = time.strftime("%Y-%m-%d")
        ix.ajouter("https://www.escardio.org/a", "www.escardio.org", 3, "Hyponatrémie ESC", "hyponatrémie traitement traitement prise en charge", d)
        ix.ajouter("https://www.bag.admin.ch/b", "www.bag.admin.ch", 1, "Hyponatrémie OFSP", "hyponatrémie épidémiologie", d)
        ix.ajouter("https://www.sgaim.ch/c", "www.sgaim.ch", 2, "Hyponatrémie SSMIG", "hyponatrémie prise en charge traitement posologie", d)
        ix.ajouter("https://www.sgaim.ch/d", "www.sgaim.ch", 2, "Hyponatrémie histoire", "hyponatrémie histoire", d)
        r = ix.chercher("hyponatrémie", pec=True)
        self.assertEqual([x["niveau"] for x in r], [1, 2, 2, 3])
        self.assertEqual(r[1]["url"], "https://www.sgaim.ch/c")       # priorité prise en charge à niveau égal
        self.assertTrue(all(x["consulte_le"] and x["url"] for x in r))

    def test_extraction_html(self):
        page = source_engine.extraire({"type": "text/html", "corps": "<html><title>T</title><nav>menu</nav><p>La dose est de 5 mg.</p><a href='/x'>x</a></html>".encode(), "url": "https://www.bag.admin.ch/"})
        self.assertEqual(page["titre"], "T"); self.assertNotIn("menu", page["texte"]); self.assertIn("https://www.bag.admin.ch/x", page["liens"])

if __name__ == "__main__":
    unittest.main()
