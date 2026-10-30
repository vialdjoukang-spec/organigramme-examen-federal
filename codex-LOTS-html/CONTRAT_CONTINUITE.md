# Contrat de continuité — 30.10.2026

Ordre de Vial : enchaîner LOT_019, LOT_020, LOT_021, LOT_022, LOT_023, LOT_024, puis tous les suivants jusqu'au dernier lot autorisé. Borne vérifiée dans IA_RESERVATIONS.json : LOT_133 inclus. Travail seul, sans sous-agents, sur codex/lots et uniquement dans codex-LOTS-html/. Aucun changement des réservations, du harnais commun ou du travail des autres producteurs.

Une reprise horaire dédiée est activée. Elle doit effectuer du travail réel, reprendre le premier lot incomplet et conserver ses sources, textes, corrections et preuves. Une programmation ou un pouls ne prouve pas une production. La veille locale contrôle chaque minute pendant la disponibilité du runtime ; elle ne maintient pas la machine allumée et ne lance pas elle-même un modèle. La reprise planifiée reste tributaire des outils et accès disponibles lors de son exécution.

Le dernier lot terminé en production est LOT_018, commit 950a4cd1 ; audit indépendant et rendu navigateur non effectués restent déclarés. L'accord de poursuite seul s'applique aux lots suivants : ne pas inventer de score, d'auditeur, de classement de fréquence ou de contrôle. Produire les 11 leçons et leurs contrôles avant de passer au suivant. Les incompatibilités historiques avec V8 sont expliquées, jamais masquées.

Effort recommandé : high en routine, effort supérieur pour une difficulté démontrée. Le réglage de la session n'est pas modifiable par un fichier : conserver dans le routage uniquement une information réellement confirmée, sans déclarer high comme déjà activé.

Commandes : `python3 codex-LOTS-html/outils/veille_contrat.py prendre` acquiert un verrou local ; `... controler` vérifie ; `... surveiller` boucle chaque minute ; `... liberer` libère. Le verrou local ne coordonne pas deux machines : une reprise sur un autre runtime doit d'abord vérifier l'absence d'un producteur encore actif, et ne pas démarrer si elle ne peut pas l'établir. Les mises à jour Git restent sans force. Un STOP/PAUSE ultérieur prime ; inscrire statut pause dans ETAT_CONTINUITE.json et ne pas reprendre tant qu'il persiste.

À chaque reprise : lire l'état frais, lire et signer le registre, démarrer la veille de routage, obtenir `pret codex` et `verifier codex LOT_XXX`, travailler, consigner les passes réelles, sauvegarder le checkpoint puis commit/push. Aucun arrêt après un seul lot par convenance : poursuivre tant que l'exécution le permet, puis laisser le prochain travail exact à la reprise planifiée. À LOT_133 terminé, désactiver uniquement l'automatisation de ce contrat.
