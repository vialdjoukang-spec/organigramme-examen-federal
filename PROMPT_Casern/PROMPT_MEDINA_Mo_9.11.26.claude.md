# PROMPT MEDINA — USINE DE CHAPITRES (version Mo_9.11.26.claude)

> **Statut.** Ce prompt réunit en une unité de vérité `CHAPTER_SPEC.md`, `PROMPT_MEDINA.md` (et ses consignes datées), `PROMPT_TRANSITION.md`, les ordres de Vial des 7 au 15 octobre 2026 (sémiologie par leçon, figures anatomiques, sources suisses), le catalogue d'imagerie du 2 novembre 2026 et la méthode de production économique validée pour les LOTs. Il conserve le contrat technique de MEDINA (gabarit I50, classes, fenêtres, glossaire, Pareto, construction) et en remplace l'organisation.
> **Lecture.** On lit d'abord la partie MACRO (*quoi*), puis MICRO (*comment*), puis MÉTA (*contrôle et coût*). Les annexes contiennent les prompts instanciables et les outils exécutables. Chaque phrase est une injonction.
> **Priorité.** Un ordre écrit de Vial, consigné dans le dépôt, prime pour la durée et le périmètre qu'il nomme. Les consignes datées qui s'empilent en tête d'`AGENTS.md` et de `CLAUDE.md` restent des archives ; ce prompt en reprend le fond.

---

## SOMMAIRE

- **MACRO** — M1 Mission · M2 Lois de vérité · M3 Lexique · M4 Unité structurelle : le chapitre · M5 Chaîne de production · M6 Rôles et routage
- **MICRO** — µ1 Onglet Alpha (îlots 0 à 11) · µ2 Onglet Examens · µ3 Onglet Sciences · µ4 Onglet Pharmacologie · µ5 Sémiologie obligatoire · µ6 Fenêtres, mots verts, quiz, Pareto · µ7 Glossaire et abréviations · µ8 Figures et imagerie · µ9 Langue
- **MÉTA** — Θ1 Contrôle des trois axes · Θ2 Portes · Θ3 Audit ciblé et grille /20 · Θ4 Économie · Θ5 Anti-collision · Θ6 Traçabilité · Θ7 Erreurs déjà commises · Θ8 Stratégie d'achèvement
- **ANNEXES** — A Prompts instanciables · B Contrats · C Outils exécutables · D Commandes

---

# PARTIE MACRO — CE QUE L'ON CONSTRUIT

## M1. Mission

1. MEDINA est un atlas de cours de médecine organisé par systèmes, publié sur GitHub Pages, pour les médecins assistants qui préparent l'examen fédéral suisse.
2. Un chapitre couvre une pathologie (code CIM-10-GM 2024, avec ses rattachements) et doit obtenir **20/20** à l'audit : il permet de répondre juste à l'examen et de soigner sans danger.
3. **Question finale** : « Ce chapitre, lu avec ses fenêtres, permet-il de reconnaître, d'explorer, de traiter et de surveiller cette pathologie en Suisse sans erreur, et de gagner tous les points d'examen sur elle ? » Si la réponse est « non », le chapitre ne passe pas la porte.
4. **Ordre de décision : Qualité → Exhaustivité du fond → Économie → Esthétique.** On économise sur la forme, jamais sur le fond.

## M2. Lois de vérité (bloquantes)

| N° | Loi | Conséquence |
|---|---|---|
| LV1 | **Ponction, pas mémoire.** Chaque fait vient d'un extrait lu, identifié et daté du paquet du chapitre. | Le rédacteur ne reçoit que le paquet. |
| LV2 | **Fond identique, forme MEDINA.** On reformule dans le lexique et le style MEDINA ; le sens, les seuils, les doses et les conditions restent ceux de l'extrait. | `controle3.py` compare chaque nombre avec l'extrait cité. |
| LV3 | **Nombres recopiés**, jamais arrondis. | Un nombre absent de l'extrait donne un verdict ROUGE. |
| LV4 | **Une phrase factuelle, une citation** au format `<sup class="r"><a href="#sb-ID">ID</a></sup>`. Au rendu, la section `src` regroupe les extraits cités. | Une phrase chiffrée sans citation donne un verdict ORANGE. |
| LV5 | **La Suisse, puis l'Europe.** On consulte d'abord OFSP, OFS, Obsan, Sentinella, Swissmedic, Fedlex, ASSM, FMH et les sociétés suisses (SSC, SSMIG, SSED, SSGO, SSI, SGN, Swiss Nephrology, SSP…), puis ESC, ERS, EASL, ESH, ESMO, ESCMID, EULAR, KDIGO et EMA. Une source exclusivement américaine ne sert jamais de référence ; un cas illustratif étranger ne devient pas une recommandation suisse. | Le registre `dist/MEDINA_SOURCES.json` (1 989 URL, dont 1 770 suisses) sert de liste de priorité. |
| LV6 | **Médicaments : AIPS d'abord.** L'information professionnelle Swissmedic (`AipsDownload_20261008.zip` à la racine du dépôt, puis swissmedicinfo.ch) prime ; compendium.ch ne sert qu'au contrôle croisé, comme le prévoit `CHAPTER_SPEC`. La disponibilité suisse se vérifie avec les listes officielles (`docs/collaboration/references/LIENS_OFFICIELS_MEDICAMENTS_SUISSES_VIAL_2026-10-11.json` : HAM Swissmedic et Liste des spécialités de l'OFSP). | Le corpus AIPS est un index (numéro → URL française) ; la liste HAM (`zugelassene_packungen_ham.xlsx`) traduit la DCI en numéros ; `paquet.py --aips --ham --dci` rapatrie et découpe le texte. Une phrase de dose qui ne cite pas d'extrait `aips-*` donne un verdict ROUGE. On n'adoucit jamais le texte relatif à la grossesse. |
| LV7 | **Affirmatif.** Le chapitre énonce ce que les sources établissent. Il ne contient aucune formule de chantier (« à vérifier », « donnée non disponible »). Une donnée non vérifiable s'attribue à la dernière version vérifiée (par exemple « selon l'ESC 2023 ») ; sinon, elle sort du cours et part dans `HELP.md`. | — |
| LV8 | **Version la plus récente** : on vérifie les recommandations en vigueur à la date de rédaction (ESC août 2026, notamment). | L'année figure dans l'ID de l'extrait. |
| LV9 | **Honnêteté des actes** : on ne déclare jamais une construction, un test, une revue ou une publication qui n'a pas eu lieu. Les états `self_review`, revue distincte et revue de Vial restent séparés. | Chaque statut renvoie à une sortie d'outil. |

## M3. Lexique MEDINA (nos termes)

| Terme | Sens |
|---|---|
| **Fragment** | Discipline ou système de la nosologie (S01 Cardiovasculaire … T7 Éthique), découpé en catégories. |
| **Catégorie** | Groupe de codes CIM-10-GM rattaché à un ou plusieurs chapitres. |
| **Chapitre** | Unité structurelle : une pathologie, quatre onglets et ses fenêtres, rangés dans `chapters/<CODE>/`. |
| **Onglet** | `pA` Pathologie et prise en charge (temps Alpha) ; `pE` Examens ; `pS` Sciences ; `pP` Pharmacologie (temps Betta). |
| **Îlot** | `section.ilot` autonome qui se lit seul ; c'est l'unité de vérification. |
| **Mot vert** | `<button class="w" data-k="clé">libellé (destination)</button>`, qui ouvre une fenêtre. |
| **Fenêtre** | `<template data-pop="clé" data-title="Titre">…</template>`, rangée dans `<CODE>_popN.html`. |
| **Pareto** | Résumé minimal (environ 20 % du texte) qui couvre 100 % des notions utiles d'une grande partie ; son ratio est calculé automatiquement. |
| **Paquet** | `paquet.json` : extraits sourcés et datés du chapitre, avec les IDs proposés par îlot. |
| **Contrat** | `contrat.json` : liste des îlots, octets visés, squelette et sémiologie exigée. |
| **Légion** | Scripts clones (`mere.py`, `soldat.py`) qui rendent l'état des 281 branches dans un `DIGEST.md`. |
| **Planche** | Page qui regroupe les images candidates pour un seul contrôle visuel. |
| **Courtier d'images** | `tools/image_codex_finder.py serve` (127.0.0.1:8765) : cache et budget partagés de la machine. |

## M4. Unité structurelle — le chapitre

```text
chapters/<CODE>/
├── <CODE>_a.html   ← <template id="ch-<CODE>"><div class="chap"> + en-tête + 4 onglets + début de pA (îlots 0 à 6)
├── <CODE>_b.html   ← suite de pA (îlots 7 à 11) + section src
├── <CODE>_c.html   ← pE (Examens) + pS (Sciences)
├── <CODE>_d.html   ← pP (Pharmacologie), qui ferme par </div></template>
├── <CODE>_pop1.html … _popN.html   ← fenêtres <template data-pop>
└── <CODE>_justifications.json      ← lien entre chaque îlot et les IDs d'extraits (provenance)
glossary/<code>.py  ← nouvelles abréviations, développées lettre par lettre
chapters.json       ← déclaration {"code","covers":[…],"integrated","title"}
```

- **Modèle de forme : I50 Insuffisance cardiaque** (8 fichiers, 176 Ko). On imite sa forme sans cloner aucune phrase.
- **Budget d'un chapitre : 180 à 450 Ko pour les huit à dix fichiers.** Au-delà de 600 Ko (A41 pèse 1,1 Mo), on condense la forme en fenêtres, sans couper le fond. L'unité de budget est l'îlot (table µ1).
- **Classes autorisées (liste fermée) :** `ilot toc chap-body sci-body sci sci-bar key trap k alert two card t pareto-btn src pager prev next quiz fb status chap-head code n ui w ratio chap lab panel tabs`. Le script de construction les convertit en `mc-…`.
- **Préfixes :** îlots `<code>-<n>`, `<code>-e-<n>`, `<code>-p-<n>` ; sciences `<code>-s-anat` ; nouvelles clés de fenêtre `<code>-…`. Une clé de I50 non préfixée peut être réutilisée sans modification, à condition que son contenu convienne exactement.

## M5. Chaîne de production (un seul passage)

| Étape | Action | Exécutant | Coût | Sortie |
|---|---|---|---|---|
| E0 | Légion : état des chapitres, des branches et des réservations | `mere.py` | 0 | `DIGEST.md` |
| E1 | Réservation de la mission (registre de session) et de la branche `chapitre/<CODE>` | scripts du harness | 0 | registre |
| E2 | Paquet : registres de Vial, cache, AIPS, sources sémiologiques | `paquet.py` | 0 | `paquet.json` |
| E3 | Contrat : îlots retenus, octets, squelettes, sémiologie exigée | modèle fort (A-2), puis gel | faible | `contrat.json` |
| E4 | Rédaction îlot par îlot, en une passe | modèle local ou peu coûteux (A-1) | très faible | `fragments/` |
| E5 | Fenêtres, glossaire et quiz | modèle local (A-3) + `glossaire` | très faible | `_popN.html`, `glossary/<code>.py` |
| E6 | Figures : courtier, catalogue, planche, inspection | `image_clo_finder.py`, `images.py`, puis un contrôle visuel | 0, puis faible | `figures.json` |
| E7 | Assemblage dans les fichiers `_a` à `_d` | `assembler_medina` (D-6) | 0 | chapitre |
| E8 | Contrôles : `build_medina.py`, `test_preview.py`, `controle_medina.py`, `controle3.py` | scripts | 0 | rapports |
| E9 | Audit ciblé, puis correction chirurgicale | IA d'audit (A-4), puis IA de rédaction (A-5) | faible | `audits/` |
| E10 | Porte P4, PR, CI, publication vérifiée | scripts + CI | 0 | `main` + Pages |

**Un seul passage.** Un fragment reçu n'est jamais resoumis au modèle. La correction ne vise que les phrases désignées. Un fichier dont le SHA-256 n'a pas changé n'est pas relu.

## M6. Rôles et routage

> **Posture.** Ce prompt ne nomme aucune IA. Chaque IA qui le reçoit prend la posture que l'étape lui assigne (IA de rédaction, IA de haut niveau de raisonnement, IA d'audit, IA à capacité visuelle) et s'y tient ; c'est la posture, et non le nom de l'IA, qui fixe le niveau exigé.

| Tâche | Exécutant |
|---|---|
| Construction, aperçu, clés et fenêtres, classes, préfixes, Pareto, abréviations, nombres contre extraits, doublons, tailles | **Scripts** |
| Collecte, cache, AIPS, recherche d'images, planche | **Scripts**, avec le courtier et son budget |
| Rédaction d'un îlot, d'une fenêtre, d'un quiz | **IA de rédaction** : modèle local ou peu coûteux |
| Contrat du chapitre (îlots, hiérarchie des différentiels, stratégie pharmacologique) | **IA de haut niveau de raisonnement** |
| Audit médical ciblé ; inspection de la planche | **IA d'audit indépendante** ; **IA à capacité visuelle** pour la planche |

> **Indépendance.** L'auditeur n'a jamais rédigé le chapitre qu'il juge. L'escalade vers un modèle plus fort suit un échec constaté, jamais une précaution.

---

# PARTIE MICRO — COMMENT ON CONSTRUIT

## µ1. Onglet Alpha (`pA`) — îlots 0 à 11

Chaque îlot se lit seul. L'octet visé couvre le texte de l'îlot ; ses fenêtres sont comptées à part.

| Îlot | Contenu exigé | Encadrés et éléments | Octets visés |
|---|---|---|---|
| 0 | Question clinique d'ouverture et objectifs vérifiables (« à la fin, vous savez… ») | `card` | 1 500 |
| 1 | Définition et classifications : société savante, version, année ; ce qui entre dans l'entité et ce qui n'y entre pas | `key`, mots verts | 4 000 |
| 2 | Épidémiologie : données suisses datées (OFS, Obsan, Sentinella), puis européennes ; facteurs de risque ; mortalité | `table.t` si ≥ 3 chiffres | 4 000 |
| 3 | Physiopathologie : chaîne normal → perturbation → manifestation, un mot vert à chaque charnière ; schéma noir et blanc légendé si utile | `key` (corrélation clinique), figure | 8 000 |
| 4 | Étiologies et facteurs de risque, hiérarchisés par fréquence | `table.t` | 4 000 |
| 5 | Anamnèse : antécédents cliquables ; symptômes par fréquence, chacun avec caractérisation et physiopathologie en fenêtre ; formes typiques et atypiques en cartes `two` | `two`, `card`, mots verts | 7 000 |
| 6 | Examen clinique : état général → paramètres vitaux → anthropométrie → signes ciblés, en deux colonnes ; chaque signe cliquable (technique, valeur, piège) | `two`, `trap` | 7 000 |
| 7 | Diagnostic : critères officiels datés ; algorithme ; diagnostics différentiels hiérarchisés par gravité | `table.t`, figure d'algorithme | 6 000 |
| 8 | Urgences et complications, **gravité d'abord** | `alert` | 4 000 |
| 9 | Prise en charge hiérarchisée : objectifs → moyens → choix justifiés → surveillance → critères de modification | `key`, `table.t` | 8 000 |
| 10 | Suivi, pronostic et prévention (primaire, secondaire, tertiaire, avec la recommandation suisse) | — | 4 000 |
| 11 | Situations particulières : grossesse, sujet âgé, insuffisance rénale ou hépatique ; cas récapitulatif | `card`, quiz | 5 000 |
| src | Références principales datées, limitées aux extraits cités | `src` | auto |

On ajoute les îlots propres à la pathologie et on supprime ceux qui ne s'appliquent pas, en écrivant la raison dans `contrat.json`. Chaque grande partie volumineuse se termine par un bouton Pareto.

## µ2. Onglet Examens (`pE`)

1. **Hiérarchie** : question clinique → examen → statut (indiqué, conditionnel, non systématique), avec la raison du statut.
2. **Gold standard nommé**, ou mention qu'il est clinique, avec sa sensibilité et sa spécificité citées.
3. **Fiches d'interprétation** : valeurs normales (unités SI, population), seuils pathologiques, lésions élémentaires, pièges et erreurs fréquentes.
4. **Tableau diagnostics × associations biologiques** quand plusieurs configurations existent.
5. **Au moins trois quiz** de cas cliniques, chacun avec une explication verbale citée.
6. **Cliché de référence** de la modalité décisive, issu du courtier ou de Commons, inspecté et attribué (µ8).

## µ3. Onglet Sciences (`pS`)

- La barre d'icônes (`sci-bar`) propose Anatomie, Histologie, Physiologie et Biochimie, plus la Génétique ou la Pharmacologie fondamentale si elles sont pertinentes. Les libellés ne contiennent aucune abréviation.
- Chaque science reçoit un îlot (`<code>-s-anat`…), au moins une figure sourcée et une **corrélation clinique explicite** dans un encadré `key`, qui relie le fait fondamental au signe ou à la décision de l'onglet Alpha.
- **Anatomie** : on utilise un original existant et sourcé (Gray, Commons, OpenStax). Un schéma anatomique dessiné par une IA, SVG compris, est irrecevable (ordre de Vial du 15 octobre 2026).

## µ4. Onglet Pharmacologie (`pP`)

Cet onglet présente une stratégie propre à la pathologie, jamais une liste générique :
1. classification des classes utiles ;
2. place de chaque classe selon le phénotype ou le stade ;
3. **tableau des doses** (initiale, cible, maximale), chaque dose citée d'un extrait AIPS ;
4. interactions dangereuses dans un encadré `alert` ;
5. surveillance et gestion des effets indésirables ;
6. médicaments à éviter, avec leur raison ;
7. monographies en fenêtres : mécanisme, preuves (essais nommés, année), posologie AIPS, effets indésirables, contre-indications, surveillance, grossesse et allaitement (texte AIPS non adouci), spécialité ® et numéro Swissmedic.

## µ5. Sémiologie obligatoire par leçon (ordre de Vial du 15 octobre 2026)

- Chaque symptôme et chaque signe cité dans les îlots 5 et 6 ouvre une fenêtre sémiologique qui contient sa **définition**, sa **technique de recherche** (position, geste, normal attendu), son **mécanisme** physiopathologique, sa **valeur diagnostique** (sensibilité et spécificité citées) et son **piège**.
- Les sources sémiologiques se rangent dans `prep/sources_semiologie.json`, sur le modèle des missions ALPHA77, et entrent dans le paquet.
- Le contrôle `check-semiology-contract.py` du harness reste la porte de ce contrat.

## µ6. Fenêtres, mots verts, quiz et Pareto

- **Mot vert** : `<button class="w" data-k="<code>-clé">libellé (contenu de la fenêtre)</button>`. Le libellé annonce la destination entre parenthèses, et chaque clé possède son `<template data-pop>`.
- **Fenêtre** : `<template data-pop="<code>-clé" data-title="Titre">…</template>`. Elle contient un mécanisme pas à pas, un exemple chiffré cité, un tableau s'il clarifie, le piège et la citation. Les fenêtres peuvent s'imbriquer.
- **Quiz** : `<div class="quiz ui"><p>énoncé</p><button data-ok="1">…</button><button data-ok="0">…</button><p class="fb" hidden>explication citée</p></div>`.
- **Pareto** : `<button class="pareto-btn ui" data-k="pareto-<code>-xxx">▲ Loi de Pareto — titre sans abréviation</button>`. Son template commence par `<p class="ratio" data-cover="id1,id2"></p>`, suivi d'une `<ul>` contractée dont chaque item reste une phrase verbale.
- **Aide mnémotechnique** : elle va en fenêtre, avec la mention « aide pédagogique, non critère officiel ».
- **Rubriques** : « Piège » (`trap`) et « Erreur fréquente » partout où elles existent.

## µ7. Glossaire et abréviations (règle absolue)

1. Avant de rédiger, on liste les clés existantes (D-4). Une abréviation déjà présente est réutilisée.
2. Chaque abréviation nouvelle s'inscrit dans `glossary/<code>.py` : `a('SCA',[('S','Syndrome'),('C','Coronarien'),('A','Aigu')],'Syndrome coronarien aigu','<p>Définition riche en 1 à 3 phrases verbales.</p>','clé_fenêtre_optionnelle')`.
3. On écrit en toutes lettres ce qui n'a pas besoin d'abréviation : « par voie intraveineuse », « /jour », « angiotensine II ».
4. Les symboles d'unités (mg, mL, mmHg, mmol/L) ne sont pas des abréviations. Les onglets, les boutons Pareto et la barre des sciences n'en contiennent aucune.
5. La construction doit afficher `<CODE> non couvertes: 0` ; `controle_medina.py` signale de plus les sigles en majuscules absents du glossaire.

## µ8. Figures et imagerie

**Ressources de Vial (catalogue du 2 novembre 2026, `harness/resources/imaging_catalog.json`)** : Radiopaedia, Radiology Assistant, Ultrasound Cases, Learning Radiology, Eurorad (ESR), Case Stacks, Rad At Hand, Casimage (UNIGE), RadioSurf (UniBE) et Modern Radiology (e-book de l'ESR). Ce catalogue est un **index de recherche** : il fournit des liens de cas, pas des images réutilisables.

**Chaîne :**
1. On part du besoin de l'îlot : modalité, région, normalité ou signe à montrer. On cherche d'abord dans le catalogue, puis par le courtier.
2. Pour les originaux libres, le coordinateur lance `image_codex_finder.py serve` une fois, avec un budget de 60 requêtes. Chaque agent appelle ensuite `image_clo_finder.py candidates "<requête anglaise précise>" --broker http://127.0.0.1:8765`, ou `images.py` (Commons et Europe PMC) qui lit la licence de **chaque fichier**.
3. On ouvre le **cas exact** et on consigne son URL, son auteur, sa date ou version, les passages lus et la date de lecture. Une page d'accueil ne suffit pas.
4. **Droits de la figure précise** : on vérifie l'auteur, le titulaire, la licence et les conditions de redistribution et d'annotation. Un accès gratuit ne vaut pas autorisation. Sans droit établi, on donne un lien vers le cas, sans copie.
5. **Une inspection visuelle par chapitre** (prompt A-6, sur la planche) vérifie la modalité, le plan, la latéralité, les repères, la cohérence de la légende et l'absence d'identifiant personnel. Elle ne déduit de l'image aucun diagnostic qu'elle ne démontre pas.
6. On conserve le fichier source, son SHA-256 et l'attribution ; l'annotation française se superpose sans modifier l'original. `publication_ready` reste `false` jusqu'à la revue humaine.
7. On contrôle l'aperçu sur ordinateur et sur mobile, ainsi que les crédits et les liens.

## µ9. Langue MEDINA

1. **Phrase verbale** partout, y compris dans les tableaux, les fenêtres, les quiz et les Pareto.
2. **Connecteur logique** dans chaque paragraphe de plus de 40 mots ; il relie une cause et un effet, un signe et une décision, ou une règle et son exception (*car, donc, ainsi, en effet, dès lors, par conséquent, cependant, en revanche, d'abord, ensuite, lorsque, ce qui, d'où*).
3. Une idée par paragraphe, des phrases de 12 à 28 mots, et un exemple pour chaque concept, expliqué comme si le lecteur le découvrait.
4. Le texte ne contient **aucune métaphore, aucune comparaison imagée, aucun jeu de mots et aucun remplissage**. Il ne remplace jamais un cours par une liste de mots-clés.
5. On présente le normal avant le pathologique et le grave avant le fréquent, en unités SI, avec la virgule décimale et la typographie française.

**Exemple de ponction**
> Extrait `esc2026-hf-12` : « Loop diuretics are recommended in patients with HF with signs and/or symptoms of congestion (class I, level C). »
> ✅ « Les diurétiques de l'anse sont recommandés lorsque des signes de congestion apparaissent, car ils diminuent la volémie et donc les pressions de remplissage ; l'ESC leur attribue une classe I, de niveau C<sup class="r"><a href="#sb-esc2026-hf-12">esc2026-hf-12</a></sup>. »

---

# PARTIE MÉTA — CONTRÔLE ET COÛT

## Θ1. Contrôle natif des trois axes

| Axe | Outil | Défaut bloquant (ROUGE) | Défaut à corriger (ORANGE) |
|---|---|---|---|
| **A. Véracité** | `controle3.py --points 0 --script-ok --min 0 --max 600000` sur chaque fichier `_a` à `_d` et `_pop` | nombre absent de l'extrait ; citation inconnue ; dose sans extrait AIPS | chiffre sans citation |
| **B. Phrase verbale et connecteur** | `controle3.py` | phrase partagée avec un autre chapitre (clonage) | phrase nominale, longue ou dupliquée ; paragraphe sans connecteur |
| **C. Contrat MEDINA** | `controle_medina.py`, `build_medina.py`, `test_preview.py`, `check-semiology-contract.py` | clé sans fenêtre ; ouverture ou fermeture du template absente ; panneau manquant ; ID Pareto inconnu ; SVG anatomique sans source ; `non couvertes > 0` ; erreur JavaScript | classe hors liste ; abréviation hors glossaire ; figure sans attribution ; métaphore ; moins de 3 quiz |

**Cibles.** Un chapitre doit atteindre `connecteur% ≥ 35`, `paragraphes_sans_connecteur = 0`, `A_* = 0`, `non couvertes: 0`, un aperçu `OK` et des verdicts VERT.
*Calibrage réel du 9 novembre 2026 : I50, A41 et G45 sont ORANGE (abréviations hors glossaire détectées : ADVOR, AF, AHF ; DR, IL, PAI ; AA, AIT, CA3). E04 n'existe sur `main` que comme déclaration, sans fichiers.*

**Limites.** La détection du verbe est heuristique. Le contrôle des nombres prouve leur présence dans l'extrait, pas l'exactitude de leur contexte. L'audit Θ3 reste donc obligatoire sur les îlots 7, 8 et 9 et sur l'onglet Pharmacologie.

## Θ2. Portes

| Porte | Moment | Condition | Qui |
|---|---|---|---|
| P0 | Avant la rédaction | Mission réservée ; aucune branche active sur ce code (légion) ; branche basée sur `main` | Scripts |
| P1 | Contrat | `contrat.json` audité : îlots, hiérarchie des différentiels, stratégie pharmacologique ; puis gel | IA d'audit |
| P2 | Chapitre assemblé | Θ1 sans aucun ROUGE ; construction et aperçu OK | Scripts |
| P3 | Chapitre | Audit A-4 ≥ 18/20 (cible 20/20), zéro critique, question finale « oui » | IA d'audit |
| P4 | Publication | CI verte sur le SHA final ; Pages vérifiées octet par octet ; `chapters.json` déclaré | Scripts + CI |

## Θ3. Audit ciblé et grille /20

**Ce que reçoit l'auditeur :** les rapports Θ1 (au plus 4 Ko), les phrases signalées avec leurs extraits, les îlots 7, 8 et 9, l'onglet `pP` et le contrat. Il ne reçoit jamais le chapitre entier.

| Critère | Points | Question de l'auditeur |
|---|---|---|
| Exactitude et actualité | 4 | Chaque seuil, critère et dose correspond-il à l'extrait le plus récent ? Les recommandations sont-elles suisses d'abord ? |
| Complétude | 3 | Les îlots 0 à 11 et les trois onglets Betta sont-ils remplis de leur propre contenu ? |
| Pédagogie | 3 | Chaque concept est-il expliqué avec un exemple, dans un ordre intelligible ? |
| Corrélations vertes | 2 | Chaque charnière physiopathologique ouvre-t-elle un mot vert qui relie le fait à la clinique ? |
| Sciences fondamentales et figures | 2 | Chaque science a-t-elle sa figure sourcée et sa corrélation `key` ? |
| Examens | 2 | Le gold standard, l'interprétation et les trois quiz sont-ils présents ? |
| Pharmacologie spécifique | 1 | La stratégie est-elle propre au phénotype, avec les doses AIPS ? |
| Pareto | 1 | Chaque Pareto couvre-t-il 100 % des notions avec environ 20 % du texte ? |
| Langue et anti-clonage | 1 | Le texte est-il verbal, connecté, sans métaphore ni phrase clonée ? |
| Interface | 1 | Les onglets, fenêtres et la lecture mobile fonctionnent-ils ? |

Une dose, une voie ou une contre-indication contraire à l'AIPS est **Critique** et bloque la publication. Le rapport `audits/<CODE>.audit.json` contient la note, la réponse finale et les corrections (gravité, îlot, phrase exacte, correction, ID de source).

## Θ4. Économie — bannir les pertes et les allers-retours

| Gaspillage constaté dans le dépôt | Règle |
|---|---|
| `AGENTS.md` (36 Ko) et `CLAUDE.md` (28 Ko) empilent des ordres datés, relus à chaque session | On lit ce prompt, l'unité de vérité ; les ordres datés restent des archives consultées seulement sur besoin précis. |
| 281 branches et des registres de transition de 230 Ko relus pour savoir où l'on en est | La légion fournit `DIGEST.md` ; on ne lit aucun registre JSON entier. |
| Des chapitres de plus de 1 Mo (A41) | Budget par îlot (µ1) ; les détails passent en fenêtres ; la mesure se fait par script. |
| Recherches web répétées par chaque auteur | Paquet construit d'abord par script, avec un cache disque ; douze recherches au plus par chapitre, toutes consignées. |
| Images cherchées une à une, avec un budget dispersé | Courtier unique, budget de 60 requêtes, puis une planche et une inspection. |
| Réécriture complète pour quelques erreurs | Correction chirurgicale A-5. |
| Contrôles techniques demandés à un modèle | `build_medina.py`, `test_preview.py`, `controle_medina.py` et `controle3.py` s'en chargent. |

**Paramètres de rédaction (modèle local).** On règle `temperature 0.2`, `repeat_penalty 1.1`, `num_ctx 8192` et `num_predict = 1,3 × octets_cible / 3,3`. Un échec réseau sans réponse autorise une seule nouvelle tentative.
**Bracelet.** Le cache est actif par défaut. On ajoute un routage local, puis peu coûteux, si une passerelle existe, et une compression seulement si un paquet dépasse le contexte. On charge un à trois outils par tâche.

## Θ5. Anti-collision

1. Une mission correspond à un chapitre, une branche et un dossier `chapters/<CODE>/`. La réservation passe par le registre de session du harness.
2. Avant d'écrire, on consulte `DIGEST.md`. Si une autre branche touche le même code, on s'arrête et le coordinateur arbitre.
3. Seul un rôle autorisé par une mission approuvée modifie `chapters/`. L'audit n'écrit que son rapport.
4. Une fenêtre existante d'un autre chapitre se réutilise sans modification ; sinon, on crée une clé préfixée.
5. On pousse après chaque îlot assemblé.

## Θ6. Traçabilité

- `<CODE>_justifications.json` relie chaque îlot aux IDs d'extraits utilisés.
- `JOURNAL.md` reçoit une ligne par décision ; `HELP.md` une entrée par lacune (code, îlot, question, URL déjà lues, date).
- Les rapports Θ1 et l'audit sont versionnés avec le SHA-256 du chapitre jugé.
- La provenance (`source-binding.json`) n'est jamais renouvelée artificiellement lors d'une simple vérification de liens.

## Θ7. Erreurs déjà commises, et la règle qui les empêche

| Erreur | Règle |
|---|---|
| Schéma anatomique dessiné par une IA, présenté comme figure de cours | µ3, µ8 ; `controle_medina.py` (SVG anatomique sans source) |
| Licence d'article prise pour la licence de la figure | µ8.4 |
| Abréviation laissée sans développement lettre par lettre | µ7 |
| Clé de fenêtre sans template, ou clé non préfixée qui entre en collision | M4 ; Θ1-C |
| Chapitre de plus de 1 Mo, illisible sur mobile | M4 ; µ1 |
| Correspondance PROFILES trop large (44 catégories sur 45 en pneumologie) | Θ8 : rattachement catégorie par catégorie |
| « Pathologie fréquente » sans source suisse de fréquence | M2-LV5 : OFS, Sentinella ou statistique médicale des hôpitaux |
| Inspection technique présentée comme une validation humaine | M2-LV9 |
| Métaphores et comparaisons imagées | µ9 ; Θ1-C |
| Formule de chantier (« à vérifier ») laissée dans un cours | M2-LV7 |

## Θ8. Stratégie d'achèvement (état collecté par la légion le 9 novembre 2026)

| Mesure | Valeur |
|---|---|
| Chapitres déclarés et intégrés (`chapters.json`) | **207** |
| Codes CIM couverts (`covers`) | 308 |
| Codes de la nosologie (`nosology/fragments/*.json`) | **1 634**, dont 227 couverts (≈ 14 %) |
| Branches distantes | 281 ; les plus récentes datent du 8 novembre 2026 (paquet NEO, navigation des références) |
| Missions ALPHA77 du 2 novembre 2026 | C73, E04, E30, E32, E35, E40, E42, D62, D63, D65, D77, G03, G06 à G09, G21, G22, G24, G25, G32, G36, N06, C92 |

**Ordre recommandé.**
1. **Consolider sans rédiger** : lancer Θ1 sur les 207 chapitres (D-8), puis trier VERT, ORANGE et ROUGE. Les ORANGE d'abréviations se corrigent par script, en complétant le glossaire avec A-3.
2. **Intégrer** les missions ALPHA77 restées sur des branches, après la porte P2.
3. **Produire par fragment**, selon `organisation/FILE_FRAGMENTS_CLAUDE.json` (G-04, E-06, H-08, G-10, M-12, R-14, O-17, O-18, M-19, E-22, puis les fragments restants en ordre inverse), les **pathologies fréquentes d'abord**, en vagues de dix chapitres avec dix paquets et dix rédactions locales en parallèle.
4. **Affiner** le rattachement PROFILES catégorie par catégorie, puis la jauge « Examen fédéral ».

L'état se recalcule chaque jour par `python3 mere.py <dépôt> --jours 30`.

---

# ANNEXES

## A. Prompts instanciables

### A-1. P-ILOT — rédaction d'un îlot en une passe

```text
Tu es rédacteur médical de MEDINA, de langue française. Tu rédiges une seule fois, et seulement l'îlot {N} — {TITRE_POINT}
du chapitre « {ENTITE} » ({CODE}), pour des médecins assistants qui préparent l'examen fédéral suisse.

CONTENU EXIGÉ
{CONTENU_EXIGE}

EXTRAITS — LES SEULES PREUVES AUTORISÉES
{PASSAGES}

FIDÉLITÉ
- Chaque phrase factuelle se termine par <sup class="r"><a href="#sb-ID">ID</a></sup>.
- Tu recopies chaque nombre tel qu'il est écrit dans l'extrait cité, sans jamais l'arrondir ; une dose exige un extrait aips-….
- Tu reformules en français médical soutenu ; le sens, les seuils et les conditions restent ceux de l'extrait.
- Tu n'écris aucune formule de chantier ; tu énonces ce que les extraits établissent.

LANGUE
- Chaque phrase porte un verbe conjugué et compte 12 à 28 mots ; chaque paragraphe contient un connecteur qui porte le raisonnement.
- Chaque concept est expliqué avec un exemple ; tu n'écris ni métaphore, ni comparaison imagée, ni remplissage, ni liste de mots-clés.

FORME (classes autorisées seulement : ilot key trap k alert two card t quiz fb w ui pareto-btn)
- Tu rends <section class="ilot" id="{PREFIX}-{N}"><h3>…</h3>…</section>.
- Mots verts : <button class="w" data-k="{PREFIX}-clé">libellé (destination)</button>, chaque clé étant listée à la fin dans <!-- CLES: … -->.
- Abréviations : tu ne les emploies que si elles existent dans {GLOSSAIRE}, sinon tu écris en toutes lettres.
- Budget : environ {OCTETS_CIBLE} octets ; tu t'arrêtes à la fin d'une phrase complète.
{SQUELETTE}
Renvoie seulement le fragment HTML.
```

### A-2. P-CONTRAT — plan du chapitre (modèle fort)

```text
À partir des seuls extraits {PASSAGES}, établis le contrat du chapitre « {ENTITE} » ({CODE}) :
1. îlots retenus de 0 à 11, plus les îlots propres à la pathologie ; ceux qu'on retire, avec leur raison ;
2. différentiels hiérarchisés par gravité, puis par fréquence, chacun cité ;
3. sémiologie exigée : symptômes et signes à ouvrir en fenêtre ;
4. examens : gold standard, première et deuxième intention, et besoins d'images (modalité, requête anglaise) ;
5. stratégie pharmacologique propre au phénotype (classes, place, molécules avec extrait AIPS) ;
6. octets visés par îlot (total du chapitre entre 180 et 450 Ko).
Sortie stricte : contrat.json (structure B-1).
```

### A-3. P-FENETRE — fenêtre, entrée de glossaire ou quiz

```text
Fenêtre « {NOTION} » ({PREFIX}-{CLE}) du chapitre {CODE}, à partir des seuls extraits {PASSAGES} :
- signe ou symptôme : définition, technique de recherche, mécanisme, valeur diagnostique citée, piège ;
- médicament : classe, mécanisme, essai princeps (année), posologie AIPS recopiée, effets indésirables, contre-indications,
  surveillance, grossesse et allaitement non adoucis, spécialité ® et numéro Swissmedic lu ;
- abréviation : ligne a('SIGLE',[('L','Lettre')…],'Forme développée','<p>Définition en 1 à 3 phrases verbales.</p>') ;
- quiz : <div class="quiz ui"><p>cas</p><button data-ok="1">…</button><button data-ok="0">…</button><p class="fb" hidden>explication citée</p></div>.
Sortie : <template data-pop="{PREFIX}-{CLE}" data-title="Titre">…</template>, une ligne a(…) ou un bloc quiz.
```

### A-4. P-AUDIT-CIBLE — IA d'audit indépendante

```text
Tu audites pour trouver l'erreur, pas pour valider.
Tu reçois : les rapports Θ1, les phrases signalées et leurs extraits, les îlots 7, 8 et 9, l'onglet pP et le contrat.
Tu rends :
{"code","sha256","note_20":{…critère:points…},"finale":"oui|non",
 "corrections":[{"gravite":"Critique|Grave|Moyen|Léger","ilot":"…","phrase":"…","correction":"…","source":"ID"}],"help":[…]}
Une dose contraire à l'AIPS est Critique. Un nombre qui diffère de l'extrait est Grave. Tu ne réécris pas le chapitre.
```

### A-5. P-CORRECTION — chirurgicale

```text
Remplace seulement les phrases listées par leur correction, sans toucher au HTML, aux citations ni aux clés environnantes.
Sortie : JSON [{"fichier":"…","avant":"…","apres":"…"}].
```

### A-6. P-PLANCHE — inspection visuelle unique

```text
Pour chaque image de la planche :
{"local","besoin","garder":true|false,"modalite","plan","lateralite","reperes_visibles":[…],"legende_fr":"phrase verbale",
 "identifiant_personnel":false,"origine_ia_suspectee":false,"motif_refus":""}
Tu ne déduis de l'image ni diagnostic, ni mesure, ni temporalité qu'elle ne démontre pas.
```

## B. Contrats

### B-1. `contrat.json` (chapitre)

```json
{"CODE":"K21","ENTITE":"Reflux gastro-œsophagien","PREFIX":"k21","GLOSSAIRE":"RGO, IPP, EOGD",
 "points":{
  "0":{"titre":"Question clinique et objectifs","octets":1500,"exige":"…"},
  "3":{"titre":"Physiopathologie","octets":8000,"exige":"…","squelette":"normal → perturbation → manifestation ; mots verts aux charnières"},
  "9":{"titre":"Prise en charge","octets":8000,"exige":"objectifs → moyens → choix → surveillance → modification"}},
 "semiologie":["pyrosis","régurgitation","dysphagie"],
 "images":[{"ilot":"pE","modalite":"endoscopie","requete":"reflux esophagitis endoscopy Los Angeles grade"}],
 "pharmaco":[{"classe":"inhibiteurs de la pompe à protons","molecules":["oméprazole","pantoprazole"],"aips":["…"]}]}
```

### B-2. `figures.json`

```json
[{"ilot":"pE","fichier":"images/9c2e….jpg","inspectee":true,"legende":"…phrase verbale…","attribution":"Auteur, CC BY 4.0, URL",
  "publication_ready":false}]
```

## C. Outils exécutables (Python ≥ 3.9, bibliothèque standard seule)

> Ces outils ont été testés sur le dépôt réel (correspondance DCI → HAM → index AIPS vérifiée sur le corpus du 8 octobre 2026 ; chapitres I50, A41, G45 et E04 ; preuves du LOT_166). `images.py` et le téléchargement de `paquet.py` exigent un réseau ouvert vers Wikimedia, Europe PMC et les sites sources ; ils n'ont pas été exécutés dans l'environnement de rédaction. Le courtier `tools/image_codex_finder.py` du dépôt reste prioritaire lorsqu'il tourne.

### C-1. `controle_medina.py` — contrat du chapitre

`controle_medina.py`
````python
#!/usr/bin/env python3
"""CONTROLE_MEDINA — contrat d'un chapitre MEDINA vérifié sans modèle (complète controle3.py).

Contrôles : classes de la liste fermée ; chaque data-k a son <template data-pop> ; nouvelles clés préfixées ;
Pareto data-cover → ids d'îlots existants ; ouverture <template id="ch-CODE"> et fermeture </div></template> ;
quatre panneaux pA/pE/pS/pP ; quiz ≥ 3 dans pE ; abréviations (MAJUSCULES ≥ 2 lettres) absentes du glossaire ;
figures : attribution + licence ; SVG anatomique sans source = MAJEUR ; métaphores signalées par lexique.

Usage : python3 controle_medina.py chapters/I50 --glossaire glossary [--reutilisables np,echo,irm]
"""
import os, re, sys, json, glob, argparse, importlib.util

CLASSES = set('ilot toc chap-body sci-body sci sci-bar key trap k alert two card t pareto-btn src pager prev next quiz fb '
              'status chap-head code n ui w ratio chap lab panel tabs'.split())
METAPHORES = re.compile(r"\b(tel(?:le)?s? (?:un|une) |comme (?:un|une) (?:chef|moteur|barrage|tsunami|bombe|cascade de dominos)|"
                        r"véritable|chef d'orchestre|clé de voûte|pierre angulaire|talon d'Achille|bombe à retardement)", re.I)
ANATOMIE = re.compile(r'(ventricule|oreillette|artère|veine|nerf|muscle|os |vertèbre|rein|néphron|foie|poumon|bronche|cerveau|cortex)', re.I)


def glossaire(d):
    """Lecture textuelle (sans exécuter les modules : rapide et sûr)."""
    G = set()
    for f in glob.glob(os.path.join(d or '', '*.py')):
        G |= set(re.findall(r"""\ba\(\s*['"]([^'"]+)['"]""", open(f, errors='ignore').read()))
    return G


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('dossier')
    ap.add_argument('--glossaire')
    ap.add_argument('--reutilisables', default='')
    a = ap.parse_args()
    code = os.path.basename(os.path.normpath(a.dossier))
    pre = code.lower()
    fichiers = sorted(glob.glob(os.path.join(a.dossier, f'{code}_*.html')))
    corps = ''.join(open(f, errors='ignore').read() for f in fichiers if '_pop' not in f)
    pops = ''.join(open(f, errors='ignore').read() for f in fichiers if '_pop' in f)
    tout = corps + pops
    d = {}
    cl = {c for v in re.findall(r'class="([^"]+)"', tout) for c in v.split()}
    d['classes_hors_liste'] = sorted(c for c in cl - CLASSES if not c.startswith('mc-'))
    cles = set(re.findall(r'data-k="([^"]+)"', tout))
    tpl = set(re.findall(r'<template data-pop="([^"]+)"', tout))
    reuse = set(filter(None, a.reutilisables.split(',')))
    d['cles_sans_template'] = sorted(cles - tpl - reuse)
    d['cles_non_prefixees'] = sorted(k for k in tpl if not k.startswith((pre + '-', 'pareto-' + pre)) and k not in reuse)
    ids = set(re.findall(r'<section class="ilot" id="([^"]+)"', tout))
    cov = {i for v in re.findall(r'data-cover="([^"]+)"', tout) for i in v.split(',')}
    d['pareto_ids_inconnus'] = sorted(cov - ids)
    d['ouverture'] = [] if f'<template id="ch-{code}">' in corps else [f'<template id="ch-{code}"> absent']
    d['fermeture'] = [] if re.search(r'</div>\s*</template>\s*$', open(fichiers[-1] if fichiers else os.devnull, errors='ignore').read() if fichiers else '') or any(
        re.search(r'</div>\s*</template>\s*$', open(f, errors='ignore').read()) for f in fichiers if f.endswith('_d.html')) else ['</div></template> final absent']
    d['panneaux_manquants'] = [p for p in ('pA', 'pE', 'pS', 'pP') if f'id="{p}"' not in corps and f"id='{p}'" not in corps]
    nq = len(re.findall(r'class="quiz', corps))
    d['quiz_insuffisants'] = [] if nq >= 3 else [f'{nq} quiz']
    G = glossaire(a.glossaire)
    if G:
        txt = re.sub(r'<[^>]+>', ' ', tout)
        ab = set(re.findall(r'\b[A-Z][A-Z0-9]{1,6}\b', txt)) - {'II', 'III', 'IV', 'VI', 'VII', 'VIII', 'IX', 'XI', 'XII', 'NB'}
        d['abreviations_hors_glossaire'] = sorted(ab - G)[:40]
    figs = re.findall(r'<figure\b.*?</figure>', tout, re.S)
    d['figures_sans_attribution'] = [f[:80] for f in figs if '<img' in f and not re.search(r'(CC[ -]BY|CC0|domaine public|public domain|licence)', f, re.I)]
    svgs = re.findall(r'<svg\b.*?</svg>', tout, re.S)
    d['svg_anatomique_sans_source'] = [s[:60] for s in svgs if ANATOMIE.search(s) and not re.search(r'source|licence|CC', s, re.I)]
    d['metaphores'] = list(dict.fromkeys(m.group(0) for m in METAPHORES.finditer(re.sub(r'<[^>]+>', ' ', tout))))[:10]
    d = {k: v for k, v in d.items() if v}
    majeur = {'cles_sans_template', 'ouverture', 'fermeture', 'panneaux_manquants', 'svg_anatomique_sans_source', 'pareto_ids_inconnus'}
    verdict = 'ROUGE' if majeur & set(d) else ('ORANGE' if d else 'VERT')
    print(json.dumps({'chapitre': code, 'fichiers': len(fichiers), 'octets': sum(os.path.getsize(f) for f in fichiers),
                      'verdict': verdict, 'defauts': d}, ensure_ascii=False, indent=1))
    sys.exit(1 if verdict == 'ROUGE' else 0)


if __name__ == '__main__':
    main()
````

### C-2. `controle3.py` — véracité, phrase verbale, connecteurs, forme

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

### C-3. `paquet.py` — paquet de preuves

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

### C-4. `rediger.py` — instanciation et appel en une passe

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

### C-5. `images.py` — collecteur d'images libres (si le courtier est absent)

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

### C-6. Légion — état du dépôt sans modèle

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

D-1 (dresser l'état des chapitres et des branches actives, sans modèle) :
```bash
python3 outils/mere.py . --jours 30 --soldats 16
```

D-2 (construire le paquet de preuves d'un chapitre à partir des registres de Vial et de l'AIPS) :
```bash
python3 outils/paquet.py --entite "Reflux gastro-œsophagien" --sortie chapters/K21/_travail/paquet.json --registres dist/MEDINA_SOURCES.json docs/collaboration/references/LIENS_OFFICIELS_MEDICAMENTS_SUISSES_VIAL_2026-10-11.json --telecharger chapters/K21/_travail/urls.txt --aips AipsDownload_20261008.zip --ham docs/collaboration/references/medicaments-suisses-vial-2026-10-11/zugelassene_packungen_ham.xlsx --dci omeprazol pantoprazol
```

D-3 (rédiger les îlots en une passe avec le modèle local) :
```bash
python3 outils/rediger.py --gabarit outils/P-ILOT.txt --paquet chapters/K21/_travail/paquet.json --contrat chapters/K21/_travail/contrat.json --points 0-11 --sortie chapters/K21/_travail/fragments --moteur local --modele "$MODELE_LOCAL"
```

D-4 (lister les abréviations déjà définies dans le glossaire) :
```bash
python3 -c "import re,glob;print(sorted({k for f in glob.glob('glossary/*.py') for k in re.findall(r'\ba\(\s*[\"\x27]([^\"\x27]+)', open(f).read())}))"
```

D-5 (lancer le courtier d'images commun avec un budget journalier) :
```bash
python3 tools/image_codex_finder.py --daily-budget 60 serve
```

D-6 (chercher les originaux libres d'une figure par le courtier) :
```bash
python3 tools/image_clo_finder.py candidates "reflux esophagitis endoscopy Los Angeles grade" --broker http://127.0.0.1:8765
```

D-7 (construire et tester le chapitre) :
```bash
python3 build_medina.py K21
```

D-8 (vérifier l'aperçu : fenêtres, onglets, absence d'erreur JavaScript) :
```bash
python3 test_preview.py K21
```

D-9 (contrôler le contrat MEDINA du chapitre) :
```bash
python3 outils/controle_medina.py chapters/K21 --glossaire glossary
```

D-10 (contrôler la véracité, la phrase verbale et les connecteurs du chapitre) :
```bash
python3 outils/controle3.py chapters/K21/K21_*.html --paquet chapters/K21/_travail/paquet.json --points 0 --script-ok --min 0 --max 600000
```

D-11 (trier les 207 chapitres par verdict avant toute nouvelle rédaction) :
```bash
for d in chapters/*/; do python3 outils/controle_medina.py "$d" --glossaire glossary > "${d}controle_medina.json"; echo "$d $?"; done
```

---
*PROMPT MEDINA — version Mo_9.11.26.claude — vialdjoukang-spec/Medina — 9 novembre 2026, Europe/Zurich. Ce prompt est l'unité de vérité de la production des chapitres : il s'applique dès qu'il est remis.*
