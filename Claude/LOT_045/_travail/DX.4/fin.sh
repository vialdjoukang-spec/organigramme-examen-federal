cd /home/user/wt/lot-045
export OUTILS_REF=/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils PAQUET_CACHE=/tmp/claude_paquet_cache
python3 Claude/LOT_045/_travail/DX.4/build.py && python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 045 --cible DX.4 --titre "DX.4 — Asthme et bronchite à éosinophiles" --ex ${1:-6} 2>&1 | grep -v POINT
