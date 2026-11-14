"""Tests unitaires de la légion. Aucun réseau."""
import os, shutil, sys, tempfile, unittest

ICI = os.path.dirname(os.path.abspath(__file__))
LEGION = os.path.dirname(ICI)
SCRIPTS = os.path.dirname(LEGION)
sys.path.insert(0, LEGION)
sys.path.insert(0, SCRIPTS)

import attestations as A
import anonymiser
import europepmc
import injecter
import licences as L
import recepteur
import socle


class Licences(unittest.TestCase):
    def test_liste(self):
        for lic in ("CC0", "CC0 1.0", "Public domain", "PD", "CC BY", "CC BY 4.0", "CC BY-SA 4.0", "cc by"):
            self.assertTrue(L.licence_ok(lic), lic)
        for lic in ("", "CC BY-NC", "CC BY-NC 4.0", "CC BY-ND", "CC BY-NC-SA 4.0", "all rights reserved"):
            self.assertFalse(L.licence_ok(lic), lic)

    def test_auteur_et_url(self):
        self.assertEqual(L.raison_licence("CC BY 4.0", "Auteur", "https://exemple.org/a"), "")
        self.assertIn("auteur", L.raison_licence("CC BY", "", "https://exemple.org/a"))
        self.assertIn("URL", L.raison_licence("CC0", "Quelqu'un", ""))


class Attestations(unittest.TestCase):
    def test_age_sexe_adulte(self):
        t = "Axial CT in a 54-year-old man."
        self.assertEqual(A.age_ans(t), 54)
        self.assertEqual(A.sexe(t), "M")
        self.assertEqual(A.adulte_de(54), "oui")
        self.assertEqual(A.sexe("Man erkennt eine Fraktur"), "")

    def test_priorite_et_tranche(self):
        adulte = {"age_ans": 40, "sex": "F"}
        mineur = {"age_ans": 8, "sex": "F"}
        muet = {"age_ans": None, "sex": ""}
        self.assertLess(A.priorite(adulte), A.priorite(mineur))
        self.assertLess(A.priorite(mineur), A.priorite(muet))
        self.assertTrue(A.ages_comparables(30, 44, {"age": {"ecart_max_ans": 15}}))
        self.assertFalse(A.ages_comparables(17, 19, {"age": {"ecart_max_ans": 15}}))
        self.assertFalse(A.ages_comparables(30, 50, {"age": {"ecart_max_ans": 15}}))

    def test_redaction(self):
        t = A.rediger("Patient 884422, né le 03.04.1979, homme de 45 ans, a@b.c")
        self.assertNotIn("884422", t)
        self.assertNotIn("03.04.1979", t)
        self.assertNotIn("a@b.c", t)
        self.assertIn("45", t)


class Anonymisation(unittest.TestCase):
    def test_masque_mots_et_pixels(self):
        mots = ["PATIENT", "884422", "03.04.1979", "45", "ans", "F"]
        idx = anonymiser.mots_a_masquer(mots)
        self.assertIn(0, idx)
        self.assertIn(1, idx)
        self.assertNotIn(3, idx)
        self.assertNotIn(5, idx)
        from PIL import Image
        im = Image.new("RGB", (40, 20), (255, 255, 255))
        anonymiser.masquer_image(im, [{"l": 0, "t": 0, "w": 10, "h": 10}])
        self.assertEqual(im.getpixel((1, 1)), (0, 0, 0))
        self.assertEqual(im.getpixel((30, 10)), (255, 255, 255))


class EuropePMC(unittest.TestCase):
    def test_nc_ne_telecharge_pas(self):
        appels = {"xml": 0, "zip": 0}

        class Faux:
            def search(self, requete, n):
                return [
                    {"pmcid": "PMC1", "license": "cc by-nc", "authorString": "A", "title": "t"},
                    {"pmcid": "PMC2", "license": "cc by", "authorString": "B", "title": "u"},
                ]

            def xml(self, pmcid):
                appels["xml"] += 1
                self.vu = pmcid
                return '<article><p>https://creativecommons.org/licenses/by-nc/4.0/</p></article>'

            def zip(self, pmcid):
                appels["zip"] += 1
                return b""

        faux = Faux()
        rendus = europepmc.articles("pneumothorax", n=2, client=faux)
        self.assertEqual(appels["zip"], 0)
        self.assertEqual(appels["xml"], 1)
        self.assertEqual(faux.vu, "PMC2")
        self.assertFalse(rendus[0]["accepte_licence"])
        self.assertFalse(rendus[1]["accepte_licence"])

    def test_figure_sans_archive_tant_que_non_demandee(self):
        xml = """<article xmlns:xlink="http://www.w3.org/1999/xlink">
          <license><ext-link xlink:href="https://creativecommons.org/licenses/by/4.0/">by</ext-link></license>
          <fig><caption><p>CT of a 54-year-old man.</p></caption>
          <graphic content-type="image" xlink:href="g1.webp"/></fig></article>"""

        class Faux:
            def search(self, requete, n):
                return [{"pmcid": "PMC9", "license": "cc by", "authorString": "B", "title": "u"}]

            def xml(self, pmcid):
                return xml

            def zip(self, pmcid):
                raise AssertionError("archive trop tôt")

        rendus = europepmc.articles("ct", client=Faux())
        self.assertTrue(rendus[0]["accepte_licence"])
        self.assertEqual(rendus[0]["figures"][0]["href"], "g1.webp")
        self.assertEqual(A.age_ans(rendus[0]["figures"][0]["caption"]), 54)


class Recepteur(unittest.TestCase):
    def test_consignes(self):
        chemin = os.path.join(os.path.dirname(socle.ROOT), "CONSIGNES_VIAL.md")
        with open(chemin, encoding="utf-8") as f:
            cfg, file = recepteur.analyser(f.read())
        self.assertEqual(cfg["cartes"]["fond"], "#F3FAFD")
        self.assertEqual(cfg["cartes"]["bordure"], "#87CEEB")
        self.assertEqual(cfg["cartes"]["texte"], "#0B2540")
        self.assertEqual(cfg["police"], "Atkinson Hyperlegible")
        self.assertEqual(cfg["disposition"]["normale"], "gauche")
        self.assertEqual(cfg["fleches"], "cachees_derriere_bouton")
        self.assertEqual(cfg["survol"], "lie")
        self.assertEqual(cfg["couleur_structure"], "identique_des_deux_cotes")
        self.assertEqual(cfg["aspect_sans_source"], "Interprétation de l'image (non sourcée)")
        self.assertEqual(cfg["age"]["ecart_max_ans"], 15)
        self.assertEqual(cfg["sexe"]["concordance_regions"][0], "bassin")
        self.assertTrue(file)
        self.assertTrue(all(x["marque"] == recepteur.MARQUE for x in file))
        self.assertTrue(any("contour" in x["texte"] for x in file))


class Injecteur(unittest.TestCase):
    def _image(self, path, secret=True):
        from PIL import Image, ImageDraw, ImageFont
        im = Image.new("RGB", (640, 200), (240, 240, 240))
        d = ImageDraw.Draw(im)
        police = os.path.join(socle.ROOT, "fonts", "AtkinsonHyperlegible-Regular.ttf")
        font = ImageFont.truetype(police, 28)
        if secret:
            d.text((16, 20), "45 ans F", fill=(0, 0, 0), font=font)
            d.text((16, 80), "PATIENT 884422 03.04.1979", fill=(0, 0, 0), font=font)
        else:
            d.rectangle([10, 10, 40, 40], fill=(0, 0, 0))
        im.save(path, "JPEG", quality=90)

    def test_refus_et_fantome(self):
        racine = tempfile.mkdtemp()
        try:
            os.makedirs(os.path.join(racine, "entrant"))
            os.makedirs(os.path.join(racine, "manifest"))
            socle.ecrire_json(os.path.join(racine, "diagnostics.json"), [
                {"id": "IMG-307", "dx": "Pied", "cliche": "IRM — STIR", "region": "Membre inférieur"}
            ])
            mauvais = os.path.join(racine, "entrant", "mauvais.jpg")
            self._image(mauvais, secret=False)
            socle.ecrire_json(os.path.splitext(mauvais)[0] + ".json", {
                "id": "IMG-307", "cote": "pathologique", "source": "https://exemple.org/nc",
                "licence": "CC BY-NC 4.0", "auteur": "Quelqu'un", "age": 40, "sexe": "F",
            })
            bon = os.path.join(racine, "entrant", "fantome.jpg")
            self._image(bon, secret=True)
            socle.ecrire_json(os.path.splitext(bon)[0] + ".json", {
                "id": "TEST-ENTRANT", "cote": "pathologique", "source": "https://exemple.org/fantome",
                "licence": "CC0 1.0",
                "license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
                "auteur": "Fantôme de harnais, aucun patient",
                "age": 45, "sexe": "F", "fantome": True, "test_of": "IMG-307",
                "graine": [0.5, 0.5],
                "note": "Image synthétique. Aucun patient.",
            })
            res = injecter.traiter(os.path.join(racine, "entrant"), racine=racine)
            par = {r["fichier"]: r for r in res["resultats"]}
            self.assertFalse(par["mauvais.jpg"]["ok"])
            self.assertTrue(os.path.isfile(os.path.splitext(mauvais)[0] + ".refus.md"))
            self.assertFalse(os.path.isfile(os.path.join(racine, "manifest", "IMG-307.json")))
            self.assertTrue(par["fantome.jpg"]["ok"])
            m = socle.lire_json(os.path.join(racine, "manifest", "TEST-ENTRANT.json"))
            self.assertEqual(m["statut"], "partiel")
            self.assertNotEqual(m["statut"], "complet")
            self.assertEqual(m["patho"]["sex"], "F")
            self.assertEqual(m["patho"]["age_ans"], 45)
            if anonymiser.tesseract_disponible():
                import pytesseract
                from PIL import Image
                texte = pytesseract.image_to_string(Image.open(bon), lang="eng")
                self.assertNotIn("884422", texte)
        finally:
            shutil.rmtree(racine)


class Inventaire(unittest.TestCase):
    def test_dix(self):
        ids = socle.choisir(10)
        self.assertGreaterEqual(len(ids), 10)
        for mid in ids:
            m, _ = socle.manifeste(mid)
            self.assertEqual(m["statut"], "introuvable")


if __name__ == "__main__":
    unittest.main()
