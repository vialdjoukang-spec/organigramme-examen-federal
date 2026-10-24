#!/usr/bin/env python3
"""Agent 2 — équipe 2, Appel A + Partie 1 (DX.1–DX.2), LOT_238–248 — point d'entrée mince vers common/sync_reviewer.py avec la configuration de CET agent uniquement."""
import sys
from pathlib import Path
ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent / "common"))
import sync_reviewer
sys.exit(sync_reviewer.main(ICI / "config.json", sys.argv[1:]))
