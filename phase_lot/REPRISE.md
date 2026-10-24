> **Consigne humaine prioritaire, mise à jour le 24.10.2026 :** Thunder est l’utilisateur humain (compte GitHub vialdjoukang-spec), et non une IA Grok. ChatGPT rédige A et B. Rien n’est transmis, déposé ou publié sans sa validation humaine explicite du livrable concerné. Les rédactions restent locales jusque-là. LOT_Tunder, sur main, sert à la réception pour relecture après fusion effective de la PR272 et autorisation de transmission. LOT_Finaux_Audités reste réservé aux cours acceptés. Aucun agent ne fabrique une approbation humaine ni ne l’infère d’un commit sur le compte partagé. Les anciennes mentions d’un compte externe/IA ou d’une publication automatique ci-dessous sont remplacées par cette consigne.

# Reprise — Phase LOT

Le mandat actif est celui du 24 octobre 2026 : produire des cours HTML autonomes sur les LOTS 1 à 10, un LOT à la fois, audit humain Thunder. La priorité historique de l'application sur main n'est pas le chantier présent.

1. Lire AGENTS.md dans ce dossier et instructions/MANDAT.md.
2. Lire config/file.json. Lire le LOT marqué ACTIF : LOT2 commence sa recherche A high ; LOT1 est produit localement, non transmis et non audité. B attend A entièrement terminé.
3. Consulter preuves/agents.json et la branche lot/001/a avant de relancer : ne pas dupliquer un auteur actif. L'agent interactif n'est pas présumé vivant après fermeture du chat.
4. Récupérer le dernier checkpoint GitHub ; les chemins locaux d'une ancienne session ne sont pas garantis persistants. Recréer les worktrees si nécessaire.
5. Ne pas réécrire le prompt ni le plan PDF au lieu de produire. Continuer le prochain point clinique avec les sources primaires lues.
6. Thunder est identifié : utilisateur humain sur vialdjoukang-spec, droits admin vérifiés. Aucun audit autodécerné. Ne rien supprimer.

Le plan PDF est versionné à la racine de ce dossier. La tâche horaire « Poursuivre les LOTS PROFILES » a été créée et activée. L'enregistrement ne fournit pas encore de prochain passage ; un passage est enregistré à 00:28 UTC et le prompt a été reçu dans la session active. Le résultat détaillé et la reprise après inactivité restent à prouver. Le fichier de sonde GitHub 30 minutes est un code fourni, pas un workflow activé sur main.


## Reprise des accès

Le 24.10.2026 vers 00:29 UTC, Git/gh a renvoyé HTTP 401. Le connecteur MCP GitHub reste fonctionnel. Dans ce cas, ne pas contourner l’authentification : utiliser `github_fetch_file` pour lire `lot-pilotage/etat:phase_lot_lease.json`, vérifier propriétaire et expiration, puis `github_update_file` avec le SHA du blob lu. Un SHA périmé ou un bail concurrent actif interdit la reprise ; relire et ne jamais écraser aveuglément. Le renouvellement courant a réussi par ce chemin MCP.

Les derniers cours complets sont locaux et peuvent être plus récents que le checkpoint clinique déjà présent sur GitHub. L’absence d’un fichier distant ne signifie pas que sa rédaction n’a jamais eu lieu. Vérifier les chemins et empreintes du dernier état technique ; si les fichiers locaux sont indisponibles, signaler cette limite et ne pas annoncer une reprise depuis un candidat distant inexistant.


## État figé du LOT1 et poursuite du LOT2

LOT1 : candidat complet local dans `/workspace/work/LOT_001_CANDIDAT_RELECTURE_20261024T0041Z`, archive voisine `.zip`. L’empreinte exacte et les sept HTML sont consignés dans `preuves/candidat_LOT001.json` ; aucun fichier clinique nouveau n’a été poussé. Ne pas régénérer le candidat figé à partir des anciens constructeurs : les révisions finales ont été intégrées séparément et leurs octets sont conservés. Les six branches auteurs et la branche candidat sont enregistrées localement ; elles ne sont pas autorisées à être poussées. La validation humaine de transmission est en attente, distincte de l’audit médical final.

LOT2 : `/root/lot002_appel_a` a été lancé en GPT-6.1 Sol high, dossier privé `/workspace/work/lot002-a`, branche locale `lot/002/a`. Vérifier son état réel et `research_checkpoint.json` avant toute relance ; ne pas créer un auteur concurrent écrivant au même chemin. La recherche terminée sera reprise par une invocation medium séparée, puis A devra avoir livré tout son HTML avant B1 à B5. L’absence de checkpoint au tout début du travail ne prouve pas que l’agent est inactif. Si sa présence ne peut pas être vérifiée, ne pas écraser son dossier.
