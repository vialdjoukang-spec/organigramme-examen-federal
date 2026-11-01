# LOT_004 · G4 Fatigue, lassitude — Type A — CHANGELOG

## v1.0.0 (1 nov. 2026, Zurich UTC+1) — première série
- 88 questions Type A (5 options, une seule clé) : **52 EX · 20 AP · 16 SPE** (59,1 / 22,7 / 18,2 %) ; 24 R · 50 D · 14 P ; clés A18 B18 C18 D17 E17, jamais 3 identiques d'affilée (seed 13). 1 question à polarité négative (1,1 %, rasburicase et G6PD).
- SPE : Psychiatrie ×3, Endocrinologie ×3, Médecine intensive ×2, Hématologie ×2, Psychogériatrie, Rhumatologie, Médecine du sommeil, Médecine interne, Pédiatrie, Oncologie (bouton 🔥).
- Couverture DD : **11/11 DX avec ≥ 2 EX cibles** (4 à 6 EX par DX), aucun gap ; chaque DX a au moins 1 AP ou SPE, sauf DX.8 qui n'a pas d'AP (2 SPE). Voir `COUVERTURE_DD.md`.
- Drapeaux rouges testés : E1 suicide (DX.1), E2 diabète décompensé (DX.4), E3 crise surrénalienne (DX.5), E4 saignement / anémie (DX.6), E5 perte de poids / adénopathie (DX.11) ; plus artérite, rupture de rate, compression médullaire, hypercalcémie maligne, neutropénie fébrile, coma myxœdémateux, somnolence au volant.
- Indice de longueur contrôlé : la bonne réponse est l'option la plus longue dans 10/88 questions (11,4 %) et la plus courte dans 9/88 (10,2 %).
- Blueprint : 43 évaluation / diagnostic, 43 prise en charge, 2 mécanismes ; 6 settings (cabinet, urgences, hôpital, policlinique, EMS, domicile).
- Carte réflexe (3 questions, psychique-sommeil, biologie de base, durée-effort, locomoteur-organe, ordre E1–E5) + algorithme (Phase A §algo et §10) intégrés.
- Sources exclusivement `repo/LOT_Claude_Finaux/LOT_004/` (Phase A §/algo, Phase B DX.n §), 63 liens distincts, 0 cassé. Aucune image (aucun cliché dans le LOT).
- Valeurs du LOT incohérentes, non testées à la limite : spécificité du PHQ-9 (88 % en Phase A, 0,85 en DX.1) ; seuil de ferritine (< 50 µg/L en Phase A d'après Vaucher, < 30 µg/L en DX.6 d'après le Delphi suisse ; la vignette utilise 22 µg/L) ; seuil de traitement de l'infraclinique (TSH > 10 pour l'ETA 2013, > 20 pour le BMJ 2019 : la question cite l'ETA). Les seuils marqués « À vérifier » en DX.5 (perte de poids, taille ganglionnaire) ne sont pas utilisés.
- 💡 fermé par défaut, mode révision avec confirmation ; rendu Chrome 390 px OK. PDF : questions puis corrigé en annexe (90 pages).
