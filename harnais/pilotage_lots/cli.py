#!/usr/bin/env python3
"""Inspecte un instantané Git local ; aucune écriture distante ni ordonnanceur."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from harnais.pilotage_lots.engine import evaluate_lot, validate_state


class GitReader:
    def __init__(self, repository):
        self.repository = repository

    def head(self, branch):
        return subprocess.run(["git", "rev-parse", "--verify", "refs/heads/" + branch + "^{commit}"], cwd=self.repository, check=True, capture_output=True, text=True).stdout.strip()

    def file(self, path, head):
        result = subprocess.run(["git", "show", head + ":" + path], cwd=self.repository, capture_output=True)
        if result.returncode:
            raise FileNotFoundError(path)
        return result.stdout


def collect(reader, state, now):
    validate_state(state)
    jobs = [evaluate_lot(reader, job, now) for job in state["jobs"]]
    return {"checked_at": now.isoformat(), "prompt": "V0", "status": state["status"],
            "stop_requested": state["stop_requested"], "deployment_enabled": state.get("deployment_enabled") is True,
            "may_execute": state["status"] == "active" and not state["stop_requested"] and state.get("deployment_enabled") is True,
            "clinical_validation": False, "automatic_assignment": False, "jobs": jobs,
            "scope": "Contrôle de preuves publiées ; aucune observation des processus GPT ni audit clinique automatique."}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, default=ROOT)
    parser.add_argument("--registry-ref", default="HEAD")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    reader = GitReader(args.repository)
    head = subprocess.run(["git", "rev-parse", "--verify", args.registry_ref + "^{commit}"], cwd=args.repository, check=True, capture_output=True, text=True).stdout.strip()
    state = json.loads(reader.file("harnais/pilotage_lots/etat.json", head))
    result = collect(reader, state, datetime.now(timezone.utc))
    result["registry_head"] = head
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, TypeError, KeyError, OSError, subprocess.SubprocessError) as exc:
        print("Pilotage non vérifiable : " + str(exc), file=sys.stderr)
        raise SystemExit(1)
