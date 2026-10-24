"""T10 : aucun module du script synchrone n'écrit hors de lot_readonly.ecrire_sortie ; aucune dépendance à une IA."""
import ast, re, unittest
from pathlib import Path
C = Path(__file__).resolve().parents[1]
INTERDITS = {"write_text", "write_bytes", "unlink", "rename", "rmtree", "chmod", "remove", "truncate", "symlink_to", "touch"}

class TestStatique(unittest.TestCase):
    def test_relecteur_sans_ecriture_directe(self):
        for nom in ("sync_reviewer.py", "controle_v7.py", "v7_rules.py"):
            arbre = ast.parse((C / nom).read_text())
            for n in ast.walk(arbre):
                if isinstance(n, ast.Call):
                    f = n.func; nomf = f.attr if isinstance(f, ast.Attribute) else getattr(f, "id", "")
                    self.assertNotIn(nomf, INTERDITS, f"{nom}:{n.lineno} {nomf}")
                    if nomf == "open":
                        modes = [a.value for a in n.args[1:2] if isinstance(a, ast.Constant)] + [k.value.value for k in n.keywords if k.arg == "mode" and isinstance(k.value, ast.Constant)]
                        self.assertTrue(all(set(m) <= set("rbt") for m in modes), f"{nom}:{n.lineno} open en écriture")
                        self.assertTrue(modes or nom != "sync_reviewer.py", f"{nom}:{n.lineno} open sans mode explicite")

    def test_aucune_dependance_ia(self):
        motif = re.compile(r"\b(openai|anthropic|chatgpt|gpt-[0-9]|llm|langchain|transformers|huggingface|x\.ai|grok)\b", re.I)
        for p in list(C.glob("*.py")) + list(C.parent.glob("agent_*/*.py")) + list(C.parent.glob("*.py")):
            for i, l in enumerate(p.read_text().splitlines(), 1):
                if l.lstrip().startswith(("import", "from")) or "http" in l:
                    self.assertIsNone(motif.search(l), f"{p.name}:{i}")

if __name__ == "__main__":
    unittest.main()
