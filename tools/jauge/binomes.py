#!/usr/bin/env python3
"""Deux jauges des binômes (prévalences, monographies), zéro jeton, déterministe.

Copie versionnée de /workspace/ssp/jauge/binomes.py. Lit origin/main (ou --ref) par `git show`
dans le dépôt (OEF_REPO, sinon la racine git de ce fichier), sans worktree ni
changement de branche. Champs absents → 0, jamais d'exception.

  Prévalences  : data/ck/prev.json  (prev_pct + src + date_lu + loc ; P3)
  Monographies : data/ck/mono/*.json (def epi phy cli exp dia + but mes pha)
  Audités      : audit/RAPPORT_AUDIT_MEDICAL.md (SSP entre parenthèses, « relu »)
                 audit/RAPPORT_AUDIT_MONO.md    (clés mono, « relu »)
                 ou champ audite / audite_par sur une monographie

Usage :
  binomes.py [--ref origin/main] [--json] [--check] [--init]
"""
import hashlib, json, os, re, subprocess, sys, unicodedata
import math
from datetime import date
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ""))
from mono_build import chronologie_ready as mono_chronologie_ready

def _repo():
    e = os.environ.get("OEF_REPO")
    if e:
        return e
    r = subprocess.run(["git", "-C", os.path.dirname(os.path.abspath(__file__)), "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    return r.stdout.strip() or "/workspace/oef"


REPO = _repo()
BASE = os.path.join(REPO, ".etat_local", "dernier_envoi_binomes.json")  # hors suivi git
# Legacy: six protocol sections represented by the existing required fields.
MONO_REQ = ("def", "epi", "phy", "cli", "exp", "dia", "but", "mes", "pha")
SSP_RE = re.compile(r"\bS\d+(?:\.\d+)+\b")
# ## G1 · thorax (S2.4, S2.5) · PR #43 · relu le 17.10.2026
# ## Lot 1 (endocardite-infectieuse, pneumonie) · relu le …
HEAD_RE = re.compile(r"^##\s+.+\(([^)]*)\).*relu", re.I | re.M)
CHRONO_REVIEW_PATH = "tools/coordination/relectures.json"
SOURCES_PATH = "data/ck/src.json"


def git(*a, ok=False):
    r = subprocess.run(["git", "-C", REPO, *a], capture_output=True, text=True)
    if r.returncode and not ok:
        raise SystemExit(r.stderr or f"git {' '.join(a)} → {r.returncode}")
    return r.stdout if r.returncode == 0 else ""


def show(ref, path):
    return git("show", f"{ref}:{path}", ok=True)


def const(app, name):
    k = "\nconst " + name + "="
    if app.count(k) != 1:
        return None
    i = app.find(k) + len(k)
    return json.JSONDecoder().raw_decode(app, i)[0]


def mid(name):
    x = "".join(c for c in unicodedata.normalize("NFKD", name.lower()) if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", x).strip("-")


def load_prev(ref):
    raw = show(ref, "data/ck/prev.json")
    if not raw:
        return {}
    try:
        return {k: v for k, v in json.loads(raw).items() if not k.startswith("_")}
    except json.JSONDecodeError:
        return {}


def load_mono(ref):
    M = {}
    for f in git("ls-tree", "--name-only", ref, "data/ck/mono/", ok=True).split():
        if not f.endswith(".json"):
            continue
        try:
            M.update({k: v for k, v in json.loads(show(ref, f)).items() if not k.startswith("_")})
        except json.JSONDecodeError:
            continue
    return M


def headers_ids(md):
    """Identifiants entre parenthèses des titres « … relu … »."""
    out = []
    for m in HEAD_RE.finditer(md or ""):
        out.extend(x.strip() for x in m.group(1).split(",") if x.strip())
    return out


def chronology_fingerprint(value):
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    import hashlib
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def chronology_review_ids(raw, monos, ids, sources, report_loader):
    """Use the central review ledger, requiring a current, fully verified attestation."""
    try:
        data = json.loads(raw or "{}")
    except (TypeError, json.JSONDecodeError):
        return set()
    if (not isinstance(data, dict) or type(data.get("version")) is not int or data["version"] != 1
            or not isinstance(data.get("monographies"), dict)):
        return set()
    reviewed = set()
    for key, record in data["monographies"].items():
        value = monos.get(key)
        if key not in ids or not isinstance(value, dict) or not chronologie_ok(value):
            continue
        if (not isinstance(record, dict) or record.get("chronologie_relue") is not True
                or record.get("statut") != "revue_documentaire"
                or record.get("validation_clinique") is not False
                or record.get("sha256") != chronology_fingerprint(value)):
            continue
        try:
            read_date = date.fromisoformat(record.get("date_lu", ""))
        except (ValueError, TypeError):
            continue
        if read_date > date.today():
            continue
        source_ids = record.get("sources")
        if (not isinstance(source_ids, list) or not source_ids
                or any(not isinstance(source_id, str) or source_id not in sources for source_id in source_ids)):
            continue
        report_path = record.get("rapport")
        if (not isinstance(report_path, str) or not report_path.strip()
                or report_path.startswith("/") or ".." in report_path.split("/")):
            continue
        report_raw = report_loader(report_path)
        if not report_raw:
            continue
        expected_report_hash = record.get("rapport_sha256")
        if (not isinstance(expected_report_hash, str)
                or hashlib.sha256(report_raw.encode("utf-8")).hexdigest() != expected_report_hash):
            continue
        reviewed.add(key)
    return reviewed


def prev_ok(e):
    try:
        read_date = date.fromisoformat(e.get('date_lu', ''))
    except (ValueError, TypeError):
        return False
    value = e.get('prev_pct')
    return (type(value) in (int, float) and math.isfinite(value) and 0 < value <= 100
            and e.get('statut') != 'À vérifier' and read_date <= date.today()
            and all(isinstance(e.get(k), str) and e[k].strip() for k in ('src', 'loc')))


def prev_av(e):
    return e.get("prev_pct") is None or e.get("statut") == "À vérifier"


def mono_ok(v):
    return all(isinstance(v.get(f), str) and v[f].strip() for f in MONO_REQ)


def chronologie_ok(v):
    """Structural readiness only; this is not clinical review or source validation."""
    if (type(v.get("prototype_version")) is not int or v.get("prototype_version") != 1
            or type(v.get("chronologie_version")) is not int or v.get("chronologie_version") != 1):
        return False
    if not all(isinstance(v.get(k), str) and v[k].strip()
               for k in ("exp_ref", "exp_premier", "exp_bio", "exp_morph", "exp_fonc")):
        return False
    return mono_chronologie_ready(v)


def mesurer(ref="origin/main"):
    app = show(ref, "app_v2.html")
    if not app:
        raise SystemExit(f"app_v2.html absent à {ref}")
    NOT = const(app, "NOT") or {}
    PV = load_prev(ref)
    mono = load_mono(ref)

    # ---- Gauge 1 : une entrée par diagnostic de NOT
    tot_prev = a_verif = n_prev = 0
    detail_prev = {}  # ssp → (ok, av, tot) pour --check
    for c, bloc in NOT.items():
        noms = bloc[0] if bloc else []
        by_i = {e["i"]: e for e in PV.get(c, {}).get("items", []) if isinstance(e.get("i"), int)}
        ok = av = 0
        for i, _ in enumerate(noms):
            e = by_i.get(i)
            if e and prev_ok(e):
                ok += 1
            elif e and prev_av(e):
                av += 1
        tot_prev += len(noms)
        n_prev += ok
        a_verif += av
        detail_prev[c] = (ok, av, len(noms))

    # Audités Galien : SSP cités dans un titre « relu » du rapport
    galien_md = show(ref, "audit/RAPPORT_AUDIT_MEDICAL.md")
    ssp_aud = {x for x in headers_ids(galien_md) if SSP_RE.fullmatch(x)}
    n_aud_prev = sum(detail_prev.get(c, (0, 0, 0))[2] for c in ssp_aud)

    # ---- Gauge 2 : monographies uniques (clés = libellés normalisés de NOT)
    ids = {mid(d) for bloc in NOT.values() for d in (bloc[0] if bloc else []) if d}
    n_mono = sum(1 for k in ids if k in mono and mono_ok(mono[k]))
    # Audités Hérophile : rapport mono, ou champ sur l'entrée
    hero_md = show(ref, "audit/RAPPORT_AUDIT_MONO.md") or show(ref, "audit/RAPPORT_AUDIT_HEROPHILE.md")
    keys_aud = {x for x in headers_ids(hero_md) if not SSP_RE.fullmatch(x)}
    for k, v in mono.items():
        if v.get("audite") or v.get("audite_par") or v.get("aud"):
            keys_aud.add(k)
    n_aud_mono = sum(1 for k in keys_aud if k in ids)
    mono_chrono = {k for k in ids if k in mono and chronologie_ok(mono[k])}
    try:
        sources_raw = json.loads(show(ref, SOURCES_PATH) or "[]")
        source_ids = {item["id"] for item in sources_raw if isinstance(item, dict) and isinstance(item.get("id"), str)}
    except json.JSONDecodeError:
        source_ids = set()
    chrono_reviewed = chronology_review_ids(show(ref, CHRONO_REVIEW_PATH), mono, ids, source_ids,
                                           lambda path: show(ref, path))
    n_aud_chrono = sum(1 for k in chrono_reviewed if k in mono_chrono and k in ids)

    def pct(n, d):
        return round(100 * n / d) if d else 0

    return {
        "ref": ref,
        "prevalences": {
            "ok": n_prev, "total": tot_prev, "pct": pct(n_prev, tot_prev),
            "a_verifier": a_verif, "audites": n_aud_prev,
        },
        "monographies": {
            "ok": n_mono, "total": len(ids), "pct": pct(n_mono, len(ids)),
            "audites": n_aud_mono,
        },
        "chronologie_structures": {
            "ok": len(mono_chrono), "total": len(ids), "pct": pct(len(mono_chrono), len(ids)),
        },
        "chronologie_relectures": {
            "ok": n_aud_chrono, "total": len(ids), "pct": pct(n_aud_chrono, len(ids)),
        },
        "_detail_prev": detail_prev,
        "_ids": ids,
        "_mono": mono,
    }


def barre(p):
    n = max(0, min(10, round(p / 10)))
    return "█" * n + "░" * (10 - n)


def lignes(R):
    P, M = R["prevalences"], R["monographies"]
    C, A = R["chronologie_structures"], R["chronologie_relectures"]
    return [
        f"Prévalences   {barre(P['pct'])}  {P['pct']:>3} %  ({P['ok']}/{P['total']} · audités {P['audites']})",
        f"Monographies  {barre(M['pct'])}  {M['pct']:>3} %  ({M['ok']}/{M['total']} · audités {M['audites']})",
        f"Chronologies  {barre(C['pct'])}  {C['pct']:>3} %  ({C['ok']}/{C['total']} · structurées)",
        f"Relectures    {barre(A['pct'])}  {A['pct']:>3} %  ({A['ok']}/{A['total']} · chronologies relues)",
    ]


def check(R, ssp=("S2.4", "S2.5", "S3.1")):
    """Recount manuel sur 3 SSP : doit égaler detail_prev."""
    ref = R["ref"]
    NOT = const(show(ref, "app_v2.html"), "NOT") or {}
    PV = load_prev(ref)
    err = []
    for c in ssp:
        noms = (NOT.get(c) or [[]])[0]
        by_i = {e["i"]: e for e in PV.get(c, {}).get("items", []) if isinstance(e.get("i"), int)}
        ok = av = 0
        for i in range(len(noms)):
            e = by_i.get(i)
            if e and prev_ok(e):
                ok += 1
            elif e and prev_av(e):
                av += 1
        got = R["_detail_prev"].get(c, (0, 0, 0))
        if got != (ok, av, len(noms)):
            err.append(f"{c}: script={got} manuel={(ok, av, len(noms))}")
    # mono : 3 premières clés alphabétiques présentes (ou absentes)
    ids = sorted(R["_ids"])
    for k in ids[:3]:
        v = R["_mono"].get(k)
        expect = bool(v and mono_ok(v))
        got = k in R["_mono"] and mono_ok(R["_mono"][k])
        if expect != got:
            err.append(f"mono {k}: script={got} manuel={expect}")
    chrono_manual = sum(1 for k in ids if k in R["_mono"] and chronologie_ok(R["_mono"][k]))
    if chrono_manual != R["chronologie_structures"]["ok"]:
        err.append(f"chronologies structurées: script={R['chronologie_structures']['ok']} manuel={chrono_manual}")
    try:
        sources_raw = json.loads(show(ref, SOURCES_PATH) or "[]")
        source_ids = {item["id"] for item in sources_raw if isinstance(item, dict) and isinstance(item.get("id"), str)}
    except json.JSONDecodeError:
        source_ids = set()
    reviewed = chronology_review_ids(show(ref, CHRONO_REVIEW_PATH), R["_mono"], set(ids), source_ids,
                                     lambda path: show(ref, path))
    review_manual = sum(1 for k in reviewed if k in R["_mono"] and chronologie_ok(R["_mono"][k]))
    if review_manual != R["chronologie_relectures"]["ok"]:
        err.append(f"chronologies relues: script={R['chronologie_relectures']['ok']} manuel={review_manual}")
    # totaux = somme des détails
    s_ok = sum(t[0] for t in R["_detail_prev"].values())
    s_tot = sum(t[2] for t in R["_detail_prev"].values())
    if (s_ok, s_tot) != (R["prevalences"]["ok"], R["prevalences"]["total"]):
        err.append(f"somme SSP ≠ total: {(s_ok, s_tot)} vs "
                   f"{(R['prevalences']['ok'], R['prevalences']['total'])}")
    return err


def init_baseline(R):
    data = {
        "prevalences": R["prevalences"]["pct"],
        "monographies": R["monographies"]["pct"],
        "ref": R["ref"],
    }
    os.makedirs(os.path.dirname(BASE), exist_ok=True)
    with open(BASE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    return data


if __name__ == "__main__":
    args = sys.argv[1:]
    ref = args[args.index("--ref") + 1] if "--ref" in args else "origin/main"
    R = mesurer(ref)
    if "--check" in args:
        err = check(R)
        print("\n".join(lignes(R)))
        if err:
            print("ÉCHEC:\n" + "\n".join(err), file=sys.stderr)
            sys.exit(1)
        print(f"check OK · 3 SSP + totaux · ref={ref}")
        sys.exit(0)
    if "--init" in args or not os.path.exists(BASE):
        init_baseline(R)
    if "--json" in args:
        out = {k: R[k] for k in ("ref", "prevalences", "monographies", "chronologie_structures", "chronologie_relectures")}
        if os.path.exists(BASE):
            out["dernier_envoi"] = json.load(open(BASE, encoding="utf-8"))
        print(json.dumps(out, ensure_ascii=False))
    else:
        print("\n".join(lignes(R)))
