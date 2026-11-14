# Contre-audit V2 : EXP_c.json (EXP-103 à EXP-153), 14.11.2026

**Version auditée** : EXP_c.json, 125 290 octets, SHA-256 `30990c8b…3cb5893` (commit 0b1145ad7). Je l'ai comparée par programme à la version V1 (`e3c5bc991`, SHA-256 `22c58c00…`). Le diff compte 209 changements.
**Méthode** : j'ai relu `CORRECTIONS_EXP_103_153.md`. J'ai confronté chaque correction AIPS au texte en cache de 8 AIPS (Gynipral 44438, Gonal-f 56689, Lucrin Dépôt 51903, Haldol 26891, Synacthen 31723, Viagra 54642, Utrogestan 45351, Prolia 60210). J'ai vérifié les 9 valeurs patchées. J'ai relu toutes les puces réécrites de `autres` (≈ 165), au-delà d'un simple échantillon.

## 1. Défauts V1 : statut

| V1 | id | Statut | Contrôle |
|---|---|---|---|
| C1 | 109 | corrigé | Gynipral : la citation « Administrer le contenu d'une ampoule … 5 à 10 minutes » est conforme au texte. La limite de 48 h est conforme. |
| C2 | 113 | corrigé, **1 défaut résiduel** | Gonal-f : la citation, les paliers de 37,5 UI et l'indication du groupe II de l'OMS sont conformes. Le clomifène est marqué honnêtement comme absent. En revanche, Gonal-f ne figure pas dans `sources` (voir P2). |
| C3 | 143 | corrigé | Lucrin : la citation 0,3 mg/kg et le tableau de doses par poids (7,5 / 11,25 / 15 mg) sont conformes. |
| C4 | 153 | corrigé | Haldol : la dose du sujet âgé (moitié de la plus faible dose, maximum à la moitié) et les trois contre-indications sont conformes. |
| G5 | 136 | corrigé, **1 nuance** | Synacthen : le gold (0 et 30 min) et la source sont conformes. Le mot « ou » trahit l'AIPS (voir P3). |
| G6 | 122 | corrigé, **1 incohérence** | La valeur normale est corrigée, mais `traces.normal` garde l'ancien seuil (voir P4). |
| G7 | 135 | corrigé | La source est maintenant ATS 2020 et elle est étiquetée « américaine ». |
| G8 | 114 | corrigé | L'AIPS mentionne bien « médicament libérant du monoxyde d'azote (p.ex. la molsidomine…) », donc « donneurs de NO » est exact. Le riociguat manque (voir P7). |
| M9 à M19 | — | corrigés | Utrogestan, Zometa, Prolia (citation conforme), crise surrénalienne hors AIPS, bolus de NaCl 3 %, OAC, Gastaldi, Garcia-Borreguero, Vesicare et traces chiffrées : tout est présent. |
| L20 à L22 | — | corrigés, **1 erreur nouvelle** | Les puces sont devenues verbales, avec une phrase fausse (voir P1). Le 4AT de rang 2 est remplacé par la CAM. La ligne SSGO est supprimée. |

**Compléments honnêtement marqués, donc non bloquants** : clomifène, oxybate, métyrapone, kétoconazole et urée (absents du corpus, je l'ai vérifié) ; bétaméthasone, MgSO4 et progestérone en obstétrique (« hors AIPS ; schéma : À vérifier (avis d'experts SGGG à identifier) ») ; OAC (« À vérifier sur fedlex »).

## 2. Valeurs patchées (9)

Les valeurs patchées de 106, 107, 116, 117, 124, 135 et 141 sont conformes au patch V1 et étiquetées. Le patch de 114 et celui de 122 sont conformes dans `valeurs_normales`, mais leurs `traces` restent incohérentes (P4, P5). Pour 141, la trace normale (≥ 10) et la trace pathologique (< 7) ne se recouvrent pas : une zone grise reste sans statut (P6).

## 3. Défauts restants et PATCH exacts

| # | Grav. | id · champ | Extrait actuel | PATCH exact |
|---|---|---|---|---|
| P1 | **Grave** (erreur nouvelle) | 137 · autres[2].pourquoi_pas_gold | « il exige une ponction lombaire » (cathétérisme des sinus pétreux) | `"il exige un cathétérisme veineux fémoral bilatéral jusqu'aux sinus pétreux"` |
| P2 | Moyen | 113 · sources | Gonal-f est absent de la liste. | Ajouter `"AIPS Gonal-f PEN n° 56689, août 2026, refdata (lu)"` |
| P3 | Moyen | 136 · valeurs_normales[0].valeur ; traces.patho | « > 500 (180 µg/l) ou hausse ≥ 200 (70 µg/l) » ; « … < 500 nmol/l et hausse < 200 nmol/l » | valeur : `"hausse ≥ 200 (70 µg/l), c.-à-d. > 500 (180 µg/l) à 30 min"` ; patho : `"Courbe plate : cortisol à 30 min ≤ 500 nmol/l"`. Raison : l'AIPS écrit « supérieure ou égale à 200 nmol/l […], c.-à-d. s'il dépasse 500 nmol/l ». Le « ou » ferait passer pour normale une hausse de 100 à 300 nmol/l. |
| P4 | Moyen | 122 · traces.a_chercher.normal | « TcPO2 normale > 50 mmHg au dos du pied » | `"TcPO2 ≥ 60 mmHg au dos du pied (pas d'ischémie)"` |
| P5 | Moyen | 114 · traces.a_chercher.normal | « pic systolique > 35 cm/s, diastole quasi nulle » | `"Doppler pénien après injection : pic systolique > 30 cm/s, télédiastolique ≤ 5 cm/s"` |
| P6 | Léger | 141 · traces.a_chercher.normal | « pic de GH ≥ 10 µg/l (ou ≥ seuil du laboratoire) » | `"Courbe de stimulation : pic de GH au-dessus du seuil du laboratoire (≈ 7 µg/l avec les dosages calibrés IS 98/574)"` |
| P7 | Léger | 114 · traitement[1] | « contre-indiqué avec les dérivés nitrés et donneurs de monoxyde d'azote » | Ajouter `" ou un stimulateur de la guanylate cyclase (riociguat)"`, qui figure dans les contre-indications de l'AIPS Viagra |
| P8 | Léger | 135 · sources | INOX est cité dans les valeurs, mais pas dans `sources`. | Ajouter `"Essai INOX, Lacasse Y et al., N Engl J Med 2020;383:1129-38 (protocole lu ; article non lu)"` |
| P9 | Léger | 122 · valeurs_normales[0].source | « IWGDF/ESVS/SVS 2023 (non lu) » pour les trois seuils | `"≥ 25 : IWGDF/ESVS/SVS 2023 ; ≥ 60 et < 30 : revue secondaire (non lus)"` |

**Échantillon des puces réécrites** : le sens est conservé dans ≈ 164 puces sur 165. Seule P1 est fausse. Quelques reformulations restent faibles sans être fausses : « elles se trompent souvent en réanimation » (145) ; « il complète les autres examens » (111, 147, 150), qui reste vague.

## 4. Verdict

**audit-ko (mineur).** Les 4 critiques et les 4 graves de V1 sont corrigés, avec des citations AIPS conformes au texte. La correction a introduit une erreur médicale nouvelle et grave (P1, la ponction lombaire attribuée au cathétérisme des sinus pétreux), et trois incohérences moyennes entre valeurs et traces (P3 à P5) restent ouvertes. Il faut appliquer P1 à P5. Je relis seulement ces 5 points et le lot passe en `audit-ok` ; P6 à P9 sont recommandés. Je n'ai rien modifié d'autre, ni commit ni push.
