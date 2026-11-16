#!/bin/bash
cd /home/user/wt/lot-047
export PAQUET_CACHE=/tmp/claude_paquet_cache
(cd Claude/LOT_047/_travail/PA && python3 expand.py) || exit 1
python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 047 --cible PA --titre "LOT_047 — S2.8 — Brûlures rétrosternales (pyrosis)" --ex ${1:-4} 2>&1 | cut -c1-${2:-600}
