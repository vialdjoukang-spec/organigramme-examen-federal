#!/usr/bin/env python3
"""Robustesse des 160 scriptones contre tout bug d'entrée et de concurrence (unittest, stdlib) :
  python3 harnais/brain/scriptones/test_robustesse.py [-v]      (BRAIN_FUZZ_COMPLET=1 : 60 troncatures par scriptone au lieu de 6)
Entrées malformées (vide, binaire, balises non fermées, imbrication profonde, NUL), fichiers tronqués à des positions aléatoires,
encodages (UTF-8 avec BOM, UTF-16, cp1252, mojibake, CRLF), fichier géant ; panne interne annoncée (Z0) sans casser le contrat ;
concurrence : 16 processus sur un même journal (flock), verrou exclusif d'écriture, 16 cours en parallèle dans l'orchestre."""
import json, os, random, re, shutil, subprocess, sys, tempfile, time, unittest
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
D = Path(__file__).resolve().parent
sys.path.insert(0, str(D)); sys.path.insert(0, str(D.parent))
import bus, reseau, mutation

PY = [e["id"] for e in reseau.registre()["scriptones"] if e["langage"] == "python"]
K = 60 if os.environ.get("BRAIN_FUZZ_COMPLET") else 6
LOURDS = {"s12_ordonnanceur", "s13_disjoncteur", "s18_vote"} | {f"b{n:02d}_M" for n in range(1, 15)}


def entrees(g, r, k):
    out = ["", " ", "<html>", "<h3>2. Épidémiologie</h3><p>", "\x00\x01\x02", bytes(r.getrandbits(8) for _ in range(3000)).decode("latin-1"),
           "<div>" * 1500 + "x" + "</div>" * 10, g.replace("\n", "\r\n"), "﻿" + g, g.encode("utf-8").decode("latin-1"),
           re.sub(r"</(?:p|li|table|details|div)>", "", g), g.replace("<", "&lt;", 50)]
    out += [g[:r.randrange(len(g))] for _ in range(k)]
    out += [g[:a] + g[a + r.randint(1, 400):] for a in (r.randrange(len(g)) for _ in range(k // 2 + 1))]
    return out


class Fuzz(unittest.TestCase):
    def test_aucune_entree_ne_casse_un_scriptone(self):
        pannes = []; n = 0
        for i in PY:
            m = reseau.module(i); g, _ = mutation.dore(m); r = random.Random(i)
            for x in entrees(g, r, 2 if i in LOURDS else K):
                s = bus.executer(m, "", html=x, ecrire=False); n += 1
                self.assertEqual(bus.valider(s), [], i)
                if s.get("panne"): pannes.append(f"{i} : {s['panne']['type']} {s['panne']['message'][:80]}")
        self.assertEqual(pannes, [], f"{len(pannes)} pannes sur {n} entrées : {pannes[:5]}")

    def test_geant(self):
        g = mutation.DORE.read_text(encoding="utf-8"); x = g.replace("</main>", "<p>Le patient reste stable.</p>" * 40000 + "</main>")
        for i in ("s11_collecteur", "a11_H", "b11_X", "s3_concision", "s16_economie"):
            t0 = time.time(); s = bus.executer(reseau.module(i), "", html=x, ecrire=False); self.assertEqual(bus.valider(s), []); self.assertLess(time.time() - t0, 60, i)

    def test_panne_annoncee_jamais_avalee(self):
        class Faux:
            ID, REGION, VERSION, __file__ = "s3_concision", "AUL", "0", str(D / "s3_concision.py")
            @staticmethod
            def analyser(t, nom, opt=None): raise ZeroDivisionError("bug simulé")
        s = bus.executer(Faux, "", html="<p>x</p>", ecrire=False)
        self.assertEqual(bus.valider(s), []); self.assertEqual(s["panne"]["type"], "ZeroDivisionError"); self.assertEqual([d["code"] for d in s["doleances"]], ["Z0"])


class Encodages(unittest.TestCase):
    def setUp(self): self.d = Path(tempfile.mkdtemp())
    def tearDown(self): shutil.rmtree(self.d, ignore_errors=True)

    def test_lecture_tolerante(self):
        g = mutation.DORE.read_text(encoding="utf-8")
        for enc, b in (("utf-8-sig", g.encode("utf-8-sig")), ("utf-16", g.encode("utf-16")), ("cp1252", g.encode("cp1252", errors="replace"))):
            f = self.d / f"c_{enc}.html"; f.write_bytes(b); t, e = bus.lire(f)
            self.assertIn("Hypothermie accidentelle", t, enc); self.assertFalse(t.startswith("﻿"), enc)
            r = subprocess.run([sys.executable, str(D / "alpha/a02_R.py"), str(f), "--json"], capture_output=True, text=True, timeout=60)
            self.assertIn(r.returncode, (0, 1), r.stdout[-200:]); self.assertEqual(json.loads(r.stdout)["encodage"], e)

    def test_collecteur_voit_les_degats(self):
        g = mutation.DORE.read_text(encoding="utf-8"); C = reseau.module("s11_collecteur")
        codes = lambda x: {d["code"] for d in C.analyser(x, "t")[0]}
        self.assertIn("K1", codes(g[:len(g) // 2])); self.assertIn("K3", codes(g.encode("utf-8").decode("latin-1"))); self.assertIn("K5", codes(g.replace("</p>", "\x00</p>", 1)))
        self.assertIn("K4", codes("<html><body><p>vide</p></body></html>"))

    def test_entree_contrat_malformee(self):
        for c in ("{", "[]", '{"options": 3}', '{"fichier": "/nexiste/pas.html"}'):
            r = subprocess.run([sys.executable, str(D / "s3_concision.py"), "--contrat", "-"], input=c, capture_output=True, text=True, timeout=60)
            self.assertEqual(r.returncode, 2, (c, r.stdout)); self.assertIn("ERREUR D'ENTRÉE", r.stdout)


def _ecrire(args):
    chemin, k, n = args
    for s in range(n): bus.evenement(dict(run=f"p{k}", seq=s, type=bus.TYPES[s % 6], de=f"α{k % 14 + 1}", vers="BUS", msg="x" * (s % 50)), Path(chemin))
    return k


class Concurrence(unittest.TestCase):
    def setUp(self): self.d = Path(tempfile.mkdtemp())
    def tearDown(self): shutil.rmtree(self.d, ignore_errors=True)

    def test_journal_16_processus(self):
        j = self.d / "ev.jsonl"
        with ProcessPoolExecutor(16) as ex: list(ex.map(_ecrire, [(str(j), k, 150) for k in range(16)]))
        t = j.read_text(encoding="utf-8"); s = reseau.module("s14_journal").analyser(t, "ev")
        self.assertEqual(len(t.splitlines()), 16 * 150); self.assertEqual(s[0], [], s[0][:3])

    def test_verrou_exclusif(self):
        f = self.d / "c.html"; f.write_text(reseau.module("a02_R").MUTANTS[0][1](mutation.DORE.read_text(encoding="utf-8"), random.Random(1)), encoding="utf-8")
        h = bus.sha(f.read_bytes())
        with bus.verrou(f):
            r = subprocess.run([sys.executable, str(D / "alpha/a02_R.py"), str(f), "--appliquer"], capture_output=True, text=True, timeout=60)
            self.assertEqual(r.returncode, 4, r.stdout); self.assertEqual(bus.sha(f.read_bytes()), h)
        r = subprocess.run([sys.executable, str(D / "alpha/a02_R.py"), str(f), "--appliquer", "--json"], capture_output=True, text=True, timeout=60)
        self.assertTrue(json.loads(r.stdout)["modifie"]); self.assertFalse(Path(str(f) + ".brainlock").exists())

    def test_16_cours_en_parallele(self):
        import orchestre
        g = mutation.DORE.read_text(encoding="utf-8"); fs = []
        for k in range(16):
            f = self.d / f"LOT_000_Phase_B_V0_DX.{k + 1}.html"; f.write_text(g, encoding="utf-8"); fs.append(f)
        j = self.d / "ev.jsonl"; R = orchestre.lot(fs, 16, j)
        self.assertEqual(len(R), 16); self.assertTrue(all(r["verdict"] == "sortie : audité" for r in R), [r["verdict"] for r in R])
        self.assertEqual(reseau.module("s14_journal").analyser(j.read_text(encoding="utf-8"), "ev")[0], [])
        self.assertTrue(all(bus.sha(f.read_bytes()) == bus.sha(g.encode()) for f in fs))          # dry-run : rien écrit


if __name__ == "__main__":
    unittest.main()
