# Audit médical agressif — Syndromes SY-55 à SY-81 (14.11.2026)

Auditeur indépendant (aucune rédaction). Méthode : lecture des 27 JSON ; contrôle de chaque dose par `aips_fiche.py fiche` (23 URL refdata citées + 7 AIPS citées « swissmedicinfo-pro », relues sur refdata) ; recherche `aips_fiche.py trouve` des molécules déclarées « absentes du corpus » ; lecture des 10 images (`Read`) et de leur licence (API Commons) ; contrôle des renvois S-xx. Calculs refaits : Ca corrigé 2,70 + 0,02 × 10 = 2,90 ; osmolalité 2 × 125 + 5 + 5 = 260 : justes.

## Verdict : **NON audit-ok** — 7 Critiques, 9 Graves, 8 Moyens, 6 Légers

## Score §12.2

| Critère | Note | Raison |
|---|---|---|
| Définitions, symptômes, signes | 2 | Justes (Sepsis-3, SJS < 10 % / NET > 30 %, signes B, SCORTEN 7 items) |
| Valeurs, seuils | 1 | Critères de Hunter faux (SY-73) ; cible hyponatrémie américaine |
| VITE DIT CAFé | 1 | Lettres détournées (« D métabolique », grossesse en D, HPT en D) |
| Drapeaux rouges, examens | 2 | Pertinents |
| Management, doses AIPS | 0 | 4 molécules déclarées « absentes » sont au corpus ; 3 doses AIPS non extraites ou fausses |
| Urgences vitales | 1 | Anaphylaxie : dose hospitalière 0,5 mg i.m. absente ; DT sans voie i.v. ; glucagon et alcool |
| Différentiels, synthèse CS | 2 | Justes, 2 phrases |
| Sources | 1 | Européennes citées mais non lues alors que le chiffre est dans la source ; extrait Solu-Medrol inadapté |
| Images | 1 | Licences conformes ; SY-67 visage partiellement identifiable |
| Phrases verbales | 2 | Conformes |

## Critiques (bloquants)

| # | Fiche, champ | Extrait | PATCH exact | Source lue |
|---|---|---|---|---|
| C1 | SY-56 management[3] | « calcitonine absente du corpus AIPS consulté (À vérifier) » | « calcitonine dans la crise hypercalcémique : perfusion i.v. de 5 à 10 U.I./kg dans 500 ml de NaCl 0,9 % pendant au moins 6 h/jour, ou 2 à 4 injections i.v. lentes, avec réhydratation (AIPS Miacalcic® Ampoules n° 38605, janvier 2022) » | refdata 0af2727e… |
| C2 | SY-63 management[2] ; SY-67 management[2] | « acide folique absent du corpus AIPS consulté (À vérifier) » | « acide folique 5 mg 1 fois/jour jusqu'à normalisation de l'hémogramme, jusqu'à 15 mg/jour ; l'anémie hémolytique figure parmi les causes de carence ; contre-indication : ne jamais le donner seul dans l'anémie pernicieuse, l'associer à la vitamine B12 (AIPS Acidum folicum Streuli® n° 36752, janvier 2023) » | refdata be588d7d… |
| C3 | SY-63 management[2] | « dose selon le tableau de l'AIPS, non extrait : À vérifier » | « besoins selon le schéma simplifié : Hb < 100 g/l : 1500 mg (35 à < 70 kg) ou 2000 mg (≥ 70 kg) ; Hb 100 à < 140 g/l : 1000 ou 1500 mg ; dose unique ≤ 20 mg/kg en perfusion et ≤ 1000 mg, au plus 1000 mg par semaine (AIPS Ferinject® n° 57851, juin 2025) » | refdata efc261d9… |
| C4 | SY-69 management[2] | « lithium : seule une AIPS de chlorure de lithium diagnostique figure au corpus consulté (À vérifier) » | « lithium sur avis psychiatrique, après ECG : épisode maniaque aigu, en général 4 comprimés de Quilonorm retard (1800 mg de carbonate de lithium) en plusieurs prises, pour une lithiémie de 0,8 à 1,2 mmol/l (AIPS Quilonorm® retard n° 35960, mars 2025) » | refdata b838b25e… |
| C5 | SY-70 management[2] | « halopéridol i.m. (… dose de cette indication non extraite : À vérifier) » | « halopéridol 5 mg i.m., renouvelable toutes les heures, 15 mg/jour suffisant le plus souvent, maximum 20 mg/jour (AIPS Haldol® n° 26891, novembre 2024) » | refdata d9759cb5… |
| C6 | SY-71 management[2] et sources SY-69/70/71 | « ou 1 à 10 mg i.m. » | « ou 2 à 5 mg i.m., renouvelable toutes les heures, maximum 10 mg/jour ; après 65 ans, commencer à la moitié de la plus faible dose adulte, sans dépasser la moitié de la dose adulte (AIPS Haldol® n° 26891, novembre 2024) ». La patiente du cas a 84 ans. | idem |
| C7 | SY-73 management[2] ; SY-74 management[1] ; sources Valium | « hors AIPS pour ce toxidrome (… anxiété, excitation, sédation de base) ; dose : À vérifier avec Tox Info Suisse » | « diazépam i.v. lent (0,5 à 1 ml/min), 0,1 à 0,2 mg/kg, répétable toutes les 8 h, matériel de réanimation prêt ; l'AIPS cite les « épisodes d'agitation motrice » (AIPS Valium® n° 28840, juin 2023) ; le toxidrome n'est pas nommé » | refdata c3b3c7fe… |

## Graves

| # | Fiche, champ | Défaut | PATCH exact |
|---|---|---|---|
| G1 | SY-80 management[1], a_dire[1] | Seule la dose d'auto-injecteur (300 µg) figure ; en milieu de soins, la station utilise l'ampoule. | Ajouter : « Avec l'ampoule : adrénaline 1 mg/ml, 500 µg (0,5 ml) i.m., répétable toutes les 5 min selon PA, pouls et respiration ; 6–12 ans 0,3 mg, 6 mois–6 ans 0,15 mg ; demi-dose sous amitriptyline, imipramine ou bêtabloquant (AIPS Adrenalin Sintetica n° 56551, novembre 2024). » |
| G2 | SY-72 management[1], drapeaux | Délirium tremens traité seulement par oxazépam oral. | Ajouter : « délirium tremens ou voie orale impossible : diazépam 0,1 à 0,2 mg/kg i.v. lent, répété toutes les 8 h, puis relais oral (AIPS Valium® n° 28840, juin 2023) ». |
| G3 | SY-55 management[1] | Glucagon proposé sans réserve ; l'AIPS le dit « peu ou pas » efficace après jeûne prolongé, insuffisance surrénale ou hypoglycémie induite par l'alcool ; indication limitée au diabétique sous insuline. | Ajouter : « Chez l'alcoolique, le dénutri ou sous sulfonylurée, préférer le glucose i.v. : le glucagon a peu ou pas d'effet quand le glycogène hépatique est épuisé (AIPS GlucaGen® n° 31489, novembre 2021). » |
| G4 | SY-63 management[2] | B12 parentérale sans dose ; folates avant B12 non interdits. | « vitamine B12 1000 µg i.m. 1 fois/semaine jusqu'à normalisation, puis 1000 µg/mois à vie en cas de malabsorption (AIPS Vitarubine® n° 21672, juillet 2025) ; ne jamais donner l'acide folique seul avant d'avoir exclu une carence en B12. » |
| G5 | SY-64 management[2] | « antidote d'un AOD : À vérifier » alors que idarucizumab (Praxbind® n° 65804), andexanet (Ondexxya® n° 67759) et concentré de complexe prothrombinique (Beriplex® n° 00665) sont au corpus. | Nommer ces trois AIPS et citer leur dose après lecture. |
| G6 | SY-78 management[1] | Forme sévère : « molécule et dose : À vérifier » ; la benzylpénicilline i.v. nomme l'érysipèle. | « forme sévère : benzylpénicilline 1 à 5 millions U.I./jour i.v. en 4 à 6 doses, à augmenter dans les infections graves (AIPS Pénicilline « Grünenthal » n° 56271, mai 2023) ; autre choix selon ssi.guidelines.ch. » |
| G7 | SY-62 management[2] | Dose intra-articulaire (« épaule 20 mg ») appliquée à une bursite sous-acromiale. | « bursite ou tendinite : injection intrafocale de Kenacort-A 10 seulement, 10 à 40 mg selon la taille de la région, intervalle ≥ 2 semaines (AIPS Kenacort®-A n° 26177, décembre 2021) ». |
| G8 | SY-73 examens[0] | Critère de Hunter tronqué : « hypertonie avec température > 38 °C ». | « hypertonie, température > 38 °C et clonus oculaire ou inductible » (source australienne Dunkley 2003, à relire). |
| G9 | SY-57 management[0] | « hausse de 4 à 6 mmol/l » est la cible du panel américain ; le volume est donné par la source européenne citée. | « 150 ml de NaCl 3 % i.v. en 20 min, sodium contrôlé à 20 min, répéter 2 fois au plus jusqu'à +5 mmol/l (source européenne : ESE/ESICM/ERA-EDTA 2014, lu via un résumé secondaire, texte à relire) ; ensuite ≤ 10 mmol/l le 1er jour, puis ≤ 8 mmol/l par 24 h (à vérifier dans le texte). » |

## Moyens

| # | Fiche, champ | Défaut | PATCH |
|---|---|---|---|
| M1 | SY-74 drapeaux[0] | Bicarbonate « dose À vérifier » sans dire hors AIPS. | « hors AIPS : Bicarbonate de sodium Bichsel 8,4 % n° 36797 indique acidoses et intoxication aux barbituriques, pas les tricycliques ». |
| M2 | SY-80 management[2] | « bronchodilatateur… dose À vérifier » ; Ventolin® n° 37397 est au corpus. | Nommer le salbutamol et citer la dose AIPS lue. |
| M3 | SY-79 management[0] | « Reconnaître le sepsis par le qSOFA » : SSC 2021 déconseille le qSOFA seul comme dépistage. | « Suspecter le sepsis devant toute infection avec signe de dysfonction d'organe ; le qSOFA aide au pronostic, pas au dépistage seul (source internationale : SSC 2021). » |
| M4 | SY-67 sources[3] | L'extrait Solu-Medrol décrit l'anaphylaxie, pas l'AHAI. | Remplacer par : « Affections hématologiques : Anémie hémolytique auto-immune acquise ; dose ≥ 0,5 mg/kg/24 h, adaptée à la sévérité ». |
| M5 | SY-77 management[2] | Angio-œdème bradykinique : inefficacité d'adrénaline, antihistaminique et corticoïde non dite. | Ajouter la phrase (déjà présente en SY-80). |
| M6 | SY-68 management[3] | « PROFILES 2 EPA 2d, base de l'examen dès 2028 » : aucune source listée. | Sourcer ou supprimer. |
| M7 | SY-68 management[2] | Escitalopram après 65 ans omis. | « après 65 ans : 5 mg/jour, au maximum 10 mg (AIPS Escitalopram-Mepha n° 62787, avril 2026) ». |
| M8 | SY-55 management[1] | GlucaGen indiqué chez le diabétique sous insuline : la sulfonylurée sort de l'indication. | Le préciser. |

## Légers

L1 SY-56 : seuil Zometa « ≥ 3,0 » → « > 3,0 mmol/l (12,0 mg/dl) » ; Zometa contre-indiqué en grossesse et allaitement. L2 Lettres VITE DIT CAFé : « D (métabolique) » (SY-70, SY-71), grossesse en D (SY-60), HPT en D (SY-56) : choisir F (fonctionnel) ou nommer « métabolique » hors lettre. L3 SY-77 : EAACI « 2021 » dans examens, « 2022 » dans sources. L4 SY-75 : « Titrer chez le dépendant… (déduction) » est écrit dans l'AIPS (Mises en garde : sevrage aigu) : citer l'AIPS. L5 SY-67 image : visage partiellement identifiable (yeux, nez) et crédit « CDC/Sellers » alors que Commons indique « Unknown author » ; préférer un gros plan scléral. L6 Schéma : clé `image.legende` absente de SCHEMA_SYNDROME.md (ajouter au schéma).

## Points contrôlés sans défaut

Doses conformes à l'AIPS lue : GlucaGen 1 mg / 0,5 mg ; Benerva ≤ 200 mg/j parentéral ; Zometa 4 mg/100 ml ≥ 15 min ; naproxène ; paracétamol 4 g ; Kenacort intra-articulaire ; ceftriaxone 1–2 g (≤ 4 g) ; Konakion 10–20 mg i.v. ≥ 30 s ; céfépime 2 g/8 h ; pipéracilline-tazobactam ; allopurinol ; escitalopram 10–20 mg ; olanzapine 10–15 mg ; Haldol délire p.o. et manie p.o. ; oxazépam ; naloxone 0,4–2 mg et seuil 10 mg ; Jext 300/150 µg, 5–15 min, cuisse antéro-latérale (AIPS octobre 2026) ; Tavegyl 2 mg i.v. lent ; cétirizine (hors AIPS dans l'urticaire aiguë : exact) ; Firazyr 30 mg ; Ospen ; noradrénaline 8–12 µg/min ; Normolytoral 40–50 ml/kg. Numéros Swissmedic et dates : conformes (Noradrenalin n° 60955, Valium n° 28840, Normolytoral n° 43916 vérifiés dans le texte). Images : 10 licences conformes à Commons (CC BY, CC BY-SA, CC0, domaine public, « Attribution ») ; signes visibles. Renvois S-01 à S-35 : existants.

## Question finale : la série peut-elle passer en audit-ok ? **Non.**
Il manque : C1–C7 (quatre AIPS déclarées absentes alors qu'elles sont au corpus ; trois doses AIPS non extraites ou fausses), puis G1–G9, en priorité G1 (adrénaline 0,5 mg i.m.), G2 (délirium tremens) et G3 (glucagon chez l'alcoolique).
