# HELP — DX.8 Embolie pulmonaire (LOT_046, S2.7)

Molécules : monopréparations AIPS lues pour rivaroxaban (Xarelto 58728), apixaban (Eliquis 61549), enoxaparine (Clexane 49456),
héparine non fractionnée (Liquémine 15159, Heparin Sintetica 67780), alteplase (Actilyse 48313), edoxaban (Lixiana 65149),
phenprocoumone (Marcoumar 19395). Relance avec --autorisation 49456 61549 15159 65149 19395 (la première relance par --dci
n'avait lu que des génériques : Hepaxane, Apixaban Devatis, Rivaroxaban Viatris).

Sans AIPS lisible (classe et conduite sans milligramme dans le cours) : fondaparinux (Arixtra, 55937), dabigatran (Pradaxa, 61385),
noradrénaline, dobutamine.

Lacunes de sources (aucune phrase n'a été écrite sans extrait) :
- Épidémiologie suisse propre à l'EP (OFS, Obsan) non trouvée ; chiffres européens (ESC 2019) et genevois (HUG, TVP) utilisés.
- Chiffres ESC corrompus par l'OCR (« 39115 », « <_500 »...) : incidence annuelle, seuils NT-proBNP/lactate, 370 000 décès
  et 8,5 milliards d'euros écrits en toutes lettres ou omis ; à re-vérifier sur la version imprimée de l'ESC 2019.
- Prescription exacte du CTPA (protocole d'injection, produit de contraste) : non présente dans les sources lues.
- Auscultation et signes de surcharge droite à l'inspection (turgescence jugulaire, B2 claquant) : aucun extrait lu.
- Arrêt de travail, assurance et aspects sociaux de l'EP : aucune source suisse lue.
- Discrimination radio-clinique de l'anémie et du pneumothorax : traitée dans les DX.9 et DX.10, non sourcée ici.
- Divergence assumée : Clexane (AIPS) recommande l'HNF en cas d'EP sans TVP clinique, l'ESC 2019 préfère HBPM ou fondaparinux ;
  le cours suit l'AIPS et cite l'ESC comme divergente.

## Mise à jour après correction (2026-11-10)
- Pradaxa (61385), Arixtra (55937), noradrénaline (Noradrenalin Sintetica 67023) et dobutamine (Dobutrex 45687) ont une AIPS lue : la rubrique « sans AIPS » ci-dessus est caduque. Doses citées : Pradaxa 150 mg deux fois par jour après au moins 5 jours d'héparine, Arixtra 7,5/5/10 mg selon le poids, noradrénaline 8 à 12 µg/min (70 kg), dobutamine 2,5 à 10 µg/kg/min.
- LV8 : la grossesse (9.c, 11) cite l'ESC 2019 ; les ESC 2025 « maladies cardiovasculaires et grossesse » (chapitre TEV), plus récentes, restent à lire.
- Le contrôle de nombres (controle3) ne lit pas les extraits OCR où les colonnes sont collées (« >_75 », « e8.5 », « 370 … 000 », tableau « 0 0.35 0.21 ») : 10 phrases (370 000 décès, 8,5 milliards, 80 ans et plus, 75 ans et plus, 6 semaines post-partum, 0,35 % et 7,56 %) restent A_nombre_absent_de_l_extrait alors que les chiffres figurent bien dans l'extrait cité.
