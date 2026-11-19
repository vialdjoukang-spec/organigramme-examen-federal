"""Automate déterministe (0 token) d'audit mécanique, de manifeste SHA-256 et de
synchronisation double dépôt pour les 248 LOTs de cours PROFILES 2023 :

1. Dépôt local  : A.__Antigravitty_SSPs_cours/
2. Dépôt GitHub : organigramme-examen-federal/Gemini_Antigravity/

Référentiel appliqué : PROMPT_Alpha_19.11.26.md (calibre 80-100 Ko texte pur,
HTML hors images 80-150 Ko, front-end L1 forme.css/forme.js, fond blanc #fff,
zéro popover/title/script interne, zéro remplissage boilerplate, zéro lacune).
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any

WORKSPACE = Path(__file__).resolve().parents[1]
LOCAL_COURS_DIR = WORKSPACE.parent / "A.__Antigravitty_SSPs_cours"
ORG_REPO_DIR = Path(
    r"C:\Users\viald\.gemini\antigravity\brain\88273131-1dc6-4ff2-9b1c-10d61290375c\scratch\org_repo"
)
GITHUB_GEMINI_DIR = ORG_REPO_DIR / "Gemini_Antigravity"

BOILERPLATE_RE = re.compile(r"(jalon\s+\d+\s+permet\s+de|DX\.\d+\.\d+\s*·)", re.I)
LACUNE_RE = re.compile(r"\b(à vérifier|donnée non trouvée|chiffre non disponible|nom à venir|TODO)\b", re.I)
STYLE_SCRIPT_SVG_RE = re.compile(r"<(?:style|script|svg)\b[^>]*>.*?</(?:style|script|svg)>", re.I | re.S)
IMG_OR_SVG_RE = re.compile(r"<(?:img|svg)\b[^>]*(?:/>|>.*?</svg>)", re.I | re.S)
TAG_RE = re.compile(r"<[^>]+>")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def extract_pure_text(raw_html: str) -> str:
    stripped = STYLE_SCRIPT_SVG_RE.sub(" ", raw_html)
    stripped = TAG_RE.sub(" ", stripped)
    stripped = html.unescape(stripped)
    return re.sub(r"\s+", " ", stripped).strip()


def html_bytes_without_images(raw_html: str) -> int:
    no_imgs = IMG_OR_SVG_RE.sub("", raw_html)
    return len(no_imgs.encode("utf-8"))


def audit_html_file(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    pure_text = extract_pure_text(raw)
    pure_bytes = len(pure_text.encode("utf-8"))
    no_img_bytes = html_bytes_without_images(raw)
    raw_bytes = path.stat().st_size

    has_forme_css = "../_polices/forme.css" in raw or "_polices/forme.css" in raw
    has_forme_js = "../_polices/forme.js" in raw or "_polices/forme.js" in raw
    has_popover = "popover=" in raw or "popovertarget=" in raw
    has_title_attr = bool(re.search(r"<[a-z][^>]*\btitle=", raw, re.I))
    has_inline_script = bool(re.search(r"<script(?![^>]*forme\.js)[^>]*>", raw, re.I))
    has_compendium = bool(re.search(r"\bCompendium(\.ch)?\b", pure_text, re.I))
    boiler_hits = len(BOILERPLATE_RE.findall(pure_text))
    lacune_hits = len(LACUNE_RE.findall(pure_text))
    fen_count = raw.count('class="fenetre') + raw.count("class='fenetre")
    mb_count = raw.count('class="fenetre mb') + raw.count("class='fenetre mb")
    aips_count = len(re.findall(r"#sb-aips-\d+", raw))
    img_count = len(re.findall(r"<img\b", raw, re.I))
    svg_count = len(re.findall(r"<svg\b", raw, re.I))
    has_paire = 'class="paire"' in raw or "class='paire'" in raw

    issues: list[str] = []
    if not has_forme_css or not has_forme_js:
        issues.append("Gabarit forme.css / forme.js manquant")
    if has_popover:
        issues.append("Attribut popover interdit (utiliser :target)")
    if has_title_attr:
        issues.append("Attribut title= interdit")
    if has_inline_script:
        issues.append("Balise <script> propre interdite")
    if has_compendium:
        issues.append("Référence Compendium interdite (AIPS Swissmedic requis)")
    if boiler_hits > 0:
        issues.append(f"Remplissage boilerplate détecté ({boiler_hits} occurrences)")
    if lacune_hits > 0:
        issues.append(f"Formule de lacune interdite dans le HTML ({lacune_hits})")
    if not (80_000 <= pure_bytes <= 100_000):
        issues.append(f"Texte pur hors calibre 80-100 Ko ({pure_bytes} o)")
    if not (80_000 <= no_img_bytes <= 150_000):
        issues.append(f"HTML hors images hors bande 80-150 Ko ({no_img_bytes} o)")
    if fen_count < 3:
        issues.append(f"Fenêtres :target insuffisantes ({fen_count})")

    return {
        "file": path.name,
        "sha256": sha256_file(path),
        "rawBytes": raw_bytes,
        "htmlNoImageBytes": no_img_bytes,
        "pureTextBytes": pure_bytes,
        "fenetreCount": fen_count,
        "mbCount": mb_count,
        "aipsRefs": aips_count,
        "imgCount": img_count,
        "svgCount": svg_count,
        "hasPaire": has_paire,
        "boilerHits": boiler_hits,
        "lacuneHits": lacune_hits,
        "hasCompendium": has_compendium,
        "validAlpha": len(issues) == 0,
        "issues": issues,
    }


def classify_lot_dir(lot_dir: Path) -> dict[str, Any]:
    """Classe sans appel IA un dossier LOT_NNN selon son contenu réel sur disque."""
    if not lot_dir.exists():
        return {"status": "ABSENT", "filesCount": 0, "htmlFiles": []}
    htmls = sorted(lot_dir.glob("*.html"))
    if not htmls:
        return {"status": "ABSENT", "filesCount": 0, "htmlFiles": []}

    # Détection d'un bundle monolithique antérieur (ex. LOT_033_S1.17_complet.html)
    if len(htmls) == 1 and "_complet" in htmls[0].name:
        return {
            "status": "LOT_BUNDLE_MONOLITHIQUE_A_ECLATER",
            "filesCount": 1,
            "htmlFiles": [htmls[0].name],
            "totalBytes": htmls[0].stat().st_size,
        }

    file_audits = [audit_html_file(h) for h in htmls]
    boiler_total = sum(a["boilerHits"] for a in file_audits)
    valid_count = sum(1 for a in file_audits if a["validAlpha"])
    expected_names = {"Phase_A"} | {f"DX.{i}" for i in range(1, 11)}
    found_parts = set()
    for a in file_audits:
        if "Phase_A" in a["file"]:
            found_parts.add("Phase_A")
        m = re.search(r"DX\.(\d+)", a["file"])
        if m:
            found_parts.add(f"DX.{m.group(1)}")

    if boiler_total >= 5:
        status = "PRE_ALPHA_BOILERPLATE_A_REFAIRE"
    elif len(expected_names - found_parts) > 0:
        status = "PARTIEL_A_COMPLETER"
    elif valid_count == len(file_audits) and len(file_audits) >= 11:
        status = "PRET_AUDIT_ALPHA"
    else:
        status = "A_RENFORCER_ALPHA"

    return {
        "status": status,
        "filesCount": len(htmls),
        "validAlphaFiles": valid_count,
        "boilerTotal": boiler_total,
        "htmlFiles": [a["file"] for a in file_audits],
        "audits": file_audits,
    }


def write_lot_manifest(lot_dir: Path) -> Path:
    res = classify_lot_dir(lot_dir)
    manifest = {
        "lot": lot_dir.name,
        "status": res["status"],
        "promptRef": "PROMPT_Alpha_19.11.26",
        "humanMedicalValidation": False,
        "filesCount": res["filesCount"],
        "files": res.get("audits") or [{"file": fn, "sha256": sha256_file(lot_dir / fn)} for fn in res["htmlFiles"]],
    }
    mpath = lot_dir / "MANIFESTE.json"
    mpath.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return mpath


def build_etat_248() -> dict[str, Any]:
    catalog = json.loads((WORKSPACE / "data" / "catalog.json").read_text(encoding="utf-8"))["items"]
    claude_dir = ORG_REPO_DIR / "Claude"
    entries = []
    summary: dict[str, int] = {}

    for idx, item in enumerate(catalog, 1):
        lot_name = f"LOT_{idx:03d}"
        local_lot = LOCAL_COURS_DIR / lot_name
        gh_gemini_lot = GITHUB_GEMINI_DIR / lot_name
        gh_claude_lot = claude_dir / lot_name

        local_cls = classify_lot_dir(local_lot)
        gh_gem_cls = classify_lot_dir(gh_gemini_lot)
        has_claude = gh_claude_lot.exists() and any(gh_claude_lot.glob("*.html"))

        if local_cls["status"] != "ABSENT":
            overall = local_cls["status"]
        elif gh_gem_cls["status"] != "ABSENT":
            overall = gh_gem_cls["status"]
        elif has_claude:
            overall = "CLAUDE_L1_EXISTANT_GITHUB"
        else:
            overall = "ABSENT"

        summary[overall] = summary.get(overall, 0) + 1
        entries.append({
            "lot": idx,
            "lotId": lot_name,
            "ssp": item["code"],
            "titleFr": item.get("fr") or item["title"],
            "overallStatus": overall,
            "localStatus": local_cls["status"],
            "githubGeminiStatus": gh_gem_cls["status"],
            "githubClaudePresent": has_claude,
            "syncedBothRepos": local_cls["status"] == gh_gem_cls["status"] and local_cls["status"] != "ABSENT",
        })

    return {
        "schemaVersion": "1.0.0",
        "promptRef": "PROMPT_Alpha_19.11.26.md",
        "humanMedicalValidation": False,
        "totalLots": len(entries),
        "summary": summary,
        "lots": entries,
    }


def _copy_if_exists(src: Path, dst: Path) -> bool:
    if not src.exists():
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return True


def sync_infra() -> None:
    """Synchronise PROMPT_Alpha_19.11.26.md, _polices/, _outils/ et _harnais/ vers les 2 dépôts."""
    prompt_src = WORKSPACE / "PROMPT_Alpha_19.11.26.md"
    polices_src = ORG_REPO_DIR / "Claude" / "_polices"
    outils_src = ORG_REPO_DIR / "Claude" / "_outils"
    harnais_src = ORG_REPO_DIR / "Claude" / "_harnais"

    useful_outils = [
        "controle3.py", "forme.py", "verif_aips.py", "cliche.py",
        "restaurer_fond.py", "inventaire_images.py", "lecon.py",
    ]
    useful_harnais = [
        "abreviations.py", "aips_fiche.py", "sources_cache.py",
        "extrait.py", "memoire_agent.py", "MEMOIRE_GLOBALE.md",
    ]

    for target_root in (LOCAL_COURS_DIR, GITHUB_GEMINI_DIR):
        target_root.mkdir(parents=True, exist_ok=True)
        _copy_if_exists(prompt_src, target_root / "PROMPT_Alpha_19.11.26.md")

        # _polices/
        pol_dst = target_root / "_polices"
        pol_dst.mkdir(parents=True, exist_ok=True)
        if polices_src.exists():
            for f in polices_src.iterdir():
                if f.is_file():
                    shutil.copy2(f, pol_dst / f.name)

        # _outils/
        out_dst = target_root / "_outils"
        out_dst.mkdir(parents=True, exist_ok=True)
        shutil.copy2(Path(__file__), out_dst / "sync_antigravity_lots.py")
        for fn in useful_outils:
            _copy_if_exists(outils_src / fn, out_dst / fn)
        for fn in useful_harnais:
            if fn.endswith(".py"):
                _copy_if_exists(harnais_src / fn, out_dst / fn)

        # _harnais/
        har_dst = target_root / "_harnais"
        har_dst.mkdir(parents=True, exist_ok=True)
        _copy_if_exists(harnais_src / "MEMOIRE_GLOBALE.md", har_dst / "MEMOIRE_GLOBALE.md")
        _copy_if_exists(harnais_src / "donnees" / "aips_corpus_index.json", har_dst / "aips_corpus_index.json")

    etat = build_etat_248()
    etat_json = json.dumps(etat, ensure_ascii=False, indent=2) + "\n"
    for target_root in (LOCAL_COURS_DIR, GITHUB_GEMINI_DIR):
        (target_root / "_harnais" / "ETAT_FILE_248.json").write_text(etat_json, encoding="utf-8")

    print("Infrastructure synchronisee sur les 2 depots.")
    print("Resume ETAT_FILE_248 :", json.dumps(etat["summary"], ensure_ascii=False))


def sync_lot(lot_num: int) -> int:
    lot_name = f"LOT_{lot_num:03d}"
    local_lot = LOCAL_COURS_DIR / lot_name
    gh_lot = GITHUB_GEMINI_DIR / lot_name

    if local_lot.exists():
        src, dst = local_lot, gh_lot
    elif gh_lot.exists():
        src, dst = gh_lot, local_lot
    else:
        print(f"Erreur : {lot_name} introuvable dans les deux depots.")
        return 1

    write_lot_manifest(src)
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    etat = build_etat_248()
    etat_json = json.dumps(etat, ensure_ascii=False, indent=2) + "\n"
    (LOCAL_COURS_DIR / "_harnais" / "ETAT_FILE_248.json").write_text(etat_json, encoding="utf-8")
    (GITHUB_GEMINI_DIR / "_harnais" / "ETAT_FILE_248.json").write_text(etat_json, encoding="utf-8")
    print(f"{lot_name} synchronise avec MANIFESTE SHA-256 vers les 2 depots.")
    return 0


def clean_check() -> int:
    allowed_top_dirs = {"_polices", "_outils", "_harnais"}
    allowed_top_files = {"PROMPT_Alpha_19.11.26.md"}
    bad: list[str] = []

    for label, root in (("LOCAL", LOCAL_COURS_DIR), ("GITHUB_GEMINI", GITHUB_GEMINI_DIR)):
        if not root.exists():
            bad.append(f"{label}: dossier racine absent")
            continue
        for item in sorted(root.iterdir()):
            if item.is_file():
                if item.name not in allowed_top_files:
                    bad.append(f"{label}: fichier racine non autorise -> {item.name}")
            elif item.is_dir():
                if item.name not in allowed_top_dirs and not re.match(r"^LOT_\d{3}$", item.name):
                    bad.append(f"{label}: dossier non autorise -> {item.name}")
            for sub in root.rglob("*"):
                if sub.is_file() and sub.name in {"bun.lock", "package.json", "server.js", "metadata.json"}:
                    bad.append(f"{label}: fichier parasite -> {sub}")
                if sub.is_file() and sub.suffix.lower() == ".zip":
                    bad.append(f"{label}: archive zip redondante -> {sub}")

    if bad:
        print("ANOMALIES PROPRETE :", "\n".join(bad))
        return 1
    print("PROPRETE CONFIRMEE : uniquement les fichiers concourant aux 248 LOTs dans les 2 depots.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Automatisation double dépôt & contrôle Alpha 19.11.26")
    ap.add_argument("--sync-infra", action="store_true", help="Installer/synchroniser l'infrastructure sur les 2 dépôts")
    ap.add_argument("--sync-lot", type=int, help="Synchroniser un LOT_NNN entre Local et GitHub")
    ap.add_argument("--audit-only", action="store_true", help="Mettre à jour et afficher ETAT_FILE_248.json")
    ap.add_argument("--clean-check", action="store_true", help="Vérifier l'absence de fichiers parasites ou redondants")
    args = ap.parse_args()

    if args.sync_infra:
        sync_infra()
    if args.sync_lot is not None:
        rc = sync_lot(args.sync_lot)
        if rc != 0:
            return rc
    if args.audit_only:
        etat = build_etat_248()
        print(json.dumps(etat["summary"], ensure_ascii=False, indent=2))
    if args.clean_check:
        return clean_check()
    if not any([args.sync_infra, args.sync_lot is not None, args.audit_only, args.clean_check]):
        ap.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
