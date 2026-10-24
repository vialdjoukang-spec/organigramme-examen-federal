import json, multiprocessing, tempfile, time, unittest
from pathlib import Path
from aides import config_temp
import config as cfgmod, compteur_tokens
from token_bucket import SeauPartage
RACINE = Path(__file__).resolve().parents[2]

def _prendre(d, q):
    s = SeauPartage(d, "lt_public", 10 / 60, 5); q.put(sum(s.prendre(attente_max=0) for _ in range(5)))

class TestPartage(unittest.TestCase):
    def test_seau_partage_entre_deux_processus(self):
        with tempfile.TemporaryDirectory() as d:
            q = multiprocessing.Queue(); ps = [multiprocessing.Process(target=_prendre, args=(d, q)) for _ in range(2)]
            [p.start() for p in ps]; [p.join() for p in ps]
            self.assertEqual(q.get() + q.get(), 5)       # capacité commune : 5 jetons au total, pas 10

    def test_recul_partage(self):
        with tempfile.TemporaryDirectory() as d:
            a = SeauPartage(d, "x", 1, 3); b = SeauPartage(d, "x", 1, 3)
            self.assertEqual(a.reculer(), 30); self.assertTrue(b.bloque()); self.assertFalse(b.prendre(attente_max=0))

    def test_configs_agents_disjointes(self):
        c1 = cfgmod.charger(RACINE / "agent_1" / "config.json"); c2 = cfgmod.charger(RACINE / "agent_2" / "config.json")
        self.assertEqual((c1["lot_min"], c1["lot_max"], c2["lot_min"], c2["lot_max"]), (227, 237, 238, 248))
        for k in ("cache_dir", "output_dir"): self.assertNotEqual(c1[k], c2[k])
        self.assertEqual(c1["shared_state_dir"], c2["shared_state_dir"])
        self.assertNotEqual(c1["compteur"]["csv"], c2["compteur"]["csv"])
        self.assertEqual(c1["languagetool"]["budget_req_per_min"], 10)

    def test_config_invalide(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "c.json"; p.write_text(json.dumps({"agent": 1}))
            with self.assertRaises(cfgmod.ConfigErreur): cfgmod.charger(p)

class TestCompteur(unittest.TestCase):
    def test_compteur(self):
        with tempfile.TemporaryDirectory() as d:
            cfg = cfgmod.charger(config_temp(d))
            with self.assertRaises(ValueError): compteur_tokens.ajouter(cfg, "LOT_227", "1", " ".join(["mot"] * 16))
            with self.assertRaises(ValueError): compteur_tokens.ajouter(cfg, "LOT_240", "1", "LOT_240 terminé")
            compteur_tokens.ajouter(cfg, "LOT_227", "1", "LOT_227 terminé ; suivi coché.")
            compteur_tokens.ajouter(cfg, "LOT_228", "1", "LOT_228 terminé ; suivi coché.")
            compteur_tokens.ajouter(cfg, "LOT_228", "3", "URGENT · Agent 1 · LOT_228 : AIPS inaccessible.")
            compteur_tokens.ajouter(cfg, "LOT_228", "T", "Retour relecteur : 3 P2 corrigés ; détail dans le suivi.")
            r = compteur_tokens.calculer(cfg)
            self.assertEqual(r["mesure"]["messages_envoyes"], 3); self.assertEqual(r["mesure"]["informations_routees_vers_tunder"], 1)
            e = r["estimation"]; self.assertEqual(e["messages_sans_regle"], 2 * 19)
            self.assertEqual(e["jetons_economises"], (38 - 3) * (120 + 120))
            self.assertIn("ESTIMATION", compteur_tokens.rendu([r]))

if __name__ == "__main__":
    unittest.main()
