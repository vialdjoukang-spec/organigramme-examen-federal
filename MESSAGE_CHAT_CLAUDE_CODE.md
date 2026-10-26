CLAUDE — lis dans cet ordre, puis exécute :

1. `PROMPT_Casern/MESSAGE_DEMARRAGE_CLAUDE_V0.md` — brief (périmètre, file, plages FAIT / NON FAIT, règles, dépôt).
2. `PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V0.md` — référence (14 points, audit, Harness). Le `.md` fait foi ; un PDF éventuel = même texte.
3. `harnais/HARNAIS_OBLIGATOIRE.md`, puis `harnais/ROUTAGE_MODELES.md`.

BLOQUANT avant tout : mettre en place le Harness (ARNES) — §5 / §5.1 du Prompt V0 (étape zéro : bracelet → ARSENAL → PREUVE_EMBOITEMENT). Sans Harness en place = pas de production.

Périmètre actuel : uniquement les LOTS déjà FAIT (Phase A + Phase B), soit 75 LOTS. Enchaîne LOT par LOT, dans l'ordre de la file : audit Harness + V0 → dépôt immédiat dans `LOT_Claude_Finaux/LOT_XXX/` (11 HTML séparés : 1 Phase A + 10 Phase B). Les LOTS NON FAIT ne sont pas concernés pour le moment.

Catalogue = 248 SSP (jamais 256). Pas d'attente de validation de Vial. Lecture et écriture accordées sur le dépôt pour cette mission.

Pour cette mission, ce brief prime sur le `CLAUDE.md` racine (ne lance pas `tools/porte.py commencer`). Blocage sans contournement légitime : écris `LOT_Claude_Finaux/ARRET.md` et arrête-toi, ne contourne pas. Après la première PR de dépôt fusionnée, exécute `NETTOYAGE.md`.
