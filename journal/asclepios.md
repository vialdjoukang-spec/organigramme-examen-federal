# Journal Asclépios
## 17.10.2026 — Étape 1 (audit examen physique, sans modification de app_v2.html)
- Extraits : GES, PHT, NOT, TIP via tools/json_inject.py (non commités).
- Scripts réutilisables : tools/audit_examen/analyse.py (stats, matrice auto, signaux d'ordre, doublons ; lancer depuis la racine), render.py (MD → PDF Chrome headless), sk.py (licences Wikimedia via API).
- Livrables : /workspace/ssp/audit_examen/AUDIT_examen_physique.{md,pdf}.
- Résultat : 308 gestes / 20 régions (3 axes mélangés) ; 7 lacunes, 12 doublons, 9 violations d'ordre confirmées (48 signaux auto) ; TIP champ 5 : 15 vides, 6/233 structurés par région.
- Étape 2 bloquée en attente de validation par Vial.

## 17.10.2026 — Étape 2 (validée par Vial)
- tools/asclepios/ges_v2.py : 3 axes, sous-régions (tête-cou 6, TR-OGE 4, rachis 5, coude-main 2), module Vaisseaux périphériques (8 gestes déplacés du cœur), module Relevé ganglionnaire (3 gestes nouveaux), ATM, globe vésical, neuro-vasculaire distal épaule et genou ; 9 violations d’ordre corrigées ; 12 doublons → 23 paires de renvois.
- tools/asclepios/tip_exam.py : champ 5 de 198 SSP réparti par région puis par phase, éléments d’origine verbatim (0 perdu, 196 intertitres conservés en italique), 728 puces vers les gestes ; 15 vides « À compléter » ; 35 laissés (moins de 25 % d’éléments anatomiques).
- Croquis : 19 intégrés ; écartés : photo de mesure tensionnelle (personne identifiable), Gray1218 (montre le cœur, pas les poumons) remplacé par Gray965.
- Tests : 72/72 (dont test_examen 16/16), gardes 5/5.
