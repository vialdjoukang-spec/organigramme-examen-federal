#!/usr/bin/env python3
"""validate.py — deterministic, zero-token checks on every manifest/IMG-*.json.
CLI:  python3 scripts/validate.py [--only IMG-001,IMG-002] [--quiet] [--include-test]
Out:  table on stdout (id | statut déclaré | statut validé | erreurs | avertissements) + validate_report.json
Exit code 1 if any ERROR.
Rules:
  E  manifest JSON valid; id in diagnostics.json; statut in complet|partiel|introuvable
  E  (complet|partiel) normal+patho files exist, are JPEG, long side <= 1024
  E  licence in whitelist (CC0, Public domain/PD, CC BY x.y, CC BY-SA x.y); author + source_url present
  E  complet => modality, plane (and sequence when given) identical normal vs patho; modality matches cliché
  E  complet => image normale présente
  E  complet => les deux clichés sont d'un adulte (champ adulte = oui) et chaque oui a une adulte_preuve
       (légende ou signe de maturité : physes soudées, dentition définitive, sutures ou morphologie adultes).
  E  complet et région bassin, sein ou organes génitaux => sexe M/F écrit et identique des deux côtés
  E  dans ces régions, sexes établis et discordants => erreur
  E  complet => contour rectangulaire de ≤ 5 points interdit
  E  polygone trop régulier (variance des rayons et des angles quasi nulle) interdit
  E  lésion non ponctuelle : au moins 8 sommets distincts
  E  complet => >= 1 arrow role=principale
  E  every arrow: tip/from in [0,1], label, role in whitelist, evidence, confidence in haute|moyenne|basse
  E  every arrow: contour = polygone fermé (dernier point = premier, ≥ 3 sommets distincts, chaque point dans [0,1])
  E  every arrow: definition + definition_source non vides ; complet interdit « À vérifier » comme définition ou source
  E  confidence basse => arrow label quoted in a_verifier
  E  introuvable => queries non-empty
  W  partiel without pair_match explanation; pixel identical normal/patho; caption_source missing
"""
import json, math, os, re, sys, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WL = re.compile(r"^(cc0( 1\.0)?|public domain|pd(-[\w-]+)?|cc[ -]by(-sa)?[ -]\d\.\d( [a-z]{2,})?|cc[ -]by(-sa)?)$", re.I)
ROLES = {"principale", "associee", "secondaire", "complication"}
CONF = {"haute", "moyenne", "basse"}
MOD = {"TDM": {"tdm", "ct", "scanner", "angio-tdm", "coroscanner", "uro-tdm", "entéro-tdm"},
       "IRM": {"irm", "mri", "arm", "angio-irm", "entéro-irm", "cholangio-irm"},
       "RX": {"rx", "radiographie", "x-ray", "radiograph", "mammographie", "transit", "opacification"},
       "US": {"us", "échographie", "echographie", "doppler", "ultrasound", "écho"},
       "MN": {"mn", "scintigraphie", "tep", "tep-tdm", "pet", "pet-ct", "spect", "tep-scanner"},
       "INT": {"int", "angiographie", "artériographie", "dsa", "phlébographie"}}

def norm(s):
    return re.sub(r"\s+", " ", (s or "").strip().lower())

def mod_ok(cliche, m):
    pref = cliche.split(" — ")[0].strip()
    allowed = MOD.get(pref)
    if not allowed:
        return True
    m = norm(m)
    return m in allowed or any(m.startswith(a) for a in allowed) or m == pref.lower()

def img_check(path, errs, tag):
    p = os.path.join(ROOT, path or "")
    if not path or not os.path.isfile(p):
        errs.append(f"{tag}: fichier absent ({path})"); return None
    with open(p, "rb") as f:
        head = f.read(3)
    if head != b"\xff\xd8\xff":
        errs.append(f"{tag}: pas un JPEG")
    try:
        from PIL import Image
        with Image.open(p) as im:
            if max(im.size) > 1024:
                errs.append(f"{tag}: {im.size} > 1024 px")
            if "exif" in im.info:
                errs.append(f"{tag}: EXIF présent (passer normalize.py)")
            return im.size
    except Exception as e:
        errs.append(f"{tag}: illisible {e}")

def inunit(v):
    return isinstance(v, (list, tuple)) and len(v) == 2 and all(
        isinstance(c, (int, float)) and not isinstance(c, bool) and 0 <= c <= 1 for c in v)

def _pt(v):
    if not inunit(v):
        return None
    return (float(v[0]), float(v[1]))

SEX_REG = re.compile(
    r"\b(seins?|mammaire|mammographie|breast|utérus|uterus|utérin\w*|uterin\w*|ovaires?|"
    r"prostate|testicules?|pénis|penis|vagin\w*|vulve|scrotum|endomètre|endometre|"
    r"génitaux|genitaux|cervix|grossesse|placenta)\b|bassin(?!\s+versant)",
    re.I)

def sexe_requis(m, dx):
    """Vial, 14.11.2026 10:48 : le sexe concordant n'est exigé que là où il change l'anatomie."""
    if (dx or {}).get("region") == "Pelvis":
        return True
    blob = " ".join([
        (dx or {}).get("dx") or "", (dx or {}).get("cliche") or "",
        m.get("dx") or "", m.get("cliche") or "",
        (m.get("normal") or {}).get("region") or "",
        (m.get("patho") or {}).get("region") or "",
    ])
    return bool(SEX_REG.search(blob))

def adulte_code(v):
    """oui, non, '' si absent ou « À vérifier », None si illisible."""
    s = norm(v)
    if s in ("oui", "adulte", "adult", "yes"):
        return "oui"
    if s in ("non", "enfant", "child", "no"):
        return "non"
    if not s or s in ("à vérifier", "a vérifier", "a verifier"):
        return ""
    return None

def sex_code(v):
    """M, F, '' si absent ou « À vérifier », None si la valeur n'est pas reconnue."""
    s = norm(v)
    if s in ("m", "h", "homme", "masculin", "male", "man"):
        return "M"
    if s in ("f", "femme", "feminin", "féminin", "female", "woman"):
        return "F"
    if not s or s in ("à vérifier", "a vérifier", "a verifier"):
        return ""
    return None

def coarse_rectangle(contour):
    """Rectangle (4 coins, angles droits) stocké en 5 points ou moins, fermeture comprise."""
    if not isinstance(contour, list) or not (4 <= len(contour) <= 5):
        return False
    pts = []
    for p in contour:
        q = _pt(p)
        if q is None:
            return False
        pts.append(q)
    if math.hypot(pts[0][0] - pts[-1][0], pts[0][1] - pts[-1][1]) <= 0.015:
        verts = pts[:-1]
    else:
        verts = pts[:]
    uniq = []
    for x, y in verts:
        if not any(abs(x - a) < 1e-4 and abs(y - b) < 1e-4 for a, b in uniq):
            uniq.append((x, y))
    if len(uniq) != 4:
        return False
    cx = sum(p[0] for p in uniq) / 4
    cy = sum(p[1] for p in uniq) / 4
    uniq.sort(key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
    for i in range(4):
        ax = uniq[i][0] - uniq[i - 1][0]
        ay = uniq[i][1] - uniq[i - 1][1]
        bx = uniq[(i + 1) % 4][0] - uniq[i][0]
        by = uniq[(i + 1) % 4][1] - uniq[i][1]
        na, nb = math.hypot(ax, ay), math.hypot(bx, by)
        if na < 1e-6 or nb < 1e-6:
            return False
        if abs((ax * bx + ay * by) / (na * nb)) > 0.25:
            return False
    return True

def _angles(verts):
    ang = []
    n = len(verts)
    for i in range(n):
        ax, ay = verts[i][0] - verts[i - 1][0], verts[i][1] - verts[i - 1][1]
        bx, by = verts[(i + 1) % n][0] - verts[i][0], verts[(i + 1) % n][1] - verts[i][1]
        na, nb = math.hypot(ax, ay), math.hypot(bx, by)
        if na < 1e-8 or nb < 1e-8:
            continue
        cos = max(-1.0, min(1.0, (ax * bx + ay * by) / (na * nb)))
        ang.append(math.acos(cos))
    return ang

def too_regular(contour):
    """Variance des rayons et des angles quasi nulle : polygone régulier, pas une silhouette."""
    if not isinstance(contour, list) or len(contour) < 4:
        return False
    pts = []
    for p in contour:
        q = _pt(p)
        if q is None:
            return False
        pts.append(q)
    if math.hypot(pts[0][0] - pts[-1][0], pts[0][1] - pts[-1][1]) <= 0.015:
        verts = pts[:-1]
    else:
        verts = pts
    uniq = []
    for x, y in verts:
        if not any(abs(x - a) < 1e-3 and abs(y - b) < 1e-3 for a, b in uniq):
            uniq.append((x, y))
    if len(uniq) < 6:
        return False
    cx = sum(p[0] for p in uniq) / len(uniq)
    cy = sum(p[1] for p in uniq) / len(uniq)
    radii = [math.hypot(x - cx, y - cy) for x, y in uniq]
    mean = sum(radii) / len(radii)
    if mean < 1e-6:
        return False
    var_r = sum((r - mean) ** 2 for r in radii) / len(radii)
    cv = math.sqrt(var_r) / mean
    ang = _angles(uniq)
    if len(ang) < 6:
        return False
    mean_a = sum(ang) / len(ang)
    var_a = sum((a - mean_a) ** 2 for a in ang) / len(ang)
    return cv < 0.045 and math.sqrt(var_a) < 0.12

def ponctuelle(contour):
    """Petite lésion : le cadre du contour tient dans 4 % de l'image."""
    pts = [_pt(p) for p in contour if _pt(p)]
    if len(pts) < 3:
        return True
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return max(max(xs) - min(xs), max(ys) - min(ys)) < 0.04

def contour_ok(contour, errs, tag):
    """Polygone fermé, ≥ 3 sommets distincts, chaque point dans l'image (0–1)."""
    if not isinstance(contour, list) or len(contour) < 4:
        errs.append(f"{tag}: contour absent ou non fermé (< 3 sommets + fermeture)")
        return
    pts = []
    for j, p in enumerate(contour, 1):
        q = _pt(p)
        if q is None:
            errs.append(f"{tag}: point {j} hors de l'image ou invalide")
            return
        pts.append(q)
    dist = ((pts[0][0] - pts[-1][0]) ** 2 + (pts[0][1] - pts[-1][1]) ** 2) ** 0.5
    if dist > 0.015:
        errs.append(f"{tag}: polygone non fermé (le dernier point doit répéter le premier)")
        return
    verts = pts[:-1]
    uniq = {(round(x, 3), round(y, 3)) for x, y in verts}
    if len(uniq) < 3:
        errs.append(f"{tag}: moins de 3 sommets distincts")

def check(m, dx, errs, warns):
    st = m.get("statut")
    if st not in ("complet", "partiel", "introuvable"):
        errs.append(f"statut invalide: {st}"); return
    if dx and norm(m.get("dx")) != norm(dx["dx"]):
        warns.append(f"dx diffère de diagnostics.json ({dx['dx']})")
    if st == "introuvable":
        if not m.get("queries"):
            errs.append("introuvable sans 'queries' tentées")
        return
    n, p = m.get("normal") or {}, m.get("patho") or {}
    for tag, side in (("normal", n), ("patho", p)):
        if not side:
            if st == "partiel":
                warns.append(f"{tag}: absent (partiel)"); continue
            errs.append(f"{tag}: bloc absent")
            if st == "complet" and tag == "normal":
                errs.append("complet sans image normale")
            continue
        img_check(side.get("file"), errs, tag)
        lic = (side.get("license") or "").strip()
        if not WL.match(lic):
            errs.append(f"{tag}: licence hors liste blanche «{lic}»")
        if not (side.get("author") or "").strip():
            errs.append(f"{tag}: auteur absent")
        if not (side.get("source_url") or "").startswith("http"):
            errs.append(f"{tag}: source_url absente")
        if dx and side.get("modality") and not mod_ok(dx["cliche"], side["modality"]):
            (errs if st == "complet" else warns).append(f"{tag}: modalité «{side.get('modality')}» ≠ cliché «{dx['cliche']}»")
    if n and p:
        for k in ("modality", "plane", "sequence"):
            a, b = norm(n.get(k)), norm(p.get(k))
            if k == "sequence" and not a and not b:
                continue
            if a != b or (k != "sequence" and not a):
                (errs if st == "complet" else warns).append(f"{k}: normal «{n.get(k)}» ≠ patho «{p.get(k)}»")
        fa, fb = os.path.join(ROOT, n.get("file", "")), os.path.join(ROOT, p.get("file", ""))
        if os.path.isfile(fa) and os.path.isfile(fb) and open(fa, "rb").read() == open(fb, "rb").read():
            errs.append("normal et patho identiques (même fichier)")
    sn, sp = sex_code(n.get("sex")), sex_code(p.get("sex"))
    requis = sexe_requis(m, dx)
    if sn is None or sp is None:
        errs.append("sexe illisible (attendu : M, F ou « À vérifier »)")
    elif requis and sn and sp and sn != sp:
        errs.append(f"sexe discordant : normal {sn} ≠ patho {sp}")
    elif requis and st == "complet" and (not sn or not sp or sn != sp):
        errs.append("complet : sexe requis (bassin, sein ou organes génitaux) non concordant")
    elif (not requis) and sn and sp and sn != sp:
        warns.append(f"sexe différent hors région sexuelle : normal {sn} ≠ patho {sp}")
    an, ap = adulte_code(n.get("adulte")), adulte_code(p.get("adulte"))
    if an is None or ap is None:
        errs.append("adulte illisible (attendu : oui, non ou « À vérifier »)")
    elif st == "complet" and (an != "oui" or ap != "oui"):
        errs.append("complet : les deux clichés doivent être ceux d'un adulte")
    elif st == "complet":
        for tag, side in (("normal", n), ("patho", p)):
            preuve = (side.get("adulte_preuve") or "").strip()
            if not preuve or norm(preuve) in ("à vérifier", "a vérifier", "a verifier"):
                errs.append(f"complet : {tag} adulte sans adulte_preuve")
    if p and not p.get("caption_source"):
        warns.append("patho: caption_source absent")
    arrows = (p or {}).get("arrows") or []
    if st == "complet" and not any(a.get("role") == "principale" for a in arrows):
        errs.append("complet sans flèche role=principale")
    av = " ".join(m.get("a_verifier") or []).lower()
    for i, a in enumerate(arrows, 1):
        t = f"flèche {i}"
        if not inunit(a.get("tip")): errs.append(f"{t}: tip hors [0,1] ou absent")
        if not inunit(a.get("from")): errs.append(f"{t}: from hors [0,1] ou absent")
        if inunit(a.get("tip")) and inunit(a.get("from")) and \
           ((a["tip"][0] - a["from"][0]) ** 2 + (a["tip"][1] - a["from"][1]) ** 2) ** .5 < 0.04:
            warns.append(f"{t}: flèche très courte (<4 % de l'image)")
        if not (a.get("label") or "").strip(): errs.append(f"{t}: label absent")
        if a.get("role") not in ROLES: errs.append(f"{t}: role «{a.get('role')}» invalide")
        if not (a.get("evidence") or "").strip(): errs.append(f"{t}: evidence absente")
        c = a.get("confidence")
        if c not in CONF: errs.append(f"{t}: confidence «{c}» invalide")
        defin = (a.get("definition") or "").strip()
        dsrc = (a.get("definition_source") or "").strip()
        if not defin:
            errs.append(f"{t}: définition radiologique absente")
        elif st == "complet" and norm(defin) in ("à vérifier", "a vérifier"):
            errs.append(f"{t}: définition « À vérifier » incompatible avec complet")
        if not dsrc:
            errs.append(f"{t}: définition non sourcée (definition_source absent)")
        elif st == "complet" and norm(dsrc) in ("à vérifier", "a vérifier", "visuel"):
            errs.append(f"{t}: définition non sourcée (complet)")
        contour_ok(a.get("contour"), errs, t)
        if st == "complet" and coarse_rectangle(a.get("contour")):
            errs.append(f"{t}: contour rectangulaire (≤ 5 points)")
        ctn = a.get("contour")
        if isinstance(ctn, list) and ctn and not ponctuelle(ctn):
            verts = ctn[:-1] if len(ctn) > 1 else ctn
            uniq = {(round(p[0], 3), round(p[1], 3)) for p in verts if _pt(p)}
            if len(uniq) < 8:
                errs.append(f"{t}: lésion non ponctuelle avec moins de 8 sommets")
        if too_regular(ctn):
            errs.append(f"{t}: polygone trop régulier (rayons et angles quasi constants)")
        if c == "basse" and (a.get("label") or "").strip().lower() not in av:
            errs.append(f"{t}: confiance basse mais «{a.get('label')}» absent de a_verifier")
    if st == "partiel" and not (m.get("pair_match") or m.get("a_verifier")):
        warns.append("partiel sans explication (pair_match/a_verifier)")

def main():
    a = sys.argv[1:]
    only = set()
    if "--only" in a:
        only = set(a[a.index("--only") + 1].split(","))
    quiet, inc_test = "--quiet" in a, "--include-test" in a
    dxs = {d["id"]: d for d in json.load(open(os.path.join(ROOT, "diagnostics.json")))}
    rep, nerr = [], 0
    for f in sorted(glob.glob(os.path.join(ROOT, "manifest", "*.json"))):
        b = os.path.basename(f)
        if b == "SCHEMA.json" or (b.startswith("TEST-") and not inc_test):
            continue
        errs, warns = [], []
        try:
            m = json.load(open(f))
        except Exception as e:
            rep.append({"file": b, "id": b, "declared": "?", "valid": "erreur", "errors": [f"JSON invalide: {e}"], "warnings": []}); nerr += 1; continue
        mid = m.get("id") or b[:-5]
        if only and mid not in only:
            continue
        dx = dxs.get(mid) or dxs.get(m.get("dx_id", ""))
        if not dx and not b.startswith("TEST-"):
            errs.append("id absent de diagnostics.json")
        if b.startswith("TEST-") and not dx:
            dx = dxs.get(m.get("test_of", ""))
        check(m, dx, errs, warns)
        valid = "erreur" if errs else m.get("statut")
        nerr += bool(errs)
        rep.append({"file": b, "id": mid, "declared": m.get("statut"), "valid": valid, "errors": errs, "warnings": warns})
    cnt = {}
    for r in rep:
        cnt[r["valid"]] = cnt.get(r["valid"], 0) + 1
    summary = {"manifests": len(rep), "par_statut_valide": cnt, "avec_erreurs": nerr,
               "diagnostics_total": len(dxs), "complets_valides": cnt.get("complet", 0)}
    json.dump({"summary": summary, "items": rep}, open(os.path.join(ROOT, "validate_report.json"), "w"), ensure_ascii=False, indent=1)
    w = max([10] + [len(r["id"]) for r in rep])
    print(f"{'id':<{w}} | déclaré     | validé      | E | W | 1re erreur / avertissement")
    for r in rep:
        if quiet and not r["errors"]:
            continue
        first = (r["errors"] or r["warnings"] or [""])[0]
        print(f"{r['id']:<{w}} | {str(r['declared']):<11} | {str(r['valid']):<11} | {len(r['errors'])} | {len(r['warnings'])} | {first[:110]}")
    print("RÉSUMÉ", json.dumps(summary, ensure_ascii=False))
    sys.exit(1 if nerr else 0)

if __name__ == "__main__":
    main()
