# JOURNAL — LOT_017 — S1.1 Diplopie, ptosis, mouvements oculaires anormaux — Phase A

Rédacteur Phase A, 30.10.2026 (Europe/Zurich). Une ligne par hypothèse ou décision prise sans règle explicite (HARNAIS §4 : choix le plus prudent pour le patient).

## Lectures préalables
- Lus : `DECISION_SEANCE.md`, `LECONS_LOT_016.md`, `LOT_016/LECONS_LOT_015.md`, Prompt V0 §9–14 (lecture ciblée), extraction des points 1–2 de la Phase A de LOT_016 (modèle de structure), `harnais/controle_lot.py` (règles), `harnais/audit_langue.py` (règles de sigles et d'abréviations).
- Non lus, sur ordre du brief : `CONTINUATION.md`, `PROCHAINE_ACTION.md`, `ETAT.md`, `porte.py`, `checkpoint.py`.

## Hypothèses et décisions
1. Critère d'ordre du Bloc 2 : fréquence comme cause d'un ptosis ou d'une diplopie binoculaire acquis chez l'adulte en Europe. Le ptosis aponévrotique passe en DX.1 (8,5 % des 50 ans ou plus, calcul dérivé 34/400 de S35), devant la paralysie microvasculaire (26,8 % des diplopies binoculaires, S5). Ordre indicatif (HELP H17-07).
2. Rangs 5 à 9 : sans série commune, l'ordre suit la hiérarchie de Lagrèze (orbite avant tronc, S6), puis les incidences (S12, S14, S16, S24 × S38) ; l'ACG précède l'HTIC parce qu'un chiffre de diplopie existe pour l'ACG (7,15 %, S24) et pas pour l'HTIC.
3. Dix DX retenus parmi les quinze suggérés par le brief. Non retenus comme DX : botulisme, Miller Fisher, Wernicke, apoplexie pituitaire (rares ; placés en étape 0 de l'algorithme et dans la fenêtre « urgences hors liste ») ; traumatisme orbitaire (SSP S8.7) ; compression du sinus caverneux (catégorie fourre-tout, regroupée avec les tumeurs) ; strabisme décompensé et sagging eye (fréquents mais bénins ; SSP S1.20).
4. Gravité : E1 anévrisme (rupture mortelle), E2 AVC, E3 dissection, E4 ACG, E5 HTIC, E6 myasthénie (crise), E7 orbitopathie (neuropathie optique) ; E8 SEP, E9 microvasculaire (diagnostic d'exclusion), E10 ptosis aponévrotique.
5. Données des États-Unis (S17, S18, S19 ; S24 canadienne) : utilisées comme données primaires d'épidémiologie, jamais comme recommandation ; aucune recommandation exclusivement américaine citée.
6. S41 (rapport de cas) cité seulement pour le mécanisme des fibres pupillaires périphériques du III ; la conduite (imagerie de tout III) s'appuie sur S18 et S39.
7. Glyphes du PDF CHUV 2015 (S42) : seuils de CRP repris comme « ≥ 8 mg/L » et « ≥ 26,9 mg/L » (lecture « L » = ≥ cohérente avec « âge L 50 ans ») ; le seuil de poids « M 60 kg » n'est pas repris (HELP H17-12).
8. Doses : AIPS seulement (S2, caches `.cache/aips/19943.txt`, `29349`, `35112`, `23533`, `10989`, `21191`, `58314`, `69795`, `53770`). Hors information professionnelle écrit en clair : prednisone et IgIV dans la myasthénie, méthylprednisolone dans l'orbitopathie et l'ACG, thiamine 600 mg/j (EFNS), acétazolamide dans l'HTIC, sélénium dans l'orbitopathie.
9. Numéros Swissmedic par forme galénique lus dans les documents AIPS : Mestinon comprimés 10 mg 19943, dragées 60 mg 19945, retard 180 mg 56387 ; Benerva ampoules 10989, comprimés 25636.
10. Nouveaux caches AIPS écrits : `.cache/aips/19943.txt` (Mestinon), `58314.txt` (Privigen), `69795.txt` (TEPEZZA) ; documents téléchargés dans le sous-dossier scratchpad `LOT_017_PhaseA_redacteur/`.
11. Extraits recopiés de LOT_016 (contenu inchangé, provenance notée) : S40 (ESUR) et S43 (ESE/ES 2024).
12. Espaces insécables : aucune, selon la leçon 11 de LOT_015 et le modèle LOT_016, malgré l'alerte « insecable » de `audit_langue.py` (HELP H17-14).
13. Abréviations « i.v. » et « i.m. » : remplacées par « intraveineuse », « intramusculaire » (liste des abréviations interdites de `audit_langue.py`).
14. Âge dans l'ACG : « plus de 50 ans » (leçon 4 de LOT_016) ; dans les séries de paralysies isolées : « 50 ans ou plus » (critère de S17).
15. Crise surrénalienne de l'apoplexie pituitaire : dose ESE/ES 2024 (S43) signalée comme empruntée ; prélèvement de cortisol seulement s'il ne retarde rien (leçon 3 de LOT_016).

## Contrôles mécaniques
- `python3 harnais/controle_lot.py verifier "lot en cours de production/LOT_017" --sans-nom --json` : zéro critique, zéro avertissement ; 14 points présents ; 41 fenêtres popover.
- `python3 harnais/audit_langue.py … --json` : zéro critique ; avertissements restants « pv_simple » (indicatif) et « insecable » (décision 12).
- Aucun score attribué par le rédacteur (Prompt V0 §12.2).
