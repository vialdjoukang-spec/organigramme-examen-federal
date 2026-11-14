# Audit médical — tour de vérification V2, SY-28 à SY-54 (14.11.2026)

## Méthode

- J'ai lu `CORRECTIONS_SYNDROMES_28_54.md`, puis les champs corrigés des 27 JSON.
- **AIPS citées.** J'ai rouvert par URL refdata (`aips_fiche.py fiche`) les 35 AIPS citées, dont les nouvelles : Insulines HM n° 44610, Bactrim forte n° 48306, Hydrocortisone Galepharm n° 57970, Metronidazol i.v. B. Braun n° 48018, Lasix comprimés n° 30629, Morphini HCl Streuli n° 56554, Kaliumchlorid B. Braun n° 29552, Trandate n° 41529, Aspirine Cardio n° 51795, Albumin CSL 20 % n° 52476, Erythrocin i.v. n° 20258 et Naloxon OrPha n° 56952 (schéma du surdosage).
- **Citations.** Les citations des drapeaux rouges, des examens et du management sont comparées au texte AIPS en cache. Toutes sont retrouvées, aux espaces de refdata près (« 0 . 4 », « mmol / l »). Seules restent hors cache les citations HUG ou RMS, qui ne sont pas des AIPS.
- **Corpus.** `trouve` ne trouve aucune AIPS de gluconate de calcium injectable : seul un hydrogel 2,5 % figure au corpus. La mention « absente » de SY-42 est donc exacte.
- **Sources HUG.**
  - Stratégie HUG « Maladie rénale chronique » 2024 (PDF hug.ch lu ici) : elle dit mot pour mot que le dépassement d'une kaliémie de 5,5 mmol/l « constitue un critère d'initiation de dialyse ». SY-42 est conforme.
  - Stratégie HUG « Asthme » 2026 : déjà contrôlée au premier tour.
- **Seuils de JBDS.** Recherche web limitée à des protocoles hospitaliers secondaires qui citent JBDS ; le texte primaire de JBDS n'a pas été lu.
- **Images.** Lues : SY-35 et SY-50 sont recadrées sur un œil, et aucun visage n'est identifiable. SY-51 est bien retirée : le fichier est supprimé, le JSON passe en « a_fournir » et aucun autre fichier n'y renvoie.

## Verdict : **corrections requises** (1 grave). Après le PATCH G4, le lot peut passer en **audit-ok**.

## État des 9 critiques et 3 graves du premier tour

| # | Fiche | État | Preuve AIPS ou source |
|---|---|---|---|
| C1 | SY-54 | Corrigé | « Seul Actrapid HM (solution d'insuline) peut être administré par voie intraveineuse » ✓ |
| C2 | SY-47 | Corrigé | L'aspirine en prévention est déclarée hors AIPS ✓ |
| C3 | SY-47 | Corrigé | « jusqu'à une dose de 160 mg/h » ; contre-indication asthme/BPCO ✓ |
| C4 | SY-45 | Corrigé | Bactrim forte 1 cp matin et soir, « à intervalles de 12 heures » ✓ |
| C5 | SY-53 | Corrigé | « Insuffisance surrénale chronique: 10 à 20 mg par jour… » ✓ |
| C6 | SY-32 | Corrigé | 15 mg/kg puis 7,5 mg/kg toutes les 6 h ✓ |
| C7 | SY-36 | Corrigé | « ½ à 1 à 2 comprimés/jour » ✓ |
| C8 | SY-29, SY-47 | Corrigé | Mg « Bichsel » n° 56394, octobre 2025 ✓ |
| C9 | SY-28, 32, 43, 48 | Corrigé | Morphine « 2 – 10 mg » IV ✓ (voir L1) |
| G1 | SY-42 | Corrigé | Calcium, insuline-glucose (hors AIPS, signalé) et salbutamol (hors AIPS) ; seuils RMS ✓ |
| G2 | SY-54 | **Partiellement** : voir G4 | KCl AIPS ✓ (« 40 mmol/l K+ dans la solution », « 10 mmol/l heure », 200 mmol/j) |
| G3 | SY-29, 30, 31 | Corrigé | Cible de SpO2 de 88 à 92 % attribuée à HUG BPCO 2026 (citation non relue par moi ; plausible) |

Corrections secondaires contrôlées : M1 (dates « Mise à jour » : Atrovent octobre 2024 ✓, Inderal janvier 2023 ✓…), M2 (contre-indication Inderal citée), M4 (albumine : AIPS « individuellement », « 1-2 ml/min » ✓), L4 (naloxone « 0.4 à 2 mg » ✓), L5 (Erythrocin hors AIPS ✓).

## Défaut restant — PATCH exact

| # | Gravité | Emplacement | Extrait | PATCH |
|---|---|---|---|---|
| G4 | Grave (seuil d'urgence mal attribué) | SY-54 drapeaux[1] et management[1] | « Kaliémie < 3,3 mmol/l … (source britannique : JBDS 2011 …) » ; « rien au-dessus de 5,3 mmol/l, de petites quantités entre 3,3 et 5,3 mmol/l (JBDS 2011 …) » | Les seuils 3,3 et 5,3 mmol/l sont américains (ADA), pas britanniques. Les protocoles qui citent JBDS utilisent > 5,5 / 3,5–5,5 / < 3,5 mmol/l. Écrire : « K⁺ > 5,5 mmol/l : pas de potassium ; 3,5–5,5 mmol/l : 40 mmol de KCl par litre de soluté ; < 3,5 mmol/l : avis senior et potassium supplémentaire (source britannique : JBDS, via des protocoles hospitaliers secondaires, À vérifier dans le texte JBDS) ; la concentration de 40 mmol/l respecte le maximum de l'AIPS Kaliumchlorid B. Braun n° 29552 ». Si le seuil d'insuline différée < 3,3 mmol/l est conservé, l'attribuer à « (source américaine : ADA, Kitabchi 2009 — non lu) ». |

## Légers

L1 : le maximum « Généralement, ne pas dépasser une dose journalière de 100 mg » se rapporte, dans l'AIPS Morphini HCl Streuli, à la perfusion continue. Écrire « (en perfusion continue) » dans SY-28, 32 et 48.
L2 : SY-48 renvoie à une « posologie pédiatrique de la même AIPS », mais ce tableau vise les gouttes orales chez l'enfant de moins de 12 ans. Pour le cas de 14 ans, la dose adulte s'applique : supprimer le renvoi pédiatrique.
L3 : les recadrages SY-35 (≈ 150 px) et SY-50 (≈ 120 px) sont très petits ; préférer un recadrage depuis l'original en pleine résolution.
L4 : SY-42 drapeaux[0] devrait préciser « hyperkaliémie réfractaire », comme le fait la même stratégie HUG (indications de dialyse : « troubles métaboliques réfractaires tels que … l'hyperkaliémie »).

Question finale : **non** tant que G4 reste ouvert ; **oui** après G4.

## Clôture
G4 et les légers L1, L2, L4 appliqués ; L3 (recadrage plus fin de SY-35) reporté faute d'accès à Commons (429), image déjà sans visage identifiable : **audit-ok** pour SY-28 à SY-54.
