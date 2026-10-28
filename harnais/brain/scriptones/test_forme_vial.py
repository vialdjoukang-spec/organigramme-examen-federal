#!/usr/bin/env python3
"""Tests d'intégrité du circuit duo → professeur (néo-conception du 28.10.2026) : rendu de l'algorithme sans ligne géante, réparation sûre
des balises et des lignes, contrôles H1/H2/Q0, sous-cellules en tableau, contrôle de langue aligné (algorithme hors prose, glossaire CSS),
porte unique `fin` (réparation automatique avant verdict).  python3 harnais/brain/scriptones/test_forme_vial.py"""
import json, re, subprocess, sys, tempfile, unittest
from pathlib import Path
D = Path(__file__).resolve().parent; R = D.parents[2]
sys.path.insert(0, str(D))
import s21_forme_vial as S


def cours(p7="<p>Texte.</p>", p8="<p>Le diagnostic repose sur la clinique.</p>", fin_="", tete=""):
    pts = "".join(f'<h3 id="dxt-p{n}"><strong>{n}. Point {n}</strong></h3>\n' + (p7 if n == 7 else p8 if n == 8 else
                  "<p>Le médecin examine la patiente avec soin.</p>") + "\n" for n in range(1, 15))
    return (f"<!DOCTYPE html><html><head>{tete}</head><body><section class=\"monograph\" id=\"dxt\">\n{pts}{fin_}</section>\n"
            "<details class=\"refs\" id=\"refs\"><summary>Sources bibliographiques</summary><ol><li>[S1] Source.</li></ol></details>\n"
            "<!-- FIN_FICHIER dxt -->")


def modele(n=60):
    no = [{"id": f"q{i}", "type": "losange" if i % 2 == 0 else "case", "texte": f"Question {i} ?",
           "detail": "Le médecin recherche le signe ; " + "le détail reste long. " * 12} for i in range(n)]
    li = [{"de": f"q{i}", "a": f"q{i + 1}", "etiquette": "Non" if i % 2 == 0 else ""} for i in range(n - 1)]
    return {"titre": "Devant le symptôme", "noeuds": no, "liens": li}


class Rendu(unittest.TestCase):
    def test_aucune_ligne_geante_et_traits_orthogonaux(self):
        h = S.rendre(modele(), "algo1")
        self.assertTrue(all(len(l) <= 10000 for l in h.split("\n")), max(len(l) for l in h.split("\n")))
        for d in re.findall(r'<path class="tr" d="([^"]*)"', h): self.assertFalse(re.search(r"[^MHV\d\s.-]", d), d)
        self.assertNotRegex(h, r"<circle|<ellipse|border-radius:\s*50%")
        self.assertEqual(h.count('class="algo-d"'), 60)

    def test_corriger_idempotent(self):
        t = cours(p8='<p>Texte.</p><template class="algo-modele">' + json.dumps(modele(5)) + "</template>")
        t1 = S.corriger(t); self.assertIn('data-brain="algo"', t1); self.assertEqual(S.corriger(t1), t1)


class Reparation(unittest.TestCase):
    def test_table_non_fermee_fermee_avant_le_point_suivant(self):
        t = cours(p8="<div style='overflow-x:auto;'><table><tr><td>a</td></tr>\n<p>suite</p>")
        self.assertTrue(any(n == 8 for *_, n in S.desequilibres(t)))
        t2, J = S.equilibrer(t)
        self.assertEqual(S.desequilibres(t2), []); self.assertIn("</table></div><h3 id=\"dxt-p9\"", t2); self.assertTrue(J)

    def test_fermante_orpheline_retiree(self):
        t = cours(p8="<p>Texte.</p></div>")
        t2, J = S.equilibrer(t)
        self.assertEqual(S.desequilibres(t2), []); self.assertNotIn("</p></div>", t2); self.assertIn("orpheline", J[0])

    def test_fichier_equilibre_intact(self):
        t = cours(); self.assertEqual(S.equilibrer(t), (t, []))

    def test_lignes_coupees_hors_modele(self):
        long_ = "".join(f"<p>Phrase {i} du cours.</p>" for i in range(900))
        tpl = '<template class="algo-modele">{"x":"' + "</p>" * 3000 + '"}</template>'
        t = cours(p8=long_ + tpl)
        t2, J = S.couper_lignes(t)
        self.assertTrue(J); self.assertIn(tpl, t2)                       # modèle JSON jamais coupé
        self.assertEqual(re.sub(r"\s", "", t2), re.sub(r"\s", "", t))     # rien d'ajouté ni de retiré hors sauts de ligne
        self.assertTrue(all(len(l) <= 10000 or "algo-modele" in l for l in t2.split("\n")))


class Controles(unittest.TestCase):
    def codes(self, t): return {d["code"] for d in S.analyser(t, "t.html")[0]}

    def test_h1_h2(self):
        self.assertIn("H1", self.codes(cours(p8="<div><p>a</p>")))
        self.assertIn("H2", self.codes(cours(p8="<p>" + "mot " * 3000 + "</p>")))

    def test_q0_sans_syndrome(self):
        self.assertIn("Q0", self.codes(cours()))

    def test_syndrome_en_tableau(self):
        sc = ('<span class="sc dx"><input type="checkbox" id="p7-1-a"><label class="dxt" for="p7-1-a">Rougeur</label>'
              '<span class="dxc"><b>Recherche :</b> Le médecin inspecte le visage pendant l\'accès.</span></span>')
        p7 = ("<div style='overflow-x:auto;'><table><tr><th>Syndrome</th><th>Symptômes fonctionnels</th><th>Signes physiques</th></tr>"
              f"<tr><td><em>7.1</em> Syndrome vasomoteur</td><td><ul><li>Bouffées</li></ul></td><td>{sc}</td></tr></table></div>")
        c = self.codes(cours(p7=p7)); self.assertFalse(c & {"Q0", "Q2", "Q3", "Q4"}, c)
        c = self.codes(cours(p7=p7.replace("Symptômes fonctionnels", "Signes fonctionnels"))); self.assertIn("Q2", c)


class Langue(unittest.TestCase):
    def test_algorithme_hors_prose_et_glossaire(self):
        algo = S.rendre(modele(8), "algo1").replace("le détail reste long. ", "le détail reste long et le médecin le lit. ")
        glos = '<style>abbr[data-k="XYZQ"]::after{content:"XYZQ : sigle de test"}</style>'
        t = cours(p8="<p>Le XYZQ guide la décision clinique du médecin.</p>", tete=glos).replace(
            '<h3 id="dxt-p10"><strong>10. Point 10</strong></h3>\n<p>Le médecin examine la patiente avec soin.</p>',
            '<h3 id="dxt-p10"><strong>10. Point 10</strong></h3>\n<p>L\'algorithme écarte d\'abord les urgences vitales du patient.</p>' + algo)
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "t.html"; f.write_text(t, encoding="utf-8"); r = Path(d) / "r.md"
            subprocess.run([sys.executable, str(R / "harnais/controle_langue.py"), str(f), "--rapport", str(r)], cwd=R, capture_output=True, timeout=600)
            x = r.read_text(encoding="utf-8")
        self.assertNotIn("[PHRASES] point 10", x); self.assertNotIn("XYZQ", x.split("abréviation")[1].splitlines()[0])


class PorteUnique(unittest.TestCase):
    def test_fin_repare_avant_verdict(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "LOT_999_Phase_B_V0_DX.1.html"; f.write_text(cours(), encoding="utf-8")
            run = lambda *a: subprocess.run([sys.executable, str(R / "harnais/brain/circuit_vial.py"), *a], cwd=R, capture_output=True, text=True, timeout=900)
            run("memoire", "duo", str(f))
            f.write_text(cours(p8="<div style='overflow-x:auto;'><table><tr><td>Le tableau reste ouvert.</td></tr>"), encoding="utf-8")
            p = run("fin", str(f), "--role", "duo")
            self.assertIn("RÉPARÉ", p.stdout, p.stdout + p.stderr); self.assertNotEqual(p.returncode, 0)   # réparé, mais refusé (Q0, etc.)
            self.assertEqual(S.desequilibres(f.read_text(encoding="utf-8")), [])
            self.assertIn("langue", p.stdout)                                                               # la porte mesure la langue d'audit_lot

    def test_retrait_declare(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "LOT_999_Phase_B_V0_DX.1.html"; f.write_text(cours(p8="<p>Le seuil retenu est de 12 % chez les patientes.</p>"), encoding="utf-8")
            run = lambda *a: subprocess.run([sys.executable, str(R / "harnais/brain/circuit_vial.py"), *a], cwd=R, capture_output=True, text=True, timeout=900)
            run("memoire", "duo", str(f)); f.write_text(cours(), encoding="utf-8")
            self.assertIn("chiffres disparus", run("fin", str(f), "--role", "duo").stdout)
            self.assertNotEqual(run("retirer", str(f), "12 %", "faux").returncode, 0)                     # motif trop court : refusé
            self.assertEqual(run("retirer", str(f), "12 %", "introuvable dans le résumé PubMed de la source citée").returncode, 0)
            p = run("fin", str(f), "--role", "duo"); self.assertNotIn("chiffres disparus", p.stdout); self.assertIn("RETRAITS DÉCLARÉS", p.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=1)
