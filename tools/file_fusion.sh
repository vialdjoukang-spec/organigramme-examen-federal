#!/usr/bin/env bash
# File de fusion-publication automatique (gratuit : gh + git + python3). Lancé par tools/veille_relance.sh
# et par .github/workflows/file-fusion.yml. Ne s'arrête jamais sur un échec : il le consigne dans
# journal/echecs_fusion.md et passe à la PR ou à la chaîne suivante. Code de sortie toujours 0 (sauf usage).
#
# Règles (CONTINUATION.md § Fusion) : fusion seulement si label audit-ok, CI requise verte, branche à jour,
# commit de fusion (--merge, --match-head-commit), jamais squash, jamais force-push, jamais --admin,
# jamais d'affaiblissement de la protection de main. Label « attente-vial » = faute critique : on ne touche pas.
#
# Usage : tools/file_fusion.sh [--dry-run] [--chaine NOM] [--sans-publier] [--ci] [--droits]
#   --dry-run      n'écrit rien (ni API en écriture, ni journal) : imprime ce qui serait fait
#   --chaine NOM   une seule chaîne de tools/etapes.json (prev, hygie, panacee, doses, glossaire…)
#   --ci           exécution GitHub Actions (journal dans le résumé du job, pas dans le dépôt)
#   --droits       contrôle les droits de fusion (admin, auto-merge, commit de fusion, protection) puis sort
set -uo pipefail
RACINE="${OEF_REPO:-$(cd "$(dirname "$0")/.." && pwd)}"
export GH_REPO="${GH_REPO:-vialdjoukang-spec/organigramme-examen-federal}"
DRY=0; CHAINE=""; PUBLIER=1; CI=0; DROITS=0
while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run) DRY=1 ;; --chaine) CHAINE="${2:-}"; shift ;; --sans-publier) PUBLIER=0 ;;
    --ci) CI=1 ;; --droits) DROITS=1 ;;
    -h|--help) sed -n '2,15p' "$0"; exit 0 ;;
    *) echo "option inconnue : $1" >&2; exit 64 ;;
  esac; shift
done
exec 3>&2  # canal des messages --dry-run (non masqué par les redirections)
JOURNAL="$RACINE/journal/echecs_fusion.md"
LOCAL="$RACINE/.etat_local"; mkdir -p "$LOCAL"
VUS="$LOCAL/echecs_vus.txt"; touch "$VUS"
horodate() { date '+%Y-%m-%d %H:%M %Z'; }
info() { echo "[file_fusion] $*" >&2; }
echec() { # $1 = PR, $2 = raison ; dédoublonné (même PR, même raison → une seule ligne)
  local cle="$1|$2"; info "ÉCHEC #$1 : $2"
  [ "$DRY" = 1 ] && return 0
  grep -qxF "$cle" "$VUS" 2>/dev/null && return 0
  echo "$cle" >> "$VUS"
  if [ "$CI" = 1 ]; then echo "- $(horodate) · #$1 · $2" >> "${GITHUB_STEP_SUMMARY:-/dev/stdout}"; return 0; fi
  [ -f "$JOURNAL" ] || printf '# Échecs de fusion-publication (tools/file_fusion.sh)\n\nUne ligne par échec nouveau. Le travail continue toujours ; Codex traite ces lignes à l’étape 2 ou dans l’étape de la chaîne.\n\n' > "$JOURNAL"
  echo "- $(horodate) · #$1 · $2" >> "$JOURNAL"
}
oublier() { [ "$DRY" = 1 ] || { grep -v "^$1|" "$VUS" > "$VUS.tmp"; mv "$VUS.tmp" "$VUS"; }; }
ecrire() { # exécute une commande d'écriture, ou l'imprime en --dry-run
  if [ "$DRY" = 1 ]; then echo "[file_fusion] [dry-run] $*" >&3; return 0; fi
  "$@"
}
command -v gh >/dev/null || { info "gh absent : file de fusion sautée (le travail continue)"; exit 0; }
gh auth status >/dev/null 2>&1 || { info "gh non authentifié : file de fusion sautée (le travail continue)"; exit 0; }

if [ "$DROITS" = 1 ]; then
  gh api "repos/$GH_REPO" --jq '{admin:.permissions.admin, push:.permissions.push, auto_merge:.allow_auto_merge, merge_commit:.allow_merge_commit, squash:.allow_squash_merge}' > "$LOCAL/droits.json" 2>/dev/null \
    || { info "lecture des droits impossible"; exit 0; }
  gh api "repos/$GH_REPO/branches/main/protection" --jq '{checks:.required_status_checks.contexts, strict:.required_status_checks.strict, enforce_admins:.enforce_admins.enabled}' >> "$LOCAL/droits.json" 2>/dev/null || true
  cat "$LOCAL/droits.json"; exit 0
fi

REQUIS="$(gh api "repos/$GH_REPO/branches/main/protection" --jq '.required_status_checks.contexts|join(" ")' 2>/dev/null)"
REQUIS="${REQUIS:-garde html tests visuel}"
CHAINES="$(python3 - "$RACINE/tools/etapes.json" "$CHAINE" <<'PY'
import json, sys
c = json.load(open(sys.argv[1], encoding="utf-8"))["chaines"]
for k, v in c.items():
    if not sys.argv[2] or k == sys.argv[2]:
        print(k, *v)
PY
)"
FUSIONNEES=0
while read -r nom prs; do
  [ -n "${nom:-}" ] || continue
  info "chaîne $nom : $prs"
  for n in $prs; do
    js="$(gh pr view "$n" --json state,labels,mergeStateStatus,headRefOid,isDraft,statusCheckRollup 2>/dev/null)" \
      || { echec "$n" "lecture de la PR impossible (réseau ou droits)"; break; }
    read -r etat audit vial draft fusion sha verdict <<<"$(JS="$js" python3 - "$REQUIS" <<'PY'
import json, os, sys
d = json.loads(os.environ["JS"])
req = sys.argv[1].split()
lab = [l["name"] for l in d.get("labels", [])]
res = {}
for c in d.get("statusCheckRollup") or []:
    nom = c.get("name") or c.get("context")
    st = (c.get("conclusion") or c.get("state") or c.get("status") or "").upper()
    if c.get("status") and c.get("status") != "COMPLETED":
        st = "PENDING"
    res[nom] = st
v = "vert"
for r in req:
    s = res.get(r, "ABSENT")
    if s in ("FAILURE", "ERROR", "CANCELLED", "TIMED_OUT", "ACTION_REQUIRED", "STARTUP_FAILURE"):
        v = "rouge:" + r; break
    if s not in ("SUCCESS", "NEUTRAL", "SKIPPED"):
        v = "attente:" + r
print(d["state"], int("audit-ok" in lab), int("attente-vial" in lab), int(d.get("isDraft", False)),
      d.get("mergeStateStatus", "UNKNOWN"), d.get("headRefOid", "-"), v)
PY
)"
    case "$etat" in MERGED|CLOSED) info "#$n $etat"; oublier "$n"; continue ;; esac
    if [ "$vial" = 1 ]; then info "#$n attend l'accord de Vial (faute critique) : chaîne suspendue"; break; fi
    if [ "$draft" = 1 ] || [ "$audit" = 0 ]; then info "#$n attend son audit (pas de label audit-ok)"; break; fi
    # Exécutions « action_required » (commits du bot) : approuver ou relancer.
    for id in $(gh run list --commit "$sha" --status action_required --json databaseId --jq '.[].databaseId' 2>/dev/null); do
      ecrire gh api -X POST "repos/$GH_REPO/actions/runs/$id/approve" >/dev/null 2>&1 \
        || ecrire gh run rerun "$id" >/dev/null 2>&1 \
        || echec "$n" "CI action_required (run $id) : pousser un commit vide sur la branche (git commit --allow-empty) ou approuver dans Actions"
    done
    case "$fusion" in
      BEHIND)
        if ecrire gh api -X PUT "repos/$GH_REPO/pulls/$n/update-branch" -f expected_head_sha="$sha" >/dev/null 2>&1; then
          info "#$n mise à jour avec main (CI relancée)"
        else
          echec "$n" "update-branch refusé : fusionner origin/main en local puis rebuild (skill ssp-fusion-patch)"
        fi
        break ;;
      DIRTY)
        echec "$n" "conflit avec main : git merge origin/main + merge_shards.py + mono_build.py/prev_build.py (jamais à la main)"
        break ;;
    esac
    case "$verdict" in
      rouge:*) echec "$n" "contrôle requis ${verdict#rouge:} en échec"; break ;;
      attente:*) info "#$n CI en cours (${verdict#attente:})"; break ;;
    esac
    if [ "$fusion" != "CLEAN" ] && [ "$fusion" != "HAS_HOOKS" ] && [ "$fusion" != "UNSTABLE" ]; then
      info "#$n état $fusion : on attend"; break
    fi
    if ecrire gh pr merge "$n" --merge --match-head-commit "$sha"; then
      info "#$n FUSIONNÉE (commit de fusion)"; oublier "$n"; FUSIONNEES=$((FUSIONNEES+1))
    else
      echec "$n" "gh pr merge refusé (protection, tête changée ou droits)"; break
    fi
  done
done <<<"$CHAINES"

if [ "$FUSIONNEES" -gt 0 ] && [ "$PUBLIER" = 1 ]; then
  ecrire gh workflow run pages.yml --ref main >/dev/null 2>&1 && info "Pages relancé" \
    || echec "pages" "publication Pages non relancée (gh workflow run pages.yml) : réessai au prochain passage"
fi
info "terminé : $FUSIONNEES fusion(s)"
exit 0
