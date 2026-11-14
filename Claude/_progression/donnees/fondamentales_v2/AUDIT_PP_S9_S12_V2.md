# Contre-audit V2 — PP-S9 à PP-S12 après corrections

Auditeur indépendant, 14.11.2026. Pièces lues : `CORRECTIONS_PP_S9_S12.md` et les 36 JSON corrigés, relus par script. Ni commit ni push ; seul ce fichier est écrit.

## 1. Contrôles mécaniques

| Contrôle | Résultat |
|---|---|
| Renvois SY, S, IMG, EX, PH, y compris `renvoi_pharmaco` | 100 % existants (IMG-294 Épiphysiolyse, IMG-295 Perthes, SY-5, SY-15, EX-9-S11-personnalite, EX-9-S11-trouble-obsessionnel-compulsif inclus) |
| `affections[]` comparé aux noms de `detail_affections` | Identiques dans les 36 fiches |
| Doses chiffrées | Aucune |
| Affections ajoutées | 19, conformes à la liste du rédacteur ; total 140 |

## 2. Vérification des corrections demandées

| # | Statut | Constat |
|---|---|---|
| M1, M2, M3 | Corrigés | M1 et M3 sont exacts. M2 est corrigé, mais le texte est adouci : voir N1. |
| M4 CIVD | Corrigé | « le TP (Quick, en %) baisse, le TCA s'allonge » est exact. |
| M5, M6 AHAI | Corrigés | La forme chaude et la forme froide sont distinguées ; C3 et l'hémolyse hépatique sont exacts. |
| M7 Spondylodiscite | Corrigé | Le germe se fixe d'abord dans le plateau sous-chondral, puis gagne le disque. |
| M8 Sarcomes | Corrigé | Ostéosarcome et Ewing, chondrosarcome et parties molles sont distingués avec justesse. |
| M9 Compression médullaire | Corrigé | Les corticoïdes en urgence, puis la chirurgie ou la radiothérapie, figurent. |
| M10 Impétigo | Corrigé | La forme bulleuse (desmogléine 1) est distinguée de la forme croûteuse. |
| M11 Anti-HMGCR | Corrigé | Exact. |
| M12, M16 Sevrages | Corrigés | Benzodiazépines et opioïdes prescrits restent en Ia ; l'alcool passe en F, avec un renvoi croisé ; GABA-A et NMDA sont décrits avec justesse. |
| M13 Métamizole | Accepté | La reformulation du rédacteur est retenue. La source lue le confirme : « accident d'origine immuno-allergique… ne dépendent pas de la dose » (Swissmedic, page vérifiée ce jour). Mon M13 initial est retiré. |
| R1, R3 | Corrigés | `traitement_cible` vaut `null` (S11-A, S11-T). |
| R2 | Corrigé | `PH-S1-antidementiels`. |
| R4 | Corrigé | `renvoi_pharmaco` pointe vers les thymorégulateurs, le lithium et le valproate. |
| R5 | Corrigé | PP-S12-Tr pointe vers `EX-2-S9-radiographie-standard-age-osseux`. |
| S1 à S5 | Corrigés | Les sources sont propres à chaque lettre. Swiss TPH passe avant l'OMS. Les étiquettes sont cohérentes. |
| S6 | Corrigé partiellement | J'ai vérifié la source « Swissmedic Vigilance-News éd. 32 (mai 2024), valproate » dans le PDF original : elle est réelle. Cependant, son statut est « résumé », alors que la citation exige une lecture mot pour mot (voir N1). |

## 3. Arbitrage M15

**Décision : on renomme.** Le nom actuel, « ostéonécrose de la mâchoire aux bisphosphonates », est médicalement faux, puisque le texte cite le dénosumab. L'identité repose sur l'`id` (PP-S9-Ia), non sur le libellé. Un champ `nom_audit` parallèle crée deux vérités.

PATCH :
1. Dans PP-S9-Ia, poser `detail_affections[3].nom` et `affections[3]` = `"ostéonécrose de la mâchoire liée aux antirésorbeurs (bisphosphonates, dénosumab)"`, puis supprimer `nom_audit`.
2. Dans `recensement_sf/recensement_sf.json`, ligne 3771 (bloc PP-S9-Ia), faire le même remplacement. Cette modification relève du coordinateur, car l'auditeur ne touche pas ce fichier.

## 4. Nouveaux défauts (corrections et 19 ajouts)

| # | Gravité | Emplacement | Extrait (≤ 200 car.) | Défaut | PATCH exact |
|---|---|---|---|---|---|
| N1 | **Grave** | PP-S11-F, trouble bipolaire, `cible_therapeutique` | « Le valproate est tératogène : on l'évite chez la fille et la femme en âge de procréer, sauf si toutes les conditions… » | Le texte adoucit la source. Swissmedic écrit « contre-indiquée » ; la contre-indication pendant la grossesse et le risque paternel manquent. | « Le valproate est tératogène : sa prescription est contre-indiquée chez les jeunes filles et les femmes en âge de procréer, sauf si toutes les conditions du programme de prévention de la grossesse sont remplies, et pendant la grossesse dans le trouble bipolaire ; un risque de troubles neurodéveloppementaux est possible chez l'enfant d'un père traité dans les trois mois précédant la conception (Swissmedic, Vigilance-News éd. 32, mai 2024). » Passer le statut de la source à « lu le 14.11.2026 (PDF FR, messages-clés) ». |
| N2 | Moyen | PP-S10-T, LAP, `cible_therapeutique` | « L'acide tout-trans-rétinoïque et le trioxyde d'arsenic lèvent le blocage… » | Le syndrome de différenciation manque. C'est la complication mortelle propre à ce traitement. | Ajouter : « La différenciation massive peut provoquer un syndrome de différenciation (fièvre, détresse respiratoire, épanchements, prise de poids), que les corticoïdes traitent. » |
| N3 | Moyen | PP-S12-Ia, angio-œdème sous IEC, `cible_therapeutique` | « l'icatibant… ou le concentré d'inhibiteur de C1 agissent » | Le texte affirme trop : les essais contrôlés n'ont pas démontré cette efficacité. L'indication suisse de l'icatibant vise l'angio-œdème héréditaire (AIPS non lu). | « …l'icatibant ou le concentré d'inhibiteur de C1 se discutent hors indication dans les formes graves, sans efficacité démontrée par les essais ; l'antihistaminique et le corticoïde n'agissent pas ; on sécurise d'abord les voies aériennes. » |
| N4 | Léger | PP-S11-I, encéphalite herpétique, `renvoi_examens` | `["EX-3-S11-eeg-…"]` | La PCR du LCR est citée dans l'examen, mais pas dans les renvois. | Ajouter `"EX-1-S1-lcr-pcr-multiplex"` en tête. |
| N5 | Léger | PP-S9-C, Duchenne, `cible_therapeutique` | « des thérapies ciblées (saut d'exon) existent selon la mutation » | Le statut d'autorisation en Suisse n'est pas vérifié. | « …des thérapies ciblées selon la mutation sont en développement ou d'autorisation limitée (statut Swissmedic non vérifié). » |
| N6 | Léger | PP-S9-Tr, épiphysiolyse | Classée Tr | Le classement contredit IMG-294 (lettre D) et le mécanisme décrit : glissement sous le poids, avec un terrain endocrinien. | Déplacer dans PP-S9-D, ou garder en Tr et ajouter `"renvoi_fiche":"PP-S9-D"` ; harmoniser avec IMG-294. |
| N7 | Léger | PP-S9-I, arthrite de Lyme, `cible_therapeutique` | « une ceftriaxone intraveineuse ou un traitement anti-inflammatoire traitent la synovite persistante » | La séquence est confondue. | « Si l'arthrite persiste, une seconde cure orale ou la ceftriaxone intraveineuse suivent ; une synovite qui persiste après les antibiotiques relève d'un traitement anti-inflammatoire, voire d'une synovectomie. » |
| N8 | Léger | PP-S10-A, SAPL, `cible_therapeutique` | « Les AVK anticoagulent au long cours… » | La forme obstétricale n'a pas de cible thérapeutique. | Ajouter : « pendant la grossesse, l'aspirine et l'héparine de bas poids moléculaire remplacent les AVK, qui sont tératogènes. » |
| N9 | Léger | PP-S10-I, parvovirus B19, `clinique` | — | L'anasarque fœtale manque. | Ajouter : « chez la femme enceinte, le virus peut provoquer une anémie fœtale et une anasarque. » |
| N10 | Léger | PP-S11-F, TOC, `cible_therapeutique` | « souvent à dose plus élevée que dans la dépression (AIPS) » | L'AIPS est citée sans avoir été lue. | Remplacer « (AIPS) » par « (AIPS suisse, non lu) ». |

Les 19 ajouts sont par ailleurs exacts : aplasie (attaque T, ATG, ciclosporine, agoniste de la TPO), SAPL (trois anticorps, persistance, AOD déconseillés dans les formes à haut risque), LAP (PML-RARA, CIVD fibrinolytique), TDAH, TCA (syndrome de renutrition), TOC, personnalité, syndrome malin (dantrolène, bromocriptine), hydrocéphalie à pression normale (triade, test de ponction), encéphalite herpétique, eczéma de contact (type IV), canal lombaire étroit (pouls présents), Perthes, Duchenne (Gowers).

## 5. Verdict

| Critère | V1 | V2 |
|---|---|---|
| Exactitude physiopathologique | 1/2 | 2/2 une fois N2 et N3 appliqués |
| Classement VITE DIT CAFé | 1/2 | 2/2 (N6 reste mineur) |
| Couverture de l'examen fédéral | 1/2 | 1/2 : 17 omissions « Moyen » restent ouvertes (sclérodermie, Paget, SDRC, intoxication au lithium, lichen plan, syphilis secondaire, etc.) |
| Renvois | 1/2 | 2/2 |
| Doses | 2/2 | 2/2 |
| Sources | 0/2 | 1/2 : une source suisse par système, mais aucune recommandation de société lue en entier |

**Verdict : NON, pour une seule raison bloquante : N1 (texte Swissmedic adouci sur le valproate).** Une fois N1, N2, N3 et le renommage M15 appliqués, le lot passe à « oui sous réserve ». La réserve tient aux omissions « Moyen » du §5 V1 et à l'absence de recommandation suisse lue en entier ; elle ne bloque pas `audit-ok` si le coordinateur l'accepte et la consigne.

Sources vérifiées par l'auditeur : [Swissmedic, Vigilance-News éd. 32, mai 2024 (PDF FR)](https://www.swissmedic.ch/dam/swissmedic/fr/dokumente/marktueberwachung/vigilance/vigilance-news-mai-2024.pdf.download.pdf/FR_SMC_Vigilance-News%20Ed.%2032_FINAL_20240528.pdf), messages-clés sur le valproate, lus le 14.11.2026 ; [Swissmedic, Métamizole et agranulocytose](https://www.swissmedic.ch/swissmedic/fr/home/medicaments-a-usage-humain/surveillance-du-marche/pharmacovigilance/vigilance-news/novalgin_und_agranulozytose.html), lu le 14.11.2026.
