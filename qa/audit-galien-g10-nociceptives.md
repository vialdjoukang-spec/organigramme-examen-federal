# Contre-lecture indépendante · G10 · douleurs nociceptives

Date : 18.10.2026. Périmètre : les deux nouvelles fiches `douleur-nociceptive-somatique` et `douleur-nociceptive-viscerale`, les cinq définitions associées et leurs deux nouvelles références. Diff examiné contre `origin/main`, instantané public 4edba7f. Aucune validation médicale humaine n’est revendiquée.

## Sources effectivement relues

- HUG, *Antalgie dans les services médicaux et chirurgicaux adultes*, novembre 2023 : couverture, pages 3–9, 14–15, 19–20 et 31 ; colophon vérifié. Lecture ciblée du PDF officiel téléchargé, et non lecture intégrale. URL : https://www.hug.ch/sites/interhug/files/structures/reseau_douleur_/documents/antalgie_2023_a6_web.pdf
- HUG, *La douleur abdominale chronique d’origine digestive*, 2023 : pages 3–6, mécanismes, examen et signes d’alarme. Lecture ciblée du PDF officiel téléchargé. URL : https://www.hug.ch/sites/interhug/files/2023-09/strategie_douleur_abdominale_chronique_2023_avec_lien.pdf
- HUG, *Douleur — aide-mémoire destiné aux soignants*, mise à jour 28.03.2025 : définitions, anamnèse, prise en charge et précautions des antalgiques, effectivement relues. URL : https://www.hug.ch/soins-palliatifs-aide-memoire-destine-aux-soignants/douleur

Le guide antalgique plus ancien et le poster multicolonne ne fondent pas cet avis. Les formulations discutables du document abdominal sur les « viscères insensibles » et les « voies efférentes sensitives » n’ont pas été reproduites.

## Verdict par élément

| Élément | Verdict documentaire | Motifs |
|---|---|---|
| Douleur nociceptive somatique | Accepté avec réserves explicites conservées | Le mécanisme reste général et ne se réduit pas à une lombalgie. L’examen recherche la cause et, après chirurgie, des complications locales. Les AINS restent liés à une indication adéquate en douleur aiguë, avec risques digestifs, rénaux et cardiovasculaires ; un opioïde éventuel exige une surveillance de la vigilance et de la respiration. Aucun dosage HUG n’est importé. |
| Douleur nociceptive viscérale | Accepté avec réserves explicites conservées | La fiche distingue mécanisme et étiologie. Elle borne les signes d’alarme digestifs au contexte abdominal chronique et ne généralise ni ce bilan ni cette temporalité à toutes les douleurs viscérales. L’antalgie tient compte des fonctions rénale, hépatique et respiratoire ; la prévention de la constipation reste adaptée à la cause abdominale. |
| Nocicepteur, nociception, viscéral | Accepté | Définitions brèves compatibles avec les passages relus ; aucune confusion entre mécanisme et diagnostic étiologique. |
| Douleur somatique | Accepté après correction | La définition demeure située dans la classification des douleurs ; l’alias global ambigu a été retiré. |
| Irradiation douloureuse | Accepté après correction | La définition décrit l’extension d’une douleur ; l’alias global ambigu a été retiré. |

Les deux fiches conservent leurs prévalences, sex-ratios et posologies suisses « À vérifier ». Les fréquences de maladie avancée, les pourcentages de sous-groupes, les doses et les tableaux numériques d’adaptation HUG ne sont pas transposés. L’amélioration sous antalgique ne sert pas de preuve diagnostique. `data/ck/prev.json` est identique à `origin/main` : aucun gain de couverture quantitative n’est revendiqué.

## Fautes de portée corrigées pendant la contre-lecture

1. **Alias global « somatique » associé à « Douleur somatique ».** Il aurait aussi proposé la définition de douleur pour des occurrences existantes comme « thérapie somatique », « mutation germinale ou somatique » et « bilan somatique ». Correction : retrait du champ `alias` de `douleur-somatique`, vérifié dans le fichier final. Les autres textes n’ont pas été réécrits pour masquer le problème.
2. **Alias global « irradiation » associé à « Irradiation douloureuse ».** Il aurait proposé cette définition pour l’irradiation thérapeutique et les mentions d’imagerie « sans irradiation ». Ces deux emplois existent déjà dans `hyp.json` et `glo.json`. Correction : retrait du champ `alias` de `irradiation-douleur`, vérifié dans le fichier final.

## Vérifications et limites

Les fichiers finaux ont été relus après retrait des deux alias. La session principale signale la reconstruction et G1–G8 verts, sans nouveau signalement ; Lyncée indique zéro terme nouveau, référence 3559. Ces résultats communiqués sont distincts de la présente contre-lecture documentaire.

Le Chromium attendu par Playwright est absent : `work/tests-complets.log` indique un exécutable introuvable dans `chromium_headless_shell-1234`. Un Chromium système existe toutefois : `/usr/bin/chromium`, version 154.0.8037.57, vérifiée pendant cet audit. La suite complète n’est pas validée localement par l’exécution consignée. La CI exacte de la tête proposée, y compris les contrôles navigateur et visuels requis, doit être verte avant fusion.

**Avis documentaire final favorable, sans défaut bloquant identifié sur ce lot après les corrections décrites.** Les réserves explicites restent ouvertes ; cet avis ne lève pas les inconnues et ne constitue pas un accord médical humain.

Complément de vérification du parent : 82/82 tests du socle CK réussis. L’essai avec CHROME_PATH=/usr/bin/chromium démarre le navigateur, puis la navigation file:// est refusée par net::ERR_BLOCKED_BY_ADMINISTRATOR. Aucun contournement tenté. La suite complète demeure à vérifier dans la CI exacte ; logs locaux hors dépôt.
