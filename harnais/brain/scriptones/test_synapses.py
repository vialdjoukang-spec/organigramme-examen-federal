#!/usr/bin/env python3
"""Tests des 160 scriptones par le registre (unittest, stdlib) : python3 harnais/brain/scriptones/test_synapses.py [-v]
Registre (160, 20 + 70 + 70), gabarit sans dérive, empreintes, contrat JSON sur le doré et sur un mutant de chaque classe, dry-run,
idempotence des écrivains, preuve statique « un écrivain par zone », confluence de la chaîne, CLI par contrat sur stdin, doléances de Vial."""
import json, random, re, subprocess, sys, unittest
from pathlib import Path
D = Path(__file__).resolve().parent
sys.path.insert(0, str(D))
import bus, reseau, mutation

REG = reseau.registre()
PY = [e for e in REG["scriptones"] if e["langage"] == "python"]


class Registre(unittest.TestCase):
    def test_160_scriptones(self):
        z = {}
        for e in REG["scriptones"]: z[e["zone"]] = z.get(e["zone"], 0) + 1
        self.assertEqual(REG["total"], 160); self.assertEqual(z, {"transversal": 20, "alpha": 70, "beta": 70})
        self.assertEqual(len({e["id"] for e in REG["scriptones"]}), 160)
        for n in range(1, 15):
            self.assertEqual(sum(e["synapse"] == f"α{n}" for e in REG["scriptones"]), 5); self.assertEqual(sum(e["synapse"] == f"β{n}" for e in REG["scriptones"]), 5)

    def test_chaque_scriptone_a_contrat_test_mutation_empreinte(self):
        for e in REG["scriptones"]:
            self.assertTrue(e["mutants"], e["id"]); self.assertRegex(e["sha256"], r"^[0-9a-f]{64}$"); self.assertEqual(e["cout_jetons"], 0)
            p = (D / e["fichier"]).resolve(); self.assertTrue(p.exists(), e["id"]); self.assertEqual(bus.sha(p.read_bytes()), e["sha256"], f"registre périmé : {e['id']}")
            if e["langage"] == "python": self.assertEqual(bus.verifier_empreintes(bus.rel(p)), [], e["id"])

    def test_gabarit_sans_derive(self):
        r = subprocess.run([sys.executable, str(D.parent / "outils/gabarit.py"), "--verifier"], capture_output=True, text=True, timeout=120)
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_un_seul_ecrivain_par_zone(self):
        self.assertEqual(reseau.conflits_statiques(), {})
        ecr = [i for i, _ in reseau.ecrivains()]
        self.assertEqual(sorted(ecr), sorted(e["id"] for e in REG["scriptones"] if e["ecrit"] and e["langage"] == "python" and e["id"] != "s14_journal"))

    def test_jumeaux_dans_l_autre_zone_meme_point(self):
        for e in REG["scriptones"]:
            if e["zone"] in ("alpha", "beta"):
                j = reseau.entree(e["jumeau"]); self.assertIsNotNone(j, e["id"]); self.assertNotEqual(j["zone"], e["zone"]); self.assertEqual(j["point"], e["point"])

    def test_doleances_de_vial_couvertes(self):
        servies = {v for e in REG["scriptones"] for v in e["doleances_vial"]}
        self.assertTrue({1, 2, 3, 4, 5, 6, 7, 8, 9} <= servies, servies)


class Contrat160(unittest.TestCase):
    def test_dore_muet_et_mutants_detectes(self):
        for e in PY:
            m = reseau.module(e["id"]); g, _ = mutation.dore(m)
            s = bus.executer(m, "", html=g, ecrire=False); self.assertEqual(bus.valider(s), [], e["id"]); self.assertEqual(s["doleances"], [], e["id"])
            for nom, fn, code in m.MUTANTS:
                x = fn(g, random.Random(7)); x, opt = x if isinstance(x, tuple) else (x, {})
                s = bus.executer(m, "", html=x, options=opt, ecrire=False)
                self.assertEqual(bus.valider(s), [], f"{e['id']} {nom}"); self.assertIn(code, {d["code"] for d in s["doleances"]}, f"{e['id']} {nom}")
                self.assertNotIn("panne", s, f"{e['id']} {nom}")

    def test_ecrivains_idempotents_et_dry_run(self):
        g = mutation.DORE.read_text(encoding="utf-8")
        for i, _ in reseau.ecrivains():
            m = reseau.module(i)
            for nom, fn, code in m.MUTANTS[:2]:
                x = fn(g, random.Random(3)); x = x[0] if isinstance(x, tuple) else x
                c = m.corriger(x, {}); self.assertEqual(m.corriger(c, {}), c, f"{i} {nom}")
                s = bus.executer(m, "", html=x, ecrire=False); self.assertTrue(s["dry_run"]); self.assertFalse(s["modifie"])

    def test_chaine_confluente_sur_mutants(self):
        g = mutation.DORE.read_text(encoding="utf-8"); W = [i for i, _ in reseau.ecrivains()]; r = random.Random(11)
        for i in ("a02_R", "a02_Q", "b05_C", "b07_L", "s6_barre14", "a09_S"):
            x = reseau.module(i).MUTANTS[0][1](g, random.Random(5)); x = x[0] if isinstance(x, tuple) else x
            ref, _ = reseau.corriger_tout(x)
            for _ in range(3):
                o = W[:]; r.shuffle(o); self.assertEqual(reseau.corriger_tout(x, o)[0], ref, i)

    def test_cli_contrat_stdin_synapse_generee(self):
        g = mutation.DORE.read_text(encoding="utf-8"); x = reseau.module("a02_R").MUTANTS[0][1](g, random.Random(2))
        r = subprocess.run([sys.executable, str(D / "alpha/a02_R.py"), "--contrat", "-"], input=json.dumps({"html": x, "fichier": "x.html"}), capture_output=True, text=True, timeout=60)
        s = json.loads(r.stdout); self.assertEqual(bus.valider(s), []); self.assertIn("AR1", {d["code"] for d in s["doleances"]}); self.assertTrue(s["corrigeable"])

    def test_recit_negatif_supprime_sans_notion_perdue(self):
        h = ('<main><section class="monograph"><h3><strong>2. Épidémiologie</strong></h3><p>La maladie touche 3 % des adultes (OFS 2023). '
             "L'incidence suisse annuelle n'a pas été lue : À vérifier. Elle augmente avec l'âge.</p><p>Aucun chiffre suisse n'a été lu.</p></section></main>")
        m = reseau.module("a02_R"); c = m.corriger(h, {})
        self.assertNotIn("vérifier", c); self.assertNotIn("Aucun chiffre", c); self.assertIn("3 % des adultes (OFS 2023)", c); self.assertIn("Elle augmente avec l'âge.", c)
        self.assertNotIn("<p></p>", c); self.assertEqual(m.analyser(c, "t")[0], [])
        mixte = h.replace("Elle augmente avec l'âge.", "La létalité atteint 4 % ; le chiffre suisse n'a pas été lu.")
        D_ = m.analyser(mixte, "t")[0]; self.assertIn("AR2", {d["code"] for d in D_})
        self.assertIn("La létalité atteint 4 %", m.corriger(mixte, {}))          # une phrase porteuse n'est jamais supprimée par script
        self.assertEqual(m.analyser('<main><h3>2. Épidémiologie</h3><p>Le mécanisme n\'est pas connu. Les examens servent à vérifier l\'absence de contre-indication.</p></main>', "t")[0], [])

    def test_epidemiologie_en_un_bloc(self):
        h = ('<main><section class="monograph"><h3><strong>2. Épidémiologie</strong></h3><p>La maladie touche 3 % des adultes (OFS 2023).</p>'
             "<p><strong>Âge.</strong> Elle augmente avec l'âge.</p><p>Les femmes sont plus touchées (Obsan 2021).</p></section></main>")
        m = reseau.module("a02_Q"); c = m.corriger(h, {})
        self.assertEqual(c.count("<p>"), 1); self.assertEqual(bus.jetons(bus.texte(h)), bus.jetons(bus.texte(c)))       # aucun mot perdu
        self.assertEqual([d["code"] for d in m.analyser(c, "t")[0]], ["AQ2"])                                              # reste l'étiquette (agent)

    def test_barre_fixe_cliquable(self):
        g = mutation.DORE.read_text(encoding="utf-8"); nav = re.search(r'(?s)<nav id="brain-barre14".*?</nav>', g).group(0)
        self.assertEqual(len(re.findall(r'href="#', nav)), 15); ids = set(re.findall(r'\sid="([^"]+)"', g))
        self.assertTrue(all(h in ids for h in re.findall(r'href="#([^"]+)"', nav))); self.assertIn("position:fixed", g); self.assertIn("scroll-margin-top", g)


if __name__ == "__main__":
    unittest.main()
