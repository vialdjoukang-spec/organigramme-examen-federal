# Validation de production — LOT_020, S1.4

Onze HTML complets, relus en session unique selon l’ordre de Vial. Ce constat ne constitue ni validation clinique, ni audit indépendant, ni note de qualité médicale.

- 275 contrôles statiques V8 réussis sur les onze fichiers.
- 14 parties et 14 questions par leçon, soit 154 questions originales.
- 149 fenêtres atteignables dans le graphe de liens, fermeture explicite ; six sous-fenêtres.
- 36 paragraphes de citation AIPS retrouvés dans les six informations professionnelles locales tracées ; normalisation des espaces seulement.
- Neuf empreintes du harnais inchangées ; style officiel et polices embarquées vérifiés.

| Fichier | Texte principal (Ko) | Fenêtres (Ko) |
|---|---:|---:|
| [LOT_020_Phase_A_V0.html](LOT_020_Phase_A_V0.html) | 7.3 | 23.9 |
| [LOT_020_Phase_B_V0_DX.1.html](LOT_020_Phase_B_V0_DX.1.html) | 4.7 | 11.7 |
| [LOT_020_Phase_B_V0_DX.2.html](LOT_020_Phase_B_V0_DX.2.html) | 4.2 | 8.1 |
| [LOT_020_Phase_B_V0_DX.3.html](LOT_020_Phase_B_V0_DX.3.html) | 4.3 | 9.7 |
| [LOT_020_Phase_B_V0_DX.4.html](LOT_020_Phase_B_V0_DX.4.html) | 4.2 | 12.3 |
| [LOT_020_Phase_B_V0_DX.5.html](LOT_020_Phase_B_V0_DX.5.html) | 4.0 | 7.5 |
| [LOT_020_Phase_B_V0_DX.6.html](LOT_020_Phase_B_V0_DX.6.html) | 3.7 | 7.4 |
| [LOT_020_Phase_B_V0_DX.7.html](LOT_020_Phase_B_V0_DX.7.html) | 4.1 | 10.5 |
| [LOT_020_Phase_B_V0_DX.8.html](LOT_020_Phase_B_V0_DX.8.html) | 4.2 | 7.7 |
| [LOT_020_Phase_B_V0_DX.9.html](LOT_020_Phase_B_V0_DX.9.html) | 4.3 | 12.2 |
| [LOT_020_Phase_B_V0_DX.10.html](LOT_020_Phase_B_V0_DX.10.html) | 4.1 | 8.4 |

Mesure par harnais/taille_xy.py : cours sous 100 Ko et chaque diagnostic sous 9 Ko de texte principal. Les fenêtres sont hors plafond. Les empreintes finales sont dans MANIFESTE.json.

## Résultats officiels et limites

Les contrôleurs officiels ont réellement retourné le code 1. Rapports bruts dans audits/controle_officiel.json et audits/langue_*.json. Les règles historiques imposent une absence générale de title, des sources [S1], des h3 et une bande de taille brute ; V8 demande abbr title, exposants, îlots h2 et plafond du texte principal. Leur détection historique des monographies est aussi incompatible avec ces titres. Le contrôle complémentaire ne transforme pas ces résultats en succès officiel.

Les avertissements linguistiques ont été relus : phrases longues et ponctuation des citations AIPS conservées littéralement ; sigles développés dans abbr ; répétitions d’étiquette de fenêtre et de références, sans phrase clinique dupliquée. Détails et corrections dans CORRECTIONS_AUDIT.md.

Relecture interne réelle des décisions cliniques et de la cohérence des onze leçons : mécanismes faciaux, urgences, diagnostics atypiques, statut des traitements, limites d’âge, fonctions rénale et hépatique, contre-indications, grossesse/allaitement et parcours spécialisés. Aucun auditeur indépendant ni médecin n’a validé ces textes. Aucun score ni nombre de défauts médicaux graves restant n’est établi. Classement pédagogique faute de prévalences comparatives documentées.

Rendu navigateur et mobile non vérifié. Les tentatives antérieures dans cet environnement étaient bloquées (Chromium file:// refusé ; téléchargement Playwright HTTP 403). Aucun nouveau test visuel n’est revendiqué et aucune restriction n’a été contournée. Popovers vérifiés statiquement seulement.
