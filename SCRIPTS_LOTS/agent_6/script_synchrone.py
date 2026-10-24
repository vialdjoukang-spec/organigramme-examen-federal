#!/usr/bin/env python3
"""Agent 6 — équipe 2, Partie 3 (DX.6–DX.7), LOT_240–248 — point d'entrée mince vers common/sync_reviewer.py avec la configuration de CET agent uniquement."""
import sys
from pathlib import Path
ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent / "common"))
import sync_reviewer
sys.exit(sync_reviewer.main(ICI / "config.json", sys.argv[1:]))
