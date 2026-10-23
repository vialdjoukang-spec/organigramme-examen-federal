# CATALOGUE · outils gratuits, automates, MCP et skills (Étape 0)

Généré par `python3 tools/catalogue.py`, puis complété par Codex. À présenter avant toute étape de contenu.

## 1. Scripts du dépôt (gratuits, déterministes)

| Script | Rôle |
|---|---|
| `tools/_app.py` | Fonctions communes : localisation d'une constante JS de premier niveau par str.find. |
| `tools/aips_verbatim.py` | Compare les extraits aux textes officiels Refdata ; ne valide aucune dose clinique. |
| `tools/aletheia.py` | Alétheia · Janus · vérité des sources : doses (G1), source et date (G2), domaines (G3). |
| `tools/arsenal/_c.py` | Commun arsenal : racine, chargement, sortie JSON compacte.""" |
| `tools/arsenal/audit_diff.py` | Pour l'auditeur : seules les valeurs modifiées (base...HEAD) avec leurs sources, en JSON lignes. |
| `tools/arsenal/ci_attente.sh` | Attend TOUS les contrôles de la PR de la branche courante (ou $1) sur le commit HEAD poussé. |
| `tools/arsenal/ci_verdict.py` | stdin : JSON de `gh pr checks --json name,bucket`. Sortie : VERT (0), ROUGE <échecs> (1), ATTENTE (2).""" |
| `tools/arsenal/extrait.py` | Sort UNIQUEMENT le bloc à traiter, en JSON compact (jamais app_v2.html entier). |
| `tools/arsenal/lot.py` | Vérifie un lot en une commande ; une ligne par défaut, -v pour le détail. Code 1 si erreur. |
| `tools/arsenal/pr.sh` | pr.sh "<titre>" [SSP …] : rebase origin/main, régénère (mono_build, cours/appliquer <SSP>, ck_build), |
| `tools/asclepios/ges_v2.py` | Asclépios · restructuration de GES (3 axes, sous-régions, ordre strict, renvois, lacunes). |
| `tools/asclepios/tip_autres_a.py` | Asclépios · revue des blocs « Autres éléments ciblés » (lot A : G, S1, S2, S3), 17.10.2026. |
| `tools/asclepios/tip_autres_b.py` | Asclépios · revue des blocs « Autres éléments ciblés » (lot B : S4 à S9), 17.10.2026.""" |
| `tools/asclepios/tip_autres_c.py` | Asclépios · revue des blocs « Autres éléments ciblés » (lot C : F et O), 17.10.2026.""" |
| `tools/asclepios/tip_exam.py` | Asclépios · normalise TIP[*].c[5] (Examen physique ciblé) en format compact rendu par exFmt() : |
| `tools/asclepios/tip_nouveaux.py` | Asclépios · 15 champs 5 de TIP (« Examen physique ciblé ») écrits le 17.10.2026 ; sources dans tip_sources.py.""" |
| `tools/asclepios/tip_revue.py` | Asclépios · applique au champ 5 de TIP (data/TIP.json) : 15 champs écrits (tip_nouveaux.py, sources tip_sources.py) |
| `tools/asclepios/tip_sources.py` | Asclépios · sources lues le 17.10.2026 pour les 15 champs 5 de TIP écrits (tip_revue.py).""" |
| `tools/audit/galien_region.py` | Galien · six automates d'audit régional (tools/audit/regions.yml), au-dessus du niveau 1 d'Atlas et Janus. |
| `tools/audit/niveau1.py` | Audit médical de niveau 1 · Janus et Galien · huit contrôles déterministes, zéro jeton (CI). |
| `tools/audit/prevalence.py` | Contrôle mécanique des fréquences des diagnostics différentiels (data/ck/prev.json) · Asclépios, 17.10.2026. |
| `tools/audit/rapport_fautes.py` | Galien et Janus · « Rapport d'audit médical : les fautes corrigées ». |
| `tools/audit/verbes_gen.py` | Janus · génère tools/audit/verbes_conjugues.txt.gz, la liste des formes verbales conjuguées |
| `tools/audit_examen/analyse.py` | redundancy: similar item titles across different regions |
| `tools/audit_examen/render.py` | @page{size:A4 landscape;margin:12mm}body{font-family:'DejaVu Sans',sans-serif;font-size:9pt;text-align:justify;color:#111} |
| `tools/audit_examen/sk.py` |  |
| `tools/budget.py` | Budgets de taille (Héphaïstos, étendus par Atlas le 17.10.2026 pour le chantier Nerfs crâniens et CK) : |
| `tools/build_exi.py` | Thémis · 17.10.2026 · écrit data/EXI.json et data/SESSION.json (source : research_exigences.md, pages lues le 17.10.2026). |
| `tools/build_mem.py` | Mnémosyne · construit data/MEM.json mot pour mot à partir de research_memorisation.md. |
| `tools/catalogue.py` | Génère CATALOGUE.md : scripts et automates gratuits, workflows, skills du dépôt, MCP et droits. |
| `tools/check_fonctions_asset.py` | Vérifie l'extraction des fonctions et reconstruit le script principal.""" |
| `tools/check_hash.py` | Garde I1 : l'empreinte SHA-256 de orig/app.html ne doit jamais changer.""" |
| `tools/ck_build.py` | Atlas · compilateur des données CK : data/ck/*.json → assets/ck/*.js (contrôle G5). |
| `tools/ck_common.py` | Atlas et Janus · fonctions communes aux outils CK (compilateur, Lyncée, audit de niveau 1). |
| `tools/coordination/calculer.py` | Suivi couplé 8/9, sans écriture clinique ni validation automatique.""" |
| `tools/coordination/relance.py` | Ordonnanceur léger : observe les exécutions, évite doublons et respecte le budget.""" |
| `tools/cours/appliquer.py` | Appliquer un lot relu aux seules parties TIP.c ; préserver DD et fondamentaux.""" |
| `tools/cours/controler.py` | Suivi des cours SSP : relecture liée au contenu, jamais déduite du numéro.""" |
| `tools/cs_build.py` | Chiron · compilateur des stations CS : data/cs/*.json → assets/st/*.js. |
| `tools/dedale/annoter.py` | Dédale-A · composition des 3 vues annotées d'un nerf crânien (face, profil, trois quarts). |
| `tools/dedale/crane.py` | Dédale-C · crâne 3D au crayon (traits pleins à graisse hiérarchisée) pour les 3 vues d'un nerf crânien. |
| `tools/dedale/freestyle.py` | Dédale-3D · rendu au crayon des vues d'un nerf crânien à partir du modèle Z-Anatomy. |
| `tools/dedale/masques.py` | Dédale-M · silhouettes pleines des territoires (masques) à partir du modèle Z-Anatomy, en mémoire réduite. |
| `tools/dedale/trace.py` | Dédale-T · plan du nerf au crayon à partir d'une planche de Gray (domaine public), par automate. |
| `tools/dedale/verifier.py` | Dédale-V · contrôle des schémas de nerfs crâniens (CI, zéro jeton). |
| `tools/doses_check.py` | Pharmakon · contrôle de la table suisse des doses (data/ck/doses_ch.json), zéro jeton. |
| `tools/file_fusion.sh` | File de fusion-publication automatique (gratuit : gh + git + python3). Lancé par tools/veille_relance.sh |
| `tools/galien/aips_relecture_20261017.py` | Corrections après relecture des 98 lignes contre 73 textes AIPS Refdata officiels. |
| `tools/galien/cs_corr01.py` | Galien · corrections de niveau 2 des 5 stations CS pilotes (PR #40), 17.10.2026. Rejouable sur data/cs/stations.json.""" |
| `tools/galien/doses_glossaire_20261017.py` |  |
| `tools/galien/glo_migration_20261018.py` | Année de publication/mise à jour établie, sinon champ omis. |
| `tools/galien/glo_mono_g2_20261018.py` | Quatre nouveaux termes des monographies main, sans admission en baseline.""" |
| `tools/galien/glo_mono_g3_20261018.py` | Trois termes des nouvelles monographies, définitions provisoires explicites.""" |
| `tools/galien/glo_mono_g5_20261018.py` | Trois termes des monographies G5, sans source ni validation inventée.""" |
| `tools/galien/mono_g7_final.py` | Audit partiel G7/G8 : exclure les chiffres non CH/UE et les doses non encore auditées. |
| `tools/galien/prev_g1_corr.py` | Galien · audit G1 prévalence (S2.4, S2.5), 17.10.2026. Rejouable : extract NOT/TIP, ce script, inject NOT/TIP, prev_build. |
| `tools/galien/prev_g2_corr.py` | Galien · audit G2 prévalence (S2.7 dyspnée), 17.10.2026. Rejouable : extract NOT/TIP, ce script, inject NOT/TIP, prev_build. |
| `tools/galien/prev_g3_corr.py` | Galien · audit G3 prévalence (S3.1 douleur abdominale aiguë), 17.10.2026. Rejouable : extract NOT/TIP, ce script, inject, prev_build. |
| `tools/galien/prev_g4_corr.py` | Galien · audit G4 prévalence (G6 fièvre, F1.19 syncope), 17.10.2026. Rejouable : extract NOT/TIP, ce script, inject, prev_build. |
| `tools/galien/prev_g4_final.py` | Relecture G4 du 18.10.2026 : Limper, BASEL IX, HAS 2019, ESGE 2019, ESC 2018. |
| `tools/galien/prev_g5_inconnus.py` | Initialise le lot G5 sans inventer de chiffre ; ne remplace aucun lot existant.""" |
| `tools/galien/tip_corr01.py` | Galien · corrections de niveau 2 du champ 5 de TIP (PR #33, d253d06), 17.10.2026. |
| `tools/garde/appel.py` | Appel de Vial (R15) : une ligne sur « Pilote Codex » avec @vialdjoukang-spec (courriel GitHub), |
| `tools/garde/checkpoint.py` | Point de contrôle de chaque PR (R15) · .github/workflows/checkpoint.yml. |
| `tools/garde/codex_cloud_120.py` | Relais GitHub → Codex cloud : contrôle120s, baux communs, réponse vérifiée, sans faux démarrage.""" |
| `tools/garde/commun.py` | Garde-fous R15 · fonctions communes (zéro jeton, gratuit : GitHub Actions + gh CLI). |
| `tools/garde/fin.py` | Garde local de clôture : 0 = preuves réunies, 1 = reste à faire, 2 = erreur. |
| `tools/garde/permanence.py` | Veille bornée : passages120s pendant une fenêtre de20min ; les notifications ne prouvent aucune exécution IA.""" |
| `tools/garde/progres.py` | Garde du progrès (R15) · lancé toutes les CFG.cron_min minutes par .github/workflows/garde-progres.yml. |
| `tools/garde/recyclage.py` | Recyclage (R15) : PR ouvertes et branches sans commit depuis CFG.recyclage_inactif_min minutes. |
| `tools/garde/relance_bail.py` | Réservation CAS d'un lancement CLI, distincte d'une preuve de travail IA.""" |
| `tools/gestes/_squelette.py` | Génère gestes/<region>.html : squelette vide (2 colonnes, bandes, image, fenêtres), sans texte clinique.""" |
| `tools/gestes/squelette_abdomen.py` |  |
| `tools/gestes/squelette_cheville_pied.py` |  |
| `tools/gestes/squelette_coeur_vaisseaux.py` |  |
| `tools/gestes/squelette_constantes.py` |  |
| `tools/gestes/squelette_coude_main.py` |  |
| `tools/gestes/squelette_epaule.py` |  |
| `tools/gestes/squelette_ganglions.py` |  |
| `tools/gestes/squelette_genou.py` |  |
| `tools/gestes/squelette_geriatrie.py` |  |
| `tools/gestes/squelette_hanche.py` |  |
| `tools/gestes/squelette_meninge_gcs.py` |  |
| `tools/gestes/squelette_neuro_moteur.py` |  |
| `tools/gestes/squelette_neuro_nc.py` |  |
| `tools/gestes/squelette_peau.py` |  |
| `tools/gestes/squelette_pediatrie.py` |  |
| `tools/gestes/squelette_psychiatrie.py` |  |
| `tools/gestes/squelette_rachis.py` |  |
| `tools/gestes/squelette_seins.py` |  |
| `tools/gestes/squelette_tete_cou.py` |  |
| `tools/gestes/squelette_thorax.py` |  |
| `tools/gestes/squelette_tr_genital.py` |  |
| `tools/gestes/squelette_vasc.py` |  |
| `tools/html_check.py` | Validation HTML par cliquet : le validateur Nu ne doit signaler aucune erreur nouvelle. |
| `tools/inventaire_a_verifier.py` | Inventorie les champs À vérifier d'un instantané Git, sans modifier le contenu clinique.""" |
| `tools/jauge/binomes.py` | Deux jauges des binômes (prévalences, monographies), zéro jeton, déterministe. |
| `tools/json_inject.py` | Extrait ou réinjecte une constante JSON de app_v2.html (skill ssp-json-data). |
| `tools/links_changed.py` | Écrit les URL réellement nouvelles/modifiées ; une ligne minifiée ne rend pas nouveaux ses liens inchangés.""" |
| `tools/lyncee.py` | Lyncée · Janus · détecteur des termes médicaux non définis (contrôle G4, zéro jeton). |
| `tools/mandat/betta_controle.py` | BETTA : contrôle structurel des monographies DD d'un SSP (protocole 6 rubriques). |
| `tools/mandat/planifier.py` | File ALPHA → BETTA → GAMMA : propose du travail, ne rédige ni n'atteste un audit.""" |
| `tools/merge_shards.py` | Résout les conflits de data/ck/mono/*.json par fusion à 3 voies clé par clé (base, ours=HEAD, theirs=MERGE_HEAD).""" |
| `tools/mono_build.py` | Monographies des diagnostics différentiels (Hygie, 17.10.2026). |
| `tools/nc_svg_check.py` | Janus · contrôle des schémas de nerfs crâniens (assets/nc/*.svg) pour Dédale. |
| `tools/nc_svg_js.py` | Hermès · compile chaque schéma de nerf en chaîne JS insérable, pour que les couches fonctionnent aussi en file://. |
| `tools/porte.py` | Porte des étapes et état de pilotage (Codex). Gratuit, déterministe, sans dépendance. |
| `tools/predecesseurs_fusion.py` | Verrou des chaînes pour l'auto-fusion : le filet et le workflow suivent le même ordre.""" |
| `tools/prev_build.py` | Compile data/ck/prev.json : constante PRV de app_v2.html (ordre et chiffres) et assets/ck/prev.js (cadre, source). |
| `tools/prevalences/__init__.py` | Recherche documentaire des prévalences ; aucun chiffre clinique auto-publié.""" |
| `tools/prevalences/auditeur.py` | Auditeur statistique déterministe des candidats, sans validation clinique. |
| `tools/prevalences/consolider.py` | Réunit les résultats catégoriels sans perdre les relectures concurrentes.""" |
| `tools/prevalences/f.py` | Automate de recherche catégorie F ; --help pour les options.""" |
| `tools/prevalences/g.py` | Automate de recherche catégorie G ; --help pour les options.""" |
| `tools/prevalences/jauges.py` | Calculateur multi-secteur : python3 tools/prevalences/jauges.py [--distant]. |
| `tools/prevalences/moteur.py` | Moteur partagé des quatre automates, sans dépendance Python externe. |
| `tools/prevalences/o.py` | Automate de recherche catégorie O ; --help pour les options.""" |
| `tools/prevalences/rapport.py` | Centralisation des contrôles statistiques et synthèse PDF pour les jauges.""" |
| `tools/prevalences/relance_agent.py` | File de contrôle pour l'agent statistique via l'intégration Codex du dépôt. |
| `tools/prevalences/s.py` | Automate de recherche catégorie S ; --help pour les options.""" |
| `tools/prevalences/selection.py` | Sélection documentaire prudente entre estimations comparables. |
| `tools/propose_skills.py` | Proposition automatique de skills (gratuit, déterministe). |
| `tools/slim.py` | Vue de code sans données (skill ssp-extrait-cible). |
| `tools/tip_data.py` | Source TIP par SSP et asset classique synchrone, avec contrôle strict de dérive. |
| `tools/veille_relance.sh` | Veille de relance locale : relance Codex sur la mission enregistrée |
| `tools/visuel_reference.sh` | Automate Iris · adopte la référence visuelle proposée par la CI pour une demande de fusion (skill ssp-qualite-visuelle). |

Patches rejouables : 45 dans `tools/patches/` (skill ssp-patch).

## 2. Automates GitHub Actions (gratuits, dépôt public)

| Workflow | Rôle |
|---|---|
| `.github/workflows/appel-vial.yml` | Appel de Vial (R15) : étiquette attente-vial sur une PR ou une issue (ou lancement manuel, ou escalade de |
| `.github/workflows/auto-fusion.yml` | Auto-fusion après audit (label audit-ok). |
| `.github/workflows/checkpoint.yml` | Checkpoint R15 sur chaque PR : section « Automates actifs » réelle, aucune fausse fin d'étape en boucle, |
| `.github/workflows/ci.yml` | CI · Héphaïstos (socle) et Janus (contrôles). Chaque demande de fusion vers main |
| `.github/workflows/codex-cloud-120.yml` | Nouveau relais cloud : passages120s dans une fenêtre20min, cron GitHub5min ; pas de garantie temps réel. |
| `.github/workflows/file-fusion.yml` | File de fusion-publication planifiée (gratuite) : relance tools/file_fusion.sh toutes les 20 minutes. |
| `.github/workflows/garde-progres.yml` | Ancien garde en secours manuel désactivé ; relais actif : codex-cloud-120.yml. |
| `.github/workflows/liens-hebdo.yml` | Contrôle hebdomadaire des liens de l'app et de TIP externalisé, avec cache (Héphaïstos). |
| `.github/workflows/pages-apres-fusion.yml` | Relance Pages après chaque fusion vers main. |
| `.github/workflows/pages.yml` | Publication GitHub Pages (Héphaïstos) : l'application et ses croquis (assets/) sont publiés. |
| `.github/workflows/prevalences-recherche.yml` |  |
| `.github/workflows/veille-ve1.yml` | Veille ve1 (Argos, phase 1), tirée de tools/templates/veille-squelette.yml. |
| `.github/workflows/veille-ve2.yml` | Veille ve2 (Argos, phase 1), tirée de tools/templates/veille-squelette.yml. |
| `.github/workflows/visuel.yml` | Automate Iris · qualité visuelle (Janus, chantier Frontend Premium). |

## 3. Outils système gratuits

- `git` : présent
- `gh` : présent
- `python3` : présent
- `node` : présent
- `npx` : présent
- `jq` : présent
- `flock` : présent
- `pdftotext` : présent
- `curl` : présent
- `codex` : absent
- `crontab` : absent

## 4. Skills du dépôt (`docs/skills/`)

- `ssp-aips-verbatim` : Vérifier des extraits de doses contre les téléchargements officiels Refdata, sans confondre conformité documentaire et validation clinique.
- `ssp-audit-medical` : Lis ce skill avant toute fusion qui touche un contenu clinique : l’audit
- `ssp-chaine-clinique` : Lis ce skill avant d’écrire un contenu de la partie CK : geste, sémiologie,
- `ssp-construction-ck` : Reconstruire les monographies, prévalences et doses après un lot ou une fusion, sans modifier les fichiers générés à la main.
- `ssp-continuite` : Lis ce skill au début de chaque session, à chaque porte d’étape et dès que ton
- `ssp-extrait-cible` : Lis ce skill avant toute lecture du fichier de travail app_v2.html : il
- `ssp-fusion-patch` : Lis ce skill quand main a avancé pendant ton chantier : il intègre main dans ta branche sans jamais
- `ssp-images-licence` : Lis ce skill avant d’ajouter une image : les images cliniques sont réelles,
- `ssp-json-data` : Lis ce skill dès que tu modifies une constante de données de app_v2.html (TIP,
- `ssp-patch` : Lis ce skill avant toute modification du code de app_v2.html : chaque
- `ssp-pilotage-codex` : Lis ce skill au début de chaque session Codex : porte des étapes, veille de relance, file de fusion, modèle des tâches répétitives.
- `ssp-posologie-suisse` : Lis ce skill dès qu’un texte mentionne un médicament ou une dose : chaque dose
- `ssp-prevalences-automates` : Rechercher les fréquences CH/Europe par catégorie SSP, afficher les jauges ou reprendre la file de l’agent statistique.
- `ssp-qa-regression` : Lis ce skill pour contrôler une branche avant fusion : il fixe la référence
- `ssp-qualite-visuelle` : Lis ce skill avant de toucher à la présentation de app_v2.html (CSS, thèmes, typographie) et avant
- `ssp-revue-diff` : Lis ce skill pour relire une demande de fusion ou ton propre travail : la
- `ssp-schema-nerf` : Lis ce skill avant de produire ou de modifier un schéma de nerf crânien : le
- `ssp-signe-infobulle` : Lis ce skill dès qu’un texte de l’application emploie un signe, un syndrome ou
- `ssp-synthese-locale` : Lis ce skill avant de construire la « Synthèse locale » d’un module d’examen :
- `ssp-tests` : Lis ce skill après chaque patch ou chaque injection de données : tu vérifies
- `ssp-verite` : Lis ce skill avant de livrer tout texte visible et avant chaque fusion :
- Propositions automatiques : `docs/skills/PROPOSITIONS.md` (`python3 tools/propose_skills.py`).

## 5. Serveurs MCP et connecteurs de Codex

Observé le 20.10.2026 : connecteur GitHub disponible (lecture/écriture du dépôt, PR et Actions) ; CLI `gh` effectivement utilisée pour P0. Connecteur cloud-environment : état du réseau et des accès. Recherche web disponible pour les lectures documentaires ultérieures. Aucun MCP médical ni navigateur MCP présumé. Les connecteurs Pages et Drive ne servent pas ce mandat.

## 6. Skills et outils propres à Codex

Outils réellement accessibles : exécution shell/Python/JavaScript, édition de fichiers, Git, `gh`, agents spécialisés et skills du dépôt. P0 utilise shell, scripts déterministes et deux agents indépendants pour les audits techniques. Le skill `cloud-environment-runtime` a été lu pour le réseau. Les outils web serviront aux lectures scientifiques P1–P4 ; Playwright est vérifié par la CI. Aucun outil image utilisé. Les modèles de chaque agent sont consignés selon leur exécution réelle, sans attestation fabriquée.

- `agent cloud Cursor` : agent de codage cloud Cursor (ouverture des pull requests de ce dépôt).

## 7. Droits de fusion-publication

```
{"admin":true,"auto_merge":true,"merge_commit":true,"push":true,"squash":false}
{"checks":["garde","html","tests","visuel"],"enforce_admins":true,"strict":true}
```
Référence historique ci-dessus, pas une observation courante des protections. Le 20.10.2026, API dépôt : admin/maintain/push=true et auto_merge=true. La lecture de la protection retourne HTTP 403 « Resource not accessible by integration » ; aucune règle modifiée. CI exacte et contrôles minimaux sont exigés indépendamment de cette limite.

## 8. Modèle des tâches répétitives

Ordre de Vial : toute tâche répétitive utilise **GPT 6 Luna** (`gpt-6-luna`). Sinon : le modèle le moins cher disponible, noté dans ETAT.md.
