# Étude — conscience embarquée et coût en jetons

Mesures du 31.10.2026. Facteur 3,12 octets par jeton, le même proxy que `compteur_conso.py` et `etude/chiffres.json`. Aucun chiffre de cette page n'est un rappel de modèle : ou il est lu dans un fichier cité, ou il est calculé à partir de ceux-là, ou il est marqué estimation avec la méthode.

## Choix

Conscience légère, exécutée par le rédacteur, pas un second audit. La conscience médicale (cohérence, définitions, seuils, éléments centraux absents) est distincte de la conscience linguistique (terminologie). On ne restaure pas le duo. Le couple « duo + conscience » est une estimation sans mesure directe : il n'existe aucun LOT duo pur qui ait été audité.

## Ce que dit l'analyse git + transcripts (non recomptée ici pour le 73)

Seuls le V0 de LOT_134 (01:55–02:06) et son DX.1 approfondi (02:33) relèvent du duo. Le reste de LOT_134 et LOT_135 a été approfondi en harnais seul (08:50, 10:07) : leurs audits portent donc sur du harnais seul.

`corrections.jsonl` : graves natifs 8 (LOT_134) et 6 (LOT_135), critique 0. Type langue : 20 et 30. Type différent de langue : 29 et 16. `chiffres.json` compte le médical à 30 et 16 (une correction `medical_langue` de plus sur 134). Les 30 corrections de langue du LOT_135 sont le décompte `type == langue` du fichier (46 lignes en tout).

Le chiffre « 73 retraits/ROUGE » sur le harnais seul 136–154 (0,83 par fichier, contre 2,09 par fichier audité) vient de cette analyse. Il n'a pas été recompté par ce script. L'arithmétique du 2,09, elle, se vérifie : (30+16)/22 fichiers = 2,09. 73/88 = 0,83 si le dénominateur est 8 LOT × 11 HTML.

## Backtest LOT_134 et LOT_135

Instantané : `git show` du parent du premier commit dont le sujet contient « audit médical » (fond) ou « conformité » (langue). 11/11 fichiers pour LOT_134. 9/11 pour le fond de LOT_135 (DX.7 et DX.8 n'ont pas ce mot dans le sujet ; les 6 graves sont sur des fichiers qui ont l'instantané : Phase A, DX.2, DX.5, DX.9).

Règle de classe, explicite. Les audits n'emploient pas le mot critique. On ne promeut pas « grave » en critique.

- critique : 0 correction d'audit.
- grave : gravité d'audit « grave » et type différent de langue.
- mineure : léger, moyen, ou langue.

Appariement : au moins deux mots de cinq lettres en commun entre l'ordre et l'avant/après, ou un pont (ne explique → n'explique, sigle, Alvarado, 14/100, 30 mm). Ce n'est pas un jugement clinique. Un même ordre peut rappeler deux corrections (Alvarado, SOFA).

| | critique | grave | mineure |
|---|---:|---:|---:|
| LOT_134 or / rappelés | 0 | 8 / 4 (50 %) | 41 / 2 (4,9 %) |
| LOT_135 or / rappelés | 0 | 6 / 0 (0 %) | 40 / 11 (28 %) |
| Ensemble | 0 | 14 / 4 (29 %) | 81 / 13 (16 %) |

Précision des ordres (un ordre est vrai s'il rappelle au moins une correction) : LOT_134 3/10 = 30 %, LOT_135 4/4 = 100 %, ensemble 7/14 = 50 %. Les 7 écarts du LOT_134 sont tous « AIPS non développé » sur des fichiers où l'audit n'a pas écrit cette correction. Aucun BLOQUANT sur ces instantanés.

Les 4 graves rappelés du LOT_134 sont les deux phrases Alvarado « stratégie opératoire » et les deux confusions SOFA / qSOFA. Les 6 graves du LOT_135 (14/100 contre 14/1 000, 500 ml, site de décompression) ne sont pas dans le corps pédagogique sous une forme que la règle attrape : le parent de l'audit de la Phase A ne contient pas la chaîne « 14/ ». L'erreur vit dans le fond, pas dans une coquille.

Autotest synthétique : 0 échec (`autotest.py`). Les fautes injectées (8 000 mg/j, 500 µg, kaliémie 25 mmol/l, Ottawa absent, Alvarado sans réserve) sont prises. Les doses dans les plafonds lus ne le sont pas.

## LOT_149 à 154 (texte actuel, lecture seule)

12 ordres, 0 BLOQUANT. Voulus par la mission (retraits connus) : seuils 0/1 h (LOT_150), Ottawa et Fleischner (LOT_152), de Winter, Wellens, S1Q3T3 (LOT_154). Signaux posologiques prévus : Konakion sans plafond extrait, prednisone sans plage dans le cache (LOT_151). Linguistique utile : AIPS nu (DX.6 et DX.9 du 154), mmol/L (DX.7).

Faux positif estimé : 1 sur 12, la ligature « Oedème » → « œdème » (DX.2 du 152). Forme lisible, gravité mineure, pas une alarme de dose. LOT_149 et LOT_153 : 0 ordre.

## Jetons

Sortie plafonnée, une passe `fichier` par HTML.

- Backtest, instantanés d'audit : LOT_134 677 jetons pour 11 fichiers ; LOT_135 293 jetons pour 9 fichiers. Moyenne 48,5 jetons par fichier, soit 533 jetons pour 11 fichiers.
- Corrections induites : octets du champ `apres` des corrections rappelées / 3,12. LOT_134 : 169. LOT_135 : 260. Moyenne 214 jetons par LOT. Les ordres non appariés ne sont pas comptés comme une réécriture.
- Surcoût retenu pour le tableau : 533 + 214 = 747 jetons par LOT.
- Contrôle sur le texte actuel 149–154 (sortie seule, 11 fichiers, pas de champ `apres`) : 302, 365, 376, 397, 302, 488. Moyenne 372 jetons par LOT.

Harnais seul, `chiffres.json` : 2 471 293 jetons pour 7 LOT, soit 353 042 par LOT. Sans harnais : 4 618 963 / 8 609 394 / 11 738 644 (basse, centrale, haute). Gain publié : 46,5 % / 71,3 % / 78,9 %.

Avec la conscience, 7 × 747 = 5 229 jetons de plus sur l'ensemble. Total 2 476 522. Gain : 46,4 % / 71,2 % / 78,9 %. La baisse est d'un dixième de point sur la centrale.

## Tableau

| Mode | Jetons par LOT | Gain contre sans harnais | Erreurs résiduelles | Confiance |
|---|---:|---|---|---|
| Harnais seul | 353 042 | 71,3 % [46,5–78,9] | Critique 0 dans les audits. Graves natifs 8 et 6, non vus par la porte. Retraits/ROUGE 0,83 par fichier sur 136–154 (analyse externe, non recomptée) contre 2,09 corrections médicales par fichier audité. | Mesure `chiffres.json` pour les jetons. Le 0,83 est donné, pas remesuré. |
| Harnais seul + conscience | 353 789 | 71,2 % [46,4–78,9] | Sur le backtest : critiques or 0 et gold 0. Graves résiduels 4/8 et 6/6 (rappel 4/14). Mineures résiduelles 68/81. Les retraits Ottawa, Fleischner, Wellens, de Winter, S1Q3T3 et seuils 0/1 h sont signalés sur 150, 152 et 154. | Mesure du backtest. L'appariement de mots sous-estime un rappel réel et ne juge pas le fond. Confiance moyenne sur les absences nommées et la posologie chiffrée ; basse sur le fond clinique que l'audit a corrigé en prose. |
| Duo (harnais + routage) + conscience | non mesuré | non mesuré | non mesuré | Estimation sans mesure directe. |

## Duo : estimation sans mesure directe

Il n'y a pas de LOT duo pur audité. On ne peut donc pas mesurer le gain d'un duo restauré, avec ou sans conscience.

`ROUTAGE_GROK.jsonl` fait 33 077 octets de journal. Ce n'est pas un coût de modèle. `chiffres.json` ne sépare pas les jetons du V0 (01:55–02:06) ni du DX.1 (02:33) du reste du LOT_134. Les 733 271 jetons d'audit des deux LOT sont le coût d'audits tombés sur du harnais seul, pas la preuve qu'un routage évite des erreurs.

Si l'on réintroduisait ces audits, l'ordre de grandeur déjà mesuré est 733 271 jetons pour deux LOT, soit environ 367 000 par LOT audité, à comparer aux 747 de la conscience. Ce n'est pas un coût du duo : c'est le coût des audits que l'ordre de Vial a sortis de la boucle.

## Recommandation

Garder le harnais seul et ajouter la conscience au prompt des prochains rédacteurs. Ne pas restaurer le duo. Le surcoût mesuré (747 jetons par LOT) laisse le gain à 71,2 % au lieu de 71,3 %. La conscience attrape le geste « retirer plutôt que sourcer » sur les éléments centraux nommés, que ni la porte ni la certitude ne voient. Elle ne remplace pas un audit de fond : zéro des six graves du LOT_135.
