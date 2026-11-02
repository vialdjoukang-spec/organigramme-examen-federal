# Audit pharmacologique ciblé DX2 / DX7 — 1020

02.11.2026 UTC. Auditeur distinct `audit_1020`, non auteur. Écritures limitées au présent rapport et à RESERVES_CLINIQUES_1020.json ; aucun Git, fichier auteur ou réseau utilisé par cet auditeur.

**Verdict Markdown : ajouts P11 recevables pour intégration préparatoire aux empreintes ci-dessous.** Les doses reproduites concordent avec les notices exactes consultées dans les caches. Ce verdict porte sur deux exemples pharmacologiques contextualisés, sans valider un protocole prescriptif complet ni les autres médicaments. Aucun score, aucune validation humaine revendiquée.

## Versions exactes

| Fichier relatif au LOT133 | SHA-256 |
|---|---|
| `_travail/DX2_REDACTION_0427.md` | `8c7ee1530a947cca84ca11f6997ee1879355bf94a63ce0f267ec1f55909190a9` |
| `_travail/DX7_REDACTION_0427.md` | `86090f1e489ffb4f7327526d18e60d4521b51323f85e7c051a70fe3b8db960b6` |
| `evidence/PHARMA_DX2_1020.json` | `753b558e49d6ad55135bbd59fbc7672687ddcc992b42fa37d8d37ef99ede5aab` |
| `evidence/PHARMA_DX7_1020.json` | `c0b5323db2d90828ab0cccff238d1cea250dd983d708d6c7ec7782388dc5c10c` |
| `evidence/DX2_0427.json` | `e9e50ee4a551ffcb7424ed935675a83b002381402241d0261b17f6b02b369610` |
| `evidence/DX7_0427.json` | `ab94a58e7140795896ef6ba6e3d9d109e82e0f8fd1ffd3806e3ef458a43a4e24` |

Avant contrelecture puis sur les versions finales, `controler_brouillons.py` exécuté : parties1–14 et questions1–14 présentes dans chaque Markdown. Cette preuve structurelle ne valide pas les traitements. Le fond ancien repose sur AUDIT_DX2_DX7_0427 ; nouvelle lecture centrée sur P11 et notices ajoutées.

## DX2 — Rocephin

Lecture directe du cache S7_direct_paragraphes.txt : rubriques indications/posologie/CI/précautions/interactions, lignes1–180, administration L589–591, numéro L649 et date L664. Tous les paragraphes extraits ont été retrouvés dans le HTML brut après normalisation des espaces. Toutes les empreintes déclarées de PHARMA_DX2_1020 concordaient lors du contrôle ; dose et formulation finale relues après correction grammaticale.

Notice suisse Rocephin44625, juin2025 : septicémie et méningite de germes sensibles ; adulte1–2g toutes les24h, dose quotidienne unique jusqu’à4g si infection sévère ou germe moyennement sensible. Le texte précise que ce repère général ne fixe ni dose initiale universelle du purpura fulminans ni schéma de méningite adulte. Rubrique méningite pédiatrique non transposée, durée adulte réservée à la stratégie adaptée. Pas de retard des soins induit.

Injection IV2–4min et perfusion≥30min concordantes ; préparation selon dose/présentation explicitement requise. Lidocaïne IM jamais IV ; absence de calcium lors de reconstitution/dilution et administration simultanée, y compris deux lignes, puis rinçage avant administration successive chez adulte : conforme. Hypersensibilité, plafond2g/j si clairance<10ml/min ou dialyse, absence de complément postdialyse, conditions rénale/hépatique isolées et atteinte combinée grave : concordants.

Pas de correction clinique bloquante identifiée. Sécurité ciblée, sans inventaire exhaustif des effets indésirables : le cache contient notamment réactions cutanées graves, hémolyse, colite et encéphalopathie qui ne sont pas développées dans ce cours. Cela ne rend pas fausses les doses vérifiées ; le repère ne doit pas devenir une notice autonome. Acquisition HTTP200 du02.11 attestée par l’auteur, vérification locale du brut par l’auditeur ; dernière révision ultérieure non exclue.

## DX7 — Forxiga

Lecture directe du cache français aips_forxiga_fr.txt L1–345 (composition, indication, posologies/rein/foie, CI, précautions, interactions, grossesse/allaitement, résumé sécurité), numéro65176 L1209 et date août2026 L1223. SHA du cache texte et JSON brut concordants ; texte complet effectivement présent dans la réponse fournisseur archivée. Acquisition fournisseur04.10.2026 distinguée de lecture02.11 ; pas de téléchargement réglementaire direct du jour revendiqué.

IC ventriculaire gauche symptomatique chronique de l’adulte en association : indication correctement délimitée. Dose10mg orale1fois/j indépendante des repas ; DFGe≥25, initiation non recommandée sous25, poursuite possible du traitement déjà établi et arrêt avant dialyse/transplantation : concordants. Dose initiale5mg en insuffisance hépatique sévère puis10mg si tolérée avec absence d’étude dans cette population : source reproduite sans masquer sa limite.

Hypotension/déshydratation avec diurétiques, insuline/sulfonylurée et hypoglycémie, lithium, mycoses, urgence Fournier, hypersensibilité, type1, grossesse/allaitement : synthèse concordante. Suspicion d’acidocétose même sans hyperglycémie importante, test cétonique et arrêt jusqu’à clarification ; interruption lors de pathologie aiguë grave/chirurgie/jeûne, si possible3jours avant et reprise stable/alimentation orale : conformes au cache. Le cours ne présente pas Forxiga comme traitement initial universel du choc.

Discordance documentaire détectée : résumé sécurité L330 et titre DELIVER L995 indiquent FEVG>40, tandis que paragraphe L997 indique≤40. L’auteur a consigné cette anomalie dans les preuves après signalement ; >40 retenu dans le cours est soutenu par le résumé effectivement lu. Aucune correction de la notice ni résolution réseau prétendue. Pas de correction clinique bloquante identifiée dans P11.

## Réserves et suite

Réserve ancienne « aucune notice AIPS lue/aucune dose » désormais levée uniquement pour ces deux spécialités et passages. DX2 garde les lacunes de protocole adulte spécifique, alternatives et traitements de soutien ; OFSP2022 nécessite réconciliation actuelle. DX7 garde la réserve autres molécules, protocole aigu, S5 partiel et ESC2026 non ouvert. Les limites du périmètre adulte ne réclament pas automatiquement extension pédiatrique ou obstétricale.

L’inventaire RESERVES_CLINIQUES_1020 distingue documentation, complétude de prescription et images. Les blocages documentaires historiques déjà levés ne sont pas réactivés. DX1 changement de titre seul documenté dans RENDU_DX_0330 ; DX3 correction du gras/comparateurs documentée et relue dans COHERENCE_TRANSVERSALE_0858 : leurs écarts SHA n’invalident pas automatiquement le fond antérieur.

La concordance HTML initialement attendue est réalisée dans le complément ci-dessous.

## Complément final — concordance HTML

Après notification root, extraction réelle de P11 des deux HTML avec `cache_controles.py extraire`, lecture des corps/fenêtres complets extraits, puis lecture DOM ciblée des chapeaux et notices S7/S8 et contrôle des liens AIPS. Aucun HTML complet affiché. Doses, indications, exclusions, sécurité et réserves décrites ci-dessus sont conservées. Chapeaux : population adulte et modalités médicamenteuses limitées aux spécialités citées, sans ancienne affirmation contradictoire d’absence de dose.

Rocephin conserve juin2025 et limites méningite adulte/fraîcheur. Forxiga conserve août2026, lecture ciblée, nature fournisseur et absence d’interrogation directe du registre. Date fournisseur04.10.2026 et discordance DELIVER restent dans les preuves ; le rendu ne revendique pas téléchargement direct. URL exactes des deux notices présentes.

| HTML final contrôlé | Octets | SHA-256 |
|---|---:|---|
| `LOT_133_Phase_B_V0_DX.2.html` | 102651 | `92d02b0a531262890210be2bbbb4889f2c93aa66eea72b80a35e345a10c02252` |
| `LOT_133_Phase_B_V0_DX.7.html` | 100397 | `1457e7804dea06aebd2235ef95baed5e719de19d52f435b1e28398059292476f` |

**Concordance ciblée recevable pour intégration préparatoire aux SHA HTML ci-dessus.** Aucun défaut posologique ou altération clinique identifié dans P11. Root rapporte19contrôles statiques et quatre configurations Chromium par HTML ; ils ne sont pas revendiqués comme exécutés par cet auditeur. Aucun audit exhaustif des autres parties ou de l’iconographie ajouté. Les réserves de documentation, de couverture thérapeutique et d’images persistent selon leur nature dans l’inventaire associé.
