# Pack d'implémentation S2 — fichiers à AJOUTER sous `grok-LOTS-html/`

Rien d'existant n'est modifié (ni `registre_ia.py`, ni `ROUTAGE_GROK.json`, ni `routage_grok.py`, ni `harnais/`, ni `ressources_ia/`).
Python standard uniquement, zéro jeton, aucune dépendance, aucune écriture hors `connaissance/COUTS.jsonl` et `_cache/` (non commité).

| Fichier | Rôle |
|---|---|
| `outils/porte_zero_jeton.py` | `avant <poste> <fichier>` : FIN_FICHIER, taille x (9 Ko DD / 100 Ko Phase A), ids V8, balises, `<script>`, popover, « non validé cliniquement », critiques `audit_langue` **nouveaux par rapport au modèle V8**, sceau SHA, citations « » mot pour mot, ordre des postes. `precommit` : même contrôle sur l'index git + périmètre `grok-LOTS-html/`. VERT / ORANGE / ROUGE. |
| `outils/contexte_lot.py` | `construire LOT_XXX` : un paquet par poste (règles + base + rôle + brief + leçons + squelette du modèle 20,8 Ko au lieu de 253,7 Ko), ordre du plus stable au plus volatil. |
| `outils/couts.py` | `noter` (une ligne par passe, barème relatif), `bilan` (par LOT / poste), `tarifs`. |
| `outils/vault_lint.py` | aucune note orpheline, aucun lien cassé, `PIEGES.md` ≤ 8 Ko. |
| `connaissance/` | `00_ACCUEIL.md` (hub), `PIEGES.md` (P-01…P-13), `PROMPTS_QUI_MARCHENT.md`, `HOOKS.md`, `JOURNAL_CONNAISSANCE.md`, `COUTS.jsonl` (vide), `TARIFS_RELATIFS.json` (HYPOTHÈSES), `PREVISION_SIMULATION.json`, `ADR/ADR-001…003`. |

## Test
```
python3 tester_pack.py            # copie le clone en lecture seule dans /tmp, pose le pack, 24 contrôles positifs et négatifs
```
Dernier résultat : 24 OK, 0 échec (31.10.2026, heure de Zurich).

## Usage par poste (rappel)
1. `python3 grok-LOTS-html/outils/contexte_lot.py construire LOT_134 --poste redacteur` → donner le fichier produit au run.
2. Après chaque fichier : `python3 grok-LOTS-html/outils/porte_zero_jeton.py avant auditeur-medical <fichier>` → ROUGE = corriger (script ou mécanique), pas d'audit.
3. Fin de passe : `python3 grok-LOTS-html/outils/couts.py noter LOT_134 redacteur --ko-entree … --ko-sortie … --tours …`.
4. Fin de LOT : `couts.py bilan LOT_134` ; `vault_lint.py`.

## Reste manuel pour Vial
- Activer le garde 5 minutes : copier `outils/garde-grok-temps-reel.yml` vers `.github/workflows/` **sur `main`** (les workflows planifiés ne tournent que depuis la branche par défaut).
- Ajouter à `.git/hooks/pre-commit` (hors dépôt versionné) : `python3 grok-LOTS-html/outils/porte_zero_jeton.py precommit || exit 1`.
- Trancher la règle de clôture « `controle_lot` = 0 critique » : elle est incompatible avec le format V8 (66 critiques sur LOT_016 V8, dus aux règles V0 du harnais).
- Remplacer `TARIFS_RELATIFS.json` par les vrais barèmes de l'abonnement ; après 3 à 5 LOTs, comparer `couts.py bilan` à `PREVISION_SIMULATION.json`.
- Relire et élaguer `PIEGES.md` (seule la curation humaine empêche son gonflement).
