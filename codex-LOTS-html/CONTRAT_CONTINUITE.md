# Contrat de continuité — 30.10.2026

Ordre de Vial : enchaîner LOT_019, LOT_020, LOT_021, LOT_022, LOT_023, LOT_024, puis tous les suivants jusqu'au dernier lot autorisé. Borne vérifiée dans IA_RESERVATIONS.json : LOT_133 inclus. Travail seul, sans sous-agents, sur codex/lots et uniquement dans codex-LOTS-html/. Aucun changement des réservations, du harnais commun ou du travail des autres producteurs.

Une reprise horaire dédiée est activée. Elle doit effectuer du travail réel, reprendre le premier lot incomplet et conserver ses sources, textes, corrections et preuves. Une programmation ou un pouls ne prouve pas une production. La veille locale contrôle chaque minute pendant la disponibilité du runtime ; elle ne maintient pas la machine allumée et ne lance pas elle-même un modèle. La reprise planifiée reste tributaire des outils et accès disponibles lors de son exécution.

Le point initial du contrat était LOT_018, commit 950a4cd1. Au checkpoint du 31.10.2026, LOT_019 (35e1d64b) et LOT_020 (eb65e0b2) sont terminés en production ; LOT_021 est terminé en production (onze leçons et 275 contrôles V8) ; la suite est LOT_022. ETAT_CONTINUITE.json et REPRISE_CODEX.md portent la suite exacte. Audit indépendant et rendu navigateur non effectués restent déclarés. L'accord de poursuite seul s'applique aux lots suivants : ne pas inventer de score, d'auditeur, de classement de fréquence ou de contrôle. Produire les 11 leçons et leurs contrôles avant de passer au suivant. Les incompatibilités historiques avec V8 sont expliquées, jamais masquées.

Effort recommandé : high en routine, effort supérieur pour une difficulté démontrée. Le réglage de la session n'est pas modifiable par un fichier : conserver dans le routage uniquement une information réellement confirmée, sans déclarer high comme déjà activé.

Commandes : `python3 codex-LOTS-html/outils/veille_contrat.py prendre` acquiert un verrou local ; `... controler` vérifie ; `... surveiller` boucle chaque minute ; `... liberer` libère. Le verrou local ne coordonne pas deux machines : une reprise sur un autre runtime doit d'abord vérifier l'absence d'un producteur encore actif, et ne pas démarrer si elle ne peut pas l'établir. Les mises à jour Git restent sans force. Un STOP/PAUSE ultérieur prime ; inscrire statut pause dans ETAT_CONTINUITE.json et ne pas reprendre tant qu'il persiste.

À chaque reprise : lire l'état frais, lire et signer le registre, démarrer la veille de routage, obtenir `pret codex` et `verifier codex LOT_XXX`, travailler, consigner les passes réelles, sauvegarder le checkpoint puis commit/push. Aucun arrêt après un seul lot par convenance : poursuivre tant que l'exécution le permet, puis laisser le prochain travail exact à la reprise planifiée. À LOT_133 terminé, désactiver uniquement l'automatisation de ce contrat.

## Avenant — ordre explicite de Vial du 31.10.2026

« Tu fais à présent 2 LOTs en parallèles ». Cette instruction remplace la consigne de travail seul pour la production simultanée de deux lots. Une session coordonnatrice conserve le verrou exclusif et les écritures globales ainsi que Git. Chaque agent travaille dans un dossier de lot distinct, autorisé au registre. La clôture et la reprise restent dans l’ordre croissant, sans saut, avec la borne 133 vérifiée. Aucun autre producteur, branche ou automate n’est modifié. Deux agents ne constituent pas automatiquement un audit indépendant.

## Consigne de reprise ultérieure — 31.10.2026

Le nouvel ordre reçu après la clôture de LOT_034/035 rétablit « seul et sans sous-agents ». La production reprend donc séquentiellement à LOT_036, sous le verrou unique de la session principale. L’avenant précédent décrit uniquement la paire achevée.

## Priorité ultérieure — illustrations annotées, 31.10.2026

Vial ordonne une pause des nouveaux diagnostics, le rattrapage des illustrations depuis le début, puis la reprise automatique après correction. `CONSIGNE_ILLUSTRATIONS.md` porte les critères détaillés et les limites vérifiées. La correction des lots018–040 est autorisée malgré leur clôture rédactionnelle antérieure. Le statut pause interdit de reprendre040 DX2 tant que ce rattrapage n'est pas vérifié ; il n'interdit pas le travail de correction demandé. La reprise après correction est déjà autorisée. Les prochaines productions doivent appliquer ces critères dès leur création. Aucun autre automate n'est modifié.

Autorisation suivante de Vial : créer nos propres scripts d'illustration et de dessin pour satisfaire le besoin. Les outils absents ne constituent plus un prérequis bloquant. Utiliser les deux scripts créés sous codex-LOTS-html/outils/, avec leurs preuves de sources et de rendu. La pause rédactionnelle reste une priorité de correction, pas une attente de permission ni de localisation d'anciens outils.

Précision suivante de Vial : lorsqu'une leçon comporte des schémas, le texte de ses fenêtres n'a aucun plafond de taille. Toutes les images, tous les clichés et tous les schémas sont placés dans les fenêtres et toujours annotés. Le plafond de9Ko reste celui de la fiche de base du DD. Les tailles des fenêtres et du fichier complet sont des mesures informatives, pas un motif de suppression des explications ou illustrations. Voir la règle prioritaire dans CONSIGNE_ILLUSTRATIONS.md.

## Priorité et dérogation de Vial — renforcement médical, 01.11.2026

Vial signale un audit médical indépendant jugeant les fenêtres trop pauvres et demande expressément deux agents Astra pour renforcer les parties1–14, avec une structure clinique approfondie et du gras/italique pertinent. Le rapport externe n’a pas été fourni : son contenu détaillé n’est pas réputé lu. Cette consigne autorise la correction médicale des leçons déjà produites et la délégation à deux agents pour cette campagne. Le responsable conserve le verrou exclusif, les fichiers globaux et Git.

La plage fraîche reste018–133. Ses moitiés arithmétiques sont018–075 et076–133 ; la seconde ne contient aucune leçon produite par Codex. Pour traiter le contenu existant immédiatement, répartition de travail annoncée à Vial :018–028 (121leçons) et029–040 (123leçons), révisable à sa réponse. Première tranche : PhaseA etDX1 des LOT018 et029, fichiers disjoints. Aucun nouveau lot n’est créé par cette répartition.

Le renforcement prime pendant cette campagne ; les illustrations existantes doivent être conservées. La dette iconographique et la pause des nouveaux diagnostics restent consignées. Les fenêtres doivent expliquer les liens entre mécanisme, signes, examens, décisions, pronostic et suivi ; une augmentation de volume seule ne prouve pas la qualité. Sources suisses puis européennes réellement lues, AIPS pour toute dose, distinctions adulte/enfant et situations particulières quand pertinentes. Les agents sont rédacteurs ; leur propre relecture ne constitue pas un nouvel audit indépendant. Le responsable revoit les changements avant publication.

### Précision prioritaire suivante de Vial — équipe obligatoire

Vial précise : renforcer les cours déjà présents, y introduire des images réelles trouvées sur internet, et construire les futurs cours d’emblée riches en notions et illustrés. Il demande de recommencer cette démarche avec le maximum d’agents nécessaires et interdit désormais le travail solitaire. Cette consigne remplace la limite de deux agents pour cette campagne. Six agents sont effectivement mobilisés : deux rédacteurs Astra, deux chercheurs/iconographes, un contrelecteur médical distinct et un contrôleur de présentation. Le responsable coordonne les fichiers, garde le verrou et publie les résultats contrôlés.

Les sources d’images peuvent être élargies au-delà des trois plateformes initiales, avec provenance, droits de réutilisation et diagnostic vérifiés. Ne pas confondre licence du code et licence des images. Une image réelle doit être acquise et inspectée ; une légende ou une capture inaccessible ne suffit pas. Les paires originale/annotée restent dans les fenêtres d’examens. Les cours futurs suivront les mêmes exigences de fond et d’illustration, sans saut de lot ni dépassement de la réservation fraîche. Les contenus existants sont repris progressivement ; aucune refonte globale ne sera déclarée achevée sur une première tranche.


## Reprise solo du 01.11.2026 — dernier ordre de Vial
Le dernier ordre demande expressément de poursuivre seul et sans sous-agents. Il remplace pour cette session les anciennes modalités de travail en équipe. La priorité au renforcement médical des cours existants et aux images annotées demeure. Reprise ciblée : LOT_018 DX3 puis LOT_029 DX3 ; préservation de la production initiale. Les nouvelles passes seront des relectures internes, sans revendication de contrelecture indépendante. Borne fraîchement relue : LOT_133 inclus.

## Ordre prioritaire de Vial du02.11.2026 — sens descendant

Commencer par le dernier lot du contrat puis revenir vers018. Borne fraîche133. Cette instruction remplace l’ordre croissant pour la suite. Travail seul maintenu ; renforcer les fenêtres avec faits structurants en gras, explications médicales concises et illustrations sourcées.133 ne contient aucun HTML : début par préparation PhaseA, sans le déclarer achevé. La reprise des nouveaux cours demandée par cet ordre est consignée ; la dette des illustrations antérieures reste ouverte.
