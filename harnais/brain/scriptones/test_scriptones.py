#!/usr/bin/env python3
"""Tests unitaires des scriptones (unittest, stdlib) : python3 harnais/brain/scriptones/test_scriptones.py [-v]
Contrat JSON, dry-run, --appliquer, idempotence, empreintes, mutation, cas réels connus (police cassée, arbre, tableaux, budgets)."""
import hashlib, importlib, json, os, random, shutil, subprocess, sys, tempfile, unittest
from pathlib import Path
D = Path(__file__).resolve().parent
sys.path.insert(0, str(D))
import bus, mutation

NOMS = mutation.NOMS
DORE = (D.parent / "dore/cours_dore.html").read_text(encoding="utf-8")
M = {n: importlib.import_module(n) for n in NOMS}


class Contrat(unittest.TestCase):
    def test_sortie_valide_dore_et_mutants(self):
        for n, m in M.items():
            s = bus.executer(m, "", html=DORE, ecrire=False); self.assertEqual(bus.valider(s), [], n); self.assertEqual(s["doleances"], [], n)
            for nom, fn, code in m.MUTANTS:
                s = bus.executer(m, "", html=fn(DORE, random.Random(1)), ecrire=False)
                self.assertEqual(bus.valider(s), [], f"{n} {nom}"); self.assertIn(code, {d["code"] for d in s["doleances"]}, f"{n} {nom}")
                for d in s["doleances"]: self.assertTrue(d["correction_prescrite"] and d["ancre"] and d["region"] == m.REGION)

    def test_contrat_stdin(self):
        c = json.dumps({"html": M["s8_tableaux"].MUTANTS[0][1](DORE, random.Random(2)), "fichier": "x.html"})
        r = subprocess.run([sys.executable, str(D / "s8_tableaux.py"), "--contrat", "-"], input=c, capture_output=True, text=True, timeout=60)
        s = json.loads(r.stdout); self.assertEqual(bus.valider(s), []); self.assertTrue(s["dry_run"]); self.assertIn("T2", {d["code"] for d in s["doleances"]})


class Fichiers(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp()); self.f = self.d / "c.html"
        self.f.write_text(M["s1_police"].MUTANTS[4][1](DORE, random.Random(3)), encoding="utf-8")   # police cassée (P7)

    def tearDown(self): shutil.rmtree(self.d, ignore_errors=True)

    def sha(self): return hashlib.sha256(self.f.read_bytes()).hexdigest()

    def test_dry_run_n_ecrit_rien(self):
        h = self.sha(); r = subprocess.run([sys.executable, str(D / "s1_police.py"), str(self.f)], capture_output=True, text=True)
        self.assertEqual(r.returncode, 1); self.assertIn("P7", r.stdout); self.assertEqual(self.sha(), h)

    def test_appliquer_puis_idempotent(self):
        r = subprocess.run([sys.executable, str(D / "s1_police.py"), str(self.f), "--appliquer", "--json"], capture_output=True, text=True)
        s = json.loads(r.stdout); self.assertTrue(s["modifie"]); self.assertEqual([d for d in s["doleances"] if d["code"] == "P7"], [])
        h = self.sha(); r = subprocess.run([sys.executable, str(D / "s1_police.py"), str(self.f), "--appliquer", "--json"], capture_output=True, text=True)
        self.assertFalse(json.loads(r.stdout)["modifie"]); self.assertEqual(self.sha(), h)

    def test_empreinte_alteree_refuse(self):
        c = self.d / "copie"; shutil.copytree(D, c, ignore=shutil.ignore_patterns("__pycache__"))
        subprocess.run([sys.executable, "-c", "import sys;sys.path.insert(0,'.');import bus;bus.ecrire_empreintes()"], cwd=c, check=True)
        with open(c / "s3_concision.py", "a") as fh: fh.write("\n# altération\n")
        r = subprocess.run([sys.executable, str(c / "s3_concision.py"), str(self.f)], capture_output=True, text=True)
        self.assertEqual(r.returncode, 3); self.assertIn("ALTÉRATION", r.stdout)


class Pipeline(unittest.TestCase):
    def test_pipeline_idempotent_et_sans_perte(self):
        sys.path.insert(0, str(D.parent)); import cerveau
        src = (D.parent / "dore/source.html").read_text(encoding="utf-8")
        for x in (src, DORE, M["s1_police"].MUTANTS[4][1](DORE, random.Random(9))):
            a = cerveau.corriger(x); self.assertEqual(cerveau.corriger(a), a)
            n0 = sorted(bus.jetons(bus.texte_visible(x[slice(*bus.bornes_cours(x))])) - bus.jetons(bus.texte_visible(a[slice(*bus.bornes_cours(a))])))
            self.assertEqual([w for w in n0 if not w.isdigit() and w not in {"classi"}], [], "notion perdue par une correction mécanique")   # résumé « Classification » de l'arbre → titre de carte (voulu, comme forme_interactive)


class Mutation(unittest.TestCase):
    def test_mutation_verte(self):
        r = mutation.lancer(8); self.assertTrue(r["vert"], (r["faux_positifs"], r["evasions"][:3], r["idempotence_ko"])); self.assertEqual(r["detectes"], r["total"])


class Unitaires(unittest.TestCase):
    def test_phrases_decimales(self):
        self.assertEqual(len(bus.phrases("La mortalité atteint 22,3 %. Elle monte à 25,3 % après 65 ans, p. ex. chez l'âgé.")), 2)

    def test_police_cassee(self):
        s1 = M["s1_police"]; ok = s1._fonte()
        self.assertFalse(s1.cassee(ok)); self.assertTrue(s1.cassee('url(data:font/woff2;base64,d09GMgAB\nAAAA)'))
        self.assertTrue(max(len(l) for l in ok.split("\n")) < 3000)

    def test_creux_retire_sans_toucher_le_reste(self):
        h = "<main><section class=\"monograph\"><h3><strong>1. X</strong></h3><p>En effet, le médecin examine la peau. Il est important de noter que la dose baisse.</p></section></main>"
        self.assertIn("<p>Le médecin examine la peau. La dose baisse.</p>", M["s3_concision"].corriger(h))

    def test_portee_tableau(self):
        h = ("<main><section class=\"monograph\"><h3><strong>2. Épidémiologie</strong></h3><table><caption>Gravité, adultes, Berne, 2000–2019, n = 439</caption>"
             "<tr><th>Stade</th><th>Part des cas</th><th>Mortalité</th></tr><tr><td>Léger</td><td>63 %</td><td>16 %</td></tr><tr><td>Sévère</td><td>37 %</td><td>38 %</td></tr></table></section></main>")
        Dl, _ = M["s8_tableaux"].analyser(h, "t"); t4 = [d for d in Dl if d["code"] == "T4"]
        self.assertEqual(len(t4), 1); self.assertIn("Mortalité dans ce stade (%)", t4[0]["correction_prescrite"])
        self.assertIn("<th>Mortalité (%)</th>", M["s8_tableaux"].corriger(h)); self.assertIn("<td>16 %</td>", M["s8_tableaux"].corriger(h))

    def test_arbre_brut_vers_deroulant(self):
        src = (D.parent / "dore/source.html").read_text(encoding="utf-8"); s5 = M["s5_arbre"]
        a, f, typ, mod = s5.trouver(src); self.assertEqual(typ, "brut"); ch = s5.chemin(mod)
        self.assertEqual([len(n["enfants"]) for n in ch], [3, 4, 0]); self.assertTrue(ch[-1]["cible"])
        r = s5.corriger(src); self.assertEqual(r.count('<details class="arbn'), 3); self.assertIn('class="cible"', r)
        self.assertEqual(s5.corriger(r), r)

    def test_budget_point2(self):
        Dl, Mx = M["s4_budget"].analyser(M["s4_budget"].MUTANTS[0][1](DORE, random.Random(5)), "t")
        b1 = [d for d in Dl if d["code"] == "B1"][0]; self.assertIn("439", b1["correction_prescrite"]); self.assertGreater(Mx["lignes_point_2"], 4)


@unittest.skipUnless(shutil.which("node") and subprocess.run(["node", "-e", "require('playwright')"], capture_output=True).returncode == 0 and not os.environ.get("BRAIN_SANS_NAVIGATEUR"), "playwright absent")
class Captures(unittest.TestCase):
    def test_police_cassee_vue_au_navigateur(self):
        d = Path(tempfile.mkdtemp())
        try:
            (d / "LOT_000_Phase_B_V0_DX.1.html").write_text(M["s1_police"].MUTANTS[4][1](DORE, random.Random(3)), encoding="utf-8")
            (d / "LOT_000_Phase_B_V0_DX.2.html").write_text(DORE, encoding="utf-8")
            r = subprocess.run(["node", str(D.parents[1] / "bilan/captures.js"), "--fichier", str(d / "LOT_000_Phase_B_V0_DX.1.html"), str(d / "LOT_000_Phase_B_V0_DX.2.html"),
                                "--sortie", str(d / "out"), "--chapitres", "2"], capture_output=True, text=True, timeout=180)
            self.assertEqual(r.returncode, 0, r.stderr[-300:]); j = json.loads((d / "out/captures.json").read_text())
            v1 = {x["fichier"] for x in j["doleances"] if x["code"] == "V1" and x["severite"] == "CRITIQUE"}
            self.assertEqual(v1, {"LOT_000_Phase_B_V0_DX.1.html"})
            idx = [c["index"] for c in j["captures"] if c["fichier"].endswith("DX.2.html")]; self.assertEqual(len(set(idx)), 2)
            self.assertTrue(all(c["image"] for c in j["captures"]))
        finally: shutil.rmtree(d, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
