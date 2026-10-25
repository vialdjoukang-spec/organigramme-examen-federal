#!/usr/bin/env python3
"""Cumulative Drive × GitHub cross-audit for LOT_001–LOT_248.
Europe/Zurich 2026-10-25. Spies: CSV Drive + Flash inventory + lot/audit branches.
"""
from __future__ import annotations
import csv, json, re, os, collections
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

BASE = Path("/workspace/BASE_LOTS_CUMUL_2026-10-25")
TZ = ZoneInfo("Europe/Zurich")
NOW = datetime.now(TZ).isoformat(timespec="seconds")
PRIOR_DRIVE_43 = {1,2,3,4,5,6,7,8,9,10,105,106,107,108,109,113,211,212,213,214,215,216,217,218,227,228,229,230,231,233,234,235,236,237,238,239,240,241,242,243,244,246,247}

def pct(n, d):
    return 0 if d == 0 else round(100 * n / d)

def parse_titles():
    titles = {}
    # page1 dump
    for path in [
        "/workspace/agent-tools/62af89c1-45df-4e8c-a368-a81a3b6319c8.txt",
        "/workspace/agent-tools/5345a4fc-55f0-4076-845d-78f36776e9e3.txt",
    ]:
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8", errors="replace").read()
        for m in re.finditer(r'"name":\s*"(LOT_(\d{3})\s*—[^"]+)"', text):
            titles[int(m.group(2))] = m.group(1)
    # also from inline page2 we already have in process - ensure 200-248 from second file if present
    # Fallback short titles from situations / tsv
    situ = {}
    if os.path.exists("/workspace/situations.json"):
        situ = {int(k): v for k, v in json.load(open("/workspace/situations.json")).items()}
    if os.path.exists("/tmp/lot_situations.tsv"):
        for line in open("/tmp/lot_situations.tsv"):
            parts = line.strip().split("\t")
            if len(parts) >= 2 and parts[0].startswith("LOT_"):
                situ[int(parts[0].split("_")[1])] = parts[1]
    for i in range(1, 249):
        if i not in titles:
            if i in situ:
                titles[i] = f"LOT_{i:03d} — {situ[i]}"
            else:
                titles[i] = f"LOT_{i:03d}"
    return titles

def drive_chapters_from_csv(row):
    """Map Drive CSV fichiers/statut → A chapters, B chapters, audited flag."""
    fichiers = (row.get("Fichiers présents (Drive)") or "").strip()
    statut = (row.get("Statut") or "").strip()
    # exclude "non audité" false positive
    s_norm = re.sub(r"non\s+audité", "", statut, flags=re.I)
    f_norm = re.sub(r"non\s+audité", "", fichiers, flags=re.I)
    audited = bool(re.search(r"\bAUDITÉ\b", s_norm, re.I) or re.search(r"\bAUDITÉ\b", f_norm, re.I) or statut.upper().startswith("AUDITÉ"))
    # placeholders
    if "A_REDIGER" in statut.upper() or "A_RÉDIGER" in statut.upper() or "_A_REDIGER" in fichiers.upper():
        return 0, 0, False, "placeholder"
    if "À RÉDIGER" in statut or statut.startswith("À RÉDIGER") or "A RÉDIGER" in statut:
        if fichiers in ("-", "",):
            return 0, 0, False, "à_rédiger"
    # explicit complete
    if "5/5" in fichiers or "5/5" in statut or "A/P1/P2/P3/P4" in fichiers:
        return 11, 11, audited, "csv_5/5"
    if "V5 complète" in statut or "ACHEVÉ" in statut:
        return 11, 11, audited, "csv_achevé"
    if audited:
        return 11, 11, True, "csv_audité"
    # partial file tokens
    tokens = set()
    for t in re.split(r"[/\s,]+", fichiers):
        t = t.strip().upper()
        if t:
            tokens.add(t)
    has_a = "A" in tokens or "APPEL_A" in fichiers.upper() or fichiers.upper().startswith("A")
    # (V5) alone often means incomplete V5 marker without file list — treat carefully
    if fichiers == "(V5)":
        # look at statut
        m = re.search(r"\((\d)/5\)", statut)
        if m:
            n = int(m.group(1))
            # n files of A+P1..P4
            a = 11 if n >= 1 else 0
            # remaining as B approx: each of P1-P4 ~ 2.75 chapters → use discrete
            b_parts = max(0, n - 1)
            b = {0: 0, 1: 3, 2: 6, 3: 8, 4: 11}.get(b_parts, 11)
            return a, b, False, f"csv_v5_marker_{n}/5"
        if "incomplète" in statut.lower():
            # try to parse missing
            if "Appel A manquant" in statut:
                return 0, 6, False, "csv_v5_no_A"
            if "P3 manquante" in statut:
                return 11, 8, False, "csv_v5_no_P3"
            if "P2 manquante" in statut:
                return 11, 6, False, "csv_v5_no_P2"
            return 6, 6, False, "csv_v5_incomplète"
        return 0, 0, False, "csv_v5_unknown"
    a = 11 if ("A" in tokens or has_a) else 0
    p_count = sum(1 for p in ("P1", "P2", "P3", "P4") if p in tokens)
    b = {0: 0, 1: 3, 2: 6, 3: 8, 4: 11}.get(p_count, 0)
    # EN COURS (n/5)
    m = re.search(r"\((\d)/5\)", statut)
    if m and a == 0 and b == 0:
        n = int(m.group(1))
        a = 11 if n >= 1 else 0
        b = {0: 0, 1: 0, 2: 3, 3: 6, 4: 8, 5: 11}.get(n, 0)
        if n == 1:
            b = 0
        return a, b, False, f"csv_en_cours_{n}/5"
    if fichiers in ("-", ""):
        return 0, 0, False, "csv_empty"
    return a, b, audited, f"csv_tokens:{fichiers}"

def dx_set_from_filenames(names):
    """Extract DX chapter numbers 1-10 from filenames."""
    dx = set()
    for n in names:
        low = n.lower()
        # DX.1, DX.10, dx1, D1.1 patterns
        for m in re.finditer(r"dx\.?\s*(\d{1,2})", low):
            v = int(m.group(1))
            if 1 <= v <= 10:
                dx.add(v)
        # ranges DX.6_a_DX.7 or DX.8_a_DX.10
        for m in re.finditer(r"dx\.?\s*(\d{1,2})\s*_?a_?_?dx\.?\s*(\d{1,2})", low):
            a, b = int(m.group(1)), int(m.group(2))
            for v in range(min(a, b), max(a, b) + 1):
                if 1 <= v <= 10:
                    dx.add(v)
        # Partie_N with DX ranges already handled
    return dx

def github_from_flash(flash_inv):
    by = collections.defaultdict(list)
    for e in flash_inv:
        by[int(e["lot"])].append(e)
    out = {}
    for lot, ents in by.items():
        files = []
        branches = []
        for e in ents:
            branches.append(e.get("branch"))
            for f in e.get("lot_files") or []:
                files.append(f)
        basenames = [f.split("/")[-1] for f in files]
        has_a = any("appel_a" in b.lower() for b in basenames)
        dx = dx_set_from_filenames(basenames)
        a_ch = 11 if has_a else 0
        b_ch = min(11, len(dx)) if dx else 0
        # If >=4 Appel_B files and no precise DX parse, fall back
        b_files = [b for b in basenames if "appel_b" in b.lower()]
        if b_ch < 11 and len(b_files) >= 4 and len(dx) >= 8:
            b_ch = 11
        if b_ch < 11 and len(dx) >= 10:
            b_ch = 11
        # A-branch often has DX.1-4 and B has DX.5-10 — if both suffixes substantive and has_a and dx covers 10
        suf = {e.get("suffix") for e in ents if e.get("substantive")}
        if has_a and "A" in suf and "B" in suf and len(dx) >= 9:
            b_ch = 11
        if has_a and len(b_files) >= 3 and len(dx) >= 10:
            b_ch = 11
        out[lot] = {
            "a": a_ch,
            "b": b_ch,
            "dx": sorted(dx),
            "files": basenames,
            "branches": branches,
            "evidence": f"flash files={len(basenames)} dx={sorted(dx)} has_a={has_a}",
        }
    return out

def github_from_lot_audit_branches(branch_names, lot_audit_inv=None):
    """lot/LOT_XXX and audit/LOT_XXX imply full A+B when present (V7 delivered)."""
    out = {}
    for name in branch_names:
        m = re.match(r"(audit|lot)/LOT_(\d{3})", name)
        if not m:
            continue
        kind, num = m.group(1), int(m.group(2))
        cur = out.get(num, {"a": 0, "b": 0, "audited": False, "branches": [], "evidence": ""})
        cur["branches"].append(name)
        cur["a"] = 11
        cur["b"] = 11
        if kind == "audit":
            cur["audited"] = True
            cur["evidence"] = f"audit branch {name}"
        else:
            # lot/ = complete delivery, NOT audited
            cur["evidence"] = cur["evidence"] or f"lot branch {name}"
        out[num] = cur
    return out

def label_for(a, b, audited):
    if a >= 11 and b >= 11:
        if audited:
            return "audité"
        return "achevé mais non audité · non édité"
    if a == 0 and b == 0:
        return "à rédiger"
    return "en cours"

def status_bucket(label):
    if label == "audité":
        return "audité"
    if label.startswith("achevé"):
        return "achevé"
    if label == "en cours":
        return "en cours"
    return "à rédiger"

def main():
    titles = parse_titles()
    rows = list(csv.DictReader(open("/workspace/STATUT_LOTS_001_248.csv")))
    assert len(rows) == 248
    flash = json.load(open("/workspace/flash-full-inventory.json"))
    gh_flash = github_from_flash(flash)
    branches = [ln.strip() for ln in open("/tmp/all-branches.txt") if ln.strip()]
    gh_lot = github_from_lot_audit_branches(branches)

    lots = []
    for row in rows:
        n = int(row["LOT"].split("_")[1])
        d_a, d_b, d_aud, d_ev = drive_chapters_from_csv(row)
        g_a = g_b = 0
        g_aud = False
        g_parts = []
        if n in gh_flash:
            g_a = max(g_a, gh_flash[n]["a"])
            g_b = max(g_b, gh_flash[n]["b"])
            g_parts.append(gh_flash[n]["evidence"])
        if n in gh_lot:
            g_a = max(g_a, gh_lot[n]["a"])
            g_b = max(g_b, gh_lot[n]["b"])
            g_aud = g_aud or gh_lot[n].get("audited", False)
            g_parts.append(gh_lot[n]["evidence"])
        # best of both
        a = max(d_a, g_a)
        b = max(d_b, g_b)
        audited = d_aud or g_aud
        # source of best
        drive_score = d_a + d_b
        gh_score = g_a + g_b
        if drive_score > 0 and gh_score > 0:
            source = "both"
        elif gh_score > drive_score:
            source = "GitHub"
        elif drive_score > 0:
            source = "Drive"
        else:
            source = "none"
        # if one source strictly better on a dimension, still both if both contribute
        if (d_a > 0 or d_b > 0) and (g_a > 0 or g_b > 0):
            source = "both"
        elif g_a > 0 or g_b > 0:
            source = "GitHub"
        elif d_a > 0 or d_b > 0:
            source = "Drive"
        else:
            source = "none"
        lab = label_for(a, b, audited)
        title_full = titles.get(n, row["LOT"])
        # short title: FR part after first em-dash
        short = title_full
        if " — " in title_full:
            parts = title_full.split(" — ", 2)
            if len(parts) >= 3:
                short = parts[1] + " — " + parts[2].split(" | ")[0]
            elif len(parts) == 2:
                short = parts[1].split(" | ")[0]
        lots.append({
            "lot": n,
            "lot_id": f"LOT_{n:03d}",
            "title": short.strip(),
            "title_full": title_full,
            "a_chapters": a,
            "b_chapters": b,
            "a_display": f"A {a}/11 ({pct(a,11)}%)",
            "b_display": f"B {b}/11 ({pct(b,11)}%)",
            "combined_22": a + b,
            "combined_pct": pct(a + b, 22),
            "acheve": a >= 11 and b >= 11,
            "audite": audited and a >= 11 and b >= 11,
            "label": lab,
            "status": status_bucket(lab),
            "source": source,
            "drive": {"a": d_a, "b": d_b, "audited": d_aud, "evidence": d_ev,
                      "csv_statut": row["Statut"], "csv_fichiers": row["Fichiers présents (Drive)"],
                      "folder_id": row.get("ID dossier Drive du LOT", "")},
            "github": {"a": g_a, "b": g_b, "audited": g_aud, "evidence": "; ".join(g_parts),
                       "branches": (gh_flash.get(n, {}).get("branches") or []) + (gh_lot.get(n, {}).get("branches") or [])},
        })

    acheves = [L for L in lots if L["acheve"]]
    audites = [L for L in lots if L["audite"]]
    non_aud = [L for L in acheves if not L["audite"]]
    new_vs_43 = sorted(set(L["lot"] for L in acheves) - PRIOR_DRIVE_43)
    lost_vs_43 = sorted(PRIOR_DRIVE_43 - set(L["lot"] for L in acheves))

    summary = {
        "generated_at": NOW,
        "timezone": "Europe/Zurich",
        "denominator": 248,
        "definition": {
            "appel_A": "SSP plan+liste : 10 DD par prévalence décroissante + 1 cours SSP = 11 chapitres",
            "appel_B": "généralement 4 fichiers (ou plus) dont les chapitres DX.1–DX.10 somment à 11",
            "fait": "Appel A = 11/11 ET Appel B = 11/11 (max Drive, GitHub)",
            "label_non_audite": "achevé mais non audité · non édité",
        },
        "count_acheve": len(acheves),
        "count_display": f"{len(acheves)} / 248",
        "count_audite": len(audites),
        "count_acheve_non_audite_non_edite": len(non_aud),
        "lots_acheves": [L["lot"] for L in acheves],
        "lots_audites": [L["lot"] for L in audites],
        "lots_acheves_non_audites_non_edites": [L["lot"] for L in non_aud],
        "new_vs_prior_drive_43": new_vs_43,
        "new_vs_prior_drive_43_count": len(new_vs_43),
        "lost_vs_prior_drive_43": lost_vs_43,
        "spy_method": "Drive: STATUT_LOTS_001_248.csv (fichiers A/P1–P4, V5/V7, AUDITÉ) + titres dossiers LOTS_Finaux. GitHub: flash-full-inventory.json (Appel_A + DX.1–10 sur branches flash A/B) + branches lot/LOT_* et audit/LOT_*. Max(Drive,GitHub) par lot. Pas de téléchargement binaire.",
    }

    # write data
    (BASE / "data").mkdir(parents=True, exist_ok=True)
    payload = {"summary": summary, "lots": lots}
    json.dump(payload, open(BASE / "data/lots_cumul.json", "w"), ensure_ascii=False, indent=2)
    with open(BASE / "data/lots_cumul.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["lot","title","A","B","A_display","B_display","combined","combined_pct","acheve","audite","label","status","source"])
        for L in lots:
            w.writerow([L["lot_id"], L["title"], L["a_chapters"], L["b_chapters"], L["a_display"], L["b_display"],
                        L["combined_22"], L["combined_pct"], int(L["acheve"]), int(L["audite"]), L["label"], L["status"], L["source"]])
    json.dump(summary, open(BASE / "data/summary.json", "w"), ensure_ascii=False, indent=2)
    json.dump(titles, open(BASE / "mirrors/titles_248.json", "w"), ensure_ascii=False, indent=2)

    # markdown table
    md = []
    md.append(f"# État cumulatif Drive × GitHub — LOT_001 à LOT_248\n")
    md.append(f"- Généré : **{NOW}** (Europe/Zurich)\n")
    md.append(f"- Total achevé (A+B) : **{len(acheves)} / 248**\n")
    md.append(f"- Audités : **{len(audites)}** · Achevés non audités · non édités : **{len(non_aud)}**\n")
    md.append(f"- Nouveaux vs Drive-seul 43 : **{len(new_vs_43)}** → {new_vs_43}\n")
    md.append("\n## Table des matières\n")
    md.append("- [Synthèse](#synthèse)\n- [Lots achevés (jaune)](#lots-achevés)\n- [Table complète 001–248](#table-complète)\n")
    md.append("\n## Synthèse\n\n")
    md.append("| Indicateur | Valeur |\n|---|---|\n")
    md.append(f"| Achevés A+B | {len(acheves)} / 248 |\n")
    md.append(f"| Audités | {len(audites)} |\n")
    md.append(f"| Achevé mais non audité · non édité | {len(non_aud)} |\n")
    md.append(f"| En cours | {sum(1 for L in lots if L['status']=='en cours')} |\n")
    md.append(f"| À rédiger | {sum(1 for L in lots if L['status']=='à rédiger')} |\n")
    md.append("\n## Lots achevés\n\n")
    md.append(", ".join(f"{L['lot']:03d}" for L in acheves) + "\n")
    md.append("\n## Table complète\n\n")
    md.append("| Lot | Titre | Chapitres | Statut | Source |\n|---|---|---|---|---|\n")
    for L in lots:
        mark = " ★" if L["acheve"] else ""
        md.append(f"| {L['lot_id']}{mark} | {L['title'][:80]} | {L['a_display']} · {L['b_display']} | {L['label']} | {L['source']} |\n")
    (BASE / "table").mkdir(parents=True, exist_ok=True)
    open(BASE / "table/etat_cumul.md", "w").write("".join(md))

    # HTML
    rows_html = []
    for L in lots:
        cls = "acheve" if L["acheve"] else ("encours" if L["status"]=="en cours" else "todo")
        rows_html.append(
            f"<tr class='{cls}' id='{L['lot_id']}'>"
            f"<td>{L['lot_id']}</td>"
            f"<td>{html_esc(L['title'])}</td>"
            f"<td>{L['a_display']} · {L['b_display']}<br><small>{L['combined_22']}/22 ({L['combined_pct']}%)</small></td>"
            f"<td>{html_esc(L['label'])}</td>"
            f"<td>{L['source']}</td></tr>"
        )
    toc = " · ".join(f"<a href='#{L['lot_id']}'>{L['lot']:03d}</a>" for L in acheves)
    html = f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"/>
<title>État cumulatif LOT_001–248 — {NOW}</title>
<style>
body{{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;margin:24px;color:#111;line-height:1.35}}
h1,h2{{margin:0.6em 0 0.3em}}
.meta{{color:#444;margin-bottom:1em}}
table{{border-collapse:collapse;width:100%;font-size:13px}}
th,td{{border:1px solid #ccc;padding:6px 8px;vertical-align:top}}
th{{background:#222;color:#fff;position:sticky;top:0}}
tr.acheve{{background:#FFE600 !important}} /* bright yellow */
tr.acheve td{{font-weight:600}}
tr.encours{{background:#FFF8DC}}
tr.todo{{background:#fafafa}}
.badge{{display:inline-block;background:#FFE600;padding:2px 8px;border-radius:4px;font-weight:700}}
.toc{{font-size:12px;margin:8px 0 16px;line-height:1.8}}
summary{{cursor:pointer}}
</style></head><body>
<h1>État cumulatif Drive × GitHub — LOT_001 à LOT_248</h1>
<p class="meta">Généré le {NOW} (Europe/Zurich). Définition : Appel A = 11 chapitres (10 DD + cours SSP) · Appel B = 11 chapitres (DX.1–10). Achevé = A et B à 11/11. Max(Drive, GitHub).</p>
<p><span class="badge">{len(acheves)} / 248 achevés</span>
 &nbsp; Audités : <b>{len(audites)}</b>
 &nbsp; Non audités · non édités : <b>{len(non_aud)}</b>
 &nbsp; Nouveaux vs Drive-seul 43 : <b>{len(new_vs_43)}</b></p>
<details open><summary><b>Table des matières — lots achevés (jaune)</b></summary>
<div class="toc">{toc}</div></details>
<h2>Table complète</h2>
<table>
<thead><tr><th>Lot</th><th>Titre officiel</th><th>Chapitres (A · B)</th><th>Statut</th><th>Source</th></tr></thead>
<tbody>
{''.join(rows_html)}
</tbody></table>
<h2>Méthode espions</h2>
<p>{html_esc(summary['spy_method'])}</p>
<p>Nouveaux lots vs recensement Drive-seul 43 : {html_esc(str(new_vs_43))}</p>
</body></html>"""
    open(BASE / "table/etat_cumul.html", "w").write(html)
    open("/workspace/etat_cumul.html", "w").write(html)

    # README
    readme = f"""# BASE_LOTS_CUMUL_2026-10-25

Passation cumulative Drive × GitHub pour les 248 SSP (LOT_001–LOT_248).

## Résultat

- **{len(acheves)} / 248** lots achevés (Appel A + Appel B)
- Audités : {len(audites)}
- Achevé mais non audité · non édité : {len(non_aud)}
- Nouveaux vs Drive-seul (43) : {len(new_vs_43)} → {new_vs_43}

## Définition

- **Appel A** : plan + liste SSP, 10 diagnostics différentiels par prévalence décroissante + 1 cours SSP = **11 chapitres**
- **Appel B** : généralement 4 fichiers (ou plus) couvrant DX.1–DX.10 = **11 chapitres**
- **Fait / achevé** : A=11/11 **et** B=11/11, en prenant le **max** entre Drive et GitHub
- Label si achevé non audité : `achevé mais non audité · non édité`

## Contenu

| Chemin | Rôle |
|---|---|
| `data/lots_cumul.json` | État machine-readable complet |
| `data/lots_cumul.csv` | Table plate |
| `data/summary.json` | Synthèse compteurs |
| `table/etat_cumul.md` | Table markdown |
| `table/etat_cumul.html` | Table HTML (jaune vif sur achevés) |
| `table/etat_cumul.pdf` | PDF pour prévisualisation Drive |
| `spies/build_cumul.py` | Script de reconstruction |
| `mirrors/` | Titres et pointeurs légers |

## Comment continuer

1. Relire `data/summary.json` et `data/lots_cumul.json`.
2. Pour un lot « en cours », regarder `drive.csv_fichiers` et `github.branches`.
3. Ne **pas** fusionner les PR Flash sans audit (chevauchement V7-Tunder).
4. Mettre à jour en relançant `python3 spies/build_cumul.py` après refresh CSV / inventaire Flash.
5. Drive parent LOTS_Finaux : `1DaFAd0uamsJQY2NH0ocuy2bhpfcVk9Vu`.

Généré : {NOW} Europe/Zurich.
"""
    open(BASE / "README.md", "w").write(readme)
    print(json.dumps(summary, ensure_ascii=False, indent=2))

def html_esc(s):
    return (s or "").replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

if __name__ == "__main__":
    main()
