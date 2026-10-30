# JOURNAL_DX1 — LOT_014 — Phase B — DX.1 Cardiopathie ischémique (syndrome coronarien aigu ou cicatrice d'infarctus)

Rédacteur Phase B DX.1, 30.10.2026 (Europe/Zurich). Fichier : `LOT_014_Phase_B_V0_DX.1.html`, 121 753 octets, SHA-256 `92b9e78c309d59f6ae8521b0338b28e684a0a0263e798e41489579c7f9b4d230`. `controle_lot.py verifier --sans-nom` : 0 critique, 0 avertissement pour ce fichier ; 25 fenêtres popover ; 14 points.

## Hypothèses et décisions (une ligne chacune)

- Aucune recommandation suisse propre au SCA trouvée : le fichier applique ERC 2025 (relais SRC), ESC 2023 (lu par WebFetch, citations ≤ 125 caractères) et le commentaire DGK 2024 pour les classes de recommandation, car les tableaux ESC sont des images.
- Classes ESC 2022 (DAI, gilet, ablation, autopsie) lues dans la Pocket-Leitlinie DGK 2022, adaptation allemande de l'ESC 2022 : `evidence/DX1_DGK2022_Pocket_VA_KHK.txt`.
- Discordance HUG 2023 (« un décès toutes les trente minutes », ≈ 17 520/an, calcul dérivé) contre OFS 2024 (6 354 décès par cardiopathie ischémique) : le fichier retient l'OFS et signale la discordance.
- Durée de double antiagrégation : ESC 2023 = 12 mois ; AIPS Efient (59136) = « 15 mois » ; AIPS Brilique (61389) = « au moins 12 mois » : les trois textes sont cités sans trancher.
- Température après ROSC : ERC-ESICM 2025 ≤ 37,5 °C ; ESC 2023 (DGK) fièvre > 37,7 °C : divergence présentée dans une fenêtre.
- AAS i.v. : l'AIPS Aspirine Cardio (51795) prévoit 200–300 mg i.v. ou oral dans l'infarctus ; la seule forme i.v. du corpus (47256) n'a qu'une indication antalgique : écrit tel quel.
- Héparine : doses du SCA prises dans l'AIPS Heparin-Na B. Braun (46613), seule héparine du corpus lue avec un schéma SCA ; calendrier aPTT pris dans Heparin Sintetica (67780).
- Métoprolol : l'AIPS Beloc ZOK (52110) n'a pas d'indication post-infarctus ; la dose d'entretien vient de Beloc i.v. (56191).
- Cordarone (41060) chez l'enfant : le document lié contient à la fois « ni l'administration ni la sécurité … n'ont été étudiées » et « n'est pas recommandée » (alcool benzylique) ; le fichier retient « non recommandée » (correction d'audit n° 6 de la Phase A, vérifiée le 30.10.2026).
- LPGA art. 3/4 : l'infarctus est présenté comme maladie par lecture des définitions ; la jurisprudence n'a pas été consultée et le fichier l'écrit.
- LCR art. 15d : état au 01.04.2025, car le HTML de la version au 01.07.2026 (présente dans la base SPARQL Fedlex) n'est pas publié dans le filestore le 30.10.2026.
- AECVP 2017 tableau 3 : les trois premières lignes « coronary artery disease » sont sûres ; la ligne « incertain » du fichier donne seulement des exemples (lecture de colonnes ambiguë au-delà de la 3e ligne).
- Exemple de certificat « mort naturelle » d'un coronarien connu (point 11) : application de l'IRM-UZH 2026 §4.1, présentée comme exemple, avec la condition de récusation OEC art. 89.
- PCSK9 : sigle non développé dans les sources ; le fichier le décrit d'après le mécanisme de l'AIPS Repatha (65622), sans dose.
- SGLT2, GLP-1 : sigles non développés dans une source lue ; retirés du fichier.
- Extraits AIPS mis en cache le 30.10.2026 : 51795, 47256, 61389, 59136, 54509, 46613, 49456, 55937, 55418, 46461, 55459, 40558, 51039, 56191, 54085, 53875, 57147, 60955, 52710, 67780, 65622 ; extrait complémentaire d'Actilyse (posologie de l'infarctus) dans `evidence/DX1_AIPS_SCA_extraits.txt` sans modifier `.cache/aips/48313.txt`.
