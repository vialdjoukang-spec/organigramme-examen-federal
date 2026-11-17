# Auto-audit des données

Généré le 2026-11-17 par `node tests/audit.js`. Validation : 0 erreur(s), 0 avertissement(s).

## Cardiologie

- Pathologies : 6 · cartes : 18 · cas : 1 · questions rédigées : 0.
- Affirmations : 180. « À vérifier » : 35 (19.4 %). Pharmacologie internationale seule : 8. Doses détectées : 0.

### Affirmations « À vérifier »

| Carte | Rubrique | Affirmation |
|---|---|---|
| SCA avec sus-décalage ST | Fondamentaux | Un thrombus occlut une artère coronaire ; le myocarde d’aval souffre d’une ischémie transmurale. À vérifier. |
| SCA avec sus-décalage ST | fréquence | Aucune donnée suisse de fréquence n’a été lue. À vérifier. |
| SCA sans sus-décalage ST | Suivi et orientation | Critères d’hospitalisation et de suivi à sourcer. À vérifier. |
| SCA sans sus-décalage ST | fréquence | Aucune donnée suisse de fréquence n’a été lue. À vérifier. |
| Dissection aortique aiguë | contre | Tu ne donnes ni antiagrégant, ni héparine, ni fibrinolyse tant que la dissection suspectée n’est pas exclue par l’imagerie. À vérifier : formulation explicite non trouvée dans une source suisse lue. |
| Embolie pulmonaire | Diagnostics différentiels | Différentiels discriminants à sourcer (source suisse). À vérifier. |
| Embolie pulmonaire | Suivi et orientation | Critères d’hospitalisation ou de traitement ambulatoire à sourcer. À vérifier. |
| Embolie pulmonaire | fréquence | Aucune donnée suisse de fréquence n’a été lue. À vérifier. |
| Péricardite aiguë | Suivi et orientation | Critères d’hospitalisation et de suivi à sourcer. À vérifier. |
| Péricardite aiguë | pièges | La source lue date de 2016 ; vérifie la mise à jour européenne plus récente. À vérifier. |
| Infarctus du ventricule droit | Fondamentaux | L’occlusion proximale de la coronaire droite peut priver le ventricule droit de perfusion. À vérifier. |
| Infarctus du ventricule droit | Démarche diagnostique | L’hypotension avec poumons clairs oriente vers une atteinte droite. À vérifier. |
| Infarctus du ventricule droit | fréquence | Aucune donnée suisse de fréquence n’a été lue. À vérifier. |
| ECG 12 dérivations | Fondamentaux | L’ECG enregistre l’activité électrique du cœur. À vérifier. |
| ECG 12 dérivations | contre | L’ECG n’a pas de contre-indication ; il ne doit jamais retarder un geste vital. À vérifier. |
| Dérivations droites V3R–V4R | Fondamentaux | Les électrodes placées à droite explorent la paroi du ventricule droit. À vérifier. |
| Dérivations droites V3R–V4R | contre | Ce geste n’a pas de contre-indication connue. À vérifier. |
| Dérivations droites V3R–V4R | fréquence | Aucune donnée suisse de fréquence n’a été lue. À vérifier. |
| Angio-CT aortique | Fondamentaux | Le produit de contraste opacifie la lumière aortique et révèle le voile intimal et le faux chenal. À vérifier. |
| Angio-CT aortique | fréquence | Aucune donnée suisse de fréquence n’a été lue. À vérifier. |
| Acide acétylsalicylique | contre | Une dissection suspectée et non exclue l’interdit. À vérifier : formulation explicite non trouvée dans une source suisse lue. |
| Héparine non fractionnée | contre | Une dissection suspectée et non exclue l’interdit. À vérifier : formulation explicite non trouvée dans une source suisse lue. |
| Inhibiteur P2Y12 | contre | Une dissection suspectée et non exclue l’interdit. À vérifier : formulation explicite non trouvée dans une source suisse lue. |
| Inhibiteur P2Y12 | pièges | Les recommandations ont évolué (ESC 2020 → 2023) : vérifie le protocole local actuel. À vérifier. |
| Inhibiteur P2Y12 | fréquence | Aucune donnée suisse de fréquence n’a été lue. À vérifier. |
| Dérivés nitrés | fréquence | Aucune donnée suisse de fréquence n’a été lue. À vérifier. |
| Oxygène | Fondamentaux | L’oxygène corrige l’hypoxémie ; il n’a pas d’intérêt démontré sans hypoxémie dans le SCA. À vérifier. |
| Oxygène | pièges | Le protocole HUG écrit « FiO₂ < 90 % » ; le sens clinique est la saturation (SpO₂). À vérifier auprès des HUG. |
| Oxygène | fréquence | Aucune donnée suisse de fréquence n’a été lue. À vérifier. |
| Antalgie opioïde titrée | contre | Les contre-indications détaillées n’ont pas été lues dans une source suisse. À vérifier. |
| Antalgie opioïde titrée | pièges | L’antalgie ne remplace pas la reperfusion. À vérifier. |
| Antalgie opioïde titrée | fréquence | Aucune donnée suisse de fréquence n’a été lue. À vérifier. |
| Bêtabloquant IV | pièges | Un bêtabloquant chez un patient hypotendu risque d’aggraver le bas débit. À vérifier. |
| Bêtabloquant IV | fréquence | Aucune donnée suisse de fréquence n’a été lue. À vérifier. |
| Alarme STEMI → ICP primaire | fréquence | Aucune donnée suisse de fréquence n’a été lue. À vérifier. |

### Affirmations appuyées seulement sur la pharmacologie internationale (autorisé)

| Carte | Rubrique | Affirmation | Source |
|---|---|---|---|
| Infarctus du ventricule droit | pièges | Le manuel de pharmacologie range lui aussi l’infarctus du VD parmi les contre-indications des nitrés. | os-nitres |
| Troponine hs (0/1 h) | Fondamentaux | Les dosages hs mesurent des traces de troponine, de l’ordre du ng/l ; ils rendent possibles des algorithmes d’exclusion rapides. | sp-troponine |
| Acide acétylsalicylique | pièges | Le même blocage prive l’estomac de ses prostaglandines protectrices ; un ulcère peut saigner. | os-antiplaquettaires |
| Inhibiteur P2Y12 | Fondamentaux | Ce médicament occupe le site de l’ADP sur la plaquette ; le signal d’activation ne passe plus. | os-antiplaquettaires |
| Dérivés nitrés | Fondamentaux | Les nitrés dilatent veines et artères : le cœur reçoit moins de sang, pompe contre une pression plus basse, et la TA chute. | os-nitres |
| Dérivés nitrés | contre | Avec un inhibiteur de la PDE5, les deux vasodilatations s’additionnent et la TA peut s’effondrer. | os-nitres |
| Antalgie opioïde titrée | Fondamentaux | L’opioïde agit sur ses récepteurs du système nerveux et atténue le message douloureux. | os-opioides |
| Bêtabloquant IV | Fondamentaux | Le bêtabloquant occupe les récepteurs β1 du cœur : la FC ralentit, la contraction faiblit, la TA systolique baisse. | os-betabloquants |

## Sources

- **hug-smur-sca** (suisse · hôpital universitaire) — Protocole SMUR 5.1.1 « Syndrome coronarien aigu », version 1.7b (15.12.2023). HUG – Brigade sanitaire cantonale, Genève (références : ESC 2023 ACS). <https://www.hug.ch/sites/interhug/files/structures/smur/protocoles/2023.12.15_visio_sca_bg.pdf> — lu le 2026-11-17. PDF intégral lu (2 pages).
- **hug-smur-liste** (suisse · hôpital universitaire) — Protocoles SMUR – Brigade sanitaire cantonale (journal des modifications). HUG, Genève. <https://www.hug.ch/brigade-sanitaire-cantonale/protocoles> — lu le 2026-11-17. Page lue : protocole SCA v1.7b du 20.12.2023, « retrait de la double anti-agrégation ».
- **kssg-acs** (suisse · hôpital cantonal) — Kardiovaskuläres Manual 2023 – Akutes Koronarsyndrom (ACS). Kantonsspital St.Gallen, hôpital cantonal (CC BY 4.0) – bâti sur ESC 2017/2018/2020. <https://pressbooks.delivros.ch/kvmanual2023/chapter/71-autosave-v1/> — lu le 2026-11-17. Chapitre lu en entier, y compris l’algorithme 0/1 h (traduit de l’allemand).
- **kssg-aorte** (suisse · hôpital cantonal) — Kardiovaskuläres Manual 2023 – Akutes Aortensyndrom. Kantonsspital St.Gallen, hôpital cantonal (CC BY 4.0). <https://pressbooks.delivros.ch/kvmanual2023/chapter/73-revision-v1/> — lu le 2026-11-17. Chapitre et algorithme lus (traduit de l’allemand).
- **kssg-le** (suisse · hôpital cantonal) — Kardiovaskuläres Manual 2023 – Tiefe Venenthrombose und Lungenembolie. Kantonsspital St.Gallen, hôpital cantonal (CC BY 4.0). <https://pressbooks.delivros.ch/kvmanual2023/chapter/77-revision-v1/> — lu le 2026-11-17. Partie « Lungenembolie » lue (traduit de l’allemand).
- **rms-pericarde-2016** (suisse · revue suisse) — Maladies du péricarde : quoi de neuf en 2016 ? (Rev Med Suisse 2016;12:1475-8). Revue Médicale Suisse – Service de cardiologie, Hôpital du Valais (Sion). <https://www.revmed.ch/view/451280/3831615/RMS_529_1475.pdf> — lu le 2026-11-17. PDF lu. Attention : article fondé sur ESC 2015 ; une mise à jour ESC existe (À vérifier).
- **unige-daa-2009** (suisse · faculté de médecine) — Approche diagnostique et prise en charge de la dissection aortique aiguë aux urgences (thèse, 2009). Université de Genève – Archive ouverte UNIGE (M. Blondon). <https://archive-ouverte.unige.ch/unige:2442> — lu le 2026-11-17. Thèse lue (introduction, clinique, ECG, radiographie, traitement). Source datée.
- **rms-sca-2024** (suisse · revue suisse) — Prise en charge du SCA. Recommandations 2023 de la Société européenne de cardiologie (Rev Med Suisse 2024;20:1026-31). Revue Médicale Suisse – HUG (Planchat, Musayeb, Degrauwe, Iglesias, Roffi). <https://www.revmed.ch/revue-medicale-suisse/2024/revue-medicale-suisse-875/prise-en-charge-du-syndrome-coronarien-aigu.-recommandations-2023-de-la-societe-europeenne-de-cardiologie> — lu le 2026-11-17. Résumé seul lu (texte intégral réservé aux abonnés).
- **bs-algo-2026** (suisse · services de sauvetage (hôpitaux cantonaux)) — Algorithmen für die präklinische Notfallmedizin, version 2.0 (01.11.2026) – C6 SCA, C7 Aortendissektion. Rettungsdienst Kantonsspital Baselland, Rettungsdienste NordWestSchweiz, Sanität Basel, Rettungsdienst Winterthur, Einsiedeln (publié par le canton de Bâle-Ville). <https://media.bs.ch/original_file/c1c87e093d53450b61e0c7499d06a49fc5476b48/algorithmen-fuer-die-praeklinische-notfallmedizin.pdf> — lu le 2026-11-17. Chapitres C6, C7 et fiches pharmacologiques ASS et héparine lus (traduit de l’allemand). Doses non reprises.
- **os-antiplaquettaires** (pharmaco) — Pharmacology for Nurses – 20.3 Antiplatelets. OpenStax (CC BY-NC-SA 4.0). <https://openstax.org/books/pharmacology/pages/20-3-antiplatelets> — lu le 2026-11-17. Section lue.
- **os-anticoagulants** (pharmaco) — Pharmacology for Nurses – 20.2 Anticoagulants. OpenStax (CC BY-NC-SA 4.0). <https://openstax.org/books/pharmacology/pages/20-2-anticoagulants> — lu le 2026-11-17. Section lue.
- **os-nitres** (pharmaco) — Pharmacology for Nurses – 18.7 Nitrates. OpenStax (CC BY-NC-SA 4.0). <https://openstax.org/books/pharmacology/pages/18-7-nitrates> — lu le 2026-11-17. Section lue.
- **os-betabloquants** (pharmaco) — Pharmacology for Nurses – 18.4 Beta-Adrenergic Blockers. OpenStax (CC BY-NC-SA 4.0). <https://openstax.org/books/pharmacology/pages/18-4-beta-adrenergic-blockers> — lu le 2026-11-17. Section lue.
- **os-opioides** (pharmaco) — Pharmacology for Nurses – 14.3 Opioid Agonists and Antagonists. OpenStax (CC BY-NC-SA 4.0). <https://openstax.org/books/pharmacology/pages/14-3-opioid-agonists-and-antagonists> — lu le 2026-11-17. Section lue.
- **sp-troponine** (pharmaco) — StatPearls – Analytical and Clinical Aspects of Troponin Testing (PMID 29939582). StatPearls / NCBI Bookshelf – résumé lu via Europe PMC. <https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:29939582%20AND%20SRC:MED&resultType=core> — lu le 2026-11-17. Résumé seul lu (NCBI bloque la lecture automatisée).
