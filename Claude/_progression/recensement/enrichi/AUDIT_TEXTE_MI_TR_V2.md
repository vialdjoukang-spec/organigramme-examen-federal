# Contre-audit V2 — champs texte de MI_TR.json après CORRECTIONS_TEXTE_MI_TR.md

Auditeur indépendant, 14.11.2026. Les images sont hors champ.

**Méthode (ce que j'ai fait)**
- J'ai relu dans `MI_TR.json` les 33 entrées touchées : gold, autres, traitement et sources.
- J'ai comparé chaque dose réécrite à l'AIPS déjà lue en V1, que j'ai relue par son URL refdata.
- J'ai ouvert deux nouvelles AIPS : Co-Amoxi-Mepha i.v. (n° 56758) et Zinacef (n° 41940).
- J'ai vérifié la date de COLCTAB et l'édition 2026 de la recommandation EAU sur le cancer de la prostate.

## 1. Défauts V1 : contrôle

| Classe | Résultat | Détail |
|---|---|---|
| Critiques (11) | **11/11 corrigés** | 290, 291, 308, 316, 324, 327 (×2), 332, 333 (×2) et 335 sont conformes à l'AIPS lue. La date COLCTAB « juin 2026 » est exacte : l'AIPS indique « ajout d'informations pertinentes pour la sécurité par Swissmedic : juin 2026 » |
| Majeurs (17) | **16/17 corrigés, 1 partiel** | Partiel : 296 et 315 gardent « doses À vérifier » alors qu'une AIPS au corpus répond (voir § 2) |
| Mineurs (10) | 10/10 traités | Deux mineurs nouveaux (voir § 3) |

Je n'ai trouvé aucune dose fausse introduite par la correction. Les points suivants sont exacts : TXA hors schéma AIPS (Stragen 65978, févr. 2024), Actemra® ACG débutante toutes les 2 semaines ou récidivante 1×/semaine (58868), CRYSVITA 0,4 mg/kg toutes les 2 semaines chez l'enfant et 1 mg/kg toutes les 4 semaines chez l'adulte (66801), vitamine D3 de 1000 à 5000 UI/j pendant 6 semaines (69997), et le gold 309 avec la radiographie au rang 3.

## 2. Point à trancher : *Kingella kingae* (296, 315), classé **Critique** car une AIPS du corpus répond

| AIPS lue | Indication ostéo-articulaire | Verdict |
|---|---|---|
| Co-Amoxi-Mepha i.v., n° 56758, mise à jour sept. 2026 | Oui : « Infections ostéo-articulaires : en particulier ostéomyélite, principalement causées par Staphylococcus aureus. » | Dose AIPS applicable |
| Zinacef (céfuroxime i.v.), n° 41940, mise à jour mai 2026 | Non : la liste ne contient ni os ni articulation. Elle ne cite qu'une prophylaxie en chirurgie orthopédique | Hors AIPS |

Citation de la posologie pédiatrique (Co-Amoxi-Mepha i.v., enfants de 3 mois à environ 12 ans ou 40 kg) : « Infections graves Jusqu'à 55 mg/kg (50 mg/kg d'amoxicilline et 5 mg/kg d'acide clavulanique) toutes les 6 heures en perfusion brève d'au moins 30 minutes. »

**PATCH 296, traitement[0], et 315, traitement[0]** : remplacer « amoxicilline-acide clavulanique ou céfuroxime (Paediatrica 34(4), 2023 : non vérifié CH, doses À vérifier) » par :
« amoxicilline-acide clavulanique i.v. jusqu'à 55 mg/kg (50 mg/kg d'amoxicilline) toutes les 6 h en perfusion d'au moins 30 min, infection grave de l'enfant de 3 mois à 12 ans (AIPS Co-Amoxi-Mepha i.v., n° 56758, septembre 2026) ; céfuroxime : hors AIPS dans l'infection ostéo-articulaire (Zinacef®, n° 41940, ne cite pas cette indication) ; choix de *Kingella* : Paediatrica 34(4), 2023, non vérifié CH ».
Ajouter aux sources : « AIPS Co-Amoxi-Mepha i.v. (refdata) ».

## 3. Défauts restants ou nouveaux

| Id | Gravité | Extrait → PATCH |
|---|---|---|
| 296, 315 | **Critique** | Voir § 2 |
| 327 | Mineur | « édition la plus récente (2025) » → « 2026 ». L'EAU a publié sa mise à jour en mars 2026 |
| 304 | Mineur | sources : ajouter « AIPS Clexane® (refdata) ». La ligne traitement la cite, mais la liste des sources ne la reprend pas |
| 341 | Mineur | La ligne traitement cite toujours « niveaux de référence diagnostiques (OFSP) », mais sa source a été retirée. Lire la directive de l'OFSP sur les niveaux de référence et la citer datée ; sinon écrire « (non vérifié CH) » |
| 308 | Mineur | Ajouter la limite de l'AIPS : « au maximum 6 mg par crise ; arrêt en cas de diarrhée ou de vomissements (AIPS COLCTAB®) » |

## 4. Retrait des 3 sources suisses non lues (293, 340, 341)

**Le retrait est acceptable** : il vaut mieux retirer une source que d'en citer une sans l'avoir lue (règle « rien d'inventé »). Ce n'est pas un défaut bloquant. La source suisse manque toutefois sur deux sujets d'examen : le dépistage échographique des hanches selon Graf (293) et le circuit de protection de l'enfant (340). Il reste à lire ces sources, puis à les réintroduire avec leur date. Le cas de 341 est en mineur au § 3.

## Verdict

**Corrections requises**, avec un seul point bloquant : le patch du § 2 (296, 315). Une fois ce patch appliqué, le texte de MI_TR peut recevoir `audit-ok`. Les mineurs du § 3 restent souhaitables mais ne bloquent pas.

## Clôture
Patchs du tour 2 appliqués mot pour mot (296, 315 Co-Amoxi-Mepha 56758 ; céfuroxime hors AIPS ; 304, 308, 327, 341) : **audit-ok** pour le texte de MI_TR (IMG-289 à 344).
