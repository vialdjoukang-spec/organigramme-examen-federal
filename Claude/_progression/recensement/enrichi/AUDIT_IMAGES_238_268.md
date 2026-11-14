# Audit radiologique des images IMG-238 à IMG-268 (PE_MS.json), 14.11.2026

Méthode : chaque copie `_verif/IMG-xxx.png` a été regardée. Légende et licence de chaque article relues dans le XML Europe PMC. Pour 262, les figures source (fichiers `i210247-2` et `-3` de PMC9948152) ont été téléchargées et comparées à `img/IMG-262_patho.jpg`.

**Verdict : corrections requises** (1 critique, 4 majeurs).

## 1. Critique

| id | Défaut constaté | PATCH exact |
|---|---|---|
| 262 RCIU | L'image retenue est le fichier `i210247-2` de PMC9948152. Le bandeau de l'appareil y indique « 3 Trim ». Le spectre passe **sous la ligne de base** en fin de diastole, au point désigné par la flèche « ED » : c'est une **diastole inversée (REDV)**, et non une diastole nulle. Le vrai tracé AEDV du 2e trimestre est le fichier `-3`, où la diastole reste à 0 au niveau de « EDV ». Le texte enseigne donc le mauvais stade. | Option 1, garder l'image et corriger le texte : `technique` = « Doppler pulsé de l'artère ombilicale au troisième trimestre : diastole inversée (REDV) ; annotations des auteurs » ; `lesion` = « diastole inversée (REDV) » ; `semio` = « Le flux passe sous la ligne de base en fin de diastole : c'est le stade le plus sévère, à haut risque d'acidose et de mort fœtale, qui impose une décision d'extraction selon le terme. » Option 2 : remplacer l'image par le fichier `i210247-3` (AEDV, 2e trimestre, CC BY 4.0), avec le repère 1 sur la pointe « EDV », à poser puis contrôler sur `_verif`. |

## 2. Majeurs

| id | Défaut constaté | PATCH exact |
|---|---|---|
| 242 HBP | Le **nom du patient** et la date figurent en clair dans le bandeau supérieur du cliché (`_verif`). Le dépôt est public : aucune donnée personnelle n'y est admise. | Recadrer `img/IMG-242_patho.jpg` pour supprimer la bande supérieure (environ 8 % de la hauteur). Recalculer ensuite le repère 1 : y = (42 − 8)/0,92 ≈ 37 ; x inchangé. Régénérer `_verif`. |
| 240 Rupture vésicale | Le cliché est en fenêtre large et presque noir. Il ne permet pas de voir la fuite de contraste que la `semio` décrit. La légende la mentionne, mais l'œil ne la retrouve pas. L'examen n'est pas une cysto-TDM, ce qui est bien déclaré. | Ajuster le fenêtrage (niveau et contraste) de `img/IMG-240_patho.jpg`, puis le déclarer dans `technique`. Si rien n'apparaît : `semio` = « La paroi du dôme s'interrompt (flèche) au contact d'une ascite abondante ; la fuite de contraste se démontre au mieux par une cysto-TDM rétrograde ». |
| 252 Torsion d'annexe | La `semio` du repère 3 parle de « flux conservé ». La légende de la fig. 6 dit au contraire « absent ovarian vascularity » chez les deux patientes. Les signaux colorés de B sont extra-ovariens. | Repère 3 : `lesion` = « ovaire sans flux interne » ; `semio` = « Chez la deuxième patiente, l'ovaire ne contient aucun signal couleur ; les signaux visibles restent extra-ovariens. » Le message « un flux conservé n'exclut pas la torsion » passe dans `syndrome`. |
| 248 Abcès prostatique | Les pointes des repères tombent à la limite entre l'abcès et le parenchyme échogène, et non dans les plages « AB » des auteurs. | Repère 1 : x = 36, y = 33. Repère 2 : x = 64, y = 37. Contrôler sur `_verif`. |

## 3. Mineurs

| id | Défaut constaté → PATCH |
|---|---|
| 247 | Licence « CC BY-SA » erronée : la source (SA J Radiol, AOSIS) porte « Creative Commons Attribution License » → `licence` = « CC BY ». La description « vaisseaux fémoraux (flèche blanche) ; hydrocèle (flèche noire) » ne figure pas dans la légende de la fig. 2 → la retirer ou la sourcer dans le texte. |
| 255 | Le repère 2 (72 ; 58) tombe sur le stroma central → déplacer sur la couronne folliculaire, x = 82, y = 45. Le contexte (stimulation ovarienne, hyperstimulation sévère) est à ajouter dans `technique`. |
| 254 | Le normal vient d'une patiente traitée pour un cancer du rectum. C'est déclaré, et la coupe est sus-jacente à la tumeur : utérus et ovaires normaux. Remplacement souhaitable mais non bloquant. |
| 249 / 252 / 253 / 255 | Le même ovaire normal (PMC4745314, « unremarkable scan ») est utilisé quatre fois. La réutilisation n'est pas trompeuse. Pour 252, la technique diffère (sus-pubienne pédiatrique contre endovaginale adulte) → à déclarer dans `technique`. |
| 239 | « même patiente » → « même patient » : la prostate est mesurée, il s'agit d'un homme. |
| 244 | Le normal vient d'un garçon de 12 ans, le patho d'un homme de 59 ans : âge à déclarer (c'est déjà fait pour le normal). |
| 265 | Le normal est en T2, le patho en STIR → préciser « séquence différente » dans `technique`. |

## 4. Contrôles sans défaut

238, 241, 243, 245, 246, 249, 250, 251, 253, 256, 257, 258, 259, 260, 261 (fig. 9 vérifiée), 263, 264, 266, 267, 268.

Licences : CC BY 2.0, 3.0 ou 4.0, vérifiées dans le XML, sauf l'étiquette de 247. Le crédit est présent partout.
