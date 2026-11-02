# Harnais local : cache, extraction et activité

Ce complément laisse `controler.py` et le harnais commun intacts. Il s'exécute ponctuellement, sans modèle, réseau, boucle, service ou nouvel automate. Il ne remplace ni le contrôle d'infrastructure initial ni un audit médical indépendant.

Depuis la racine du dépôt :

```sh
python3 -B codex-LOTS-html/harness/cache_controles.py verifier codex-LOTS-html/LOT_133
python3 -B codex-LOTS-html/harness/cache_controles.py extraire codex-LOTS-html/LOT_133/LOT_133_Phase_B_V0_DX.1.html --points 2,3,4,8,9,11,12
python3 -B codex-LOTS-html/harness/cache_controles.py activite
python3 -B -m unittest discover -s codex-LOTS-html/harness -p test_cache_controles.py -v
```

Les chemins d'exemple doivent correspondre aux fichiers disponibles. L'extraction retourne uniquement les points sélectionnés ; `--html` conserve leurs balises. Le lecteur n'a donc pas à ouvrir le HTML complet. Une sélection invalide ou sans point reconnu échoue explicitement. Pour les fichiers historiques, le découpage reprend les conventions du validateur fourni. Pour V8, l’adaptateur utilise lxml (installé dans cet environnement) et extrait les sections demandées avec leurs fenêtres liées, y compris les sous-fenêtres. Une section ou une cible manquante fait échouer l’extraction. Les fenêtres étrangères sont exclues. Le harnais commun reste intact.

## Cache strict

Les résultats mécaniques complets des LOT sont stockés dans `codex-LOTS-html/.cache/harnais/`. La clé SHA-256 comprend : chemins et contenus de tous les HTML, présence et contenu de la liste canonique, code du validateur et de ses modules Python voisins (récursivement), code de ce complément, version et exécutable Python, option `--sans-nom` et dépendances déclarées. Ajouter, supprimer ou renommer un HTML invalide donc aussi le résultat. Le cache historique du validateur, indexé seulement par version déclarée et contenu HTML, est neutralisé en mémoire ; aucun fichier partagé n'est modifié.

Le validateur actuel utilise uniquement la bibliothèque standard et lit les HTML et la liste canonique. Si un futur contrôle lit une donnée ou un module externe, le déclarer avec `--dependance chemin` (répétable). Cette déclaration fait partie du contrat d'utilisation : aucun outil ne peut deviner les dépendances externes d'un validateur arbitraire. Les fichiers déclarés absents sont aussi représentés dans l'empreinte. Une installation Python standard correspondant à sa version est supposée ; ce cache n'atteste pas l'intégrité du système d'exploitation.

Le résultat stocké porte sa propre somme de contrôle ; JSON tronqué ou résultat altéré entraîne un recalcul. Les écritures sont atomiques. Si une entrée change pendant un calcul, le résultat n'est pas enregistré et la commande échoue en demandant une relance. Un résultat non conforme est lui aussi réutilisable pour les mêmes entrées : le code de sortie reste 1. Codes : 0 = aucun critique mécanique, 1 = non-conformité (ou erreur de lecture d'activité), 2 = erreur d'exécution. `--sans-nom` ne contrôle pas la complétude du LOT et reste un diagnostic, pas une validation finale.

La bande de taille provient du validateur commun réellement chargé : actuellement 80–150 Ko. Le document historique fourni mentionne 100–200 Ko ; ce complément n'invente pas une nouvelle règle et ne modifie aucune des pièces.

## Activité par agent, lecture seule

`activite` lit les journaux JSONL disponibles directement dans `codex-LOTS-html/` et `harness/`. `--source chemin` permet de sélectionner un ou plusieurs fichiers JSON/JSONL (objet événement ou liste d'événements). Attribution par `agent`, puis `agent_id`, puis `producteur` ; sinon `non_attribue`. Chaque événement conserve son fichier source et sa ligne. Le modèle seul ne permet pas d'identifier un agent. Les erreurs de lecture ou de JSON sont exposées, jamais escamotées.

Ce rapport décrit des événements consignés. Il ne prouve ni qu'un processus tourne actuellement, ni que le modèle déclaré a été exécuté, ni des jetons ou coûts non enregistrés. Les traces historiques ne sont pas transformées en agents actifs. Aucune validation clinique ne découle du cache ou du rapport d'activité.

## GitHub et exécution

Du code hébergé sur GitHub reste du code stocké : sa présence ne démarre aucun agent ni contrôle. Ces commandes s'exécutent dans le processus Python local de l'environnement où elles sont lancées. GitHub Actions pourrait exécuter une commande dans un runner, mais aucun workflow Actions n'est installé ici : `.github/` est hors du périmètre autorisé `codex-LOTS-html/`. Ce complément n'active aucun automate existant.

## Vérification réalisée

Huit tests exécutent le vrai validateur sur un LOT synthétique complet et conforme (Phase A + 10 Phase B). Ils vérifient le résultat conforme, la réutilisation sans exécution du validateur, l'invalidation HTML/inventaire/liste canonique/code à version constante/dépendances/options, le recalcul après corruption, l'extraction ciblée et l'attribution des événements. Les fichiers temporaires sont créés puis supprimés dans `harness/`, sans réseau ni écriture ailleurs. Les données synthétiques vérifient la mécanique uniquement.

## Reprise du 02.11.2026 à 03h30 UTC

Correction de l’extraction V8 : les identifiants a-pN et dxN-pN et les fenêtres liées sont pris en charge. Neuf tests réussis, dont une fixture avec sous-fenêtre, fenêtre non demandée et partie absente. Les huit tests antérieurs du cache restent verts. La dépendance lxml concerne cette extraction, pas le validateur commun ni sa clé de cache.
