# PROMPT_PRODUCTION_V2 — prompt maître du chantier de production de LOTs

Autonome : une IA qui ne lit que ce fichier comprend le projet, retrouve l'état et produit. Détail normatif : `PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V0.md` (« Prompt V0 », lecture ciblée par `grep -n` puis `sed -n`, jamais en entier). En cas de conflit, ce fichier et l'ordre écrit de Vial priment pour l'organisation ; le Prompt V0 prime pour le fond.

## 1. But
Dépôt `organigramme-examen-federal`, branche de travail `production-v2`. Il produit, LOT après LOT (file stricte LOT_001 → LOT_248), des leçons médicales HTML pour l'examen fédéral suisse de médecine. Un LOT = un SSP (symptôme, signe ou situation) = 1 fichier Phase A + 10 fichiers Phase B (un par diagnostic différentiel, DX.1 à DX.10), soit 11 HTML. Le LOT n+1 ne démarre que si le LOT n est achevé (déposé, ou bloqué et consigné). Le dépôt final est `LOT_Claude_Finaux/LOT_XXX/` ; le brouillon vit dans `lot en cours de production/LOT_XXX/`.

## 2. Règles de fond (non négociables)
1. Sources suisses d'abord (Fedlex avec date d'état, OFSP, OFS, Obsan, OPAS, liste des spécialités, sociétés suisses), puis européennes (ESC, ESPEN, EULAR, NICE, etc.). Jamais une source américaine exclusive. Chaque source est lue réellement, numérotée [Sn], avec titre, organisme, année, URL, date de consultation ; l'extrait daté va dans `evidence/`. Non lue ou introuvable : écrire « À vérifier » ou « donnée non trouvée dans les sources consultées ». Jamais de chiffre de mémoire.
2. Doses et spécialités : information professionnelle suisse (AIPS) seulement, jamais le Compendium. Corpus local `.cache/aips/AipsDownload_20261008.xml` (extraits `.cache/aips/<n°>.txt`). Citer mot pour mot la dose, la contre-indication, la grossesse, l'allaitement, l'enfant, l'arrêt ; numéro Swissmedic par forme galénique. Chercher par nom de spécialité dans le XML avant d'écrire « À vérifier (AIPS) ». Tout usage hors information professionnelle est écrit en clair.
3. Aucune donnée personnelle dans le dépôt (public).
4. Ne jamais modifier `/workspace/ssp/app.html`. Ne jamais travailler sur `main` : branche `production-v2`.
5. N'affirmer que ce qui est fait et vérifié. Un guillemet = une citation sourcée. Aucun refus d'audit : celui qui trouve la faute la corrige en place (Prompt V0 §16.1).
6. Aucun méta-terme dans le HTML (« Phase B », « LOT », « corpus »). Mention finale : « Contenu établi à partir des sources citées ; non validé cliniquement par un médecin. »

## 3. Format d'un LOT
- 14 points par monographie (Prompt V0 §11) : 1 définition ; 2 épidémiologie (Suisse puis Europe) ; 3 physiopathologie ; 4 démarche diagnostique (graves d'abord, 🚩) ; 5 anamnèse et drapeaux rouges ; 6 examen physique ; 7 approche syndromique ; 8 diagnostic positif et critères ; 9 examens complémentaires (9.a à 9.d) ; 10 arbre décisionnel ; 11 prise en charge suisse (11.A à 11.D) ; 12 prévention ; 13 points clés ; 14 pièges d'examen. Phase B : `<h3 id="dxN-p1">` … `dxN-p14`, `<h2>DX.N — nom exact de la liste canonique</h2>`.
- Phase A : monographie du SSP, 10 DD par prévalence décroissante avec gravité explicite (E1…), tableau comparatif, algorithme graves d'abord.
- Taille : bande 80 000–150 000 octets ; viser 110–125 Ko à la rédaction ; plafond pratique 140 000 octets (chaque audit ajoute 4 à 12 Ko).
- HTML5 autonome ; grandes fenêtres par l'API `popover` (bouton `popovertarget` dans la phrase, `<div id="dxN-…" popover class="fenetre">` après le `</p>`, bouton Fermer avec `popovertargetaction="hide"`) ; aucun JavaScript, aucun `title=`, aucune espace insécable ; ids préfixés `dxN-`.
- **Rappels de sciences fondamentales (ordre de Vial du 30.10.2026).** Pour les SSP dont le raisonnement repose sur l'anatomie et la physiologie (neuro-ophtalmologie et neurologie, endocrinologie et métabolisme, néphrologie, cardiologie, hématologie, etc.), le point 3 (physiopathologie) contient systématiquement les rappels de base indispensables à la compréhension (anatomie, physiologie, biochimie) : soit une explicitation brève entre parenthèses, soit un terme cliquable ouvrant une fenêtre `popover` qui l'explique (anatomie des voies, boucles de régulation, mécanismes). Rappels sourcés (manuel ou revue), courts, au service du raisonnement clinique ; l'auditeur médical vérifie leur exactitude, l'auditeur de conformité leur présence.
- Dernière ligne : `<!-- FIN_FICHIER LOT_XXX_Phase_A -->` (ou `…_Phase_B_DX.N`). Absent = troncature présumée.
- Nommage : `LOT_XXX_Phase_A_V0.html`, `LOT_XXX_Phase_B_V0_DX.N.html`.
- Liste canonique : le rédacteur de Phase A écrit `LISTE_DX_CANONIQUE_PROVISOIRE.md` ; l'auditeur médical de la Phase A la gèle en `LISTE_DX_CANONIQUE.md` (noms, ordre, numéros identiques à la Phase A). Les Phase B ne démarrent qu'après ce gel et la respectent mot pour mot.
- Écrits par le rédacteur : HELP (questions sans réponse certaine, `## H…`, Prompt V0 §18), JOURNAL, `evidence/INDEX.md`. Écrits par l'audit : `CORRECTIONS_AUDIT.md` (corrections à hériter ; passe transversale T1…Tn), `audits/corrections.jsonl`, `audits/scores.jsonl`.

## 4. Chaîne de production et routage
Par fichier : rédacteur → auditeur-médical → auditeur-conformité → (une fois les 11 fichiers audités) passe transversale → dépôt.

| Poste | Agent (`.claude/agents/`) | Modèle · effort |
|---|---|---|
| Phase A | `redacteur-phase-a` | opus · xhigh |
| Phase B (un fichier par agent) | `redacteur` | opus · xhigh |
| Audit médical, correction en place (max si > 30 % à réécrire) | `auditeur-medical` | opus · xhigh |
| Audit conformité, correction en place | `auditeur-conformite` | sonnet · high |
| Passe transversale T1…Tn | `auditeur-medical` | opus · xhigh |
| Inventaires, tris, manifestes | `mecanique` | haiku · medium |
| Contrôles déterministes | scripts | aucun |

Règles : un auditeur n'audite jamais ce qu'il a rédigé ; escalade seulement sur échec constaté ; chaque lancement d'agent s'écrit en une ligne dans `journal/routage.jsonl` (horodatage, lot, fichier, agent, modèle, effort, raison). Détail : `harnais/ROUTAGE_MODELES.md`. Briefs types (appels d'une ligne : « Lis le brief ; LOT ; N ») : `harnais/briefs/AUDIT_MEDICAL.md`, `harnais/briefs/CONFORMITE.md`, et `lot en cours de production/LOT_XXX/BRIEF_PHASE_B.md` (rédacteur ; à écrire pour chaque LOT en copiant celui du LOT précédent). Les agents ne committent pas : la session principale (chef de production) commite et pousse.

## 5. Parallélisme et économie de jetons
- Au plus 5 agents opus en parallèle, après le gel de la liste canonique ; chemins disjoints (un fichier par agent).
- Les agents ne lisent ni `CONTINUATION.md`, ni `PROCHAINE_ACTION.md`, ni `ETAT.md`, ni `porte.py`, ni `checkpoint.py` (la procédure Codex du `CLAUDE.md` ne s'applique pas à ce chantier, ordre de Vial).
- Prompt V0, `HARNAIS_OBLIGATOIRE.md`, `ROUTAGE_MODELES.md` : `grep -n` puis `sed -n` sur les sections nommées par le brief.
- HTML lu par points : `python3 harnais/controle_lot.py extraire <fichier> --points 2,3,…` ; pas de relecture intégrale répétée.
- Forme et langue : `python3 harnais/audit_langue.py <fichier> --json` d'abord (zéro jeton) ; l'effort va au fond.
- Téléchargements et scripts : seulement dans `<scratchpad>/<LOT>_<fichier>_<rôle>/`, jamais à la racine du dépôt ni du scratchpad.
- Réponse finale d'un agent : 10 lignes au plus (15 pour l'auditeur médical), chemins des fichiers écrits, sans répéter les journaux.
- SHA-256 inchangé = scores inchangés : pas de relecture. Ne jamais reprendre un agent par SendMessage (recharge tout son historique) : relancer un agent neuf avec le brief et l'état disque.

## 6. Pause et reprise : PONS-OBLONGATA
Mémoire de reprise sans modèle : `python3 harnais/pons_oblongata.py <commande>`.
- `capture` (défaut) : lit le disque et écrit `journal/PONS_OBLONGATA.json` (machine), `journal/REPRISE.md` (≤ 80 lignes : où on en est, sûr, incertain, prochaines actions) et `journal/pons/AAAAMMJJ-HHMM.json` (50 derniers). Automatique après chaque commit (`harnais/hooks/post-commit`, installé par `sh harnais/installer_hooks.sh`) et à la fin de chaque audit (hook Stop des deux auditeurs).
- `pause "motif"` : capture + `journal/PAUSE`. Pendant la pause aucun agent n'est lancé ; les agents en cours finissent leur fichier (pause douce, aucun jeton perdu) ; arrêt dur seulement sur ordre explicite de Vial.
- `reprise` : affiche REPRISE.md et lève la pause. `etat` : une ligne par fichier. `veille [--intervalle 20]` : surveille le disque et recapture ; PID dans `journal/pons.pid` ; arrêt par SIGTERM.
- Étapes déduites : aucun fichier / rédaction en cours / rédigé / audit médical fait / conformité faite / transversale faite / déposé. Un agent lancé (routage.jsonl) sans retour postérieur sur disque est « probablement en cours ou interrompu » : vérifier le disque avant de relancer.
- Reprise : lire `journal/REPRISE.md` seul (pas l'historique), exécuter les « prochaines actions », ne relancer que ce qui manque.

## 7. Carte des scripts (`harnais/`)
| Script | Rôle |
|---|---|
| `controle_lot.py` | `verifier <dossier> [--json]` (14 points, bande, FIN_FICHIER, popover, liste A↔B, SHA) ; `extraire <fichier> --points …` ; `manifeste <dossier>` |
| `audit_langue.py` | alertes de langue et de forme d'un fichier (`--json`, `--corriger`) |
| `rapport_qualite.py` | agrège `corrections.jsonl` et `scores.jsonl` en `RAPPORT_QUALITE.html/.json` |
| `etat_des_lieux.py` | `ETAT_DES_LIEUX.html` (chantier, git, journaux) |
| `routage_miroir.py` | `ROUTAGE_MIROIR.html` depuis `journal/routage.jsonl` |
| `progression.py` | `PROGRESSION.html` |
| `scinder_1_10.py` | découpe d'un HTML multi-DD en 1 fichier par DD |
| `banc_essai_langue.py`, `analyse_harnais.py` | mesure de l'audit de langue ; analyse du harnais |
| `bracelet/bracelet_suggest.py` | suggère 1 à 3 outils pour une tâche |
| `pons_oblongata.py`, `hooks/`, `installer_hooks.sh` | mémoire de reprise (section 6) |
Vérification de syntaxe : `python3 -m py_compile harnais/*.py`. Si un script manque, le reconstruire à partir de ce tableau : chacun est déterministe et sans modèle.

## 8. Cycle d'un LOT
1. `DECISION_SEANCE.md` (SSP, producteurs, découpage), `evidence/`, leçons du LOT précédent (`LECONS_LOT_XXX.md`).
2. Phase A (rédacteur-phase-a) ; audit médical (gèle la liste) ; audit conformité.
3. Phase B : jusqu'à 5 rédacteurs opus en parallèle ; chaque fichier passe par `controle_lot.py verifier`, audit médical, audit conformité.
4. Passe transversale : applique les items T1…Tn de `CORRECTIONS_AUDIT.md` à tous les fichiers, marque « **Fait** », écrit les extraits `evidence/` manquants, resynchronise les SHA dans `scores.jsonl` par script.
5. Écrire `LECONS_LOT_XXX.md` pour le LOT suivant.

## 9. Procédure de dépôt
1. Copier les 11 HTML, `LISTE_DX_CANONIQUE.md` et `audits/` dans `LOT_Claude_Finaux/LOT_XXX/`.
2. `python3 harnais/controle_lot.py verifier LOT_Claude_Finaux/LOT_XXX` : 0 critique, 0 avertissement ; puis `manifeste` (écrit `MANIFESTE.json`).
3. `python3 harnais/rapport_qualite.py` ; `etat_des_lieux.py` et `progression.py` si demandé.
4. `LOT_Claude_Finaux/ETAT_FILE.json` : `statut_audit` ACCEPTE (ou BLOQUE), `cycles`, `score_A`, `score_B`, `verdict`, `depose: true`, `note` (corrections, graves, critiques).
5. `JOURNAL.md` racine : une ligne datée (décision, incident, nombre de corrections). Checklist Prompt V0 §19.
6. `python3 harnais/pons_oblongata.py capture`, commit sur `production-v2`, PR ; CI vérifiée une fois avant le dépôt, puis fusion par commit de fusion. Pas de notifications de PR en continu.

## 10. Leçons accumulées (LOT_014 à LOT_016 ; 900 corrections au LOT_015, 390 au LOT_016)
- Potassium i.v. : contrôler la diurèse avant (AIPS KCl 29552), citer acidose et déshydratation sévère ; kaliémie < 3,5 mmol/L : potassium d'abord, insuline différée.
- Crise surrénalienne : prélever cortisol et ACTH juste avant l'hydrocortisone si cela ne retarde rien ; adulte ESE/ES 2024 (100 mg i.v./i.m., NaCl 0,9 %, 200 mg/24 h) ; enfant BSPED 2023 ; l'AIPS de Solu-Cortef ne fixe pas de dose de crise.
- Contre-indications AIPS complètes pour chaque médicament conseillé (rénale avant tout ajustement : Aldactone, Lasix, Comilorid ; bêtabloquants et insuffisance cardiaque ; antithyroïdiens) ; grossesse, allaitement, enfant mot pour mot ; règle d'arrêt de chaque molécule.
- Numéro Swissmedic par forme galénique, vérifié par script dans le XML ; ne pas étendre une limitation de remboursement d'une spécialité à une autre ; relire la liste des spécialités (dates, ≥ ou >).
- Artérite à cellules géantes : « plus de 50 ans », avis spécialisé dans les 24 heures. Test VIH : directive OFSP PICT 2015 (OPAS art. 12d). PPR/ACG et autres DD graves ne s'omettent pas au point 4 ni dans l'arbre.
- Hors information professionnelle dit en clair ; un raisonnement déduit des AIPS n'est pas présenté comme recommandation ; guillemets réservés aux citations.
- Version la plus récente et officielle (diaporamas ESC, registre de l'Union) avant d'écrire « non lu » ; extrait `evidence/` contenant réellement le passage cité.
- Taille : 110–125 Ko au premier jet. Format : `popovertargetaction="hide"` sur chaque Fermer, balises `</td>`, `</tr>`, `</th>` conservées.
- Un agent interrompu laisse un fichier cohérent (corrections atomiques et journalisées) : relancer l'audit en entier plutôt que de reconstituer.
