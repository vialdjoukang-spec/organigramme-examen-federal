# Sources et lectures — LOT039 — 31.10.2026

sources.json porte désormais54références, dans l’ordre des exposants :14pour PhaseA puis les ajouts DX1–6. Les JSON lot39_* et39dx* conservent les réponses exactes des outils : pages et passages effectivement exposés, résultats de recherche, éventuelles limites de fenêtre. Ils ne constituent pas une archive intégrale de tous les sites ni une preuve de lecture des liens non ouverts.

- lot39_initial : recherche initiale suisse.
- lot39_ch1 : HUG décollement de rétine/diagnostic, Jules-Gonin diplopie, SSO signes d’urgence.
- lot39_ch2eu : HUG cataracte/glaucome/DMLA ; début du chapitre CEN diplopie.
- lot39_neuro : recherche neurologique et passages CEN sur les causes urgentes de diplopie.
- lot39_detail : Jules-Gonin névrite optique, HUG rétine/uvéite ; HUG migraine lu mais mécanisme vasculaire simplifié non utilisé ; début COUF.
- lot39_triage : critères/commentaires ICHD-3 aura et passages COUF sur occlusion artérielle, bilan vasculaire et artérite. Lecture ciblée des passages, pas tout le chapitre.
- lot39_relecture_recherche puis lot39_relecture_ch : recherche et lecture des pages HUG diagnostic DMLA (03.09.2025) et glaucome formes/diagnostic (18.04.2024), ajoutées comme sources13/14.

Dates : retenir les dates affichées par les pages, pas l’estimation de publication du moteur. Copyright ICHD-3 2021 n’est pas une date de révision démontrée. SSO/CEN/COUF : date exacte de révision non établie dans les passages lus.

Aucun médicament dosé prescrit dans la Phase A et aucun extrait AIPS : ne pas présenter un contrôle de zéro citation comme validation pharmacologique. Compléter avant monographies concernées.

autorisation_reprise.json : preuve de séquence, périmètre et contrôle avant production. Aucun autre automate ni harnais commun modifié.

## Lectures spécifiques DX1–4

- 39dx1_search/ch/clinique/complement : Jules-Gonin myopie, hypermétropie, astigmatisme, presbytie et brochure lentilles ; HUG chirurgie réfractive ; Ameli diagnostic pédiatrique. Les premières fenêtres contenant surtout la navigation ont été complétées par la lecture clinique ciblée.
- cyclogyl_frais.html/.txt et AIPS_32634.json : texte officiel frais intégralement lu, empreintes et référence commune. formes_swissmedic_32634.json : deux dosages et conditionnements relus, sans modification de la source commune.
- 39dx2_search/read/guidelines/eu_ch : SSO cataracte, HUG chirurgie/avant/après/laser capsulaire ; recommandations principales ESCRS. NICE403 en accès direct, passages indexés effectivement affichés lus. Aucun accès intégral à NICE ou annexes ESCRS revendiqué.
- aprokam_frais.html/.txt et AIPS_63029.json : notice officielle fraîche intégrale ; formes_swissmedic_63029.json vérifie les conditionnements. audits/aips_checkpoint_dx4.json rattache les60extraits aux empreintes finales des deux HTML et aux notices.
- 39dx3_search/read/eu/suivi : HUG causes/diagnostic rétinien, Cambridge DPV version6 février2026, RNIB et NHS. PDF RCOphth expiré, pas déclaré lu. RNIB et NHS dates2023 conservées malgré révision attendue2026 non affichée.
- 39dx4_search/ch_eu/formes/formes_ch : HUG traitement et retour après décollement, SSO traitement/formes/diagnostic/pronostic, Cambridge chirurgie version8 avril2026, alerte professionnelle RCOphth protoxyde2018. Premier clic par URL refusé puis clics par référence réussis, erreurs conservées. Page SSO des formes : titre réel « Formes de décollement de la rétine », chemin URL « blessures-oculaires-dans-la-vie-quotidienne » conservé tel qu’observé.

Les résultats étrangers hors Europe non ouverts ne sont pas utilisés comme références lues. Les pourcentages généraux des brochures ne sont pas présentés comme une étude de fréquence suisse. Les arbitrages cliniques et limites sont détaillés dans les relectures et HELP.


## Lectures DX5–6

- 39dx5_search/ch_eu/detail/eu_clinique : HUG diagnostic, traitement DMLA et injection ; Jules-Gonin ; NHS et HCL ; EMA refus Syfovre. NICE403 et NCBI vérification d’accès non déclarés lus intégralement. Dates HUG2025, NHS22.01.2025, HCL26.02.2026, EMA page30.10.2025 avec décision2024 distinguées.
- Eylea2 : notice fraîche septembre2026, sections cliniques réellement lues, sans prétendre lire tous les résultats d’essais. AIPS_62393002.json et formes_swissmedic_eylea.json distinguent clé documentaire, seringue62393, flacon62397 et présentations2mg/8mg.
- 39dx6_search/ch/eu/eu_detail/egs_page : HUG formes/diagnostic et laser, SSO glaucome, Belgian Glaucoma Society ; RCOphth sections initiales, diagnostic et prise en charge aiguë exposées. PDF réellement publié juin2022 malgré chemin2026. La page EGS6 est accessible, pas le contenu du livre : téléchargement officiel en erreur, miroir trop volumineux via web et tunnel403 via shell. Aucun chapitre EGS6 présenté comme lu.
- Diamox et Timoptic : notices officielles fraîches HTML/textes/gzip. Les paragraphes cliniques indication, posologie, contre-indications, précautions, interactions, grossesse/allaitement ont été lus. Pas tous les essais cliniques. La lecture des archives communes avait montré des coupures internes de mots ; sources communes préservées, citations fondées sur le texte frais. AIPS_21191.json et AIPS_41634.json indiquent ce choix et les empreintes. Formes Swissmedic vérifiées dans formes_swissmedic_dx6.json : comprimés21191, injectable22002, Timoptic41634 distinct de XE52509.
- Glaupax38412 : archive parcourue mais affichage tronqué ; produit non prescrit ni cité dans DX6. Pas de lecture intégrale revendiquée.
- Comparateur local _travail/verifier_aips_checkpoint.py :140paragraphes des DX1/2/5/6 retrouvés dans les HTML frais. Deux modes de sérialisation DOM explicités pour les anciennes citations Aprokam, sans rapprochement approximatif des mots. Échec initial conservé dans audits/aips_checkpoint_dx6_extraction_initiale.json.

Les rapports v8_dx5_initial et v8_checkpoint_dx5 sont historiques, antérieurs à la fin C07. Le checkpoint courant est v8_checkpoint_dx6.json ; BILAN_REPRISE.json porte les empreintes finales. Les fichiers HTML PhaseA et DX1–4 restent inchangés.

## Lectures DX7–8

39dx7_search_ch/ch/eu/details : Inselspital, Jules-Gonin, HUG stratégie2025 (urgence et section6.4), HCL12.02.2026 et ICR06.03.2024. Dexafree et Atropine : notices fraîches intégralement lues, formes Swissmedic vérifiées ; fichiers HTML/texte/gzip et AIPS_57477/AIPS_46994035.

39dx8_search_ch/ch/ch_eu/search_eu/eu/detail/examsearch/exam/examdetail/examclinique : sources CH puis européennes, sorties exactes conservées. CHUV introduction et annexe3 lues, pas tout le protocole. JG18.08.2025 ; OnO11.03.2025 avec limites étiologiques ; HCL névrite et NMO12.02.2026, MOG17.03.2026. NEMOS introduction, poussées et début prévention, correction ravulizumab05.04.2024 lue, pas les tableaux thérapeutiques complets. CEN passages neuropathies/urgences/pupille et SFO orientation/atypies/diagnostic, pas chapitres entiers. Solumedrol_frais : sections cliniques et manipulation lues, limites dans AIPS_35112.json. Formes500mg/1g vérifiées.

Checkpoint courant v8_checkpoint_dx8.json et aips_checkpoint_dx8.json :223citations retrouvées, dont49DX7 et34DX8. Les sept HTML préexistants sont conservés.


## Lectures DX9–10 et clôture

39dx9_search_ch/ch_eu/chdetail/chsuite/typique : Société suisse des céphalées édition11.2 (date exacte non établie), HUG stratégie2017, ICHD-3 aura générale/typique/rétinienne, synthèse SFEMC2021 et mécanismes Inserm2020. Lecture ciblée, pas toutes les30pages suisses. Notice Imigran fraîche septembre2025 et Algifor décembre2024 : sections cliniques lues, pas toutes les données d’essais/précliniques. HTML/texte/gzip, métadonnées et formes_swissmedic_dx9.json conservés. 56paragraphes cités.

39dx10_ch_cen/eu/urgences/europe_lue/recherche3/complements/iii_article : Jules-Gonin diplopie et CHUV introduction/annexe3 relus, CEN examen/causes/urgences réellement affichés, COUF introduction/imagerie, Sussex clinique/prismes/suivi, filière BHR, correspondance Patel–Burdon sur PMC. Les limites et éléments non retenus sont explicités dans RELECTURE_DX10.md. PDF écossais refusé403 via web et shell ; Nature redirigé vers authentification, pas déclaré lu. Une première URL Nature incorrecte n’est pas retenue ; l’identifiant exact01349-1 a été retrouvé par recherche puis article lu sur PMC8727561.

Clôture : v8_final.json, aips_final.json, COHERENCE_FINALE.md et BILAN_REPRISE.json font foi pour les onze HTML. Les contrôles antérieurs restent des états historiques. Les279extraits sont retrouvés sans modification des notices communes. Neuf HTML du checkpoint d32097a9 inchangés.
