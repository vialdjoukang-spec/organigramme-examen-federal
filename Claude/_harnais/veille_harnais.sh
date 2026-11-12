#!/usr/bin/env bash
# VEILLE_HARNAIS — boucle locale gratuite (zéro modèle) : toutes les 10 min, régénère MEMOIRE.md des LOT actifs,
# la progression des agents et le modèle de consommation. Lancement : nohup bash Claude/_harnais/veille_harnais.sh 23 24 25 &
# Chaque worktree LOT est lu sur place (/home/user/wt/r-0NN) ; rien n'est commité par la veille.
H=$(cd "$(dirname "$0")" && pwd)
while true; do
  for n in "$@"; do w=/home/user/wt/r-$(printf %03d "$n"); [ -d "$w" ] && (cd "$w" && python3 "$H/resumeur.py" "$n" >/dev/null 2>&1); done
  (cd "$H/../.." && python3 Claude/_harnais/suivi.py >/dev/null 2>&1 && python3 Claude/_harnais/modele.py >/dev/null 2>&1)
  sleep 600
done
