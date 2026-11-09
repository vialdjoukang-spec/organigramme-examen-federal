#!/usr/bin/env bash
# Surveillance légère toutes les 5 min : `harnais sante` sur l'instance de l'agent (+ état des runs Actions des instances cloud).
# Usage : boucle_sante.sh <instance> [<instance_cloud> …]  — un seul exemplaire par instance (flock).
# Silencieuse : n'écrit ALERTE.json qu'en cas d'échec ; l'agent ne réagit qu'à ce fichier.
set -u
I="$(readlink -f "$1")"; shift; C="$(cd "$(dirname "$(readlink -f "$0")")/../coeur" && pwd)"
exec 9>"$I/sante/.boucle.flock"; flock -n 9 || { echo "boucle déjà active pour $I"; exit 0; }
echo $$ > "$I/sante/boucle.pid"; PERIODE="${HARNAIS_PERIODE_S:-300}"
while true; do
  timeout 240 "$C/bin/harnais" --instance "$I" sante >> "$I/logs/sante_boucle.log" 2>&1 || true
  for X in "$@"; do timeout 60 "$C/bin/harnais" --instance "$(readlink -f "$X")" cloud-etat > /dev/null 2>> "$I/logs/sante_boucle.log" || true; done
  tail -n 2000 "$I/logs/sante_boucle.log" > "$I/logs/.t" 2>/dev/null && mv "$I/logs/.t" "$I/logs/sante_boucle.log"
  sleep "$PERIODE"
done
