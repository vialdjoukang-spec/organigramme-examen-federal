#!/bin/bash
# Passe 1 (index locaux + Europe PMC), puis passe 2 (Commons, lente à cause des 429), puis planche.
cd "$(dirname "$0")"
python3 chercher.py --de IMG-042 --a IMG-344 --sans-commons
python3 chercher.py --de IMG-042 --a IMG-344 --complement
python3 chercher.py --de IMG-042 --a IMG-344 --complement
python3 planche.py
