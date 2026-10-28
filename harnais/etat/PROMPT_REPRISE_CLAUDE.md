# PROMPT CLAUDE — orchestrateur du projet des fiches Flash (28.10.2026)

## 1. Mission
Produire, pour Vial (médecin en spécialisation), les fiches de révision Flash des 248 SSP du catalogue suisse PROFILES 2023 (= 248 LOT ; liste et statuts : `harnais/etat/LOTS_248_DD.md`, 75 faits, 173 à faire). Dépôt `vialdjoukang-spec/organigramme-examen-federal`, branche `claude/blissful-edison-1vq7na`. Réponses courtes, en français, livrable d'abord.

## 2. Ordres de Vial (non négociables)
- La production des cours prime ; les audits viennent après le 248e LOT. Professeurs, auditeurs et agents Opus sont **suspendus** (`.cache/brain/sans_professeur`).
- Aucun agent ne doit refuser un travail légitime : un refus est détecté, consigné, puis relancé une fois avec le contexte. Jamais de refus sec : refus notifié + correction, et le fichier progresse.
- Souplesse : un défaut sans conséquence pour l'apprentissage est un avertissement.
- **Volume (ordre du 28.10, nuit) : 80 à 150 Ko pour les cours en cours et futurs ; au-delà de 150 Ko, le cours ne passe pas : détruire davantage de superflu. Les cours déjà faits ne sont pas retouchés.** Vial relira bientôt des cours partie par partie pour juger de leur allure.
- Agir vite : on retouche l'existant plutôt que de repartir de zéro.

## 3. Fiche Flash (le produit)
- C'est une fiche de lecture : loi de Pareto, 20 % d'information utile pour 80 % du résultat ; le reste est du bruit et est retiré. Du mécanisme vers la clinique, puis vers le traitement qui s'en déduit.
- Phrases complètes (sujet, verbe conjugué, complément), registre universitaire soutenu, termes dédiés, une idée par phrase, aucune redite.
- Mise en page : îlots à bordure, texte justifié ; points 1-2-3-4 dans un même îlot, 5-6 dans un autre, le reste replié ; page aérée, jamais saturée.
- Fenêtres : vraies fenêtres modales, mots interactifs partout ; symptômes et signes d'examen cliquables (comment les rechercher) ; syndrome en tableau à 2 colonnes symptôme | signes physiques ; détails d'algorithme en fenêtres.
- Prise en charge : titre gras, bande colorée, souligné ; 1- But ; 2- Moyens et méthodes : A. Urgences (non-spécialiste, puis service spécialisé), B. Hors urgences (mesures générales, puis spécifiques par priorité). Algorithme en cases, traits horizontaux et verticaux uniquement.
- Références : `harnais/etat/COURS_FLASH.md`, gabarit `harnais/brain/gabarit_flash.html`.

## 4. Volume
**80 à 150 Ko** par cours (en cours et futurs) ; **> 150 Ko : refusé** (V1 bloquant), il faut élaguer encore (redites, détails secondaires, notions voisines). Cible de rédaction ≈ 100 Ko. Mesure : `python3 harnais/brain/mesure_ko.py`. Le lanceur parallèle fait jusqu'à 2 passes de dégraissage par Sonnet si le cours dépasse 150 Ko. Toujours vérifier que le fond reste exact après toute coupe. Les cours déjà rédigés (LOT_001 : 16, LOT_002 : 9) gardent leur version actuelle.

## 5. Vérité médicale
Doses : AIPS suisse seulement (jamais le Compendium) ; jamais de chiffre ni de dose inventés ; source suisse d'abord pour le local (recommandations, filières), non suisse admise pour l'universel ; source lue et datée, sinon « À vérifier ». Grille des 14 points + Prompt universel (annexe).

## 6. Circuit et outils
- Lanceur parallèle : `harnais/brain/lancer_parallele.py` (un agent Sonnet 5.5 par fragment de point, 240 s ; assemblage ; mise en forme par l'agent `assembleur-mise-en-forme` ; porte unique ; reprise `--reprendre`).
- Capacité Sonnet réglable à chaud : `.cache/brain/sonnet_max` (48). Surveiller la charge (4 cœurs).
- Relance idempotente : `bash harnais/brain/relance_tout.sh`. État : `python3 harnais/brain/radar.py`. Suivi par leçon : `python3 harnais/brain/suivi_html.py`.
- Hygiène : `macrophage.py` (détruit seulement ce que le signal nomme, jamais une zone utile), `detective.py` (nouveaux fichiers).
- Le conteneur redémarre souvent : tout est enregistré leçon par leçon (`journal/*.fait.json`).

## 7. État à la pause (28.10.2026, ~23:05 UTC)
LOT_001 : 16/16 leçons rédigées (`essai_lot001/`) ; LOT_002 : 9/16 ; LOT_003 : 0/14 ; LOT_004 : 0/12. Rien promu dans `LOT_Claude_Finaux`. Le fichier AIPS doit être dans `.cache/aips/AipsDownload_20261008.xml` (le redemander à Vial si le conteneur est neuf).

## 8. Reprendre, dans l'ordre
1. `python3 harnais/brain/radar.py`. 2. `bash harnais/brain/relance_tout.sh`. 3. Veille de 15 min par `send_later` tant que des agents tournent. 4. Republier l'état des lieux (https://claude.ai/artifact/2xqRY3GJsgpLBFhXM2VR6S) et le suivi par leçon (https://claude.ai/artifact/KAujan5Hb5tTh7xPWLMbTk) à chaque étape. 5. Étendre au LOT 005 puis aux suivants.

## 9. Livrables à Vial
3 captures du LOT_001 (îlots, fenêtre ouverte, tableau de syndrome, algorithme) et le tableau .md des fautes restantes ; faute critique, grave ou moyenne marquée et localisée (registre JSON) ; une seule tentative de correction, puis tableau à Vial pour recours externe. Puis PR (draft) et fusion par commit de fusion après CI verte.

## 10. Règles du dépôt
Ne jamais modifier `/workspace/ssp/app.html`. Aucune donnée personnelle dans ce dépôt public. Ne commiter dans `LOT_Claude_Finaux` que si la porte et le pré-commit passent, jamais en les contournant. Commits terminés par « Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com> » et « Claude-Session: https://claude.ai/code/session_01QZK4dvwhmDEnsTae9bMPTq ».

## 11. Questions ouvertes pour Vial
Volume exact (100–150 ou 100–200 Ko) ; sens du message coupé « Les Lots avec… » ; coût (~5 $ par leçon mesuré, de l'ordre de 20 000 $ pour 248 LOT) et rythme acceptable.

---

# ANNEXE — LA GRILLE DES 14 POINTS (texte intégral, inchangé depuis le premier jour : `harnais/GRILLE_14_POINTS.md`)

Valeur de vérité 1 de l'audit médical. Éditée par Vial le 26.10.2026 à partir du Prompt ULTIME V0 (§11, §12, §14.4). Source unique : `harnais/grille14/gen.py`.

> **Principe de chaque point : CONCIS + DENSE + EXHAUSTIF : concision absolue, densité maximale, aucune information utile perdue, aucun bavardage.**

## Règles générales

- **Règle de forme** : Titre de chaque point en gras (<strong>), sous-titres en italique (7.1, 9.a, 11.B…). Aucun point ne manque. Aucun point n'est mal affecté.
- **La présence ne vaut pas la conformité** : Quatorze numéros présents ne prouvent rien. Chaque point contient son contenu (pas celui d'un autre) et réussit ses questions d'obsession.
- **Procédure** : Après chaque point rédigé, on relit et on répond honnêtement aux questions. Une seule réponse « non » impose de réécrire le point avant de passer au suivant.
- **Question finale** : « Vial peut-il gagner 90 à 100 % des points et traiter ce patient en sécurité ? »
- **Format FLASH** : Cours concis, très denses, utiles seulement. Pas de bavardage. Le texte est le cours : ni méthode, ni date de rédaction, ni genèse des sources dans le texte. Les sources sont en dernière page, sous un mot cliquable ; dans le texte, un numéro entre crochets en exposant affiche la source sur une petite bande de fond bleu ciel. Les cours extensifs vont dans Médina.
- **Mots cliquables** : Chaque terme technique, signe, examen, médicament, score ou article de loi ouvre une fenêtre (définition brève) ou un déroulé (contenu plus long). Jamais dans les titres du plan. Une fenêtre ne coupe jamais une phrase.

## Les 14 points : ce qui est attendu et les questions à se poser avant de passer au point suivant

### 1. Définition et sémantique

**Exigence.** Définition claire et exacte, tirée d'une source fiable (selon la source disponible : société savante médicale ou outil de classification : CIM, etc.). Niveau sémantique : information à contextualiser.

**Questions :**
- Q1.1 La définition est-elle précise ?
- Q1.2 Est-elle détaillée sur l'essentiel tout en restant concise (1 à 4 phrases ; la richesse dans les fenêtres) ?
- Q1.3 Le lecteur distingue-t-il clairement l'entité de ses notions voisines ?

**Amendement (Vial).** Situer l'entité du général au particulier, avec entre parenthèses la classification d'origine (CIM-11, DSM-5, ATC…).

### 2. Épidémiologie (Suisse, puis Europe)

**Exigence.** Prévalence et/ou incidence selon ce qui est disponible. Source prioritaire : Suisse (OFS, OFSP, registres, Obsan) ; Europe si le chiffre suisse manque. Âge, sexe, groupes à risque, géographie, mortalité. Enjeux de santé publique (coût, dépistage, gravité). Badge de fréquence uniquement s'il est sourcé.

**Questions :**
- Q2.1 Le candidat peut-il décrire la distribution dans la population (prévalence, incidence, âge, sexe, groupes à risque, géographie suisse) ?
- Q2.2 Les enjeux (santé publique, coût, gravité, dépistage) sont-ils donnés et compris ?
- Q2.3 Les chiffres utiles, et seulement eux, sont-ils sourcés et datés ?

**Amendement (Vial).** Les sources sont en fin de page ; un numéro entre crochets en exposant affiche la source sur une petite bande de fond bleu ciel.

### 3. Physiopathologie

**Exigence.** Cascade moléculaire → cellulaire → tissulaire → clinique, de la cause au signe, étape par étape (amorce, développement, installation, maintien). Lien explicite entre chaque lésion ou perte fonctionnelle et la classe médicamenteuse ou la stratégie qui la corrige. Tableau de corrélation obligatoire : lésion / perturbation → exploration qui la montre → thérapeutique qui la corrige (mécanisme).

**Questions :**
- Q3.1 L'amorce, le développement, l'installation et le maintien sont-ils compréhensibles étape par étape ?
- Q3.2 Les mécanismes expliquent-ils les complications et le pronostic ?
- Q3.3 Chaque lésion ou perte fonctionnelle est-elle reliée à la classe médicamenteuse ou stratégie qui la corrige, avec son mécanisme ?
- Q3.4 Un tableau de corrélation rend-il ce lien évident ?
- Q3.5 Tout cela reste-t-il concis ?

### 4. Démarche diagnostique

**Exigence.** Se référer toujours au titre : donner les étapes à suivre, graduellement, jusqu'au diagnostic. (1) S'assurer de l'absence de drapeaux rouges : les citer. Chaque drapeau rouge existant est cliquable ; sa fenêtre explique, de façon directe, concise et précise, pourquoi c'est un drapeau rouge. (2) En l'absence d'urgence ou de drapeau rouge : préciser, étape par étape, les grandes étapes qui mènent au diagnostic. Les détails viennent dans les points suivants.

**Questions :**
- Q4.1 Les drapeaux rouges sont-ils cités, expliqués et associés aux diagnostics ?
- Q4.2 Chaque DD dangereux a-t-il son signe ou examen qui tranche et son piège ?

### 5. Anamnèse ciblée et drapeaux rouges

**Exigence.** Questions clés, chacune justifiée par sa raison physiopathologique (pourquoi cette question change la décision). Principe du mot interactif cliquable, qui ouvre la fenêtre explicative. Chronologie, facteurs déclenchants, comorbidités, médicaments, contexte suisse pertinent. Drapeaux rouges actionnables : ce qu'ils imposent tout de suite (urgence, imagerie, avis spécialisé), pas une liste décorative.

**Questions :**
- Q5.1 Chaque question clé porte-t-elle sa raison physiopathologique ?
- Q5.2 Les drapeaux rouges imposant l'urgence sont-ils complets et actionnables ?

### 6. Examen physique ciblé, région par région

**Exigence.** Donner les étapes d'un examen physique ciblé, en progression topographique, systémique ou topo-systémique. Exemple : Région 1 → signe 1, signe 2… ; Région 2 → signe 1, signe 2… signe n. Chaque signe est cliquable et sa fenêtre explique de façon concise : la technique précise du geste (comment faire, où poser les mains, quel seuil), la valeur diagnostique (sensibilité / spécificité qualitatives si connues) et le piège d'interprétation.

**Questions :**
- Q6.1 Le normal est-il présenté avant le pathologique ?
- Q6.2 Chaque signe a-t-il sa technique de recherche et sa valeur diagnostique ?

### 7. Approche syndromique (7.1, 7.2…)

**Exigence.** Syndromes numérotés : 7.1, 7.2, 7.3… 7.n. Chaque syndrome est éclaté en signes fonctionnels et signes physiques, chacun défini. Pour chaque signe : geste de recherche concret et mécanisme physiopathologique. Pas de syndrome nommé sans contenu exploitable au lit du malade.

**Questions :**
- Q7.1 Les syndromes sont-ils énumérés (7.1, 7.2…) ?
- Q7.2 Chaque syndrome est-il éclaté en signes fonctionnels d'un côté et signes physiques de l'autre ?
- Q7.3 Chaque signe est-il défini (fenêtre) ?
- Q7.4 Est-il dit comment rechercher chaque signe physique (geste, position, manœuvre, résultat normal et pathologique) ?
- Q7.5 Chaque signe est-il relié à son mécanisme ?

### 8. Diagnostic positif et critères

**Exigence.** Critères de la société savante avec année : majeurs / mineurs, seuils chiffrés, durée minimale, exclusions. Ce qui suffit au diagnostic et ce qui ne suffit pas (piège d'examen). Scores ou classifications (stades, grades) avec leur usage clinique immédiat.

**Questions :**
- Q8.1 Le lecteur sait-il quels critères posent le diagnostic avec certitude (majeurs, mineurs, seuils) ?
- Q8.2 Sait-il ce qui ne suffit pas à poser le diagnostic ?

### 9. Examens complémentaires

**Exigence.** Structure obligatoire : 9.a gold standard (si existant) ; 9.b 1re intention ; 9.c alternatives ; 9.d 2e intention. Pour chaque examen : indication, ce qu'on prescrit exactement, tableau d'interprétation (résultat → signification → conduite). Contre-indications et limites utiles au candidat.

**Questions :**
- Q9.1 Est-il dit si un gold standard existe ? Nommé en premier avec sensibilité, spécificité, seuil ; s'il est clinique, c'est écrit.
- Q9.2 Sinon, les examens de 1re et 2e intention sont-ils donnés, avec le critère de passage ?
- Q9.3 Le lecteur peut-il prescrire chaque examen comme le demande la société savante (indication, moment, préparation) ?
- Q9.4 Peut-il l'interpréter grâce au tableau normal (SI suisses) | seuil | signification | conduite ?
- Q9.5 Les cas de figure (positif, négatif, limite, discordant) sont-ils traités ?
- Q9.6 Les alternatives (grossesse, enfant, DFGe < 30 mL/min, allergie aux produits iodés, dispositif non compatible IRM) sont-elles données ?

### 10. Arbre décisionnel

**Exigence.** [À COMPLÉTER PAR VIAL : le texte saisi est « Devant le SSP : symptôme, etc. ». Texte du Prompt V0 conservé en attendant : embranchements explicites « si X → Y », lisibles en une lecture ; commence par l'exclusion des graves, puis discrimine les fréquents ; chaque nœud renvoie à un signe, un examen ou une action concrète.]

**Questions :**
- Q10.1 Chaque embranchement indique-t-il quel signe ou résultat mène à quelle décision ?

### 11. Prise en charge selon les recommandations suisses

**Exigence.** 11.A But thérapeutique (ce qu'on vise, horizons de temps). 11.B Moyens, de façon chronologique : d'abord la situation d'urgence, avec précision chronologique (1, 2, 3…) ; puis, hors urgence, le traitement dans l'ordre : 1 mesures générales, 2 pharmacologique, 3 non pharmacologique… n. Ordre du traitement ; pharmacologie complète avec AIPS suisse (spécialité ®, dose, voie) ; non pharmacologique ; situations spéciales (grossesse, insuffisances, âges extrêmes). 11.C Surveillance (quoi, fréquence, seuils d'alerte). 11.D Pronostic, critères de guérison / sortie, pistes de recherche 2026 si pertinentes et sourcées.

**Questions :**
- Q11.1 Le but du traitement est-il chiffré ?
- Q11.2 Le lecteur sait-il dans quel ordre procéder et pourquoi ?
- Q11.3 Formes compliquées : conduite d'urgence et prise en charge chronologique pour chaque complication ?
- Q11.4 Formes non compliquées : mesures générales initiales et pourquoi ; puis ordre des étapes et pourquoi ?
- Q11.5 Médicaments : pour chaque molécule, classe, autres principes actifs de la classe, pharmacocinétique et pharmacodynamie utiles, effets indésirables dont informer le patient, spécialité suisse ®, dose AIPS, durée, contre-indications, interactions majeures ?
- Q11.6 Non médicamenteux : mesures physiques, nutrition, rééducation, psychothérapie, chirurgie, dispositifs ?
- Q11.7 Social et professionnel : arrêt de travail, assurances (LAMal, LAA, LAI), conduite, soutien, réinsertion ?
- Q11.8 Situations spéciales : femme enceinte et allaitante (texte AIPS non adouci), sujet âgé, enfant, insuffisant hépatique, insuffisant rénal (paliers de DFGe) ?
- Q11.9 Surveillance : quoi, quand, pourquoi, seuils d'arrêt pour toxicité ?
- Q11.10 Sortie d'hospitalisation : critères de retour à domicile un par un ?
- Q11.11 Pronostic et guérison : critères de guérison ou état de la recherche 2026 ?

**Amendement (Vial).** Fenêtre du médicament : DCI + marque, classe (ATC), groupe pharmacologique avec ses chefs de file, indications et posologies lues dans l'AIPS.

### 12. Prévention

**Exigence.** Primaire, secondaire et tertiaire, chacune avec recommandation suisse (organisme, année) quand elle existe. Gestes concrets (vaccination, dépistage, éducation, réadaptation), populations cibles et seuils d'intervention. Lien clair avec le risque épidémiologique du point 2.

**Questions :**
- Q12.1 Les trois niveaux sont-ils traités avec les recommandations suisses (vaccinations, dépistages, mesures), avec substance et pas seulement des titres ?

### 13. Points clés

**Exigence.** Trois à six phrases courtes, verbales, intactes, mémorisables la veille de l'examen. Chaque phrase porte une décision clinique ou un fait critique (pas de slogan vague). Aucune fenêtre qui coupe la phrase porteuse.

**Questions :**
- Q13.1 Les 3 à 6 phrases suffisent-elles à résumer ce qu'un médecin ne doit jamais oublier, et chaque phrase est-elle intacte (non coupée par une fenêtre) ?

### 14. Pièges et questions fréquentes à l'examen fédéral suisse

**Exigence.** Chaque piège est formulé comme une question d'examen, suivi immédiatement de la bonne réponse et, si utile, de la raison courte. Couvrir les confusions de doses, de critères, de gravité et de conduite. Rien d'inventé : calé sur le fond des points 1 à 13.

**Questions :**
- Q14.1 Les pièges réels de l'examen fédéral (confusions classiques, seuils, contre-indications) sont-ils donnés, chacun avec sa bonne réponse ?

## Style des cours

- **Phrases** : Zéro phrase nominale : chaque phrase porte un verbe conjugué. Phrases simples, courtes, une idée chacune. Pas de nuance qui complique. Pas de listes télégraphiques.
- **Concision** : Chaque point tient en 1 à 4 phrases courtes et denses ; la richesse vit dans les fenêtres et les tableaux. Zéro répétition, remplissage, méta-commentaire ou métaphore.
- **Précision** : Chaque abréviation est développée à sa première apparition. Chaque valeur porte son chiffre, son unité SI et son seuil suisse (ex. natrémie < 135 mmol/L). Le normal avant le pathologique. Virgule décimale, typographie française.
- **Fenêtres et mots cliquables** : Chaque terme technique, signe, examen, médicament, score ou article de loi ouvre une fenêtre ou un déroulé. Jamais dans les titres du plan. Une fenêtre ne coupe jamais une phrase.
- **Police et tableaux** : Police Atkinson Hyperlegible. Gros tableaux colorés, données utiles organisées et aérées.

## Audit médical : deux valeurs de vérité

- **Valeur de vérité 1 : conformité à la grille** : Chaque question de la grille reçoit 2 (pleinement satisfaite), 1 (partiellement) ou 0 (absente ou fausse), ou « sans objet » avec raison écrite. Score de la monographie = somme obtenue ÷ somme maximale. Calculé par l'auditeur, jamais par le rédacteur.
- **Valeur de vérité 2 : véracité des affirmations** : Doses = texte AIPS suisse lu. Chiffres retrouvés dans leur source ouverte. Références existantes (PMID). Rien d'inventé : sinon « À vérifier » ou « non quantifié ».
- **Décision** : Un audit médical est fait lorsque les informations sont vraies (V2) ET que le contenu de chaque point respecte la grille (V1). Validé : score ≥ 90 %, zéro critique, question finale « oui ». Cible 95 à 100 %. Un seul fichier sous le seuil bloque le LOT.

## Notation (Prompt §12.2)

| Résultat | Décision |
|---|---|
| ≥ 95 %, zéro critique, question finale « oui » | Cible atteinte : validé |
| 90 à 94 %, zéro critique, question finale « oui » | Validé ; les questions à 1 sont listées pour amélioration |
| < 90 %, ou ≥ 1 critique, ou question finale « non » | Refusé : retour au rédacteur avec la liste des questions à 0 ou 1 |

## Décisions et points en attente

- Point 11 : le numéro Swissmedic n'est plus exigé (parfois introuvable). Retrait voulu par Vial. Un numéro n'est écrit que s'il est lu dans l'AIPS, jamais déduit.
- Point 2 : « histoire naturelle » retirée de l'exigence ; Q2.2 d'origine supprimée et questions renumérotées (Q2.1 à Q2.3). Décision validée.
- Point 8 : Q8.2 (« sait-il ce qui ne suffit pas ? ») rétablie, car l'exigence garde « ce qui ne suffit pas ». Décision validée.
- Point 10 (arbre décisionnel) : texte du Prompt V0 conservé jusqu'à ce que Vial fournisse sa version complète. Décision validée.
- Audit V1 (note de la grille) : un auditeur Opus par territoire, sur le texte final. Décision validée.
- Taille des fichiers FLASH : bande indicative 80–200 Ko (Vial, 27.10.2026), jamais bloquante : simple avertissement.
