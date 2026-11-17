# Audits LOT 1 à LOT 8 — listes de corrections

Audit du 22 octobre 2026 : un auditeur médical et un auditeur linguistique indépendants par lot, contre le prompt de base V6.

| Lot | SSP | Critique | Grave | Moyen | Léger | Total | Liste Word |
|---|---|---|---|---|---|---|---|
| 1 | G1 — Transpiration anormale | 1 | 61 | 49 | 15 | 126 | [LOT_1_Liste_Corrections_Audit.docx](LOT_1_Liste_Corrections_Audit.docx) |
| 2 | G2 — Tuméfaction et adénopathie | 2 | 31 | 47 | 23 | 103 | [LOT_2_Liste_Corrections_Audit.docx](LOT_2_Liste_Corrections_Audit.docx) |
| 3 | G3 — Soif excessive (polydipsie) | 5 | 59 | 50 | 13 | 127 | [LOT_3_Liste_Corrections_Audit.docx](LOT_3_Liste_Corrections_Audit.docx) |
| 4 | G4 — Fatigue et épuisement | 8 | 60 | 63 | 24 | 155 | [LOT_4_Liste_Corrections_Audit.docx](LOT_4_Liste_Corrections_Audit.docx) |
| 5 | G5 — Sensation de maladie et malaise | 1 | 82 | 56 | 32 | 171 | [LOT_5_Liste_Corrections_Audit.docx](LOT_5_Liste_Corrections_Audit.docx) |
| 6 | G6 — Fièvre | 2 | 37 | 18 | 16 | 73 | [LOT_6_Liste_Corrections_Audit.docx](LOT_6_Liste_Corrections_Audit.docx) |
| 7 | G7 — Flushing | 0 | 4 | 18 | 12 | 34 | [LOT_7_Liste_Corrections_Audit.docx](LOT_7_Liste_Corrections_Audit.docx) |
| 8 | G8 — Hypothermie | 7 | 44 | 43 | 16 | 110 | [LOT_8_Liste_Corrections_Audit.docx](LOT_8_Liste_Corrections_Audit.docx) |
| **Total** | | **26** | **378** | **344** | **151** | **899** | |

## Mode d'emploi
- Chaque liste Word donne, pour chaque problème : fichier, emplacement (Bloc › point › fenêtre), extrait exact, correction et source.
- L'extrait se retrouve par Ctrl+F dans le fichier cloné du même dossier ; un script a contrôlé qu'il existe mot pour mot.
- Le correcteur coche la case après correction : elle devient un ☒ rouge. L'auditeur suivant contrôle les cases cochées.
- Les constats bruts (JSON) et les rapports médicaux et linguistiques sont dans `audits/`.

## Réserves
- Audit produit par IA : il ne remplace pas une validation clinique par un médecin.
- LOT 3 : l'auditeur médical déclare avoir tiré de mémoire une partie des détails de l'ESE 2014 ; revérifier les constats sur le NaCl 3 % dans le texte primaire.
- LOT 8 : le texte primaire ERC 2025 n'était pas accessible chez l'éditeur ; il a été lu dans une copie PDF et recoupé avec le Resuscitation Council UK 2025.
- Les Google Docs ont été clonés par export HTML : ce ne sont pas des copies à l'octet de l'original Google Docs.
- Dépôt des listes Word dans Drive : bloqué par un filtre de sécurité (LOT 6) ; non relancé. Les listes font foi ici.
