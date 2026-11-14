# Corrections — Syndromes SY-1 à SY-27 (14.11.2026)

Réponse à `AUDIT_SYNDROMES_01_27.md`. Toutes les doses ont été relues par URL refdata avec `aips_fiche.py` le 14.11.2026, y compris les AIPS Trandate (n° 41529) et Iopidine (n° 52813), dont le cache, vide jusque-là, a été rechargé. Les 27 JSON se rechargent avec json.load. Ni commit ni push.

## Critiques, graves, moyens et légers appliqués

- C1, G2 — SY-19 : héparine remplacée par les lignes AIPS « angor instable/NSTEMI » et « STEMI avec fibrinolytique » ; réserve ESC 2023 sur le prétraitement par ticagrélor.
- C2, G7 — SY-25 : labétalol cité d'après l'AIPS Trandate n° 41529 ; esmolol déclaré hors AIPS (phrase de l'AIPS citée) ; cible ESC 2024 À vérifier.
- C3, M2 — SY-6 : NaCl 10 % B. Braun n° 29555 cité (HTIC hors AIPS) ; écart du mannitol signalé et contre-indications ajoutées.
- C4, G5, M2 — SY-13 : apraclonidine hors indication (Iopidine n° 52813) ; contre-indications du timolol citées ; contradiction de l'AIPS Spersacarpine signalée ; mannitol ajouté.
- C5 — SY-4 : méclozine (Itinerol B6 n° 18383) à la place du dimenhydrinate, limité au mal des transports (Trawell n° 43194).
- C6 — SY-24 : liste des cinq antibiotiques supprimée (règle § 23) ; L4 : Libman-Sacks reformulé comme diagnostic différentiel.
- G1, L5 — SY-23 : contre-indication du rivaroxaban et non-recommandation de l'apixaban pendant la grossesse ; énoxaparine ; Wells précisé (2 points, version à deux niveaux).
- G3, L7 — SY-14 : prednisolone dite hors AIPS aussi dans la synthèse orale ; Sullivan 2007 résumé lu (10 jours, dose non donnée) ; réserve sur l'identifiabilité du visage.
- G6 — SY-15 : icatibant (Firazyr n° 58178) pour l'angio-œdème héréditaire ; nourrisson : compressions thoraciques.
- G4, M9 — SY-5 : ceftriaxone adulte 4 g/j (maximum AIPS) contre 2 g × 2 (ESCMID), durées AIPS ; délais OFSP non chiffrés.
- M9, L4 — SY-12 : seuils de PA de l'AIPS Actilyse ; simulateurs reformulés comme diagnostic différentiel.
- M1 — SY-3 : écart thiamine AIPS (≤ 200 mg/j) / EFNS signalé.
- M3, L4 — SY-21 : cible PAM ≥ 65 mmHg et hydrocortisone (À vérifier) ; anaphylaxie médicamenteuse laissée en I, anaphylaxie non médicamenteuse en A.
- M4, L6 — SY-27 : critères de Light et pH < 7,2 (À vérifier) ; légende de l'image précisée.
- M5 — SY-17 : seuils NT-proBNP/BNP ajoutés (ESC 2021, À vérifier).
- M6, L1 — SY-1 : synthèse orale corrigée ; légende de l'image corrigée.
- M7 — SY-26 : amoxicilline 3 g/j précisée (borne haute AIPS).
- M8 — SY-7, SY-10, SY-11 : sources complétées (script USZ Neurostatus non récupéré, mention honnête). L4 SY-10 : botulisme laissé en F avec mécanisme (toxique) — À discuter : il pourrait aller en I (infectieux).
- L2 — SY-2, SY-20 : renvois en double supprimés (DaTSCAN, ECG).
- L3 — SY-9 : repère « genou » (À vérifier).
- L4 — SY-18 : infarctus du VD en V ; péricardite constrictive laissée aux diagnostics différentiels seulement.
## Restes « À vérifier »

- Les cibles et seuils européens (ESC 2021, ESC 2023, ESC 2024, ESCMID, EFNS, BTS, Surviving Sepsis) sont repris sans relecture des textes.
- La dose quotidienne de prednisolone de l'essai de Sullivan 2007 manque : le résumé lu via PubMed ne la donne pas.
- Les recommandations suisses (SSI, Société suisse de neurologie) n'ont pas été lues, et le script USZ Neurostatus n'a pas été récupéré.
- La dose d'hydrocortisone (SY-21) et l'icatibant hors AOH (angio-œdème sous IEC) restent à vérifier.

## Tour 2 (réponse à `AUDIT_SYNDROMES_01_27_V2.md`)

- C7 — SY-21 : l'hydrocortisone est citée mot pour mot d'après l'AIPS Solu-CORTEF® n° 23533 (octobre 2025), relue par URL refdata le 14.11.2026. Indication : « Choc dû à insuffisance corticosurrénalienne ». L'AIPS donne des doses initiales jusqu'à 100 mg IV en 30 s au minimum, puis des doses toutes les 2, 4 ou 6 h. Elle ne fixe aucune dose pour la crise surrénalienne : le schéma revient à l'endocrinologue.
- Botulisme — SY-10 : reclassé en « I (infectieux) » comme toxi-infection à Clostridium botulinum ; l'entrée « F » vaut désormais « — ».
- L8 — SY-27 : le renvoi IMG-132 est retiré de la radiographie et gardé sur l'échographie.
- L9 — SY-13 : les contre-indications AIPS du mannitol sont ajoutées (Mannitol 20% B. Braun n° 31754).
- Les 27 JSON se rechargent avec json.load ; ni commit ni push.
