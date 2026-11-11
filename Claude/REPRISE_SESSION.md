# Reprise MEDINA — dépôt vialdjoukang-spec/organigramme-examen-federal (état au 11.11.2026, 15 h, Zurich)

Message de transition écrit par la session précédente. À coller en tête de la prochaine session, ou à lire ici.

## Ordres de Vial en vigueur
- Claude a le droit sur tous les LOTs, en ordre croissant (`ATTRIBUTIONS.json`, clé `ordre_2026_11_11`).
- Protocole : `Claude/_outils/PROTOCOLE_FABLE.md`. Missions : `MISSION_FICHIER_L1.md` (rédacteur d'un fichier),
  `MISSION_AUDIT_L1.md` (auditeur), `.claude/agents/designer.md`, `Claude/_reference/MISSION_FICHE.md` (fiches).
- Qualité absolue : sources suisses puis européennes lues et datées ; AIPS de chaque molécule relue sur refdata ; quand
  l'AIPS ne porte pas une dose, une société savante suisse fait foi et la phrase écrit « hors AIPS » ; aucun fait sourcé
  unique perdu ; audit puis contre-audit par des auditeurs neufs ; PR avec « Prompt L1 lu et appliqué. », section
  « ## Automates actifs », étiquette `audit-ok`, fusion automatique par commit de fusion, abonnement à la PR.
- Économie : un rédacteur ne reçoit qu'un fichier qui ne passe pas les portes (`controle3 --script-ok`, `verif_aips.py`,
  80–150 Ko) ; il rédige si le fichier est vide ou à l'ancienne architecture, il retouche s'il existe ; jamais de doublon.
- Exigences pédagogiques (prérequis anatomo-fonctionnels avec schéma réel, jamais de SVG ; information vitale ; diagnostics
  difficiles pas à pas ; concision) : pleinement à partir du LOT_021, sans retour en arrière.
- Designer : branche `claude/designer`, cours à 100 % seulement, aspect seulement, outils gratuits ; le chef d'orchestre
  relit ses preuves et ouvre la PR.
- HELP.md de chaque LOT : court (lacunes ouvertes, décisions en vigueur, doutes) ; les retraits vont dans les messages de commit.
- Utiliser les connecteurs (PubMed, Consensus, Elicit, droit suisse, web), Suisse d'abord.
- Chaque matin à 8 h 00 (Europe/Zurich) : envoyer la page réceptacle (tâche planifiée « Progression des LOTs à 8h00 »).
- Montrer régulièrement les planches de 5 captures par cours (`Claude/_outils/planche5.py`).
- Messages dans le chat : courts, centrés sur l'utile. Vial est souvent sur mobile.

## Fait
- LOT_001 à LOT_016 (motifs G1 à G16) : renforcés L1, audités, fusionnés dans main. PR #634 (LOT_015), #638 (LOT_016).
- Outils fusionnés : #635 et #636 (protocole, `verif_aips.py`, `planche5.py`, `capture5.py` pour les fenêtres `:target`,
  `controle3` qui accepte « hors AIPS »), #637 (HELP courts des LOT_001–015), #639 et #640 (feuille commune et finition du
  designer sur LOT_014–016), #641 (page réceptacle).
- Page réceptacle en ligne : https://vialdjoukang-spec.github.io/organigramme-examen-federal/progression.html
  (`outils/receptacle.py`, `outils/publier_cours.py`, `Claude/_reference/prets.txt` = « 1-16 »). Onglet Cours : 176 cours
  ouvrables par le nom du motif et du diagnostic. Onglets Examens complémentaires (184 fiches prévues) et Pharmacologie
  (191 fiches prévues) : arborescence seule (`Claude/_reference/examens.json`, `pharmaco.json`).

## En cours (worktrees de la session précédente : à recréer depuis les branches poussées)
- LOT_017 (S1.1 Diplopie, ptosis) — branche `claude/lot-017-renfort-l1` : liste gelée ; 9 fichiers sur 11 aux portes ;
  restent DX.7 et DX.10 ; puis planche, audit, corrections, contre-audit, PR.
- LOT_018 (S1.2 Perte de vision) — `claude/lot-018-renfort-l1` : liste gelée ; rédaction à faire sur les 11 fichiers
  (Phase A de 260 Ko à ramener sous 150 Ko).
- LOT_019 (S1.3 Altération de la voix) — `claude/lot-019-renfort-l1` : liste gelée ; Phase A, DX.3, DX.6, DX.8 aux
  portes ; les sept autres étaient en rédaction (vérifier ce qui a été poussé).
- LOT_020 (S1.4 Asymétrie du visage) — `claude/lot-020-renfort-l1` : liste gelée ; Phase A, DX.1, 2, 4, 5, 8, 9 rédigés ;
  DX.3, 6, 7, 10 étaient en rédaction ; vérifier les portes de chaque fichier, puis audit.
  Les fichiers d'origine des LOT_019 et 020 n'avaient que 20 à 40 Ko de texte (le reste : styles intégrés) : rédaction entière.
- Fiches pilotes — branche `claude/fiches-reference` : « Hémogramme : lignée rouge et indices » et « Inhibiteurs de
  l'enzyme de conversion » en rédaction. Dès qu'elles sont rendues : les intégrer (`outils/receptacle.py`), envoyer
  l'ébauche HTML à Vial, attendre son avis sur le modèle avant de lancer les 373 autres.

## À faire ensuite
1. Finir les LOT_017 à 020 (portes → planche → audit → corrections → contre-audit → HELP court → PR), ajouter chaque LOT
   fusionné à `Claude/_reference/prets.txt`.
2. Designer : bandeau des cours sans « LOT_0NN · DX.n » (code et nom du motif à la place) ; `<title>` au format
   « Nom du diagnostic — Nom du motif » ; sous-titre 9.a « Examen de référence » pour les cours à venir.
3. LOT_021 et suivants, par vagues, avec les exigences pédagogiques complètes.
4. Fiches des onglets Examens et Pharmacologie, après validation du modèle par Vial (loi de Pareto : 20 % d'information
   qui font 80 % des décisions ; structure identique ; conduite suisse sourcée ; 6 000 à 9 000 octets).

## Points en attente de Vial
- Photographie d'un visage identifiable dans LOT_020 DX.1 (Wikimedia, licence libre) : la garder ou la retirer (dépôt public).
- Corrections de langue par un modèle moins cher (Fable gardé pour la vérification médicale et l'audit) : oui ou non.
- Relever `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` (plafond actuel : 20 agents) pour accélérer.
- Doutes médicaux listés dans le HELP.md de chaque LOT (LOT_006 antipaludiques sans AIPS ; LOT_007 liste à 10 ou 12 ;
  LOT_011 lorazépam et foie ; LOT_008 adrénaline entre 30 et 35 °C ; LOT_016 sel de potassium et acidose).

## Pièges techniques appris
- La machine a 4 processeurs : l'outil Workflow ne lance que 2 agents à la fois ; lancer les rédacteurs directement
  (un par fichier), jusqu'à 20 en parallèle. Un fichier lourd épuise le contexte d'un agent : un agent par fichier.
- Plusieurs agents dans un même worktree : valider par chemin (`git commit -- <fichiers>`), jamais `git add -A` ;
  HELP.md et REPRISE.log sont partagés.
- `forme.py` : ne jamais passer un motif `LOT_0*` (il touche les LOTs non renforcés) ; lister les LOTs voulus.
- `controle3` lancé sur un LOT entier détecte les phrases partagées entre fichiers : le relancer avant l'audit.
- Le corpus AIPS est dans le dépôt Medina (`/home/user/Medina/AipsDownload_20261008.zip`) ; refdata est lisible par curl.
- Aucune donnée personnelle dans ce dépôt public.
