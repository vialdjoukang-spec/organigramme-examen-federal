#!/bin/bash
# pousser_lecon.sh LOT CIBLE "message" : commit + push d'une seule leçon (HTML + _travail/<CIBLE> + HELP) sur claude/lot-LOT
set -e
L=$1; C=$2; M=$3
cd /home/user/wt/lot-$L
if [ "$C" = "PA" ]; then H=Claude/LOT_$L/LOT_${L}_Phase_A_V0.html; else H=Claude/LOT_$L/LOT_${L}_Phase_B_V0_$C.html; fi
git add "$H" "Claude/LOT_$L/_travail/$C"
git commit -q -m "LOT_$L $C — $M

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01JErHPsz6iGRK59YaJbKkbs"
for i in 1 2 3 4; do git push -q -u origin claude/lot-$L 2>&1 | grep -v '^remote:' && break; sleep $((2**i)); done
git log --oneline -1
