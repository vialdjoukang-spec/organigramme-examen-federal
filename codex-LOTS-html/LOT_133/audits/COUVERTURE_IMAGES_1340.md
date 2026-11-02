# Couverture iconographique clinique — LOT_133 — passe 1340

Les dix parties 9 ont été extraites avec `harness/cache_controles.py extraire --points 9 --html`. Les parties 8 et 10 de DX10 ont également été lues pour choisir sa véritable fenêtre d’imagerie. Les parties 1 ont été extraites pour confirmer le périmètre diagnostique. Aucun HTML complet n’a été affiché.

Le plan est un livrable de préparation : **0 image acquise, 0 pixel inspecté, 0 annotation localisée** dans cette tâche. Les réserves iconographiques de `RESERVES_CLINIQUES_1252.json` restent ouvertes. Les sommes SHA des HTML et des extractions P9 figurent dans le JSON.

## Liens réellement présents

Dans les sections retenues, seul le bouton-titre est cliquable. Il ouvre la fenêtre `dxN-detailP` existante ; aucun signe individuel n’est cliquable. Le JSON distingue le texte exact du déclencheur, le passage d’ancrage existant et le signe proposé. Il ne prétend pas qu’un nouveau lien existe.

| DX | Fenêtre existante | Priorité clinique proposée | Limite essentielle |
|---|---|---|---|
| 1 | `dx1-detail9` | Hématome intraparenchymateux spontanément hyperdense, exemple du versant hémorragique du cours | Ce cliché illustre un AVC hémorragique, pas tous les AVC. Une TDM normale n’exclut pas une ischémie précoce ; aucune étiologie, datation précise ou décision thérapeutique ne découle de cette coupe seule. |
| 2 | `dx2-detail9` | Plages purpuriques, avec nécrose seulement si visible et documentée | Illustration de la lésion à prélever, non cliché d’imagerie interne ni preuve microbiologique ; un purpura ne suffit pas à diagnostiquer sepsis, CIVD ou infection invasive à méningocoque. |
| 3 | `dx3-detail9` | Pneumothorax visible : ligne pleurale viscérale avec absence de trame pulmonaire en périphérie | Illustre une cause possible d’IRA, sans établir la gravité gazométrique ; sensibilité limitée en décubitus et pour petits pneumothorax. La prise en charge urgente ne dépend pas d’une illustration pédagogique. |
| 4 | `dx4-detail9` | Sphérocytes dans un cas documenté d’hémolyse | La morphologie soutient une orientation ; elle ne prouve ni l’anémie ni son caractère immunologique. TDA, bilan d’hémolyse et contexte restent nécessaires ; pas de diagnostic d’AHAI sur pixels seuls. |
| 5 | `dx5-detail9` | Calcul de la voie biliaire principale hyperéchogène avec cône d’ombre postérieur, si effectivement présent | Un examen négatif ne suffit pas à exclure un calcul. La dilatation seule n’identifie pas la cause, et l’absence de cône d’ombre n’exclut pas tout petit calcul. |
| 6 | `dx6-detail9` | Épanchement péritonéal autour du foie, illustrant l’ascite | L’ascite ne prouve pas la cirrhose et l’aspect échographique ne diagnostique pas une infection du liquide. La ponction diagnostique répond à une question différente ; image isolée insuffisante pour guider un geste. |
| 7 | `dx7-detail9` | Dilatation du ventricule gauche dans un cas documenté d’insuffisance cardiaque | Un cliché fixe illustre la structure, pas la fonction systolique/diastolique ni les pressions. Aucun calcul de FEVG ou diagnostic de HFpEF ne sera inféré ; une séquence authentique serait nécessaire pour l’analyse du mouvement. |
| 8 | `dx8-detail9` | Persistance de la lumière veineuse sous compression, compatible avec TVP dans le cas documenté | Le panneau compte comme une unité pédagogique, mais comporte deux acquisitions réelles. Ne prouve pas la date de la thrombose ni l’absence de TVP ailleurs ; un flux Doppler conservé n’exclut pas une obstruction partielle. |
| 9 | `dx9-detail9` | Schizocytes orientant vers une fragmentation érythrocytaire | Les schizocytes ne prouvent pas un PTT ni un déficit ADAMTS13. La corrélation avec hémolyse, plaquettes, coagulation et contexte distingue MAT/CIVD/autres causes ; l’absence dans un champ n’exclut pas une MAT. |
| 10 | `dx10-detail8` | Masse ou nodule pulmonaire dans un cas de cancer primitif documenté | Une coupe ne détermine ni histologie, ni PD-L1, ni profil moléculaire, ni TNM complet. P9 concerne les biomarqueurs ; la fenêtre pertinente retenue est P8, consacrée au bilan d’extension. |

## Choix et limites de couverture

- DX2 : photographie de la lésion à prélever, cohérente avec la biopsie cutanée décrite en P9 ; ce n’est pas une preuve microbiologique ni une image radiologique.
- DX7 : le cliché fixe illustre une anomalie structurelle ; aucune FEVG ni hypokinésie ne sera inventée à partir de pixels statiques.
- DX8 : une unité pédagogique avant/sous compression exige deux acquisitions réelles du même segment. Une photographie isolée ne suffirait pas à démontrer la non-compressibilité.
- DX10 : P9 traite histologie et biomarqueurs. Le scanner est présent en P8 (bilan d’extension), retenue pour l’insertion, et en P10 (algorithme). Aucune substitution par une immunohistochimie ne remplit artificiellement l’objectif d’imagerie pulmonaire.

Les signes proposés sont des objectifs de recherche, pas des constatations sur des images disponibles. Aucun URL, droit, cas clinique, mesure ni coordonnée de flèche n’est inventé. Un schéma peut expliquer un mécanisme, mais ne constitue jamais des pixels cliniques authentiques. Le plan privilégie une illustration pertinente par diagnostic sans prétendre couvrir toutes les lésions de chaque syndrome.

## Vérification de cette passe

JSON relu et parsé ; dix entrées distinctes ; ancrages textuels contrôlés contre les extractions ; chaque bouton et chaque ID de fenêtre retrouvé. Aucun nouvel audit clinique indépendant ni contrôle de rendu revendiqué. Les exigences de provenance, droits, paires originale/annotée et inspection restent celles du pipeline existant.
