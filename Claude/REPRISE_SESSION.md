# Reprise MEDINA — dépôt vialdjoukang-spec/organigramme-examen-federal (état au 11.11.2026, 17 h, Zurich — PAUSE demandée par Vial)

> **Lis d'abord `Claude/CONSIGNES_VIAL.md` (recueil des consignes de Vial) et applique-le.**
> **RÈGLE DE CONCISION (ordre de Vial, 11.11.2026) — tous les agents, Claude compris ; Vial exclu.** Écris extrêmement court : rapports, messages, commits, PR. Vers Vial, seulement ce qu'il doit décider, chaque question avec le lien ou le fichier de référence pour trancher ; le reste se traite entre agents, aussi brièvement.


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

## Injecté — jusqu'où (11.11.2026, 17 h)
- **100 % (audités + contre-audités) : LOT_001 à LOT_020.** LOT 1–16 fusionnés dans main. LOT 17–20 : PR #644 (017),
  #645 (018), #646 (019), #643 (020), étiquette `audit-ok`, fusion automatique armée ; **seule une panne DNS des runners
  GitHub (`playwright install-deps`, depuis 13 h 51, `main` aussi rouge) bloque la fusion** : relancer les jobs quand elle cesse.
- HTML provisoire hors ligne remis à Vial : `Progression_provisoire_LOT1-20.html` (220 cours, images incluses ; scratchpad,
  script `empaqueter.py` dans `scratchpad/bundle.*`).
- Outils : PR #642 (`claude/reprise-session`) = ce fichier, `CONSIGNES_VIAL.md`, règle de concision, controle3 renforcé
  (ancres sans cible, fenêtres imbriquées, gabarit non converti), LOT_012 f-rx-kerley corrigé. PR #647 (`claude/designer`) :
  forme.css sans ivoire (fonds blanc / bleu / vert ultra-pâles). Même blocage CI.

## En pause (à reprendre)
- **LOT_021** (S1.5 Épistaxis) `claude/lot-021-renfort-l1` : 11/11 VERT, audit 1 fait, corrections faites (commit 6d4264b) ;
  reste : contre-audit → PR.
- **LOT_022** (paupières) `claude/lot-022-renfort-l1` : liste gelée (renumérotée), 11/11 VERT, planche envoyée ;
  reste : audit 1 (A, B, arrêtés par la pause, à relancer) → corrections → contre-audit → PR. Doute : Dystonie-info.ch édité par Merz (DX.8).
- **LOT_020 DX.1** : fenêtre « voie motrice faciale » faite, mais schéma de singe (Gothard 2014) refusé → remplacer par un
  schéma HUMAIN central/périphérique (Wikimedia/Europe PMC) ; agent arrêté par la pause.
- **Réceptacle** `claude/fiches-reference` (pas de PR) : refonte v3 (19 groupes PROFILES, jauges ondulantes, Réflexe Gn,
  banque QCM vide, pharmaco 3 colonnes, chaînes d'activation, rappel anatomo-physiologique en fenêtre). Vial n'a pas
  encore validé le modèle des fiches ; ADH absente de la chaîne SRAA (à sourcer).
- LOT_023 et suivants : pas commencés.

## Méthode éprouvée (par LOT)
worktree depuis origin/main → gel P1 (`geler.py`, renuméroter les fichiers si la liste change) → 11 rédacteurs en
parallèle (Agent direct, pas Workflow) → commit fichier par fichier → planche → audit A/B → corrections → contre-audit → PR.
Briefer chaque agent : CONSIGNES_VIAL.md, base anatomo-fonctionnelle obligatoire avec image réelle, mktemp privé.

## Points en attente de Vial
- Validation du modèle des fiches (Examens / Pharmacologie) avant production massive.
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
- Le scratchpad est partagé : un agent y a créé `struct.py` (masque le module Python) ; lancer les scripts avec `python3 -I` ou depuis un mktemp privé.
