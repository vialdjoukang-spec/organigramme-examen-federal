"""Les TROIS tests prouvant la lecture seule du script synchrone sur les LOT (cahier §3.2, T8–T10)."""
import errno, os, stat, sys, tempfile, unittest
from pathlib import Path
from aides import config_temp
from fabrique_lot import fabriquer
import config as cfgmod, lot_readonly, sync_reviewer
from lot_readonly import ViolationLectureSeule

class TestLectureSeule(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); r = Path(self.tmp.name)
        self.lot = r / "LOTS" / "LOT_230"; self.f, _ = fabriquer(self.lot / "LOT_230_Appel_B_V7_Partie_2_DX.3_a_DX.5.html")
        self.cfg = cfgmod.charger(config_temp(r, languagetool={"enabled": False}))
    def tearDown(self):
        for p in self.lot.rglob("*"): os.chmod(p, 0o644)
        os.chmod(self.lot, 0o755); self.tmp.cleanup()

    def test_1_empreintes_inchangees_apres_100_passages(self):
        avant = lot_readonly.empreintes(self.lot); rel = sync_reviewer.Relecteur(self.cfg)
        for _ in range(100):
            r = rel.passage(str(self.f), avec_lt=False); self.assertEqual(r["integrite"], "ok")
        self.assertEqual(avant, lot_readonly.empreintes(self.lot))
        self.assertEqual(sorted(p.name for p in self.lot.iterdir()), [Path(self.f).name])   # aucun fichier ajouté au LOT

    def test_2_tentative_ecriture_refusee(self):
        fd = lot_readonly.ouvrir_lecture(self.f)
        try:
            with self.assertRaises(OSError) as e: os.write(fd, b"x")
            self.assertEqual(e.exception.errno, errno.EBADF)       # descripteur ouvert en O_RDONLY
        finally:
            os.close(fd)
        with self.assertRaises(ViolationLectureSeule):              # l'écrivain des scripts refuse tout chemin dans un LOT
            lot_readonly.ecrire_sortie(self.lot / "pirate.md", "x", self.lot, [str(self.lot)])
        with self.assertRaises(ViolationLectureSeule):
            lot_readonly.ecrire_sortie(self.lot / "pirate.md", "x", self.cfg["output_dir"], [str(self.lot)])
        os.chmod(self.f, 0o444); os.chmod(self.lot, 0o555)          # montage/permissions en lecture seule : le système refuse aussi
        if os.geteuid() != 0:
            with self.assertRaises(PermissionError): open(self.f, "a")
            cfg = dict(self.cfg, enforce_os_readonly=True)
            r = sync_reviewer.Relecteur(cfg).passage(str(self.f), avec_lt=False)   # le mode strict accepte un LOT non inscriptible
            self.assertIn(r["code"], (0, 1))
        os.chmod(self.lot, 0o755)
        with self.assertRaises(ViolationLectureSeule):              # et refuse de tourner si le LOT reste inscriptible
            sync_reviewer.Relecteur(dict(self.cfg, enforce_os_readonly=True)).passage(str(self.f), avec_lt=False)

    def test_3_isolation_du_dossier_de_sortie(self):
        for cle in ("output_dir", "cache_dir"):
            cfg = dict(self.cfg); cfg[cle] = str(self.lot / "retours")
            with self.assertRaises(ViolationLectureSeule):
                sync_reviewer.Relecteur(cfg).passage(str(self.f), avec_lt=False)
        cfg = dict(self.cfg); cfg["output_dir"] = str(self.lot.parent)          # LOT contenu dans la sortie : refus
        with self.assertRaises(ViolationLectureSeule):
            sync_reviewer.Relecteur(cfg).passage(str(self.f), avec_lt=False)
        self.assertFalse((self.lot / "retours").exists())
        r = sync_reviewer.Relecteur(self.cfg).passage(str(self.f), avec_lt=False)
        self.assertTrue((Path(self.cfg["output_dir"]) / "LOT_230").is_dir())

    def test_4_lot_hors_serie_refuse(self):
        autre = Path(self.tmp.name) / "LOTS" / "LOT_240"; g, _ = fabriquer(autre / "LOT_240_Appel_A_V7_Plan_et_Liste.html", lot=240)
        with self.assertRaises(ViolationLectureSeule):
            sync_reviewer.Relecteur(self.cfg).passage(str(g), avec_lt=False)

    def test_5_alerte_si_lot_modifie_pendant_le_passage(self):
        rel = sync_reviewer.Relecteur(self.cfg); orig = lot_readonly.empreintes
        etat = {"n": 0}
        def falsifie(d):
            etat["n"] += 1; e = orig(d)
            if etat["n"] == 2: e = {k: "0" * 64 for k in e}
            return e
        sync_reviewer.lot_readonly.empreintes = falsifie
        try:
            r = rel.passage(str(self.f), avec_lt=False)
        finally:
            sync_reviewer.lot_readonly.empreintes = orig
        self.assertEqual(r["code"], 3)
        self.assertTrue(list((Path(self.cfg["output_dir"]) / "LOT_230").glob("ALERTE_*.md")))

if __name__ == "__main__":
    unittest.main()
