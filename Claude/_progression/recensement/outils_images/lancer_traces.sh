#!/bin/bash
# Tracés EXP : passe 1 (index locaux + Europe PMC, 4 fils), passe 2 (Commons, séquentielle), puis planche.
cd "$(dirname "$0")"
python3 chercher_traces.py --sans-commons --fils 4
python3 chercher_traces.py --complement
python3 chercher_traces.py --complement
python3 chercher_traces.py --planche
python3 chercher_traces.py --stats
