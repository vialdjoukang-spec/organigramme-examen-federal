# PROMPT LOTS — USINE DE PRODUCTION « PROFILES » (version Lo_9.11.26.claude)

> **Statut.** Ce prompt est la référence rédactionnelle de la production des LOTs. Il intègre le fond utile de `PROMPT_ULTIME_PRODUCTION_LOTS_V0.md` et de `PROMPT_RUBRIQUE_UNE_PASSE.md` (LOT_131) : 14 points, Phase A et Phase B, sources suisses puis européennes, AIPS, audit indépendant et dépôt 1 + 10 ; il en fixe l'organisation et les contrôles.
> **Lecture.** Le prompt se lit de haut en bas, une fois. La partie MACRO fixe le *quoi*, la partie MICRO le *comment*, puis la partie MÉTA le *contrôle* et le *coût*. Les annexes contiennent les prompts instanciables et les outils exécutables. Aucune phrase n'est décorative : chacune est une injonction.
> **Priorité.** Un ordre écrit de Vial, consigné dans `DECISION_SEANCE.md`, prime sur ce prompt pour la durée et le périmètre qu'il nomme. Hors de ce périmètre, ce prompt s'applique.

---

## SOMMAIRE

- **MACRO** — M1 Mission · M2 Lois de vérité · M3 Lexique · M4 Architecture d'un LOT · M5 Chaîne de production · M6 Rôles et routage
- **MICRO** — µ1 Phase A · µ2 Phase B · µ3 Les 14 points · µ4 Rédaction · µ5 Fenêtres · µ6 Images · µ7 Gabarit HTML · µ8 SSP transversaux
- **MÉTA** — Θ1 Contrôle des trois axes · Θ2 Portes et verdicts · Θ3 Audit ciblé · Θ4 Économie · Θ5 Anti-collision · Θ6 Traçabilité · Θ7 Erreurs déjà commises · Θ8 Stratégie d'achèvement
- **ANNEXES** — A Prompts instanciables · B Contrats JSON · C Outils exécutables · D Commandes

---

# PARTIE MACRO — CE QUE L'ON CONSTRUIT

## M1. Mission

1. Le projet produit **248 LOTs**, soit un LOT par situation de soins (SSP) du référentiel **PROFILES 2023**. LOT_001 correspond à G1 et LOT_248 à O7.26, selon l'ordre officiel `smifk-cims.ch/profiles-2023/ssps`.
2. Chaque LOT doit permettre à Vial de répondre juste à toute question d'examen fédéral sur le sujet, puis de prendre le patient en charge le lendemain sans danger.
3. La **question finale** conclut chaque fichier : « Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ? » Si la réponse est « non », le fichier ne passe pas la porte, quel que soit son score.
4. L'ordre de décision ne se discute pas : **Qualité → Exhaustivité du fond → Économie → Esthétique**. Un rang inférieur ne bat jamais un rang supérieur. Dès lors, on économise sur la forme, jamais sur le fond.

## M2. Lois de vérité (bloquantes)

| N° | Loi | Conséquence opérationnelle |
|---|---|---|
| LV1 | **Ponction, pas mémoire.** Chaque fait vient d'un extrait réellement lu, identifié et daté dans le paquet de l'entité. | Le modèle rédacteur ne reçoit que le paquet ; il n'a droit à rien d'autre. |
| LV2 | **Fond identique à la source, forme dans nos termes.** On reformule dans le lexique du projet (M3), mais le sens, le seuil, la dose et la condition restent ceux de l'extrait. | Le contrôle Θ1-A compare chaque nombre de la phrase avec l'extrait cité. |
| LV3 | **Nombres recopiés.** Un chiffre, un seuil, une dose, une durée ou un pourcentage se recopient tels qu'écrits : 89 % ne devient pas 90 %. | Si un nombre est absent de l'extrait cité, le verdict est ROUGE. |
| LV4 | **Une phrase factuelle, une citation.** Toute phrase porteuse d'un fait cite son extrait par `<sup class="r"><a href="#sb-ID">ID</a></sup>`. | Une phrase chiffrée sans citation reçoit le verdict ORANGE ; une citation inconnue, le verdict ROUGE. |
| LV5 | **Hiérarchie des sources.** On consulte d'abord la Suisse (OFSP, OFS, Obsan, Swissmedic/AIPS, Fedlex, ASSM, FMH, sociétés suisses), puis l'Europe (ESC, ERS, EASL, ESMO, ESCMID, EACS, EULAR, KDIGO, EMA). Une source internationale n'entre que si elle est reconnue en Suisse. | Une recommandation exclusivement américaine (FDA, AHA, ADA, IDSA) ne sert jamais de référence. |
| LV6 | **AIPS, mot pour mot.** Dose, voie, rythme, durée, adaptation rénale et hépatique, grossesse et allaitement viennent de l'information professionnelle Swissmedic : corpus local `AipsDownload_20261008.xml` d'abord, puis swissmedicinfo.ch en contrôle. Le numéro d'autorisation (5 chiffres) se lit dans le XML ; on ne le déduit jamais d'une URL. | Le corpus AIPS est un **index** (numéro d'autorisation → URL HTML française de l'information professionnelle) ; la liste Swissmedic HAM traduit la DCI en numéros. `paquet.py --aips --ham --dci` enchaîne DCI → numéro → URL → texte rapatrié en cache → rubriques (posologie, grossesse…). Une phrase de dose qui ne cite pas d'extrait `aips-*` reçoit le verdict ROUGE. On n'adoucit jamais un texte AIPS. |
| LV7 | **Affirmatif seulement.** Le cours énonce ce que les sources établissent. Il ne contient aucune formule de lacune : ni « donnée non trouvée », ni « chiffre non disponible », ni « à vérifier ». Si un chiffre manque, la phrase dit le fait qualitatif sourcé, et la lacune part dans `HELP.md`, hors du cours. | Si aucun extrait AIPS n'est disponible, la phrase indique la classe et la conduite sans aucun milligramme, et la molécule est inscrite dans `HELP.md`. |
| LV8 | **Version la plus récente.** Avant de citer une recommandation, on vérifie qu'aucune version plus récente n'existe (par exemple EACS 13.0 plutôt que 12.0, ERC 2025 plutôt que 2015). | L'extrait porte l'année ; l'auditeur compare cette année avec le registre des versions (`sources_reconnues.json`). |
| LV9 | **Honnêteté des actes.** On n'annonce jamais un dépôt, un audit, une lecture ou un contrôle qui n'a pas eu lieu. Un chiffre de bilan doit être démontrable par un fichier. | Chaque affirmation de statut renvoie à un JSON produit par un outil (controle3, MANIFESTE, digest). |

## M3. Lexique du projet (nos termes, à employer tels quels)

| Terme | Sens exact |
|---|---|
| **SSP** | Situation de soins PROFILES ; une SSP correspond à un LOT. |
| **LOT_XXX** | Unité de production : une Phase A et dix fichiers de Phase B, soit 11 HTML. |
| **Phase A** | Monographie de la SSP en 14 points, accompagnée de la liste DX.1 à DX.10, du tableau comparatif et de l'algorithme. |
| **Phase B** | Les dix monographies de diagnostics différentiels, à raison d'un fichier par DX. |
| **DX.i** | Diagnostic différentiel de rang i dans la liste canonique, ordonné par fréquence décroissante en Suisse. |
| **Rang E** | Rang d'exclusion d'un DX grave (E1, E2…), signalé par le badge 🚩. |
| **Point** | L'une des 14 rubriques du plan monographique (µ3). |
| **Îlot** | Bloc visuel rectangulaire (`section.ilot`) qui porte un point. |
| **Fenêtre** | Contenu secondaire ouvert au clic (`popover`) : définition, mécanisme, technique, monographie de médicament, piège. |
| **Paquet** | Ensemble des extraits sourcés d'une entité (`paquet.json`), produit par `paquet.py`. |
| **Extrait / ID** | Passage numéroté d'une source (`easl-3`, `aips-27257-2`) ; c'est l'unité de preuve citée. |
| **Contrat** | Fichier `contrat.json` qui fixe, pour chaque point, le titre, le contenu exigé, le budget d'octets et le squelette. |
| **Fragment** | Sortie brute du rédacteur pour un point (`fragments/pNN.html`). |
| **Gel** | Moment où la liste canonique ou une version de fichier est figée et signée par son SHA-256. |
| **Porte** | Contrôle bloquant qu'un fichier franchit, ou non, avec un verdict VERT, ORANGE ou ROUGE. |
| **Légion** | Ensemble des scripts clones (`mere.py` et `soldat.py`) qui collectent l'état des dépôts sans modèle et rendent un `DIGEST.md`. |
| **Planche** | Page HTML qui réunit toutes les images candidates d'un LOT pour un seul contrôle visuel. |
| **HELP** | Registre des lacunes de sources (`HELP.md`), qui reste hors du cours. |
| **MANIFESTE** | Octets et SHA-256 de chaque HTML gelé. |

## M4. Architecture d'un LOT

```text
lot en cours de production/LOT_XXX/            ← seul lieu d'écriture pendant la production
├── DECISION_SEANCE.md                           ← périmètre du jour (qui, quoi, branche)
├── evidence/                                    ← extraits bruts datés (*.txt), AIPS compris
├── PA/  paquet.json · contrat.json · fragments/pNN.html · fenetres/ · controle.json
├── DX.1/ … DX.10/  (même structure que PA/)
├── LISTE_DX_CANONIQUE.md                        ← gelée après la porte de Phase A
├── images/  CANDIDATS.json · PLANCHE.html · <sha>.jpg · figures.json
├── HELP.md · JOURNAL.md · CORRECTIONS_AUDIT.md
└── audits/  <fichier>.audit.json
LOT_Claude_Finaux/LOT_XXX/                       ← dépôt final, après la porte P4 seulement
├── LOT_XXX_Phase_A_V0.html
├── LOT_XXX_Phase_B_V0_DX.1.html … DX.10.html
├── MANIFESTE.json
└── audits/
```

- **Bande d'octets :** chaque HTML final pèse de 100 000 à 200 000 octets, bornes comprises. Sous 100 000 octets, une omission est présumée et l'on complète par des extraits nouveaux. Au-dessus de 200 000 octets, on comprime la forme. Le poids vient toujours de faits distincts, jamais d'un remplissage ; `controle3.py` repère les doublons et les phrases partagées entre fichiers.
- **Nom de fichier :** `LOT_XXX_Phase_A_V0.html` et `LOT_XXX_Phase_B_V0_DX.<i>.html`. Le `<h2>` d'un DX reprend `DX.<i> — <nom exact de la liste canonique>`.
- **Fin de fichier :** la dernière ligne est `<!-- FIN_FICHIER LOT_XXX_<PARTIE> -->`.

## M5. Chaîne de production (dix étapes, un seul passage)

| Étape | Action | Exécutant | Coût modèle | Sortie |
|---|---|---|---|---|
| E0 | Légion : état des LOTs, des branches et des collisions | `mere.py` | 0 | `DIGEST.md` |
| E1 | Réservation du LOT et ouverture de la branche `prod/lot-XXX` | script, plus `DECISION_SEANCE.md` | 0 | branche |
| E2 | Collecte des sources : URL tirées des registres de Vial, téléchargement en cache, extraits AIPS | `paquet.py` | 0 | `evidence/`, `PA/paquet.json` |
| E3 | Liste DX.1 à DX.10 : sélection, ordre de fréquence, rangs E | modèle fort (A-2) | moyen | `LISTE_DX_CANONIQUE.md` (brouillon) |
| E4 | Porte P1 de la liste : audit médical ciblé, puis gel | IA d'audit (A-4) | faible | liste gelée |
| E5 | Paquets des DX, lancés en parallèle (onze paquets) | `paquet.py` × 11 | 0 | `DX.i/paquet.json` |
| E6 | Rédaction point par point, en une passe | modèle local ou peu coûteux (A-1) | très faible | `fragments/` |
| E7 | Images : collecte, planche, inspection, puis figures | `images.py`, puis un seul contrôle visuel | 0, puis faible | `figures.json` |
| E8 | Assemblage et contrôle des trois axes | `assembler.py` + `controle3.py` | 0 | HTML + `controle.json` |
| E9 | Audit ciblé des seuls défauts et des points à risque, puis correction chirurgicale | IA d'audit (A-4), puis IA de rédaction (A-5) | faible | `audits/`, HTML corrigé |
| E10 | Porte P4, manifeste, dépôt final et fusion | scripts + CI | 0 | `LOT_Claude_Finaux/LOT_XXX/` |

**Règle d'un seul passage.** Un fragment reçu n'est jamais renvoyé au modèle pour être « amélioré ». La correction vise la phrase fautive, désignée par l'audit, et rien d'autre (A-5). Une étape ne relit pas un fichier dont le SHA-256 n'a pas changé depuis son dernier verdict.

## M6. Rôles et routage (gratuit d'abord)

> **Posture.** Ce prompt ne nomme aucune IA. Chaque IA qui le reçoit prend la posture que l'étape lui assigne (IA de rédaction, IA de haut niveau de raisonnement, IA d'audit, IA à capacité visuelle) et s'y tient ; c'est la posture, et non le nom de l'IA, qui fixe le niveau exigé.

| Tâche | Exécutant | Pourquoi |
|---|---|---|
| Comptage, tailles, balises, 14 points, doublons, cohérence A↔B, nombres contre extraits, SHA-256 | **Scripts** | Ces tâches sont déterministes ; un modèle n'y apporte rien. |
| Collecte et cache des sources, AIPS, images, planches | **Scripts** | Elles sont répétitives, sans jugement, et le cache les rend gratuites. |
| Rédaction d'un point à partir d'un paquet | **IA de rédaction** : modèle local ou modèle peu coûteux | La difficulté est surtout linguistique, car le paquet porte la vérité. |
| Liste DX, ordre et rangs E (Phase A) | **IA de haut niveau de raisonnement** | Cette liste engage tout le LOT ; une erreur s'y propage dix fois. |
| Audit médical des points 4, 8, 9, 10 et 11, puis des seuls défauts signalés | **IA d'audit médical** | Ce jugement clinique est à haut risque ; l'auditeur ne lit que les phrases signalées et leurs extraits. |
| Inspection d'une planche d'images | **IA à capacité visuelle, un appel par LOT** | Une planche unique remplace trente ouvertures d'images. |

> **Indépendance.** Le rédacteur d'un fichier n'en est jamais l'auditeur. L'auditeur médical a un niveau supérieur ou égal à celui du rédacteur. L'escalade d'un modèle vers un modèle plus fort se fait sur un échec constaté (verdict ROUGE répété, doute sur une dose), jamais par précaution.

---

# PARTIE MICRO — COMMENT ON CONSTRUIT

## µ1. Phase A — fixer la vérité du LOT

1. **Collecte (E2).** `paquet.py` reçoit l'intitulé de la SSP et les registres de Vial. Il en retient d'abord les URL suisses, puis européennes.
2. **Liste des dix DX (E3), avec le prompt A-2.** Chaque DX est un vrai concurrent clinique de la SSP, distinct des neuf autres et sans catégorie fourre-tout. L'ordre suit la fréquence décroissante en Suisse, ou en Europe à défaut, et chaque rang est sourcé. Un DX grave et rare garde son rang de fréquence ; il reçoit en plus le badge 🚩, un rang E, une mention dans la phrase d'introduction et la tête de l'algorithme.
3. **Badge de fréquence.** Un pourcentage s'affiche seulement s'il est sourcé : `<span class="freq">XX %</span>` avec sa citation. Sinon, on écrit « Ne rang » avec l'argument sourcé du rang.
4. **Tableau comparatif.** Il compte dix lignes et cinq colonnes : signe clé, examen qui tranche, mécanisme, conduite immédiate et rang E.
5. **Algorithme.** Il commence par l'exclusion de E1, E2… puis discrimine les DX fréquents. Chaque nœud nomme un signe, un examen ou un geste.
6. **Porte P1, puis gel.** La liste n'est gelée qu'après l'audit A-4 : `LISTE_DX_CANONIQUE.md` enregistre alors les noms exacts, l'ordre et les numéros, signés par SHA-256. Une modification ultérieure impose un nouvel audit de la Phase A et le réalignement des dix fichiers.
7. **Monographie SSP.** Elle suit les 14 points de µ3, rédigés comme ceux d'un DX à partir de `PA/paquet.json`.

## µ2. Phase B — dix fichiers, un par DX

- La Phase B démarre seulement après le gel de la liste. Ses dix fichiers se rédigent ensuite en parallèle, chacun avec son propre paquet.
- Chaque fichier contient une seule monographie de 14 points, sans renvoi du type « voir la Phase A » et sans point omis.
- Une phrase partagée mot pour mot entre deux DX reçoit le verdict ROUGE (`B_phrase_partagee_entre_fichiers`), car elle signale un gabarit recopié et non une ponction propre au DX.
- La cohérence A↔B est critique : le nom, le numéro et l'ordre de chaque `<h2>` doivent correspondre à la liste gelée, sinon le dépôt de tout le LOT est interdit.

## µ3. Les 14 points — contrat de contenu

Le budget indique les octets visés pour le texte et les fenêtres du point (environ 130 Ko au total). L'assembleur ajoute ensuite le gabarit et les Sources.

| N° | Point | Contenu exigé (et rien d'autre) | Tableau obligatoire | Image | Budget |
|---|---|---|---|---|---|
| 1 | **Définition et sémantique** | Définition exacte de la société savante, nommée et datée ; synonymes admis et termes à éviter ; ce que l'entité est, ce qu'elle n'est pas et ce qui s'en approche. | — | — | 5 000 |
| 2 | **Épidémiologie (Suisse, puis Europe)** | Prévalence et incidence chiffrées, sourcées et datées ; âge, sexe, groupes à risque et mortalité ; histoire naturelle ; enjeux de santé publique. | Chiffre, population, année et source, si l'on dispose de trois chiffres ou plus | — | 7 000 |
| 3 | **Physiopathologie** | Chaîne moléculaire → cellulaire → tissulaire → clinique (amorce, développement, installation, maintien) ; chaque perturbation est reliée à l'examen qui la montre et au traitement qui la corrige. | **Corrélation** : perturbation → exploration → thérapeutique (mécanisme) | Schéma sourcé si l'anatomie l'exige ; jamais de schéma anatomique dessiné par une IA | 12 000 |
| 4 | **Démarche diagnostique** | Les graves d'abord (E1, E2 avec 🚩), puis les fréquents ; trois ou quatre DX discriminants, chacun avec le signe ou l'examen qui tranche, le piège et la conduite si le résultat est positif. | DX, élément qui tranche, piège, conduite | — | 8 000 |
| 5 | **Anamnèse ciblée et drapeaux rouges** | Chaque question porte sa raison physiopathologique ; chronologie, déclencheurs, comorbidités et médicaments ; chaque drapeau rouge indique l'action qu'il impose. | Drapeau rouge, signification, action immédiate | — | 8 000 |
| 6 | **Examen physique ciblé, région par région** | Le normal, puis le pathologique ; la technique du geste ; la valeur diagnostique et le piège d'interprétation. | — | Photographie clinique sourcée si un signe visible l'exige | 10 000 |
| 7 | **Approche syndromique (7.1, 7.2…)** | Syndromes numérotés, chacun éclaté en signes fonctionnels et signes physiques ; pour chaque signe, sa définition (en fenêtre), le geste de recherche et le mécanisme. | Syndrome, signes fonctionnels, signes physiques | — | 10 000 |
| 8 | **Diagnostic positif et critères** | Critères de la société savante avec leur année (majeurs, mineurs, seuils, durée, exclusions) ; ce qui suffit et ce qui ne suffit pas ; scores et stades, avec leur usage. | Critères | — | 8 000 |
| 9 | **Examens complémentaires** | *9.a* gold standard (ou mention qu'il est clinique) ; *9.b* 1<sup>re</sup> intention ; *9.c* alternatives (grossesse, enfant, DFGe < 30 mL/min, allergie à l'iode, IRM impossible) ; *9.d* 2<sup>e</sup> intention ; pour chaque examen : indication, prescription exacte et interprétation. | **Interprétation** : résultat, signification, conduite ; valeurs normales en unités SI | **Cliché de référence** de la modalité décisive, s'il existe (µ6) | 16 000 |
| 10 | **Arbre décisionnel** | Embranchements « si X → Y » lisibles en une lecture ; les graves d'abord ; chaque nœud renvoie à un signe, un examen ou une action. | — (liste imbriquée ou SVG non anatomique) | — | 6 000 |
| 11 | **Prise en charge selon les recommandations suisses** | *11.A* but chiffré ; *11.B* moyens : urgences chronologiques (fenêtre « Urgence — conduite chronologique »), ordre du traitement, pharmacologie AIPS (spécialité ®, dose, voie, durée, n° Swissmedic), non pharmacologique, situations spéciales (grossesse, allaitement, sujet âgé, enfant, insuffisance rénale ou hépatique), volet social et assurances ; *11.C* surveillance (quoi, quand, seuils d'arrêt) ; *11.D* pronostic, critères de guérison et critères de sortie énumérés un par un. | **Médicaments** : molécule ®, dose AIPS, voie, durée, contre-indication majeure, extrait AIPS | — | 20 000 |
| 12 | **Prévention** | Prévention primaire, secondaire et tertiaire, avec la recommandation suisse (organisme, année) ; gestes concrets, populations cibles et seuils ; lien avec le point 2. | — | — | 6 000 |
| 13 | **Points clés** | Trois à six phrases verbales, intactes et mémorisables, chacune porteuse d'une décision ou d'un fait critique. Aucune fenêtre ne coupe ces phrases. | — | — | 2 000 |
| 14 | **Pièges et questions fréquentes à l'examen fédéral suisse** | Chaque piège prend la forme d'une question d'examen, suivie de la bonne réponse et de sa raison ; il porte sur les confusions de doses, de critères, de gravité et de conduite, à partir des points 1 à 13. | Question, réponse, raison | — | 6 000 |

**Règle d'affectation.** Le contenu d'un point reste dans ce point. Quatorze titres présents ne prouvent rien : l'auditeur vérifie que chaque point porte son propre contenu (Θ3, grille Q).

## µ4. Rédaction — la langue du projet

1. **Phrase verbale.** Chaque phrase porte un verbe conjugué, y compris dans les fenêtres, les tableaux et les légendes. Les phrases nominales et les listes télégraphiques sont interdites.
2. **Connecteur logique.** Chaque paragraphe de plus de 40 mots contient au moins un connecteur qui porte le raisonnement : *car, donc, ainsi, en effet, dès lors, par conséquent, cependant, en revanche, d'abord, ensuite, si… alors, lorsque, ce qui, d'où*. Le connecteur relie une cause et un effet, un signe et sa décision, ou une règle et son exception ; il ne sert jamais de décor.
3. **Longueur.** Une phrase compte de 12 à 28 mots, une idée par phrase et une décision par paragraphe.
4. **Ordre.** On présente le normal avant le pathologique, le grave avant le fréquent, la cause avant le signe et le signe avant la décision.
5. **Unités.** On emploie les unités SI, la virgule décimale, les espaces insécables, les guillemets « » et les seuils suisses (par exemple, une natrémie < 135 mmol/L).
6. **Abréviations.** Chaque abréviation est développée à sa première occurrence dans le fichier.
7. **Proscrits.** Le texte ne contient ni métaphore, ni méta-commentaire, ni adresse au lecteur, ni répétition, ni remplissage, ni formule de lacune (LV7).
8. **Nos termes, leur fond.** On reformule l'extrait dans le lexique M3 et dans cette syntaxe, mais on garde le sens, les nombres et les conditions de la source.

**Exemple de transformation (ponction → rédaction)**

> Extrait `easl-3` : « A SAAG ≥ 11 g/L indicates portal hypertension with ~97 % accuracy. »
> ❌ « SAAG élevé : HTP. » (phrase nominale, sans nombre ni citation)
> ❌ « Un SAAG supérieur à 10 g/L signe une hypertension portale dans 95 % des cas. » (nombres modifiés)
> ✅ « Le gradient d'albumine sérum-ascite (SAAG) oriente vers une hypertension portale lorsqu'il atteint 11 g/L, car il reflète la pression hydrostatique sinusoïdale ; il est exact dans environ 97 % des cas<sup class="r"><a href="#sb-easl-3">easl-3</a></sup>. »

## µ5. Fenêtres

- **Une fenêtre par notion technique.** Chaque signe, examen, médicament, score, article de loi ou mécanisme ouvre une fenêtre, déclenchée par `<button class="w" popovertarget="ID">libellé</button>` et contenue dans `<div id="ID" popover class="fenetre">…</div>`.
- **Contenu.** Une fenêtre expose le mécanisme pas à pas, un exemple clinique chiffré et sourcé, un tableau s'il clarifie, le piège d'examen et la citation. Les fenêtres peuvent s'imbriquer.
- **Monographie de médicament** (point 11) : classe, autres molécules de la classe, pharmacocinétique et pharmacodynamie utiles, effets indésirables à annoncer au patient, spécialité ®, dose AIPS, durée, contre-indications et interactions majeures, chaque élément cité.
- **Fenêtre « Urgence — conduite chronologique ».** Chaque forme compliquée en reçoit une, rythmée minute par minute ou heure par heure.
- **Intégrité.** Une fenêtre ne coupe jamais une phrase porteuse : le bouton s'insère dans une phrase complète et sa fenêtre est placée après la fin du paragraphe.
- **Charte visuelle.** Les fenêtres s'ouvrent au premier plan, en grand format (≤ 860 px et 94 vw), sur un fond neutre. Les îlots ont des bords en relief. Le cours de base reste sobre.

## µ6. Images — automate collecteur (dès que la modalité décide)

**Quand.** On illustre le point 9 (cliché de la modalité décisive : radiographie, échographie, TDM, IRM, ECG, frottis, histologie) et le point 6 (signe visible). Le point 3 n'est illustré que par un schéma sourcé ; un schéma anatomique dessiné par une IA est interdit.

**Chaîne (aucun modèle avant l'inspection) :**

1. Le rédacteur de la Phase A remplit `images/besoins.json`, à raison d'une ligne par besoin : DX, point, modalité et requête anglaise précise (« pleural effusion ultrasound spine sign »).
2. `images.py` interroge Wikimedia Commons puis Europe PMC. Il lit la licence de **chaque fichier**, refuse les licences NC, ND et inconnues, rapatrie les fichiers admissibles en cache avec leur SHA-256, puis produit `PLANCHE.html`.
3. Le catalogue de Vial (Radiopaedia, Radiology Assistant, Ultrasound Cases, Eurorad, Learning Radiology, Case Stacks, Casimage, RadioSurf) fournit des **liens de cas** cités en fenêtre, jamais une copie, car leurs droits ne sont pas établis.
4. **Une seule inspection visuelle par LOT** (prompt A-6) examine la planche : modalité, plan, latéralité, repères, cohérence de la légende et absence d'identifiant personnel. La décision s'inscrit dans `figures.json` (`"inspectee": true`, légende française, attribution).
5. `assembler.py` insère seulement les figures inspectées, avec auteur, licence et URL sous l'image. Avec `--integrer-images`, le fichier reste autonome.
6. Une annotation française (flèche, repère) se superpose dans un SVG séparé, sans modifier l'original. L'original non modifié reste référencé.

> **Droits.** La licence d'un article ne vaut pas licence de sa figure. Sans droit établi pour la figure précise, on donne un lien vers le cas, sans copie.

## µ7. Gabarit HTML (produit par `assembler.py`)

```html
<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>DX.3 — …</title><style>/* charte : fond neutre, îlots 3D, fenêtres grand format */</style></head>
<body><main><h2>DX.3 — <nom exact de la liste canonique></h2>
<section class="ilot" id="dx3-p1"><h3 id="dx3-h1"><strong>1. Définition et sémantique</strong></h3>
  <div class="p">Phrase verbale citée<sup class="r"><a href="#sb-ID">ID</a></sup>, reliée par un connecteur…</div>
  <div class="t"><table>…</table></div>
  <button class="w" popovertarget="dx3-p1-f1">libellé</button> … <div id="dx3-p1-f1" popover class="fenetre">…</div>
</section>
… (points 2 à 14) …
<section class="ilot" id="dx3-sources"><h3>Sources</h3><ol><li id="sb-ID">[ID] organisme, titre, année — URL (consulté le …)</li></ol>
<p class="p">Le contenu reprend les sources citées ; il n'a pas été validé cliniquement par un médecin.</p></section>
</main></body></html>
<!-- FIN_FICHIER LOT_XXX_Phase_B_V0_DX.3 -->
```

Le gabarit impose les règles techniques suivantes : aucun `title=` servant d'infobulle, aucun `<script>`, aucune ressource externe et aucune formule convertie en image ; chaque tableau est enveloppé dans `<div class="t">` (défilement horizontal) ; le fichier reste lisible sur un écran de 390 px ; aucune ligne ne dépasse 3 000 caractères ; les balises sont équilibrées.

## µ8. SSP transversaux (éthique, droit, communication, prévention)

- Les 14 points restent ; les dix DX deviennent **dix scénarios gradués**, ordonnés par fréquence dans la pratique suisse et accompagnés de leur gravité médico-légale.
- La transposition se fait ainsi : le point 1 porte le cadre conceptuel et le code FMH ; le point 2 les données suisses (OFS, OFSP, Obsan) ; le point 3 le cadre légal exact, article et alinéa lus sur Fedlex (CC, CP, LAMal, LAA, LAI, LEp…) ; les points 4 à 8 l'évaluation situationnelle, les drapeaux rouges médico-légaux et les grilles d'entretien (SPIKES, Calgary-Cambridge, capacité de discernement selon l'ASSM) ; les points 9 à 11 les outils standardisés, l'arbre médico-légal et la conduite.
- On ne plaque jamais une physiopathologie, une posologie ou un calcul sur une SSP qui ne s'y prête pas. Un point sans objet est déclaré tel par une phrase verbale qui en donne la raison.

---

# PARTIE MÉTA — COMMENT ON CONTRÔLE ET CE QUE CELA COÛTE

## Θ1. Contrôle natif des trois axes (`controle3.py`, zéro modèle)

| Axe | Ce que le script vérifie | Défaut ROUGE (bloquant) | Défaut ORANGE (à corriger) |
|---|---|---|---|
| **A. Véracité clinico-scientifique** | Les nombres de chaque phrase citée figurent dans l'extrait cité ; chaque citation existe dans le paquet ; chaque phrase de dose cite un extrait `aips-*`. | `A_nombre_absent_de_l_extrait`, `A_citation_inconnue`, `A_dose_sans_AIPS` | `A_chiffre_sans_citation` |
| **B. Phrase verbale et connecteur** | Présence d'un verbe conjugué ; longueur de la phrase ; connecteur par paragraphe ; doublons. | `B_phrase_partagee_entre_fichiers` | `B_phrase_nominale`, `B_phrase_longue`, `B_phrase_dupliquee`, `paragraphes_sans_connecteur > 0` |
| **C. Forme et contrat** | 14 points, FIN_FICHIER, interdits HTML, tableaux enveloppés, balises équilibrées, bande d'octets. | `C_points_manquants`, `C_FIN_FICHIER_absent`, `C_balises` | `C_title_interdit`, `C_tableau_non_enveloppe`, `C_taille_hors_bande` |

**Cibles mesurables.** Chaque fichier doit atteindre `connecteur% ≥ 35`, `paragraphes_sans_connecteur = 0`, `B_phrase_nominale = 0`, `A_* = 0` et un verdict VERT.
*Calibrage réel au 9 novembre 2026 : LOT_001 DX.1 obtient 275 710 octets et un connecteur% de 18, hors bande ; LOT_166 DX.1 obtient 60 857 octets, un connecteur% de 15, 17 phrases dupliquées et 7 `title=`. Ces deux références montrent l'écart à combler.*

**Limites connues du script.** La détection du verbe est heuristique : elle repère les formes conjuguées usuelles et peut accepter une phrase nominale qui contient un mot finissant en « -ent » ou « -it ». Le contrôle des nombres vérifie leur présence dans l'extrait, pas l'exactitude de leur contexte (un seuil inversé passerait). C'est pourquoi l'audit médical Θ3 reste obligatoire sur les points 4, 8, 9, 10 et 11.

## Θ2. Portes et verdicts

| Porte | Moment | Condition de passage | Qui |
|---|---|---|---|
| **P0** | Avant toute rédaction | `DECISION_SEANCE.md` présent ; LOT non pris par une autre branche (légion) ; branche basée sur `main` | Script |
| **P1** | Liste DX | Audit A-4 de la liste : dix DX discriminants, ordre sourcé, rangs E, question finale « oui » ; gel signé | IA d'audit |
| **P2** | Chaque fichier assemblé | `controle3.py` sans aucun défaut ROUGE | Script |
| **P3** | Chaque fichier | Audit A-4 : score ≥ 90 % (cible 95–100 %), zéro critique, question finale « oui » | IA d'audit |
| **P4** | LOT complet | 11 fichiers ayant franchi P2 et P3 ; cohérence A↔B ; `MANIFESTE.json` égal aux octets audités ; CI verte | Script + CI |

Après P4, le LOT est déposé **immédiatement** dans `LOT_Claude_Finaux/LOT_XXX/` par une PR fusionnée après CI verte, sans attendre d'accord supplémentaire : la porte vaut décision. Un fichier qui échoue deux fois à P3 reçoit le verdict `REFUSE`, consigné dans `ETAT_FILE.json`, puis la file passe au LOT suivant sans blocage.

## Θ3. Audit ciblé (l'auditeur ne lit que ce qui compte)

**Ce que reçoit l'auditeur :** le `controle.json` du fichier (au plus 3 Ko) ; les phrases signalées avec l'extrait cité en regard ; les points 4, 8, 9, 10 et 11 extraits seuls ; la liste canonique. L'auditeur ne reçoit jamais le HTML entier.

**Grille Q (2 = complet, 1 = partiel, 0 = absent ou faux).**

| Point | Questions (Q) |
|---|---|
| 1 | La définition vient-elle d'une société savante nommée et datée ? Distingue-t-elle l'entité de ses voisines ? |
| 2 | Le texte donne-t-il la distribution, l'histoire naturelle et les enjeux ? Les chiffres sont-ils datés et suisses d'abord ? |
| 3 | La chaîne amorce → maintien est-elle complète ? Le tableau de corrélation relie-t-il perturbation, exploration et traitement ? |
| 4 | Les graves sont-ils placés avant les fréquents ? Chaque DX dangereux a-t-il son élément qui tranche et son piège ? |
| 5 | Chaque question d'anamnèse porte-t-elle sa raison ? Les drapeaux rouges sont-ils actionnables ? |
| 6 | Le normal précède-t-il le pathologique ? Chaque signe a-t-il sa technique et sa valeur ? |
| 7 | Les syndromes sont-ils numérotés et éclatés en signes définis, avec geste et mécanisme ? |
| 8 | Les critères sont-ils datés, avec leurs seuils ? Le texte dit-il ce qui ne suffit pas ? |
| 9 | Le gold standard est-il déclaré ? Chaque examen est-il prescriptible et interprétable, alternatives comprises ? Le cliché est-il pertinent ? |
| 10 | Chaque embranchement mène-t-il à une décision ? |
| 11 | Le but est-il chiffré ? L'ordre et sa raison sont-ils donnés ? Les urgences sont-elles chronologiques ? Les doses sont-elles conformes à l'AIPS ? Les situations spéciales, la surveillance et les critères de sortie sont-ils présents ? |
| 12 | Les trois niveaux de prévention sont-ils couverts, avec leur recommandation suisse ? |
| 13 | Les points clés comptent-ils trois à six phrases verbales intactes ? |
| 14 | Chaque piège est-il formulé en question d'examen, avec sa réponse ? |
| Finale | Ce fichier suffit-il pour réussir l'examen sur ce sujet et pour traiter ce patient sans danger ? |

Le score d'un fichier vaut la somme obtenue divisée par la somme maximale (les items sans objet, justifiés, sont exclus). Le seuil est de 90 % et la cible de 95 à 100 %. Une erreur dangereuse (dose, voie, contre-indication, conduite contraire à l'AIPS) est classée **Critique** et bloque le fichier. Le rapport `audits/<fichier>.audit.json` reste court : version (octets et SHA-256), score, réponse finale, et corrections classées Critique, Grave, Moyen ou Léger, chacune avec l'emplacement (ID de phrase), l'extrait mot pour mot, la correction et la source.

## Θ4. Économie — bannir les pertes de jetons et les allers-retours

| Gaspillage constaté | Règle qui le supprime |
|---|---|
| Un modèle qui lit un HTML de 100 à 275 Ko pour vérifier des tailles, des balises ou des points | `controle3.py` et `controle_lot.py` font ce travail ; un modèle ne lit jamais un HTML entier. |
| Une réécriture complète d'un fichier pour trois phrases fautives | Correction chirurgicale A-5 : seules les phrases désignées par leur ID sont réécrites. |
| Des sources téléchargées et relues à chaque session | Cache disque par SHA-256 (`.cache/paquet`, `.cache/images`) ; un extrait AIPS n'est lu qu'une fois, puis il sert à tout le LOT. |
| Un rédacteur qui cherche ses sources lui-même (recherches web répétées) | Le paquet est construit d'abord par script ; le rédacteur ne fait aucune recherche. |
| Un même fragment renvoyé au modèle pour « améliorer » | Un seul passage : une sortie reçue est archivée et n'est jamais resoumise. |
| 326 branches à inspecter à la main | La légion produit `DIGEST.md` (environ 25 Ko), seul fichier lu par le chef de production. |
| Un gabarit recopié d'un DX à l'autre (phrases partagées) | Verdict ROUGE `B_phrase_partagee_entre_fichiers` ; chaque DX est ponctionné dans son propre paquet. |
| Un audit complet par un modèle fort | Audit ciblé Θ3 : défauts signalés et points à risque seulement. |
| Trente ouvertures d'images une à une | Une planche, inspectée en une fois. |

**Paramètres de rédaction (modèle local).** On règle `temperature 0.2`, `repeat_penalty 1.1`, `num_ctx 8192` et `num_predict = 1,3 × octets_cible / 3,3`. Un échec réseau sans réponse autorise une seule nouvelle tentative.

**Bracelet (décider avec, pas tout allumer).** Le cache de requêtes (requests-cache ou Hishel, ici remplacés par le cache stdlib intégré) est actif par défaut. Le routage local, puis peu coûteux (LiteLLM ou RouteLLM), sert dès qu'une passerelle existe. La compression (LLMLingua) s'applique seulement si un paquet dépasse `num_ctx`. L'observation des coûts (Phoenix) s'active seulement si un dérapage est constaté. On charge un à trois outils par tâche, jamais toute la liste.

## Θ5. Anti-collision

1. Un producteur travaille sur un LOT, dans une branche `prod/lot-XXX` basée sur `main`, et écrit dans le seul dossier `lot en cours de production/LOT_XXX/`.
2. Avant d'écrire, il interroge la légion (`DIGEST.md`). Si une autre branche active touche déjà ce LOT, il s'arrête et le chef de production arbitre.
3. Sans mandat, `PROMPT_Casern/`, `HANDOFF.md`, `ETAT.md`, la CI racine et les LOTs des autres producteurs restent en lecture seule.
4. Le producteur pousse après chaque fichier assemblé : une session qui s'arrête sans branche poussée n'a rien produit.
5. Un remplacement dans `LOT_Claude_Finaux/` se fait ainsi : la nouvelle version est déposée et vérifiée, puis l'ancienne passe dans `_OBSOLETES/` avec le suffixe `_OBSOLETE_`.

## Θ6. Traçabilité

- `JOURNAL.md` reçoit une ligne par décision (date, hypothèse, raison) ; il ne contient aucune prose.
- `HELP.md` reçoit une entrée par lacune : LOT, fichier, point, question précise, URL déjà consultées et date. Une réponse reçue se vérifie sur la source primaire avant d'être réinjectée.
- `MANIFESTE.json` enregistre les octets et le SHA-256 au gel. Tout octet modifié ensuite impose de refaire les portes P2 et P3.
- `audits/*.audit.json` et `controle.json` sont versionnés avec le fichier qu'ils jugent.

## Θ7. Erreurs déjà commises, et la règle qui les empêche

| Erreur réelle | Règle |
|---|---|
| Numéro Swissmedic déduit d'une URL du Compendium | LV6 |
| Extrait « mot pour mot » fabriqué en fusionnant deux règles (ESE 2014, NaCl 3 %) | LV1, LV3, Θ1-A |
| Indication FDA donnée à la place de l'indication suisse | LV5 |
| Recommandation périmée (EACS 12.0, ERC 2015) | LV8 |
| Liste DX différente entre la Phase A et la Phase B (LOT_001) | µ1.6, µ2, P4 |
| DX grave relégué au rang 5 sans marquage | µ1.2 |
| Audit à 95,65 % accepté alors que la question finale était « non » | M1.3 |
| Texte de grossesse adouci (« peut être envisagé ») | LV6 |
| Phrase porteuse coupée par une fenêtre | µ5 |
| Fichier de 275 Ko (> 200 Ko) ou de 60 Ko (< 100 Ko) déposé | M4, Θ1-C |
| Phrases de notice ou de gabarit répétées d'un DX à l'autre (LOT_125 à 130, 9 novembre 2026) | µ2, Θ1-B |
| Doses absentes, ou mention « sans milligramme », alors que l'AIPS était disponible | LV6, `paquet.py --aips` |
| Attributs `title=` utilisés comme infobulles (LOT_166) | µ7 |
| Score d'une version reporté sur une autre ; rédacteur qui se note lui-même | Θ2, M6 |
| Session arrêtée par quota sans branche poussée | Θ5.4 |
| Dépôt annoncé mais inexistant | LV9 |

## Θ8. Stratégie d'achèvement des 248 LOTs (état collecté par la légion le 9 novembre 2026)

| Ensemble | LOTs | Action | Coût |
|---|---|---|---|
| **Existants avec 11 fichiers** (environ 132) | 1–40, 109–133, 134–146 et 149–172, 173–207 et 219–226, 232, 245 | Lancer `controle3.py` sur tous ; trier les fichiers VERT, ORANGE et ROUGE ; corriger chirurgicalement les ORANGE et ROUGE ; auditer seulement les fichiers passés à P2 | Scripts gratuits, puis audit ciblé |
| **Partiels** (environ 36) | 14, 17, 40–42, 72–78, 104–108, 110, 112, 121, 122, 137, 147, 148, 181–183, 208–216 | Compléter les DX manquants à partir de la liste existante si elle passe P1 ; sinon, refaire la Phase A | Rédaction locale |
| **Absents** (environ 80) | 43–71, 79–103, 114, 116, 118, 120, 217, 218, 227–231, 233–244, 246–248 | Chaîne M5 complète | Rédaction locale, audit ciblé |

**Ordre recommandé.** (1) Consolider les portes P2 et P3 des LOTs existants, car c'est le gain le plus rapide sans nouvelle rédaction. (2) Compléter les partiels. (3) Fabriquer les absents par vagues de dix LOTs, à raison de 11 paquets et 11 rédactions en parallèle par LOT. Cet état se recalcule chaque jour par `python3 mere.py <dépôt> --jours 30`.

---

# ANNEXES

## A. Prompts instanciables

### A-1. P-POINT — rédaction d'un point en une passe (modèle local ou peu coûteux)

```text
Tu es rédacteur médical de langue française. Tu rédiges une seule fois, et seulement le point {N} — {TITRE_POINT}
de la monographie « {ENTITE} » (LOT {LOT}, SSP {CODE_SSP}), pour des candidats à l'examen fédéral suisse.

CONTENU EXIGÉ PAR LE CONTRAT
{CONTENU_EXIGE}

EXTRAITS — LES SEULES PREUVES AUTORISÉES
{PASSAGES}

FIDÉLITÉ
- Chaque phrase factuelle se termine par <sup class="r"><a href="#sb-ID">ID</a></sup>, où ID est l'identifiant de l'extrait qui la soutient.
- Tu recopies chaque nombre tel qu'il est écrit dans l'extrait cité dans la même phrase ; tu n'arrondis jamais.
- Une dose ne s'écrit que si un extrait aips-… la contient ; sinon, tu nommes la classe et la conduite sans milligramme.
- Tu reformules dans un français médical précis, mais le sens, la condition et le seuil restent ceux de l'extrait.
- Tu n'écris aucune phrase qui signale une lacune ; tu écris ce que les extraits établissent.

LANGUE
- Chaque phrase porte un verbe conjugué ; tu n'écris aucune phrase nominale ni aucune liste télégraphique.
- Chaque phrase compte 12 à 28 mots ; chaque paragraphe relie ses faits par un connecteur logique qui porte le raisonnement
  (car, donc, ainsi, en effet, dès lors, par conséquent, cependant, en revanche, d'abord, ensuite, lorsque, ce qui).
- Tu présentes le normal avant le pathologique et le grave avant le fréquent ; tu développes chaque abréviation à sa première occurrence.
- Tu n'écris ni métaphore, ni méta-commentaire, ni adresse au lecteur, ni répétition.

FORME
- Tu rends seulement le fragment HTML du point : des <div class="p"> ; les tableaux exigés dans <div class="t"><table>…</table></div> ;
  les notions techniques en <button class="w" popovertarget="{PREFIX}-p{N}-fK">libellé</button>, avec leur
  <div id="{PREFIX}-p{N}-fK" popover class="fenetre">…</div> placé après le paragraphe.
- Tu n'écris ni <html>, ni <script>, ni title=, ni image, ni section Sources.
- Ton budget est d'environ {OCTETS_CIBLE} octets ; tu t'arrêtes à la fin d'une phrase complète.
{SQUELETTE}
SÉCURITÉ (points 5, 6 et 11 seulement) : {SECURITE}

Renvoie seulement le fragment HTML.
```

### A-2. P-LISTE-DX — Phase A, liste des dix DX (modèle fort)

```text
Rôle : clinicien hospitalo-universitaire suisse, omnipraticien senior.
Tâche : à partir des seuls extraits ci-dessous, établir pour la SSP « {SSP} » ({CODE_SSP}) la liste des dix diagnostics
différentiels qui la concurrencent réellement.
Règles :
1. Tu ordonnes les DX par fréquence décroissante en Suisse, ou en Europe à défaut ; chaque rang cite l'extrait qui le justifie.
2. Tu marques chaque DX grave de 🚩 et d'un rang d'exclusion E1, E2… ; un DX grave et rare garde son rang de fréquence.
3. Tu ne retiens ni doublon déguisé, ni catégorie fourre-tout, ni DX hors sujet.
4. Pour chaque DX, tu écris une phrase verbale qui dit pourquoi il entre dans la liste et pourquoi il occupe ce rang.
Extraits : {PASSAGES}
Sortie stricte (JSON) : {"critere_ordre":"…","dx":[{"rang":1,"nom":"…","grave":false,"E":null,"justification":"…","citations":["ID"]}…]}
```

### A-3. P-FENETRE — fenêtre de médicament ou de signe (modèle local)

```text
Rédige la fenêtre « {NOTION} » du point {N} de « {ENTITE} », à partir des seuls extraits {PASSAGES}.
Pour un médicament : classe ; autres molécules de la classe ; mécanisme ; dose AIPS recopiée (extrait aips-…) ;
voie ; durée ; contre-indications ; interactions majeures ; effets indésirables à annoncer ; grossesse et allaitement (texte AIPS non adouci).
Pour un signe : définition ; technique de recherche ; mécanisme ; valeur diagnostique ; piège.
Chaque phrase est verbale et citée. Sortie : <div id="{ID}" popover class="fenetre">…</div>
```

### A-4. P-AUDIT-CIBLE — IA d'audit (auditeur médical indépendant)

```text
Tu audites sans complaisance ; tu cherches l'erreur, tu ne valides pas.
Tu reçois : (1) controle.json ; (2) les phrases signalées, avec l'extrait cité en regard ; (3) les points 4, 8, 9, 10 et 11 ;
(4) la liste canonique.
Tu rends un JSON court :
{"fichier","sha256","score_pct","finale":"oui|non",
 "corrections":[{"gravite":"Critique|Grave|Moyen|Léger","point":N,"phrase":"…extrait exact…","correction":"…","source":"ID"}],
 "help":[…]}
Toute dose, voie ou contre-indication contraire à l'extrait AIPS est Critique. Tout nombre qui diffère de l'extrait est Grave.
Tu ne réécris pas le fichier ; tu désignes et tu corriges seulement des phrases.
```

### A-5. P-CORRECTION — correction chirurgicale (rédacteur, une passe)

```text
Remplace seulement les phrases listées par leur correction, en gardant la citation, la langue (verbe, connecteur) et le HTML environnant.
Rends un JSON [{"avant":"…","apres":"…"}] ; aucune autre modification.
```
`python3 -c` (D-7) applique ensuite les remplacements par recherche exacte : si l'ancienne phrase n'est pas trouvée exactement une fois, le remplacement échoue.

### A-6. P-PLANCHE — inspection visuelle unique (IA à capacité visuelle)

```text
Planche ci-jointe : pour chaque image, réponds par JSON
{"local","besoin","garder":true|false,"modalite","plan","lateralite","reperes_visibles":[…],"legende_fr":"phrase verbale",
 "identifiant_personnel":false,"motif_refus":""}
Tu ne déduis de l'image ni diagnostic, ni mesure, ni temporalité qu'elle ne démontre pas.
```

## B. Contrats JSON

### B-1. `contrat.json` (par entité)

```json
{"LOT":"166","CODE_SSP":"F2.18","ENTITE":"Ascite de l'hypertension portale","PREFIX":"dx1",
 "SECURITE":"🚩 péritonite bactérienne spontanée : ponction avant antibiotique ; 🚩 syndrome hépatorénal",
 "points":{
  "1":{"titre":"Définition et sémantique","octets":5000,"exige":"…(µ3, ligne 1)…","squelette":""},
  "9":{"titre":"Examens complémentaires","octets":16000,"exige":"…(µ3, ligne 9)…",
       "squelette":"<h4><em>9.a Gold standard</em></h4>…<h4><em>9.b Première intention</em></h4>…<h4><em>9.c Alternatives</em></h4>…<h4><em>9.d Deuxième intention</em></h4>…"},
  "11":{"titre":"Prise en charge selon les recommandations suisses","octets":20000,"exige":"…",
        "squelette":"<h4><em>11.A But</em></h4>…<h4><em>11.B Moyens</em></h4>…<h4><em>11.C Surveillance</em></h4>…<h4><em>11.D Pronostic et sortie</em></h4>…"}
 }}
```

### B-2. `images/besoins.json`

```json
[{"dx":"DX.1","point":9,"modalite":"échographie","requete":"ascites ultrasound Morison pouch"},
 {"dx":"DX.3","point":9,"modalite":"radiographie thoracique","requete":"parapneumonic effusion chest radiograph meniscus sign"}]
```

### B-3. `figures.json` (après inspection)

```json
[{"point":9,"fichier":"images/3fa1c09b2d6e4a10.jpg","inspectee":true,
  "legende":"L'échographie montre un liquide anéchogène dans l'espace de Morison.",
  "attribution":"Auteur X, CC BY-SA 4.0, https://commons.wikimedia.org/wiki/File:…"}]
```

## C. Outils exécutables (Python ≥ 3.9, bibliothèque standard seule)

> Ces outils sont testés de bout en bout ; la correspondance DCI → HAM → index AIPS est vérifiée sur le corpus réel (spironolactone → Aldactone® 27257, furosémide → Lasix® 30629) sur les preuves réelles du LOT_166, chaîne paquet → prompt → assemblage → contrôle. `images.py` et le téléchargement de `paquet.py` exigent un accès réseau à Wikimedia, Europe PMC et aux sites des sources ; ils n'ont pas pu être exécutés dans l'environnement de rédaction, faute de réseau.

### C-1. `controle3.py` — contrôle des trois axes

`controle3.py`
````python
#!/usr/bin/env python3
"""CONTROLE3 — contrôle gratuit (zéro modèle) des 3 axes d'un HTML de cours.

  A. VÉRACITÉ : tout nombre d'une phrase citée figure mot pour mot dans l'extrait cité ;
                toute phrase chiffrée porte une citation ; toute citation existe dans le paquet ;
                toute phrase de dose cite un extrait AIPS.
  B. LANGUE   : phrase verbale (verbe conjugué), connecteur logique par paragraphe, 8–32 mots,
                zéro phrase dupliquée (dans le fichier et entre fichiers du même lot).
  C. FORME    : points attendus présents, FIN_FICHIER, aucun title=, aucun <script>, tableaux enveloppés,
                balises équilibrées, bande d'octets.

Usage :
  python3 controle3.py FICHIER.html [FICHIER2.html ...] --paquet paquet.json [--points 14] [--min 100000 --max 200000]
Sortie : JSON par fichier (verdict VERT/ORANGE/ROUGE + défauts localisés) ; code 0 si aucun ROUGE.
"""
import re, sys, json, html, hashlib, argparse, collections

CIT = re.compile(r'<sup class="r"><a href="#sb-([\w.\-:]+)">')
NUM = re.compile(r'(?<![\w])(\d+(?:[.,’\' ]\d+)*(?:[.,]\d+)?)(?![\w])')
DOSE = re.compile(r'\b\d+(?:[.,]\d+)?\s?(?:mg|µg|mcg|UI|g(?=\s?(?:/kg|/j|/jour|par jour|toutes|i\.?v|IV|per os|p\.o)))(?!\s?/\s?(?:l|L|dl|dL|mmol))\b')
CONNECT = re.compile(r"\b(car|donc|or|ainsi|puis|alors|parce que|puisque|lorsque|quand|si|tandis que|alors que|"
                     r"afin de|afin que|pour que|de sorte que|c'est pourquoi|en effet|cependant|toutefois|"
                     r"néanmoins|par conséquent|dès lors|ensuite|enfin|d'abord|en revanche|ce qui|"
                     r"grâce à|à cause de|en raison de|si bien que|de ce fait|par ailleurs|en outre|"
                     r"autrement dit|c'est-à-dire|d'où|puisqu'|lorsqu'|qu'il)\b", re.I)
# Formes verbales conjuguées fréquentes en rédaction médicale (3e pers., présent/futur/passé composé)
VERBES = set("""est sont a ont fait font peut peuvent doit doivent reste restent devient deviennent va vont
semble semblent permet permettent signe signent oriente orientent impose imposent confirme confirment élimine
éliminent exclut excluent traite traitent associe associent survient surviennent provoque provoquent entraîne
entraînent exige exigent reçoit reçoivent touche touchent atteint atteignent dépasse dépassent varie varient
augmente augmentent diminue diminuent baisse baissent réduit réduisent favorise favorisent explique expliquent
précède précèdent suit suivent recherche recherchent mesure mesurent montre montrent révèle révèlent
définit définissent correspond correspondent comprend comprennent repose reposent consiste consistent
représente représentent constitue constituent nécessite nécessitent justifie justifient recommande recommandent
indique indiquent prescrit prescrivent administre administrent contre-indique évite évitent limite limitent
dure durent persiste persistent apparaît apparaissent disparaît disparaissent évolue évoluent aggrave aggravent
protège protègent prévient préviennent dépiste dépistent détecte détectent distingue distinguent sépare séparent
conduit conduisent mène mènent aboutit aboutissent cause causent déclenche déclenchent libère libèrent
active activent inhibe inhibent bloque bloquent stimule stimulent fixe fixent lie lient agit agissent
s'accompagne s'accompagnent s'associe s'explique s'élève se manifeste se manifestent se traduit se traduisent
se définit se recherche se mesure se prescrit se discute se pose s'impose s'observe s'installe se complique
remplace remplacent précise précisent compte comptent atteste attestent rappelle rappellent signale signalent
pose posent écarte écartent retient retiennent ordonne ordonnent adapte adaptent surveille surveillent
contrôle contrôlent corrige corrigent restaure restaurent normalise normalise prolonge prolongent
était étaient avait avaient sera seront aura auront serait seraient pourrait pourraient devrait devraient
faut suffit suffisent vise visent cible ciblent porte portent concerne concernent relève relèvent
""".split())
VERBE_RE = re.compile(r"\b(?:\w+(?:ent|ait|aient|era|eront|erait|eraient|ise|isent|it|issent))\b", re.I)
PRONOM_VERBE = re.compile(r"\b(?:il|elle|ils|elles|on|qui|cela|ce|celle-ci|celui-ci)\s+(?:ne\s+|n'|se\s+|s'|l'|le\s+|la\s+|les\s+|y\s+|en\s+)*\w+", re.I)
STRUCT = re.compile(r"\b(?:points?|DX\.?|rangs?|E|étapes?|îlots?|n°|LOT_?|Phase)\s*\d+(?:[.,]\d+)?", re.I)
SOURCES = re.compile(r'<section\b[^>]*id="[\w-]*sources"[^>]*>.*?</section>', re.S | re.I)
TAG_SS = re.compile(r'<(script|style)\b[^>]*>.*?</\1>', re.S | re.I)
VIDES = {'br', 'hr', 'img', 'meta', 'link', 'input', 'source', 'col', 'wbr', 'area', 'base', 'embed', 'track', 'param'}


def texte(fragment):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', fragment))).strip()


def nombres(s):
    out = set()
    for n in NUM.findall(s):
        n = re.sub(r'[’\' ]', '', n).replace(',', '.')
        out.add(re.sub(r'^0+(?=\d)', '', n))  # « 07 » et « 7 » désignent le même nombre
    return out


def est_verbale(ph):
    mots = {m.lower() for m in re.findall(r"[\w'’-]+", ph)}
    return bool(mots & VERBES or PRONOM_VERBE.search(ph) or VERBE_RE.search(ph))


def phrases_html(h):
    """Découpe les blocs textuels (p, li, td, div.p, dd) en phrases ; conserve le HTML brut pour les citations."""
    blocs = re.findall(r'<(p|li|td|dd|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|li|td|dd|div)>', h, re.S | re.I)
    out = []
    for tag, b in blocs:
        for brut in re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ý«])', b):
            t = texte(re.sub(r'<sup class="r">.*?</sup>', '', brut, flags=re.S))  # l'étiquette de citation n'est pas du texte
            if len(t.split()) >= 4:
                out.append((tag, brut, t))
    return out


def equilibre(h):
    pile = []
    for ferme, nom in re.findall(r'<(/?)([a-zA-Z][\w-]*)\b[^>]*?(?<!/)>', TAG_SS.sub('', h)):
        nom = nom.lower()
        if nom in VIDES:
            continue
        if not ferme:
            pile.append(nom)
        elif pile and pile[-1] == nom:
            pile.pop()
        elif nom in pile:
            return f'fermeture </{nom}> mal placée'
    return None if not pile else f'non fermées: {pile[-5:]}'


def controler(chemin, paquet, a, vus_lot):
    brut = open(chemin, 'rb').read()
    h = brut.decode('utf-8', 'ignore')
    d = collections.defaultdict(list)
    ph = phrases_html(SOURCES.sub(' ', h))  # la section Sources (générée, identique partout) n'entre pas dans l'analyse
    # A — véracité
    for tag, b, t in ph:
        cites = CIT.findall(b)
        nums = nombres(STRUCT.sub(' ', t))  # seuls les libellés structurels (point 3, DX.4, rang 2…) sont exemptés
        if nums and not cites and tag.lower() != 'td':
            d['A_chiffre_sans_citation'].append(t[:140])
        for c in cites if paquet else []:
            if c not in paquet:
                d['A_citation_inconnue'].append(c)
        if paquet and cites and nums:
            source = ' '.join(paquet.get(c, '') for c in cites)
            manq = {n for n in nums if n not in nombres(source)}
            if manq:
                d['A_nombre_absent_de_l_extrait'].append(f'{sorted(manq)} :: {t[:120]}')
        if DOSE.search(t) and not any(c.lower().startswith('aips') for c in cites):
            d['A_dose_sans_AIPS'].append(t[:140])
    # B — langue
    paras = re.findall(r'<(?:p|div class="p")(?:\s[^>]*)?>(.*?)</(?:p|div)>', h, re.S | re.I)
    sans_conn = sum(1 for p in paras if len(texte(p).split()) > 40 and not CONNECT.search(texte(p)))
    for tag, b, t in ph:
        if tag.lower() in ('td',):
            continue
        n = len(t.split())
        if not est_verbale(t):
            d['B_phrase_nominale'].append(t[:120])
        if n > 32:
            d['B_phrase_longue'].append(f'{n} mots :: {t[:90]}')
        k = hashlib.sha1(re.sub(r'\W+', '', t.lower()).encode()).hexdigest()
        if len(t) > 60:
            if k in vus_lot and vus_lot[k] != chemin:
                d['B_phrase_partagee_entre_fichiers'].append(t[:120])
            elif k in vus_lot.get('_local_' + chemin, set()):
                d['B_phrase_dupliquee'].append(t[:120])
            vus_lot.setdefault(k, chemin)
            vus_lot.setdefault('_local_' + chemin, set()).add(k)
    nph = max(1, len([1 for tg, _, _ in ph if tg.lower() != 'td']))
    conn = sum(1 for tg, _, t in ph if tg.lower() != 'td' and CONNECT.search(t))
    # C — forme
    if a.points:
        manquants = [i for i in range(1, a.points + 1) if not re.search(rf'id="[\w-]*p{i}"', h)]
        if manquants:
            d['C_points_manquants'].append(str(manquants))
    if 'FIN_FICHIER' not in h[-400:]:
        d['C_FIN_FICHIER_absent'].append('-')
    if re.search(r'\stitle=', h):
        d['C_title_interdit'].append(str(len(re.findall(r'\stitle=', h))))
    if re.search(r'<script\b', h, re.I) and not a.script_ok:
        d['C_script_interdit'].append('-')
    nus = len(re.findall(r'<table\b', h)) - len(re.findall(r'overflow-x:\s*auto[^>]*>\s*<table', h))
    if nus > 0:
        d['C_tableau_non_enveloppe'].append(str(nus))
    e = equilibre(h)
    if e:
        d['C_balises'].append(e)
    if not (a.min <= len(brut) <= a.max):
        d['C_taille_hors_bande'].append(f'{len(brut)} o (bande {a.min}–{a.max})')
    rouge = [k for k in d if k.startswith(('A_nombre', 'A_citation', 'A_dose', 'C_points', 'C_FIN', 'C_balises', 'B_phrase_partagee'))]
    verdict = 'ROUGE' if rouge else ('ORANGE' if d else 'VERT')
    return {'fichier': chemin, 'octets': len(brut), 'sha256': hashlib.sha256(brut).hexdigest()[:16],
            'verdict': verdict, 'phrases': nph, 'connecteur%': round(100 * conn / nph),
            'paragraphes_sans_connecteur': sans_conn,
            'defauts': {k: {'n': len(v), 'ex': v[:a.ex]} for k, v in d.items()}}


def charger_paquet(p):
    if not p:
        return {}
    j = json.load(open(p))
    return {x['id']: x['texte'] for x in j['passages']} if isinstance(j, dict) else {x['id']: x['texte'] for x in j}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('fichiers', nargs='+')
    ap.add_argument('--paquet')
    ap.add_argument('--points', type=int, default=14)
    ap.add_argument('--min', type=int, default=100_000)
    ap.add_argument('--max', type=int, default=200_000)
    ap.add_argument('--ex', type=int, default=3, help='exemples par défaut (concision du rapport)')
    ap.add_argument('--script-ok', action='store_true')
    a = ap.parse_args()
    P = charger_paquet(a.paquet)
    vus = {}
    R = [controler(f, P, a, vus) for f in a.fichiers]
    print(json.dumps(R, ensure_ascii=False, indent=1))
    sys.exit(1 if any(r['verdict'] == 'ROUGE' for r in R) else 0)
````

### C-2. `paquet.py` — paquet de preuves (registres de Vial, cache, AIPS en flux, sélection par point)

`paquet.py`
````python
#!/usr/bin/env python3
"""PAQUET — construit gratuitement le paquet de preuves d'une entité (SSP ou DX), point par point.

Entrées (toutes locales, aucune requête modèle) :
  --registres  fichiers JSON/MD de liens déjà validés par Vial (priorité absolue de sélection des sources)
  --textes     extraits déjà lus et datés (evidence/*.txt ; en-tête « URL: » et « Consulté: » recommandé)
  --aips       corpus AipsDownload_*.xml (lu en flux, jamais en entier) + --dci / --autorisation
  --telecharger liste d'URL à rapatrier (cache disque par SHA-256 ; aucune relecture d'une URL déjà en cache)
Sortie : paquet.json = {entite, passages:[{id,source,url,date,texte}], points:{"1":[ids…],…,"14":[…]}}

Usage :
  python3 paquet.py --entite "Ascite de l'hypertension portale" --sortie LOT_166/DX.1/paquet.json \
     --registres data/ck/src.json tools/prevalences/sources_reconnues.json \
     --textes LOT_166/evidence/*.txt --aips AipsDownload_20261008.zip --ham zugelassene_packungen_ham.xlsx \
     --dci spironolact furosemid
"""
import re, os, sys, json, html, hashlib, argparse, datetime, subprocess, urllib.request, collections, math
import zipfile
import xml.etree.ElementTree as ET

CACHE = os.environ.get('PAQUET_CACHE', '.cache/paquet')
# Lexique de sélection par point (nos termes ; enrichissable sans modèle)
POINTS = {
    1: 'définition définit terminologie synonyme classification critères consensus société savante',
    2: 'prévalence incidence épidémiologie suisse OFS Obsan âge sexe mortalité facteurs de risque histoire naturelle',
    3: 'physiopathologie mécanisme cascade lésion perturbation cellule récepteur médiateur',
    4: 'diagnostic différentiel exclure grave urgence red flag drapeau discriminant',
    5: 'anamnèse interrogatoire antécédents symptôme chronologie médicaments drapeaux rouges',
    6: 'examen physique inspection palpation percussion auscultation signe manœuvre sensibilité spécificité',
    7: 'syndrome signes fonctionnels signes physiques tableau clinique',
    8: 'critères diagnostiques majeurs mineurs seuil score stade grade classification',
    9: 'examen complémentaire gold standard référence imagerie biologie échographie scanner IRM ponction interprétation seuil',
    10: 'algorithme arbre décisionnel conduite étape si alors',
    11: 'traitement prise en charge posologie dose mg surveillance urgence grossesse insuffisance rénale hépatique sortie pronostic',
    12: 'prévention dépistage vaccination primaire secondaire tertiaire recommandation',
    13: 'retenir essentiel clé',
    14: 'piège erreur fréquente confusion examen',
}
AIPS_SECTIONS = ('posologie', "mode d'emploi", 'contre-indication', 'mises en garde', 'grossesse', 'allaitement',
                 'interactions', 'effets indésirables', 'surdosage', 'indications')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def html_txt(s):
    s = re.sub(r'<(script|style)\b.*?</\1>', ' ', s, flags=re.S | re.I)
    s = re.sub(r'<(br|/p|/li|/tr|/h\d)\b[^>]*>', '\n', s, flags=re.I)
    return re.sub(r'[ \t]+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()


def telecharger(url):
    """Cache disque (équivalent requests-cache/Hishel, stdlib) : une URL n'est rapatriée qu'une fois."""
    os.makedirs(CACHE, exist_ok=True)
    f = os.path.join(CACHE, sha(url.encode())[:24])
    if os.path.exists(f + '.txt'):
        return open(f + '.txt', encoding='utf-8').read()
    req = urllib.request.Request(url, headers={'User-Agent': 'paquet-medical/1.0 (usage pedagogique)'})
    with urllib.request.urlopen(req, timeout=25) as r:
        brut, typ = r.read(8_000_000), r.headers.get('Content-Type', '')
    open(f + '.raw', 'wb').write(brut)
    if 'pdf' in typ or url.lower().endswith('.pdf'):
        t = subprocess.run(['pdftotext', '-layout', f + '.raw', '-'], capture_output=True, text=True).stdout
    else:
        t = html_txt(brut.decode('utf-8', 'ignore'))
    entete = f'URL: {url}\nConsulté: {datetime.date.today().isoformat()}\nSHA256: {sha(brut)}\n\n'
    open(f + '.txt', 'w', encoding='utf-8').write(entete + t)
    return entete + t


def decouper(texte, stem, source, taille=700):
    url = (re.search(r'^URL:\s*(\S+)', texte, re.M) or [None, ''])[1]
    date = (re.search(r'^Consult[ée]+:\s*(\S+)', texte, re.M) or [None, ''])[1]
    corps = re.sub(r'^(URL|Consult[ée]+|SHA256):.*\n', '', texte, flags=re.M)
    blocs, cur = [], ''
    for para in re.split(r'\n\s*\n|\n(?=[A-ZÀ-Ý0-9•\-])', corps):
        para = re.sub(r'\s+', ' ', para).strip()
        if not para:
            continue
        if len(cur) + len(para) > taille and cur:
            blocs.append(cur)
            cur = ''
        cur = (cur + ' ' + para).strip()
    if cur:
        blocs.append(cur)
    return [{'id': f'{stem}-{i + 1}', 'source': source, 'url': url, 'date': date, 'texte': b} for i, b in enumerate(blocs)]


def ham(xlsx, dcis):
    """Liste Swissmedic HAM (xlsx, lue sans dépendance) : DCI latine/française → numéros d'autorisation (5 chiffres)."""
    z = zipfile.ZipFile(xlsx)
    ss = [html.unescape(re.sub(r'<[^>]+>', '', t)) for t in re.findall(r'<si>(.*?)</si>', z.read('xl/sharedStrings.xml').decode(), re.S)]
    nums = set()
    for row in re.findall(r'<row\b.*?</row>', z.read('xl/worksheets/sheet1.xml').decode(), re.S):
        cel = {}
        for attrs, inner in re.findall(r'<c\b([^>]*)>(.*?)</c>', row, re.S):
            v = re.search(r'<v>(.*?)</v>', inner)
            if v:
                col = re.search(r'r="([A-Z]+)', attrs).group(1)
                cel[col] = ss[int(v.group(1))] if 't="s"' in attrs else v.group(1)
        if any(d.lower() in ' '.join(cel.values()).lower() for d in dcis) and re.fullmatch(r'\d{1,5}', cel.get('A', '')):
            nums.add(cel['A'].zfill(5))  # colonne A = numéro d'autorisation Swissmedic
    return nums


def aips(xml_path, dcis, autorisations, reseau=True):
    """Corpus AIPS = index des informations professionnelles (Type SmPC) : numéro → URL HTML française.
    Lecture en flux ; le texte est ensuite rapatrié (cache) et découpé par rubrique (posologie, grossesse…)."""
    out, cibles, ns = [], [d.lower() for d in dcis], '{https://simisinfo.refdata.ch/MedicinalDocuments/1.0/}'
    if xml_path.endswith('.zip'):  # le zip d'origine se lit en flux, sans extraction sur disque
        z = zipfile.ZipFile(xml_path)
        xml_path = z.open(next(n for n in z.namelist() if n.lower().endswith('.xml')))
    for _, el in ET.iterparse(xml_path, events=('end',)):
        if el.tag != ns + 'MedicinalDocumentsBundle':
            continue
        no = el.findtext(f'{ns}RegulatedAuthorization/{ns}Identifier') or ''
        if el.findtext(ns + 'Type') != 'SmPC':
            el.clear(); continue
        for doc in el.findall(ns + 'AttachedDocument'):
            nom = doc.findtext(ns + 'Description') or ''
            if doc.findtext(ns + 'Language') != 'fr' or not (no in autorisations or any(c in nom.lower() for c in cibles)):
                continue
            url = next((r.findtext(ns + 'Url') for r in doc.findall(ns + 'DocumentReference') if r.findtext(ns + 'ContentType') == 'text/html'), '')
            source = f'AIPS {nom} (Swissmedic {no})'
            out.append({'id': f'aips-{no}-0', 'source': source, 'url': url, 'date': (el.findtext(ns + 'Date') or '')[:10],
                        'texte': f'Information professionnelle {nom}, autorisation Swissmedic {no}.'})
            if reseau and url:
                try:
                    contenu = telecharger(url)
                    k = 0  # compteur unique par document : un ID d'extrait ne se répète jamais entre rubriques
                    for sec in re.split(r'\n(?=(?:' + '|'.join(AIPS_SECTIONS) + r'))', contenu, flags=re.I):
                        if sec.lower().startswith(AIPS_SECTIONS):
                            for p in decouper(sec, f'aips-{no}', source, 900):
                                k += 1
                                p.update(id=f'aips-{no}-{k}', url=url)
                                out.append(p)
                except Exception as e:
                    print(f'AIPS {no} non rapatrié ({e}) : URL consignée, aucune dose écrite sans texte lu', file=sys.stderr)
        el.clear()
    return out


def registres(chemins):
    """Liens validés de Vial : servent d'ordre de priorité (domaines + URL exactes)."""
    urls = []
    for c in chemins:
        s = open(c, encoding='utf-8', errors='ignore').read()
        urls += re.findall(r'https?://[^\s"\'<>)\]]+', s)
    dom = collections.Counter(re.sub(r'^https?://(www\.)?', '', u).split('/')[0] for u in urls)
    return set(urls), dom


def selection(passages, entite, k=8):
    """BM25 allégé (stdlib) : passages les plus pertinents pour chaque point."""
    tok = lambda s: re.findall(r'\w{3,}', s.lower())
    docs = [tok(p['texte']) for p in passages]
    N, df = len(docs) or 1, collections.Counter(w for d in docs for w in set(d))
    moy = sum(map(len, docs)) / N if docs else 1
    out = {}
    for n, mots in POINTS.items():
        q = tok(mots) + tok(entite) * 2
        sc = []
        for i, d in enumerate(docs):
            tf = collections.Counter(d)
            s = sum(math.log(1 + (N - df[w] + .5) / (df[w] + .5)) * tf[w] * 2.2 / (tf[w] + 1.2 * (.25 + .75 * len(d) / moy))
                    for w in q if w in tf)
            if n == 11 and passages[i]['id'].startswith('aips'):
                s *= 2  # le point 11 privilégie l'AIPS
            sc.append((s, passages[i]['id']))
        out[str(n)] = [i for s, i in sorted(sc, reverse=True)[:k] if s > 0]
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--entite', required=True)
    ap.add_argument('--sortie', required=True)
    ap.add_argument('--registres', nargs='*', default=[])
    ap.add_argument('--textes', nargs='*', default=[])
    ap.add_argument('--telecharger', help='fichier texte : une URL par ligne')
    ap.add_argument('--aips')
    ap.add_argument('--dci', nargs='*', default=[])
    ap.add_argument('--autorisation', nargs='*', default=[])
    ap.add_argument('--ham', help='liste Swissmedic HAM .xlsx : traduit --dci en numéros d’autorisation')
    ap.add_argument('--hors-ligne', action='store_true')
    ap.add_argument('--k', type=int, default=8)
    a = ap.parse_args()
    P = []
    for t in a.textes:
        P += decouper(open(t, encoding='utf-8', errors='ignore').read(), os.path.splitext(os.path.basename(t))[0], t)
    valides, domaines = registres(a.registres) if a.registres else (set(), {})
    if a.telecharger:
        for u in [l.strip() for l in open(a.telecharger) if l.strip().startswith('http')]:
            try:
                P += decouper(telecharger(u), 'w' + sha(u.encode())[:6], u)
            except Exception as e:
                print(f'ECHEC {u} : {e}', file=sys.stderr)  # échec dit, jamais contourné
    autor = set(a.autorisation) | (ham(a.ham, a.dci) if a.ham and a.dci else set())
    if a.aips and (a.dci or autor):
        P += aips(a.aips, a.dci, autor, reseau=not a.hors_ligne)
    for p in P:
        d = re.sub(r'^https?://(www\.)?', '', p['url'] or '').split('/')[0]
        p['priorite'] = 2 if p['url'] in valides else (1 if d in domaines else 0)
    P.sort(key=lambda p: -p['priorite'])
    os.makedirs(os.path.dirname(a.sortie) or '.', exist_ok=True)
    json.dump({'entite': a.entite, 'genere': datetime.datetime.now().isoformat(timespec='minutes'),
               'passages': P, 'points': selection(P, a.entite, a.k)}, open(a.sortie, 'w'), ensure_ascii=False, indent=1)
    print(f'{a.sortie} : {len(P)} passages, {sum(p["id"].startswith("aips") for p in P)} AIPS')
````

### C-3. `rediger.py` — instanciation et appel en une passe

`rediger.py`
````python
#!/usr/bin/env python3
"""REDIGER — instancie le prompt de point (P-POINT) avec le paquet, appelle UN modèle en UNE passe, archive.

Moteurs (gratuits d'abord) :
  --moteur local      : modèle installé sur la machine (serveur local, http://127.0.0.1:11434/api/generate)
  --moteur compatible : tout point /v1/chat/completions (passerelle LiteLLM, LM Studio, vLLM, Portkey…) via --url/--cle
  --moteur sec        : n'appelle rien ; écrit les prompts instanciés (copier-coller manuel dans l'IA de rédaction choisie)
Le nom du modèle se passe par --modele ou par la variable d'environnement MODELE_LOCAL.
Règles : une sortie reçue n'est JAMAIS renvoyée au modèle (pas d'aller-retour) ; la correction est chirurgicale
(auditeur) ; une réponse vide/coupée réseau peut être relancée UNE fois.

Usage :
  python3 rediger.py --gabarit P-POINT.txt --paquet DX.1/paquet.json --contrat contrat.json \
     --points 1-14 --sortie DX.1/fragments --moteur local --modele "$MODELE_LOCAL"
contrat.json : {"LOT":"166","CODE_SSP":"F2.18","ENTITE":"…","PREFIX":"dx1","SECURITE":"…",
                "points":{"1":{"titre":"Définition et sémantique","exige":"…","octets":6000,"squelette":"…"}, …}}
"""
import os, re, json, time, argparse, hashlib, urllib.request


def passages(paquet, ids, plafond):
    P = {p['id']: p for p in paquet['passages']}
    out, n = [], 0
    for i in ids:
        p = P.get(i)
        if not p:
            continue
        bloc = f"[{i}] ({p['source']}, {p.get('date') or 's.d.'}) {p['texte']}"
        if n + len(bloc) > plafond:
            break
        out.append(bloc)
        n += len(bloc)
    return '\n'.join(out) or '(aucun extrait : n’écris que des phrases sans chiffre, ou laisse le point court)'


def appeler(moteur, modele, prompt, octets, url, cle):
    num = int(1.3 * octets / 3.3)
    if moteur == 'local':
        corps = {'model': modele, 'prompt': prompt, 'stream': False, 'think': False,
                 'options': {'temperature': 0.2, 'repeat_penalty': 1.1, 'num_ctx': 8192, 'num_predict': num}}
        req = urllib.request.Request(url or 'http://127.0.0.1:11434/api/generate', json.dumps(corps).encode(),
                                     {'Content-Type': 'application/json'})
        return json.loads(urllib.request.urlopen(req, timeout=900).read())['response']
    corps = {'model': modele, 'temperature': 0.2, 'max_tokens': num, 'messages': [{'role': 'user', 'content': prompt}]}
    req = urllib.request.Request(url, json.dumps(corps).encode(),
                                 {'Content-Type': 'application/json', 'Authorization': f'Bearer {cle or ""}'})
    return json.loads(urllib.request.urlopen(req, timeout=900).read())['choices'][0]['message']['content']


def plage(s):
    a, _, b = s.partition('-')
    return list(range(int(a), int(b or a) + 1))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--gabarit', required=True)
    ap.add_argument('--paquet', required=True)
    ap.add_argument('--contrat', required=True)
    ap.add_argument('--points', default='1-14')
    ap.add_argument('--sortie', required=True)
    ap.add_argument('--moteur', default='sec', choices=['local', 'compatible', 'sec'])
    ap.add_argument('--modele', default=os.environ.get('MODELE_LOCAL', ''))
    ap.add_argument('--url')
    ap.add_argument('--cle', default=os.environ.get('CLE_API'))
    ap.add_argument('--plafond', type=int, default=9000, help='caractères d’extraits par point')
    a = ap.parse_args()
    G, PQ, C = open(a.gabarit).read(), json.load(open(a.paquet)), json.load(open(a.contrat))
    os.makedirs(a.sortie, exist_ok=True)
    for n in plage(a.points):
        dest = os.path.join(a.sortie, f'p{n:02d}.html')
        if os.path.exists(dest):
            continue  # déjà reçu : jamais régénéré (anti-aller-retour)
        pt = C['points'][str(n)]
        val = dict(C, N=n, TITRE_POINT=pt['titre'], CONTENU_EXIGE=pt['exige'], OCTETS_CIBLE=pt['octets'],
                   SQUELETTE=pt.get('squelette', ''), PASSAGES=passages(PQ, PQ['points'].get(str(n), []), a.plafond))
        prompt = re.sub(r'\{(\w+)\}', lambda m: str(val.get(m.group(1), m.group(0))), G)
        open(os.path.join(a.sortie, f'p{n:02d}.prompt.txt'), 'w').write(prompt)
        if a.moteur == 'sec':
            continue
        for essai in (1, 2):
            try:
                t0 = time.time()
                rep = appeler(a.moteur, a.modele, prompt, pt['octets'], a.url, a.cle)
                break
            except Exception as e:
                rep = None
                if essai == 2:
                    print(f'p{n}: échec réseau {e}')
        if rep:
            rep = re.sub(r'^```(?:html)?\s*|\s*```$', '', rep.strip())
            open(dest, 'w').write(rep)
            json.dump({'modele': a.modele, 'secondes': round(time.time() - t0), 'octets': len(rep.encode()),
                       'sha256_prompt': hashlib.sha256(prompt.encode()).hexdigest()},
                      open(dest + '.meta.json', 'w'))
            print(f'p{n}: {len(rep.encode())} o')
````

### C-4. `images.py` — automate collecteur d'images libres

`images.py`
````python
#!/usr/bin/env python3
"""IMAGES — automate collecteur gratuit de clichés et figures sous licence libre (zéro modèle).

Fournisseurs (API publiques, sans clé) :
  commons   : Wikimedia Commons (namespace Fichier) — licence lue dans extmetadata de CHAQUE fichier
  europepmc : articles en accès ouvert (licence d'ARTICLE ; la figure reste « à relire »)
  catalogue : ressources académiques de Vial (Radiopaedia, Radiology Assistant, Ultrasound Cases, Eurorad…)
              → LIEN DE CAS uniquement, jamais de copie (droits non établis)
Règles : NC/ND/licence inconnue = refus ; une requête précise par figure ; cache disque ; budget journalier ;
aucune insertion automatique ; planche HTML de contrôle visuel (un seul coup d'œil pour tout le lot).

Usage :
  python3 images.py --lot LOT_166 --besoins besoins.json [--budget 60]
  besoins.json : [{"dx":"DX.1","point":9,"modalite":"échographie","requete":"ascites ultrasound Morison"}]
Sortie : LOT_166/images/CANDIDATS.json + LOT_166/images/PLANCHE.html + LOT_166/images/<sha>.<ext>
"""
import os, re, sys, json, hashlib, argparse, urllib.request, urllib.parse, datetime, html

UA = {'User-Agent': 'collecteur-images-pedagogique/1.0 (cours medicaux; contact via depot)'}
LIBRES = re.compile(r'^(cc0|cc[- ]by(?:[- ]sa)?(?:[- ]\d\.\d)?|public domain|pd|domaine public)', re.I)
REFUS = re.compile(r'\bnc\b|\bnd\b|non.?commercial|no.?deriv', re.I)
CATALOGUE = {
    'Radiopaedia': 'https://radiopaedia.org/search?q={q}&scope=cases',
    'Radiology Assistant': 'https://radiologyassistant.nl/search?q={q}',
    'Ultrasound Cases': 'https://www.ultrasoundcases.info/search/?q={q}',
    'Eurorad (ESR)': 'https://www.eurorad.org/advanced-search?search={q}',
    'Learning Radiology': 'https://www.learningradiology.com/',
    'Case Stacks': 'https://casestacks.com/',
    'Casimage (UNIGE)': 'https://www.casimage.com/',
    'RadioSurf (UniBE)': 'https://elearning.medizin.unibe.ch/',
}


def get(url, cache, budget):
    os.makedirs(cache, exist_ok=True)
    f = os.path.join(cache, hashlib.sha256(url.encode()).hexdigest()[:24])
    if os.path.exists(f):
        return open(f, 'rb').read()
    if budget['reste'] <= 0:
        raise RuntimeError('budget journalier épuisé')
    budget['reste'] -= 1
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r:
        b = r.read(15_000_000)
    open(f, 'wb').write(b)
    return b


def commons(q, cache, budget, n=6):
    p = {'action': 'query', 'format': 'json', 'generator': 'search', 'gsrnamespace': 6, 'gsrsearch': q,
         'gsrlimit': n, 'prop': 'imageinfo', 'iiprop': 'url|mime|size|extmetadata', 'iiurlwidth': 900}
    j = json.loads(get('https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(p), cache, budget))
    out = []
    for pg in (j.get('query', {}).get('pages', {}) or {}).values():
        ii = (pg.get('imageinfo') or [{}])[0]
        m = {k: re.sub('<[^>]+>', '', v.get('value', '')) for k, v in (ii.get('extmetadata') or {}).items()}
        lic = m.get('LicenseShortName', '')
        ok = bool(LIBRES.search(lic)) and not REFUS.search(lic)
        out.append({'fournisseur': 'commons', 'titre': pg.get('title'), 'page': ii.get('descriptionurl'),
                    'fichier': ii.get('thumburl') or ii.get('url'), 'mime': ii.get('mime'),
                    'auteur': m.get('Artist', '')[:200], 'licence': lic, 'licence_url': m.get('LicenseUrl', ''),
                    'description': m.get('ImageDescription', '')[:400],
                    'decision': 'admissible_a_inspecter' if ok else 'refuse_licence'})
    return out


def europepmc(q, cache, budget, n=5):
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urllib.parse.urlencode(
        {'query': f'({q}) AND OPEN_ACCESS:Y AND HAS_FT:Y', 'format': 'json', 'resultType': 'core', 'pageSize': n})
    j = json.loads(get(url, cache, budget))
    out = []
    for it in j.get('resultList', {}).get('result', []):
        lic = it.get('license') or ''
        ok = bool(LIBRES.search(lic.replace('-', ' '))) and not REFUS.search(lic)
        out.append({'fournisseur': 'europepmc', 'titre': it.get('title'), 'page': f"https://europepmc.org/article/PMC/{it.get('pmcid')}",
                    'fichier': None, 'auteur': (it.get('authorString') or '')[:200], 'licence': lic,
                    'decision': 'article_admissible_figure_a_relire' if ok else 'refuse_licence'})
    return out


def acquerir(c, dossier, cache, budget):
    """Rapatrie seulement les candidats Commons admissibles ; empreinte SHA-256 = identité de la figure."""
    if c['decision'] != 'admissible_a_inspecter' or not c.get('fichier'):
        return c
    b = get(c['fichier'], cache, budget)
    h = hashlib.sha256(b).hexdigest()
    ext = {'image/png': 'png', 'image/jpeg': 'jpg', 'image/svg+xml': 'svg', 'image/webp': 'webp'}.get(c.get('mime'), 'jpg')
    nom = f'{h[:16]}.{ext}'
    open(os.path.join(dossier, nom), 'wb').write(b)
    c.update(local=nom, sha256=h, acquis=datetime.datetime.now().isoformat(timespec='seconds'),
             inspection_visuelle=False, publication_ready=False)
    return c


def planche(cands, chemin):
    cases = []
    for c in cands:
        img = f'<img src="{c["local"]}" loading="lazy" style="max-width:100%;max-height:260px">' if c.get('local') else '<em>lien seul</em>'
        cases.append(f'<figure style="border:1px solid #889;padding:6px;margin:0"><b>{html.escape(c["besoin"])}</b><br>{img}'
                     f'<figcaption style="font-size:12px">{html.escape(c.get("titre") or "")}<br>{html.escape(c.get("licence") or "")} · '
                     f'{html.escape(c.get("auteur") or "")[:80]}<br><a href="{c.get("page")}">source</a> · {c["decision"]}</figcaption></figure>')
    open(chemin, 'w').write('<!doctype html><meta charset="utf-8"><title>Planche</title><body style="font:14px sans-serif;background:#eef1f3">'
                            '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:8px">'
                            + ''.join(cases) + '</div>')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--lot', required=True)
    ap.add_argument('--besoins', required=True)
    ap.add_argument('--budget', type=int, default=60)
    ap.add_argument('--cache', default='.cache/images')
    a = ap.parse_args()
    d = os.path.join(a.lot, 'images')
    os.makedirs(d, exist_ok=True)
    budget, tout = {'reste': a.budget}, []
    for b in json.load(open(a.besoins)):
        tag = f"{b['dx']} · point {b['point']} · {b['modalite']}"
        for f in (commons, europepmc):
            try:
                for c in f(b['requete'], a.cache, budget):
                    c['besoin'] = tag
                    tout.append(acquerir(c, d, a.cache, budget))
            except Exception as e:  # échec déclaré, jamais contourné
                tout.append({'besoin': tag, 'fournisseur': f.__name__, 'decision': f'echec: {e}'})
        for nom, u in CATALOGUE.items():
            tout.append({'besoin': tag, 'fournisseur': 'catalogue_vial', 'titre': nom,
                         'page': u.format(q=urllib.parse.quote(b['requete'])), 'decision': 'lien_de_cas_uniquement'})
    json.dump(tout, open(os.path.join(d, 'CANDIDATS.json'), 'w'), ensure_ascii=False, indent=1)
    planche([c for c in tout if c.get('fournisseur') != 'catalogue_vial'], os.path.join(d, 'PLANCHE.html'))
    print(f"{d}: {sum(1 for c in tout if c.get('local'))} images acquises, {budget['reste']} requêtes restantes")
````

### C-5. `assembler.py` — HTML final, Sources citées seules, manifeste

`assembler.py`
````python
#!/usr/bin/env python3
"""ASSEMBLER — fragments de points → HTML final autonome (charte Vial), Sources limitées aux extraits cités,
FIN_FICHIER, puis MANIFESTE (octets + SHA-256). Zéro modèle.

Usage :
  python3 assembler.py --fragments DX.1/fragments --paquet DX.1/paquet.json --contrat contrat.json \
     --titre "DX.1 — Ascite de l'hypertension portale" --sortie LOT_166_Phase_B_V0_DX.1.html [--figures DX.1/figures.json]
figures.json : [{"point":9,"fichier":"images/ab12.jpg","legende":"…","attribution":"Auteur, CC BY-SA 4.0, URL"}]
(les figures ne sont insérées qu'après inspection visuelle validée : clé "inspectee": true)
"""
import os, re, json, html, hashlib, argparse, base64

CSS = """:root{--fond:#eef1f3;--ilot:#fff;--encre:#16202a;--accent:#0b5c7a;--bord:#c9d2d9;--alerte:#9b1c1c}
*{box-sizing:border-box}body{margin:0;background:var(--fond);color:var(--encre);font:16px/1.55 "Atkinson Hyperlegible",Verdana,sans-serif}
main{max-width:980px;margin:0 auto;padding:12px}h2{font-size:1.35rem;margin:.4rem 0 1rem}
section.ilot{background:var(--ilot);border:1px solid var(--bord);border-radius:10px;padding:14px 16px;margin:0 0 14px;
box-shadow:0 1px 0 #fff inset,3px 4px 0 #cfd8de,6px 8px 14px rgba(20,40,60,.12)}
h3{font-size:1.08rem;margin:0 0 .5rem;color:var(--accent)}.p{margin:0 0 .7rem}
.t{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:.93rem}td,th{border:1px solid var(--bord);padding:5px 7px;vertical-align:top}
.fenetre{max-width:min(860px,94vw);max-height:86vh;overflow:auto;border:2px solid var(--accent);border-radius:12px;padding:16px 18px;
box-shadow:0 18px 50px rgba(0,0,0,.35)}.fenetre::backdrop{background:rgba(10,20,30,.45)}
button.w{all:unset;color:var(--accent);border-bottom:1px dotted var(--accent);cursor:pointer}
sup.r a{font-size:.72em;color:#557;text-decoration:none}.alerte{border-left:5px solid var(--alerte);padding-left:10px}
figure{margin:.6rem 0}figure img{max-width:100%;height:auto;border-radius:6px}figcaption{font-size:.86rem;color:#445}
@media(max-width:420px){body{font-size:15px}section.ilot{padding:10px}}"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--fragments', required=True)
    ap.add_argument('--paquet', required=True)
    ap.add_argument('--contrat', required=True)
    ap.add_argument('--titre', required=True)
    ap.add_argument('--sortie', required=True)
    ap.add_argument('--figures')
    ap.add_argument('--integrer-images', action='store_true', help='images en data: URI (fichier autonome)')
    a = ap.parse_args()
    C, PQ = json.load(open(a.contrat)), json.load(open(a.paquet))
    P = {p['id']: p for p in PQ['passages']}
    figs = [f for f in (json.load(open(a.figures)) if a.figures else []) if f.get('inspectee')]
    pre = C.get('PREFIX', 'dx')
    corps, cites = [], []
    for n in range(1, 15):
        f = os.path.join(a.fragments, f'p{n:02d}.html')
        frag = open(f).read() if os.path.exists(f) else '<div class="p">POINT MANQUANT</div>'
        cites += re.findall(r'href="#sb-([\w.\-:]+)"', frag)
        fig = ''
        for g in (x for x in figs if x['point'] == n):
            src = g['fichier']
            if a.integrer_images:
                ext = src.rsplit('.', 1)[-1].replace('jpg', 'jpeg')
                src = f"data:image/{ext};base64," + base64.b64encode(open(src, 'rb').read()).decode()
            fig += (f'<figure><img src="{src}" alt="{html.escape(g["legende"])}"><figcaption>{html.escape(g["legende"])} '
                    f'— {html.escape(g["attribution"])}</figcaption></figure>')
        corps.append(f'<section class="ilot" id="{pre}-p{n}"><h3 id="{pre}-h{n}"><strong>{n}. '
                     f'{html.escape(C["points"][str(n)]["titre"])}</strong></h3>{frag}{fig}</section>')
    vus = list(dict.fromkeys(cites))
    src = ''.join(f'<li id="sb-{i}">[{i}] {html.escape(P[i]["source"])}{" — " + html.escape(P[i]["url"]) if P[i].get("url") else ""}'
                  f'{" (consulté le " + P[i]["date"] + ")" if P[i].get("date") else ""}</li>' for i in vus if i in P)
    nom = os.path.splitext(os.path.basename(a.sortie))[0]
    doc = (f'<!DOCTYPE html>\n<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<title>{html.escape(a.titre)}</title><style>{CSS}</style></head><body><main><h2>{html.escape(a.titre)}</h2>'
           + '\n'.join(corps) +
           f'<section class="ilot" id="{pre}-sources"><h3>Sources</h3><ol>{src}</ol><p class="p">Le contenu reprend les sources citées ; '
           f'il n’a pas été validé cliniquement par un médecin.</p></section></main></body></html>\n<!-- FIN_FICHIER {nom} -->\n')
    open(a.sortie, 'w').write(doc)
    b = doc.encode()
    man = os.path.join(os.path.dirname(a.sortie) or '.', 'MANIFESTE.json')
    m = json.load(open(man)) if os.path.exists(man) else {}
    m[os.path.basename(a.sortie)] = {'octets': len(b), 'sha256': hashlib.sha256(b).hexdigest()}
    json.dump(m, open(man, 'w'), ensure_ascii=False, indent=1)
    absents = [i for i in vus if i not in P]
    print(f'{a.sortie}: {len(b)} o, {len(vus)} sources citées' + (f', CITATIONS INCONNUES {absents}' if absents else ''))


if __name__ == '__main__':
    main()
````

### C-6. Légion — `mere.py` et `soldat.py` (état des dépôts sans modèle)

`mere.py`
````python
#!/usr/bin/env python3
"""MÈRE — lève la légion : 1 fetch groupé, puis N soldats (processus clones de soldat.py) en vagues parallèles.
Zéro modèle. Sortie : rapports/*.json (1 par soldat) + DIGEST.md (seul fichier lu par le modèle).

Usage : python3 mere.py <depot> [--jours 10] [--soldats 16]
"""
import sys, os, json, subprocess, argparse, re, time
from concurrent.futures import ThreadPoolExecutor

ICI = os.path.dirname(os.path.abspath(__file__))


def git(depot, *a, t=900):
    return subprocess.run(['git', '-C', depot, *a], capture_output=True, text=True, errors='ignore', timeout=t).stdout


def soldat(args):
    p = subprocess.run([sys.executable, os.path.join(ICI, 'soldat.py'), *args], capture_output=True, text=True, timeout=300)
    try:
        return json.loads(p.stdout)
    except Exception:
        return {'erreur': ' '.join(args)[-120:], 'stderr': p.stderr[-200:]}


def vague(nom, missions, n, out):
    t = time.time()
    with ThreadPoolExecutor(n) as ex:
        res = list(ex.map(soldat, missions))
    with open(os.path.join(out, f'{nom}.json'), 'w') as fh:
        json.dump(res, fh, ensure_ascii=False, indent=0)
    print(f'vague {nom}: {len(missions)} soldats, {time.time()-t:.0f}s', file=sys.stderr)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('depot')
    ap.add_argument('--jours', type=int, default=10)
    ap.add_argument('--soldats', type=int, default=16)
    a = ap.parse_args()
    D = os.path.abspath(a.depot)
    nom = os.path.basename(D)
    out = os.path.join(ICI, 'rapports', nom)
    os.makedirs(out, exist_ok=True)

    # Vague 0 — branches récentes, un seul fetch groupé (profondeur 1)
    refs = git(D, 'for-each-ref', '--sort=-committerdate', '--format=%(committerdate:unix) %(refname:short)', 'refs/remotes').split('\n')
    seuil = time.time() - a.jours * 86400
    actives = [r.split()[1] for r in refs if r and int(r.split()[0]) >= seuil and r.split()[1] not in ('origin', 'origin/HEAD')]
    specs = [f'+refs/heads/{b[7:]}:refs/remotes/{b}' for b in actives]
    for i in range(0, len(specs), 40):
        git(D, 'fetch', '-q', '--depth=1', 'origin', *specs[i:i + 40])

    # Vague 1 — un soldat par branche
    B = vague('1_branches', [['branche', D, b] for b in actives], a.soldats, out)

    # Vague 2 — un soldat par LOT (version la plus récente), par prompt, par fichier de liens
    lot_ref = {}
    for r in B:  # B est trié du plus récent au plus ancien
        for L in r.get('lots', []):
            lot_ref.setdefault(L, r['ref'])
    tree = git(D, 'ls-tree', '-r', '--name-only', 'origin/main').splitlines()
    chemins_main = {}
    for f in tree:
        m = re.search(r'^(.*LOT_(\d{3}))/', f)
        if m and not f.startswith(('audit', 'qa')):
            chemins_main.setdefault(int(m.group(2)), m.group(1))
    missions_lot = []
    for L, ref in lot_ref.items():
        cands = [f for f in git(D, 'ls-tree', '-r', '--name-only', ref).splitlines() if f'LOT_{L:03d}/' in f and f.endswith('.html')]
        if cands:
            missions_lot.append(['lot', D, ref, cands[0].rsplit('/', 1)[0]])
    for L, ch in chemins_main.items():
        if L not in lot_ref:
            missions_lot.append(['lot', D, 'origin/main', ch])
    LOTS = vague('2_lots', missions_lot, a.soldats, out)

    prompts = set()
    for r in B:
        for f in r.get('prompts', []):
            prompts.add((r['ref'], f))
    for f in tree:
        if re.search(r'(PROMPT|HARNAIS|SKILL|AGENTS|CLAUDE|LIRE|SPEC|REPRISE|TRANSITION)[^/]*\.md$', f, re.I) and not f.startswith(('audit', 'livraisons', 'qa')):
            prompts.add(('origin/main', f))
    P = vague('3_prompts', [['prompt', D, r, f] for r, f in sorted(prompts)], a.soldats, out)

    liens = [f for f in tree if re.search(r'(lien|link|source|ressource|refer|imag|biblio)[^/]*\.(md|txt|json)$', f, re.I)
             and not f.startswith(('audit', 'qa', 'livraisons', 'nosology'))][:120]
    LI = vague('4_liens', [['liens', D, 'origin/main', f] for f in liens], a.soldats, out)

    # Digest ultra-concis
    o = [f'# DIGEST {nom} — {len(actives)} branches actives ({a.jours} j), {len(missions_lot)} LOT/chap., {len(P)} prompts, {len(LI)} fichiers liens']
    o.append('## Branches (date sujet | LOTs | prompts/outils neufs)')
    for r in B[:30]:
        o.append(f"- {r.get('sujet','')[:90]} | {r.get('lots')} | {r.get('prompts')} {r.get('outils', [])[:4]}")
    o.append('## LOTs (n | dx | figs | img | src | verbe% | connect% | outils)')
    for r in sorted(LOTS, key=lambda x: x.get('lot', '')):
        if 'lot' in r:
            o.append(f"- {r['lot'].split('/')[-1]}@{r['ref'].split('/')[-1][:22]} | {r['dx']} | {r['figs']} | {r['img']} | {r['src']} | {r['verbe%']} | {r['connect%']} | {r['outils'][:5]}")
    gab = {}
    for r in LOTS:
        for t in r.get('titres', []):
            gab[t] = gab.get(t, 0) + 1
    o.append('## Gabarit dominant (titre ×LOTs)')
    o.append('; '.join(f'{t}×{n}' for t, n in sorted(gab.items(), key=lambda x: -x[1])[:30]))
    o.append('## Prompts (Ko | BLOQUANT | interdit | lignes dupliquées) — plan')
    for r in sorted(P, key=lambda x: -x.get('Ko', 0))[:25]:
        if 'f' in r:
            o.append(f"- {r['f']}@{r['ref'].split('/')[-1][:20]} ({r['Ko']}|{r['bloquant']}|{r['interdit']}|{r['doublons_lignes']}) :: " + ' | '.join(r['plan'][:18]))
    o.append('## Liens (urls/suisses/imagerie)')
    for r in sorted(LI, key=lambda x: -(x.get('swiss', 0) + x.get('img', 0)))[:20]:
        if 'f' in r and r['urls']:
            o.append(f"- {r['f']} {r['urls']}/{r['swiss']}/{r['img']} {list(r['dom'])[:6]}")
    err = [r for r in B + LOTS + P + LI if 'erreur' in r]
    o.append(f'## Erreurs soldats : {len(err)}')
    with open(os.path.join(out, 'DIGEST.md'), 'w') as fh:
        fh.write('\n'.join(o))
    print(os.path.join(out, 'DIGEST.md'))


if __name__ == '__main__':
    main()
````

`soldat.py`
````python
#!/usr/bin/env python3
"""SOLDAT — un clone, une mission, zéro modèle. Lit un dépôt git SANS checkout (git show), écrit ≤ 3 Ko JSON.

Missions :
  branche  <depot> <ref>            : fichiers ajoutés/modifiés vs main (hors gros HTML), prompts/outils neufs, LOTs touchés
  lot      <depot> <ref> <chemin>   : structure + qualité d'un LOT (titres, images, sources, % verbe, % connecteur)
  prompt   <depot> <ref> <fichier>  : plan Macro→Micro (titres), taille, règles BLOQUANT/INTERDIT comptées
  liens    <depot> <ref> <fichier>  : domaines, suisses, imagerie
"""
import sys, re, json, subprocess, html, collections, os

sys.path.insert(0, os.path.dirname(__file__))
from legion import qualite, html_text, HEAD_RE, MD_HEAD, URL_RE, SWISS, IMG_DOM  # réutilise les règles


def git(depot, *a):
    return subprocess.run(['git', '-C', depot, *a], capture_output=True, text=True, errors='ignore', timeout=120).stdout


def m_branche(depot, ref):
    base = git(depot, 'merge-base', 'origin/main', ref).strip() or 'origin/main'
    lignes = git(depot, 'diff', '--name-status', '--no-renames', 'origin/main', ref).splitlines()
    fichiers = [l.split('\t', 1) for l in lignes if '\t' in l and not l.startswith('D')]  # suppressions exclues
    lots = sorted({int(m) for _, f in fichiers for m in re.findall(r'LOT_(\d{3})', f)})
    neufs = [f for s, f in fichiers if not re.search(r'LOT_\d{3}/.*\.html$|^audit/|\.(png|jpe?g|webp|pdf)$', f)]
    return {'ref': ref, 'n': len(fichiers), 'lots': lots,
            'hors_lot': neufs[:25], 'prompts': [f for f in neufs if re.search(r'PROMPT|HARNAIS|SKILL|AGENTS|CLAUDE|LIRE', f, re.I)][:10],
            'outils': [f for f in neufs if f.endswith('.py')][:15],
            'sujet': git(depot, 'log', '-1', '--format=%cs %s', ref).strip()[:120]}


def m_lot(depot, ref, chemin):
    noms = git(depot, 'ls-tree', '-r', '--name-only', ref, '--', chemin).splitlines()
    dx = [n for n in noms if re.search(r'DX\.\d+\.html$', n)]
    figs = [n for n in noms if re.search(r'\.(png|jpe?g|webp|svg)$', n)]
    q, h, img, src = [], collections.Counter(), 0, 0
    for n in [x for x in noms if x.endswith('.html')][:12]:
        s = git(depot, 'show', f'{ref}:{n}')
        img += len(re.findall(r'<img\b|<svg\b', s, re.I))
        src += len(re.findall(r'href=["\']https?://', s))
        h.update(re.sub(r'\d+', '#', html_text(t))[:50] for l, t in HEAD_RE.findall(s) if l in '23')
        q.append(qualite(html_text(s)))
    q = [x for x in q if x.get('n')]
    moy = lambda k: round(sum(x[k] for x in q) / len(q)) if q else None
    return {'ref': ref, 'lot': chemin, 'dx': len(dx), 'figs': len(figs), 'img': img, 'src': src,
            'verbe%': moy('verbe%'), 'connect%': moy('connect%'), 'titres': [t for t, _ in h.most_common(16)],
            'annexes': [n.split('/')[-1] for n in noms if n.endswith('.md')][:8],
            'outils': [n.split('/')[-1] for n in noms if n.endswith('.py')][:12]}


def m_prompt(depot, ref, f):
    s = git(depot, 'show', f'{ref}:{f}')
    return {'ref': ref, 'f': f, 'Ko': round(len(s.encode()) / 1024, 1),
            'plan': [('#' * len(a)) + ' ' + b[:80] for a, b in MD_HEAD.findall(s)][:60],
            'bloquant': len(re.findall(r'BLOQUAN', s)), 'interdit': len(re.findall(r'(?i)interdit', s)),
            'doublons_lignes': sum(n - 1 for n in collections.Counter(l.strip() for l in s.splitlines() if len(l.strip()) > 40).values() if n > 1)}


def m_liens(depot, ref, f):
    s = git(depot, 'show', f'{ref}:{f}')
    u = URL_RE.findall(s)
    d = collections.Counter(re.sub(r'^https?://(www\.)?', '', x).split('/')[0].lower() for x in u)
    return {'ref': ref, 'f': f, 'urls': len(u), 'swiss': sum(n for k, n in d.items() if any(z in k for z in SWISS)),
            'img': sum(n for k, n in d.items() if any(z in k for z in IMG_DOM)), 'dom': dict(d.most_common(12))}


if __name__ == '__main__':
    mission, *args = sys.argv[1:]
    r = {'branche': m_branche, 'lot': m_lot, 'prompt': m_prompt, 'liens': m_liens}[mission](*args)
    print(json.dumps(r, ensure_ascii=False, separators=(',', ':')))
````

`legion.py`
````python
#!/usr/bin/env python3
"""LÉGION — collecteur gratuit, multi-processus, multi-escouades (stdlib seule).

Usage : python3 legion.py <depot1> [<depot2> ...] --out <dossier>
Sortie : legion_digest.json (complet) + legion_digest.md (ultra-concis, à lire par un modèle).
Coût modèle : 0. Réutilisable comme contrôleur qualité (escouade QUALITE).
"""
import os, re, sys, json, html, subprocess, collections, argparse
from concurrent.futures import ProcessPoolExecutor

SKIP_DIRS = {'.git', 'node_modules', '__pycache__', '.venv', 'dist'}
TXT_EXT = {'.md', '.txt', '.json', '.html', '.py', '.yml', '.yaml', '.js'}
URL_RE = re.compile(r'https?://[^\s)"\'<>\]]+')
LOT_RE = re.compile(r'LOT[_ ]?(\d{3})', re.I)
DX_RE = re.compile(r'DX\.(\d+)')
SWISS = ('compendium.ch', 'swissmedicinfo', 'bag.admin.ch', 'admin.ch', 'sgim', 'ssmi', 'swissmedic',
         'medix.ch', 'pharmavista', 'sginf', 'ssi', 'chuv.ch', 'hug.ch', 'unige', 'unil', 'iml', 'kssg',
         'usz.ch', 'insel', 'smw.ch', 'revmed.ch', 'aips', 'ssp', 'fmh.ch', 'swissnoso', 'infovac', 'sgk',
         'swisscardio', 'sggg', 'paediatrieschweiz', 'tox', 'svgo', 'sgp', 'suva')
IMG_DOM = ('radiopaedia', 'wikimedia', 'openi.nlm', 'dermnet', 'eyewiki', 'pathpedia', 'ecgwaves',
           'litfl', 'webpathology', 'ultrasoundcases', 'pocus')
# Connecteurs logiques français (contrôle "phrase verbale + connecteur")
CONNECT = re.compile(r"\b(car|donc|or|ainsi|puis|alors|parce que|puisque|lorsque|quand|si|tandis que|"
                     r"alors que|afin de|afin que|pour que|de sorte que|c'est pourquoi|en effet|cependant|"
                     r"toutefois|néanmoins|par conséquent|dès lors|ensuite|enfin|d'abord|aussi|"
                     r"en revanche|ce qui|ce qui explique|via|grâce à|à cause de|en raison de|"
                     r"conduisant à|entraînant|provoquant|signant|orientant)\b", re.I)
# Heuristique verbe conjugué (FR) : auxiliaires/verbes fréquents + terminaisons 3e pers.
VERB = re.compile(r"\b(est|sont|a|ont|fait|font|peut|peuvent|doit|doivent|reste|restent|devient|"
                  r"deviennent|signe|signent|oriente|orientent|impose|imposent|confirme|confirment|"
                  r"élimine|éliminent|traite|traitent|associe|associent|survient|surviennent|"
                  r"provoque|provoquent|entraîne|entraînent|exige|exigent|reçoit|reçoivent|"
                  r"\w+(?:e|ent|it|ient|ait|aient|era|eront|ra|ront))\b", re.I)
TAG_RE = re.compile(r'<(script|style)[^>]*>.*?</\1>', re.S | re.I)
STRIP_RE = re.compile(r'<[^>]+>')
HEAD_RE = re.compile(r'<h([1-4])[^>]*>(.*?)</h\1>', re.S | re.I)
MD_HEAD = re.compile(r'^(#{1,4})\s+(.+)$', re.M)


def walk(root):
    for d, ds, fs in os.walk(root):
        ds[:] = [x for x in ds if x not in SKIP_DIRS]
        for f in fs:
            yield os.path.join(d, f)


def read(p, cap=2_000_000):
    try:
        with open(p, 'rb') as fh:
            return fh.read(cap).decode('utf-8', 'ignore')
    except Exception:
        return ''


def html_text(s):
    s = TAG_RE.sub(' ', s)
    return html.unescape(re.sub(r'\s+', ' ', STRIP_RE.sub(' ', s))).strip()


def qualite(text):
    """Escouade QUALITÉ : phrases, % avec verbe conjugué, % avec connecteur, longueur moyenne."""
    sents = [x.strip() for x in re.split(r'(?<=[.!?;])\s+|\s•\s|\n', text) if len(x.strip()) > 25]
    if not sents:
        return {'n': 0}
    v = sum(1 for x in sents if VERB.search(x))
    c = sum(1 for x in sents if CONNECT.search(x))
    return {'n': len(sents), 'verbe%': round(100 * v / len(sents)), 'connect%': round(100 * c / len(sents)),
            'mots_moy': round(sum(len(x.split()) for x in sents) / len(sents), 1)}


def analyse_fichier(p):
    """Unité de travail d'un soldat : un fichier → fiche compacte."""
    ext = os.path.splitext(p)[1].lower()
    try:
        size = os.path.getsize(p)
    except OSError:
        size = 0
    r = {'p': p, 'ext': ext, 'o': size}
    if ext not in TXT_EXT or size > 3_000_000:
        return r
    s = read(p)
    urls = URL_RE.findall(s)
    if urls:
        doms = collections.Counter(re.sub(r'^https?://(www\.)?', '', u).split('/')[0].lower() for u in urls)
        r['urls'] = len(urls)
        r['dom'] = dict(doms.most_common(8))
        r['swiss'] = sum(n for d, n in doms.items() if any(k in d for k in SWISS))
        r['imgdom'] = sum(n for d, n in doms.items() if any(k in d for k in IMG_DOM))
    if ext == '.md' and re.search(r'PROMPT|SKILL|AGENTS|CLAUDE|HARNAIS|SPEC|CONTINU|REPRISE|PASSATION|LIRE|BRACELET', os.path.basename(p), re.I):
        r['plan'] = [('#' * len(h)) + ' ' + t.strip()[:90] for h, t in MD_HEAD.findall(s)][:80]
    if ext == '.html' and re.search(r'DX\.\d+|Phase_A|chap|cours', os.path.basename(p), re.I):
        r['h'] = [f'h{l} ' + html_text(t)[:70] for l, t in HEAD_RE.findall(s)][:40]
        r['img'] = len(re.findall(r'<img\b|<svg\b', s, re.I))
        r['modal'] = len(re.findall(r'modal|dialog', s, re.I))
        r['src'] = len(re.findall(r'<a\s[^>]*href=["\']https?://', s, re.I))
        t = html_text(s)
        r['txt_o'] = len(t.encode())
        r['q'] = qualite(t)
    return r


def escouade_git(root):
    """Branches actives (dates) + LOTs présents sur les branches sans checkout (git ls-tree)."""
    out = {}
    try:
        refs = subprocess.run(['git', '-C', root, 'for-each-ref', '--sort=-committerdate',
                               '--format=%(committerdate:short)|%(refname:short)|%(subject)', 'refs/remotes'],
                              capture_output=True, text=True, timeout=60).stdout.splitlines()
        out['branches_total'] = len(refs)
        out['branches_recentes'] = refs[:15]
        prod = collections.Counter(r.split('|')[1].split('/')[1] if '/' in r.split('|')[1] else '?' for r in refs)
        out['prefixes'] = dict(prod.most_common(10))
        lots_branches = collections.defaultdict(set)
        for r in refs:
            m = LOT_RE.search(r.split('|')[1].replace('-', '_'))
            if m:
                lots_branches[int(m.group(1))].add(r.split('|')[1])
        out['lots_en_branche'] = sorted(lots_branches)
    except Exception as e:
        out['err'] = str(e)
    return out


def synthese(root, fiches):
    S = {'depot': os.path.basename(root)}
    S['fichiers'] = len(fiches)
    S['octets'] = sum(f['o'] for f in fiches)
    S['ext'] = dict(collections.Counter(f['ext'] for f in fiches).most_common(10))
    top = collections.Counter()
    for f in fiches:
        top[os.path.relpath(f['p'], root).split(os.sep)[0]] += f['o']
    S['top_dirs_Mo'] = {k: round(v / 1e6, 1) for k, v in top.most_common(15)}
    # LOTs
    lots = collections.defaultdict(lambda: {'dx': set(), 'A': 0, 'o': 0, 'img': 0, 'fig': 0, 'lieu': set(), 'q': []})
    for f in fiches:
        rel = os.path.relpath(f['p'], root)
        m = LOT_RE.search(rel)
        if not m or 'audit' in rel.split(os.sep)[0]:
            continue
        L = lots[int(m.group(1))]
        L['lieu'].add(rel.split(os.sep)[0])
        if f['ext'] == '.html':
            dm = DX_RE.search(rel)
            if dm:
                L['dx'].add(int(dm.group(1)))
            if 'Phase_A' in rel:
                L['A'] = 1
            L['o'] += f['o']
            L['img'] += f.get('img', 0)
            if f.get('q', {}).get('n'):
                L['q'].append(f['q'])
        if f['ext'] in ('.png', '.jpg', '.jpeg', '.webp', '.svg', '.gif'):
            L['fig'] += 1
    S['lots'] = {}
    for k in sorted(lots):
        L = lots[k]
        q = L['q']
        S['lots'][k] = {'dx': len(L['dx']), 'A': L['A'], 'Ko': round(L['o'] / 1024), 'img_html': L['img'],
                        'fig': L['fig'], 'lieu': sorted(L['lieu']),
                        'verbe%': round(sum(x['verbe%'] for x in q) / len(q)) if q else None,
                        'connect%': round(sum(x['connect%'] for x in q) / len(q)) if q else None}
    # Prompts
    S['prompts'] = sorted(({'f': os.path.relpath(f['p'], root), 'Ko': round(f['o'] / 1024, 1),
                            'plan': f['plan'][:25]} for f in fiches if f.get('plan')),
                          key=lambda x: -x['Ko'])[:25]
    # Liens
    L = [f for f in fiches if f.get('urls')]
    S['fichiers_liens'] = sorted(({'f': os.path.relpath(f['p'], root), 'urls': f['urls'], 'swiss': f['swiss'],
                                   'img': f['imgdom'], 'dom': f['dom']} for f in L
                                  if not os.path.relpath(f['p'], root).startswith(('audit', 'audits'))),
                                 key=lambda x: (-x['swiss'], -x['urls']))[:20]
    dom = collections.Counter()
    for f in L:
        dom.update(f['dom'])
    S['domaines_top'] = dict(dom.most_common(25))
    # Gabarit HTML dominant (titres h2 les plus fréquents)
    h = collections.Counter()
    for f in fiches:
        for t in f.get('h', []):
            if t.startswith(('h2', 'h3')):
                h[re.sub(r'\d+', '#', t)] += 1
    S['gabarit_titres'] = h.most_common(30)
    qs = [f['q'] for f in fiches if f.get('q', {}).get('n')]
    if qs:
        S['qualite_globale'] = {'docs': len(qs), 'verbe%': round(sum(x['verbe%'] for x in qs) / len(qs)),
                                'connect%': round(sum(x['connect%'] for x in qs) / len(qs)),
                                'mots_moy': round(sum(x['mots_moy'] for x in qs) / len(qs), 1)}
    return S


def md(digests):
    o = ['# LÉGION — digest\n']
    for S in digests:
        o.append(f"## {S['depot']} — {S['fichiers']} fichiers, {round(S['octets']/1e6)} Mo")
        o.append('ext ' + json.dumps(S['ext'], ensure_ascii=False))
        o.append('dirs Mo ' + json.dumps(S['top_dirs_Mo'], ensure_ascii=False))
        g = S.get('git', {})
        o.append(f"git: {g.get('branches_total')} branches; préfixes {g.get('prefixes')}; LOTs en branche {g.get('lots_en_branche')}")
        o += ['  ' + b for b in g.get('branches_recentes', [])[:8]]
        if S['lots']:
            o.append('### LOTs (n: dx|A|Ko|img|fig|verbe%|connect%|lieu)')
            o.append('; '.join(f"{k}:{v['dx']}|{v['A']}|{v['Ko']}|{v['img_html']}|{v['fig']}|{v['verbe%']}|{v['connect%']}|{','.join(v['lieu'])[:18]}"
                               for k, v in S['lots'].items()))
        o.append('### Qualité globale ' + json.dumps(S.get('qualite_globale'), ensure_ascii=False))
        o.append('### Gabarit titres h2/h3 (fréq)')
        o.append('; '.join(f'{t}×{n}' for t, n in S['gabarit_titres'][:25]))
        o.append('### Prompts (Ko) + plan')
        for p in S['prompts'][:15]:
            o.append(f"- {p['f']} ({p['Ko']}) :: " + ' | '.join(p['plan'][:14]))
        o.append('### Fichiers de liens (urls/suisses/imagerie)')
        for f in S['fichiers_liens'][:12]:
            o.append(f"- {f['f']} {f['urls']}/{f['swiss']}/{f['img']} {list(f['dom'])[:5]}")
        o.append('domaines ' + json.dumps(S['domaines_top'], ensure_ascii=False))
        o.append('')
    return '\n'.join(o)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('roots', nargs='+')
    ap.add_argument('--out', default='.')
    ap.add_argument('--workers', type=int, default=os.cpu_count())
    a = ap.parse_args()
    digests = []
    with ProcessPoolExecutor(a.workers) as ex:
        for root in a.roots:
            files = list(walk(root))
            fiches = list(ex.map(analyse_fichier, files, chunksize=64))
            S = synthese(root, fiches)
            S['git'] = escouade_git(root)
            digests.append(S)
    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, 'legion_digest.json'), 'w') as fh:
        json.dump(digests, fh, ensure_ascii=False, indent=1, default=list)
    m = md(digests)
    with open(os.path.join(a.out, 'legion_digest.md'), 'w') as fh:
        fh.write(m)
    print(f'OK {len(m.encode())} octets digest')


if __name__ == '__main__':
    main()
````

## D. Commandes (une commande par bloc, avec son but)

D-1 (dresser l'état de tous les LOTs et des branches actives, sans modèle) :
```bash
python3 outils/mere.py . --jours 30 --soldats 16
```

D-2 (construire le paquet de preuves d'un DX à partir des registres de Vial et de l'AIPS) :
```bash
python3 outils/paquet.py --entite "Ascite de l'hypertension portale" --sortie "lot en cours de production/LOT_166/DX.1/paquet.json" --registres tools/prevalences/sources_reconnues.json data/ck/src.json data/ck/doses_ch.json --textes "lot en cours de production/LOT_166/evidence/"*.txt --aips ../Medina/AipsDownload_20261008.zip --ham ../Medina/docs/collaboration/references/medicaments-suisses-vial-2026-10-11/zugelassene_packungen_ham.xlsx --dci spironolact furosemid
```

D-3 (rédiger les 14 points en une passe avec le modèle local) :
```bash
python3 outils/rediger.py --gabarit outils/P-POINT.txt --paquet "lot en cours de production/LOT_166/DX.1/paquet.json" --contrat "lot en cours de production/LOT_166/DX.1/contrat.json" --sortie "lot en cours de production/LOT_166/DX.1/fragments" --moteur local --modele "$MODELE_LOCAL"
```

D-4 (collecter les images candidates et produire la planche) :
```bash
python3 outils/images.py --lot "lot en cours de production/LOT_166" --besoins "lot en cours de production/LOT_166/images/besoins.json" --budget 60
```

D-5 (assembler le HTML final avec les figures inspectées) :
```bash
python3 outils/assembler.py --fragments "lot en cours de production/LOT_166/DX.1/fragments" --paquet "lot en cours de production/LOT_166/DX.1/paquet.json" --contrat "lot en cours de production/LOT_166/DX.1/contrat.json" --titre "DX.1 — Ascite de l'hypertension portale" --sortie "lot en cours de production/LOT_166/LOT_166_Phase_B_V0_DX.1.html" --figures "lot en cours de production/LOT_166/images/figures.json" --integrer-images
```

D-6 (contrôler les trois axes des 11 fichiers du LOT ; code 1 si un fichier est ROUGE) :
```bash
python3 outils/controle3.py "lot en cours de production/LOT_166/"LOT_166_Phase_*.html --paquet "lot en cours de production/LOT_166/DX.1/paquet.json" > "lot en cours de production/LOT_166/controle.json"
```

D-7 (appliquer une correction chirurgicale A-5 par remplacement exact) :
```bash
python3 -c "import json,sys;f=sys.argv[1];h=open(f).read();[h:=h.replace(c['avant'],c['apres']) if h.count(c['avant'])==1 else sys.exit('introuvable: '+c['avant'][:60]) for c in json.load(open(sys.argv[2]))];open(f,'w').write(h)" FICHIER.html corrections.json
```

D-8 (trier tous les LOTs existants par verdict avant toute nouvelle rédaction) :
```bash
for d in LOT_Claude_Finaux/LOT_* grok-LOTS-html/LOT_*; do python3 outils/controle3.py "$d"/*.html > "$d/controle.json"; echo "$d $?"; done
```

---
*PROMPT LOTS — version Lo_9.11.26.claude — organigramme-examen-federal — 9 novembre 2026, Europe/Zurich. Ce prompt est l'unité de vérité de la production : il s'applique dès qu'il est remis.*
