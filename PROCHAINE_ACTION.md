# PROCHAINE ACTION (écrit par tools/veille_relance.sh, ne pas éditer à la main)

Mis à jour : 18.10.2026 00:45 CEST

> Ordre de Vial : commence par l'Étape 0. Lis CONTINUATION.md en entier, coche chaque case de la porte d'ETAT.md, puis `python3 tools/porte.py verifier0` et `python3 tools/porte.py terminer`. Aucun contenu avant.

État : `{"etape_courante":0,"statut":"en_cours","lot":1}`


---

# CATALOGUE · outils gratuits, automates, MCP et skills (Étape 0)

Généré par `python3 tools/catalogue.py`, puis complété par Codex. À présenter avant toute étape de contenu.

## 1. Scripts du dépôt (gratuits, déterministes)

| Script | Rôle |
|---|---|
| `tools/_app.py` | Fonctions communes : localisation d'une constante JS de premier niveau par str.find. |
| `tools/aletheia.py` | Alétheia · Janus · vérité des sources : doses (G1), source et date (G2), domaines (G3). |
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
| `tools/check_hash.py` | Garde I1 : l'empreinte SHA-256 de orig/app.html ne doit jamais changer.""" |
| `tools/ck_build.py` | Atlas · compilateur des données CK : data/ck/*.json → assets/ck/*.js (contrôle G5). |
| `tools/ck_common.py` | Atlas et Janus · fonctions communes aux outils CK (compilateur, Lyncée, audit de niveau 1). |
| `tools/cs_build.py` | Chiron · compilateur des stations CS : data/cs/*.json → assets/st/*.js. |
| `tools/dedale/annoter.py` | Dédale-A · composition des 3 vues annotées d'un nerf crânien (face, profil, trois quarts). |
| `tools/dedale/crane.py` | Dédale-C · crâne 3D au crayon (traits pleins à graisse hiérarchisée) pour les 3 vues d'un nerf crânien. |
| `tools/dedale/freestyle.py` | Dédale-3D · rendu au crayon des vues d'un nerf crânien à partir du modèle Z-Anatomy. |
| `tools/dedale/masques.py` | Dédale-M · silhouettes pleines des territoires (masques) à partir du modèle Z-Anatomy, en mémoire réduite. |
| `tools/dedale/trace.py` | Dédale-T · plan du nerf au crayon à partir d'une planche de Gray (domaine public), par automate. |
| `tools/dedale/verifier.py` | Dédale-V · contrôle des schémas de nerfs crâniens (CI, zéro jeton). |
| `tools/file_fusion.sh` | File de fusion-publication automatique (gratuit : gh + git + python3). Lancé par tools/veille_relance.sh |
| `tools/html_check.py` | Validation HTML par cliquet : le validateur Nu ne doit signaler aucune erreur nouvelle. |
| `tools/jauge/binomes.py` | Deux jauges des binômes (prévalences, monographies), zéro jeton, déterministe. |
| `tools/json_inject.py` | Extrait ou réinjecte une constante JSON de app_v2.html (skill ssp-json-data). |
| `tools/links_changed.py` | Écrit dans links.txt les URL ajoutées ou modifiées dans app_v2.html et data/ck/ (sources CK) depuis <base>.""" |
| `tools/lyncee.py` | Lyncée · Janus · détecteur des termes médicaux non définis (contrôle G4, zéro jeton). |
| `tools/merge_shards.py` | Résout les conflits de data/ck/mono/*.json par fusion à 3 voies clé par clé (base, ours=HEAD, theirs=MERGE_HEAD).""" |
| `tools/mono_build.py` | Monographies des diagnostics différentiels (Hygie, 17.10.2026). |
| `tools/nc_svg_check.py` | Janus · contrôle des schémas de nerfs crâniens (assets/nc/*.svg) pour Dédale. |
| `tools/nc_svg_js.py` | Hermès · compile chaque schéma de nerf en chaîne JS insérable, pour que les couches fonctionnent aussi en file://. |
| `tools/porte.py` | Porte des étapes et état de pilotage (Codex). Gratuit, déterministe, sans dépendance. |
| `tools/prev_build.py` | Compile data/ck/prev.json : constante PRV de app_v2.html (ordre et chiffres) et assets/ck/prev.js (cadre, source). |
| `tools/propose_skills.py` | Proposition automatique de skills (gratuit, déterministe). |
| `tools/slim.py` | Vue de code sans données (skill ssp-extrait-cible). |
| `tools/veille_relance.sh` | Veille de relance permanente (gratuite) : détecte la fin de l'étape courante et relance Codex |
| `tools/visuel_reference.sh` | Automate Iris · adopte la référence visuelle proposée par la CI pour une demande de fusion (skill ssp-qualite-visuelle). |

Patches rejouables : 19 dans `tools/patches/` (skill ssp-patch).

## 2. Automates GitHub Actions (gratuits, dépôt public)

| Workflow | Rôle |
|---|---|
| `.github/workflows/auto-fusion.yml` | Auto-fusion après audit (label audit-ok). |
| `.github/workflows/ci.yml` | CI · Héphaïstos (socle) et Janus (contrôles). Chaque demande de fusion vers main |
| `.github/workflows/file-fusion.yml` | File de fusion-publication planifiée (gratuite) : relance tools/file_fusion.sh toutes les 20 minutes. |
| `.github/workflows/liens-hebdo.yml` | Contrôle hebdomadaire de tous les liens d'app_v2.html, avec cache (Héphaïstos). |
| `.github/workflows/pages-apres-fusion.yml` | Relance Pages après chaque fusion vers main. |
| `.github/workflows/pages.yml` | Publication GitHub Pages (Héphaïstos) : l'application et ses croquis (assets/) sont publiés. |
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
- `codex` : présent
- `crontab` : absent

## 4. Skills du dépôt (`docs/skills/`)

- `ssp-audit-medical` : Lis ce skill avant toute fusion qui touche un contenu clinique : l’audit
- `ssp-chaine-clinique` : Lis ce skill avant d’écrire un contenu de la partie CK : geste, sémiologie,
- `ssp-continuite` : Lis ce skill au début de chaque session, à chaque porte d’étape et dès que ton
- `ssp-extrait-cible` : Lis ce skill avant toute lecture du fichier de travail app_v2.html : il
- `ssp-fusion-patch` : Lis ce skill quand main a avancé pendant ton chantier : il intègre main dans ta branche sans jamais
- `ssp-images-licence` : Lis ce skill avant d’ajouter une image : les images cliniques sont réelles,
- `ssp-json-data` : Lis ce skill dès que tu modifies une constante de données de app_v2.html (TIP,
- `ssp-patch` : Lis ce skill avant toute modification du code de app_v2.html : chaque
- `ssp-pilotage-codex` : Lis ce skill au début de chaque session Codex : porte des étapes, veille de relance, file de fusion, modèle des tâches répétitives.
- `ssp-posologie-suisse` : Lis ce skill dès qu’un texte mentionne un médicament ou une dose : chaque dose
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

```
No MCP servers configured yet. Try `codex mcp add my-tool -- my-command`.
```

## 6. Skills et outils propres à Codex

Inventaire réel de cette session (17.10.2026 UTC) :

- Exécution : Bash, Python, git/gh, apply_patch, lecture d'images ; toutes étapes. Playwright Python est installé ; Chromium est en cours d'installation (tests et étape 2).
- Serveur MCP exposé à la conversation : `codex_apps`. Aucun serveur configuré dans le CLI local (`codex mcp list`). Ces deux portées sont distinctes.
- GitHub : 89 outils (lecture dépôt/PR/CI, branches, commits, PR, fusion, auto-merge, relance CI), étapes 0–17. Le CLI gh authentifié est le moyen retenu ; aucun jeton n'est copié.
- Cloud environment : état et disponibilité réseau, étape 0 et diagnostics. Skill appliqué : cloud-environment-runtime.
- Autres familles MCP disponibles : Automations (5), AXA (3), ChatGPT Spaces (40), Document Control (3), Gmail (21), Google/Drive (60), hotline (1), Pets (11), plugin management (6), safety (5), recherche (1), Sites (25). Hors périmètre clinique : aucune connexion ou écriture supplémentaire nécessaire.
- Skills disponibles : 27 modèles OpenAI (documents, présentations, tableurs), Pages (write-page, maintain-space, organize-space, manage-schedules), Sites, Google Drive/Docs/Sheets/Slides/comments, plugin-management, Pets (create-pet, pets, update-pet), cloud-environment-runtime. Seul ce dernier sert directement ; les skills du dépôt pilotent le chantier.
- Imagegen est disponible mais les images du projet doivent être réelles et licenciées : employer les sources autorisées et ssp-images-licence à l'étape 13.
- Sous-agents : modèle gpt-6-luna sélectionnable pour les tâches répétitives R8 ; le CLI local a échoué à l'authentification lors du test, donc ne pas annoncer sa relance autonome comme opérationnelle. Le modèle courant traite les décisions et réparations.
- Recherche réseau : curl/gh et connecteur de recherche ; sources CH/UE et AIPS officielles seulement pour le contenu (étapes 3–15), jamais Compendium.

Automates gratuits utiles : CI existante, garde d'empreinte, tests Playwright sous flock, audit G1–G8, Lyncée, lychee hebdomadaire et liens modifiés, compilation --check, propositions de skills, veille locale toutes les 180 s, file GitHub toutes les 20 min. `act` et pre-commit ne sont pas installés : la CI et les commandes locales couvrent ces usages sans nouvelle dépendance.

## 7. Droits de fusion-publication

```
{"admin":true,"auto_merge":true,"merge_commit":true,"push":true,"squash":false}
{"message":"Resource not accessible by integration","documentation_url":"https://docs.github.com/rest/branches/branch-protection#get-branch-protection","status":"403"}
```
Attendu : admin=true, auto_merge=true, merge_commit=true ; protection : garde, html, tests, visuel, strict.

## 8. Modèle des tâches répétitives

Ordre de Vial : toute tâche répétitive utilise **GPT 6 Luna** (`gpt-6-luna`). Sinon : le modèle le moins cher disponible, noté dans ETAT.md.

## 9. Affectation aux étapes et propositions examinées

- 0–2, 17 : porte, catalogue, propose_skills, veille, file_fusion, jauge, CI/Pages, contrôle d'empreinte, tests et captures.
- 3, 8 : prev_build + audit/prevalence ; 4–5, 9 : merge_shards + mono_build.
- 6, 10 : doses_check sur les branches de doses, AIPS officielle ; 7, 11 : ck_build + Lyncée.
- 12 : json_inject + patches rejouables + audit ; 13 : nc_svg_js/nc_svg_check ; 14 : cs_build ; 15–16 : outils précédents selon le diff.
- Skill créé : ssp-construction-ck (mono_build, prev_build, doses_check). etapes.json est un fichier, pas une commande : candidat écarté. Commits d'audit déjà couverts par ssp-audit-medical ; références visuelles par ssp-qualite-visuelle.
- Lecture de la protection via l'intégration : HTTP 403 ; conserver intégralement la protection, sans prétendre l'avoir inspectée. Les droits du dépôt sont confirmés ci-dessus.
