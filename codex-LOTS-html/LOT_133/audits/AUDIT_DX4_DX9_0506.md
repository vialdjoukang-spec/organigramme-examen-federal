# Audit de reprise indépendant — DX.4 et DX.9 — 0506

02.11.2026 UTC. Auditeur `audit_0506`, distinct des auteurs. Écriture limitée à ce rapport ; aucun fichier auteur, Git ou registre global modifié. Reprise après interruption de capacité : inventaire réel, sans reconstitution fictive de preuves.

**Constat initial historisé, désormais dépassé par le verdict final ci-dessous : audit de fond alors non clos.** Les deux brouillons ont une structure complète ; les deux preuves documentaires sont absentes au constat. La présence de caches ne certifie ni les passages effectivement lus par les auteurs ni la concordance scientifique de leurs affirmations.

| Brouillon | Octets | SHA-256 exact | Structure observée |
|---|---:|---|---|
| `_travail/DX4_REDACTION_0506.md` | 33829 | `6ce68f4eced795f35ab9a987fe32e67d22b3aba737d4044a3bd222c6492402f5` | parties1–14 et questions1–14 conformes |
| `_travail/DX9_REDACTION_0506.md` | 22914 | `cc1e84dbd967cf67972aa94a8e9bac0176f438660771989caca609325effbba8` | parties1–14 et questions1–14 conformes |

`python3 -B codex-LOTS-html/LOT_133/_travail/controler_brouillons.py <DX4> <DX9>` exécuté réellement avant lecture : code0. Ce contrôle ne valide ni fond, ni langue, ni rendu.

## Éléments effectivement présents

| Cache relatif au LOT133 | Octets | SHA-256 exact |
|---|---:|---|
| `_travail/_cache/dx4_0506/S1_texte_source.txt` | 51269 | `3040095c212474afd0b059e2ea0afcc468aa5c6a88379dccc1d0ad13954feed0` |
| `_travail/_cache/dx4_0506/S2_texte_source.txt` | 28993 | `867e41fdd6e66131256fea7413e0fa3946bec8559433459146d53fc466a6e2c5` |
| `_travail/_cache/dx4_0506/S3_texte_source.txt` | 26125 | `e075485c0e5bb14772628f1a27ba334ee5a42a801d62e9d1e1c5b7ff04e561b8` |
| `_travail/_cache/dx4_0506/S4_texte_source.txt` | 150704 | `e68db2f4c5ae44d1cdfa33f735ae6e6806b401b95ca462b99438a96674563c42` |
| `_travail/_cache/dx4_0506/S5_texte_source.txt` | 34483 | `07ce8a950c00b05c1cc755b3acac194db28c5f61a42aed946c2b23684f6b0d07` |
| `_travail/_cache/dx4_0506/lectures.json` | 332825 | `39de19c6565deb481be86236cddb61651456bb396bb31cb1ed6c371e555e9e1c` |
| `_travail/_cache/dx9_0506/berne_mecanismes.json` | 5433 | `cd95206d64ed2143bb57488d3d6981c82265604ca17c855757db203cef66332a` |
| `_travail/_cache/dx9_0506/confirmation.json` | 7225 | `1e220ea16b9c93cd2e954b1c1b633e04db253ed0a81d8c61afffe0c2734b8fa9` |
| `_travail/_cache/dx9_0506/privigen.html` | 90562 | `5dfef65edd046227c1ba4397fba19f74ff95b7f49f88fd217c5207443448764c` |
| `_travail/_cache/dx9_0506/privigen.txt` | 53080 | `e70228b2cc89f69c4432d8bedbee9e806c3b049918bd7a2c64e9a6c4a492c58d` |
| `_travail/_cache/dx9_0506/pti_conduite.json` | 17945 | `6d06409fb81e265f3575e29b7d20ab79ac967a6b0264317577c2f71c31d396ce` |
| `_travail/_cache/dx9_0506/pti_diagnostic.json` | 17284 | `541f9f8bdb3fb009b47bb2183f334e9e61ea59416deb9771380d68bd91fbdf92` |
| `_travail/_cache/dx9_0506/ptt_adamts13.json` | 2983 | `65164be7bdd989cc2e47ad6d2c7dcb20d1f10964fae3d0ec7b88ff406b1d08df` |
| `_travail/_cache/dx9_0506/tih_diagnostic.json` | 20968 | `dbe2104ef833ea86fae3374a1fb544906cec9dfdf85e53d8b0e3fde6c208a0fe` |
| `_travail/_cache/dx9_0506/tih_suisse_resume.json` | 3662 | `af32d2271edf3556522c35e14cebb5fc5299d1d323e926af3924f629a00ff03b` |

Le JSON DX4 contient cinq résultats source avec URL, titre, acquisition fournisseur, extraits et texte complet : Luxembourg anémie2021, mediX carence martiale, HUG anémie2022, PNDS AHAI2024 et HAS capital sanguin périopératoire2022. La rubrique Sources du Markdown identifie déjà S1–S5 et leurs limites. Présence et métadonnées inspectées ; cette inspection seule ne constitue pas une contrelecture complète des cinq textes.

DX9 dispose de caches HemoSurf Berne, fiche belge, extraits PNDS PTI, HAS ADAMTS13, TIH suisse et française, plus Privigen HTML/TXT. PNDS PTI/ADAMTS13/TIH suisse : extraits, pas texte intégral dans les réponses inspectées. `tih_diagnostic.json` est un objet résultat direct, contrairement aux autres enveloppes `results`. La rubrique Sources du Markdown renvoie actuellement au seul JSON de preuve absent ; les références ne sont donc pas encore autonomes.

## Manques transmis aux auteurs

| Priorité | Manque constaté | Reprise exacte demandée |
|---|---|---|
| DX4 | `evidence/DX4_0506.json` absent | Auteur : fournir mapping S1–S5, URLs exactes, dates/version distinctes des acquisitions, passages réellement lus, limites, SHA des caches et du Markdown final. Ne pas présenter toute la bibliographie comme lue. |
| DX9 | `evidence/DX9_0506.json` absent | Auteur : fournir mapping S1–S7, URLs et lectures exactes, notamment provenance/date de la notice Privigen, empreintes et limites des extractions partielles. |
| DX9 | Références visibles absentes du Markdown | Ajouter titre/URL/date/portée/limites dans Sources, sans seul renvoi à un fichier inexistant ; conserver leur visibilité lors du rendu. |
| Audit | Contrelecture scientifique non achevée | Après remise : relire points2,3,4,8,9,11,12 et passages source correspondants, vérifier seuils, branches urgentes, AIPS et corrections puis consigner verdict sur SHA exact. |
| Rendu | Aucun HTML DX4/DX9 contrôlé | Après éventuel accord préparatoire, faire la concordance ciblée des passages corrigés et notices sources. |

Le premier affichage combiné des deux Markdown a été tronqué : il ne vaut pas lecture intégrale des deux documents. Aucune dose ou recommandation n’est déclarée vérifiée sur la seule présence de Privigen. DX4 revendique absence de dose/AIPS non lu ; DX9 revendique lecture de sécurité Privigen sans dose, encore à contrôler directement. Aucun score, aucune validation clinique ou médicale humaine, aucune publication attestée. Les notifications précises ont été envoyées aux auteurs et à root ; attente de remise sans polling répétitif.

## Audit final après remise des preuves et corrections

**Verdict : DX4 et DX9 recevables pour intégration préparatoire aux empreintes ci-dessous.** Les preuves initialement absentes ont été fournies par les auteurs ; les corrections ciblées ont été relues. Aucun score ni validation clinique/médicale humaine. Les constats initiaux restent conservés pour rendre la reprise traçable.

| Version finale | Octets si Markdown | SHA-256 exact |
|---|---:|---|
| `_travail/DX4_REDACTION_0506.md` | 34449 | `8f5ad8c917fd4a1f6a373e36a250eff0bf9c608de26dc039a1c7c92df1e9b379` |
| `_travail/DX9_REDACTION_0506.md` | 27711 | `330733d7473b4b6b18cd4e780c7e538b77321a795d24b1e2b9fd26263f78b376` |
| `evidence/DX4_0506.json` | — | `be4aef28de1f3f9f71f04ceb0c6ae0ac454a763eb602fd0eafbd428b2e60f6f8` |
| `evidence/DX9_0506.json` | — | `f29451864308da2da94b55b03fc64edd3e44eef327f745d846ac7f5314e82679` |

`controler_brouillons.py` réexécuté après corrections : chaque brouillon conserve les14parties et14questions. Les empreintes de tous les caches déclarés dans les preuves finales ont été recalculées et concordent. Le nouveau complément TIH et les cinq extractions TXT de DX4 sont inclus dans ce contrôle ; leur absence de l'inventaire initial reflète leur remise ultérieure.

### Lectures effectivement effectuées

Contrelecture des caches acquis par les auteurs, sans nouvelle acquisition réseau par cet auditeur. DX4 : S1 HUG, définition/indices/réticulocytes, clinique/alarme, classification, fer/B12/inflammation et urgence transfusionnelle ; S2 mediX, ferritine/CRP/TSAT, causes dont maladie cœliaque, principes substitution, hypophosphatémie et contrôle Hb4semaines ; S3 Luxembourg, classification et bilan, ferritine/CRP, restrictions des marqueurs martiaux et macrocytose ; S4 PNDS AHAI, passages réticulocytes/hémolyse, limites du TDA, indications médullaires, causes et transfusion ; S5 HAS, passages postopératoires3.1–3.3 avec seuils, transfusion unité par unité et suivi. Les sorties tronquées ont été complétées par lectures ciblées ; aucune lecture intégrale des bibliographies/annexes revendiquée.

DX9 : S1 HemoSurf pseudothrombopénies/mécanismes ; S2 fiche belge ; S3 extraits PNDS2024 de diagnostic, myélogramme, seuils/traitement, urgences et éducation ; S4 HAS ADAMTS13, résultats ; S5 résumé suisse TIH seulement ; S6 extraits des algorithmes, tests fonctionnels et situations réanimation/CEC/ECMO, puis paragraphe continu de probabilité intermédiaire dans `tih_complet_complement.json` ; S7 Privigen exact, indication/contre-indications/surveillance, hydratation, hémolyse, atteinte rénale et date juillet2025. Les limites d'extraits et le résumé S5 sont explicitement conservés. Les recommandations françaises ne deviennent pas suisses ; le PNDS est hébergé HAS, sans validation HAS revendiquée.

### Résultats et corrections ciblés

| Chapitre/points | Résultat documentaire et clinique préparatoire |
|---|---|
| DX4 P2–3 | Terrains multiples sans fréquence suisse inventée ; production/destruction/pertes et restriction martiale inflammatoire distinguées. Hémolyse insuffisamment régénérative possible, tolérance liée à vitesse et réserves. |
| DX4 P4 | Instabilité et saignement traités sans attendre classification/bilan carentiel ; suspicion MAT et cytopénies associées adressées en urgence. |
| DX4 P8 | Hb130/120g/L attribuée sources adultes CH ; VGM local82–98 distingué convention80–100 ; réticulocytes≥120/<70G/L sans transformer intervalle intermédiaire en normalité. TDA positif seul non diagnostique. |
| DX4 P9 | Ferritine/CRP et enquêtes causales contextuelles ; fer sérique isolé insuffisant ; hémolyse et moelle ciblées. Correction demandée : attribution explicite de l'usage contextuel TSAT à mediX S2, avec ambiguïté/restriction interne S3 décrite en Sources. Correction relue ; pas revendication de consensus pour un dosage systématique. |
| DX4 P11 | HUG70g/L et70–80g/L cardiovasculaire présentés comme évaluation hospitalière ; HAS70–80g/L limité adultes stables après chirurgie non cardiaque. Hémorragie active/SCA exclus de la transposition. Unité par unité contextualisée. Fer/B12 et AHAI sans dose, voie/produit à vérifier AIPS. |
| DX4 P12 | Hb vers4semaines selon mediX, plus tôt si clinique ; ferritine différée selon voie et protocole, divergences HUG/mediX conservées. Suivi HAS4semaines limité postopératoire. |
| DX9 P2–3 | Artefact EDTA, frottis et contrôle adapté avant étiquette ; dilution citrate signalée. Mécanismes multiples, production/destruction immunes non opposées artificiellement. Source HemoSurf ancienne SHU/enfant non transposée. |
| DX9 P4 | Hémorragie grave, MAT/PTT, CIVD, TIH distinguées ; seuil hospitalisation PTI récent<20G/L contextuel, sans attente de pentade ni équivalence avec seuil transfusionnel universel. |
| DX9 P8–9 | Bilan de consommation/hémolyse et sérologies en contexte ; myélogramme non systématique même>60ans selon PNDS, divergence fiche belge explicite. ADAMTS13 prélevé avant plasma, sans retarder traitement ; <10% et intervalle10–20% correctement contextualisés. |
| DX9 P11 | PTI peu symptomatique versus urgence vitale ; corticoïdes/IgIV/transfusion associés dans cette dernière. Précautions Privigen conformes à la notice exacte, dont déficit IgA avec anti-IgA et hyperprolinémie spécifiques au produit. Aucune dose proposée ; pas protocole PTT/CIVD exhaustif revendiqué. |
| DX9 P12 | Probabilité clinique avant tests ; anti-PF4 positif non suffisant, rôle fonctionnel et limites4T en CEC/ECMO. Correction demandée : rendre explicite la substitution sans attendre si probabilité intermédiaire et test indisponible dans la journée. Première extraction coupait la condition ; auteur a fourni le passage continu exact, personnellement relu. Version finale précise aussi fonctions rénale/hépatique, risque hémorragique et prélèvements/conservation avant alternative. |
| Sources | Références DX9 complètes désormais visibles dans Markdown ; preuves absentes initiales remplacées par pièces réelles. SHA concordants, sans inférence de vérité scientifique depuis seuls hashes. |

### Réserves persistantes

DX4 : sources datées2021–2024, aucune recommandation OMS originale actuelle lue ; note de cadrage HAS2026 non traitée comme recommandation. Seuils transfusionnels ne forment pas un protocole de SCA, hémorragie massive ou hémoglobinopathie. Aucune notice AIPS exacte ni dose médicamenteuse vérifiée. DX9 : PNDS et TIH partiellement lus ; résumé suisse2020 insuffisant pour autoriser un médicament ou une dose de substitution. AIPS Privigen juillet2025 contrôlé sur sécurité ciblée seulement, pas validation d'un schéma posologique. Les deux cours restent adultes hors grossesse/pédiatrie. Toute extension substantielle nécessite nouvelle contrelecture.

## Complément final — concordance HTML ciblée

Extraction réelle par `harness/cache_controles.py extraire` de DX4P9,11 et DX9P11,12 avec fenêtres liées, puis lecture effective. Contrôle DOM des notices sources et liens externes ; pas de lecture intégrale des HTML. Root déclare contrôles statiques et quatre configurations navigateur réussis ; ils ne sont pas revendiqués comme exécutés par cet auditeur.

| HTML final | Octets | SHA-256 exact |
|---|---:|---|
| `LOT_133_Phase_B_V0_DX.4.html` | 106954 | `a5c2c22ae1a16772a8190be1f7b4232393e80d49b16a40026181a0e7bdea1e61` |
| `LOT_133_Phase_B_V0_DX.9.html` | 103078 | `aaa708fe0168aaf104c0aca2d31eba1cb8dad13141af045ee6a84ee4d29e7468` |

DX4P9 conserve l'attribution TSAT ciblée à mediX, l'absence de systématisme, les limites ferritine/TDA et l'exploration médullaire raisonnée. DX4P11 conserve le contexte postopératoire stable des seuils, l'exclusion d'une transposition à l'hémorragie/SCA, la réévaluation transfusionnelle et les réserves AIPS sans dose. Les cinq notices sources conservent dates dans les titres, portées de lecture et réserves de fraîcheur.

DX9P11 conserve les distinctions PTI/MAT/CIVD, la sécurité spécifique Privigen et l'absence de dose. DX9P12 conserve la correction probabilité intermédiaire + test indisponible dans la journée → substitution sans attendre, prélèvement avant alternative et évaluation spécialisée. Les sept notices conservent dates, limitations (notamment résumé suisse S5), complément continu S6 et AIPS juillet2025.

**Verdict complémentaire : concordance ciblée recevable pour intégration préparatoire aux SHA HTML précités.** Aucun blocage supplémentaire identifié dans ce périmètre. Les limites du rapport persistent : pas de validation clinique, pas de contrôle exhaustif des autres parties, pas de test d'interaction ou d'iconographie par cet auditeur.
