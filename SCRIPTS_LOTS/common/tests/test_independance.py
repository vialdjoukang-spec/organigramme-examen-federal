"""v1.4 — Loi d'indépendance absolue (8 agents, 2 équipes) : chemins disjoints, périmètre LOT/Partie, partage des débits."""
import io, itertools, json, os, tempfile, unittest
from contextlib import redirect_stderr
from pathlib import Path
from aides import config_temp
from fabrique_lot import fabriquer
import config as cfgmod, source_engine, sync_reviewer
from lot_readonly import ViolationLectureSeule
RACINE = Path(__file__).resolve().parents[2]
AGENTS = range(1, 9)
EQUIPE = {1: 1, 3: 1, 5: 1, 7: 1, 2: 2, 4: 2, 6: 2, 8: 2}
CHAP = {1: ["A", "P1"], 2: ["A", "P1"], 3: ["P2"], 4: ["P2"], 5: ["P3"], 6: ["P3"], 7: ["P4"], 8: ["P4"]}
NOMS = {"A": "Appel_A_V7_Plan_et_Liste", "P1": "Appel_B_V7_Partie_1_DX.1_a_DX.2", "P2": "Appel_B_V7_Partie_2_DX.3_a_DX.5",
        "P3": "Appel_B_V7_Partie_3_DX.6_a_DX.7", "P4": "Appel_B_V7_Partie_4_DX.8_a_DX.10"}

def charger(n):
    return cfgmod.charger(RACINE / f"agent_{n}" / "config.json")

def _dedans(a, b):
    a, b = os.path.realpath(a), os.path.realpath(b)
    return os.path.commonpath([a, b]) == b

class TestIndependance(unittest.TestCase):
    def test_huit_configs_valides_et_conformes(self):
        for n in AGENTS:
            c = charger(n)
            self.assertEqual((c["agent"], c["equipe"]), (n, EQUIPE[n]))
            self.assertEqual(c["lots"], list(range(c["lot_min"], c["lot_max"] + 1)))
            lots = (227, 237) if n == 1 else (238, 248) if n == 2 else (229, 237) if EQUIPE[n] == 1 else (240, 248)
            self.assertEqual((c["lot_min"], c["lot_max"]), lots)
            self.assertEqual(cfgmod.parties_pour(c, 233 if EQUIPE[n] == 1 else 243), CHAP[n])
            for ch in cfgmod.chemins_inscriptibles(c).values():
                self.assertIn(f"agent_{n}", Path(ch).parts); self.assertNotIn("partage", Path(ch).parts)
            self.assertTrue(c["shared_state_dir"].endswith(f"agent_{n}/etat"))
            self.assertEqual(c["pubmed"]["mcp_url"], "")       # aucun serveur local commun

    def test_agent_2_lot_238_239_entiers_puis_appel_a_partie_1(self):
        c = charger(2)
        for lot in (238, 239):
            self.assertEqual(cfgmod.parties_pour(c, lot), ["A", "P1", "P2", "P3", "P4"])
        for lot in range(240, 249):
            self.assertEqual(cfgmod.parties_pour(c, lot), ["A", "P1"])
        for n in (4, 6, 8):
            cn = charger(n)
            self.assertEqual(cn["lots"], list(range(240, 249)))
            self.assertFalse(cfgmod.lot_autorise(cn, 239))

    def test_aucun_chemin_partage_entre_deux_agents(self):
        cfgs = {n: charger(n) for n in AGENTS}
        for a, b in itertools.combinations(AGENTS, 2):
            pa = list(cfgmod.chemins_inscriptibles(cfgs[a]).values()); pb = list(cfgmod.chemins_inscriptibles(cfgs[b]).values())
            for x, y in itertools.product(pa, pb):
                self.assertFalse(_dedans(x, y) or _dedans(y, x), f"agents {a} et {b} : {x} / {y}")
            da = cfgs[a]["dossier_travail"]; db = cfgs[b]["dossier_travail"]
            for x, y in itertools.product([da] if isinstance(da, str) else da, [db] if isinstance(db, str) else db):
                self.assertFalse(_dedans(x, y) or _dedans(y, x), f"dossiers de travail {a}/{b}")

    def test_chaque_fichier_v7_a_exactement_un_proprietaire(self):
        cfgs = {n: dict(charger(n), dossier_travail=None) for n in AGENTS}
        for lot in range(227, 249):
            for p, nom in NOMS.items():
                f = f"/x/LOT_{lot}/LOT_{lot}_{nom}.html"
                prop = [n for n in AGENTS if cfgmod.fichier_autorise(cfgs[n], f)[0]]
                self.assertEqual(len(prop), 1, f"{f} : {prop}")

    def test_config_independante_refuse_dossier_partage(self):
        with tempfile.TemporaryDirectory() as d:
            p = config_temp(d, agent=3, lot_min=229, lot_max=237, equipe=1,
                            cache_dir=f"{d}/agent_3/cache", output_dir=f"{d}/agent_3/retours",
                            shared_state_dir=f"{d}/partage", compteur={"csv": f"{d}/agent_3/c.csv"})
            with self.assertRaises(cfgmod.ConfigErreur): cfgmod.charger(p)
            p = config_temp(d, agent=3, lot_min=229, lot_max=237, parties_autorisees=["P9"])
            with self.assertRaises(cfgmod.ConfigErreur): cfgmod.charger(p)
            p = config_temp(d, agent=3, lot_min=229, lot_max=237, lots=[228])
            with self.assertRaises(cfgmod.ConfigErreur): cfgmod.charger(p)

class TestPerimetre(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); r = Path(self.tmp.name)
        self.lot = r / "agent3" / "LOT_230"
        self.p2, _ = fabriquer(self.lot / f"LOT_230_{NOMS['P2']}.html")
        self.p3, _ = fabriquer(self.lot / f"LOT_230_{NOMS['P3']}.html")
        self.cfg = cfgmod.charger(config_temp(r, agent=3, lot_min=229, lot_max=237, lots=list(range(229, 238)), equipe=1,
                                              chapitre="Partie 2 (DX.3–DX.5)", parties_autorisees=["P2"], dossier_travail=str(r / "agent3"),
                                              cache_dir=str(r / "agent_3" / "cache"), output_dir=str(r / "agent_3" / "retours"),
                                              shared_state_dir=str(r / "agent_3" / "etat"), compteur={"csv": str(r / "agent_3" / "c.csv")},
                                              languagetool={"enabled": False}))
        self.r = r
    def tearDown(self): self.tmp.cleanup()

    def test_check_refuse_partie_hors_chapitre(self):
        with redirect_stderr(io.StringIO()) as e:
            self.assertEqual(source_engine.check(self.cfg, str(self.p3)), 2)
        self.assertIn("P3 de LOT_230 hors du chapitre", e.getvalue())
        with redirect_stderr(io.StringIO()):
            self.assertIn(source_engine.check(self.cfg, str(self.p2)), (0, 1))     # son propre fichier : contrôlé

    def test_review_refuse_partie_lot_et_dossier(self):
        rel = sync_reviewer.Relecteur(self.cfg)
        with self.assertRaises(ViolationLectureSeule): rel.passage(str(self.p3), avec_lt=False)
        autre, _ = fabriquer(self.r / "agent3" / "LOT_240" / f"LOT_240_{NOMS['P2']}.html")
        with self.assertRaises(ViolationLectureSeule): rel.passage(str(autre), avec_lt=False)
        ailleurs, _ = fabriquer(self.r / "agent5" / "LOT_230" / f"LOT_230_{NOMS['P2']}.html")
        with self.assertRaises(ViolationLectureSeule): rel.passage(str(ailleurs), avec_lt=False)
        self.assertFalse((self.r / "agent_3" / "retours").exists())           # refus avant toute écriture
        self.assertEqual(rel.passage(str(self.p2), avec_lt=False)["integrite"], "ok")
        self.assertEqual(sync_reviewer.main(self.cfg["_chemin"], ["review", str(self.p3), "--sans-lt"]), 2)

    def test_appel_a_seule_lecture_hors_chapitre(self):
        rel = sync_reviewer.Relecteur(self.cfg)
        a, _ = fabriquer(self.lot / f"LOT_230_{NOMS['A']}.html")
        self.assertEqual(rel.passage(str(self.p2), appel_a=str(a), avec_lt=False)["integrite"], "ok")
        with self.assertRaises(ViolationLectureSeule): rel.passage(str(a), avec_lt=False)          # relire l'Appel A : interdit
        with self.assertRaises(ViolationLectureSeule): rel.passage(str(self.p2), appel_a=str(self.p3), avec_lt=False)
        a231, _ = fabriquer(self.r / "agent3" / "LOT_231" / f"LOT_231_{NOMS['A']}.html")
        with self.assertRaises(ViolationLectureSeule): rel.passage(str(self.p2), appel_a=str(a231), avec_lt=False)

    def test_config_retrocompatible_sans_champs_v14(self):
        (self.r / "v13").mkdir(); c = cfgmod.charger(config_temp(self.r / "v13"))
        self.assertTrue(cfgmod.fichier_autorise(c, "/x/LOT_230/LOT_230_Appel_B_V7_Partie_3_DX.6_a_DX.7.html")[0])
        self.assertTrue(cfgmod.fichier_autorise(c, "/x/LOT_230/LOT_230_x.html")[0])
        self.assertFalse(cfgmod.fichier_autorise(c, "/x/LOT_240/LOT_240_x.html")[0])

class TestDebits(unittest.TestCase):
    ANCIEN = {"lt_req_min": 10, "lt_octets_min": 60000, "ncbi_sans_cle": 3, "ncbi_avec_cle": 10, "domaine": 1.0}

    def test_somme_des_huit_sous_les_limites_globales(self):
        cfgs = [charger(n) for n in AGENTS]
        s = lambda f: sum(f(c) for c in cfgs)
        self.assertLessEqual(s(lambda c: c["languagetool"]["budget_req_per_min"]), self.ANCIEN["lt_req_min"])
        self.assertLessEqual(s(lambda c: c["languagetool"]["budget_bytes_per_min"]), self.ANCIEN["lt_octets_min"])
        self.assertLessEqual(s(lambda c: c["languagetool"]["max_bytes_per_request"] * 1.2), self.ANCIEN["lt_octets_min"])   # rafale cumulée
        self.assertLessEqual(s(lambda c: c["pubmed"]["rate_per_s_without_key"]), self.ANCIEN["ncbi_sans_cle"] + 1e-9)
        self.assertLessEqual(s(lambda c: c["pubmed"]["rate_per_s_with_key"]), self.ANCIEN["ncbi_avec_cle"] + 1e-9)
        self.assertLessEqual(s(lambda c: c["http"]["per_domain_per_s"]), self.ANCIEN["domaine"] + 1e-9)
        for c in cfgs:
            self.assertEqual(c["languagetool"]["budget_req_per_min"], 1)
            self.assertGreater(c["pubmed"]["rate_per_s_without_key"], 0); self.assertGreater(c["http"]["per_domain_per_s"], 0)

    def test_seau_fractionnaire_utilisable(self):
        from token_bucket import SeauPartage
        with tempfile.TemporaryDirectory() as d:
            s = SeauPartage(d, "eutils", 0.375, max(1.0, 0.375))
            self.assertTrue(s.prendre(attente_max=0)); self.assertFalse(s.prendre(attente_max=0))

    def test_seaux_de_deux_agents_independants(self):
        from token_bucket import SeauPartage
        c3, c4 = charger(3), charger(4)
        self.assertNotEqual(c3["shared_state_dir"], c4["shared_state_dir"])
        with tempfile.TemporaryDirectory() as d:
            a = SeauPartage(Path(d) / "agent_3" / "etat", "lt_public", 1 / 60, 1); b = SeauPartage(Path(d) / "agent_4" / "etat", "lt_public", 1 / 60, 1)
            a.reculer(); self.assertTrue(a.bloque()); self.assertFalse(b.bloque())   # un 429 chez l'un ne bloque pas l'autre
            self.assertTrue(b.prendre(attente_max=0))

if __name__ == "__main__":
    unittest.main()
