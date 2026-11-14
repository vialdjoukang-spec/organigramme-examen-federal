# Audit médical V2 — fiches Status S-25 à S-35 (14.11.2026)

Tour de vérification de `CORRECTIONS_STATUS_25_35.md`.

**Méthode.**
- J'ai relu les 11 JSON après correction, champ par champ, en les aplatissant.
- J'ai listé `img/` et vérifié qu'aucun JSON ne pointe vers un fichier absent.
- J'ai cherché les fichiers retirés dans les JSON et dans `STATUS.html`.
- J'ai lu le rendu de la fenêtre occultante dans `generer_status.py` et `STATUS.html`.
- Je n'ai fait aucune nouvelle requête web : les sources ont été lues au premier tour.

## 1. Critique et majeurs : contrôle

| N° | Point | État | Preuve |
|---|---|---|---|
| C1 | S-30, horloge Elsevier | Corrigé | Le fichier est absent de `img/`. Le nom n'apparaît plus que dans le texte `a_fournir`, qui explique le retrait. |
| M1 | S-28, Thomas 2002 | Corrigé | Les trois signes portent Se et LR+ (0,97 ; 0,94) et une Sp déduite. L'interprétation devient « aucune valeur discriminante ». sources[3] porte « résumé lu ». |
| M2 | S-28, définition du Kernig | Corrigé | Angle cuisse-jambe d'environ 135° (« À vérifier »). |
| M3 | S-28, photo de 1909 | Corrigé | Le fichier est absent ; `a_fournir` décrit un adulte figurant. |
| M4 | S-32, Apgar | Corrigé | « Apgar 8 (2+2+2+1+1) ». |
| M5 | S-32, oxymétrie suisse 2005 | Corrigé | Mesure au pied le 1er jour : ≥ 95 % normal ; 90–94 % contrôle ; < 90 % ou contrôle < 95 % échocardiographie. Kuelling SMW 2009 cité. C'est conforme à la figure lue. |
| M6 | S-32, nouveau-né identifiable | Corrigé | Le fichier est absent ; `a_fournir` prévoit un cadrage sous le menton. |
| M7 | S-33, courbes 2026 | Corrigé | Courbes dans materiel[3], manoeuvres_speciales[0].technique[1] et sources[1] : 15.06.2026, PEZZ, OMS pour l'IMC de 0 à 2 ans, Zurich et KiGGS. |
| M8 | S-30, ASSM 2019 et articles CC | Corrigé | Quatre capacités ASSM § 2.4 et seuil « fortement limitées » § 2.5. Art. 370 ss, 378 et 379 CC. |
| M9 | S-25, HINTS+ | Corrigé | technique[4] HINTS+ avec HUG 2024. Valeur Kattah : « 101 patients, ≥ 1 facteur de risque, résumé lu ». La mention des neuro-otologistes est retirée. |
| M10 | S-34, TUG | Corrigé | > 15 s (World Falls Guidelines, « À vérifier ») et ≥ 12 s (STEADI) côte à côte. HUG 2026 cité. Lever de chaise : EWGSOP2. |
| M11 | S-35, codes EPA | Corrigé | 2kk = influence, 2ll = violences, 2mm = mort et heure du décès, dans epa et sources[0]. L'estimation grossière du délai est ajoutée. |

Les mineurs du premier tour ont aussi été vérifiés : S-26 (clonus, NINDS), S-27 (IWGDF, rétropulsion), S-29, S-31, S-35 (art. 253 al. 4, TEN-4, Langlois « britannique »).

La fenêtre occultante des lividités est active : `"occulter": true`, classe `vignette occ`, flou de 28 px et voile cliquable dans `STATUS.html`.

Je n'ai relevé aucune erreur médicale nouvelle.

## 2. Défauts résiduels (tous mineurs, non bloquants)

| Grav. | Fiche, champ | Ancien → Nouveau |
|---|---|---|
| Mineur | generer_status.py l. 149 (voile) | Le texte « Image intime masquée » est faux pour un défunt. → `img.get("voile", "Image sensible masquée : cliquer pour l’ouvrir")`, et dans S-35 manoeuvres_speciales[1].image ajouter `"voile": "Image de défunt masquée : cliquer pour l’ouvrir"`. |
| Mineur | S-35 manoeuvres_speciales[1].image.credit | La consigne « Image de défunt, à afficher derrière une fenêtre occultante. » est redondante maintenant que le voile existe → « Image de défunt. goga312, Wikimedia Commons… ». |
| Mineur | S-26 duree.cs et version_cs.cible | « épreuves de Barré et de Mingazzini » / « Il réalise Barré et Mingazzini » → « épreuve des bras tendus et épreuve de Mingazzini ». |
| Mineur | S-25 manoeuvres_speciales[9].interpretation | « Profil périphérique (…) : névrite vestibulaire » → « Profil périphérique (…) **et audition normale** : névrite vestibulaire ». Cela met l'interprétation en cohérence avec le HINTS+. |
| Mineur | S-30 sources[2] | « art. 16 … et art. 377 ss … non relu, À vérifier » → « art. 16, 370 ss, 377–378 et 379 CC (art. 379 lu ; autres non relus, À vérifier) ». |
| Mineur | S-30 examen_complet[Manœuvres].gestes[9].anomalies[0].signifie | « représentant thérapeutique, directives anticipées » → « directives anticipées, puis représentant thérapeutique ». |
| Mineur | S-32 sources[1] | « Kuelling B et al. » → « Kuelling B » (auteur unique). |
| Mineur | S-35 sources[3] | « art. 253 … textes non relus » → « art. 253 CPP lu (al. 4) ; art. 321 CP et LAVI non relus, À vérifier ». |

Restent hors de mon audit, sur décision de Vial :
- la règle sur les gravures historiques ;
- le recadrage de la photo Weber ;
- les 10 licences Commons non relues (HTTP 429).

## 3. Verdict
**audit-ok.** Le critique et les 10 majeurs sont corrigés, sans erreur nouvelle. Les 8 mineurs ci-dessus peuvent suivre sans bloquer la publication.

Réserve : les 10 licences Commons non relues restent à vérifier avant mise en ligne publique.
