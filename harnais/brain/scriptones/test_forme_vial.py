#!/usr/bin/env python3
"""Tests d'intégrité du circuit duo → professeur (néo-conception du 28.10.2026) : rendu de l'algorithme sans ligne géante, réparation sûre
des balises et des lignes, contrôles H1/H2/Q0, sous-cellules en tableau, contrôle de langue aligné (algorithme hors prose, glossaire CSS),
porte unique `fin` (réparation automatique avant verdict) ; Cours Flash (volume, îlots, fenêtres modales, gabarit, mode mémorisé, lanceur).  python3 harnais/brain/scriptones/test_forme_vial.py"""
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


class Registre(unittest.TestCase):
    def test_registre_tableau_et_marquage(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "LOT_999_Phase_B_V0_DX.1.html"; f.write_text(cours(p8="<div><p>On voit ça.</p>"), encoding="utf-8")
            run = lambda *a: subprocess.run([sys.executable, str(R / "harnais/brain/circuit_vial.py"), *a], cwd=R, capture_output=True, text=True, timeout=900)
            run("registre", str(f), "--json", f"{d}/r.json", "--md", f"{d}/r.md", "--marquer", f"{d}/c.html")
            reg = json.loads(Path(f"{d}/r.json").read_text())["fautes"]
            self.assertTrue(any(r["code"] == "H1" and r["severite"] == "GRAVE" and r["ligne"] > 0 for r in reg))
            self.assertIn("| fichier | ligne | ancre | sévérité | code | constat | correction attendue | contexte |", Path(f"{d}/r.md").read_text())
            self.assertIn("brain-faute", Path(f"{d}/c.html").read_text())


# ───────────────────────── COURS FLASH (harnais/etat/COURS_FLASH.md) ─────────────────────────
GAB = R / "harnais/brain/gabarit_flash.html"


def gabarit(): return GAB.read_text(encoding="utf-8")


def flash_codes(t, sev=None):
    return {d["code"] for d in S.flash(t, "t.html")[0] if sev is None or d["severite"] == sev}


def gonfler(t, octets):
    """Porte le fichier à `octets` (commentaire de remplissage avant FIN_FICHIER : aucun contenu)."""
    n = octets - len(t.encode()) - 9
    return t.replace("<!-- FIN_FICHIER", "<!--" + "x" * max(n, 0) + "-->\n<!-- FIN_FICHIER")


class Flash(unittest.TestCase):
    def test_gabarit_conforme_et_css_identique(self):
        t = gabarit(); self.assertIn(S.CSS_FLASH, t)                                   # gabarit fourni aux agents = CSS posée par le script
        t2, _ = S.reparer(t, True)
        D, M = S.analyser(t2, "g.html", {"flash": True})
        self.assertEqual([d["code"] for d in D if d["severite"] in ("GRAVE", "CRITIQUE")], [])
        self.assertEqual(M["flash"]["syndromes_tableau"], 1); self.assertGreaterEqual(M["flash"]["ilots"], 10)
        self.assertNotRegex(t2, r"\stitle\s*=|<script")
        sys.path.insert(0, str(R / "harnais")); import controle_lot as CL
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "LOT_999_Phase_B_V0_G.1.html"; f.write_text(t2, encoding="utf-8")
            self.assertEqual(CL.analyse_fichier(f)["critiques"], [])

    def test_compatibilite_sans_flash(self):
        t, _ = S.reparer(gonfler(gabarit(), 300 * S.KO))
        self.assertFalse({d["code"][0] for d in S.analyser(t, "g.html")[0]} & {"V", "I", "W", "N"})

    def test_bande_de_volume(self):
        t, _ = S.reparer(gabarit(), True)
        self.assertIn("V1", flash_codes(gonfler(t, 281 * S.KO), "GRAVE"))              # > 280 Ko : bloquant
        c = flash_codes(gonfler(t, 210 * S.KO)); self.assertIn("V2", c); self.assertNotIn("V1", c)
        self.assertNotIn("V2", flash_codes(gonfler(t, 210 * S.KO), "GRAVE"))           # > 200 Ko : avertissement seulement
        self.assertFalse(flash_codes(gonfler(t, 150 * S.KO)) & {"V1", "V2", "V3"})
        self.assertIn("V3", flash_codes(t, "MOYEN"))

    def test_ilots(self):
        t, _ = S.reparer(gabarit(), True)
        self.assertIn("I1", flash_codes(re.sub(r'class="ilot"', 'class="x"', t), "GRAVE"))
        fus = t.replace('</section>\n\n<section class="ilot" data-ilot="5-6">', "\n", 1).replace("</section>\n\n<details", "</section>\n<details", 1)
        self.assertIn("I3", flash_codes(fus, "MOYEN")); self.assertNotIn("I3", flash_codes(fus, "GRAVE"))
        self.assertIn("I4", flash_codes(t.replace('<details class="ilot" data-ilot="8">', '<details class="ilot" data-ilot="8" open>'), "MOYEN"))
        self.assertIn("I6", flash_codes(t.replace('<section class="ilot" data-ilot="1-4">', '<section class="ilot" data-ilot="1-4" style="max-width:600px">')))
        self.assertIn("I5", flash_codes(re.sub(r'(?s)<style id="brain-flash">.*?</style>', "", t)))
        self.assertIn("I2", flash_codes(t.replace('<section class="ilot" data-ilot="1-4">', '<section class="ilot" data-ilot="1-4"></section>', 1), "GRAVE"))

    def test_fenetres(self):
        t, _ = S.reparer(gabarit(), True)
        sans_tab = re.sub(r'(?s)<div style="overflow-x:auto"><table>.*?</table></div>', "<p>Le syndrome associe des symptômes et des signes.</p>", t)
        self.assertIn("W5", flash_codes(sans_tab, "GRAVE"))
        a, b = t.index('id="lecon-p6"'), t.index('<details class="ilot" data-ilot="7">')
        p6 = re.sub(r'(?s)<span class="sc dx">.*?</span></span>', "signe", t[a:b])
        self.assertIn("W4", flash_codes(t[:a] + p6 + t[b:], "GRAVE"))
        trois = t.replace("<tr><th>Symptômes fonctionnels</th><th>Signes physiques</th></tr>", "<tr><th>Symptômes fonctionnels</th><th>Signes physiques</th><th>Examen</th></tr>")
        self.assertIn("W6", flash_codes(trois, "MOYEN"))
        long_ = t.replace("</strong></h3>\n<p>[Phrase complète : la prévalence", '</strong></h3>\n<p><span class="tm" tabindex="0">terme<span class="df">'
                          + "le détail est trop long pour un survol " * 8 + "</span></span> [Phrase complète : la prévalence", 1)
        self.assertIn("W8", flash_codes(long_, "MOYEN"))
        self.assertIn('<label class="fx-x"', t[t.index('class="algo-det"'):])                     # détails d'algorithme : fenêtre modale fermable

    def test_notions_voisines_dans_le_corps(self):
        t, _ = S.reparer(gabarit(), True)
        bloc = t.replace("<p>[Phrase complète : les critères", "<p><b>Notions voisines</b></p><ul><li>Entité A.</li><li>Entité B.</li></ul>\n<p>[Phrase complète : les critères", 1)
        self.assertIn("N1", flash_codes(bloc, "GRAVE"))
        self.assertNotIn("N1", flash_codes(t))                                                    # le différentiel en fenêtre (point 4) est admis

    def test_reparation_respecte_les_ilots(self):
        t, _ = S.reparer(gabarit(), True)
        cas = t.replace("<p>[Phrase complète : l'examen de référence confirme …]</p>", "<div><p>[Phrase complète : l'examen de référence confirme …]</p>", 1)
        self.assertTrue(any(n == 9 for *_, n in S.desequilibres(cas)))                           # localisé au point 9, pas aux points des îlots
        self.assertFalse(any(n in (4, 6) for *_, n in S.desequilibres(cas)))
        t2, J = S.equilibrer(cas)
        self.assertEqual(S.desequilibres(t2), []); self.assertTrue(J)
        self.assertEqual(len(S.ilots(t2)), len(S.ilots(t))); self.assertTrue(all(b for _, b, _, _ in S.ilots(t2)))
        self.assertIn('</div></details>\n\n<details class="ilot" data-ilot="10">', t2)

    def test_bus_fenetres_modales(self):
        import bus
        h = '<p>Visible.</p><div class="fxw"><div class="fx"><div class="fx-b"><p>Caché 42 %.</p></div></div></div><p>Fin.</p>'
        self.assertEqual(bus.texte_visible(h), "Visible. Fin."); self.assertTrue(bus.zones_fenetres(h))


class FlashCircuit(unittest.TestCase):
    cv = staticmethod(lambda *a: subprocess.run([sys.executable, str(R / "harnais/brain/circuit_vial.py"), *a], cwd=R, capture_output=True, text=True, timeout=900))

    def test_mode_memorise_porte_et_registre(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "LOT_999_Phase_B_V0_G.1.html"; f.write_text(gabarit(), encoding="utf-8")
            m = self.cv("memoire", "duo", str(f), "--flash"); self.assertIn("COURS FLASH", m.stdout)
            self.assertIn("gabarit_flash.html", m.stdout)
            g = S.reparer(gabarit(), True)[0]
            f.write_text(re.sub(r'(?s)<div style="overflow-x:auto"><table>.*?</table></div>', "<p>Le syndrome associe des symptômes et des signes.</p>", g), encoding="utf-8")
            p = self.cv("point", str(f), "7")                                                       # mode repris de l'instantané, sans drapeau
            self.assertNotEqual(p.returncode, 0); self.assertIn("W5", p.stdout)
            f.write_text(g.replace('data-ilot="8">', 'data-ilot="8" open>'), encoding="utf-8")
            p = self.cv("point", str(f), "8"); self.assertIn("AVERTISSEMENTS FLASH", p.stdout); self.assertIn("I4", p.stdout)
            f.write_text(gonfler(g, 290 * S.KO), encoding="utf-8")
            fin_ = self.cv("fin", str(f), "--role", "duo")
            self.assertNotEqual(fin_.returncode, 0); self.assertIn("GRAVE Flash", fin_.stdout); self.assertIn("V1", fin_.stdout)
            self.cv("registre", str(f), "--json", f"{d}/r.json", "--md", f"{d}/r.md")
            reg = json.loads(Path(f"{d}/r.json").read_text()); self.assertTrue(reg["flash"])
            self.assertTrue(any(r["code"] == "V1" and r["severite"] == "GRAVE" and r["ligne"] == 1 for r in reg["fautes"]))
            self.assertIn("| V1 |", Path(f"{d}/r.md").read_text())

    def test_lanceur_flash_par_defaut(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "LOT_999_Phase_B_V0_G.1.html"; f.write_text(gabarit(), encoding="utf-8")
            L = lambda *a: subprocess.run([sys.executable, str(R / "harnais/brain/lancer_circuit.py"), str(f), "--dry-run", "--journal", d, *a], cwd=R, capture_output=True, text=True, timeout=120)
            L(); b = json.loads((Path(d) / "bilan.json").read_text())
            pr = b[0]["etapes"]["duo"]["appels"][0]["cmd"][2]; self.assertIn("--flash", pr); self.assertIn("gabarit_flash.html", pr)
            self.assertIn("--flash", b[0]["etapes"]["professeur"]["appels"][0]["cmd"][2])
            L("--classique"); b = json.loads((Path(d) / "bilan.json").read_text())
            self.assertNotIn("--flash", b[0]["etapes"]["duo"]["appels"][0]["cmd"][2])


if __name__ == "__main__":
    unittest.main(verbosity=1)
