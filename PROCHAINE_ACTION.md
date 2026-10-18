## G10 lot4 · douleurs nociceptives · 18.10.2026 22:33 Europe/Zurich
État : reprise depuis main 4edba7f ; #114 et #115 fusionnées, publication clinique précédente vérifiée. Deux monographies (douleur-nociceptive-somatique, douleur-nociceptive-viscerale) et cinq définitions : 257/2287 sur branche, G10 9/14, glossaire 597. Prévalences 45/2587 et doses AIPS 98 lignes inchangées. Contrôles de données G1–G8, constructeurs et Lyncée verts ; CI de la tête exacte, fusion et publication de ce lot encore requises.
Prochaine : terminer cette intégration puis radiculalgie et polyneuropathie douloureuse ; ensuite douleur neuropathique centrale, céphalée primaire et composante affective. Étape 8 associée au lot par le plan commun ; S1.3–S1.6, S8 après #37 et Panacée O7.14–O7.12 restent dus. Aucune fin de boucle.
Sources : guide HUG Antalgie novembre 2023, pages ciblées 3–9,14–15,19–20,31 ; stratégie abdomen chronique digestif 2023 pages3–6 ; aide-mémoire palliatif du28.03.2025. Lecture datée18.10.2026 ; sources brutes conservées seulement en work/.
Pièges : catégorie somatique non réduite à la lombalgie ; bilan abdominal chronique non étendu à toute douleur viscérale. Alias globaux somatique et irradiation retirés car ils détournaient des sens hors douleur. Ni taux de population/sous-groupe ni dose HUG importés. Aucune validation clinique humaine revendiquée.
Veille : workflow actif, cron configuré10min ; à20:28UTC dernière garde observée39159622388 (push19:37), recherche39159637648 réussie. Pas de preuve de déclenchement effectif toutes les10min : ne pas promettre cette régularité ni une rédaction autonome dans une session fermée. AuthCLI401, relais MCP fonctionnel ; aucune authentification copiée.
À vérifier : prévalence et sex-ratio des deux mécanismes, posologies AIPS, cause précise selon présentation ; binaire Playwright absent puis navigation file:// refusée avec Chromium système ; suite navigateur complète laissée à la CI exacte.

## G10lot3 · reprise après coordination et PDFoutils · 18.10.2026 Europe/Zurich
État : coordination#112fusionnée2262309 et amorçage#113fusionnéf7e52c6 ; garde10min39159622388 réussie, rechercheG/S/F/O39159637648 lancée. InventairePDF demandé livré et vérifiéHTTP200 ; état daté, non confondu avec synthèsePDFerreurs. CLIauth401 ; MCPGitHub et lecturepublique fonctionnent, aucun secret copié.
Contenu : deux monographies rédigées et relues, céphalée en coup de tonnerre et douleur cancéreuse ; cinq définitions et cinq sourcesHUG, dont protocole2024 inspecté en images par auteur et auditeur. Branche255/2287, G10 7/14, glossaire592, référence3559 ;45/2587 et98lignesAIPS inchangées. Registre couplé enrichi de ces deux relectures, réserves conservées ; aucun couple clinique certifié.
Prochaine : intégrer après CIexacte, vérifierPages, puis G10douleurs nociceptives somatique et viscérale, radiculalgie, polyneuropathie douloureuse, douleur neuropathique centrale, céphalée primaire et composante affective. Prévalences liées au lot courant ; S1.3–S1.6, PanacéeO7.14–O7.12 et reliquats conservés.
Pièges : scannerprécoce sousconditions et relecture spécialisée ; anévrisme sanssaignement ne prouve pas rupture ; délaiPL ne retarde pas soins. Douleur nouvelle non automatiquement progression tumorale ; antalgie adaptée et fonctions rénale/respiratoire prises en compte. Ni fréquence de sous-groupe ni doseHUG transposée. Aucun accordmédical humain revendiqué, aucune fin de boucle.

## Coordination8/9 · veille10min · 18.10.2026 Europe/Zurich
État : dispositif commun implémenté, compteur par diagnostic et occurrenceSSP, registre lié aux empreintes, file de maturation et ordonnanceur régulé. Monographies253/2287 et prévalences45/2587 inchangées ; deux relectures monographiques initialisées, aucune prévalence rétrovalidée. Recherches ciblées SPILF/SFMV ajoutées, coupe-circuit300s et exemples documentaires prioritaires dans le PDF. Veille10min, notifications20min, recherches au plus4h,2DD/catégorie si file≥200 sinon8,2catégories simultanées/budget180s. Contrelecture indépendante favorable après corrections,117tests prévalences verts ; CI/fusion/activation exactes requises.
Prochaine : après intégration et lancement réels, reprendre exactement G10 céphalée en coup de tonnerre puis douleur cancéreuse. Étape8 reste liée ; le succès d’une relance n’est pas une preuve d’exécution d’agent. Pas de clôture de boucle.
Pièges : ne pas partager une prévalence entre SSP, ne pas confondre structure et maturité documentaire, ne pas fermer à100% arrondi. Un plan corrompu interdit le dispatch mais ne supprime pas la garde. Voir docs/coordination-8-9.md.

# PROCHAINE ACTION (écrit par tools/veille_relance.sh, ne pas éditer à la main)

Mis à jour : 18.10.2026 15:07 UTC

> Ordre de Vial : continue avec l'étape suivante. Étape 8, lot 8 : Prévalences en rouge des 248 SSP (22 SSP sans différentiel). Lis AGENTS.md, puis CONTINUATION.md section « Étape 8 », ETAT.md et PROCHAINE_ACTION.md ; lance `python3 tools/porte.py commencer 8` ; travaille ; à la fin `python3 tools/porte.py terminer`. Modèle : GPT 6 Luna (gpt-6-luna). Ne t'arrête jamais devant un obstacle : consigne-le et passe à la suite.

État : `{ "etape_courante": 8, "statut": "en_cours", "lot": 8, "maj": "2026-10-18T15:07:06+00:00", "en_attente": {  "8": {   "motif": "Lot 7 : G15, G16, S1.1 et S1.2, 54 fréquences explicitement inconnues ; 45/2587 inchangé. CI exacte et fusion requises.",   "dernier_lot": 101,   "prochain_lot": [    "S1.3",    "S1.4",    "S1.5",    "S1.6"   ],   "attente_s8": "S8 après audit #37 ; ne pas dupliquer ou inventer ses différentiels."  },  "9": {   "motif": "#102 : psoriasis et urticaire chronique, six définitions de soutien ; 244/2287 monographies dans le lot. Critères formels psoriasis et posologies AIPS encore À vérifier. Relire le statut de fusion et les CI dans GitHub ; cinq G9, G10 et Panacée restent dus.",   "pr_g9": 91,   "tests_g9": {    "head": "7af1a77",    "reussis": 278,    "total": 278,    "journal_local": "/tmp/oef-g9-tests.log"   },   "pr_complement": 98,   "pr_gales": 100,   "prochains_g9": [    "lymphome-de-hodgkin",    "pemphigoide-bulleuse-etendue",    "polyglobulie-de-vaquez",    "dermatite-atopique",    "lichen-plan"   ],   "pr_dermatoses": 102  },  "10": {   "motif": "98 lignes / 73 documents relus sur branches ; aucune nouvelle dose non lue ajoutée. DigiFab retrouvé par recherche officielle et accès direct HTTP 200, révision 02/2026 ; document anglais converti de cinq pages à deux colonnes. Extraction structurée/audit restant, aucune formule aplatie transposée : audit/DIGIFAB-RECHERCHE-20261018.json. Pas de fin de boucle."  },  "11": {   "motif": "Branche dermatose : six définitions de soutien, 569 entrées, référence Lyncée 3563. Zéro terme nouveau non défini, boucle ouverte."  },  "12": {   "motif": "#83 fusionnée : 72 titres critiques restaurés, contrôles requis verts et 278 tests. Correctifs Fermer #84, calendrier et disposition #65, cibles Notions #68 fusionnés. Audit transversal encore dû ; correction terminologique cardioverter sourcée dans cette relève. Proposition potentiellement critique #88 attente-vial, conduite hors main. Actualisation cloud : accord de Vial reçu et #88 fusionnée dans main aacfff7 ; audit transversal toujours dû.",   "prs": []  },  "13": {   "motif": "#39 fusionnée (17cf10a), entrées sourcées conservées. Prototype #80 en brouillon, attente-vial. Dédale-V : zéro échec après svgo 4.0.0, mais croquis non approuvé et sources/style à confirmer.",   "prs": [    80   ]  },  "14": {   "motif": "Cinq stations pilotes présentes ; aucune nouvelle approbation Vial reçue. Conserver valide_par_vial=false ; aucune nouvelle série lancée avant leur relecture, conformément à CONTINUATION."  },  "15": {   "prs": [    81   ],   "motif": "#41 fusionnée (5de965f) : 17 remplacements sur 16 fiches, après #83, registres réunis et contrôles requis verts. #81 lot 3 reste en brouillon, audit médical complet encore dû."  },  "16": {   "motif": "#32 fusionnée (617878e) après adoption examinée et contrôles requis verts. Nouvelle référence CI et procédé runner intégrés. #37 : 60 DD S8 rejoués, audit médical final restant. #16 fermée avec motif et branche conservée.",   "prs": [    37   ]  },  "17": {   "motif": "Clôture refusée : branche dermatose 45/2587 fréquences, 244/2287 monographies, 98 lignes AIPS ; cinq G9, G10, Panacée, audits #37/#81, croquis et stations restent dus.",   "cloture_validee": false,   "tests_main_snapshot": {    "sha": "42a432d3e5ddb657e8b9cfba35c9340189222761",    "reussis": 276,    "total": 276,    "journal_local": "/tmp/oef-main-apres-correction.log"   },   "publication": {    "date": "2026-10-18T01:14:46.131018+00:00",    "sha": "51cb2e50d478a55f3ead1a3a238def32ae0c7c98",    "http": 200,    "main_sha256": "9e4720c6ce86056e4648eaa8744fe183479d9ddbf6419f1bb13ad60d8a800969",    "public_sha256": "9e4720c6ce86056e4648eaa8744fe183479d9ddbf6419f1bb13ad60d8a800969",    "identique": true   },   "publication_assets": {    "date": "2026-10-18T01:15:06.641386+00:00",    "sha": "51cb2e50d478a55f3ead1a3a238def32ae0c7c98",    "fichiers": [     {      "fichier": "assets/mono/mono-s.js",      "http": 200,      "identique": true,      "main_sha256": "690e9873851ae2edaa1c6c4e501406c8fde6bd0999f2349263d898a88517d1aa",      "public_sha256": "690e9873851ae2edaa1c6c4e501406c8fde6bd0999f2349263d898a88517d1aa"     },     {      "fichier": "assets/ck/prev.js",      "http": 200,      "identique": true,      "main_sha256": "7d3a67e4ef067e590a2436b4c393177184a263680f1c4311a162df6ed882576c",      "public_sha256": "7d3a67e4ef067e590a2436b4c393177184a263680f1c4311a162df6ed882576c"     },     {      "fichier": "assets/ck/glo-index.js",      "http": 200,      "identique": true,      "main_sha256": "7ef4298a44e9e08d031a4a22e914aba68ac1123b8373e89d8cd9cd248bc63c66",      "public_sha256": "7ef4298a44e9e08d031a4a22e914aba68ac1123b8373e89d8cd9cd248bc63c66"     },     {      "fichier": "assets/ck/src.js",      "http": 200,      "identique": true,      "main_sha256": "228eb866bc50fb8771691230e303c7097c5af6d139a333414200e021e1d8e176",      "public_sha256": "228eb866bc50fb8771691230e303c7097c5af6d139a333414200e021e1d8e176"     }    ]   },   "publication_controle": {    "date": "2026-10-18T02:54:35.358687+00:00",    "sha": "6bbbde73712209f1d118ca9d73e0c19219578258",    "fichiers": [     {      "fichier": "index.html",      "http": 200,      "identique": true,      "main_sha256": "fadb5760c516e9bb35a10b7baa58dfe5a8b83b0b0549b1a563cc822dddf1bff6",      "public_sha256": "fadb5760c516e9bb35a10b7baa58dfe5a8b83b0b0549b1a563cc822dddf1bff6"     },     {      "fichier": "app_v2.html",      "http": 200,      "identique": true,      "main_sha256": "fadb5760c516e9bb35a10b7baa58dfe5a8b83b0b0549b1a563cc822dddf1bff6",      "public_sha256": "fadb5760c516e9bb35a10b7baa58dfe5a8b83b0b0549b1a563cc822dddf1bff6"     },     {      "fichier": "assets/mono/mono-s.js",      "http": 200,      "identique": true,      "main_sha256": "0e5972a91859c004917c2bafc57e867fb3dd631b678290899cb067e1013282c3",      "public_sha256": "0e5972a91859c004917c2bafc57e867fb3dd631b678290899cb067e1013282c3"     },     {      "fichier": "assets/ck/prev.js",      "http": 200,      "identique": true,      "main_sha256": "9900cf0476373d11f8534b7cca7e9cb636a9e097b413125637bc2904ec8b351b",      "public_sha256": "9900cf0476373d11f8534b7cca7e9cb636a9e097b413125637bc2904ec8b351b"     },     {      "fichier": "assets/ck/glo-index.js",      "http": 200,      "identique": true,      "main_sha256": "0f3a2d27fe537290ebfe0256e05d51109e016ff3f4f67fcce63d04cbf857e220",      "public_sha256": "0f3a2d27fe537290ebfe0256e05d51109e016ff3f4f67fcce63d04cbf857e220"     },     {      "fichier": "assets/ck/src.js",      "http": 200,      "identique": true,      "main_sha256": "c44d05b190fc85f3b7072e68e89aef548806adf8f0401a8560637729103bf35c",      "public_sha256": "c44d05b190fc85f3b7072e68e89aef548806adf8f0401a8560637729103bf35c"     }    ]   },   "tests_ci_snapshot": {    "pr": 41,    "head": "35d25e03a9b19922c8f88530c7e5e2a523eac450",    "suite": 278,    "ci": 39090117080,    "visuel": 39090117181   },   "publication_reprise": {    "sha": "774de7427d4fcd6b6071ecdf5176fd4f2b26219b",    "workflow": 39137471916,    "resultat": "succès Pages après #101 ; accès public direct encore CONNECT 403 dans cette session, comparaison octet par octet non vérifiée."   }  } }, "dernier_controle_etape": 17, "cloture_validee": false, "etapes_validees_apres_attente": {  "3": {   "prs": [    43,    44,    45,    58,    47   ],   "resultat": "toutes fusionnées"  },  "5": {   "prs": [    60,    62   ],   "resultat": "toutes fusionnées ; incident ordre 62 avant 60 conservé"  },  "7": {   "prs": [    65,    68   ],   "resultat": "fusionnées dans cet ordre ; 543 entrées, référence 3567 ; cibles 24 px, adoption examinée, contrôles requis verts"  },  "4": {   "prs": [    50,    53,    54,    64,    49   ],   "resultat": "toutes fusionnées ; #64 observée à 11:59 UTC"  },  "6": {   "prs": [    59,    61,    67,    70   ],   "resultat": "toutes fusionnées ; accords Vial lus, audits et CI conservés. Aciclovir, KCl et RhD inconnu gardent leurs réserves explicites."  } }, "signalements_attente_vial": [], "accords_vial_20261018": {  "88": {   "source": "https://github.com/vialdjoukang-spec/organigramme-examen-federal/pull/88",   "accord_recu": true,   "audit_final": "requis",   "fusion": "observée sur main aacfff7, tête d4fa7f7"  },  "64": {   "source": "https://github.com/vialdjoukang-spec/organigramme-examen-federal/pull/64",   "accord_recu": true,   "audit_final": "fusion antérieure observée ; pas de nouvel audit primaire revendiqué dans cette reprise",   "fusion": "observée 427f557f1bbd0091266bdabea4b5bfde5385ab56"  },  "67": {   "source": "https://github.com/vialdjoukang-spec/organigramme-examen-federal/pull/67",   "accord_recu": true,   "audit_final": "recontrôle consigné et CI requise verte sur la tête fusionnée",   "fusion": "observée a5ef3b5bebdc0e4002ca06602b2dd3ea97bc215c"  },  "70": {   "source": "https://github.com/vialdjoukang-spec/organigramme-examen-federal/pull/70",   "accord_recu": true,   "audit_final": "recontrôle consigné et CI requise verte sur la tête fusionnée",   "fusion": "observée a27fb1da70d71387331c15fffdc42dee43d8ff8e"  } }, "ordre_fusion_demande": [  88,  64,  91,  67,  70 ], "reprise_cloud_20261018": {  "branches_poussees": {   "64": "fusionnée 427f557f1bbd0091266bdabea4b5bfde5385ab56",   "91": "fusionnée d0c0dfa02d9a348df6ecf74d084cdd28c52f1278",   "67": "fusionnée a5ef3b5bebdc0e4002ca06602b2dd3ea97bc215c",   "70": "fusionnée a27fb1da70d71387331c15fffdc42dee43d8ff8e"  },  "validation_locale": "G1–G8 réussis sur les cinq branches après corrections ; CK et comparateur AIPS réussis sur #67",  "blocage": "Accès GitHub/API, EDF, HUG et documents AIPS rétablis ; Oxford 403, recherche Europe PMC expirée, navigateur file:// et lecture Pages github.io bloqués.",  "configuration": "Accès réellement testés, voir audit/RESEAU-REPRISE-20261018.json sur #98.",  "boucles_8_9": "#97 fusionnée, 60 fréquences inconnues explicites ; #98 contient deux propositions G9. Boucles ouvertes, aucune fréquence nouvelle." }}`

Échecs de fusion récents (journal/echecs_fusion.md) :

- 18.10.2026 · lot 5 : Europe PMC répond par une coquille HTML et ses URL API testées 404/530 ; recherche directe du journal européen utilisée, sans prétendre avoir lu un texte Europe PMC. Source Brest enregistrée par son DOI canonique HTTP 200, sans changer la liste des domaines admis. Conflits de sources/rapport entre #99 et #100 réunis par id et sections, assets reconstruits. Contrôles non affaiblis.
- 18.10.2026 · Recontrôle après modification réseau par Vial : API GitHub, texte EDF et HUG HTTP 200 ; site public github.io toujours CONNECT 403 dans cette session, dont les observations ne contiennent pas ce domaine. Aucune application de la configuration présumée. DOI HypnoLaus renvoie vers Elsevier refusé : aucun chiffre repris. Poursuite du contenu.
- 18.10.2026 Europe/Zurich · lot 7 : Chromium Playwright absent localement, suite arrêtée avant exécution. CI navigateur requise sans modifier les assertions. Les quatre URL HUG initialement supposées ont répondu 404 ; navigation depuis l’index officiel vers les documents réels. Pages désormais HTTP 200 et app identique à bfa43f2 : ancien blocage levé sur cette URL.

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

## Ajouts de la session (18.10.2026 UTC)
- `tools/aips_verbatim.py` et ses 3 tests : conformité documentaire aux textes Refdata ; aucune validation clinique implicite.
- Skill local `docs/skills/ssp-aips-verbatim/SKILL.md` : unités Symbol, cache et limites de la comparaison.
- #82 : contrôle testé des prédécesseurs de fusion ; #84 : fermeture d’infobulle reproduite et corrigée.

## Ajouts de la reprise du 18.10.2026

- `python3 tools/inventaire_a_verifier.py --ref origin/main --sortie audit/RESTE_A_VERIFIER_20261018.json` : inventaire déterministe des champs explicitement marqués, sans modifier le contenu clinique ; conserve SHA et pointeur de chaque champ. N’est pas un audit ni un critère de clôture.
- #65 : patches rejouables `0030-glossaire-commandes-calendrier.py` et `0031-glossaire-flux-grille-flex.py` ; commandes de sélection préservées, liens sans déplacement des grilles/flex. Deux régressions ajoutées, suite portée à 278.
- `Visuel` propose depuis #32 l’entrée manuelle `adopter_pr` pour exécuter le script habituel d’adoption sur runner quand les artefacts sont inaccessibles localement ; tête/branche/base vérifiées, CI après adoption toujours obligatoire.

- #68 : `0032-cibles-notions.py` porte les liens et boutons Notions à 24 px sans nouvelle règle CSS dans le corps ; adoption de référence examinée sur runner puis CI complète verte.

## Garde-fous R15 (GitHub Actions, gratuits, indépendants de tout PC)

| Automate | Rôle |
|---|---|
| `garde-progres.yml` · `tools/garde/progres.py` | Toutes les 10 min : mesure le contenu de main ; STALL (30 min sans contenu) → `@codex` sur « Pilote Codex » ; 2 stalls → courriel à Vial. |
| `tools/garde/recyclage.py` | PR sans commit depuis 60 min → `@codex reprends ou ferme avec motif` (ne ferme rien). |
| `checkpoint.yml` · `tools/garde/checkpoint.py` | Chaque PR : « Automates actifs », pas de fausse fin d'étape en boucle, pas de dose sans ligne AIPS. `--inventaire` : automates actifs. |
| `appel-vial.yml` · `tools/garde/appel.py` | Étiquette `attente-vial` → courriel à Vial + `@codex` continue ailleurs. |
| `tools/garde/config.json` | Seuils en minutes. |

## Inventaire réel · reprise du 18.10.2026 Europe/Zurich
Cette session utilise exec_command (git/gh/curl/Python), apply_patch, lecture locale et MCP cloud_environment.environment_status. Skill cloud-environment-runtime appliqué ; skills versionnés de continuité, audit, vérité, posologie et construction utilisés. Aucun connecteur GitHub supplémentaire requis : gh accède réellement à l’API. Les anciennes listes d’outils ci-dessus sont historiques. Automates GitHub permanents maintenus ; aucune nouvelle veille sur PC. Sources et limites réseau : audit/RESEAU-REPRISE-20261018.json.
