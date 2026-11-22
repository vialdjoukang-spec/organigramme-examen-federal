"""Consignes récurrentes → config/interface.json. Le reste va dans la file."""
import os, re, subprocess, sys
import socle

MARQUE = "à interpréter par un agent"
_HEX = r"(#[0-9A-Fa-f]{6})"


def _puce(ligne):
    s = ligne.strip()
    if s.startswith("- "):
        return s[2:].strip()
    return ""


def analyser(texte):
    cfg = {"source": "imagerie_GROK/CONSIGNES_VIAL.md"}
    file = []
    for ligne in (texte or "").splitlines():
        corps = _puce(ligne)
        if not corps:
            continue
        hit = False
        m = re.search(rf"fond\s+{_HEX}.*bordure\s+{_HEX}.*texte\s+{_HEX}", corps, re.I)
        if m:
            cfg["cartes"] = {"fond": m.group(1).upper(), "bordure": m.group(2).upper(),
                             "texte": m.group(3).upper()}
            hit = True
        if re.search(r"Atkinson Hyperlegible", corps):
            cfg["police"] = "Atkinson Hyperlegible"
            hit = True
        elif re.search(r"^Police\s*:", corps, re.I):
            cfg["police"] = corps.split(":", 1)[1].strip()
            hit = True
        if re.search(r"gauche", corps, re.I) and re.search(r"droite", corps, re.I) and re.search(r"normal", corps, re.I):
            cfg["disposition"] = {"normale": "gauche", "pathologique": "droite"}
            hit = True
        if re.search(r"fl[eè]ches?", corps, re.I) and re.search(r"cach|bouton", corps, re.I):
            cfg["fleches"] = "cachees_derriere_bouton"
            hit = True
        if re.search(r"survol", corps, re.I) and re.search(r"li[ée]", corps, re.I):
            cfg["survol"] = "lie"
            hit = True
        if re.search(r"m[eê]me couleur", corps, re.I) and re.search(r"structure", corps, re.I):
            cfg["couleur_structure"] = "identique_des_deux_cotes"
            hit = True
        if re.search(r"palette", corps, re.I):
            paires = re.findall(rf"([A-Za-z0-9_-]+)\s+{_HEX}", corps)
            if paires:
                cfg["palette"] = {n: h.upper() for n, h in paires}
                hit = True
        if "Interprétation de l'image (non sourcée)" in corps:
            cfg["aspect_sans_source"] = "Interprétation de l'image (non sourcée)"
            hit = True
        if re.search(r"adultes?", corps, re.I) and re.search(r"priorit", corps, re.I):
            cfg.setdefault("age", {})["priorite"] = "adulte"
            hit = True
        m_ecart = re.search(r"(\d+)\s+ans", corps)
        if m_ecart and re.search(r"[eé]cart", corps, re.I):
            cfg.setdefault("age", {})["ecart_max_ans"] = int(m_ecart.group(1))
            hit = True
        if all(mot in corps.lower() for mot in ("bassin", "sein")) and re.search(r"g[eé]nit", corps, re.I):
            cfg["sexe"] = {"concordance_regions": ["bassin", "sein", "organes génitaux"]}
            hit = True
        if not hit:
            file.append({"texte": corps, "marque": MARQUE, "source": "CONSIGNES_VIAL.md"})
    return cfg, file


def appliquer(chemin=None, relancer=True, out=None, only="IMG-001"):
    chemin = chemin or os.path.join(os.path.dirname(socle.ROOT), "CONSIGNES_VIAL.md")
    texte = open(chemin, encoding="utf-8").read()
    cfg, file = analyser(texte)
    socle.ecrire_json(socle.CONFIG, cfg)
    socle.ecrire_json(socle.FILE, {"marque": MARQUE, "items": file})
    socle.journal("consigne", parametres=sorted(k for k in cfg if k != "source"), file=len(file))
    code_b = code_v = 0
    page = ""
    if relancer:
        page = out or os.path.join(socle.DEMO, "Radio_Paires_consigne.html")
        cmd = [sys.executable, os.path.join(socle.SCRIPTS, "build_app.py"),
               "--external", "--only", only, "--out", page]
        code_b = subprocess.run(cmd, cwd=socle.ROOT).returncode
        code_v = subprocess.run(
            [sys.executable, os.path.join(socle.SCRIPTS, "validate.py"), "--quiet"],
            cwd=socle.ROOT).returncode
    return {"config": cfg, "file": file, "page": page, "build": code_b, "validate": code_v}


def main(argv=None):
    import argparse
    p = argparse.ArgumentParser(description="Consignes de Vial → config/interface.json")
    p.add_argument("--consignes", default="")
    p.add_argument("--out", default="")
    p.add_argument("--only", default="IMG-001")
    p.add_argument("--sans-relance", action="store_true")
    a = p.parse_args(argv)
    res = appliquer(a.consignes or None, relancer=not a.sans_relance,
                    out=a.out or None, only=a.only)
    print(f"config {socle.CONFIG}")
    print(f"file {len(res['file'])} → {socle.FILE}")
    if res["page"]:
        print(f"page {res['page']} build={res['build']} validate={res['validate']}")
    return 0 if res["build"] == 0 and res["validate"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
