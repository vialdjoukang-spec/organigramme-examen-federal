#!/usr/bin/env python3
"""build_app.py — génère app/Radio_Paires.html (fichier unique hors-ligne).
CLI: python3 scripts/build_app.py [--external] [--include-test] [--out app/Radio_Paires.html]
  défaut       : images embarquées en data URI JPEG (fichier autonome)
  --external   : référence ../images/... (fichier léger, dossier images/ requis à côté)
  --include-test : manifests TEST-*.json appliqués à leur diagnostic (champ test_of), badge TEST
Le statut affiché est le statut VALIDÉ par validate.py (un manifest en erreur n'est jamais « complet »).
"""
import base64, glob, json, os, sys, html, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate as V
ROOT = V.ROOT

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
        o = {k: s.get(k, "") for k in ("source_url", "license", "license_url", "author", "sex", "modality", "sequence", "plane", "region", "note", "caption_source")}
        im = img(s.get("file"))
        if im:
            with Image.open(os.path.join(ROOT, s["file"])) as I:
                o["w"], o["h"] = I.size
            o.update(im)
        o["arrows"] = [{k: x.get(k) for k in (
            "tip", "from", "label", "role", "evidence", "confidence",
            "contour", "definition", "definition_source")} for x in s.get("arrows") or []]
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
    tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "app_template.html"), encoding="utf-8").read()
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
