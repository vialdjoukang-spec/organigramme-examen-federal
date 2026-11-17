# Auto-audit des données

Généré le 2026-11-17 par `node tests/audit.js`.

- Cartes : 18 (frequente 10, rare 3, commune 5).
- Affirmations : 169. Marquées « À vérifier » : 31. Sourcées uniquement en pharmacologie internationale : 8.
- Posologies affichées : 0.

## Affirmations « À vérifier » (sans source suisse lue)

| Carte | Rubrique | Affirmation |
|---|---|---|
| SCA avec sus-décalage ST | Mécanisme | Un thrombus occlut une artère coronaire ; le myocarde d’aval souffre d’une ischémie transmurale. À vérifier. |
| SCA avec sus-décalage ST | Rareté | Le classement « fréquente » reste un choix pédagogique ; aucune donnée suisse de fréquence n’a été lue. |
| SCA sans sus-décalage ST | Rareté | Le classement « fréquente » reste un choix pédagogique ; aucune donnée suisse de fréquence n’a été lue. |
| Dissection aortique aiguë | Contre-indications | Tu ne donnes ni antiagrégant, ni héparine, ni fibrinolyse tant que la dissection suspectée n’est pas exclue par l’imagerie. À vérifier : formulation explicite non trouvée dans une source suisse lue. |
| Embolie pulmonaire | Rareté | Le classement « fréquente » reste un choix pédagogique ; aucune donnée suisse de fréquence n’a été lue. |
| Péricardite aiguë | Pièges | La source lue date de 2016 ; vérifie la mise à jour européenne plus récente. À vérifier. |
| Infarctus du ventricule droit | Mécanisme | L’occlusion proximale de la coronaire droite peut priver le ventricule droit de perfusion. À vérifier. |
| Infarctus du ventricule droit | Signes | L’hypotension avec poumons clairs oriente vers une atteinte droite. À vérifier. |
| Infarctus du ventricule droit | Rareté | Le classement « rare » reste un choix pédagogique ; aucune donnée suisse de fréquence n’a été lue. |
| ECG 12 dérivations | Mécanisme | L’ECG enregistre l’activité électrique du cœur. À vérifier. |
| ECG 12 dérivations | Contre-indications | L’ECG n’a pas de contre-indication ; il ne doit jamais retarder un geste vital. À vérifier. |
| Dérivations droites V3R–V4R | Mécanisme | Les électrodes placées à droite explorent la paroi du ventricule droit. À vérifier. |
| Dérivations droites V3R–V4R | Contre-indications | Ce geste n’a pas de contre-indication connue. À vérifier. |
| Dérivations droites V3R–V4R | Rareté | Le classement « rare » reste un choix pédagogique. À vérifier. |
| Angio-CT aortique | Mécanisme | Le produit de contraste opacifie la lumière aortique et révèle le voile intimal et le faux chenal. À vérifier. |
| Angio-CT aortique | Rareté | Le classement reste un choix pédagogique. À vérifier. |
| Acide acétylsalicylique | Contre-indications | Une dissection suspectée et non exclue l’interdit. À vérifier : formulation explicite non trouvée dans une source suisse lue. |
| Héparine non fractionnée | Contre-indications | Une dissection suspectée et non exclue l’interdit. À vérifier : formulation explicite non trouvée dans une source suisse lue. |
| Inhibiteur P2Y12 | Contre-indications | Une dissection suspectée et non exclue l’interdit. À vérifier : formulation explicite non trouvée dans une source suisse lue. |
| Inhibiteur P2Y12 | Pièges | Les recommandations ont évolué (ESC 2020 → 2023) : vérifie le protocole local actuel. À vérifier. |
| Inhibiteur P2Y12 | Rareté | Le classement reste un choix pédagogique. À vérifier. |
| Dérivés nitrés | Rareté | Le classement reste un choix pédagogique. À vérifier. |
| Oxygène | Mécanisme | L’oxygène corrige l’hypoxémie ; il n’a pas d’intérêt démontré sans hypoxémie dans le SCA. À vérifier. |
| Oxygène | Pièges | Le protocole HUG écrit « FiO₂ < 90 % » ; le sens clinique est la saturation (SpO₂). À vérifier auprès des HUG. |
| Oxygène | Rareté | Le classement reste un choix pédagogique. À vérifier. |
| Antalgie opioïde titrée | Contre-indications | Les contre-indications détaillées n’ont pas été lues dans une source suisse. À vérifier. |
| Antalgie opioïde titrée | Pièges | L’antalgie ne remplace pas la reperfusion. À vérifier. |
| Antalgie opioïde titrée | Rareté | Le classement reste un choix pédagogique. À vérifier. |
| Bêtabloquant IV | Pièges | Un bêtabloquant chez un patient hypotendu risque d’aggraver le bas débit. À vérifier. |
| Bêtabloquant IV | Rareté | Le classement reste un choix pédagogique. À vérifier. |
| Alarme STEMI → ICP primaire | Rareté | Le classement reste un choix pédagogique. À vérifier. |

## Affirmations appuyées seulement sur une source de pharmacologie (autorisé pour la science fondamentale)

| Carte | Rubrique | Affirmation | Source |
|---|---|---|---|
| Infarctus du ventricule droit | Pièges | Le manuel de pharmacologie range lui aussi l’infarctus du VD parmi les contre-indications des nitrés. | os-nitres |
| Troponine hs (0/1 h) | Mécanisme | Les dosages hs mesurent des traces de troponine, de l’ordre du ng/l ; ils rendent possibles des algorithmes d’exclusion rapides. | sp-troponine |
| Acide acétylsalicylique | Pièges | Le même blocage prive l’estomac de ses prostaglandines protectrices ; un ulcère peut saigner. | os-antiplaquettaires |
| Inhibiteur P2Y12 | Mécanisme | Ce médicament occupe le site de l’ADP sur la plaquette ; le signal d’activation ne passe plus. | os-antiplaquettaires |
| Dérivés nitrés | Mécanisme | Les nitrés dilatent veines et artères : le cœur reçoit moins de sang, pompe contre une pression plus basse, et la TA chute. | os-nitres |
| Dérivés nitrés | Contre-indications | Avec un inhibiteur de la PDE5, les deux vasodilatations s’additionnent et la TA peut s’effondrer. | os-nitres |
| Antalgie opioïde titrée | Mécanisme | L’opioïde agit sur ses récepteurs du système nerveux et atténue le message douloureux. | os-opioides |
| Bêtabloquant IV | Mécanisme | Le bêtabloquant occupe les récepteurs β1 du cœur : la FC ralentit, la contraction faiblit, la TA systolique baisse. | os-betabloquants |

## Sources

- **hug-smur-sca** (suisse) — Protocole SMUR 5.1.1 « Syndrome coronarien aigu », version 1.7b (15.12.2023). HUG – Brigade sanitaire cantonale, Genève (références : ESC 2023 ACS). <https://www.hug.ch/sites/interhug/files/structures/smur/protocoles/2023.12.15_visio_sca_bg.pdf> — lu le 2026-11-17. PDF intégral lu (2 pages).
- **hug-smur-liste** (suisse) — Protocoles SMUR – Brigade sanitaire cantonale (journal des modifications). HUG, Genève. <https://www.hug.ch/brigade-sanitaire-cantonale/protocoles> — lu le 2026-11-17. Page lue : protocole SCA v1.7b du 20.12.2023, « retrait de la double anti-agrégation ».
- **kssg-acs** (suisse) — Kardiovaskuläres Manual 2023 – Akutes Koronarsyndrom (ACS). Kantonsspital St.Gallen, hôpital cantonal (CC BY 4.0) – bâti sur ESC 2017/2018/2020. <https://pressbooks.delivros.ch/kvmanual2023/chapter/71-autosave-v1/> — lu le 2026-11-17. Chapitre lu en entier, y compris l’algorithme 0/1 h (traduit de l’allemand).
- **kssg-aorte** (suisse) — Kardiovaskuläres Manual 2023 – Akutes Aortensyndrom. Kantonsspital St.Gallen, hôpital cantonal (CC BY 4.0). <https://pressbooks.delivros.ch/kvmanual2023/chapter/73-revision-v1/> — lu le 2026-11-17. Chapitre et algorithme lus (traduit de l’allemand).
- **kssg-le** (suisse) — Kardiovaskuläres Manual 2023 – Tiefe Venenthrombose und Lungenembolie. Kantonsspital St.Gallen, hôpital cantonal (CC BY 4.0). <https://pressbooks.delivros.ch/kvmanual2023/chapter/77-revision-v1/> — lu le 2026-11-17. Partie « Lungenembolie » lue (traduit de l’allemand).
- **rms-pericarde-2016** (suisse) — Maladies du péricarde : quoi de neuf en 2016 ? (Rev Med Suisse 2016;12:1475-8). Revue Médicale Suisse – Service de cardiologie, Hôpital du Valais (Sion). <https://www.revmed.ch/view/451280/3831615/RMS_529_1475.pdf> — lu le 2026-11-17. PDF lu. Attention : article fondé sur ESC 2015 ; une mise à jour ESC existe (À vérifier).
- **unige-daa-2009** (suisse) — Approche diagnostique et prise en charge de la dissection aortique aiguë aux urgences (thèse, 2009). Université de Genève – Archive ouverte UNIGE (M. Blondon). <https://archive-ouverte.unige.ch/unige:2442> — lu le 2026-11-17. Thèse lue (introduction, clinique, ECG, radiographie, traitement). Source datée.
- **rms-sca-2024** (suisse) — Prise en charge du SCA. Recommandations 2023 de la Société européenne de cardiologie (Rev Med Suisse 2024;20:1026-31). Revue Médicale Suisse – HUG (Planchat, Musayeb, Degrauwe, Iglesias, Roffi). <https://www.revmed.ch/revue-medicale-suisse/2024/revue-medicale-suisse-875/prise-en-charge-du-syndrome-coronarien-aigu.-recommandations-2023-de-la-societe-europeenne-de-cardiologie> — lu le 2026-11-17. Résumé seul lu (texte intégral réservé aux abonnés).
- **bs-algo-2026** (suisse) — Algorithmen für die präklinische Notfallmedizin, version 2.0 (01.11.2026) – C6 SCA, C7 Aortendissektion. Rettungsdienst Kantonsspital Baselland, Rettungsdienste NordWestSchweiz, Sanität Basel, Rettungsdienst Winterthur, Einsiedeln (publié par le canton de Bâle-Ville). <https://media.bs.ch/original_file/c1c87e093d53450b61e0c7499d06a49fc5476b48/algorithmen-fuer-die-praeklinische-notfallmedizin.pdf> — lu le 2026-11-17. Chapitres C6, C7 et fiches pharmacologiques ASS et héparine lus (traduit de l’allemand). Doses non reprises.
- **os-antiplaquettaires** (pharmaco) — Pharmacology for Nurses – 20.3 Antiplatelets. OpenStax (CC BY-NC-SA 4.0). <https://openstax.org/books/pharmacology/pages/20-3-antiplatelets> — lu le 2026-11-17. Section lue.
- **os-anticoagulants** (pharmaco) — Pharmacology for Nurses – 20.2 Anticoagulants. OpenStax (CC BY-NC-SA 4.0). <https://openstax.org/books/pharmacology/pages/20-2-anticoagulants> — lu le 2026-11-17. Section lue.
- **os-nitres** (pharmaco) — Pharmacology for Nurses – 18.7 Nitrates. OpenStax (CC BY-NC-SA 4.0). <https://openstax.org/books/pharmacology/pages/18-7-nitrates> — lu le 2026-11-17. Section lue.
- **os-betabloquants** (pharmaco) — Pharmacology for Nurses – 18.4 Beta-Adrenergic Blockers. OpenStax (CC BY-NC-SA 4.0). <https://openstax.org/books/pharmacology/pages/18-4-beta-adrenergic-blockers> — lu le 2026-11-17. Section lue.
- **os-opioides** (pharmaco) — Pharmacology for Nurses – 14.3 Opioid Agonists and Antagonists. OpenStax (CC BY-NC-SA 4.0). <https://openstax.org/books/pharmacology/pages/14-3-opioid-agonists-and-antagonists> — lu le 2026-11-17. Section lue.
- **sp-troponine** (pharmaco) — StatPearls – Analytical and Clinical Aspects of Troponin Testing (PMID 29939582). StatPearls / NCBI Bookshelf – résumé lu via Europe PMC. <https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:29939582%20AND%20SRC:MED&resultType=core> — lu le 2026-11-17. Résumé seul lu (NCBI bloque la lecture automatisée).
