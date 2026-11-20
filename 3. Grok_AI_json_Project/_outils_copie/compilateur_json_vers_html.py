#!/usr/bin/env python3
"""COMPILATEUR_JSON_VERS_HTML.PY — Compilateur déterministe (0 token IA)
SSP_nnn/source_json/*.json -> LOT_nnn_*.html + SSP_nnn_<code>_UNIQUE.html.

Règles absolues :
- Police Atkinson Hyperlegible (via forme.css)
- Zéro arbre décisionnel (.fm-canvas)
- Modales centrées <div class="fen"> + 2 onglets PK/PD SVG (via pkpd_transform)
- Infobulles Why bleu paillette (<span class="why" data-why="...">)
- Signature IA fixe (#signature-ia) juste avant </body>
"""
from __future__ import annotations

import html as H
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(BASE, "_outils")
SCRATCH = r"C:\Users\viald\.gemini\antigravity\brain\e9cc0e6b-d793-463e-9feb-4f3c095c5839\scratch"
sys.path.insert(0, TOOLS)
sys.path.insert(0, SCRATCH)

import assembler_unique as au  # noqa: E402
import pkpd_transform as pt  # noqa: E402
from optimiser_ssp import NON_BLUE_PAL, optimise_ssp  # noqa: E402

SIG_FINAL = (
    '<div id="signature-ia" style="position:fixed;right:12px;bottom:10px;z-index:9999;'
    'background:#fff;border:2px solid #000;padding:4px 10px;font:700 12px/1.3 Arial,sans-serif;'
    'text-transform:uppercase;color:#000">'
    '<div>DÉBUT : 2026-11-21 00:10 (EUROPE/ZURICH) · MODÈLE : GEMINI 4 NEON (MEDIUM) · PLATEFORME : ANTIGRAVITY</div>'
    '</div>'
)


def _why_span(term: str, tip: str) -> str:
    safe_tip = H.escape(str(tip).replace(">", "supérieur à").replace("<", "inférieur à"), quote=True)
    return f'<span class="why" data-why="{safe_tip}">{H.escape(str(term))}</span>'


def _build_pkpd_modal(prefix: str, idx: int, drug: dict) -> tuple[str, str]:
    key = re.sub(r"[^a-z0-9]+", "-", str(drug.get("nom", f"med-{idx}")).lower()).strip("-") or f"med-{idx}"
    mid = f"f-{prefix}-m-{key}"
    title = str(drug.get("titre") or drug.get("nom") or f"Médicament {idx}")
    target = str(drug.get("cible_moleculaire") or drug.get("cible") or "Cible pharmacologique spécifique")
    pk_rows = drug.get("pharmacocinetique") or drug.get("pk_rows") or []
    pd_rows = drug.get("pharmacodynamique") or drug.get("pd_rows") or []

    def _rows_html(rows):
        out = []
        for r in rows:
            if isinstance(r, dict):
                k = r.get("parametre") or r.get("cle") or r.get("titre") or ""
                v = r.get("valeur") or r.get("detail") or r.get("texte") or ""
            elif isinstance(r, (list, tuple)) and len(r) >= 2:
                k, v = r[0], r[1]
            else:
                k, v = "Repère", str(r)
            out.append(f"<tr><th>{H.escape(str(k))}</th><td>{H.escape(str(v))}</td></tr>")
        return "".join(out)

    raw = (
        f'<section class="fenetre mb" id="{mid}" role="dialog" aria-label="{H.escape(title)}">'
        f'<div class="fen"><a class="fermer" href="#">Fermer ✕</a>'
        f'<h4>{H.escape(title)}</h4>'
        f'<h5>1 · Pharmacocinétique</h5>'
        f'<div class="t"><table><tbody>{_rows_html(pk_rows)}</tbody></table></div>'
        f'<h5>2 · Pharmacodynamique &amp; Clinique</h5>'
        f'<div class="t"><table><tbody>{_rows_html(pd_rows)}</tbody></table></div>'
        f'</div></section>'
    )
    modal_html = pt.transform_one_mb(raw).replace("<span>Cible moléculaire spécifique</span>", f"<span>{H.escape(target)}</span>")
    chip = f'<a class="ouvre med-chip" href="#{mid}">{H.escape(title.split(" — ")[0])}</a>'
    return chip, modal_html


def compile_one_json(ssp_num: int, json_path: str, dx_idx: int, entites: list[dict], out_dir: str) -> str:
    data = json.load(open(json_path, encoding="utf-8"))
    meta = data.get("meta") or {}
    code = str(meta.get("code_profiles") or meta.get("code") or f"SSP_{ssp_num:03d}")
    circuit = str(meta.get("circuit") or "MONOGRAPHIQUE").upper()
    nom = str(meta.get("titre") or meta.get("nom") or f"Cours {dx_idx}")
    cim = str(meta.get("cim") or code)
    urgence = str(meta.get("urgence") or "clinique")
    p = "pa" if dx_idx == 0 else f"dx{dx_idx}"
    fname = f"LOT_{ssp_num:03d}_Phase_A_V0.html" if dx_idx == 0 else f"LOT_{ssp_num:03d}_Phase_B_V0_DX.{dx_idx}.html"
    accent = NON_BLUE_PAL[(ssp_num + dx_idx) % len(NON_BLUE_PAL)]

    # PK/PD modals
    chips, modals = [], []
    for i, d in enumerate(data.get("fiches_pkpd") or [], 1):
        ch, mh = _build_pkpd_modal(p, i, d)
        chips.append(ch)
        modals.append(mh)

    # Why tooltips indexed by section
    why_by_sec: dict[int, list[dict]] = {}
    for w in data.get("infobulles_why") or []:
        if isinstance(w, dict):
            sec = int(w.get("section") or w.get("point") or 1)
            why_by_sec.setdefault(sec, []).append(w)

    sections = data.get("sections") or []
    barre_links = "".join(
        f'<a href="#{p}-p{s.get("point", i)}"><b>{s.get("point", i)}</b>{H.escape(str(s.get("titre", ""))[:22])}</a>'
        for i, s in enumerate(sections, 1)
    )

    sec_blocks = []
    for i, s in enumerate(sections, 1):
        num = int(s.get("point") or i)
        stitle = str(s.get("titre") or f"Point {num}")
        paras = [f"<p>{H.escape(str(t))}</p>" for t in (s.get("paragraphes") or [])]
        pts = s.get("points_cles") or []
        if pts:
            paras.append("<ul>" + "".join(f"<li>{H.escape(str(t))}</li>" for t in pts) + "</ul>")
        whys = why_by_sec.get(num, [])
        if whys:
            badges = " · ".join(_why_span(w.get("terme", "Repère ✦"), w.get("explication", "")) for w in whys)
            paras.append(f"<p><strong>Repères clés :</strong> {badges}</p>")
        if num == 11 and chips:
            paras.append(f"<p>Fiches pharmacologiques PK/PD à deux onglets : {', '.join(chips)}.</p>")
        if num == 14:
            for q_idx, q in enumerate(data.get("vignettes_qcm") or [], 1):
                if isinstance(q, dict):
                    opts = "".join(f"<li>{H.escape(str(o))}</li>" for o in (q.get("options") or []))
                    paras.append(
                        f'<div class="qcm"><h4>Vignette {q_idx} — {H.escape(str(q.get("titre", "")))}</h4>'
                        f'<p>{H.escape(str(q.get("enonce", "")))}</p>'
                        f'<ul>{opts}</ul>'
                        f'<p><strong>{H.escape(str(q.get("reponse_justifiee", "")))}</strong></p></div>'
                    )
        sec_blocks.append(
            f'    <section class="point" id="{p}-p{num}">\n'
            f'      <h3>{num}. {H.escape(stitle)}</h3>\n'
            f'      {"".join(paras)}\n'
            f'    </section>'
        )

    # Tables -> modals
    for t_idx, tbl in enumerate(data.get("tableaux_cliniques") or [], 1):
        if not isinstance(tbl, dict):
            continue
        tid = f"f-{p}-tbl-{t_idx}"
        cap = str(tbl.get("titre") or f"Tableau clinique {t_idx}")
        cols = tbl.get("colonnes") or []
        rows = tbl.get("lignes") or []
        th = "".join(f"<th>{H.escape(str(c))}</th>" for c in cols)
        tb = "".join("<tr>" + "".join(f"<td>{H.escape(str(cell))}</td>" for cell in r) + "</tr>" for r in rows)
        modals.append(
            f'<section class="fenetre fm-tab-fen" id="{tid}" role="dialog" aria-label="{H.escape(cap)}">'
            f'<div class="fen"><a class="fermer" href="#">Fermer ✕</a><h4>{H.escape(cap)}</h4>'
            f'<div class="t"><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div></div></section>'
        )

    bib_items = []
    for s_idx, src in enumerate(data.get("sources_suisses") or [], 1):
        if isinstance(src, dict):
            sid = str(src.get("id") or f"src-{s_idx}")
            txt = f"{src.get('organisation', '')} — {src.get('titre', '')} ({src.get('date', '')})"
        else:
            sid, txt = f"src-{s_idx}", str(src)
        bib_items.append(f'<li id="sb-{H.escape(sid)}">{H.escape(txt)}</li>')

    html_doc = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="ssp-circuit" content="{H.escape(circuit)}">
  <title>{H.escape(code)} — {H.escape(nom)}</title>
  <link id="forme-vial" rel="stylesheet" href="../../_polices/forme.css">
  <script src="../../_polices/forme.js" defer></script>
</head>
<body style="--fm-a:{accent};--fm-a-mid:{accent};--fm-a-pale:#fdf7f6;--fm-a-doux:#f7e8e6" data-theme="med">
  <nav id="brain-barre14" aria-label="Plan du cours">
    {barre_links}
    <a href="#{p}-sources"><b>§</b>Sources</a>
  </nav>
  <header id="fm-bandeau">
    <div class="fm-code"><span>{H.escape(code)}</span><span class="fm-phase">Circuit {H.escape(circuit)} · CIM {H.escape(cim)} · Urgence : {H.escape(urgence)}</span></div>
    <div class="fm-nom">{H.escape(nom)}</div>
  </header>
  <main>
    <h2 class="fm-double">{H.escape(nom)} ({H.escape(cim)})</h2>
{chr(10).join(sec_blocks)}
{chr(10).join(modals)}
    <section class="ilot" id="{p}-sources">
      <h3>Sources</h3>
      <ol>{''.join(bib_items)}</ol>
    </section>
  </main>
  {SIG_FINAL}
  <!-- FIN_FICHIER {fname[:-5]} -->
</body>
</html>
"""
    out_path = os.path.join(out_dir, fname)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_doc)
    return out_path


def compile_ssp(n: int) -> None:
    ssp_dir = os.path.join(BASE, f"SSP_{n:03d}")
    sj_dir = os.path.join(ssp_dir, "source_json")
    src_dir = os.path.join(ssp_dir, "_sources")
    os.makedirs(src_dir, exist_ok=True)
    nj_path = os.path.join(src_dir, "NOTIONS.json")
    if not os.path.exists(nj_path):
        nj_path = os.path.join(ssp_dir, "NOTIONS.json")
    nj = json.load(open(nj_path, encoding="utf-8"))
    entites = nj["entites"]

    count = 0
    for idx in range(0, len(entites) + 1):
        jfn = "Phase_A.json" if idx == 0 else f"DX.{idx}.json"
        jp = os.path.join(sj_dir, jfn)
        if os.path.exists(jp):
            compile_one_json(n, jp, idx, entites, src_dir)
            count += 1
    optimise_ssp(n)
    au.un(n)
    print(f"SSP_{n:03d}: {count} fichiers JSON compilés -> HTML + UNIQUE.html")


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        compile_ssp(int(arg))
