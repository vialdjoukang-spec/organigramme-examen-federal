# Audit médical 9 — LOT_103 Phase A (S7.9 Troubles de la sensibilité)

- Date : 15.11.2026. Contre-auditeur neuf, lecture seule. Base : `6cf7490dae5a7e2a4de85c75551bcc306cbe3448`.
- Fichier : `Grokbot/LOT_103/LOT_103_Phase_A_V0.html`, 109 027 octets, SHA-256 `ca8b589aafa7e1771575c0e00205ae8f6a747db036eaf172d1c68b9a908e2d1b`.
- Liste : `LISTE_DX_CANONIQUE.md`, non gelée par le rédacteur. Question finale : **oui**. Gel : possible, non signé ici.
- **Verdict : CONFORME. Score : 100/100.** Critiques : 0. Graves : 0. Mineurs : 3.
- Grille Θ3 (2, 1 ou 0) : p1 à p14 = 2. Somme 28/28.

## Portes

`controle3.py --script-ok` : VERT, 109 027 octets, 395 phrases, connecteur 32 %, paragraphes sans connecteur 0, aucun défaut. `verif_aips.py` : OK, 0 AIPS citée. `aips_fiche.py verifier` : 0 défaut bloquant. `abreviations.py` : 0 sigle non développé. « car » : 0. Aucune phrase dupliquée. Pas de cheville pour franchir 35 %. Aucun milligramme.

## Liste

Les dix noms sont des maladies concurrentes. E1 attaque, E2 Guillain-Barré, E3 myélopathie cervicale, E4 vasculite provisoire suivent le délai et la létalité lus. Le rang 1 (3,8 %, dénominateur dit) et le rang 2 (30 à 40 % des polyneuropathies) sont honnêtes. Les rangs 3 à 10 n'ont pas de cohorte commune : le texte le dit, donc ce n'est pas un Grave. La lombalgie irradiée et la neuropathie des chimiothérapies ne sont pas numérotées.

## Ce qui a été ouvert et qui tient

NHS England, PDF 2025, pages du Guillain-Barré : diagnostic hospitalier du syndrome ou d'une variante, puis « Significant disability (Hughes Grade 4) OR Disease progression towards intubation and ventilation OR mEGRIS score ≥ 3 OR Poor prognosis mEGOS ≥ 4 ». Exclusion lue : formes légères et/ou non progressives sans intubation. Miller Fisher : pas d'immunoglobuline habituelle, sauf chevauchement avec faiblesse. Le cours reprend les quatre « ou », Hughes 4 inclus, et il ne recopie pas les 2 g/kg.

StatPearls NBK507888 : le trajet dorsal croise par les fibres arquées internes dans le bulbe, puis le lemnisque atteint le thalamus et le gyrus postcentral. NBK507824 (14.08.2023) : synapse dans la substance gélatineuse, croisement dans la moelle vers le côté opposé, montée antérolatérale, thalamus, gyrus postcentral. Les phrases du point 3 y figurent. Le trajet du pied au plexus n'est plus là.

IASP 2011 : paresthésie = sensation anormale, spontanée ou évoquée, et le mot vise ce qui n'est pas désagréable. EAN/PNS 2023 : immunoglobulines ou échanges si le patient ne marche plus sans aide ; compte jusqu'à 20 ; chute de capacité vitale forcée de plus de 30 % en 24 heures. Atroshi 1999 : 14,4 %, 3,8 %, 4,9 %, 2,7 %, 2 466/2 960, 18,4 % des 125 témoins. Obsan, OFS 2023, Société suisse de la SEP, Espagne 2024, Keddie 2021 (1,65 à 1,88), Spijker (9,4, 17,2, 53/103) et les trois revues suisses tiennent sur les extraits relus. OpenStax, fichier Wikimedia 1313, CC BY 4.0, schéma en couleur puis lame : pas un SVG, pas une image générée. Eurorad 18806 et 18552 restent des liens.

## Anciens défauts (audits 1 à 8)

Le grave de l'audit 8 est corrigé : le croisement cite NBK507888 et NBK507824, plus la revue de 2019. Les deux mineurs de l'audit 8 sont corrigés : Miller Fisher est dans la cellule NHS, et la toux avec le compte cite l'EAN. Le grave de l'audit 7 ne revient pas : le seuil n'est plus celui de Keddie. Les graves des audits 1 à 6 ne sont pas revenus : 83,2/100 000, rapport 1,6, décomptes 2022 et fourchette SEP 2016 absents ; 15 % et 23,1/1 000 séparés ; Liège ne fixe pas l'opération ; aucun milligramme ; queue de cheval seulement dans le cas Eurorad.

## Critique

Aucun. Aucune dose en milligrammes, aucune conduite contraire à l'AIPS ou au PDF 2025.

## Grave

Aucun.

## Mineur

1. **Le couple doigt/orteil devient un « ou ».** « la limite inférieure au doigt ou à l'orteil est de 6,9/5,5 entre 20 et 39 ans ». Bernard-Valnet, 20.11.2019, écrit « doigt/orteil » pour 6,9/5,5, puis 6,2/4,7 : le doigt a le premier chiffre, l'orteil le second. Correction : « la limite inférieure est de 6,9 au doigt et de 5,5 à l'orteil entre 20 et 39 ans ». Phrase suivante : « Entre 40 et 60 ans, cette limite passe à 6,2 au doigt et à 4,7 à l'orteil, sans qu'il s'agisse encore d'une maladie ».

2. **Le confinement est écrit comme un fait, alors que Keddie le suppose.** « parce que le confinement a réduit des pathogènes qui précèdent le syndrome, comme Campylobacter ». Keddie, Brain 2021, écrit que la baisse « may be » l'effet du confinement sur Campylobacter et les virus respiratoires, et il le présente comme une hypothèse. Correction : « On demande une infection récente, parce que des pathogènes comme Campylobacter précèdent le syndrome, et le confinement a pu en réduire la transmission ».

3. **« Guérissent » dépasse « s'amender ».** « puisque plus de 90 % guérissent sans chirurgie ». Schaller, 25.11.2015, écrit que plus de 90 % des patients « voient leurs symptômes s'amender sans chirurgie ». Correction : « puisque plus de 90 % voient leurs symptômes s'amender sans chirurgie ».

Prompt L1 lu et appliqué.
