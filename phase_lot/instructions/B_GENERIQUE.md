# Contrat des rôles B — tous les LOTS

Ce contrat est technique. Le message d’assignation précise le LOT, le rôle, le dossier d’écriture et le dossier A terminé. La sélection de ce LOT est l’unique référence des noms et de l’ordre : B1 reçoit DX.1–2, B2 DX.3–4, B3 DX.5–6, B4 DX.7–8 et B5 DX.9–10. Les anciens fichiers B1.md à B5.md concernent le LOT1 et ne doivent pas fournir les noms d’un autre LOT.

## Règles communes

1. Lire AGENTS.md, MANDAT.md, le V7 intégral, rubric.json et la sélection A. Vérifier que la rédaction A est complète avant de commencer. La consigne humaine remplace la cadence historique et les auditeurs IA du V7.
2. Thunder est l’utilisateur humain vialdjoukang-spec, seul auditeur médical, des 14 parties et linguistique. Les auteurs ne lui attribuent aucune décision, note ou signature. Une auto-vérification rédactionnelle n’est pas cet audit.
3. Écrire exclusivement dans le dossier privé assigné. Ne modifier ni dépôt, ni application, ni ancien automate, ni état commun, ni autre auteur. Ne lancer aucun sous-agent, ne prendre aucun bail et ne créer aucune PR. Aucune transmission ou publication clinique sans validation humaine du livrable exact. Root importe les chemins réservés après contrôle.
4. Préserver les fichiers de recherche et les versions antérieures. Les paquets bruts restent dans internal/. Avant modification d’une pièce couverte par un manifeste de recherche, conserver sa copie et son manifeste dans internal/research_snapshot/. Les empreintes de rédaction sont distinctes des empreintes historiques.
5. Les sources sont suisses, puis européennes, puis internationales applicables en Suisse. Aucune donnée de mémoire, aucun numéro Swissmedic déduit d’une URL, aucune recommandation exclusivement américaine. Les données officielles locales prouvent identité/autorisation, pas posologie.
6. Toute dose, voie, adaptation et durée enseignée exige le passage professionnel AIPS approprié, avec spécialité, formulation, population et version exactes. Distinguer les recommandations de société de la notice ; une divergence ne permet pas de les fusionner. Vérifier aussi pharmacocinétique/pharmacodynamie utiles, contre-indications, interactions, grossesse/allaitement, toxicités et surveillance.
7. Un passage de table des matières n’est pas une preuve clinique. Pour une recommandation critique, localiser le corps, conserver le passage et sa provenance, vérifier sa portée et les versions. Un paquet reçu n’est pas une preuve de lecture intégrale.
8. Une preuve héritée peut être relue et utilisée dans sa portée réelle ; ne pas la présenter comme une nouvelle ouverture réseau. La réutilisation de preuves ne permet pas de recopier le cours d’un autre SSP.
9. Toute lacune reçoit un HELP précis : contexte, question, recherche déjà faite, source attendue et emplacement de réinjection. Une source inaccessible n’autorise aucune invention ni contournement. Les CLI refusées ne sont pas relancées avec une autre identité ; utiliser les MCP disponibles dans leur périmètre normal.
10. Sauvegarder un checkpoint horodaté après chaque étape substantielle, même incomplète. Distinguer recherche achevée, rédaction achevée, transmission et audit. Aucune case vide n’est une acceptation implicite.

## Invocation recherche high

Le modèle demandé est GPT-6.1 Sol, effort high. Il n’est pas changé à chaud. Le chercheur ne rédige pas le HTML final et ne lance pas l’invocation medium.

Lire les preuves A et, si utile, les preuves primaires déjà collectées pour une même maladie. Compléter les besoins propres aux deux monographies et les versions applicables, avec lectures ciblées et objectifs indépendants groupés. Ne pas refaire les sondes larges de liens dont le refus proxy est déjà documenté. Ne pas prétendre qu’une URL est fonctionnelle à partir d’une ancienne sonde.

Pour chaque diagnostic, préparer la matière des 14 points et les 51 questions exactes du rubric. Vérifier les critères diagnostiques, techniques d’examen et populations, explorations et interprétations, situations particulières, urgences, surveillance, critères de sortie et prévention. Ne pas transférer un seuil pédiatrique à l’adulte ni un agrégat statistique à un sous-type. Les calculs sont reproduits par outil et distingués des recommandations.

Livrer evidence.json, HELP.json, research_handoff.md, research_question_index.json et research_checkpoint.json. L’index comprend 102 entrées, 51 par diagnostic, avec identifiant, libellé exact, diagnostic, sources/passages et limites. Le checkpoint comporte le LOT entier, le rôle, l’invocation et l’effort demandés ; research_complete=true uniquement après passation vérifiée ; production_complete=false et writing_medium_executed=false. Fournir les empreintes. Les corps sources et scripts restent privés dans internal/.

## Invocation rédaction medium

Le modèle demandé est GPT-6.1 Sol, effort medium, après clôture effective du high. Lire sa passation, vérifier ses empreintes et utiliser les passages pertinents. Une nouvelle preuve nécessaire est signalée à root pour retour ciblé high ; ne pas compléter de mémoire.

Rédiger une monographie complète à la fois, puis la seconde. Chaque diagnostic utilise article data-monograph="DX.n", 14 sections data-point="1" à "14" et les sous-parties data-subpoint="9.a" à "9.d" et "11.A" à "11.D" une fois chacune. Conserver les noms A exacts. Le texte principal tient en une à quatre phrases par point ; fenêtres et tableaux portent les détails utiles, avec mécanismes, exemples, signes, gestes et sources. Le normal précède le pathologique. Le français est soutenu, clair, verbal et relié par des connecteurs, y compris dans les tableaux.

Livrer un HTML combiné de 90 000 à 200 000 octets ou deux HTML autonomes par diagnostic si nécessaire. Ne pas gonfler le texte pour une taille, ni supprimer un contenu utile pour tenir la limite. Si un diagnostic seul impose un découpage par points, prévenir root pour adapter le contrôle. Les brouillons et constructeurs restent dans internal/ ; seuls les HTML finaux occupent le premier niveau du dossier.

Le fichier est autonome : DOCTYPE, langue française, viewport et CSS embarqué. Une balise title non vide dans head est obligatoire et porte le code PROFILES ; l’interdit concerne l’attribut title utilisé comme infobulle, pas cette balise de métadonnées. Aucune image, script ou ressource externe n’est ajouté. Chaque tableau est enveloppé dans un div avec overflow-x:auto ; les identifiants et ancres sont uniques et cohérents ; aucune ligne ne dépasse 3 000 caractères. Les références numérotées, versions, URL et dates de consultation sont conservées. Le fichier porte la mention exacte « Contenu produit par IA à partir des sources citées ; non validé cliniquement par un médecin. » et se termine après /html par FIN_FICHIER.

Lire le rapport du watcher indépendant après les sauvegardes et corriger les écarts techniques. Les refus de rendu navigateur déjà documentés ne sont pas contournés ; l’affichage réel reste non vérifié lorsqu’il n’a pas été contrôlé. Aucun passage structurel ne vaut validation médicale.

Livrer selfcheck.json avec 102 questions exactes, leurs diagnostics, emplacements, sources, réponses de rédacteur et réserves, sans score humain. Fournir HELP actualisé, handoff_redaction.md et checkpoint.json avec lot entier, rôle, production_complete=true seulement après rédaction intégrale, fichiers/tailles/empreintes et limites. L’audit, l’accord humain et la transmission restent faux ou nuls. Signaler à root la fin réelle et les lacunes.
