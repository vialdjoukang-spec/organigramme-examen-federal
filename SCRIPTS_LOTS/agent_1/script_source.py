#!/usr/bin/env python3
"""Agent 1 (LOT_227–237) — point d'entrée mince vers common/source_engine.py avec la configuration de cet agent."""
import sys
from pathlib import Path
ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent / "common"))
import source_engine
sys.exit(source_engine.main(ICI / "config.json", sys.argv[1:]))
