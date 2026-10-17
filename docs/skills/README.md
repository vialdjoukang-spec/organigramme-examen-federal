# Skills du projet (copie lisible par Codex)

Chaque skill est `docs/skills/<nom>/SKILL.md` (miroir exact de `skills/<nom>/SKILL.md` et de la bibliothèque de l'assistant Grok Bot, invisible hors de la box). Lis celui de ton étape avant d'agir.

| Skill | Quand |
|---|---|
| `ssp-pilotage-codex` | Chaque session : porte, veille, file de fusion (Étape 0 et toutes) |
| `ssp-continuite` | Relève entre sessions, HANDOFF.md |
| `ssp-verite` | Toute source, tout chiffre (R1) |
| `ssp-posologie-suisse` | Toute dose : AIPS verbatim (Étapes 6, 10) |
| `ssp-audit-medical` | Tout audit avant `audit-ok` (R6) |
| `ssp-fusion-patch`, `ssp-patch` | Conflits, patches de `app_v2.html` (Étapes 3–7) |
| `ssp-json-data`, `ssp-extrait-cible` | Données JSON extraites/injectées |
| `ssp-chaine-clinique`, `ssp-signe-infobulle`, `ssp-synthese-locale` | Contenu CK, glossaire, infobulles (Étapes 8, 9, 11) |
| `ssp-revue-diff` | Relecture d'un diff |
| `ssp-tests`, `ssp-qa-regression`, `ssp-qualite-visuelle` | Tests, captures, contrôle visuel (Étape 2, fins de lot) |
| `ssp-images-licence`, `ssp-schema-nerf` | Images et schémas des nerfs (Étape 13) |

Nouveaux skills proposés automatiquement : `PROPOSITIONS.md` (`python3 tools/propose_skills.py`).
