#!/usr/bin/env python3
"""Automate de recherche catégorie S ; --help pour les options."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.prevalences.moteur import main
if __name__ == '__main__':
    raise SystemExit(main('S'))
