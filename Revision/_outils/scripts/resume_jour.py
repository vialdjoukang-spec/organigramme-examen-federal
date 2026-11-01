#!/usr/bin/env python3
"""Résumé dynamique du travail Revision / QCM / Flash du jour (Europe/Zurich).
Usage: python3 resume_jour.py [--write] [--json]
Régénère Revision/RESUME_JOUR.md et met à jour les % dans ETAT_DES_LIEUX_QCM.md si présent.
"""
from __future__ import annotations
import argparse, csv, json, re, subprocess
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Europe/Zurich")
ROOT = Path("/workspace/grok")
REV = ROOT / "Revision"
G_DIR = REV / "G_symptomes_generaux"
MAP = {
    "G01": ("LOT_001", "Transpiration anormale"),
    "G02": ("LOT_002", "Tuméfaction / adénopathie"),
    "G03": ("LOT_003", "Soif excessive / polydipsie"),
    "G04": ("LOT_004", "Fatigue, lassitude"),
    "G05": ("LOT_005", "Sensation de maladie"),
    "G06": ("LOT_006", "Fièvre, frissons, hyperthermie"),
    "G07": ("LOT_007", "Bouffées vasomotrices (flush)"),
    "G08": ("LOT_008", "Hypothermie"),
    "G09": ("LOT_009", "Prurit"),
    "G10": ("LOT_010", "Douleurs de tous types"),
    "G11": ("LOT_011", "Troubles du sommeil"),
    "G12": ("LOT_012", "Œdème diffus ou localisé"),
    "G13": ("LOT_013", "Décès non naturel"),
    "G14": ("LOT_014", "Décès inattendu / mort subite"),
    "G15": ("LOT_015", "Prise de poids, obésité"),
    "G16": ("LOT_016", "Perte de poids / appétit"),
}

def now():
    return datetime.now(TZ)

def find_ssp_dirs():
    if not G_DIR.exists():
        return []
    return sorted([p for p in G_DIR.iterdir() if p.is_dir() and re.match(r"G\d{2}_", p.name)])

def load_json_bank(d: Path):
    js = list(d.glob("*_TypeA_Reflexe.json")) + list(d.glob("*TypeA*.json"))
    for j in js:
        try:
            return json.loads(j.read_text(encoding="utf-8")), j
        except Exception:
            continue
    return None, None

def stats_from_bank(data):
    if not data:
        return None
    qs = data.get("questions") or (data if isinstance(data, list) else [])
    if isinstance(data, dict) and "questions" in data:
        qs = data["questions"]
    n = len(qs)
    niv = Counter((q.get("niveau") or q.get("niv") or "?").lower() for q in qs)
    return {
        "n": n,
        "ex": niv.get("examen", 0) + niv.get("ex", 0),
        "ap": niv.get("approfondissement", 0) + niv.get("ap", 0),
        "spe": niv.get("specialiste", 0) + niv.get("spe", 0),
        "statut": (data.get("qualite") or {}).get("statut") if isinstance(data, dict) else None
            or data.get("statut") if isinstance(data, dict) else "revue_auto",
    }

def git_head():
    repo = ROOT / "repo"
    try:
        out = subprocess.check_output(
            ["git", "-C", str(repo), "rev-parse", "--short", "HEAD"],
            text=True, stderr=subprocess.DEVNULL,
        ).strip()
        br = subprocess.check_output(
            ["git", "-C", str(repo), "rev-parse", "--abbrev-ref", "HEAD"],
            text=True, stderr=subprocess.DEVNULL,
        ).strip()
        return br, out
    except Exception:
        return "?", "?"

def scan():
    rows = []
    for code, (lot, titre) in MAP.items():
        dirs = [p for p in find_ssp_dirs() if p.name.startswith(code)]
        if not dirs:
            rows.append({"code": code, "lot": lot, "titre": titre, "statut": "absent", "n": 0, "ex": 0, "ap": 0, "spe": 0, "html": None})
            continue
        d = dirs[0]
        data, jp = load_json_bank(d)
        st = stats_from_bank(data) or {"n": 0, "ex": 0, "ap": 0, "spe": 0, "statut": "brouillon"}
        htmls = list(d.glob("*_TypeA_Reflexe.html"))
        statut = "revue_auto" if htmls and st["n"] else ("brouillon" if (htmls or jp) else "absent")
        if st.get("statut"):
            statut = st["statut"] if st["n"] else statut
        rows.append({
            "code": code, "lot": lot, "titre": titre, "statut": statut,
            "n": st["n"], "ex": st["ex"], "ap": st["ap"], "spe": st["spe"],
            "html": str(htmls[0].relative_to(REV)) if htmls else None,
            "dir": d.name,
        })
    return rows

def pct(rows):
    # 1 SSP avec HTML+n_q>0 = prêt
    ready = sum(1 for r in rows if r["n"] > 0 and r["html"])
    return ready, len(rows), round(100 * ready / len(rows), 1) if rows else 0.0

def deliverables_today():
    items = []
    for path, label in [
        (ROOT / "STRATEGIE_QCM_EXAMEN_CH.md", "Stratégie QCM examen CH"),
        (ROOT / "EVALUATION_MEDICAL_LANGUE_LOT_001_248.html", "Évaluation médicale/langue 001–248"),
        (REV / "ETAT_DES_LIEUX_QCM.md", "État des lieux QCM"),
        (REV / "README.md", "README Revision"),
        (REV / "_outils" / "PEDAGOGIE_PREPARATION_SANS_COMPARAISON.md", "Architecture « Préparation sans comparaison »"),
        (REV / "_outils" / "CHARTE_REDACTION.md", "Charte de rédaction QCM Type A"),
        (REV / "_outils" / "PROFIL_GRAND_MAITRE_BITUNDER.md", "Profil Grand Maître Professeur Bitunder"),
    ]:
        if path.exists():
            items.append(f"- `{path.relative_to(ROOT) if path.is_relative_to(ROOT) else path}` — {label}")
    for h in sorted((REV / "G_symptomes_generaux").glob("G*_*/*Reflexe.html")) if (REV / "G_symptomes_generaux").exists() else []:
        items.append(f"- `{h.relative_to(ROOT)}` — {h.parent.name[:3]} Type A Réflexe (+ JSON, COUVERTURE_DD.md, CHANGELOG.md)")
    for path, label in [
        (ROOT / "STRATEGIE_QCM_EXAMEN_CH.html", "Stratégie QCM (HTML)"), (ROOT / "STRATEGIE_QCM_EXAMEN_CH.pdf", "Stratégie QCM (PDF)"),
        (ROOT / "EVALUATION_MEDICAL_LANGUE_LOT_001_248.json", "Évaluation (JSON)"), (ROOT / "EVALUATION_MEDICAL_LANGUE_LOT_001_248.pdf", "Évaluation (PDF)"),
        (ROOT / "QCM-banque" / "LOT_001" / "README_POINTEUR.md", "Pointeur QCM-banque → Revision/G01"),
        (REV / "_index" / "MAP_G1_G16.json", "Carte G1–G16 (DX par SSP)"),
        (REV / "_outils" / "scripts" / "build_ssp.py", "Build générique SSP"),
        (REV / "_outils" / "scripts" / "etat_lieux.py", "État des lieux + REGISTRE"),
    ]:
        if path.exists():
            items.append(f"- `{path.relative_to(ROOT)}` — {label}")
    return items

def render_md(rows):
    ready, total, p = pct(rows)
    br, hd = git_head()
    ts = now().strftime("%Y-%m-%d %H:%M Europe/Zurich")
    lines = [
        f"# Résumé du jour — Revision QCM",
        f"",
        f"*Généré dynamiquement le {ts} par `Revision/_outils/scripts/resume_jour.py`.*",
        f"",
        f"## Progression G1–G16",
        f"",
        f"**{ready}/{total} SSP prêts ({p} %)** · branche locale repo `{br}` @ `{hd}`",
        f"",
        f"| SSP | LOT | Titre | Statut | Q | EX | AP | SPE | HTML |",
        f"|-----|-----|-------|--------|---|----|----|-----|------|",
    ]
    for r in rows:
        html = r["html"] or "—"
        lines.append(
            f"| {r['code']} | {r['lot']} | {r['titre'][:40]} | {r['statut']} | {r['n']} | {r['ex']} | {r['ap']} | {r['spe']} | `{html}` |"
        )
    lines += [
        "",
        "## Livrables détectés (jour / Revision)",
        "",
    ]
    lines += deliverables_today() or ["- (aucun fichier marqueur encore)"]
    lines += [
        "",
        "## Relève Λ",
        "",
        f"- Progression globale G : **{p} %** ({ready}/{total}).",
        f"- Prochain SSP absent : **{next((r['code'] for r in rows if r['n']==0), '—')}** · détail couverture DD et blockers : `ETAT_DES_LIEUX_QCM.md`.",
        f"- Contraintes : GitHub only (jamais Drive) ; pas de PR/merge/main/force-push sans ordre Vial.",
        "",
        "## Prêt à pousser (CloudAgent)",
        "",
        "- Cible : `vialdjoukang-spec/organigramme-examen-federal`, branche **`grok/revision`** — jamais Drive, jamais force-push, jamais `main`, pas de PR.",
        "- À synchroniser dans le dépôt : `Revision/` entier (sans `__pycache__/`, sans `_print.html`) ; `QCM-banque/LOT_001/README_POINTEUR.md` ; `STRATEGIE_QCM_EXAMEN_CH.{md,html,pdf}` ; `EVALUATION_MEDICAL_LANGUE_LOT_001_248.{html,json,pdf}` ; script résumé dynamique `Revision/_outils/scripts/resume_jour.py`.",
        "- Source de vérité : `/workspace/grok/Revision` (la copie `repo/Revision` @ HEAD local est plus ancienne : G1 v2, pas de G2).",
        "",
        "## Commandes",
        "",
        "```bash",
        "python3 /workspace/grok/Revision/_outils/scripts/resume_jour.py --write",
        "python3 /workspace/grok/Revision/_outils/scripts/etat_lieux.py  # si présent",
        "```",
        "",
    ]
    return "\n".join(lines), {"ready": ready, "total": total, "pct": p, "rows": rows, "ts": ts}

def write_registre(rows):
    path = REV / "_index" / "REGISTRE.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ssp","lot","titre","n_q","ex","ap","spe","statut","chemin_html","maj"])
        w.writeheader()
        ts = now().isoformat(timespec="minutes")
        for r in rows:
            w.writerow({
                "ssp": r["code"], "lot": r["lot"], "titre": r["titre"],
                "n_q": r["n"], "ex": r["ex"], "ap": r["ap"], "spe": r["spe"],
                "statut": r["statut"], "chemin_html": r["html"] or "", "maj": ts,
            })

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    rows = scan()
    md, meta = render_md(rows)
    if args.json:
        print(json.dumps(meta, ensure_ascii=False, indent=2))
    else:
        print(md)
    if args.write:
        REV.mkdir(parents=True, exist_ok=True)
        (REV / "RESUME_JOUR.md").write_text(md, encoding="utf-8")
        full = REV / "_outils" / "scripts" / "etat_lieux.py"
        if full.exists():  # l'état des lieux complet (couverture DD, REGISTRE détaillé) fait foi
            subprocess.run(["python3", str(full)], check=False)
            print(f"\n→ écrit {REV/'RESUME_JOUR.md'} ; ETAT_DES_LIEUX_QCM.md + REGISTRE.csv par etat_lieux.py", flush=True)
            return
        write_registre(rows)
        # sync short etat
        etat = [
            f"# État des lieux QCM — G1–G16",
            f"",
            f"*Maj {meta['ts']} — voir aussi RESUME_JOUR.md*",
            f"",
            f"**Progression : {meta['pct']} %** ({meta['ready']}/{meta['total']} SSP avec banque HTML).",
            f"",
            f"Détail : généré par `resume_jour.py --write`.",
            f"",
            f"## Relève Λ",
            f"- % G1–G16 : **{meta['pct']}**",
            f"- Prochain : {next((r['code']+' '+r['titre'] for r in rows if r['n']==0), 'file G complète')}",
            f"- GitHub : `grok/revision` (jamais Drive)",
            f"",
        ]
        (REV / "ETAT_DES_LIEUX_QCM.md").write_text("\n".join(etat), encoding="utf-8")
        print(f"\n→ écrit {REV/'RESUME_JOUR.md'} et ETAT_DES_LIEUX_QCM.md", flush=True)

if __name__ == "__main__":
    main()
