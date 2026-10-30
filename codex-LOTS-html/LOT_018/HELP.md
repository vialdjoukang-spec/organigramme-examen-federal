# Points de suivi — LOT_018

État du 30.10.2026 : onze leçons produites, relecture interne terminée et contrôles statiques V8 réussis. Voir `VALIDATION.md` et `ACCORD_POURSUITE.md`. La production ne reste plus en attente du gel de la liste.

## H1 — Ordre des diagnostics : décision éditoriale documentée

La liste est stabilisée dans `LISTE_DX_CANONIQUE.md`, identique aux dix titres et à la Phase A. Les sources ne démontrent pas une hiérarchie de fréquence commune aux urgences et aux consultations lentes. Les numéros sont donc explicitement pédagogiques ; les priorités d’urgence restent distinctes. Aucun rang de prévalence n’a été inventé.

## H2 — Indépendance de la relecture : limite déclarée

Vial demande un travail seul et a autorisé la poursuite après le signalement du point d’arrêt. Les onze leçons ont été produites, relues et contrôlées dans la session principale. Les rôles `relecture-interne`, `controle-v8` et `transversale-interne` portent `independant: false`. Les rôles d’auditeur externe restent différés et non exécutés ; ils ne sont pas utilisés pour simuler un audit. Aucun score médical indépendant n’est attribué.

## H3 — Contrôleur historique et V8 : divergence expliquée

Les rapports officiels négatifs sont conservés. Leurs critères historiques (`title`, `[S1]`, `h3`, bande d’octets) diffèrent du format V8 demandé dans la section 12 du prompt maître. Le rapport complémentaire `audits/validation_v8.json` vérifie les critères statiques V8 sans modifier le harnais. Le détail des écarts et des avertissements est dans `VALIDATION.md`. Cela ne vaut pas correction du harnais commun.

## H4 — Rendu visuel : non vérifié

Le téléchargement du navigateur Playwright a reçu HTTP 403 (« Domain forbidden »). Chromium présent sur la machine a refusé l’ouverture locale avec `net::ERR_BLOCKED_BY_ADMINISTRATOR`. Aucune restriction n’a été contournée. Lecture mobile, clavier, contraste, défilement et maintien de la fenêtre parente après fermeture d’une sous-fenêtre restent à constater dans un navigateur autorisé. Aucune capture ni validation mobile n’est revendiquée.

## H5 — Glucocorticoïdes dans l’ACG : distinction précisée

DX.10 et la Phase A distinguent désormais l’indication ACG de Prednisone Streuli (29349), sa plage AIPS générale, la dose d’induction EULAR 40–60 mg/j et les bolus sélectionnés de méthylprednisolone proposés par EULAR. Le bénéfice visuel de ces derniers est indiqué comme incertain. Ils ne sont pas attribués à une posologie ACG explicite de Solu-MEDROL (35112). Les citations d’administration, de contre-indications et de grossesse/allaitement sont conservées mot pour mot ; un usage hors information professionnelle doit être identifié par l’équipe qui prescrit.

Les traitements de fond non détaillés et les données suisses introuvables restent signalés comme tels dans les leçons. La clôture de rédaction ne signifie pas couverture de toutes les spécialités possibles ni validation clinique par un médecin.
