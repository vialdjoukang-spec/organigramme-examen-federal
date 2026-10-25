#!/usr/bin/env python3
"""carburant_v0 — met à jour PROMPT ULTIME V0 via injections déclaratives.

Usage:
  python3 carburant_v0.py            # applique les injections, scrub anti-IA, régénère PDF
  python3 carburant_v0.py --list     # liste les injections
  python3 carburant_v0.py --dry-run  # montre le diff sans écrire
  python3 carburant_v0.py --push     # après apply : commit+push PR #447 (branche cursor/prompt-ultime-v0)

Aucune mention d'IA dans le prompt produit.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MD_PATH = ROOT / "PROMPT_ULTIME_PRODUCTION_LOTS_V0.md"
PDF_PATH = ROOT / "PROMPT_ULTIME_PRODUCTION_LOTS_V0.pdf"
INJECTIONS_PATH = ROOT / "carburant_v0_injections.json"
BUILD_PY = Path("/workspace/inv-dd/prompt-v0/_build/build.py")
MIRROR_DIR = Path("/workspace/inv-dd/prompt-v0")
WORKTREE = Path("/workspace/wt-prompt-casern")
BRANCH = "cursor/prompt-ultime-v0"
PR_HINT = "https://github.com/vialdjoukang-spec/organigramme-examen-federal/pull/447"

# Patterns anti-IA (case-insensitive). Le prompt ne doit en contenir aucun.
AI_PATTERNS = [
    r"\bIA\b",
    r"\bI\.A\.\b",
    r"\bLLM\b",
    r"\bGPT\b",
    r"\bChatGPT\b",
    r"\bClaude\b",
    r"\bGrok\b",
    r"\bOpenAI\b",
    r"\bAnthropic\b",
    r"\bGemini\b",
    r"\bCopilot\b",
    r"intelligence artificielle",
    r"modèle de langage",
    r"agent (?:IA|LLM|GPT)",
    r"prompt (?:système|system)",
]


def load_injections() -> list[dict]:
    data = json.loads(INJECTIONS_PATH.read_text(encoding="utf-8"))
    return data.get("injections", [])


def find_blockquote_end(md: str, start: int) -> int:
    """Retourne l'index juste après le bloc quote markdown qui commence à start."""
    # start pointe au début d'une ligne « > ... »
    i = start
    n = len(md)
    while i < n:
        # avance jusqu'à fin de ligne
        nl = md.find("\n", i)
        if nl < 0:
            return n
        line = md[i : nl + 1]
        if line.startswith(">") or line.strip() == "":
            # blank line inside blockquote ends it in CommonMark if next isn't >
            if line.strip() == "":
                # peek next non-empty
                j = nl + 1
                while j < n and md[j] == "\n":
                    j += 1
                if j >= n or not md[j:].startswith(">"):
                    return nl + 1
            i = nl + 1
            continue
        return i
    return n


def apply_insert_after_block(md: str, inj: dict) -> tuple[str, str]:
    needle = inj["anchor_contains"]
    skip = inj.get("skip_if_contains")
    if skip and skip in md:
        return md, f"SKIP {inj['id']} (déjà présent)"
    idx = md.find(needle)
    if idx < 0:
        return md, f"FAIL {inj['id']} : ancre introuvable"
    # remonter au début de la ligne
    line_start = md.rfind("\n", 0, idx) + 1
    end = find_blockquote_end(md, line_start)
    text = inj["text"]
    if not text.endswith("\n"):
        text += "\n"
    # s'assurer d'une ligne vide entre blocs
    insert = "\n" + text
    if md[end : end + 1] == "\n":
        new_md = md[:end] + insert + md[end:]
    else:
        new_md = md[:end] + "\n" + insert + md[end:]
    return new_md, f"OK {inj['id']} : insert_after_block @ {line_start}"


def apply_replace_line_matching(md: str, inj: dict) -> tuple[str, str]:
    skip = inj.get("skip_if_contains")
    # Pour meta-date : skip si la nouvelle phrase « filtre de qualité » est déjà dans la ligne Date
    pattern = re.compile(inj["anchor_regex"], re.M)
    m = pattern.search(md)
    if not m:
        return md, f"FAIL {inj['id']} : regex sans match"
    if skip and skip in m.group(0):
        return md, f"SKIP {inj['id']} (déjà présent)"
    text = inj["text"]
    if not text.endswith("\n"):
        text += "\n"
    new_md = md[: m.start()] + text + md[m.end() :]
    # si match ne consomme pas le \n final de la ligne
    if m.group(0).endswith("\n") and text.endswith("\n"):
        pass
    elif not m.group(0).endswith("\n") and md[m.end() : m.end() + 1] == "\n":
        # remplacer sans manger le \n suivant ; text a déjà \n → ok si on ne double pas
        if text.endswith("\n") and md[m.end() : m.end() + 1] == "\n":
            new_md = md[: m.start()] + text.rstrip("\n") + md[m.end() :]
    return new_md, f"OK {inj['id']} : replace_line_matching"


APPLIERS = {
    "insert_after_block": apply_insert_after_block,
    "replace_line_matching": apply_replace_line_matching,
}


def apply_all(md: str, injections: list[dict], only_active: bool = True) -> tuple[str, list[str]]:
    reports = []
    out = md
    for inj in injections:
        if only_active and not inj.get("active", True):
            reports.append(f"OFF {inj['id']}")
            continue
        mode = inj["mode"]
        fn = APPLIERS.get(mode)
        if not fn:
            reports.append(f"FAIL {inj['id']} : mode inconnu {mode}")
            continue
        out, msg = fn(out, inj)
        reports.append(msg)
    return out, reports


def scrub_anti_ia(md: str) -> list[str]:
    hits = []
    for pat in AI_PATTERNS:
        for m in re.finditer(pat, md, flags=re.I):
            # contexte ligne
            line_start = md.rfind("\n", 0, m.start()) + 1
            line_end = md.find("\n", m.end())
            if line_end < 0:
                line_end = len(md)
            line = md[line_start:line_end].strip()
            hits.append(f"L~{md[: m.start()].count(chr(10))+1}: /{pat}/ → {line[:120]}")
    return hits


def build_pdf() -> None:
    if not BUILD_PY.is_file():
        raise SystemExit(f"build.py introuvable : {BUILD_PY}")
    # sync mirror MD first so build paths stay consistent
    MIRROR_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(MD_PATH, MIRROR_DIR / MD_PATH.name)
    env = os.environ.copy()
    r = subprocess.run(
        [sys.executable, str(BUILD_PY)],
        cwd=str(BUILD_PY.parent),
        env=env,
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        sys.stderr.write(r.stdout + "\n" + r.stderr)
        raise SystemExit(f"build PDF échoué (code {r.returncode})")
    # mirror PDF
    if PDF_PATH.is_file():
        shutil.copy2(PDF_PATH, MIRROR_DIR / PDF_PATH.name)
    print(r.stdout.strip() or "pdf ok")


def sync_worktree() -> None:
    dest = WORKTREE / "PROMPT_Casern"
    if not dest.is_dir():
        print(f"WARN worktree absent : {WORKTREE}")
        return
    dest.mkdir(parents=True, exist_ok=True)
    for name in (
        MD_PATH.name,
        PDF_PATH.name,
        "carburant_v0.py",
        "carburant_v0_injections.json",
    ):
        src = ROOT / name
        if src.is_file():
            shutil.copy2(src, dest / name)
    # mirror script too
    shutil.copy2(ROOT / "carburant_v0.py", MIRROR_DIR / "carburant_v0.py")
    shutil.copy2(INJECTIONS_PATH, MIRROR_DIR / "carburant_v0_injections.json")


def push_pr() -> None:
    if not WORKTREE.is_dir():
        raise SystemExit(f"worktree manquant : {WORKTREE}")
    sync_worktree()
    cmds = [
        ["git", "status", "-sb"],
        ["git", "add", "PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V0.md",
         "PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V0.pdf",
         "PROMPT_Casern/carburant_v0.py",
         "PROMPT_Casern/carburant_v0_injections.json"],
        ["git", "commit", "-m",
         "Prompt V0: filtre de qualité (pas plafond d’ambition); carburant_v0"],
        ["git", "push", "-u", "origin", "HEAD"],
    ]
    for c in cmds:
        print("+", " ".join(c))
        r = subprocess.run(c, cwd=str(WORKTREE), capture_output=True, text=True)
        sys.stdout.write(r.stdout)
        sys.stderr.write(r.stderr)
        if r.returncode != 0 and c[1] != "commit":
            # commit peut échouer si rien à committer
            if "nothing to commit" in (r.stdout + r.stderr):
                print("rien à committer")
                continue
            raise SystemExit(f"git {' '.join(c[1:])} échoué")
        if r.returncode != 0 and "nothing to commit" in (r.stdout + r.stderr):
            print("rien à committer")
    print(f"PR (sans merge) : {PR_HINT}")


def cmd_list() -> None:
    for inj in load_injections():
        flag = "ON " if inj.get("active", True) else "OFF"
        print(f"{flag}  {inj['id']}  [{inj['mode']}]  {inj.get('section','')}")


def main() -> int:
    ap = argparse.ArgumentParser(description="carburant à V0 — injections PROMPT ULTIME V0")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--push", action="store_true", help="commit+push branche PR #447 après apply")
    ap.add_argument("--no-pdf", action="store_true")
    args = ap.parse_args()

    if args.list:
        cmd_list()
        return 0

    if not MD_PATH.is_file():
        raise SystemExit(f"MD introuvable : {MD_PATH}")
    if not INJECTIONS_PATH.is_file():
        raise SystemExit(f"injections introuvables : {INJECTIONS_PATH}")

    original = MD_PATH.read_text(encoding="utf-8")
    injections = load_injections()
    new_md, reports = apply_all(original, injections)
    for r in reports:
        print(r)

    hits = scrub_anti_ia(new_md)
    if hits:
        print("ANTI-IA FAIL :")
        for h in hits:
            print(" ", h)
        return 2
    print("ANTI-IA OK (0 hit)")

    if args.dry_run:
        if new_md == original:
            print("dry-run : aucun changement")
        else:
            # mini diff stats
            print(f"dry-run : {len(original)} → {len(new_md)} octets ({len(new_md)-len(original):+d})")
            # show new obsession line if present
            for line in new_md.splitlines():
                if "filtre de qualité, pas un plafond d’ambition" in line:
                    print("PREVIEW:", line[:200])
                    break
        return 0

    MD_PATH.write_text(new_md, encoding="utf-8")
    print(f"écrit : {MD_PATH} ({len(new_md)} octets)")

    if not args.no_pdf:
        build_pdf()
        print(f"PDF : {PDF_PATH} ({PDF_PATH.stat().st_size if PDF_PATH.is_file() else 0} octets)")

    sync_worktree()
    print(f"miroirs : {MIRROR_DIR} ; worktree {WORKTREE}/PROMPT_Casern")

    if args.push:
        push_pr()

    print("--- rapport ---")
    print(f"MD  : {MD_PATH}")
    print(f"PDF : {PDF_PATH}")
    print(f"inj : {INJECTIONS_PATH}")
    print(f"script : {Path(__file__).resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
