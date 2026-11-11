# MISSION — auditeur indépendant d'une moitié de LOT (protocole Fable, 11.11.2026)

> **RÈGLE DE CONCISION (ordre de Vial, 11.11.2026) — tous les agents, Claude compris ; Vial exclu.** Écris extrêmement court : rapports, messages, commits, PR. Vers Vial, seulement ce qu'il doit décider, chaque question avec le lien ou le fichier de référence pour trancher ; le reste se traite entre agents, aussi brièvement.


Ta mission te donne : le LOT (NNN), les fichiers, le worktree, le nom du rapport, et s'il s'agit de l'audit 1 ou du
contre-audit. Tu n'as rédigé aucun de ces fichiers. Tu ne modifies AUCUN HTML, tu ne commites rien, pas de
checkout/reset/stash. Tu écris un seul fichier : le rapport `Claude/LOT_NNN/audits/<nom>.audit.json`.
Économise ton contexte : n'ouvre jamais un fichier entier ; extrais par scripts (points 1, 6, 9, 11, 14, fiches `.mb`,
bibliographie) et vérifie par script tout ce qui peut l'être.

Lis d'abord le bloc L1 en tête de `PROMPT_Casern/PROMPT_LOTS_L1_10.11.26.claude.md` (sections L1-… seulement),
`Claude/LOT_NNN/LISTE_DX_CANONIQUE.md` et `Claude/LOT_NNN/HELP.md` (décisions, retraits et doutes des rédacteurs).
Contre-audit : lis aussi le premier rapport et vérifie que chaque correction est réellement et correctement appliquée.

## À vérifier, par ordre de priorité

- **Prérequis anatomo-fonctionnel (dès LOT_021, et LOT_020 DX.1) :** si le diagnostic exige une base d'anatomie ou de physiologie, son absence, ou l'absence d'image réelle expliquant le pourquoi du signe, est un défaut **Grave**.
1. **Doses et AIPS.** `python3 Claude/_outils/verif_aips.py <fichiers>` : aucun défaut bloquant ; chaque alerte « dose
   absente » relue. Puis relis à la main au moins 40 renvois sur le texte AIPS réel (URL refdata de la bibliographie ; index
   `/home/user/Medina/AipsDownload_20261008.zip`), en priorité les urgences et les fiches : dose, voie, durée,
   contre-indications, grossesse et allaitement, âge. Une dose de recommandation que l'AIPS ne porte pas doit être écrite
   comme telle (« hors AIPS », source citée, sans ancre AIPS collée pour la forme). Quand l'AIPS ne porte pas la dose, une
   société savante suisse lue et datée fait foi au même titre ; quand l'AIPS la porte, la conduite suit l'AIPS et la
   divergence est écrite. Jamais le Compendium.
2. **Exactitude médicale.** Seuils, critères, drapeaux rouges, ordre et gravité, conduite d'urgence ; version la plus
   récente des recommandations ; sources suisses puis européennes ; aucune source seulement américaine en appui d'une
   décision ; chaque chiffre porté par la source citée (sonde au moins 25 chiffres sur la source elle-même) ; rien d'inventé.
3. **Faits perdus.** Relis la liste des retraits dans les messages de commit des fichiers (`git log -- <fichier>`) : tout fait sourcé unique et utile à l'examen fédéral doit
   être rétabli ; propose en échange la redite précise à retirer.
4. **Règles L1.** Point 1 = définition seule ; aucune ancienne architecture ; fenêtres `:target` ; examen physique en une
   fenêtre par région ; une fiche `.mb` par molécule ; point 14 ≥ 6 questions ; aucune redite dans un fichier ni entre
   fichiers du LOT ; aucune formule de lacune ou de fabrication ; 80 000–150 000 octets ; `controle3 --script-ok` VERT ;
   cohérence Phase A ↔ DX (noms exacts, rangs E, mêmes chiffres).
5. **Pédagogie (ordre de Vial du 11.11.2026).** Prérequis anatomo-fonctionnels installés quand le diagnostic l'exige,
   avec un schéma réel sourcé et lu (jamais un SVG dessiné ni une image générée) ; information vitale visible d'emblée
   (drapeaux rouges, délais, ce qu'il faut prévoir) ; raisonnement pas à pas pour un diagnostic réputé difficile chez le
   médecin assistant débutant, avec l'erreur classique ; densité et concision (signale toute phrase creuse ou redite).
   Ces exigences s'appliquent pleinement à partir du LOT_021. Jusqu'au LOT_020 (cours rédigés avant l'ordre), un manque
   de ce type se note en « Léger », sans bloquer et sans correction exigée.
6. **Design** (Playwright préinstallé, `chromium.launch()` sans option) à 1280 et 390 px : fenêtres centrées et occultantes
   (une fenêtre plus haute que l'écran défile à l'intérieur), aucun débordement horizontal, aucun lien interne ni
   inter-fichiers cassé, tableaux lisibles à 390 px.

Pour vérifier une source ou chercher la recommandation suisse la plus récente, charge les connecteurs par `ToolSearch`
(PubMed, Consensus, Elicit, Legal Data Hunter pour le droit suisse, recherche web), en visant d'abord les sources suisses.

## Rapport
`{"verdict":"ACCEPTE|corrections","date":"…","base":"<sha HEAD>","leves":[…],"restants":[{"fichier","gravite":"Critique|Grave|Moyen|Léger","constat","avant":"<extrait exact du HTML, occurrence unique>","correction":"<texte de remplacement prêt à coller>","source"}],"point14":{…},"octets":{…}}`
Chaque correction tient compte de la taille : si elle ajoute des octets à un fichier proche de 150 000, donne la redite à
retirer en échange. ACCEPTE exige zéro Critique et zéro Grave.
Réponse finale en 14 lignes au plus : verdict, défauts par gravité et par fichier, réponses aux questions de ta mission.
