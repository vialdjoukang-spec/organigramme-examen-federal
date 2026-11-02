# Cohérence transversale ciblée — LOT133 — 0858

02.11.2026 UTC. Auditeur distinct `audit_0858`. Rapport préparatoire, sans score ni validation médicale humaine. Aucun fichier auteur ou registre partagé modifié.

## Périmètre réellement lu

Liste canonique et GUIDE du harnais lus. Extraction effective avec `python3 -B codex-LOTS-html/harness/cache_controles.py extraire` : Phase A points 2,3,4,8,9,11,12 ; DX1–4 et DX6–9 points 4,8,9,11,12 avec fenêtres liées. Les sorties DX2/DX3 initialement tronquées ont été complétées par une seconde extraction (DX2 P12 ; DX3 P4,8,9,11,12). Aucun HTML de plus de 50 Ko lu entier. Les points 2/3 des DX historiques, autres parties, QCM, images et interactions ne sont pas réaudités ici. Les sources et AIPS historiques ne sont pas nouvellement contre-lus par ce contrôle transversal : leurs audits antérieurs restent distincts.

DX5 et DX10 absents à ce premier constat : cohérence globale 1–10 encore ouverte. Le présent rapport doit être complété après remise et rendu.

## Concordances et différences interprétées

| Axe | Constats dans les extraits lus |
|---|---|
| Signe et diagnostic | Phase A distingue pâleur/Hb, purpura/numération ou sepsis, ictère/bilirubine puis obstacle, œdèmes/cause, hippocratisme/étiologie. DX4 confirme l'anémie par hémogramme ; DX9 demande contrôle technique/frottis, sépare PTI, MAT, CIVD et TIH. Aucun automatisme diagnostique opposé identifié. |
| Urgence | Phase A et DX1/2/3/4/6/7/8/9 priorisent défaillance, alerte et stabilisation. L'imagerie, les cultures, ADAMTS13 ou classification ne retardent pas les mesures urgentes. La régression du déficit ne supprime pas l'appel dans Phase A/DX1. |
| Purpura et infection | Phase A conserve la limite pédiatrique de sa source HUG ; le parcours adulte DX2 ne la transforme pas en protocole enfant. DX2 et DX9 reconnaissent sepsis/CIVD et cultures négatives possibles. Le seuil PTI récent <20 G/L est contextuel, pas un seuil universel de danger du purpura. |
| Gazométrie | Phase A indique son rôle pour oxygénation/ventilation/pH. DX3 précise qu'elle n'est pas préalable au traitement ni systématique pour toute dyspnée ; une SpO₂ fiable et le besoin d'oxygène peuvent objectiver l'IRA hypoxémique. Il s'agit d'une précision, pas d'une injonction contradictoire. |
| Hémolyse/ictère | Phase A oriente l'ictère et l'anémie ; DX4 distingue bilirubine non conjuguée/hémolyse et bilan causal. DX6 sépare terrain chronique, complication et déclencheur. L'ictère n'est pas assimilé systématiquement à l'obstruction. Comparaison DX5 encore requise. |
| Congestion et respiratoire | DX3 distingue IRA de novo, œdème cardiogénique et BPCO hypercapnique ; DX7 réserve oxygène à l'hypoxémie, assistance à l'indication, diurétiques à la congestion. Les sources et situations ne sont pas assimilées. Phase A et DX7 ont des consignes concordantes sur poids, souffle et urgence. |
| TVP | Phase A et DX8 utilisent probabilité prétest, D-dimères pour faible probabilité et échographie si vraisemblable. Le délai 5–7 jours après examen négatif avec suspicion persistante concorde. DX8 nuance selon examen limité/complet de bonne qualité ; le résumé Phase A n'énonce pas cette nuance, mais n'impose pas une clôture faussement rassurante. |
| Antithrombotiques | DX1 distingue prévention artérielle, anticoagulation cardioembolique et thromboprophylaxie ; DX8 ne transfère pas les réductions de dose de FA à la TVP. DX9 précise qu'une TIH peut être thrombotique et que HNF→HBPM n'est pas la substitution appropriée. Aucune contradiction identifiée dans ces passages. |
| Médicaments et doses | Phase A ne prescrit aucune dose ; cela n'interdit pas les schémas spécifiques des DX6 et DX8 avec notices dédiées. Réserves AIPS des autres traitements conservées. Cette comparaison n'est pas une nouvelle validation pharmaceutique des doses historiques. |
| Terrains et fréquence | Canonique adulte, grossesse/pédiatrie à part, dix exemples sans classement suisse de fréquence. La référence pédiatrique de Phase A est explicitement bornée. Aucun rang universel n'est déduit ici. |

## Défaut réel transmis

DX3 P8 comporte des marqueurs Markdown littéraux dans l'HTML extrait : « maintenir ces valeurs**. Il définit l’acidose hypercapnique par **pH ». Défaut de rendu identifié et transmis à root pour correction centralisée ; il ne modifie pas les seuils eux-mêmes. Aucun autre conflit clinique bloquant observé dans le seul périmètre lu. Cette absence de constat ne vaut pas audit exhaustif.

## Empreintes du premier état lu

| HTML | SHA-256 |
|---|---|
| LOT_133_Phase_A_V0.html | `5cd6b8a0ffe797989e08ab20b2b2b8127cb0a6d7118eb55e8a31ee4542767cee` |
| LOT_133_Phase_B_V0_DX.1.html | `d1081c88077c79478eae3f8564296dd48ce617c23be5044482278e4fb6e95636` |
| LOT_133_Phase_B_V0_DX.2.html | `2d8786b50e94b97db99b6fa2f62214b95bc9e72a10624b4f82697385bd63b798` |
| LOT_133_Phase_B_V0_DX.3.html | `31572cbe7f0d79922252eab93cfbb3cd890e1cd7dfa96861c4dae8b3a38bb461` |
| LOT_133_Phase_B_V0_DX.4.html | `a5c2c22ae1a16772a8190be1f7b4232393e80d49b16a40026181a0e7bdea1e61` |
| LOT_133_Phase_B_V0_DX.6.html | `edf67b89f32979be7a7b7fc59049cf7b7b9117c87117d6e61ed1bb8a752b6aa2` |
| LOT_133_Phase_B_V0_DX.7.html | `25000d74dde9338305030ee50338b54298027fc28dd5ac309cde5f559233f9fb` |
| LOT_133_Phase_B_V0_DX.8.html | `09d614dbfb7c8c1ffd1a0781de7526d3ea69088dc17fc93d8d688ef016c54c7b` |
| LOT_133_Phase_B_V0_DX.9.html | `aaa708fe0168aaf104c0aca2d31eba1cb8dad13141af045ee6a84ee4d29e7468` |

## Correction DX3 contrôlée

Root a corrigé centralement l'interprétation des comparateurs comme balises HTML, sans changer le Markdown clinique. Nouvelle extraction effective P8 : les marqueurs littéraux autour de la définition ont disparu ; PaO₂ <60 mmHg, SpO₂ <90 %, pH ≤7,35 et PaCO₂ >45 mmHg restent lisibles et inchangés. Concordance ciblée acquise. Les tests de rendu et 19 contrôles statiques sont rapportés par root, non exécutés par cet auditeur.

SHA HTML DX3 après correction : `31572cbe7f0d79922252eab93cfbb3cd890e1cd7dfa96861c4dae8b3a38bb461` (104964 octets). Le SHA du premier état ci-dessus est historique.

## Complément DX5 et DX10 après remise

Les deux nouvelles leçons ont été contre-lues sur Markdown (rapport `AUDIT_DX5_DX10_0858.md`), puis extraites effectivement en HTML : DX5 P4,9,11,12 ; DX10 P4,7,8,9,11,12. Leur P2/3 et les passages DX5P8, DX10P5/6 ont été lus en Markdown. Les corrections d'appel 144 sont présentes dans les deux HTML et distinguées d'une recommandation française.

| Comparaison | Constat ciblé |
|---|---|
| Phase A/DX5 | Ictère confronté à biologie, puis obstacle recherché par échographie, IRM ou écho-endoscopie selon les résultats. La CPRE n'est pas première exploration automatique de tout ictère. Triade douleur–fièvre–ictère incomplète possible, urgence sans attente d'un bilan électif. |
| DX2/DX5 | Infection avec défaillance : stabilisation et anti-infectieux sans délai induit ; prélèvements si non retardants et contrôle de source. Les délais ESGE2019 contextualisés de drainage ne deviennent pas permission de retarder réanimation/antibiothérapie. |
| DX4/DX5/DX6 | Anémie hémolytique, obstacle mécanique et hépatopathie décompensée ne sont pas assimilés sur l'ictère seul. Les examens ciblent mécanisme puis cause ; aucune simple couleur ne confirme le diagnostic. |
| Phase A/DX10 | Hippocratisme ne prouve pas le cancer ; scanner caractérise et guide le prélèvement, anatomopathologie confirme habituellement. Biomarqueurs/TEP/extension ne remplacent pas cette confirmation. |
| DX3/DX10 | Hémoptysie et obstruction centrale avec détresse donnent priorité aux voies aériennes et à l'oxygénation avant le bilan oncologique complet ; pas de scanner imposé avant stabilisation. |
| DX8/DX10 | Thrombose peut accompagner le cancer sans le prouver. Le syndrome cave peut relever de compression ou thrombose ; aucune anticoagulation universelle n'en est déduite. Les interactions et risques oncologiques restent à traiter dans la filière spécialisée. |
| Traitements et actualité | DX5 et DX10 ne proposent aucune dose. ESGE ancien attribué, TNM9 INCa2025 distingué du CEP2023 ; autorisations suisses et stratégies spécialisées restent réservées. |

**Conclusion préparatoire : aucune contradiction clinique bloquante identifiée dans les passages explicitement comparés de Phase A et DX1–10.** Cette conclusion couvre dix leçons présentes mais pas quatorze parties intégralement auditées par cet auditeur. Les contrôles globaux, interactions navigateur et éventuelles images sont distincts. Les sources anciennes/partielles et réserves posologiques demeurent ; aucun score ni validation médicale humaine.

Contrôle documentaire du rendu : DX10 conserve dates/portées/réserves des six sources. DX5 conserve portées/réserves des cinq sources mais son rendu initial omet `date_source` (HUG2025, ESGE2019 et2018) ; correction centralisée demandée avant clôture de concordance documentaire.

## Clôture documentaire ciblée

Omission des dates DX5 corrigée par root, puis notices DOM relues par l'auditeur : HUG2025-02-26, ESGE2019 et2018/actualisation2017 visibles ; les dates éditoriales SNFGE restent non établies. DX10 inchangé. Concordance préparatoire close aux empreintes suivantes ; les réserves et limites de périmètre précédentes restent applicables.

| HTML final ajouté | Octets | SHA-256 |
|---|---:|---|
| `LOT_133_Phase_B_V0_DX.5.html` | 104650 | `b022f2e3e478f506c195011a6658144539f169951509ca1731e3ac32d5aced73` |
| `LOT_133_Phase_B_V0_DX.10.html` | 94776 | `b382697cad749cefba4094920879fbd4c0efbe97c5e2296c7ded669bb1ea755a` |

La correction de rendu DX3 et la correction de dates DX5 sont les seuls défauts concrets détectés par ce contrôle transversal et ont été vérifiées après correction. La conclusion d’absence de contradiction clinique identifiée reste limitée aux extraits listés, sans audit exhaustif ni revalidation AIPS des dix leçons.
