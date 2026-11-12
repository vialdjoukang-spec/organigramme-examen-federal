#!/usr/bin/env bash
# VEILLE_HARNAIS — boucle locale gratuite (zéro modèle) : toutes les 10 min, régénère MEMOIRE.md des LOT actifs,
# la progression des agents, le modèle de consommation, Le_Gaspillon (alertes) et l'index du second cerveau.
# Auto-contrôle : chaque script en échec est consigné dans donnees/veille.log (le dispositif se surveille lui-même).
# Lancement : nohup bash Claude/_harnais/veille_harnais.sh 23 24 25 &
# Chaque worktree LOT est lu sur place (/home/user/wt/r-0NN) ; rien n'est commité par la veille.
H=$(cd "$(dirname "$0")" && pwd)
while true; do
  for n in "$@"; do w=/home/user/wt/r-$(printf %03d "$n"); [ -d "$w" ] && (cd "$w" && python3 "$H/resumeur.py" "$n" >/dev/null 2>&1); done
  for s in "suivi.py" "modele.py" "gaspillon.py" "cerveau.py index"; do
    (cd "$H/../.." && python3 Claude/_harnais/$s >/dev/null 2>>"$H/donnees/veille.log") \
      || echo "$(date -Is) ECHEC $s" >> "$H/donnees/veille.log"
  done
  [ -f "$HOME/.claude/hooks/verrou_medina.py" ] || echo "$(date -Is) ALERTE verrou MEDINA absent" >> "$H/donnees/veille.log"
  sleep 600
done
