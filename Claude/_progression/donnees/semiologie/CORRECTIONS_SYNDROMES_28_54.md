# Corrections — Syndromes SY-28 à SY-54 (14.11.2026)

Réponse à `AUDIT_SYNDROMES_28_54.md`. Les doses ont été relues par URL refdata avec `Claude/_harnais/aips_fiche.py fiche` et citées mot pour mot. Les 27 JSON passent `json.load`. Ni commit ni push.

## Critiques
| # | Fiche | Correction appliquée |
|---|---|---|
| C1 | SY-54 | La fiche cite désormais l'AIPS Insulines Humaines HM Novo Nordisk (n° 44610, avril 2026), qui autorise la voie IV : « Seul Actrapid HM (solution d'insuline) peut être administré par voie intraveineuse », perfusion stable de 0,05 à 1,0 UI/ml. Le débit de 0,1 U/kg/h vient de JBDS 2011 (résumé secondaire) et suit le protocole hospitalier. |
| C2 | SY-47 | L'aspirine en prévention est classée hors AIPS : l'Aspirine Cardio (n° 51795, mars 2026) n'a que des indications cardiovasculaires. La dose renvoie à l'Expertenbrief SGGG n° 80, non lu en entier. |
| C3 | SY-47 | Labétalol : la fiche cite la dose « jusqu'à une dose de 160 mg/h » et la contre-indication « Antécédents d'asthme bronchique ou de bronchopneumopathie obstructive » (Trandate n° 41529, mars 2026). |
| C4 | SY-45 | Co-trimoxazole : 1 comprimé de Bactrim forte matin et soir, « à intervalles de 12 heures » (Bactrim forte n° 48306, mars 2023). |
| C5 | SY-53 | Hydrocortisone orale : « 10 à 20 mg par jour, parfois davantage, avec 4 à 6 g de chlorure de sodium ou un minéralocorticoïde » (Hydrocortisone Galepharm n° 57970, août 2025). |
| C6 | SY-32 | Métronidazole IV : 15 mg/kg, puis 7,5 mg/kg toutes les 6 h pendant 3 jours, puis toutes les 12 h ; la péritonite figure dans les indications (Metronidazol i.v. B. Braun n° 48018, février 2026). |
| C7 | SY-36 | Furosémide oral : ½ à 1 à 2 comprimés de 40 mg par jour, entretien ½ à 1 comprimé (Lasix comprimés n° 30629, mai 2025). |
| C8 | SY-29, SY-47 | L'AIPS du sulfate de magnésium « Bichsel » (n° 56394, octobre 2025) figure bien au corpus ; la mention fausse « absente du corpus » est retirée. |
| C9 | SY-28, SY-48 (aussi SY-32, SY-43) | La morphine IV est nommée et dosée : « injecter lentement 2 – 10 mg », maximum 100 mg/j (Morphini HCl Streuli n° 56554, janvier 2026). |

## Graves
| # | Fiche | Correction appliquée |
|---|---|---|
| G1 | SY-42 | L'hyperkaliémie est chiffrée et traitée par étapes (RMS 2007 et 2018, lus) : modérée de 6,1 à 6,9 mmol/l, sévère dès 7 mmol/l ; onde T pointue entre 6 et 7 mmol/l. Si l'ECG est modifié : calcium (gluconate 10 %, 10–20 ml), puis insuline-glucose (10 U dans 500 ml de G10 %, hors AIPS), puis salbutamol (hors AIPS). L'AIPS d'un gluconate de calcium injectable est absente du corpus, donc « À vérifier ». Critère de dialyse : K⁺ > 5,5 mmol/l (HUG 2024). |
| G2 | SY-54 | RMS 2019, lu en entier, ne chiffre ni le seuil de K⁺ ni le volume de NaCl. La fiche retient donc les valeurs de JBDS 2011 (résumé secondaire) : K⁺ < 3,3 mmol/l, insuline différée ; de 3,3 à 5,3 mmol/l, potassium ajouté ; glucose 10 % sous 14 mmol/l. Le NaCl 0,9 % à 1 l la première heure reste « À vérifier » (JBDS non lu). Le KCl est cité selon l'AIPS Kaliumchlorid B. Braun (n° 29552) : 10 mmol/h au maximum si K⁺ > 2,5 mmol/l. Les critères diagnostiques de RMS 2019 sont complétés. |
| G3 | SY-29, SY-30, SY-31 | La cible de SpO2 du BPCO est fixée à 88–92 %, avec la citation de la stratégie HUG BPCO 2026. |

## Moyens et légers
- **M1** : les dates d'AIPS sont remplacées par la date de « mise à jour de l'information » ; celle d'Atrovent est octobre 2024.
- **M2** : SY-50 cite la contre-indication de l'Inderal (asthme, bronchospasme).
- **M3** : SY-28 cite ERC 2021 (non lu) ; aucune source suisse n'a été trouvée.
- **M4** : SY-32 et SY-36 retiennent un seuil de PNN > 250/mm³ (EASL 2018, résumé secondaire) et une compensation de 6 à 8 g d'albumine par litre au-delà de 5 l. La dose d'albumine renvoie à l'AIPS Albumin CSL 20 % (n° 52476).
- **M5** : SY-48 donne les taux de nécrose, 30 % après 6 h et 80 % après 12 h, et déconseille la détorsion manuelle (RMS 2017, lu).
- **M6** : dans SY-39, SY-40, SY-41 et SY-52, les mentions « molécule et dose À vérifier » sont supprimées et la décision est renvoyée au spécialiste.
- **L1** : le crédit de SY-35 est aligné sur Commons (auteur inconnu, CDC PHIL).
- **L4** : SY-31 cite le schéma de surdosage de la naloxone, 0,4 à 2 mg (Naloxon OrPha).
- **L5** : SY-38 ajoute l'érythromycine avant l'endoscopie (ESGE, non lu), classée hors AIPS (Erythrocin i.v. n° 20258).

## Images
- **SY-35 et SY-50** : chaque image est recadrée sur un seul œil et vérifiée à l'œil ; aucun visage n'est identifiable. Le recadrage est signalé dans le crédit, comme l'exige la licence CC BY 3.0 de SY-50.
- **SY-51** : la photo est retirée et le fichier supprimé, car le visage restait identifiable malgré le bandeau. Elle est remplacée par un « a_fournir ».
- **L3** : les licences de SY-36, 37, 41 et 52 avaient été lues dans `extmetadata` lors du premier passage : CC0, CC BY 2.0, CC BY-SA 3.0 et CC BY 2.5.

## Restent « À vérifier » (sans dose AIPS lisible en jeu)
- seuils classiques de PaO2 et de PaCO2, de protéinurie et de sévérité tensionnelle
- délai de contrôle de la TSH
- corticothérapie de maturation fœtale
- délai d'endoscopie dans l'hémorragie variqueuse
- schéma de l'infection génitale haute (IUSTI 2017)
- AIPS du gluconate de calcium injectable, absente du corpus

## Tour 2 (réponse à AUDIT_SYNDROMES_28_54_V2.md)
- **G4, SY-54** : les seuils de potassium suivent désormais le PATCH mot pour mot.
  - Paliers : K⁺ > 5,5 mmol/l, pas de potassium ; 3,5–5,5 mmol/l, 40 mmol de KCl par litre ; < 3,5 mmol/l, avis senior et potassium supplémentaire. La fiche les attribue à JBDS (source britannique, via des protocoles secondaires, texte non lu, À vérifier).
  - La concentration de 40 mmol/l est conforme à l'AIPS Kaliumchlorid B. Braun n° 29552.
  - Le seuil d'insuline différée < 3,3 mmol/l est attribué à l'ADA (source américaine : Kitabchi 2009, non lu), ajoutée aux sources.
- **L1** : la mention « (en perfusion continue) » suit désormais le maximum de 100 mg/j de morphine dans SY-28, 32, 43 et 48.
- **L2** : le renvoi à la posologie pédiatrique est supprimé de SY-48 ; la dose adulte s'applique au cas de 14 ans.
- **L3** : les images n'ont pas pu être recadrées depuis l'original en pleine résolution.
  - Wikimedia a refusé le téléchargement (HTTP 429, « robot policy »).
  - SY-50 : l'original ne fait que 300 px, et le recadrage de 120 px est donc le maximum possible.
  - SY-35 : à refaire depuis la vignette de 960 px dès que l'accès est rétabli.
- **L4, SY-42** : le premier drapeau rouge précise « hyperkaliémie réfractaire ».
- Les 27 JSON passent json.load. Ni commit ni push.
