#!/usr/bin/env python3
"""build_app.py — génère app/Radio_Paires.html (fichier unique hors-ligne).
CLI: python3 scripts/build_app.py [--external] [--include-test] [--out app/Radio_Paires.html]
  défaut       : images embarquées en data URI JPEG (fichier autonome)
  --external   : référence ../images/... (fichier léger, dossier images/ requis à côté)
  --include-test : manifests TEST-*.json appliqués à leur diagnostic (champ test_of), badge TEST
Le statut affiché est le statut VALIDÉ par validate.py (un manifest en erreur n'est jamais « complet »).
Avant d'écrire la page, contraste.py refuse un texte sous 7:1 ou un petit libellé sous 4,5:1.
Les cartes explicatives (survol, définition, légende, indice, Source) sont bleu ciel atténué :
fond #E1F3FA (#87CEEB mêlé à 75 % de blanc), bordure #87CEEB, texte #0B2540, au moins 7:1.
La page est refusée sinon.
"""
import base64, glob, json, os, sys, html, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate as V
import contraste as C
ROOT = V.ROOT
CARTE_FOND = "#E1F3FA"
CARTE_BORD = "#87CEEB"
CARTE_TEXTE = "#0B2540"
CARTES = (
    ".src-pop",
    ".structTip",
    ".codeLegend",
    ".bub.sheet",
    ".atip:not(:empty)",
    ".step:not(:empty)",
)

def verifier_cartes(css_path):
    """Refuse le gabarit si une carte explicative n'a pas le fond, la bordure et le texte imposés."""
    style = open(css_path, encoding="utf-8").read().split("<style>", 1)[-1].split("</style>", 1)[0]
    if C.ratio(CARTE_TEXTE, CARTE_FOND) + 1e-9 < 7:
        return [f"carte {CARTE_TEXTE} sur {CARTE_FOND} sous 7:1"]
    vars_ = C.variables(style)
    manquants = []
    for voulu in CARTES:
        ok = False
        for sel, decl in C.regles(style):
            if voulu not in sel:
                continue
            brut_bg = decl.get("background") or decl.get("background-color") or ""
            brut_fg = decl.get("color") or ""
            if not brut_bg.strip() or not brut_fg.strip():
                continue
            bg = C.resolve(brut_bg, vars_)
            fg = C.resolve(brut_fg, vars_)
            morceaux = (decl.get("border") or "").split()
            bord = C.resolve(morceaux[-1], vars_) if morceaux else None
            if bg == CARTE_FOND.lower() and fg == CARTE_TEXTE.lower() and bord == CARTE_BORD.lower():
                ok = True
                break
        if not ok:
            manquants.append(voulu)
    if manquants:
        return ["carte absente ou couleurs différentes : " + ", ".join(manquants)]
    return []

def main():
    a = sys.argv[1:]
    ext, inc = "--external" in a, "--include-test" in a
    out = a[a.index("--out") + 1] if "--out" in a else os.path.join(ROOT, "app", "Radio_Paires.html")
    out = os.path.abspath(out)
    dxs = json.load(open(os.path.join(ROOT, "diagnostics.json")))
    by = {d["id"]: d for d in dxs}
    mans = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "manifest", "*.json"))):
        b = os.path.basename(f)
        if b == "SCHEMA.json" or (b.startswith("TEST-") and not inc):
            continue
        try:
            m = json.load(open(f))
        except Exception as e:
            print("JSON invalide", b, e); continue
        tid = m.get("test_of") if b.startswith("TEST-") else m.get("id")
        if tid not in by:
            print("ignoré (id inconnu)", b); continue
        if tid in mans and not b.startswith("TEST-"):
            continue
        m["_test"] = b.startswith("TEST-")
        mans[tid] = m
    imgs, rows = {}, []
    def img(path):
        if not path:
            return None
        p = os.path.join(ROOT, path)
        if not os.path.isfile(p):
            return None
        if ext:
            return {"src": os.path.relpath(p, os.path.dirname(out)).replace(os.sep, "/")}
        if path not in imgs:
            imgs[path] = "data:image/jpeg;base64," + base64.b64encode(open(p, "rb").read()).decode()
        return {"ref": path}
    from PIL import Image
    def side(s):
        if not s:
            return None
        o = {k: s.get(k, "") for k in ("source_url", "license", "license_url", "author", "sex", "modality", "sequence", "plane", "region", "note", "caption_source", "age_ans", "anonymisation_verifiee")}
        if isinstance(s.get("anatomie"), list):
            o["anatomie"] = s["anatomie"]
        if isinstance(s.get("indices"), dict):
            o["indices"] = s["indices"]
        im = img(s.get("file"))
        if im:
            with Image.open(os.path.join(ROOT, s["file"])) as I:
                o["w"], o["h"] = I.size
            o.update(im)
        o["arrows"] = [{k: x.get(k) for k in (
            "tip", "from", "label", "role", "evidence", "confidence",
            "contour", "definition", "definition_source", "couleur",
            "aspect", "aspect_source")} for x in s.get("arrows") or []]
        return o
    for d in dxs:
        r = dict(d)
        r["mod"] = d["cliche"].split(" — ")[0].strip()
        m = mans.get(d["id"])
        if not m:
            r["st"] = "en recherche"
        else:
            errs, warns = [], []
            V.check(m, d, errs, warns)
            r["st"] = "non validé" if errs else m.get("statut")
            r["m"] = {"normal": side(m.get("normal")), "patho": side(m.get("patho")),
                      "pair_match": m.get("pair_match", ""), "a_verifier": m.get("a_verifier") or [],
                      "queries": m.get("queries") or [], "errors": errs, "test": m["_test"]}
        rows.append(r)
    data = {"rows": rows, "built": datetime.datetime.now().strftime("%d.%m.%Y %H:%M"), "test": inc}
    tpl_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app_template.html")
    ecarts = C.check(tpl_path) + verifier_cartes(tpl_path)
    if ecarts:
        print("CONTRASTE refusé :", *ecarts, sep="\n - ")
        sys.exit(1)
    tpl = open(tpl_path, encoding="utf-8").read()
    js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    page = tpl.replace("/*__DATA__*/null", js).replace("/*__IMGS__*/null", json.dumps(imgs))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(page)
    c = {}
    for r in rows:
        c[r["st"]] = c.get(r["st"], 0) + 1
    print(f"OK {out} ({os.path.getsize(out)//1024} Ko, {len(imgs)} images embarquées) statuts={c}")

if __name__ == "__main__":
    main()
