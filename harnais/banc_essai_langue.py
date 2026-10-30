#!/usr/bin/env python3
"""Banc d'essai gratuit (zéro jeton) : audit_langue.py rejoué contre les corrections réelles de l'auditeur de conformité.

Pour chaque fichier Phase B des LOT_013 à LOT_016 audité, retrouve dans git la version qui précède l'audit de
conformité (la version de l'historique dont le texte contient le plus de passages « avant » journalisés),
passe audit_langue.py dessus et compare aux lignes de corrections.jsonl.

Sortie : LOT_Claude_Finaux/BANC_ESSAI_LANGUE.json + résumé texte.
Usage  : python3 harnais/banc_essai_langue.py [--lots 013,014,015,016]
"""
from __future__ import annotations
import argparse, html, json, re, subprocess, sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audit_langue as AL  # noqa: E402

RACINE = Path(__file__).resolve().parent.parent
WIP = "lot en cours de production"
FIN = "LOT_Claude_Finaux"


def git(*args: str) -> bytes:
    return subprocess.run(["git", *args], cwd=RACINE, capture_output=True).stdout


def lire_jsonl(p: Path) -> list[dict]:
    return [json.loads(l) for l in p.read_text(encoding="utf8").splitlines() if l.strip()] if p.is_file() else []


def norm(s: str) -> str:
    s = html.unescape(re.sub(r"<[^>]+>", " ", s or "")).replace(" ", " ")
    return re.sub(r"[^a-z0-9àâäçéèêëîïôöùûüœ]+", " ", s.lower()).strip()


def agent_de(c: dict) -> str:
    a = c.get("auditeur")
    if isinstance(a, dict):
        a = a.get("agent")
    return (a or c.get("agent") or "?").split(" (")[0]


def blobs_historique(chemin: str) -> list[str]:
    """Contenus distincts successifs (du plus ancien au plus récent) du fichier dans l'historique git."""
    commits = git("log", "--reverse", "--format=%H", "--", chemin).decode().split()
    vus, out = set(), []
    for c in commits:
        b = git("rev-parse", f"{c}:{chemin}").decode().strip()
        if len(b) == 40 and b not in vus:
            vus.add(b)
            out.append(b)
    return out


def snippets(cs: list[dict]) -> list[tuple[dict, str]]:
    out = []
    for c in cs:
        a = norm(str(c.get("avant", "")))
        a = a[:34].rstrip()
        out.append((c, a if len(a) >= 14 else ""))
    return out


CAT_JUGEMENT = [
    ("coherence_phase_A", r"phase a|liste canonique|<h2>|mot pour mot|réalign|aligné|titre du fichier|titre de"),
    ("affectation_point", r"affect|déplac|transf|mauvais point|point \d+ (?:→|vers)|replac|ventil"),
    ("contradiction", r"contradic|incohér|incompat|discord|divergen"),
]


def classer(c: dict, det: dict, nbefore_txt: str, flagged_norms: dict[str, list[str]]) -> dict:
    """Retourne {detecte: [codes], categorie: str} pour une correction de conformité."""
    A, B = str(c.get("avant", "")), str(c.get("apres", ""))
    sn = norm(A)[:34].rstrip()
    fires = []
    if len(sn) >= 14:
        for code, lst in flagged_norms.items():
            if any(sn in x or (len(x) > 14 and x[:34] in norm(A)) for x in lst):
                fires.append(code)
    # typographie directement sur le texte « avant »
    if AL.RE_NBSP_PONCT.search(A) and False:
        pass
    if re.search(r" [;:?!»%]|« |\d (?:mg|g|kg|µg|mL|ml|mmol|UI|mmHg)\b", A) and re.search(r"[  ]", B):
        fires.append("insecable")
    if re.search(r" [.,](?:\s|$)", A):
        fires.append("espace_avant_point")
    if any(re.search(rx, A) for rx, _ in AL.ABREV_INTERDITES):
        fires.append("abreviation")
    txt = " ".join([str(c.get("point", "")), A, B, str(c.get("lecon", ""))]).lower()
    if c.get("type") == "format":
        cat = "format"
    elif re.match(r"\s*\(?\s*(supprim|passage supprim|paragraphe supprim)", B.strip().lower()) or "doublon" in txt \
            or re.search(r"redit|redite|répét|répète", txt):
        cat = "redite"
    else:
        cat = None
        for nom, rx in CAT_JUGEMENT:
            if re.search(rx, txt):
                cat = nom
                break
        if cat is None:
            if A.count(";") >= 1 and B.count(". ") > A.count(". "):
                cat = "scission_phrase"
            elif re.search(r"\b[A-Z]{2,6}\b", B) and re.search(r"\([^)]*\)", B) and not re.search(r"\([^)]*\)", A):
                cat = "sigle_developpe"
            elif B.strip().lower().startswith(("(supprim", "supprim")):
                cat = "redite"
            else:
                cat = "reformulation"
    return {"detecte": sorted(set(fires)), "categorie": cat}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lots", default="013,014,015,016")
    ap.add_argument("--sortie", default=str(RACINE / FIN / "BANC_ESSAI_LANGUE.json"))
    a = ap.parse_args()
    res = {"fichiers": [], "lots": {}, "agreg": {}}
    cat_tot, cat_det, det_par_code = Counter(), Counter(), Counter()
    med_tot = Counter()
    n_corr = n_det = 0
    for lot in a.lots.split(","):
        L = f"LOT_{lot}"
        cs_all = lire_jsonl(RACINE / FIN / L / "audits" / "corrections.jsonl")
        for c in cs_all:
            if agent_de(c) == "auditeur-medical":
                med_tot[(L, c.get("type"))] += 1
        par_dx = defaultdict(list)
        for c in cs_all:
            if agent_de(c) == "auditeur-conformite":
                m = re.match(r"\s*DX\.(\d{1,2})\b", str(c.get("lecon", "")))
                par_dx[int(m.group(1)) if m else 0].append(c)
        liste = RACINE / FIN / L / "LISTE_DX_CANONIQUE.md"
        if not liste.is_file():
            liste = RACINE / WIP / L / "LISTE_DX_CANONIQUE.md"
        for dx in range(1, 11):
            cs = par_dx.get(dx, [])
            nom = f"{L}_Phase_B_V0_DX.{dx}.html"
            chemins = [f"{WIP}/{L}/{nom}", f"{FIN}/{L}/{nom}"]
            hist = []
            for ch in chemins:
                hist += [(ch, b) for b in blobs_historique(ch)]
            if not hist or not cs:
                res["fichiers"].append({"lot": L, "dx": dx, "ignore": "pas de correction de conformité ou pas d'historique", "n_corr": len(cs)})
                continue
            sn = snippets(cs)
            utiles = [s for _, s in sn if s]
            best, bestscore = None, -1
            for ch, b in hist:
                txt = norm(git("cat-file", "blob", b).decode("utf8", "replace"))
                sc = sum(1 for s in utiles if s in txt)
                if sc >= bestscore:  # à score égal, la version la plus récente
                    best, bestscore = (ch, b, txt), sc
            ch, b, txt_norm = best
            src = git("cat-file", "blob", b).decode("utf8", "replace")
            r = AL.audit(RACINE / ch, str(liste), src=src, nom=nom)
            det = r.pop("details")
            final_src = git("cat-file", "blob", hist[-1][1]).decode("utf8", "replace")
            rf = AL.audit(RACINE / ch, str(liste), src=final_src, nom=nom)
            rf.pop("details")
            flagged = {k: [norm(x) for x in v] for k, v in det.items() if k in ("phrase_longue", "chaine_pv", "phrase_double", "sigle")}
            flagged["phrase_longue"] = [x for x in flagged["phrase_longue"]]
            lignes = []
            for c in cs:
                k = classer(c, det, txt_norm, flagged)
                k["trouve_dans_version"] = bool(len(norm(str(c.get("avant", "")))[:34].rstrip()) >= 14 and norm(str(c.get("avant", "")))[:34].rstrip() in txt_norm)
                lignes.append(k)
            for c, k in zip(cs, lignes):
                cat_tot[k["categorie"]] += 1
                n_corr += 1
                if k["detecte"]:
                    cat_det[k["categorie"]] += 1
                    n_det += 1
                    for code in k["detecte"]:
                        det_par_code[code] += 1
            confiance = bestscore / max(1, len(utiles))
            res["fichiers"].append({
                "lot": L, "dx": dx, "version": b[:10], "confiance_version": round(confiance, 2), "n_corr": len(cs),
                "n_detectees": sum(1 for k in lignes if k["detecte"]),
                "flags_avant": {x["code"]: x["n"] for x in r["avertissements"] + r["critiques"]},
                "flags_final": {x["code"]: x["n"] for x in rf["avertissements"] + rf["critiques"]},
                "critiques_avant": [x["code"] for x in r["critiques"]],
                "octets_avant": r["octets"], "octets_final": rf["octets"],
            })
    ok = [f for f in res["fichiers"] if "ignore" not in f]
    mt = Counter()
    for (L, t), n in med_tot.items():
        mt[t] += n
        res["lots"].setdefault(L, Counter())[t] += n
    res["lots"] = {k: dict(v) for k, v in res["lots"].items()}
    tot_med = sum(mt.values())
    jug = sum(cat_tot[k] for k in ("redite", "coherence_phase_A", "affectation_point", "contradiction"))
    style = cat_tot["reformulation"] + cat_tot["scission_phrase"]
    res["agreg"] = {
        "fichiers_rejoues": len(ok), "fichiers_ignores": len(res["fichiers"]) - len(ok),
        "corrections_conformite": n_corr, "detectees_par_script": n_det,
        "rappel_strict": round(n_det / n_corr, 3) if n_corr else None,
        "par_categorie": {k: {"n": cat_tot[k], "detectees": cat_det[k]} for k in cat_tot},
        "detection_par_controle": dict(det_par_code),
        "part_jugement": round(jug / n_corr, 3) if n_corr else None,
        "part_style_reformulation": round(style / n_corr, 3) if n_corr else None,
        "confiance_version_moyenne": round(sum(f["confiance_version"] for f in ok) / max(1, len(ok)), 2),
        "medical_total": tot_med, "medical_langue_format": mt["langue"] + mt["format"],
        "part_medical_langue_format": round((mt["langue"] + mt["format"]) / tot_med, 3) if tot_med else None,
        "medical_par_type": dict(mt),
    }
    Path(a.sortie).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf8")
    g = res["agreg"]
    print(f"fichiers rejoués {g['fichiers_rejoues']} (ignorés {g['fichiers_ignores']}) ; corrections conformité {n_corr} ; "
          f"détectées par le script {n_det} = {g['rappel_strict']:.1%} ; jugement {g['part_jugement']:.1%} ; "
          f"reformulation/scission {g['part_style_reformulation']:.1%} ; confiance version {g['confiance_version_moyenne']}")
    print("par catégorie :", g["par_categorie"])
    print("médical langue+format :", g["medical_langue_format"], "/", g["medical_total"], f"= {g['part_medical_langue_format']:.1%}")
    print(f"écrit : {a.sortie}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
