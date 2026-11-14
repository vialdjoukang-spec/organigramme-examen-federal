#!/usr/bin/env python3
"""Essai visuel du harnais : contours, définition, flèche fine.
Crée une paire synthétique (aucun patient), valide, construit, capture, puis efface la paire.
Les captures restent dans progression/essai-harnais/ et shots/.
"""
import json, os, shutil, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate as V
from PIL import Image, ImageDraw

ROOT = V.ROOT
SCRIPTS = os.path.dirname(os.path.abspath(__file__))
ESSAI = os.path.join(ROOT, "images", "_essai")
MAN = os.path.join(ROOT, "manifest", "TEST-harnais.json")
SHOTS = os.path.join(ROOT, "progression", "essai-harnais")

CONTOUR = [
    [0.62, 0.08], [0.74, 0.05], [0.86, 0.10], [0.91, 0.20],
    [0.88, 0.32], [0.76, 0.39], [0.64, 0.34], [0.60, 0.20], [0.62, 0.08],
]
RECT = [[0.20, 0.20], [0.55, 0.20], [0.55, 0.48], [0.20, 0.48], [0.20, 0.20]]

def fail(msg):
    print("ÉCHEC", msg)
    sys.exit(1)

def assert_rejects(arrow_patch, dx, needle):
    m = {
        "id": "IMG-134", "dx": dx["dx"], "cliche": dx["cliche"], "statut": "complet",
        "normal": {"file": "x", "license": "CC0 1.0", "author": "a", "source_url": "https://example.org/n",
                   "modality": "RX", "sequence": "thorax", "plane": "face"},
        "patho": {"file": "x", "license": "CC0 1.0", "author": "a", "source_url": "https://example.org/p",
                  "modality": "RX", "sequence": "thorax", "plane": "face", "caption_source": "essai",
                  "arrows": [dict({
                      "tip": [0.63, 0.24], "from": [0.48, 0.16],
                      "label": "Ligne pleurale viscérale", "role": "principale",
                      "evidence": "essai", "confidence": "moyenne",
                      "contour": CONTOUR,
                      "definition": "Air dans l'espace pleural.",
                      "definition_source": "Fleischner Society, Radiology 2008;246:697-722",
                  }, **arrow_patch)]},
    }
    errs, warns = [], []
    # Fichiers absents : on ne juge ici que le message demandé.
    V.check(m, dx, errs, warns)
    if not any(needle in e for e in errs):
        fail(f"contrôle muet pour {needle!r} : {errs}")

def draw_pair():
    os.makedirs(ESSAI, exist_ok=True)
    W, H = 800, 640
    def base():
        im = Image.new("RGB", (W, H), (16, 20, 26))
        d = ImageDraw.Draw(im)
        d.rectangle([360, 70, 450, 580], fill=(62, 66, 74))
        d.ellipse([70, 60, 370, 540], fill=(92, 100, 110))
        d.ellipse([440, 60, 750, 540], fill=(92, 100, 110))
        for y in range(110, 500, 52):
            d.arc([60, y, 380, y + 70], 200, 340, fill=(168, 174, 182), width=3)
            d.arc([430, y, 760, y + 70], 200, 340, fill=(168, 174, 182), width=3)
        return im
    normal, patho = base(), base()
    d = ImageDraw.Draw(patho)
    poly = [(int(p[0] * W), int(p[1] * H)) for p in CONTOUR[:-1]]
    d.polygon(poly, fill=(6, 6, 8))
    d.line([poly[0], poly[3]], fill=(245, 245, 248), width=3)
    normal.save(os.path.join(ESSAI, "normal.jpg"), "JPEG", quality=85)
    patho.save(os.path.join(ESSAI, "patho.jpg"), "JPEG", quality=85)

def manifest():
    side = lambda f: {
        "file": f"images/_essai/{f}",
        "source_url": "https://github.com/vialdjoukang-spec/organigramme-examen-federal",
        "license": "CC0 1.0",
        "license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
        "author": "Essai de harnais, image synthétique, aucun patient",
        "sex": "M",
        "modality": "RX", "sequence": "thorax", "plane": "face", "region": "thorax",
        "note": "Image dessinée par script pour l'essai du rendu. Aucun patient.",
    }
    n, p = side("normal.jpg"), side("patho.jpg")
    p["caption_source"] = "Image synthétique : hyperclarté apicale sans vaisseau, limitée par une ligne pleurale blanche."
    p["arrows"] = [{
        "tip": [0.625, 0.24], "from": [0.46, 0.14],
        "label": "Ligne pleurale viscérale",
        "role": "principale",
        "evidence": "Hyperclarté périphérique sans vaisseau, bordée par la ligne blanche tracée sur l'image d'essai.",
        "confidence": "moyenne",
        "contour": CONTOUR,
        "definition": "Présence d'air dans l'espace pleural, vue comme une hyperclarté avasculaire limitée par la ligne pleurale viscérale.",
        "definition_source": "Fleischner Society, Glossary of Terms for Thoracic Imaging, Radiology 2008;246:697-722 (Hansell et al.)",
    }]
    return {
        "id": "TEST-harnais", "test_of": "IMG-134",
        "dx": "Pneumothorax et pneumothorax compressif",
        "cliche": "RX — thorax", "statut": "complet",
        "normal": n, "patho": p,
        "pair_match": "Même modalité, même plan, même cadre. Écart : images synthétiques d'essai, pas des clichés de patients.",
        "a_verifier": ["Image synthétique : ne pas la prendre pour un cas réel."],
        "queries": ["essai harnais, aucune recherche d'image"],
    }

def run(args):
    p = subprocess.run([sys.executable, *args], cwd=ROOT, text=True, capture_output=True)
    print(p.stdout)
    if p.returncode:
        print(p.stderr)
        fail(" ".join(args) + f" → code {p.returncode}")
    return p.stdout

def main():
    dx = next(d for d in json.load(open(os.path.join(ROOT, "diagnostics.json"))) if d["id"] == "IMG-134")
    assert_rejects({"contour": [[0.1, 0.1], [1.4, 0.2], [0.2, 0.3], [0.1, 0.1]]}, dx, "hors de l'image")
    assert_rejects({"contour": [[0.1, 0.1], [0.4, 0.1], [0.4, 0.4], [0.2, 0.3]]}, dx, "non fermé")
    assert_rejects({"contour": [[0.1, 0.1], [0.4, 0.2], [0.1, 0.1]]}, dx, "3 sommets")
    assert_rejects({"definition": ""}, dx, "définition radiologique absente")
    assert_rejects({"definition_source": "À vérifier"}, dx, "définition non sourcée")
    assert_rejects({"contour": RECT}, dx, "rectangulaire")
    msex = {
        "id": "IMG-134", "dx": dx["dx"], "cliche": dx["cliche"], "statut": "complet",
        "normal": {"file": "x", "license": "CC0 1.0", "author": "a", "source_url": "https://example.org/n",
                   "modality": "RX", "sequence": "thorax", "plane": "face", "sex": "M"},
        "patho": {"file": "x", "license": "CC0 1.0", "author": "a", "source_url": "https://example.org/p",
                  "modality": "RX", "sequence": "thorax", "plane": "face", "caption_source": "essai", "sex": "F",
                  "arrows": [{"tip": [0.63, 0.24], "from": [0.48, 0.16], "label": "Ligne pleurale viscérale",
                              "role": "principale", "evidence": "essai", "confidence": "moyenne", "contour": CONTOUR,
                              "definition": "Air dans l'espace pleural.",
                              "definition_source": "Fleischner Society, Radiology 2008;246:697-722"}]},
    }
    errs, warns = [], []
    V.check(msex, dx, errs, warns)
    if not any("discordant" in e for e in errs):
        fail(f"sexe discordant non bloqué : {errs}")
    msex["normal"].pop("sex"); msex["patho"]["sex"] = "À vérifier"; msex["statut"] = "complet"
    errs = []
    V.check(msex, dx, errs, warns)
    if not any("sexe non établi" in e for e in errs):
        fail(f"sexe non établi non bloqué : {errs}")
    msex.pop("normal")
    errs = []
    V.check(msex, dx, errs, warns)
    if not any("sans image normale" in e for e in errs):
        fail(f"normale absente non bloquée : {errs}")
    print("Contrôles négatifs : OK")
    try:
        draw_pair()
        json.dump(manifest(), open(MAN, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        run([os.path.join(SCRIPTS, "validate.py"), "--include-test", "--only", "TEST-harnais"])
        html = "/tmp/radio-essai-harnais.html"
        run([os.path.join(SCRIPTS, "build_app.py"), "--include-test", "--out", html])
        run([os.path.join(SCRIPTS, "screenshot.py"), "--html", html, "--ids", "IMG-134", "--tag", "essai"])
        os.makedirs(SHOTS, exist_ok=True)
        src = os.path.join(ROOT, "shots")
        for name in os.listdir(src):
            if name.startswith("essai_"):
                shutil.copy2(os.path.join(src, name), os.path.join(SHOTS, name))
        print("Captures copiées dans", SHOTS)
    finally:
        if os.path.isfile(MAN):
            os.remove(MAN)
        shutil.rmtree(ESSAI, ignore_errors=True)
        print("Paire d'essai effacée.")

if __name__ == "__main__":
    main()
