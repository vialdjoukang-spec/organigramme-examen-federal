cd /home/user/wt/lot-046
export OUTILS_REF=/tmp/claude-0/-home-user/15c9849e-78d1-5a00-9dcf-bd21b180736d/scratchpad/ref/outils PAQUET_CACHE=/tmp/claude_paquet_cache
(cd Claude/LOT_046/_travail/DX.6 && python3 build.py)
python3 /home/user/organigramme-examen-federal/Claude/_outils/lecon.py finir --lot 046 --cible DX.6 --titre "DX.6 — Syndrome coronarien aigu" --ex ${1:-6} | grep -v '^$'
