# Journal · Coordination, intégration et continuité · Athéna

Chaque entrée porte une date (Europe/Zurich), une décision et les sources lues. Aucune donnée personnelle n’entre dans ce journal public.

- 17.10.2026 · Les dix skills de la section 10 sont rédigés dans skills/ (une page chacun, sans donnée personnelle).
- 17.10.2026 · Le plan PDF et les notes de recherche restent hors du dépôt, car ils décrivent la situation personnelle du titulaire.
- 17.10.2026 · La version datée de phase 0 et les tickets de phase 1 attendent l’accord du titulaire (interdit I6).
- 17.10.2026 · Les tickets de phase 1 (#5 à #10) sont ouverts sur GitHub ; data/MEM.json est fusionné (PR #3) ; PR #4 (Argos) attend la CI après mise à jour sur main ; le chantier Atlas est prêt sur feat/sauvegarde (56/56 locaux).
- 17.10.2026 · Les dix skills sont présents dans la bibliothèque partagée de l’assistant.

### Brouillons des tickets de phase 1 (modèle « Tâche d’agent »)
1. **[Atlas] Export et import de la progression** · prio:P0 · agent:atlas · échéance 15.11.2026 · fiche Atlas, section 4 ; critères : export JSON complet, import avec migration, erreur de stockage visible ; test : tests/test_export.py.
2. **[Thémis] Refonte « Exigences » 2027** · prio:P0 · agent:themis · échéance 29.11.2026 · fiche Thémis ; critères : data/EXI.json, chaque case cite sa source officielle datée, chaque point non confirmé porte « À vérifier ».
3. **[Argos] Veilles officielles Ve1 et Ve2** · prio:P0 · agent:argos · échéance 15.11.2026 · section 11 ; critères : workflow planifié à 0 CHF, ticket seulement si l’empreinte change.
4. **[Argos] Faisabilité Ve3 et Ve4** · prio:P1 · agent:argos · échéance 29.11.2026 · section 11, encadré « À vérifier ».
5. **[Mnémosyne] data/MEM.json** · prio:P1 · agent:mnemosyne · échéance 29.11.2026 · section 7 ; critères : chaque méthode cite sa méta-analyse par DOI vérifié.
6. **[Janus] tests/test_export.py** · prio:P0 · agent:janus · échéance 15.11.2026 · avec Atlas.

- 18.10.2026 · Codex, Étape 0 : lecture intégrale AGENTS/CONTINUATION et lectures de porte faites ; catalogue réel et propositions examinés ; veille locale mode B, CLI non authentifié. Aucun travail clinique avant verifier0. Sources techniques : dépôt 2228be7, sorties gh, codex --help et tests locaux.
