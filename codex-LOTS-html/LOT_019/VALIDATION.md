# Validation de production — LOT_019, S1.3

Onze HTML complets, relus en session unique selon l’ordre de Vial. Ce constat ne constitue ni validation clinique, ni audit indépendant, ni note de qualité médicale.

- 275 contrôles statiques V8 réussis sur les onze fichiers.
- 14 parties et 14 questions par leçon, soit 154 questions originales.
- 145 fenêtres atteignables dans le graphe des liens, avec fermeture explicite ; deux sous-fenêtres. Fonctionnement au navigateur non essayé pour ce lot.
- 5 paragraphes de citation AIPS retrouvés dans la source officielle locale 52433 ; normalisation des espaces seulement.
- Neuf empreintes du harnais inchangées. Polices embarquées et style officiel vérifiés.

| Fichier | Texte principal (Ko) | Fenêtres (Ko) |
|---|---:|---:|
| [LOT_019_Phase_A_V0.html](LOT_019_Phase_A_V0.html) | 5.7 | 18.8 |
| [LOT_019_Phase_B_V0_DX.1.html](LOT_019_Phase_B_V0_DX.1.html) | 4.6 | 8.3 |
| [LOT_019_Phase_B_V0_DX.2.html](LOT_019_Phase_B_V0_DX.2.html) | 4.7 | 7.7 |
| [LOT_019_Phase_B_V0_DX.3.html](LOT_019_Phase_B_V0_DX.3.html) | 4.2 | 7.1 |
| [LOT_019_Phase_B_V0_DX.4.html](LOT_019_Phase_B_V0_DX.4.html) | 4.1 | 7.3 |
| [LOT_019_Phase_B_V0_DX.5.html](LOT_019_Phase_B_V0_DX.5.html) | 4.4 | 7.3 |
| [LOT_019_Phase_B_V0_DX.6.html](LOT_019_Phase_B_V0_DX.6.html) | 4.5 | 7.0 |
| [LOT_019_Phase_B_V0_DX.7.html](LOT_019_Phase_B_V0_DX.7.html) | 4.1 | 8.7 |
| [LOT_019_Phase_B_V0_DX.8.html](LOT_019_Phase_B_V0_DX.8.html) | 4.4 | 9.8 |
| [LOT_019_Phase_B_V0_DX.9.html](LOT_019_Phase_B_V0_DX.9.html) | 3.8 | 8.0 |
| [LOT_019_Phase_B_V0_DX.10.html](LOT_019_Phase_B_V0_DX.10.html) | 4.0 | 9.5 |

Mesure par `harnais/taille_xy.py` : x ≤100 Ko pour le cours et x ≤9 Ko par diagnostic. Les fenêtres sont hors plafond. Le manifeste contient les empreintes finales.

## Contrôleurs historiques

Les contrôleurs officiels ont été réellement exécutés et retournent le code 1. Rapports bruts conservés dans `audits/controle_officiel.json` et `audits/langue_*.json`. Les erreurs détectées correspondent aux règles historiques incompatibles avec V8 : interdiction générale de `title` alors que `<abbr title>` est demandé ; sources littérales `[S1]` alors que les exposants sont demandés ; quatorze `h3` au lieu des îlots `h2` ; bande de 80–150 Ko du fichier alors que V8 plafonne le texte principal. Le contrôle complémentaire ne transforme pas ces échecs en succès officiel.

Les sigles signalés sont développés dans les balises `abbr`. Les espaces insécables réclamées restent exclues par le prompt. Les points-virgules signalés ont été relus ; il s’agit d’un avertissement stylistique. La phrase identique répétée dans DX.5 a été reformulée. Les citations AIPS restent littérales.

## Relecture et limites

La relecture interne a vérifié : mobilité versus vibration, immobilité versus paralysie, risque respiratoire bilatéral, diagnostic histologique des lésions suspectes, différences entre lésions bénignes, traitement conservateur de la laryngite, statut hors indication et unités non interchangeables de la toxine, chiffre suisse de cancer sans période inventée, anatomie après laryngectomie totale. La cohérence des onze titres, des délais de persistance et de la hiérarchie des urgences a été relue.

Aucun auditeur indépendant ni médecin n’a validé ces textes. Aucun score ni nombre de défauts médicaux graves restant n’est établi. Le classement est pédagogique, faute de prévalences comparatives documentées.

Rendu navigateur et mobile non vérifié. Les tentatives antérieures sur cet environnement étaient bloquées (Chromium `file://` refusé, téléchargement Playwright HTTP 403) ; aucun nouveau test visuel n’est revendiqué ici et aucune restriction n’a été contournée. La structure native des popovers a été contrôlée statiquement.
