# Audit médical — tour de vérification V2, SY-1 à SY-27 (14.11.2026)

Méthode : lecture de `CORRECTIONS_SYNDROMES_01_27.md` ; relecture des champs corrigés dans les 27 JSON. Les 39 AIPS citées ont été ouvertes par URL refdata (`aips_fiche.py fiche`), et chaque citation a été comparée au texte en cache, espaces et apostrophes normalisés. Toutes les citations sont retrouvées, y compris Trandate n° 41529 (mise à jour mars 2026), Iopidine n° 52813 (mai 2023), NaCl 10 % n° 29555, Itinerol B6 n° 18383, Firazyr n° 58178 et les deux lignes SCA de l'héparine n° 46613. Le contrôle a aussi porté sur les ajouts : contre-indications du mannitol et du timolol, grossesse sous Eliquis et Clexane, durées Rocephin, seuils de PA d'Actilyse.

## Verdict : **corrections requises** (1 critique nouvelle). Après le PATCH C7, le lot peut passer en **audit-ok**.

## Contrôle des 6 critiques et 7 graves du premier tour

| Défaut | Fiche | État | Contrôle par URL |
|---|---|---|---|
| C1 héparine SCA | SY-19 | Corrigé | « 60-70 U.I./kg PC (dose maximale : 5 000 U.I.) … 12 - 15 U.I./kg PC par heure (maximum 1 000 U.I. par heure) » ; STEMI : « 60 U.I./kg PC (maximum 4 000 U.I.) » ✓ |
| C2 labétalol | SY-25 | Corrigé | « 50 mg … injection intraveineuse lente (1 minute au minimum) … sans dépasser une dose globale de 200 mg » ✓ |
| C3 NaCl 10 % | SY-6 | Corrigé | Indications « Hyponatrémie. Hypochlorémie… » ✓ ; HTIC déclarée hors AIPS ✓ |
| C4 apraclonidine | SY-13 | Corrigé | « traitement d'appoint, lorsque l'efficacité d'autres médicaments antiglaucomateux s'est avérée trop faible » ✓ |
| C5 dimenhydrinate | SY-4 | Corrigé | Itinerol B6 : « Nausées et vomissements de toutes origines » ; « 1–2 supp. … ou 1–4 gélules » ✓ ; Trawell : « Traitement des maux de voyage » ✓ |
| C6 antibiotiques | SY-24 | Corrigé | Liste supprimée ✓ |
| G1 grossesse | SY-23 | Corrigé | Citations Xarelto, Eliquis et Clexane ✓ |
| G2 ticagrélor | SY-19 | Corrigé | Réserve ESC 2023 marquée « non relu » (honnête) |
| G3 prednisolone | SY-14 | Corrigé | « hors AIPS » figure aussi dans la synthèse orale ✓ ; dose de l'essai encore « À vérifier » |
| G4 ceftriaxone | SY-5 | Corrigé | 4 g/j (maximum AIPS) ; écart ESCMID signalé ✓ |
| G5 timolol, pilocarpine | SY-13 | Corrigé | Contre-indications Timoptic ✓ ; contradiction Spersacarpine signalée ✓ |
| G6 icatibant, nourrisson | SY-15 | Corrigé | « une injection unique de Firazyr 30 mg en sous-cutanée … 6 heures plus tard » ✓ |
| G7 esmolol | SY-25 | Corrigé | « L'utilisation de Brevibloc est réservé au traitement per- et postopératoire immédiat » ✓ |

## Défaut nouveau — PATCH exact

| # | Gravité | Emplacement | Extrait | PATCH | Source lue |
|---|---|---|---|---|---|
| C7 | Critique (règle §23 : « À vérifier (AIPS) » sur une molécule du corpus) | SY-21 management[4] | « hydrocortisone si une insuffisance surrénalienne aiguë est l'étiologie retenue (dose : AIPS non lue, À vérifier) » | Remplacer par : « hydrocortisone (indication « Choc dû à insuffisance corticosurrénalienne ») : « Dans les cas d'urgence, le traitement initial se fera de préférence par injection intraveineuse » ; « Des doses initiales allant jusqu'à 100 mg doivent être administrées par voie intraveineuse en 30 secondes au minimum » ; doses suivantes « à des intervalles de 2, 4 ou 6 heures selon la réponse et l'état du patient » (AIPS Solu-CORTEF® (hydrocortisone) n° 23533, mise à jour octobre 2025, lu le 14.11.2026). L'AIPS ne fixe pas de dose pour la crise surrénalienne : schéma de l'endocrinologue. » | AIPS Solu-CORTEF, URL refdata 521df69c…-fr.html |
| L8 | Léger | SY-27 examens[0] et [1] | « renvoi » : « IMG-132 » deux fois | Laisser IMG-132 sur l'échographie et retirer ce renvoi de la radiographie, ou citer l'IMG propre à la radiographie. | — |
| L9 | Léger | SY-13 management[1] | Mannitol ajouté sans ses contre-indications (elles ne figurent qu'en SY-6) | Ajouter : « contre-indications AIPS : « Insuffisance cardiaque. Congestion pulmonaire marquée/oedème pulmonaire. Déshydratation importante » » (AIPS Mannitol 20% B. Braun n° 31754) ✓ lu. | AIPS lue |

## Arbitrage du botulisme (SY-10) : **I (infectieux)**, pas F

Le botulisme est une toxi-infection à *Clostridium botulinum*. La forme alimentaire est une intoxication par la toxine préformée ; les formes du nourrisson et des plaies sont de vraies infections. La lettre F (fonctionnel, métabolique) ne convient pas : la cause est un agent biologique, et non un trouble métabolique.

PATCH SY-10 `etiologies` :
- Retirer « botulisme (toxine : bloc présynaptique) » de l'entrée « F (fonctionnel, métabolique) », puis écrire `"causes": ["—"]`.
- Ajouter à l'entrée « I (infectieux) » : « botulisme (toxi-infection à *Clostridium botulinum* : la toxine bloque la libération présynaptique d'acétylcholine) ».

## Restes acceptés (marqués « À vérifier », non bloquants)

- Cibles ESC, ESCMID, EFNS, BTS et Surviving Sepsis non relues.
- Dose quotidienne de l'essai de Sullivan 2007 absente.
- Recommandations SSI non lues.

Ces points sont signalés honnêtement dans les fiches ; il faudra les sourcer au prochain passage.

Question finale : **non** tant que C7 reste ouvert ; **oui** après C7 et l'arbitrage du botulisme.
