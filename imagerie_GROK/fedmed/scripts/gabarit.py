"""Gabarit obligatoire des fenêtres, lu par reinjecter.py."""
from pathlib import Path

ICI = Path(__file__).resolve().parent
JS = (ICI / "viewer.js").read_text(encoding="utf-8")
CSS = (ICI / "viewer.css").read_text(encoding="utf-8")
