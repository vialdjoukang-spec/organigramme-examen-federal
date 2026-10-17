#!/usr/bin/env bash
# Veille de relance permanente (gratuite) : détecte la fin de l'étape courante et relance Codex
# avec l'ordre de Vial « continue avec l'étape suivante ». Ne s'arrête jamais sur un obstacle.
#
# Deux modes de relance :
#   A. Codex CLI présent (`codex` dans le PATH) : `codex exec --full-auto -C <dépôt> [-m modèle] "<ordre>"`
#      en arrière-plan, un seul à la fois (verrou), journal dans .etat_local/codex_exec.log.
#      Modèle des étapes répétitives : $MODELE_REPETITIF (défaut gpt-6-luna, ordre de Vial « GPT 6 Luna ») ;
#      s'il est refusé, relance sans -m (modèle par défaut) et le note dans ETAT.md.
#   B. Sans Codex CLI (Codex web, IDE, cloud) : l'ordre est écrit dans PROCHAINE_ACTION.md, que Codex
#      lit au début de chaque session (AGENTS.md l'impose).
#
# À chaque passage : 1) file de fusion (tools/file_fusion.sh) ; 2) critère de fin automatique de l'étape
# (tools/porte.py critere) ; 3) si l'étape est terminée → porte.py avancer + relance ; 4) si l'étape est en
# cours mais qu'aucun Codex ne tourne et qu'ETAT.json n'a pas bougé depuis $INACTIF_MIN minutes → relance
# « reprends l'étape N ».
#
# Usage : tools/veille_relance.sh [--une-fois | --boucle [SECONDES]] [--dry-run] [--sans-fusion] [--sans-codex]
#   cron (toutes les 3 min) : */3 * * * * cd /chemin/du/depot && bash tools/veille_relance.sh --une-fois
#   boucle                  : nohup bash tools/veille_relance.sh --boucle 180 >/dev/null 2>&1 &
set -uo pipefail
RACINE="${OEF_REPO:-$(cd "$(dirname "$0")/.." && pwd)}"
export OEF_REPO="$RACINE"
LOCAL="$RACINE/.etat_local"; mkdir -p "$LOCAL"
JOURNAL="$LOCAL/veille_relance.log"
MODELE_REPETITIF="${MODELE_REPETITIF:-gpt-6-luna}"
INACTIF_MIN="${INACTIF_MIN:-20}"
MODE="une"; PAUSE=180; DRY=0; FUSION=1; CODEX=1
while [ $# -gt 0 ]; do
  case "$1" in
    --une-fois) MODE="une" ;;
    --boucle) MODE="boucle"; case "${2:-}" in ''|--*) ;; *) PAUSE="$2"; shift ;; esac ;;
    --dry-run) DRY=1 ;; --sans-fusion) FUSION=0 ;; --sans-codex) CODEX=0 ;;
    -h|--help) sed -n '2,22p' "$0"; exit 0 ;;
    *) echo "option inconnue : $1" >&2; exit 64 ;;
  esac; shift
done
DRYOPT=""; [ "$DRY" = 1 ] && DRYOPT="--dry-run"
log() { local l; l="$(date '+%Y-%m-%d %H:%M:%S %Z') · $*"; echo "[veille] $l" >&2; [ "$DRY" = 1 ] || echo "$l" >> "$JOURNAL"; }
champ() { python3 -c "import json,sys;print(json.load(open('$RACINE/ETAT.json')).get('$1',''))" 2>/dev/null; }
modele_etape() { python3 - "$RACINE" "$1" <<'PY' 2>/dev/null
import json, sys
for e in json.load(open(sys.argv[1] + "/tools/etapes.json", encoding="utf-8"))["etapes"]:
    if e["n"] == int(sys.argv[2]):
        print(e.get("modele", "defaut"))
PY
}
codex_actif() { pgrep -f '(^|/)codex exec( |$)' >/dev/null 2>&1; }

ecrire_prochaine() { # $1 = ordre
  local f="$RACINE/PROCHAINE_ACTION.md"
  if [ "$DRY" = 1 ]; then log "[dry-run] PROCHAINE_ACTION.md ← $1"; return; fi
  {
    echo "# PROCHAINE ACTION (écrit par tools/veille_relance.sh, ne pas éditer à la main)"
    echo
    echo "Mis à jour : $(date '+%d.%m.%Y %H:%M %Z')"
    echo
    echo "> $1"
    echo
    echo "État : \`$(cat "$RACINE/ETAT.json" 2>/dev/null | tr -d '\n')\`"
    echo
    echo "Échecs de fusion récents (journal/echecs_fusion.md) :"
    echo
    tail -n 5 "$RACINE/journal/echecs_fusion.md" 2>/dev/null | grep '^- ' || echo "- aucun"
    if [ -f "$RACINE/CATALOGUE.md" ]; then
      printf '\n---\n\n'
      cat "$RACINE/CATALOGUE.md"
    fi
  } > "$f"
}

relancer() { # $1 = ordre, $2 = numéro d'étape
  ecrire_prochaine "$1"
  if [ "$CODEX" = 0 ] || ! command -v codex >/dev/null 2>&1; then
    log "mode B (sans Codex CLI) : ordre écrit dans PROCHAINE_ACTION.md"; return
  fi
  if codex_actif; then log "Codex tourne déjà : pas de seconde session"; return; fi
  local mod; mod="$(modele_etape "$2")"
  if [ "$DRY" = 1 ]; then log "[dry-run] codex exec --full-auto -C $RACINE ${mod/luna/-m $MODELE_REPETITIF} \"$1\""; return; fi
  (
    exec 9>"$LOCAL/codex.lock"; flock -n 9 || exit 0
    if [ "$mod" = "luna" ]; then
      codex exec --full-auto -C "$RACINE" -m "$MODELE_REPETITIF" "$1" >> "$LOCAL/codex_exec.log" 2>&1 && exit 0
      if tail -n 30 "$LOCAL/codex_exec.log" | grep -qiE "model.*(not (found|available|supported)|unknown|invalid|does not exist)"; then
        echo "- $(date '+%d.%m.%Y %H:%M %Z') · modèle $MODELE_REPETITIF refusé : étape $2 relancée avec le modèle le moins cher disponible (défaut de Codex)." >> "$RACINE/ETAT.md"
        codex exec --full-auto -C "$RACINE" ${MODELE_SECOURS:+-m "$MODELE_SECOURS"} "$1" >> "$LOCAL/codex_exec.log" 2>&1
      fi
    else
      codex exec --full-auto -C "$RACINE" "$1" >> "$LOCAL/codex_exec.log" 2>&1
    fi
  ) &
  log "mode A : codex exec lancé (étape $2, modèle ${mod})"
}

passage() {
  git -C "$RACINE" fetch -q origin 2>/dev/null || log "git fetch impossible (réseau) : on continue"
  if [ "$FUSION" = 1 ]; then bash "$RACINE/tools/file_fusion.sh" $DRYOPT >> "$LOCAL/file_fusion.log" 2>&1 || log "file_fusion a échoué : on continue"; fi
  local n statut
  n="$(champ etape_courante)"; statut="$(champ statut)"
  [ -n "$n" ] || { log "ETAT.json illisible : réinitialisé à l'étape 0"; [ "$DRY" = 1 ] || echo '{"etape_courante":0,"statut":"en_cours","lot":1}' > "$RACINE/ETAT.json"; n=0; statut=en_cours; }
  if [ "$statut" = "en_cours" ] && python3 "$RACINE/tools/porte.py" critere "$n" >/dev/null 2>&1; then
    log "critère de fin de l'étape $n atteint"
    python3 "$RACINE/tools/porte.py" terminer $DRYOPT >/dev/null 2>&1; statut="terminee"
  fi
  if [ "$statut" = "terminee" ]; then
    local ordre
    ordre="$(python3 "$RACINE/tools/porte.py" avancer $DRYOPT 2>/dev/null | tail -n 1)"
    [ "$DRY" = 1 ] || n="$(champ etape_courante)"
    if [ "$n" -ge 1 ] && ! python3 "$RACINE/tools/porte.py" verifier0 >/dev/null 2>&1; then
      ordre="Ordre de Vial : l'Étape 0 n'est pas complète. Termine l'Étape 0 de CONTINUATION.md (python3 tools/porte.py verifier0) avant tout contenu."
    fi
    log "étape terminée → $ordre"; relancer "$ordre" "$n"; return
  fi
  # Étape en cours : relance si personne ne travaille depuis INACTIF_MIN minutes.
  local age=999999
  [ -f "$RACINE/ETAT.json" ] && age=$(( ( $(date +%s) - $(stat -c %Y "$RACINE/ETAT.json") ) / 60 ))
  if ! codex_actif && [ "$age" -ge "$INACTIF_MIN" ]; then
    local o; o="$(python3 "$RACINE/tools/porte.py" ordre 2>/dev/null)"
    o="${o/continue avec l\'étape suivante/reprends l\'étape en cours}"
    log "étape $n en cours, inactive depuis ${age} min → relance"; relancer "$o" "$n"
    [ "$DRY" = 1 ] || touch "$RACINE/ETAT.json"
  else
    log "étape $n en cours (dernière activité il y a ${age} min)"
  fi
}

if [ "$MODE" = "boucle" ]; then
  log "veille démarrée (boucle, ${PAUSE} s)"
  while true; do passage; sleep "$PAUSE"; done
else
  passage
fi
exit 0
