CLAUDE — lis dans cet ordre, puis exécute :

1. `PROMPT_Casern/MESSAGE_DEMARRAGE_CLAUDE_V0.md` — brief (périmètre, file, équipes, règles, dépôt).
2. `PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V0.md` — référence d'audit et de production ; tu t'y réfères à chaque audit.
3. `harnais/HARNAIS_OBLIGATOIRE.md`, puis `harnais/ROUTAGE_MODELES.md`.

BLOQUANT : Harness (Prompt §5/§5.1 : bracelet → ARSENAL → PREUVE_EMBOITEMENT). Sans preuve verte, pas de production.

Exécution : LOT_001 → LOT_010 (file active de 10), un LOT à la fois ; le LOT n+1 ne démarre que si le LOT n est achevé, poussé et mergé (ou REFUSE/BLOQUE consigné et mergé).
- LOT VIDE → fabrication, 3 agents : 2 rédacteurs + 1 auditeur médico-linguistique.
- LOT NON VIDE → audit médico-linguistique uniquement, 2 agents (rédacteur seulement si l'audit échoue).
- 11 HTML par LOT (1 Phase A + 10 Phase B), 100–200 Ko par fichier, bornes comprises ; but = densité d'information, aucune notion omise.
- Dépôt immédiat dans `LOT_Claude_Finaux/LOT_XXX/` après audit conforme (≥ 90 %, zéro critique, question finale « oui », LOT complet, `controle_lot.py verifier` = CONFORME).

Catalogue = 248 SSP (jamais 256). Pas d'attente de validation de Vial. Lecture et écriture accordées. Ce brief prime sur le `CLAUDE.md` racine. Blocage sans contournement légitime → `LOT_Claude_Finaux/ARRET.md`, arrêt. Après la 1re PR de dépôt fusionnée : `NETTOYAGE.md` (PR `nettoyage-v0`).
