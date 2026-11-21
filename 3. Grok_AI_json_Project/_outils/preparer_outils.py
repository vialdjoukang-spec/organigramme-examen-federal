#!/usr/bin/env python3
"""preparer_outils.py — à lancer UNE fois : décompresse cartographie_DATA.json.gz."""
import gzip, os, shutil
d = os.path.dirname(os.path.abspath(__file__))
gz = os.path.join(d, "cartographie_DATA.json.gz")
out = os.path.join(d, "cartographie_DATA.json")
if os.path.exists(gz) and not os.path.exists(out):
    with gzip.open(gz, "rb") as a, open(out, "wb") as b:
        shutil.copyfileobj(a, b)
print("Outils prêts.")
