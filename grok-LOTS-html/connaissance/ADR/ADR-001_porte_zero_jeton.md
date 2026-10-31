# ADR-001 — Porte zéro jeton avant toute passe de modèle (2026-10-31) — [Accueil](../00_ACCUEIL.md)

**Contexte.** Les contrôles mécaniques (taille, FIN_FICHIER, structure, langue) coûtent 0 jeton mais, aujourd'hui, ne sont lancés que dans la passe d'un modèle, qui lit un JSON bruyant (≈ 7 Ko, faux critiques V0, voir P-01) et peut déclencher un second audit médical si une correction de taille arrive après coup (PROMPT_PRODUCTION_V2 §12).
**Décision.** `outils/porte_zero_jeton.py avant <poste> <fichier>` s'exécute avant chaque passe de modèle ; ROUGE = on ne lance pas la passe payante, on corrige d'abord. Le critère de langue est différentiel par rapport à `MODELE_DD_V8.html`.
**Conséquences.** (+) un audit médical ne porte plus que sur un fichier mécaniquement valide. (−) la porte ne dit rien du fond médical ; VERT ≠ correct. (−) à maintenir si le harnais ou le modèle V8 changent (le calcul de base se refait à chaque appel).
