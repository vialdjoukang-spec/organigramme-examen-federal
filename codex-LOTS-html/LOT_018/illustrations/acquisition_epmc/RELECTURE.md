# Relecture interne de provenance — 01.11.2026

Travail seul, sans sous-agents. Départ `2cca24335b22761beab1a2f6d72ccbf723e4e78e`, branche codex/lots et borne18–133 relues. Verrou officiel acquis ; registre du jour lu/signé, pret et verifier018 réussis. Aucune leçon modifiée.

## Lectures réellement faites

Les trois XML complets de Hao2022, Werner2019 et Heiferman/Fawzi2019 sont conservés avec leurs empreintes dans ACCES_API.json. Lecture ciblée des titres, auteurs, licences et légendes ; paragraphe appelant la figure1 de Hao également lu. L’acquisition du texte complet ne vaut pas lecture intégrale. Les trois notices Commons ont été relues. Les publications servent ici à établir la provenance des figures, pas à introduire des recommandations ni des doses.

## Correction PROV01

Commons indique que Fundus_-_diabetic_retinopathy.png provient de la figure1, panneauA de Hao et al. L’article original décrit sa figure1 comme un organigramme de l’étude. La figure2 présente deux photographies du fond d’œil ; la figure3 comporte l’interface et les annotations d’un logiciel d’IA. Ces légendes ne permettent pas d’identifier le fichier Commons sans comparer les pixels.

Le candidat rd-fond-oeil devient donc `suspendu_provenance`. L’ancienne attribution figure1A n’est plus présentée comme établie. Il n’est pas réattribué par supposition à figure2A. La licence CC BY4 annoncée dans Commons et présente dans l’article ne suffit pas, à elle seule, à résoudre cette discordance de panneau. L’importeur existant exclut cette décision. Un test local vérifie son refus avant requête même avec une politique réseau simulée autorisée.

Werner : la légende originale confirme l’œil droit et distingue photographie, angiographie34s après injection et OCT sans œdème maculaire cystoïde. La notice Commons décrit les deux premiers panneaux ; leur cadrage reste à examiner. Le masquage de fluorescence décrit n’est pas assimilé automatiquement à une non-perfusion.

Heiferman/Fawzi : la légende originale confirme une néovascularisation choroïdienne subclinique ayant évolué vers une DMLA exsudative. Les stades et les panneaux ne seront pas annotés avant inspection de l’image.

## Accès et limite réelle

Le domaine Europe PMC reste autorisé. Sa page et son API publique en lecture répondent maintenant200 avec le client identifié. Trois textes XML et trois métadonnées ont été acquis. Les métadonnées indiquent que les images sont hébergées sur `cdn.ncbi.nlm.nih.gov`, domaine actuellement exclu comme les domaines Wikimedia. Aucune requête vers ces hôtes exclus, aucun changement de proxy, de certificat ou de politique réseau. Aucun cliché acquis, annoté, inspecté ou intégré.

Le403 ancien n’est donc plus présenté comme un blocage de tout Europe PMC. Les premiers essais404 du mauvais chemin REST et403 du client urllib par défaut sont consignés avec leur portée limitée. Les chemins corrects proviennent du JavaScript public du site ; les réponses exactes sont conservées.

## Contrôles et correction RAP01

Le bilan affiche désormais neuf candidats retenus et un suspendu, dix notices candidates au total. Les11fiches et leurs tailles sont recalculées sans changer les leçons. Premier résultat144/145 conservé dans CONTROLE_BILAN_AVANT_CORRECTION.json : l’explication dépliée contenait le titre anglais sans le terme français « organigramme ». Ce terme a été ajouté ; seconde passe145/145.

Dix tests locaux de l’importeur passent ; HTTP simulé explicitement.22ouvertures de détails réelles dans Chromium, ordinateur et tactile émulé ;4captures du rapport inspectées. Le haut du rapport mobile et la fiche suspendue dépliée sont visibles dans les captures ; aucune inspection globale de toute la page mobile n’est prétendue. La comparaison SHA-256 confirme244leçons inchangées et neuf fichiers du harnais intacts.

Aucun nouveau contrôle V8, AIPS ou linguistique des leçons, aucun audit indépendant ni validation médicale humaine. Le rattrapage018 reste incomplet. La suite exige l’accès effectif aux fichiers d’images, puis leur inspection, l’annotation et le contrôle des rendus avant toute intégration. Les nouveaux diagnostics040 DX2 restent suspendus selon la priorité de Vial.

Correction META01 lors de la vérification finale : l’export des noms avait inclus les éditeurs scientifiques parmi les auteurs. Le filtre XML porte maintenant sur le groupe author ;11/6/2auteurs et éditeurs séparés. Les notices candidates avaient déjà les bons auteurs et restent inchangées sur ce point.

Contrôle Git : des espaces de fin de ligne sont présents dans deux XML et la page HTML source reçus du serveur. Les réponses originales restent conservées octet pour octet, empreintes vérifiées ; aucun avertissement ne vise le code ou la rédaction. Résultat brut par fichier/ligne dans CONTROLE_DIFF.json, sans prétendre un diff-check entièrement vert.
