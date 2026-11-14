# Contre-audit V2 : EXP-001 à EXP-051 (`enrichi/EXP_a.json`)

Auditeur indépendant, 14.11.2026. J'ai appliqué les skills `medecin-expert` et `expert-web`.
Version auditée : `EXP_a.json` du commit `5f0bd327f`, 155 471 octets. Le JSON est valide et contient 51 entrées.

**Ce que j'ai fait**
- J'ai lu `CORRECTIONS_EXP_001_051.md`.
- J'ai comparé par script la version V1 (commit `e3c5bc991`) et la version V2 : 32 entrées ont changé, et j'ai lu chaque champ modifié.
- J'ai relu par URL refdata le passage cité des AIPS suivantes :
  - Rivotril 37756, Depakine 34734, Atropine SDU Faure 46994 ;
  - Levetiracetam DESITIN cpr 65154, Synacthen 31723 ;
  - Eylea 2 mg 62393, Vabysmo 68395 ;
  - Eliquis 61549 (rubriques posologie et fonction rénale) ;
  - Prednisone Streuli 29349.
- J'ai relu les directives ASSM 2017 (texte intégral) et le projet ASSM 2025.

## 1. Critiques et graves de V1 : état

| Id | Vérification | État |
|---|---|---|
| C1 (007) | L'EEG est retiré des examens admis. Le seuil de 2 µV porte l'étiquette « source américaine ACNS ». La liste des examens admis est conforme à l'ASSM 2017 (perfusion-TC et angio-TC, Doppler transcrânien codé couleur, ASN, IRM). | **Corrigé**, avec une erreur d'attribution (N1) |
| C2 (007) | La date 2017 (approuvée le 16.05.2017, en vigueur depuis le 15.11.2017) est exacte. Le principe des quatre yeux et la PaCO2 ≥ 60 mmHg (8 kPa) sont conformes au texte de 2017. | **Corrigé** |
| C3 (002) | Les citations de Rivotril sont exactes au mot. L'ordre (1 mg, puis 1–4 mg, puis 0,25–0,5 mg/min, puis ≤ 10 mg) est fidèle. | **Corrigé** |
| C4 (001, 006) | La restriction et la contre-indication du valproate sont citées au mot ; l'indication « petit-mal/absences » est exacte. | **Corrigé** |
| C5 (016) | Atropine 0,5 % : indication, « 1 goutte 1 à 3 fois par jour », surveillance et blocage du canal lacrymal sont cités au mot. | **Corrigé** |
| G1 (008) | McDonald 2024 (Lancet Neurol 2025;24:850) : nerf optique comme 5e localisation, par IRM, OCT ou PEV. | **Corrigé** |
| G2 (009) | ERC-ESICM 2025 : fièvre ≤ 37,5 °C pendant 36–72 h, NSE > 60 µg/l maintenue, NSE < 17 µg/l comme prédicteur favorable. La source secondaire est déclarée. | **Corrigé** |
| G3 (048, 049) | ERC 2025 est cité. | **Corrigé**, mais l'étiquette de lecture est fausse (N2) |
| G4 (025) | Règle INFARCT exacte : un seul signe suffit ; le HINTS est limité au syndrome vestibulaire aigu continu. | **Corrigé** |
| G5 (016) | PEDIG porte l'étiquette « source américaine ». | **Corrigé** |
| G6 (006, 013) | **Synacthen** : je confirme que l'AIPS 31723 indique le « Syndrome de West » mais dit « L'utilisation et la sécurité … n'ont jusqu'à présent pas été étudiées chez l'enfant et l'adolescent ». Écrire « dose non citée » est donc exact, et mon PATCH V1 (« citer la rubrique Posologie ») est retiré. ACTH placée au même rang que la vigabatrine : correct. Les citations de Vabysmo et d'Eylea sont exactes au mot. | **Corrigé**, avec des dates fausses (N3) |
| G7 (035) | La mise en garde sur la myasthénie est citée au mot (AIPS 29349). | **Corrigé** |

Les moyens et légers de V1 sont aussi corrigés : M1–M9 et L1–L4, L6, L7.

**L5 (apixaban)** : le rédacteur a raison. Dans la FANV, l'AIPS Eliquis 61549 dit : « Indépendamment de la fonction rénale seule, une réduction de la posologie est nécessaire » seulement si au moins 2 critères sur 3 sont présents. Elle ajoute qu'apixaban « n'est pas recommandé » si la clairance est < 15 ml/min ou en dialyse. Mon PATCH V1 (réduire la dose à 15–29 ml/min) était faux et je le retire. Le texte V2 est conforme.

## 2. Défauts restants (nouveaux ou hérités de mon PATCH V1)

| # | Id · champ | Extrait (mot pour mot) | Gravité | PATCH exact | Source lue |
|---|---|---|---|---|---|
| N1 | 007 · `autres[0].quand`, `autres[1].quand` | « …ou si une lésion infratentorielle isolée est possible (ASSM 2017) » ; « déconseillé chez l'enfant (ASSM 2017) » | Moyen (l'erreur vient de mon PATCH V1) | Le texte de 2017 ne contient pas ces deux points : ils viennent du **projet 2025**. Écrire : `autres[0].quand` = « obligatoire si la défaillance du cerveau n'est pas suffisamment expliquée, si des facteurs potentiellement réversibles ne peuvent être exclus ou si l'examen des nerfs crâniens est impossible (ASSM 2017, ch. 3.2.1 et 3.3) ; le projet ASSM 2025 ajoute la lésion infratentorielle isolée possible ». `autres[1].quand` = « examen admis par l'ASSM 2017, à documenter sur les artères intra- et extracrâniennes ; réservé à des médecins expérimentés, en l'absence d'autres méthodes ; le projet 2025 le déconseille chez l'enfant ». `montre` = « pics systoliques < 50 cm/s ou signal biphasique (flux oscillant) ». | ASSM 2017, ch. 3.3 et annexe E ; projet ASSM 2025, annexe B |
| N2 | 048 · `traitement[0]`, `sources[3]` ; 049 · `sources[3]` | « ERC 2025, Adult Advanced Life Support ; amiodarone 300 mg après le 3e choc, 150 mg après le 5e » ; « — résumé » | Moyen | Je n'ai pas lu le chapitre ALS 2025 (erreur 403) et le moment de l'injection vient de mon PATCH V1. Écrire : « (Source européenne : ERC 2025, Adult Advanced Life Support, Resuscitation 2025 — non lu, À vérifier ; moment de l'amiodarone à vérifier) ». Même mention pour 049 (algorithme bradycardie). | Page des chapitres erc.edu (lue) ; texte non lu |
| N3 | 001 · `traitement[0]`, `sources[3]` ; 013 · `sources[2]`, `sources[3]` | « n° 65154, février 2025 » ; « refdata 24.09.2026 » ; « refdata 20.02.2026 » | Léger (DATE) | Mettre la date « Mise à jour de l'information » de chaque AIPS : Levetiracetam DESITIN cpr 65154 → « avril 2023 » ; Vabysmo 68395 → « octobre 2026 » ; Eylea 62393 → « septembre 2026 ». | AIPS 65154, 68395, 62393 (lues) |
| N4 | 001 · `traitement[0]` | « Adultes (≥18 ans) et adolescents (12 à 17 ans) de plus de 40 kg » | Conforme | La citation est exacte. Le libellé du comprimé diffère de celui de la forme pour perfusion (« dès 16 ans de 50 kg ») ; aucun patch. | AIPS 65154 |

Aucune nouvelle erreur de dose. Toutes les citations AIPS ajoutées ou corrigées sont exactes au mot.

## 3. Score §12.2 (7 critères × 2 = 14)

| Critère | V1 | V2 | Raison |
|---|---|---|---|
| Gold, 1re intention, ordre | 1 | 2 | 004, 007, 037 et 046 sont corrects |
| Lecture du tracé | 1 | 2 | HINTS exact ; gabarit EEG adapté au coma |
| Valeurs normales et unités | 1 | 1 | Aucune norme suisse (SGKN) ; plusieurs valeurs restent « À vérifier » |
| Calculs | 2 | 2 | 051 est désormais cohérent (indice chronotrope 56 %) |
| Syndrome et traitement (AIPS) | 0 | 2 | Aucune critique ; citations exactes |
| Actualité | 0 | 2 | ERC-ESICM 2025, McDonald 2024, EGS 2025 et ASSM datée |
| Sources étiquetées et honnêtes | 1 | 1 | N2 (« résumé » au lieu de « non lu ») ; SSC, SGKN et Swiss Resuscitation Council toujours « non lu » |
| **Total** | 6/14 | **12/14 = 86 %** | |

## 4. Verdict

**Refusé, de peu** : 86 % (sous le seuil de 90 %), zéro critique, zéro grave. Les 5 critiques et les 7 graves de V1 sont corrigés sans nouvelle erreur de dose.

Question finale : **non**, tant que N1 et N2 ne sont pas appliqués. Ce sont deux attributions inexactes, et elles viennent de mes propres PATCH V1.

Pour atteindre 95 % : appliquer N1 à N3, puis ouvrir au moins une source suisse pour les valeurs normales et une pour l'adoption des recommandations ESC/ERC (SSC, Swiss Resuscitation Council). Une fois N1 et N2 appliqués, la réponse devient « oui ».

## Clôture
N1 à N3 appliqués mot pour mot (tour 2) ; zéro critique et zéro grave restant : **audit-ok** pour EXP-001 à 051.
