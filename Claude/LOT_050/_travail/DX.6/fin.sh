cd /home/user/wt/lot-050; export PAQUET_CACHE=/tmp/claude_paquet_cache
(cd Claude/LOT_050/_travail/DX.6 && python3 build.py) >/dev/null
python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 050 --cible DX.6 --titre "DX.6 — Flutter atrial" --ex 6 2>&1 | cut -c1-900
