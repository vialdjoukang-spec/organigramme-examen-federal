#!/usr/bin/env python3
"""Agent 4 — équipe 2, Partie 2 (DX.3–DX.5), LOT_240–248 — point d'entrée mince vers common/source_engine.py avec la configuration de CET agent uniquement."""
import sys
from pathlib import Path
ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent / "common"))
import source_engine
sys.exit(source_engine.main(ICI / "config.json", sys.argv[1:]))
