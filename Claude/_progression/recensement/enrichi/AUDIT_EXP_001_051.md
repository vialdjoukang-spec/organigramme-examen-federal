# Audit médical agressif : EXP-001 à EXP-051 (`enrichi/EXP_a.json`)

Auditeur indépendant (je n'ai rien rédigé), 14.11.2026. J'ai appliqué les skills `medecin-expert` et `expert-web`.
Version auditée : `EXP_a.json`, 149 051 octets, SHA-256 `ac53fddce52a0a863ba2f4fa74a89ba8ceca46f13b04de3f9f7485038148dcbc`. Le JSON est valide et contient 51 entrées. Le cadrage vient de `recensement.json > explorations`.

**Ce que j'ai fait**
- J'ai lu les 51 entrées champ par champ : gold, première intention, autres, traces, lecture, valeurs normales, calculs, syndrome, traitement et sources.
- J'ai relu dans le corpus refdata, par URL (cache `~/.cache/medina_aips`), le passage cité de 30 AIPS : Levetiracetam DESITIN 62616, Lorazepam Xilmac 50490, Midazolam Accord 66718, **Rivotril 37756**, Buccolam 62556, Duphalac 32894, Xifaxan 63216, Aciclovir Labatec 60325, Sabril 50043, **Synacthen 31723**, **Depakine 34734**, Solu-Medrol 35112, Latanoprost-Mepha 60612, Dostinex 51756, Lucentis 57664, **Eylea 62393**, **Vabysmo 68395**, Luxturna 67371, **Atropine SDU Faure 46994**, Prednisone Streuli 29349, Betahistin-Mepha 58124, Pedmarqsi 70194, Nasonex 70546, Duloxetin-Mepha 66098, Privigen 58314, Mestinon 19943, Firdapse 61853, Rilutek 53678, Qalsody 68577, Agamree 69650, Gutron 44977, Florinef 31095, Eliquis 61549, Krenosin 51567, Amiodarone Labatec 59528 et Atropin Sulfat Aguettant 65276. L'éthosuximide est absent du corpus (Petinimid, Suxilep et Zarontin cherchés).
- J'ai lu en ligne :
  - le texte intégral des directives ASSM 2017 (PDF sams.ch, « 2e tirage mars 2019 ») ;
  - le texte intégral du projet ASSM mis en consultation du 16.06 au 19.09.2025 ;
  - la notice PubMed 41123621 (ERC-ESICM 2025, post-réanimation) ;
  - une revue secondaire de 2026 (Front Med 2026;1775538) qui résume ERC-ESICM 2025 ;
  - des résumés secondaires de McDonald 2024, EGS 6e éd. 2025, OFSP MCJ et AWMF Hörsturz.
- J'ai refait les 10 calculs par script. Ils sont tous exacts (détail au §3).

## 1. Défauts

| # | Id · champ | Extrait (mot pour mot) | Gravité | PATCH exact | Source lue |
|---|---|---|---|---|---|
| C1 | 007 · `autres[3]` et `valeurs_normales[0]` | « EEG … selon les directives, si la perfusion ne peut pas être évaluée » ; « < 2 µV [ASSM, directives 2017 — À vérifier] » | **Critique** | `autres[3].quand` = « hors directives suisses : l'EEG n'est **pas** un examen complémentaire admis par l'ASSM pour le constat de mort ; il sert seulement à explorer un facteur confondant (toxique, métabolique) avant le diagnostic ». `valeurs_normales[0].source` = « Source américaine : ACNS 2006 — l'ASSM ne fixe aucun seuil EEG ». Ajouter à `autres[0].quand` : « obligatoire si l'arrêt des fonctions n'est pas suffisamment démontré, si un facteur réversible ne peut pas être exclu, si l'examen des nerfs crâniens est impossible ou si une lésion infratentorielle isolée est possible ; examens admis : angio-TDM avec perfusion, angiographie par soustraction numérique, Doppler/duplex transcrânien codé couleur (déconseillé chez l'enfant), angio-IRM avec perfusion ». | ASSM 2017, ch. 3 et annexe (lus) ; projet ASSM 2025, ch. 3.3.1 (lu) |
| C2 | 007 · `sources[0]`, `gold` | « directives 2017 (version révisée À vérifier) — non lu » | **Critique** (vérifiable, lu par moi) | « ASSM, Diagnostic de la mort en vue de la transplantation d'organes et préparation du prélèvement d'organes, approuvées le 16.05.2017, en vigueur depuis le 15.11.2017 (2e tirage 2019) — lu ; révision mise en consultation du 16.06 au 19.09.2025, pas encore adoptée au 14.11.2026 ». Ajouter au gold : « deux médecins qualifiés, dont un non impliqué dans le traitement (principe des quatre yeux) ; test d'apnée jusqu'à une PaCO2 ≥ 60 mmHg (8 kPa) ». | sams.ch (PDF 2017 et projet 2025) |
| C3 | 002 · `traitement[0]` | « dose de l'état de mal non citée, car les AIPS suisses … ne retiennent pas cette indication » | **Critique** | « Clonazépam i.v. (Rivotril®) : “Rivotril i.v. ou i.m. est un produit de choix dans le traitement de toutes les formes de l'état de mal épileptique” ; adulte : “une ampoule (1 mg)… Généralement, 1-4 mg suffisent… La dose totale injectée ne doit pas dépasser 10 mg”, au plus 0,25–0,5 mg/min (AIPS Rivotril® n° 37756, octobre 2023). Lorazépam Xilmac 50490 : indication absente, “destiné uniquement à la distribution à l'étranger” ». | AIPS Rivotril 37756 ; AIPS Lorazepam Xilmac 50490 (lues) |
| C4 | 001 · `traitement[1]` ; 006 · `traitement[0]` | « éviter le valproate … (restriction AIPS valproate, non lue en entier) » ; « Absences : éthosuximide ou valproate » | **Critique** | Citer : « [le valproate ne doit pas être utilisé] chez les filles et les femmes en âge de procréer sauf en cas d'inefficacité ou d'intolérance aux autres alternatives médicamenteuses… conformément au programme de prévention de la grossesse » ; contre-indication : « chez les jeunes filles et les femmes en âge de procréer, sauf si toutes les conditions du programme de prévention de la grossesse sont remplies » (AIPS Depakine® n° 34734, septembre 2025 ; indication « petit-mal/absences » et « syndrome de West »). Garder « éthosuximide : AIPS absente du corpus (À vérifier) ». | AIPS Depakine 34734 (lue) |
| C5 | 016 · `traitement[1]` | « pénalisation par atropine (dose non citée) » | **Critique** | « Atropine collyre 0,5 % : indication “traitement de l'amblyopie chez l'enfant strabique” ; “Instiller 1 goutte 1 à 3 fois par jour” ; jeunes enfants d'abord sous surveillance médicale ; comprimer le canal lacrymal (AIPS Atropine SDU Faure n° 46994, novembre 2025) ». | AIPS 46994 (lue) |
| G1 | 008 · `autres[0].pourquoi_pas_gold` ; `gold.examen` ; `sources[0]` | « n'entrent pas dans les critères McDonald 2017 » | **Grave** | « critères de McDonald 2024 : le nerf optique devient la 5e localisation de dissémination spatiale, prouvée par IRM orbitaire, OCT (asymétrie interoculaire de la RNFL) ou PEV (latence P100 retardée) » ; source : « Source internationale : Montalban et al., révision 2024 des critères de McDonald, Lancet Neurol 2025;24:850 ; Saidha et al., Lancet Neurol 2025;24:880 — résumés secondaires ». | Résumés ECTRIMS et PubMed 40975103 |
| G2 | 009 · `gold`, `valeurs_normales[1]`, `traitement[0]`, `sources[0]` | « ERC-ESICM 2021 » ; « Contrôle ciblé de la température » | **Grave** | Remplacer toutes les mentions 2021 par « Source européenne : Nolan, Sandroni et al., ERC-ESICM 2025, post-réanimation, Intensive Care Med 2025;51:2213 (Resuscitation 2025;215 Suppl 1:110809) — notice PubMed lue ; détails par revue secondaire ». `traitement[0]` = « prévenir activement la fièvre (≤ 37,5 °C) pendant 36 à 72 h chez tout patient comateux ». Ajouter : « ERC 2025 introduit des prédicteurs de bon pronostic (NSE < 17 µg/l, réponse motrice 4–5 à 72–96 h) » ; NSE > 60 µg/l à 48 et/ou 72 h reste valable. Ajouter « Swiss Resuscitation Council (adopte ERC 2025) — À vérifier ». | PubMed 41123621 ; Front Med 2026 (lue) |
| G3 | 048 · `traitement[0]` ; 049 · `traitement[0]` | « défibrillation immédiate et réanimation (ERC) » | **Grave** | « (Source européenne : ERC 2025, Adult Advanced Life Support, Resuscitation 2025 ; amiodarone 300 mg après le 3e choc, 150 mg après le 5e) ». Pour 049, ajouter « ERC 2025 bradycardie » en source. | ERC 2025, page des chapitres (lue) ; AIPS 59528 |
| G4 | 025 · `lecture[2]` | « Combiner : HIT normal + nystagmus changeant de direction + skew = central (AVC) » | **Grave** | « Un seul signe suffit pour évoquer une cause centrale : HIT normal, OU nystagmus qui change de direction, OU skew deviation (INFARCT). Le HINTS ne s'applique qu'au syndrome vestibulaire aigu continu avec nystagmus. » | Kattah, Stroke 2009;40:3504 (cité dans le fichier) |
| G5 | 016 · `sources[1]` | « Source européenne : Pediatric Eye Disease Investigator Group (PEDIG) » | **Grave** (étiquette fausse) | « Source américaine : PEDIG (NEI, États-Unis) » ; chercher la source suisse : Swiss Paediatrics / Société suisse d'ophtalmologie. | Fait vérifiable : le PEDIG est financé par le NEI américain |
| G6 | 006 · `traitement[2]` ; 013 · `traitement[1]` | « Corticothérapie ou ACTH en alternative (dose non citée) » ; « aflibercept, faricimab (dose non citée) » | **Grave** | 006 : « tétracosactide : indication “Syndrome de West” (AIPS Synacthen® n° 31723, juin 2023) ; dose : citer la rubrique Posologie ». Remplacer « en alternative » par « en première ligne, au même rang que la vigabatrine (sauf sclérose tubéreuse) ». 013 : « faricimab : “6 mg (0,05 ml)… toutes les 4 semaines… lors des 4 premières injections” (AIPS Vabysmo® n° 68395) ; aflibercept : “dose recommandée de 2 mg” (AIPS Eylea® 2 mg n° 62393) ». | AIPS 31723, 68395, 62393 (lues) |
| G7 | 035 · `traitement[1]` | « prednisone : « doit être dosé dans chaque cas … » » | **Grave** | Ajouter la mise en garde de l'AIPS : « myasthénie grave et inhibiteurs de la cholinestérase : … le risque d'une crise de myasthénie est augmenté ; les inhibiteurs de la cholinestérase devraient … être arrêtés 24 heures avant » (AIPS Prednisone Streuli® 29349) ; débuter à faible dose et augmenter progressivement. | AIPS 29349 (lue) |
| M1 | 001 · `traitement[0]`, `sources[2]` | « 500 mg deux fois par jour » (forme pour perfusion) | Moyen | Citer la forme orale (Levetiracetam DESITIN cpr n° 65154) et le texte complet : « adultes et adolescents dès 16 ans de 50 kg ou plus : 500 mg deux fois par jour ; dose initiale plus faible de 250 mg deux fois par jour possible ». | AIPS 62616 (lue) |
| M2 | 004 · `gold.premiere_intention` ; 046 · idem | « Aciclovir i.v. empirique… » ; « Manœuvre vagale ou adénosine… » | Moyen | 004 : « IRM cérébrale avec diffusion et FLAIR, puis ponction lombaire ; aciclovir i.v. dès la suspicion sans attendre ». 046 : `null` (le gold, l'ECG 12 dérivations, est déjà l'examen de première intention) ; laisser l'adénosine en rang 2. | Cohérence interne |
| M3 | 051 · `autres[2].montre` vs `calculs[0]` | « < 80 % de la fréquence prédite » ; « < 80 % de la réserve (ou < 85 % de FMP) » | Moyen | `montre` = « FC maximale < 85 % de la FMP, ou indice chronotrope < 0,8 de la réserve » ; dans l'exemple, ajouter la réserve (FC de repos 60/min : (110 − 60)/(150 − 60) = 56 %). | Calcul refait |
| M4 | 037 · `gold.examen` | « au moins trois régions … critères de Gold Coast » | Moyen | « EMG dans ≥ 2 régions (Gold Coast : atteinte du motoneurone périphérique dans au moins 2 régions, ou centrale et périphérique dans 1 région) ». | Shefner, Clin Neurophysiol 2020;131:1975 |
| M5 | 010 · `valeurs_normales`, `sources` | « EGS … 5e éd. 2020 » | Moyen | « Source européenne : EGS, Terminology and Guidelines, 6e éd., Br J Ophthalmol, septembre 2025 — résumé ». | Résumés EGS/Medthority |
| M6 | 037 · `sources[2]` ; 033 · `sources[1]` | « EFNS 2012 SLA » ; « EFNS/EAN … 2010 » | Moyen | 037 : « Source européenne : EAN/ERN EURO-NMD, SLA, Eur J Neurol 2024 — À vérifier ». 033 : « NeuPSIG 2025 (Lancet Neurol 2025) — À vérifier », car EFNS 2010 est dépassé. | Non lu (référence à confirmer) |
| M7 | 005 · `sources[0]`, `sources[1]`, `traitement[2]` | « OFSP … non lu, À vérifier » ; « Source internationale : critères diagnostiques CDC 2018 » | Moyen | « OFSP, MCJ à déclaration obligatoire ; Centre national de référence des maladies à prions (NRPE), Zurich (bag.admin.ch) » ; « Source américaine : CDC 2018 » ; ajouter une source européenne : critères européens actualisés (Hermann et al., Lancet Neurol 2021 — À vérifier). | Pages OFSP (résumé lu) |
| M8 | 023 · `sources[1]` ; 027 · `valeurs_normales[0]`, `sources[0]` ; 041, 044 · `sources` | « Source internationale : JCIH 2019 » ; « Source américaine : ASHA 1994 » ; Robinson 2000 ; Nuwer 2012 | Moyen | Étiqueter ainsi : « Source américaine » pour JCIH, Robinson et Nuwer. Ces entrées n'ont qu'une source américaine : chercher puis ajouter une source suisse ou européenne. Pour 027 : IGHG/PanCareSurFup (Clemens et al., Lancet Oncol 2019 — À vérifier). | §13.1 du prompt V0 |
| M9 | 002, 004, 005 · `lecture` (gabarit EEG) | « Lire les activations (hyperpnée, SLI) » ; « réactivité à l'ouverture des yeux » | Moyen | Chez le patient confus ou comateux, écrire : « Tester la réactivité aux stimuli auditifs et douloureux ; aucune activation par hyperpnée ». | Gabarit inadapté |
| L1 | 006 · `traces.normal` vs `lecture[0]` | « 10 µV/mm » / « 7 µV/mm » | Léger | Unifier la sensibilité à 10 µV/mm chez l'enfant. | — |
| L2 | 033, 034 · `lecture[0]` | « ≥ 32 °C aux membres supérieurs » | Léger | Ajouter « ≥ 30 °C aux membres inférieurs », car on mesure le sural et le tibial. | — |
| L3 | 018–021, 026 · `valeurs_normales[0]` | « ≤ 20 dB HL » | Léger | « < 20 dB HL » (grade OMS 2021 : surdité légère dès 20 dB). | OMS 2021 |
| L4 | 019 · `gold.pourquoi` | « otospongiose (type A, réflexe aboli) » | Léger | « type A ou As (compliance abaissée) ». | — |
| L5 | 045 · `calculs[1]`, `traitement[0]` | « AVC/AIT 2 » | Léger | « AVC, AIT ou embolie systémique 2 ». Ajouter la clairance de la créatinine de 15 à 29 ml/min à la réduction de dose d'apixaban (AIPS 61549). | ESC 2024 ; AIPS |
| L6 | 002 · `sources[1]` ; 011 · `sources[0]` | « ESETT … européenne/internationale » ; « ESE 2022/Pituitary Society » | Léger | « Source américaine : ESETT » ; « Source internationale : Pituitary Society, consensus 2023 (Petersenn et al.) ». | — |
| L7 | 029 · `valeurs_normales[0]` | « Vogt et al., … Rhinology 2016;54(Suppl 25) » | Léger | Référence non retrouvée. Vérifier la référence ou la remplacer par « consensus RIGA, Rhinology 2018;56:133 — À vérifier ». | — |
| L8 | Global | Sources suisses quasi absentes (SSC, Suva, SGKN, Ligue Épilepsie marquées « non lu ») | Léger à Moyen | Ouvrir et dater : Suva (bruit), epi.ch (conduite), SSC (adoption des recommandations ESC), Swiss Stroke Society. À défaut, écrire « (cherché : site, date) ». | expert-web |

## 2. Points vérifiés sans défaut

Les citations AIPS suivantes sont exactes au mot, ainsi que leur numéro et leur date : aciclovir, lactulose, rifaximine, vigabatrine, méthylprednisolone, latanoprost, cabergoline, ranibizumab, voretigène, prednisone (« surdité brusque absente » est exact), bétahistine, thiosulfate, mométasone, duloxétine, IgIV (0,4 g/kg/j × 5), pyridostigmine, amifampridine, riluzole, tofersen, vamorolone, midodrine (dernière dose ≥ 4 h avant le coucher), apixaban, adénosine, amiodarone et atropine i.v.

La fludrocortisone est signalée honnêtement comme hors indication. Les exemples de l'ESC 2024 (FA), de l'ESC 2021 (stimulation et resynchronisation), de l'ESC 2019 (TSV) et de l'ESC 2022 (arythmies ventriculaires) sont à jour. Les seuils de Salzbourg, de Bárány et de l'échelle PAS sont exacts.

## 3. Calculs refaits (Python)

| Calcul | Résultat |
|---|---|
| QTc Bazett 400/√0,8 | 447,2 ms |
| CHA2DS2-VA, homme de 72 ans hypertendu | 2 |
| PTA | 45 dB |
| TDI | 27 |
| Décrément | 25 % |
| Incrément | 150 % |
| ΔFC/ΔPAS | 0,2 |
| TCCM | 8 ms |
| FMP | 150, soit 73 % |
| FC 300/4 | 75/min |

Les dix calculs sont exacts. Seule la définition de 051 est incohérente (M3).

## 4. Score §12.2 (7 critères × 2 = 14)

| Critère | Note | Raison |
|---|---|---|
| Gold, 1re intention, ordre | 1 | Erreurs en 004, 007 (EEG), 037 et 046 |
| Lecture du tracé | 1 | HINTS faux (G4) ; gabarit EEG inadapté au coma |
| Valeurs normales et unités | 1 | Seuil EEG attribué à tort à l'ASSM ; aucune norme suisse |
| Calculs | 2 | 10/10 exacts |
| Syndrome et traitement (AIPS) | 0 | 3 critiques AIPS (C3, C4, C5) |
| Actualité (ERC 2025, ASSM, McDonald, EGS) | 0 | ERC 2021, McDonald 2017, EGS 5e éd., ASSM « non lu » |
| Sources étiquetées et honnêtes, traces | 1 | Les traces sont précises, mais le PEDIG porte une étiquette fausse et 5 entrées n'ont qu'une source américaine |
| **Total** | **6/14 = 43 %** | |

## 5. Verdict

**Refusé.** Le lot contient 5 critiques (C1 à C5), 7 graves et 9 moyens.

Question finale « Ce lot peut-il servir tel quel à un candidat suisse ? » : **non**. Il faut d'abord :
- corriger l'EEG présenté comme examen admis par l'ASSM ;
- citer Rivotril pour l'état de mal, Depakine et sa restriction chez la femme, et l'atropine pour l'amblyopie ;
- passer à ERC-ESICM 2025, à McDonald 2024 et à EGS 2025 ;
- corriger le HINTS ;
- corriger les étiquettes des sources américaines.
