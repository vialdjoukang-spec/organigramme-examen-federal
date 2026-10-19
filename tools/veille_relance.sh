#!/usr/bin/env bash
# Veille de relance locale : relance Codex sur la mission enregistrée
# avec l'ordre de Vial « continue avec l'étape suivante ». Ne s'arrête jamais sur un obstacle.
#
# Deux modes de relance :
#   A. Codex CLI présent (`codex` dans le PATH) : `codex exec -s workspace-write -C <dépôt> [-m modèle] "<ordre>"`
#      en arrière-plan, un seul à la fois (verrou), journal dans .etat_local/codex_exec.log.
#      Modèle des étapes répétitives : $MODELE_REPETITIF (défaut gpt-6-luna, ordre de Vial « GPT 6 Luna ») ;
#      s'il est refusé, relance sans -m (modèle par défaut) et le note dans ETAT.md.
#   B. Sans Codex CLI (Codex web, IDE, cloud) : l'ordre est écrit dans PROCHAINE_ACTION.md, que Codex
#      lit au début de chaque session (AGENTS.md l'impose).
#
# À chaque passage : activité/baux, état/mission ; si le lot est terminé ou si l'étape est en
# cours mais qu'aucun responsable/CI/Codex n'est actif et qu'ETAT.json n'a pas bougé depuis120s → relance
# « reprends l'étape N ».
#
# Le relanceur ne modifie pas ETAT.json et ne fusionne aucune autre chaîne.
# Usage : tools/veille_relance.sh [--une-fois | --boucle [SECONDES]] [--dry-run] [--sans-fusion] [--sans-codex]
#   boucle : nohup bash tools/veille_relance.sh --boucle 120 --sans-fusion >.etat_local/relance.log 2>&1 &
#   Requiert un accès réseau autorisé à Codex et une authentification fonctionnelle.
set -uo pipefail
RACINE="${OEF_REPO:-$(cd "$(dirname "$0")/.." && pwd)}"
export OEF_REPO="$RACINE"
LOCAL="$RACINE/.etat_local"; mkdir -p "$LOCAL"
JOURNAL="$LOCAL/veille_relance.log"
MODELE_REPETITIF="${MODELE_REPETITIF:-gpt-6-luna}"
if [ -z "${INACTIF_SECONDES:-}" ]; then
  [[ "${INACTIF_MIN:-2}" =~ ^[1-9][0-9]*$ ]] || { echo "durée invalide" >&2; exit 64; }
  INACTIF_SECONDES=$(( ${INACTIF_MIN:-2} * 60 ))
fi
MODE="une"; PAUSE=120; DRY=0; CODEX=1
while [ $# -gt 0 ]; do
  case "$1" in
    --une-fois) MODE="une" ;;
    --boucle) MODE="boucle"; case "${2:-}" in ''|--*) ;; *) PAUSE="$2"; shift ;; esac ;;
    --dry-run) DRY=1 ;; --sans-fusion) : ;; --sans-codex) CODEX=0 ;;
    -h|--help) sed -n '2,22p' "$0"; exit 0 ;;
    *) echo "option inconnue : $1" >&2; exit 64 ;;
  esac; shift
done
for nombre in "$PAUSE" "$INACTIF_SECONDES"; do
  [[ "$nombre" =~ ^[1-9][0-9]*$ ]] || { echo "durée invalide : $nombre" >&2; exit 64; }
done
# Un seul relanceur par checkout, y compris deux invocations --une-fois simultanées.
exec 8>"$LOCAL/relance_worker.lock"
flock -n 8 || exit 0
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

activite_partagee() {
  python3 "$RACINE/tools/garde/relance_bail.py" observer
}

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
    printf '%s\n' 'Règle prototypes · Vial (18.10.2026) : « pour la suite tu devras te fier à la science plus à moi ». Source CH/UE lue et datée puis contre-audit, sans redemander R13 déjà autorisé ni prétendre à une validation médicale humaine. `chronologie_version: 1` exige `bilan_ordre` et `pec_ordre` : afficher la référence puis le bilan ordonné (premier texte = `exp_premier`, il remplace les anciens champs redondants), puis les phases PEC ; garder `dia` une fois après le bilan. Les urgences commencent sans attendre un examen de confirmation. Les fiches legacy sans chronologie gardent leur rendu ; ne pas leur fabriquer d’ordre.'
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
  if [ "$CODEX" = 0 ] || ! command -v codex >/dev/null 2>&1; then
    ecrire_prochaine "$1"
    log "mode B (sans Codex CLI) : ordre écrit dans PROCHAINE_ACTION.md"; return
  fi
  if codex_actif; then log "Codex tourne déjà : pas de seconde session"; return; fi
  local mod; mod="$(modele_etape "$2")"
  if [ "$DRY" = 1 ]; then log "[dry-run] codex exec -s workspace-write -C $RACINE (étape $2, modèle $mod)"; return; fi
  (
    exec 9>"$LOCAL/codex.lock"; flock -n 9 || exit 0
    # Une tentative est un événement technique, jamais une activité clinique.
    local maintenant precedent=0 code reservation tentative=''
    maintenant="$(date +%s)"
    if [ -f "$LOCAL/derniere_tentative" ]; then read -r precedent < "$LOCAL/derniere_tentative"; fi
    [[ "$precedent" =~ ^[0-9]+$ ]] || precedent=0
    if [ $((maintenant - precedent)) -lt 120 ]; then log "tentative précédente <120s : pas de doublon"; exit 0; fi
    # Réserver avant toute écriture et avant le lancement, entre checkouts et machines.
    reservation="$(python3 "$RACINE/tools/garde/relance_bail.py" reserver)" || { log "réservation distante refusée : pas de lancement"; exit 0; }
    trap '[ -z "$tentative" ] || rm -f "$tentative"; python3 "$RACINE/tools/garde/relance_bail.py" --owner "$reservation" liberer >/dev/null 2>&1 || true' EXIT
    printf '%s\n' "$maintenant" > "$LOCAL/derniere_tentative"
    ecrire_prochaine "$1"
    tentative="$(mktemp "$LOCAL/tentative.XXXXXX")"
    local ordre_execution="$1 Déclare ton activité réelle avec le bail d’agent $reservation (tools/garde/permanence.py --github-state --agent $reservation --lease-seconds 180), puis rafraîchis-le pendant le travail réel. La mission exclusive infobulles reste prioritaire ; ne reprends aucun chantier suspendu."
    log "processus Codex démarré (étape $2, modèle $mod) ; reprise utile non encore prouvée"
    if [ "$mod" = "luna" ]; then
      python3 "$RACINE/tools/garde/relance_bail.py" --owner "$reservation" executer -- codex exec -c 'approval_policy="never"' -s workspace-write -C "$RACINE" -m "$MODELE_REPETITIF" "$ordre_execution" </dev/null > "$tentative" 2>&1
      code=$?
      cat "$tentative" >> "$LOCAL/codex_exec.log"
      [ "$code" = 0 ] && { log "processus Codex terminé, code0 ; résultat à contrôler"; exit 0; }
      if grep -qiE "model.*(not (found|available|supported)|unknown|invalid|does not exist)" "$tentative"; then
        echo "- $(date '+%d.%m.%Y %H:%M %Z') · modèle $MODELE_REPETITIF refusé : étape $2 relancée avec le modèle de secours configuré ou le défaut de Codex, coût non vérifié." >> "$RACINE/ETAT.md"
        python3 "$RACINE/tools/garde/relance_bail.py" --owner "$reservation" executer -- codex exec -c 'approval_policy="never"' -s workspace-write -C "$RACINE" ${MODELE_SECOURS:+-m "$MODELE_SECOURS"} "$ordre_execution" </dev/null >> "$LOCAL/codex_exec.log" 2>&1
        code=$?
      fi
    else
      python3 "$RACINE/tools/garde/relance_bail.py" --owner "$reservation" executer -- codex exec -c 'approval_policy="never"' -s workspace-write -C "$RACINE" "$ordre_execution" </dev/null >> "$LOCAL/codex_exec.log" 2>&1
      code=$?
    fi
    rm -f "$tentative"
    log "processus Codex terminé, code$code ; résultat à contrôler, aucune fin de mission déduite"
  ) &
  log "mode A : lancement demandé (étape $2, modèle ${mod})"
}

passage() {
  [ -e "$LOCAL/permanence/STOP" ] && { log "arrêt explicite demandé"; return 77; }
  local configuration
  configuration="$(python3 -c 'import json,sys;v=json.load(open(sys.argv[1]));assert isinstance(v,dict);print("stop" if v.get("permanence_enabled") is False else "actif")' "$RACINE/tools/garde/config.json" 2>/dev/null)" || { log "configuration illisible : aucune relance"; return; }
  [ "$configuration" = stop ] && { log "arrêt commun configuré"; return 77; }
  if codex_actif; then log "Codex tourne déjà : aucune relance ni mutation de l’étape"; return; fi
  local activite
  activite_partagee; activite=$?
  if [ "$activite" = 0 ]; then log "responsable ou CI actif : aucune relance"; return; fi
  if [ "$activite" != 1 ]; then log "activité distante inconnue : aucune relance aveugle"; return; fi
  local n statut mission etat_local
  etat_local="$(python3 - "$RACINE/ETAT.json" <<'PY'
import json,sys
v=json.load(open(sys.argv[1]))
n=v.get('etape_courante');s=v.get('statut');m=v.get('mission_exclusive',{})
assert type(n) is int and n>=0 and s in ('en_cours','terminee') and isinstance(m,dict)
mission=m.get('id','');assert isinstance(mission,str) and not any(c.isspace() for c in mission)
print(n,s,mission)
PY
  )" 2>/dev/null || { log "ETAT.json invalide : original conservé, aucune mutation ni relance"; return; }
  read -r n statut mission <<< "$etat_local"
  if [ "$mission" = infobulles_prototype6 ]; then
    [ "$n" = 9 ] || { log "mission exclusive : étape $n incohérente, aucune mutation ni relance"; return; }
  fi
  git -C "$RACINE" fetch -q origin 2>/dev/null || log "git fetch impossible (réseau) : on continue"
  # Le bail du responsable, la CI et Codex ont été contrôlés avant toute mutation.
  local age=999999
  [ -f "$RACINE/ETAT.json" ] && age=$(( $(date +%s) - $(stat -c %Y "$RACINE/ETAT.json") ))
  if ! codex_actif && { [ "$statut" = terminee ] || [ "$age" -ge "$INACTIF_SECONDES" ]; }; then
    local o; o="$(python3 "$RACINE/tools/porte.py" ordre 2>/dev/null)" || { log "ordre indisponible : aucune relance"; return; }
    [ -n "$o" ] || { log "ordre vide : aucune relance"; return; }
    o="${o/continue avec l\'étape suivante/reprends l\'étape en cours}"
    if [ "$statut" = terminee ]; then o="$o Le lot précédent est marqué terminé : vérifie sa publication et reprends la mission prioritaire ; ce statut ne clôt pas la mission exclusive."; fi
    log "étape $n en cours, inactive depuis ${age}s → relance"; relancer "$o" "$n"
  else
    log "étape $n en cours (dernière activité il y a ${age}s)"
  fi
}

if [ "$MODE" = "boucle" ]; then
  log "veille démarrée (boucle, ${PAUSE} s)"
  while true; do
    echeance=$((SECONDS + PAUSE))
    passage; [ "$?" = 77 ] && break
    while [ "$SECONDS" -lt "$echeance" ]; do
      [ -e "$LOCAL/permanence/STOP" ] && exit 0
      reste=$((echeance - SECONDS)); [ "$reste" -gt 25 ] && reste=25
      sleep "$reste"
    done
  done
else
  passage
fi
exit 0
