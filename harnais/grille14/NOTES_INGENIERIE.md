# Notes d'ingénierie du Harnais · 27.10.2026

Ordre de Vial traité : règle absolue de la contraction, conservation des notions et des explications, abréviations et médicaments partout cliquables, taille non bloquante, LOT actif, autotest complet.

## 1. Règle absolue (contracteur)

`REGLE_ABSOLUE` (constante encadrée de `harnais/contracteur/contracteur.py`) : imprimée en tête de `contracter`, `verifier`, `etat` ; écrite dans le docstring ; injectée dans la `memoire` des auditeurs B1…B5 (`grille_agent.py`). Contracter peut reformuler plus concis ; jamais résumer.

## 2. Vérification de conservation (`verifier`)

| Notion | Exigence | Méthode |
|---|---|---|
| nombres, médicaments (marques, DCI), sources de la liste, abréviations définies | 100 % | ensembles avant/après |
| couples comparateur + valeur + unité | 100 % au total **et** dans la phrase qui couvre | `RX_UNITE`, normalisation (« supérieure à » → « > », « jours » → « j », 0,40 → 0.4) |
| termes cliquables, renvois `[Sn]`, lemmes noms | ≥ 95 % | ensembles |
| tableaux, 14 points | intacts | lignes par tableau, titres h3 |
| phrases d'explication (car, parce que, donc, ainsi, provoque, entraîne, explique, permet, mécanisme, afin de, pour que, →) | couvertes ≥ 85 % | lemmes NOUN, PROPN, ADJ, NUM, VERB (sauf être, avoir, faire, pouvoir, devoir, aller) ; meilleure phrase ou deux phrases voisines (scinder est permis) |
| autres phrases | couvertes ≥ 80 %, sinon redite d'une phrase conservée (≥ 80 % et mêmes marqueurs) | index inversé des lemmes |
| négations, conditions (ne… pas, jamais, sans, aucun, contre-indiqué, interdit, éviter, seulement, uniquement, si, sauf) | présentes dans la fenêtre qui couvre ; totaux non diminués (phrases distinctes) | `MARQ` |
| excès objectif | redites quasi identiques ≤ 3 (Jaccard ≥ 0,8, corps du cours) ; phrases > 30 mots ≤ 6 % (mesure du contrôle de forme) ; phrases nominales non augmentées | — |

- **Plus de quota de volume** : le gain est affiché, jamais exigé (`CIBLE.json` n'est plus utilisé pour décider).
- La contraction mécanique est appliquée aux deux côtés avant la comparaison des phrases : elle ne peut pas créer de faux refus.
- Contraction mécanique durcie : formule creuse retirée seulement en début de phrase ; « Ainsi », « afin de », « dans la mesure où », « de manière à », « c'est-à-dire » ne sont plus touchés (connecteurs d'explication) ; « n'est en mesure de » protégé ; dédoublonnage limité aux paragraphes sans balise.
- Détecteur de phrases verbales : spaCy (VERB, AUX, forme finie), flèche, question ; sinon verbe conjugué mal étiqueté par le petit modèle (mot en minuscules entre un sujet et un déterminant ou un nombre : « la périménopause dure 2 ans »).
- Performance : environ 2 s pour 18 000 mots (spaCy) ; cache des phrases en mémoire (une phrase inchangée n'est jamais réanalysée).

## 3. Abréviations et médicaments (`forme_interactive.py`)

- Habillage de **chaque** occurrence, hors titres (h1–h6, summary, caption), hors balises, hors bibliographie (`details.refs`, bandes `.sb`) ; l'onglet Rappel mémoire est habillé mais jamais contrôlé (texte généré par script).
- Sigles : `<abbr class="ab" data-k="X">` + une règle CSS par sigle dans `<style id="sigles">` (définition écrite une fois) ; également dans les fenêtres (survol imbriqué : `.tm:hover>.df`).
- Médicaments : lien `<a class="tm med" data-auto="1" href="#med-…">` vers une bande unique par médicament (copie de la fenêtre canonique) ; jamais dans une fenêtre (les chefs de file y sont listés par construction).
- Premier essai (copie de la fenêtre à chaque occurrence) : fichiers jusqu'à 550 Ko ; solution retenue : +25 à 50 Ko par fichier.
- Contrôles CRITIQUES : `manques_forme` (sigles sans définition, médicaments sans fenêtre), `fenetres_incompletes` (DCI, classe ATC, groupe et chefs de file, indications, posologie AIPS), sur la version convertie.
- Les mesures de la grille (mots, phrases, termes, point 13) se font sur `sans_habillage(conv)` : l'habillage ne coupe pas les mots et ne gonfle aucun compte.

## 4. Taille

`BANDE.json` : 80–200 Ko, `"bloquante": false`. Grille : MOYEN ; `checkpoint.py` : AVERTISSEMENT ; `controle_lot.py` : avertissement de lot.

## 5. Moteur (`grille_agent.py`)

LOT actif lu dans `harnais/grille14/LOT_ACTIF` (repli `G14_LOT`, puis 001) ; LOT inconnu, arguments faux, fichier absent : message clair (code 2) ; verrou pris dans `fin` (détenteur nommé) ; `attendre` s'arrête sur un fichier BLOQUÉ ; panne du checkpoint : incident, code 6, aucun essai ; registre des essais sous verrou ; signature des scores d'auditeur (une hausse n'est pas une stagnation) ; en test, mémoire et preuve du bracelet dans `.cache/test_g14`.

## 6. Autotest

`python3 harnais/grille14/autotest.py` : 108 tests, environ 54 s, bac à sable, aucun commit réel. Contraction refusée si explication, mécanisme, négation, condition, unité, seuil, comparateur, nombre, médicament, DCI, terme, renvoi, source, ligne de tableau, point, définition de sigle perdus, phrase rendue nominale ou phrase supprimée sans être une redite ; acceptée pour une redite, une reformulation concise, une phrase scindée, une absence de réduction. Sigle non survolable et médicament non cliquable refusés. Non-régression sur les 16 fichiers réels de LOT_001 (lecture seule, empreintes vérifiées) contre le moteur de référence `4e2a2f1e`.

## 7. LOT_001 : écarts nouveaux (sigles sans définition / médicaments sans fenêtre)

Mesure en lecture seule, après conversion (distincts / occurrences). Aucune autre régression.

| Fichier | Sigles | Médicaments | Fenêtres incomplètes | Taille convertie |
|---|---|---|---|---|
| Phase A | 67 / 346 | 3 / 11 | 10 | 222 Ko |
| DX.1 | 26 / 99 | 4 / 5 | 0 | 256 Ko |
| DX.2 | 57 / 226 | 1 / 1 | 0 | 226 Ko |
| DX.3 | 55 / 346 | 0 / 0 | 0 | 220 Ko |
| DX.4 | 47 / 146 | 5 / 8 | 0 | 220 Ko |
| DX.5 | 34 / 150 | 3 / 5 | 1 | 173 Ko |
| DX.6 | 62 / 296 | 5 / 9 | 12 | 209 Ko |
| DX.7 | 56 / 518 | 9 / 65 | 0 | 227 Ko |
| DX.8 | 44 / 180 | 28 / 155 | 0 | 220 Ko |
| DX.9 | 71 / 244 | 8 / 22 | 0 | 226 Ko |
| DX.10 | 25 / 102 | 5 / 7 | 0 | 215 Ko |
| DX.11 | 66 / 214 | 15 / 32 | 0 | 232 Ko |
| DX.12 | 117 / 681 | 6 / 20 | 1 | 217 Ko |
| DX.13 | 98 / 414 | 11 / 15 | 0 | 236 Ko |
| DX.14 | 82 / 548 | 20 / 78 | 0 | 188 Ko |
| DX.15 | 76 / 580 | 5 / 6 | 0 | 213 Ko |

Sigles les plus fréquents sans définition : VIH, HUG, TSH, CRP, IRM, TDM, TEP, ECG, IMC, SC. Médicaments sans fenêtre : surtout des DCI citées en passant (aténolol, bisoprolol, ritonavir, amoxicilline, thiamazole, insuline, duloxétine). Une ligne « Abréviations : » complète par fichier et quelques fenêtres de médicament suffisent : chaque occurrence est ensuite habillée automatiquement. Détail : `.cache/test_g14/ecarts_LOT_001.json` (régénéré par l'autotest).

## 8. Limites connues et points restants

- Lettre + chiffres (T3, T4, B12, CD4 n'en fait pas partie) : habillés s'ils sont définis, jamais signalés (codes, stades, vitamines indiscernables).
- Majuscules sans ® d'une marque inconnue (VEOZA) : signalées comme sigles tant qu'aucune fenêtre ne les nomme.
- Seuils de couverture (85 / 80 / 80 %) et détecteur de phrases nominales : à calibrer à l'usage (décision de Vial).
- `prompt_projet.py` mentionne encore « 100–200 Ko, > 200 Ko jamais » : à aligner si Vial confirme la bande indicative.
- LOT_001 déjà fusionné : les écarts ci-dessus bloqueraient un nouveau checkpoint ; reprise à décider par Vial.
