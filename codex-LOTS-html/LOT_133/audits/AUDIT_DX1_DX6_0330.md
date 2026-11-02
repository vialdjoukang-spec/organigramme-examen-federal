# Audit indépendant DX.1 / DX.6 — reprise 0330

Auditeur : `astra_audit0330`, distinct des rédacteurs. Date : 02.11.2026. Périmètre : ajouts depuis le préaudit 0240, preuves sources et AIPS associées. Le harnais et le verrou sont centralisés par root ; aucun HTML, fichier global ou Git modifié par cet auditeur. Aucun score ni validation médicale humaine.

## Matrice des lacunes à contrôler après livraison

| Domaine | Lacune héritée / contrôle ciblé | Condition de clôture |
|---|---|---|
| DX.1 diagnostic | Imitateurs et branche hémorragique encore incomplets. | Ajouts contextualisés dans le parcours adulte et appuyés par sources effectivement consultées. |
| DX.1 traitement | Réversion, prévention antithrombotique et complications non détaillées. | Indication, chronologie et limites explicites ; chaque dose confrontée à la notice exacte. |
| DX.1 thrombolyse | Actilyse 48313 et Metalyse 69958 : notices locales de 2025, non interchangeables. | Population, fenêtre, voie, présentation et schéma pondéral conformes ; divergences recommandations/AIPS non masquées. |
| DX.6 hémorragie portale | Vasoactif et antibioprophylaxie génériques ; AIPS spécifique manquante. | Preuve suisse exacte, indication réelle distinguée de recommandation ou hors indication. |
| DX.6 ascite / infection | Albumine et autres médicaments encore non vérifiés. | Voie, population, contexte et dose documentés ; aucun transfert automatique entre indications. |
| DX.6 encéphalopathie | Duphalac : contradiction lactose ; Xifaxan : prévention des rechutes, pas preuve autonome du premier épisode aigu. | Contradiction conservée ou résolue par preuve ; pas d'extension d'indication silencieuse. |
| DX.6 diurétiques | Aldactone : schéma Na/K ; égalité à 1 non tranchée. | Pas de règle inventée ; surveillance rénale/ionique contextualisée. |
| Fraîcheur | Cache/index daté ne démontre pas actualité réglementaire réseau. | Date de notice, date de consultation et preuve d'actualisation distinguées. |
| Verdict | Gel préparatoire 0240 ne vaut pas monographie thérapeutique publiable. | Verdict séparé par document et par niveau, fondé sur versions exactes. |

## Résultat

Signal root reçu ; contrelecture ciblée des ajouts P7/P10/P11/P12 DX.1 et P11 DX.6 effectuée, avec les deux JSON de complément. Le préaudit 0240 est réutilisé pour le fond inchangé ; root assure le contrôle des quatorze parties et quatorze questions. Aucun HTML n’est couvert par ce verdict.

| Document / ajout | Preuve directement contrôlée | Résultat |
|---|---|---|
| DX.1 imitateurs | Cache `dx1_0330/lectures_web.json`, extraits S13 medinfo : migraine, crises, troubles fonctionnels, hypoglycémie et coexistence AVC/crise. | Tableau prudent, sans règle d’exclusion dangereuse ni retard d’imagerie. |
| DX.1 hémorragie / aggravation | S14 CeMIR : formes graves, effet de masse, transformation hémorragique, déglutition, crises ; conclusions d’antagonisation et avis neurochirurgical urgent. | Ajouts concordants. Aucune cible tensionnelle étrangère ni traitement curatif universel extrapolé. Les antidotes et schémas suisses restent absents. |
| DX.1 antithrombotiques | S15 HAS 2018, S16 ESO 2021 (extraits et résumé), S17 résumé ESO/FA. Notice locale Metalyse L53 et L144. | Antiagrégation non cardioembolique, anticoagulation FA et prophylaxie veineuse distinguées ; bithérapie courte sélectionnée ; évitement antiagrégants/héparine IV pendant 24 h après Metalyse conforme. Aucune dose ajoutée. Les sources sont partiellement consultées, sans prétention de lecture intégrale. |
| DX.1 AIPS | Sources gzip 48313 L59–64, L216–250, L501–511 ; 69958 L14–30, L53, L70–91, L305–313. | Indications et numéros confirmés ; présentations et unités non interchangeables. Divergences recommandations/contre-indications non supprimées. |
| DX.6 Glypressine | `44470_live.txt` L12–49, L204–211. | Indication hémorragie œsophagienne adulte ; 1 mg de sel = 0,86 mg base ; doses exprimées en Glypressine, IV, fréquence et maximum concordants. Maximum 12 mg/j pendant ≤36 h puis 6 mg/j ; durée ≤5 jours ; voie basilique, bolus strict. Poids exactement 50 kg non inventé ; pas d’extrapolation au SHR, enfant ou insuffisance rénale. |
| DX.6 Glypressine sécurité | Même notice, CI et mises en garde ciblées. | CI coronaires, grossesse et exception vitale distinguées ; surveillance cardiovasculaire/ions/liquides, QT, ischémie, congestion et choc septique à bas débit correctement signalés. |
| DX.6 rifaximine | `63216_live.txt` L55–114, L691–703. | Réduction des rechutes chez cirrhotique ≥18 ans ; 550 mg oral deux fois/jour, comprimé ; réévaluation au-delà de six mois conforme. Pas d’indication autonome pour premier épisode aigu ; association au lactulose dans données pivot explicitée. CI et prudence rénale/hépatique concordantes. |
| DX.6 lactulose / spironolactone | `32894_live.txt` rubriques encéphalopathie/CI/précautions, L142–150 ; `27257_live.txt` L25–26/L43–44 et L223–233. | Cible selles et réduction en cas de diarrhée concordantes ; contradiction lactose conservée. Na/K=1 non tranché ; aucun schéma étranger substitué, surveillance contextualisée. |
| DX.6 ceftriaxone | `44625_live.txt` L34–58, L104–109, L845–861 ; consensus autrichien S8 L508. | Prophylaxie hémorragie digestive non assimilée à prophylaxie périopératoire autorisée ; distinction hors indication explicite. Aucune dose étrangère importée. Interdiction IV de formulation lidocaïne correctement signalée. |
| DX.6 albumine | `65562_live.txt` L28–54, précautions et L174–182. | Volume circulant, voie IV, concentrations et surveillance correctement contextualisés ; pas de schéma ascite/PBS/SHR prétendument validé par une indication générale. |
| DX.6 chronologie | S8 L501/506/508 et L624/626 directement relues. | Stabilisation/vasoactif précoces et antibioprophylaxie dès admission, correction déclencheurs encéphalopathie concordantes. |

### Intégrité, fraîcheur et réserves

Les six empreintes `sha256_live` de DX6_COMPLEMENT_0330 correspondent exactement aux fichiers `*_live.response` bruts. Elles ne sont pas celles des textes extraits `*_live.txt` ; ces derniers ont été utilisés pour la lecture ciblée. Les numéros ont été retrouvés dans les rubriques d’autorisation et les dates de notice vérifiées : Duphalac février 2023, Xifaxan avril 2023, Glypressine mars 2024, Rocephin juin 2025, Albumin Biotest et Aldactone août 2025. Les HTTP 200 datés du 02.11.2026 démontrent l’accès à ces versions documentaires ; aucune recherche exhaustive dans le catalogue Swissmedic démontrant leur caractère le plus récent n’a été fournie.

La contradiction DX.6 d’introduction (« aucune dose ») a été signalée à root puis corrigée par l’auteur ; le texte reconnaît désormais les extraits posologiques ciblés. Correction relue. Les doses présentes sont des lectures documentaires contextualisées, pas un protocole thérapeutique exhaustif.

| Niveau | DX.1 | DX.6 |
|---|---|---|
| Conversion en rendu préparatoire clairement identifié | Autorisable sur version finale ci-dessous ; fraîcheur documentaire qualifiée. | Autorisable sur version corrigée ; aucune erreur posologique identifiée dans les extraits ajoutés. |
| Publication comme monographie thérapeutique complète | Non validée : réversion, antihypertenseurs, antiépileptiques, antithrombotiques et modalités spécialisées restent sans schémas suisses complets. | Non validée : albumine/PBS/SHR, autres vasoactifs et protocole antibiotique restent incomplets ; discordance lactose non résolue et cas 50 kg/Na-K=1 non précisés. |

Avant une version prescriptive, compléter aussi la synthèse des risques importants de chaque produit : notamment réaction cutanée grave sous rifaximine (notice réseau L116 et suivantes) et incompatibilités calcium/ceftriaxone. Leur absence d’un tableau préparatoire explicitement non exhaustif n’invalide pas la concordance des extraits de doses vérifiés, mais ce tableau seul ne doit pas devenir un protocole autonome.

### Versions exactes

DX.6 corrigé : 21 449 octets, SHA-256 `da40816347a27b584c2ecefd8aa395136084fcac8f3409056003701d691b32c0`.

DX.1 final : 27 910 octets, SHA-256 `00e1f35f981190d9deac8f309a4444c08d054289539a8f27892748e73f92c9d2`.

Complément final DX.1 : les deux notices HTML récupérées directement via le proxy autorisé sont présentes. Les passages ciblés des fichiers `aips_48313_reseau_cible.txt` et `aips_69958_reseau_cible.txt` ont été confrontés au texte extrait des HTML réseau : 52/52 et 86/86 passages présents après normalisation des espaces. Les passages cliniquement pertinents, indications, présentation, restrictions, numéros et dates ont été relus. La rédaction P11 a été vérifiée après correction des mentions de fraîcheur : notices juin/mai 2025 accessibles le 02.11.2026, sans preuve de dernière version du registre. L’échec initial du connecteur demeure un incident historique, remplacé pour l’acquisition par cette récupération directe réussie, sans aucune nouvelle dose introduite.

**Verdict final : conversion préparatoire autorisable pour les deux versions exactes ci-dessus ; publication comme monographies thérapeutiques complètes non validée.** L’audit n’a modifié aucun texte auteur, aucun HTML ni fichier partagé. Le contrôle du rendu et de ses liens reste à réaliser après conversion.


## Addendum — concordance ciblée des HTML V8 préparatoires

À la demande de root, extraction ponctuelle avec `cache_controles.py extraire` : point 11 de DX.1 et points 9,11 de DX.6 ; deux commandes réussies (code 0). Les autres points n’ont pas été relus. Les dix-neuf contrôles statiques par document sont rapportés verts par root ; ils ne sont pas une validation clinique.

| Périmètre | Concordance du rendu extrait avec le fond audité | Verdict ciblé |
|---|---|---|
| DX.1 P11 | Actilyse 48313 et Metalyse 69958, indication adulte, fenêtre, non-interchangeabilité, distinction recommandations/AIPS, évitement antiagrégants/héparine IV pendant 24 h : conservés. Aucun schéma posologique ajouté. Fraîcheur juin/mai 2025 consultée en 2026 et absence de garantie de dernière version explicites. Branche hémorragique et réserves pharmacologiques conservées. | Conforme au niveau préparatoire audité. |
| DX.6 P11 | Six spécialités/numéros, populations, voies et réserves conservés. Rifaximine 550 mg oral deux fois/jour et réévaluation après six mois inchangées. Glypressine : sel/base, concentration, >/<50 kg, fréquence, plafonds 12 puis 6 mg/j, limite 36 h et cinq jours inchangés. Contre-indications/surveillance, réserves poids 50 kg, Na/K=1, lactose, SHR et ceftriaxone hors indication conservées. | Aucune altération médicamenteuse ou posologique identifiée. |
| DX.6 P9 | NFS/hémostase, rein/ions, bilan hépatique, cultures, ponction, imagerie et endoscopie contextualisés. Ponction diagnostique distinguée du drainage évacuateur ; aucune nouvelle dose ni règle thérapeutique introduite. | Concordant avec la préparation clinique déjà auditée. |

Les simplifications des notes documentaires ne lèvent aucune réserve de fraîcheur ni de complétude thérapeutique. Le contenu clinique ciblé est conservé lors de la conversion. Le présent contrôle porte sur le texte extrait des fenêtres HTML ; il ne certifie pas leur comportement visuel ou interactif au navigateur.

| Fichier courant | Octets | SHA-256 |
|---|---:|---|
| `_travail/DX1_REDACTION_0240.md` | 27745 | `af58ac59e5f125b159a2ccfaf048e74620c58e29b12b08a60e4ecf1bcdc9e8fb` |
| `LOT_133_Phase_B_V0_DX.1.html` | 102312 | `84a3496718ecc56d88f5db74a285b9e05008cda9e65b813ab2d47a7db6838909` |
| `_travail/DX6_REDACTION_0240.md` | 21127 | `bc0bd54733f3b98ed83e69b310763684b30def961ee95d5fc4889ebd51d28451` |
| `LOT_133_Phase_B_V0_DX.6.html` | 94003 | `edf67b89f32979be7a7b7fc59049cf7b7b9117c87117d6e61ed1bb8a752b6aa2` |

**Décision maintenue pour ces versions : rendu préparatoire recevable ; aucune validation comme monographie thérapeutique complète.** Toutes les réserves pharmacologiques et documentaires de cet audit restent applicables. Aucun HTML modifié par l’auditeur.
