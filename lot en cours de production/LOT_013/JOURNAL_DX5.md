# JOURNAL_DX5 — LOT_013 — Phase B DX.5 « Intoxication mortelle (drogues, médicaments, monoxyde de carbone) »

Rédacteur DX.5, 30.10.2026. Une ligne par hypothèse ou décision ; aucun score attribué par le rédacteur.

- Hypothèse — transposition §9.3 : point 3 = toxicologie mortelle et thanatologie utile ; tableau de corrélation à deux colonnes de conséquence (défunt : médico-légale ; vivant exposé : antidote).
- Hypothèse — point 11 : toutes les doses visent les vivants exposés (co-victimes de CO, surdose trouvée vivante, fumées, médicaments) ; aucune dose pour le défunt.
- Décision — AIPS lues dans le corpus local puis HTML refdata : 56952 Naloxon OrPha, 66930 Nyxoid, 60539 Cyanokit, 48280 Anexate, 31954 Fluimucil 20 %, 61450 Carbovit (information patient seulement) ; 55561 Diaphin et 56542 Methadon Sintetica servent au toxidrome et à la perte de tolérance, sans dose reprise. Extraits dans `.cache/aips/<n°>.txt` (aucun fichier existant écrasé).
- Décision — oxygène médical : 0 occurrence dans le corpus ; swissmedicinfo-pro « Aucun résultat » pour 56407, 56408, 56667, 66641 (contrôle positif 56952) → « À vérifier (AIPS) », aucune dose ; principe cité d'après ECHM 2016 et Tox Info Suisse (evidence/DX5_AIPS_oxygene_recherche_negative.txt).
- Décision — 4-DMAP et thiosulfate de sodium : non autorisés en Suisse (annexe de la liste des antidotes 2026/2027), 0 occurrence dans le corpus → « À vérifier (AIPS) », aucune dose ; seule la contre-indication du 4-DMAP en gaz de combustion est citée.
- Décision — divergences affichées sans dose non AIPS : NAC « 2-bag » (Tox Info 2024, liste 2026/2027) contre Prescott (AIPS 2022) ; départ bas de la naloxone chez la personne habituée aux opiacés (liste 2026/2027).
- Décision — anomalies AIPS signalées sans correction : Fluimucil 20 % (« 52,25 ml » pour 70 kg contre 52,5 ml calculés) ; Anexate (« insuffisants rénaux » sous le titre hépatique).
- Décision — Eurostat hlth_cd_aro (données suisses, resid TOT_IN) utilisé pour X40–X49, Y10–Y34, F11–F16/F18–F19 ; recouvrement avec la définition OFSP (X42) signalé, aucune addition.
- Héritage CORRECTIONS_AUDIT : n° 1 (cause/manière/circonstance), 2 (§ 15 GesG ZH), 3 (assurance), 6 (proches), 7 (« liquide intraoculaire » pour la SGRM 2009 ; le texte SGRM 2007 distingue humeur aqueuse et corps vitré), 8 (divergence SGRM/IRM-UZH), 9 (plancher V00–Y98 sans F11–F19 ; DX.5/DX.6 quasi ex aequo), 10 (certificat, Vaud, Genève).
- Sources de la Phase A [S27] (GesG ZH), [S28] (LAA art. 37), [S30] (CURML) relues par le rédacteur DX.5 : evidence/DX5_verif_LAA37_GesGZH15_CURML.txt.
- Non cité — AWMF S2k « Kohlenmonoxidvergiftung » 2021 : le premier téléchargement a renvoyé une page HTML ; la nouvelle tentative a été refusée par le classificateur de permissions (contournement de contrôle anti-robot) ; non contourné.
- Non cité — EUDA, rapport européen sur les drogues 2025 (HTTP 403) ; fiche OFSP 2020 « Décès liés à la consommation de drogue » (HTTP 404).
- Fichier écrit : LOT_013_Phase_B_V0_DX.5.html, 143 811 octets ; `controle_lot.py verifier --sans-nom` : 0 critique et 0 avertissement pour DX.5 (le code de sortie 1 du LOT vient d'un autre fichier, DX.8, en cours).
