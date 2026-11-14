# Audit médical agressif — PP-S5 à PP-S8 (36 fiches, 143 affections)

Auditeur indépendant (non rédacteur), 14.11.2026. Posture : skills `medecin-expert` et `expert-web`.
Méthode : lecture intégrale des 36 JSON par script ; schéma lu dans `recensement_sf.json > schemas > physiopathologie` ; contrôle des renvois SY, S, IMG, EX, PH, PHY contre les catalogues (fiches PP exclues) ; recherche de doses ; confrontation des 6 numéros Swissmedic cités au corpus local (`aips_corpus_index.json`, extraits `grok-LOTS-html/LOT_15x-16x/evidence/`). Aucun fichier modifié hors ce rapport ; ni commit ni push.

## 1. Contrôles mécaniques

| Contrôle | Résultat |
|---|---|
| Renvois SY, S, EX, PH, SF, PHY | 100 % résolus. IMG-331, IMG-334, IMG-337 existent dans `recensement/recensement.json`, pas dans `donnees/`. |
| Couverture VITE DIT CAFé | 9 lettres × 4 systèmes présentes ; champs du schéma présents. |
| Doses chiffrées | Aucune. Restent des schémas qualitatifs (voir L4). |
| AIPS cités (Rhophylac 53609, Fluimucil 31954, Pantozol i.v. 52710, GlucaGen 31489, Zometa 56257, Solu-Cortef 23533, Methotrexat-Teva onco 47999) | Numéros conformes au corpus. Dates Rhophylac (février 2026) et Solu-Cortef (octobre 2025) confirmées dans l'extrait lu. Fluimucil (novembre 2022) non vérifiable : l'extrait local ne porte pas la rubrique « Mise à jour ». |

## 2. Exactitude physiopathologique

| # | Gravité | Emplacement | Extrait fautif | PATCH exact |
|---|---|---|---|---|
| E1 | Grave | PP-S5-C, `affections[0].mecanisme[2]` | « les vomissements font perdre acide chlorhydrique et potassium » | « les vomissements font perdre l'acide chlorhydrique ; l'hypovolémie active l'aldostérone et la bicarbonaturie entraîne le potassium : le rein crée l'hypokaliémie, puis l'acidurie paradoxale » |
| E2 | Moyen | PP-S5-Tr, `affections[0].consequence_clinique` | « douleur projetée à l'épaule gauche (signe de Kehr) » pour rate **ou** foie | « Choc hémorragique ; douleur projetée à l'épaule gauche (signe de Kehr, rate) ou droite (foie). » |
| E3 | Moyen | PP-S6-F, `affections[2].mecanisme[3]` | « une correction trop rapide démyélinise le pont » (valable pour l'hyponatrémie seule) | « le cerveau gonfle ou se rétracte ; corriger trop vite une hyponatrémie chronique démyélinise le pont, corriger trop vite une hypernatrémie fait gonfler le cerveau » |
| E4 | Moyen | PP-S8-F, `affections[5].mecanisme[0]` | « une carence relative en insuline suffit à bloquer la cétogenèse » (sens inversé) | « l'insuline résiduelle suffit à bloquer la cétogenèse, mais pas la production hépatique de glucose » |
| E5 | Moyen | PP-S7-I, `affections[4].mecanisme[0]` | « (toxoplasme, rubéole, CMV, herpès, syphilis) passe le placenta » | « une primo-infection maternelle (toxoplasme, rubéole, CMV, syphilis) passe le placenta ; l'herpès se transmet surtout au passage dans la filière génitale » |
| E6 | Moyen | PP-S7-Ia, `affections[0].cible_therapeutique[2].pourquoi` | « il réduit le risque de défaut de fermeture du tube neural » placé sous le valproate | « il réduit le risque de base de défaut de fermeture du tube neural ; il n'annule pas le risque propre au valproate (déduction ; à vérifier AIPS valproate) » |
| E7 | Moyen | PP-S7-T, `affections[3].renvois_semiologie` | `SY-36` (hypertension portale) pour l'ascite de carcinose | Supprimer `SY-36` ; garder `IMG-212`. |
| E8 | Léger | PP-S5-A, `affections[3].cible_therapeutique[1].classe` | « résine chélatrice (cholestyramine) » : la chélation vise les métaux | « résine fixatrice des acides biliaires (cholestyramine) » |
| E9 | Léger | PP-S6-I, `affections[3].renvois_examen` | `EX-1-S7-prelevements-vaginaux-lochies` pour une urétrite masculine | Ajouter la PCR sur premier jet ; garder le prélèvement vaginal pour la femme seulement. |
| E10 | Léger | PP-S5-F, pancréatite aiguë | Classée « Fonctionnel » alors que la cause est obstructive ou toxique | Ajouter à `honnetete` : « Pancréatite classée en F par défaut (activation enzymatique) ; cause obstructive ou toxique. » |

## 3. Affections importantes manquantes

| # | Gravité | Fiche | Manque | PATCH |
|---|---|---|---|---|
| M1 | Grave | PP-S8-T | Syndrome de Cushing (adénome corticotrope, surrénalien, sécrétion ectopique) ; acromégalie. La passerelle PHY-S8-7 cite pourtant l'acromégalie. | Ajouter deux affections : Cushing (cortisol libre urinaire, freinage à la dexaméthasone, ACTH ; cible : chirurgie, inhibiteur de la stéroïdogenèse) ; acromégalie (IGF-1, HGPO avec GH ; cible : analogue de la somatostatine, antagoniste du récepteur de la GH). |
| M2 | Grave | PP-S8-Ia | Cushing iatrogène, la forme la plus fréquente ; hypophysite et thyroïdite des inhibiteurs de points de contrôle immunitaire | Ajouter « syndrome de Cushing iatrogène » avant l'insuffisance surrénale ; ajouter « endocrinopathies des anti-PD-1/CTLA-4 ». |
| M3 | Grave | PP-S7-V | Hématome rétroplacentaire ; placenta prævia | Ajouter « hématome rétroplacentaire » : décollement, saignement, hypertonie utérine, CIVD ; cible : extraction fœtale. |
| M4 | Moyen | PP-S7-I | Streptocoque du groupe B, listériose, chorioamniotite, endométrite du post-partum | Ajouter « infection materno-fœtale bactérienne » avec antibioprophylaxie per-partum. |
| M5 | Moyen | PP-S5-I / C / F / A / Tr / V | Péritonite bactérienne spontanée ; atrésie des voies biliaires et malrotation avec volvulus ; achalasie ; cholangite sclérosante primitive ; Boerhaave et ingestion de caustiques (cités dans `mecanisme` sans affection) ; thrombose porte et Budd-Chiari | Une affection par fiche, au format existant. |
| M6 | Moyen | PP-S6-A / C / Ia / D | Anti-MBG (Goodpasture), pourtant cité dans `cascade[1]` ; jonction pyélo-urétérale, Alport ; lithium, néphrite interstitielle aux IPP, cristallurie médicamenteuse ; néphropathie diabétique | Idem. |
| M7 | Moyen | PP-S8-F / C | Système « nutrition » sans dénutrition, syndrome de renutrition ni carences ; goutte ; phénylcétonurie, pourtant dépistée en Suisse chez le nouveau-né | Idem. |
| M8 | Moyen | PP-S7-Ia / T / C / D | Syndrome d'hyperstimulation ovarienne ; maladie trophoblastique ; cryptorchidie ; ostéoporose post-ménopausique. Le cadrage de PP-S7-D annonce « tissus et os » sans affection osseuse. | Ajouter les trois premières ; pour l'os, ajouter un renvoi vers PP-S8-D. |

## 4. Sources et honnêteté

| # | Gravité | Emplacement | Défaut | PATCH exact |
|---|---|---|---|---|
| S1 | Grave | PP-S7-F, `sources[0]` | L'AIPS Methotrexat-Teva sert de caution à la GEU, alors que l'indication autorisée l'exclut (SY-46 l'écrit : « hors AIPS »). | `"ref":"AIPS Methotrexat-Teva onco n° 47999, février 2025 : GEU hors indication autorisée (lu via SY-46)"` ; dans `cible_therapeutique` : « méthotrexate (hors AIPS) ». |
| S2 | Grave | PP-S7-C, -D, -Ia, -T | Seule source : la fiche interne S-16, étiquetée « Suisse (dépôt), lu ». Une fiche du dépôt ne constitue pas une source. Les quatre fiches n'ont aucune source externe. | Marquer `"origine":"dépôt interne (non opposable)"`. Ajouter au moins une source SGGG ou RMS par fiche, statut « non lu » tant qu'elle n'a pas été lue. |
| S3 | Moyen | 30 fiches, `statut:"lu"` + `via:"fiche SY-xx"` | La lecture appartient au rédacteur de la fiche SY, pas à celui de la fiche PP. | `"statut":"lu par la fiche SY-xx, non relu ici"`. |
| S4 | Moyen | PP-S6-T, PP-S6-Tr, PP-S6-C, PP-S8-Tr, PP-S5-Tr, PP-S8-D | Les sources sont hors sujet : « Infection urinaire » pour les tumeurs et les traumatismes, « Hyponatrémie » pour le diabète insipide, « infections intra-abdominales » pour le traumatisme. PP-S8-D n'a aucune source sur l'ostéoporose. | Retirer ces sources. Pour PP-S8-D, ajouter : `{"ref":"Ferrari S et al., Recommandations ASCO/SVGO 2020, Swiss Med Wkly 2020;150:w20352","origine":"Suisse","statut":"non lu"}`. L'existence de cette référence est confirmée par une recherche web. |
| S5 | Moyen | PP-S5-I, -Tr (WSES 2017) ; PP-S6-D, -A, -V (KDIGO 2021) | L'étiquette « international » sort de la hiérarchie Suisse → Europe → OMS. KDIGO a publié des mises à jour plus récentes (non vérifié ici). | `"origine":"international, non européen (dernier recours)"`. Chercher d'abord la SSN ou l'ERA. |
| S6 | Moyen | PP-S5-D (RMS 2011, 2012), PP-S8-T (RMS 2009), PP-S8-A (RMS 2009, 2010) | Ces sources ont plus de 12 ans ; la règle demande la version la plus récente. | Ajouter `"recence":"à vérifier"` ou les remplacer. |
| S7 | Léger | PP-S6-F | « EAU Guidelines on Urolithiasis » ne porte pas d'année. | Ajouter l'année lue, sinon « (année non vérifiée) ». |

## 5. Renvois, redondance, doses, style

| # | Gravité | Emplacement | Défaut | PATCH |
|---|---|---|---|---|
| R1 | Moyen | 36 fiches, `passerelles` | Les 4 passerelles PHY sont identiques pour les 9 lettres d'un système. Les passerelles pertinentes manquent : S8-T → PHY-S8-4, -7, -8 ; S8-F → PHY-S8-6, -9 ; S8-C → PHY-S8-10 ; S6-F → PHY-S6-3, -5, -6 ; S6-Ia → PHY-S6-5, -8 ; S5-F → PHY-S5-3 ; S5-C → PHY-S5-7 ; S5-I → PHY-S5-8 ; S7-I → PHY-S7-5 ; S7-V → PHY-S7-7 ; S7-C → PHY-S7-2. | Remplacer les passerelles fiche par fiche selon cette liste. |
| R2 | Moyen | PP-S5-Ia `affections[2]` / PP-S5-I ; PP-S7-C `affections[2]` / PP-S8-C `affections[1]` ; PP-S6-I urétrite / PP-S7-I IST | Les mêmes affections reviennent avec les mêmes cibles. | Garder la forme complète en S5-I, S8-C et S7-I. Ailleurs, garder une phrase et ajouter `{"vers":"physiopathologie","id":"PP-…"}` dans `passerelles`. |
| R3 | Léger | 36 fiches | Aucune passerelle vers un cours LOT, alors que le schéma la prévoit. | Ajouter `{"vers":"cours","id":"…"}`. |
| L4 | Léger | PP-S6-Ia (« une prise quotidienne »), PP-S8-Ia (« augmentation de la dose »), PP-S8-V (« forte dose »), PP-S5-F, PP-S7-V (« faible dose ») | Ces textes décrivent un schéma posologique. | Supprimer le qualificatif ou renvoyer à l'AIPS. |
| L5 | Léger | Tamsulosine (PP-S6-F), létrozole (PP-S7-F), misoprostol (PP-S5-Ia) | Usage hors indication ou retrait possible du marché suisse, non signalé. | Ajouter « (statut AIPS à vérifier) ». |
| L6 | Léger | `cascade` de PP-S5-A, -C, -D, de PP-S6, PP-S7 et PP-S8 | Les maillons sont nominaux (« Normal : tolérance… »), alors que PP-S5-I et PP-S5-V sont verbales. Trois mnémotechniques sont en anglais : « I GET SMASHED », « stones, bones… », « triple whammy ». | Réécrire chaque maillon avec un verbe. Traduire ou retirer les mnémotechniques anglaises. |

## 6. Points vérifiés exacts (échantillon)

Les points suivants sont exacts : NAPQI et glutathion ; somatostatine et gastrine dans *H. pylori* ; rôle des bêtabloquants β1 et β2 dans l'hypertension portale ; cotransport sodium-glucose et SRO ; rôle de SGLT2 dans le rétrocontrôle tubulo-glomérulaire ; tolvaptan et AMPc ; « triple whammy » ; VHL, HIF et VEGF ; sFlt-1 et PlGF ; amiodarone de types 1 et 2 ; « α avant β » ; ordre cortisol puis thyroxine dans le syndrome de Sheehan ; diabète insipide triphasique ; rifampicine et cortisol.

## 7. Verdict

| Critère | Note (2/1/0) | Raison |
|---|---|---|
| Exactitude des chaînes Normal → Signes | 1 | Une erreur de mécanisme classique (E1) et trois formulations fausses ou inversées (E3, E4, E5). |
| Exhaustivité des affections | 1 | Cushing, acromégalie et hématome rétroplacentaire sont absents. |
| Cibles pharmacologiques et leur « pourquoi » | 2 | Les explications sont justes ; le statut hors AIPS n'est pas signalé (S1, L5). |
| Sources et honnêteté | 0 | Des fiches internes servent de source ; l'AIPS cautionne un usage hors indication ; la mention « lu » est héritée. |
| Renvois et passerelles | 1 | Les renvois sont résolus, mais les passerelles sont génériques et des doublons subsistent. |
| Aucune dose, style | 1 | Aucune dose chiffrée ; restent des qualificatifs posologiques et des cascades nominales. |

**Prêt pour `audit-ok` : non.** Il manque les corrections E1 à E7, M1 à M3, S1, S2 et R1. Les défauts Léger peuvent suivre dans une passe ultérieure.
