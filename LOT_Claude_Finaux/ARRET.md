# ARRET — 26.10.2026 (Europe/Zurich)

**Cause exacte.** Le corpus AIPS local (`AipsDownload_20261008.xml`, extrait de l'archive) ne contient que métadonnées et URL (n° d'autorisation, titulaire, liens `files.refdata.ch/…html|pdf`), pas le texte des informations professionnelles. Le texte n'est lisible que via `files.refdata.ch` / swissmedicinfo.ch : le proxy de l'environnement répond **403** (`CONNECT tunnel failed`), WebFetch échoue en DNS. Aucune dose ne peut donc être relue dans une source AIPS datée (Prompt V0 §13.2 : aucun dépôt dans ce cas).

**Dernier état.** LOT_001 : Phase A V0 rédigée (171 635 o, 14 points, liste DX canonique reprise mot pour mot), non auditée ; brouillon et `HELP.md` Q1–Q4 dans `lot en cours de production/LOT_001/`. Phase B (10 DD) non démarrée. Aucun dépôt dans `LOT_Claude_Finaux/LOT_XXX/`. Correction d'audit n°3 (Axhidrox, grossesse, n° 69243) non résolue.

**Prochaine action (Vial).** Autoriser dans les paramètres réseau de l'environnement cloud (menu de l'environnement → Edit → Network access) l'hôte `files.refdata.ch` (et `www.swissmedicinfo.ch`), ou fournir le texte AIPS en local. Puis relancer : audit médico-linguistique de la Phase A de LOT_001, gel de `LISTE_DX_CANONIQUE.md` (avec lignes `DX.<i> — <nom>` pour `controle_lot.py`), 10 fichiers Phase B.
