# MISSION — rédacteur d'UN fichier d'un LOT (protocole Fable, 11.11.2026)

Ta mission te donne : le LOT (NNN), le fichier (Phase A ou DX.i), le worktree. Tu n'écris QUE dans ce fichier, dans
`Claude/LOT_NNN/HELP.md` (ajout en fin de fichier par `>>`) et dans `Claude/LOT_NNN/REPRISE.log` (ajout de lignes, jamais
de remplacement). D'autres agents travaillent sur les autres fichiers du même worktree : jamais de checkout, reset, stash,
rebase, `--force`, `git add -A` ni `git commit -a`. Fichiers temporaires dans un `mktemp -d` privé.

## Avant d'écrire
1. Lis le bloc L1 en tête de `PROMPT_Casern/PROMPT_LOTS_L1_10.11.26.claude.md` (sections L1-… seulement), puis
   `Claude/_outils/MISSION_RENFORCEMENT.md`. Le tableau des 14 points (µ3) est dans le même prompt : lis-le par extrait.
2. Modèles aboutis, en lecture seule et par extraits : `Claude/LOT_015/LOT_015_Phase_B_V0_DX.9.html` (DX) et
   `Claude/LOT_015/LOT_015_Phase_A_V0.html` (Phase A). Reprends leur gabarit exact : fenêtres, fiches `.mb`, bibliographie.
3. `python3 Claude/_outils/controle3.py --script-ok <fichier>` : état de départ. La passe mécanique (migrer_l1,
   renfort_citations, forme) est déjà faite.
4. Économise ton contexte : ne lis jamais le fichier entier d'un bloc ; travaille par scripts Python de remplacement ciblé.

## Ce que le fichier doit être à la fin
- `controle3 --script-ok` **VERT** ; fichier entier de **80 000 à 150 000 octets** (images exclues).
- Les **14 points** présents et complets. Titre du DX : nom exact de la liste (celui du fichier, ou `LISTE_DX_CANONIQUE.md`
  quand elle existe). Point 1 = **définition seule**. Aucune ancienne architecture (arbre CIM, cartouches de codes, pastilles).
- Fenêtres centrales `:target` : `<a class="ouvre" href="#f-ID">mot</a>` dans la phrase ; `<section class="fenetre" id="f-ID"
  role="dialog" aria-label="…"><div class="fen"><a class="fermer" href="#" aria-label="Fermer">Fermer ✕</a>…</div></section>`
  après le paragraphe. Aucun `popover`, aucun `title=`, aucun script propre à la leçon ; chaque tableau dans `<div class="t">`.
- Point 5 : chaque symptôme caractérisé, typique ou non, et pourquoi. Point 6 : **une fenêtre par région**, dans l'ordre de
  l'examen (signe, geste, aspect). Point 9 : une fenêtre par examen (valeurs, interprétation, pièges). Point 11 : une fenêtre
  « Urgence — conduite chronologique » si le diagnostic peut menacer, et **une fiche `.mb` par molécule**
  (`<section class="fenetre mb" id="f-dxN-m-<molécule>">` : indication, dose, contre-indications, grossesse et allaitement
  recopiés de l'AIPS de CETTE molécule). Point 14 : **au moins 6 questions** courtes, sourcées, avec renvoi au point.
- Langue : phrases verbales complètes de 12 à 28 mots (jamais plus de 32), partout, y compris fenêtres et légendes ; français
  soigné ; aucune redite dans le fichier ni avec un autre fichier du LOT. Le détecteur de `controle3` reconnaît le verbe par
  une liste (VERBES) et par terminaison : lis-le avant de choisir tes verbes.

## Exigences pédagogiques de Vial (ordre du 11.11.2026)
Elles s'appliquent aux cours rédigés à partir du LOT_021 ; aucun retour en arrière sur les LOTs antérieurs.
- **Précision, densité, clarté.** Chaque phrase porte un fait utile et exact ; aucune phrase d'ambiance, aucune redite. La
  concision sert l'envie de lire et la vitesse de lecture : à information égale, la phrase la plus courte gagne.
- **Prérequis anatomo-fonctionnels.** Si le diagnostic ne se comprend pas sans une base d'anatomie ou de physiologie (voies
  oculomotrices, voies optiques, innervation du larynx, nerf facial et ses branches, axe corticotrope, néphron, conduction
  cardiaque…), le point 3 l'installe d'abord, en une fenêtre « Base à connaître », avec un **schéma réel pris ailleurs**
  (Wikimedia Commons ou source ouverte, licence vérifiée : `python3 Claude/_outils/cliche.py chercher/prendre/figure`),
  inséré avec sa lecture guidée (repères, pièges) et retouché ou annoté si cela sert le lecteur. **Jamais de SVG dessiné,
  jamais d'image générée.** Si Wikimedia limite le débit, mets l'image en file (`/home/user/wt/images_attente.txt`) et
  note l'insertion à faire dans `HELP.md`.
- **Information vitale.** Ce qui tue, ce qui laisse une séquelle et ce qui ne supporte aucun délai se voit tout de suite :
  drapeaux rouges, fenêtre « Urgence — conduite chronologique » (minutes, heures, jours), délai maximal de chaque geste,
  et ce qu'il faut **prévoir** (complication attendue, surveillance, critère de transfert, piège qui fait perdre du temps).
- **Diagnostics difficiles pour le médecin assistant débutant.** Quand le diagnostic est connu pour être mal compris ou
  manqué (présentations trompeuses, raisonnement en plusieurs étapes, localisation neurologique, troubles hydro-
  électrolytiques, endocrinologie dynamique…), explique le raisonnement pas à pas : mécanisme, puis signe, puis examen,
  puis décision ; donne l'erreur classique du débutant et la façon de l'éviter, avec un exemple chiffré.

## Véracité (non négociable)
- Chaque phrase chiffrée cite la source de la bibliographie qui porte ce chiffre : vérifie-le, ne colle jamais une source au hasard.
- Sources suisses puis européennes, réellement lues et datées (URL lue pendant ta mission) ; version la plus récente ; aucune
  source seulement américaine en appui d'une décision ; rien d'inventé ni écrit de mémoire.
- Chaque dose (mg, µg, UI, mmol…) cite l'ancre `sb-aips-<n° Swissmedic>` de SA molécule, présente en bibliographie avec l'URL
  refdata et la date de mise à jour ; jamais le Compendium. Lis le texte AIPS réel : index du corpus
  `/home/user/Medina/AipsDownload_20261008.zip` (XML lu en flux : numéro d'autorisation → URL
  `https://files.refdata.ch/…-fr.html`, lisible par curl), ou `Claude/_outils/lecon.py prep/extraire`. La passe mécanique
  colle de mauvaises AIPS : contrôle chaque renvoi un à un.
- **Quand l'AIPS ne porte pas la dose** (posologie, schéma, durée, âge), une **société savante suisse** fait foi au même titre
  (ordre de Vial du 11.11.2026) : recommandation suisse lue et datée (sociétés de discipline, Swiss Medical Forum, Revue
  Médicale Suisse, guides des hôpitaux universitaires, OFSP), puis européenne à défaut. La phrase cite cette source et écrit
  « hors AIPS » ; elle ne porte aucune ancre AIPS collée pour la forme (`controle3` l'accepte ainsi). Si l'AIPS porte la dose
  et qu'une recommandation diverge, la conduite enseignée suit l'AIPS et la divergence est écrite.
- Une dose d'urgence ne se donne jamais sans l'âge auquel elle s'applique.
- Utilise tous les outils disponibles pour trouver la source (corpus AIPS, refdata, recherche web, PubMed, sites des sociétés
  suisses) avant de conclure qu'une dose manque. Molécule sans AIPS suisse lisible ET sans recommandation suisse ou
  européenne lue : garde la conduite, retire le milligramme, note-le dans `HELP.md`.
- Aucune formule de lacune ni de fabrication dans le cours (« à vérifier », « non lu », « lu le… ») : la lacune va dans `HELP.md`.
- Porte mécanique : `python3 Claude/_outils/verif_aips.py <fichier>` sans défaut bloquant ; relis chaque alerte « dose absente ».

## Taille
- Fichier trop court ou incomplet (points manquants, moins de 80 Ko) : complète-le par des faits distincts, sourcés et lus,
  là où µ3 les demande (anamnèse, examen par région, examens, prise en charge, fiches). Jamais de remplissage.
- Fichier trop long : retire des **redites** (information déjà dite dans le fichier, ou tenue par la Phase A ou un autre DX du
  LOT auquel on renvoie par un lien). **Aucun fait sourcé unique n'est perdu.** Chaque retrait est listé dans le message de
  ton commit (résumé, endroit où l'information reste) : l'auditeur le relit par `git log`. Si la bande est hors d'atteinte
  sans perdre un fait, arrête-toi et dis-le.

## HELP.md : court, à jour, rien d'autre (ordre de Vial du 11.11.2026)
`Claude/LOT_NNN/HELP.md` ne contient que ce qui sert encore au projet, en trois rubriques : « Lacunes ouvertes » (source ou
AIPS introuvable, image en attente), « Décisions en vigueur » (divergence AIPS ↔ recommandation tranchée, choix de liste) et
« Doutes médicaux à trancher ». Une ligne par entrée, avec le fichier concerné. Pas d'historique, pas de journal d'agent,
pas de liste de retraits : ce qui est résolu se supprime. Ajoute tes lignes sous la bonne rubrique (`>>` en fin de fichier
si la rubrique manque) et supprime celles que ton travail résout.

## Fin de mission
- `python3 Claude/_outils/forme.py <fichier>`, puis `controle3` et `verif_aips` une dernière fois.
- Une ligne dans `REPRISE.log` : `AAAA-MM-JJ HH:MM | <fichier> | VERT/ORANGE/ROUGE | octets | reste : <5 mots>`.
- Valide par chemin : `git commit -m "<message>" -- <ton fichier> Claude/LOT_NNN/HELP.md Claude/LOT_NNN/REPRISE.log`, puis
  `git push origin <branche>` (push refusé : un autre agent a poussé depuis le même worktree, relance le push). Message
  terminé par « Prompt L1 lu et appliqué. », une ligne vide, puis les lignes Co-Authored-By et Claude-Session de ta mission.
- Si tu manques de contexte : valide et pousse l'état atteint s'il est meilleur que le départ et sans fait perdu, et dis
  exactement ce qui reste.
- Rapport en 8 lignes au plus : verdict, octets, questions au point 14, fiches `.mb`, AIPS corrigées, retraits, ce qui
  reste, doutes médicaux.
