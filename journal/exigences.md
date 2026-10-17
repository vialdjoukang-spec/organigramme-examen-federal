# Journal · Exigences et session 2027 · Thémis

Chaque entrée porte une date (Europe/Zurich), une décision et les sources lues. Aucune donnée personnelle n’entre dans ce journal public.

- 17.10.2026 · Thémis remplace les 16 points indexés (clés e0…e15) par 46 cases à identifiant stable (A1…F8, clé « x:<id> ») dans data/EXI.json, et centralise les dates dans data/SESSION.json ; tools/build_exi.py régénère les deux fichiers, et le patch 0004 les injecte en JSON strict.
- 17.10.2026 · La migration reporte e3→C6, e4→C1, e5→B1, e6…e12→B2…B8, e13→D1 et e14→F6 une seule fois (drapeau _m27) ; elle conserve les anciennes clés, et e0, e1, e2 et e15 n’ont pas d’équivalent, car le format et la nomenclature relèvent de l’onglet « Attendus ».
- 17.10.2026 · Le bandeau déclare la session 2026 terminée, affiche l’inscription 2027 du 15.12.2026 au 31.03.2027 (portail healthreg) et un compte à rebours ; les dates CK 10 et 12.08.2027 et CS 06–10.09.2027 portent « à confirmer », car seule la faculté de Genève les annonce (N1).
- 17.10.2026 · Les textes restent génériques : le dépôt est public, et aucune donnée personnelle n’y entre ; les coches restent dans le navigateur.
- Sources : S1 à S12 et N1 de research_exigences.md, toutes lues le 17.10.2026.
- Points encore à vérifier auprès de la MEBEKO (11 cases) : A3 (sens de « reconnaissance partielle »), A4 (examen complet ou partie théorique), C4 (pièces de l’inscription 2027), C6 et C7 (langue d’examen 2027), C8 (site attribué), C10 (date limite 2027 de la compensation des inégalités), D2 (solde de l’émolument), D5 (taxe partielle), E2 (dates 2027), E3 (date de publication des documents 2027).
- Suite : Thémis met SESSION à jour dès que l’OFSP publie les documents 2027, et traite chaque ticket veille:officiel d’Argos.
