"""Garde-fous R15 : classement des PR et section « Automates actifs » (hors réseau)."""
import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools", "garde"))
import checkpoint
from commun import classer


class T(unittest.TestCase):
    def test_classer(self):
        self.assertEqual(classer(["data/ck/mono/a.json", "ETAT.json"]), "contenu")
        self.assertEqual(classer(["ETAT.json", "journal/x.md", "docs/releves/r.md"]), "releve")
        self.assertEqual(classer(["tools/x.py"]), "autre")

    def test_automates(self):
        F = []
        checkpoint.ctrl_automates("Résumé", F)
        self.assertTrue(F and F[0].startswith("A"))
        F = []
        checkpoint.ctrl_automates("## Automates actifs\n- `tools/prev_build.py`\n- `ssp-audit-medical`\n", F)
        self.assertEqual(F, [])
        F = []
        checkpoint.ctrl_automates("## Automates actifs\n- `fantome.py`\n", F)
        self.assertIn("fantome.py", F[0])


if __name__ == "__main__":
    unittest.main()
