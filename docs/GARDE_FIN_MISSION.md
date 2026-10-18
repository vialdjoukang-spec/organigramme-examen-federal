# Garde local de fin de mission

Outil facultatif depuis le retour au découpage original demandé par Vial. Le protocole Gardien n’est plus obligatoire. Depuis la racine du dépôt :

```bash
python3 tools/garde/fin.py verifier
```

Prérequis : Python 3.10 ou plus récent, Linux ou macOS (verrou POSIX), aucune dépendance Python supplémentaire.

Le code de sortie vaut **0** si tous les contrôles réussissent, **1** s’il reste du travail, **2** si une configuration ou un contrôle est invalide, **130** si le contrôle a été interrompu. Une interruption n’autorise jamais une clôture.

Le registre par défaut conserve les obligations ouvertes du projet. Sans état local, le script lit `tools/garde/mission-projet.json` : l’absence du registre local ne transforme donc pas le chantier en réussite. Pour créer une copie de travail, sans écraser une copie existante :

```bash
python3 tools/garde/fin.py initialiser
python3 tools/garde/fin.py verifier --json
```

La copie est `.etat_local/mission.json`. Le rapport horodaté `.etat_local/fin-mission.json` contient les preuves contrôlées, l’empreinte du registre, les obligations restantes et la prochaine tâche. Ces fichiers sont ignorés par git. Les autres automates restent inchangés.

Chaque nouvelle demande doit être ajoutée au registre par l’agent. Une tâche déjà ouverte doit y rester jusqu’à sa validation ou à une modification explicite de la mission par Vial. Le script ne lit pas la conversation à la place de l’agent. Une tâche bloquée reste ouverte ; l’agent peut travailler sur la suivante et consigne la dépendance dans la relève.

Les contrôles disponibles sont :

- `jauge` : compare les effectifs exacts de `origin/main`, avec un dénominateur strictement positif. Un pourcentage arrondi à 100 % ne suffit pas. Faire `git fetch origin` avant une clôture ; le garde reste utilisable hors réseau et n’affirme pas que la référence locale est la dernière version distante.
- `json` : exige une valeur précise dans un fichier JSON, avec son type. `1` ne vaut pas `true`. Une clé manquante ou une preuve absente bloque la clôture.
- `sha256` : exige le contenu exact d’un fichier relu, identifié par son empreinte. Une modification du fichier exige une nouvelle vérification.
- `commande` : exécute un contrôle de confiance sous forme de tableau `argv`, sans shell, depuis la racine du dépôt. Seul le code de sortie 0 valide ce contrôle. Le délai maximal est de 60 secondes ; un dépassement arrête aussi ses descendants. Les sorties conservées sont limitées à 4096 octets. Ne pas mettre de secret dans les arguments ou les sorties et ne pas choisir de commande de publication comme contrôle : cette fonction n’est pas un bac à sable.
- `a_faire` : reste toujours ouvert, avec le motif et la preuve à réunir. Un audit médical ou un accord de Vial ne peut pas être inventé par un test logiciel. Remplacer ce contrôle seulement après avoir défini et vérifié la preuve appropriée.

Pour une mission distincte, préciser `--mission chemin/mission.json`. Le schéma est le même que celui du registre du projet : `version`, `objectif`, `taches`, puis pour chaque tâche `id`, `titre`, `controles`. Le champ facultatif `numero` identifie la mission du protocole Gardien v1.0. L’affichage fournit l’état `[EN COURS]`, l’auto-audit OUI/NON et le bloc de blocage ou de fin. Tous les contrôles d’une tâche doivent réussir. Les missions vides, les champs inconnus et les identifiants dupliqués sont refusés. Le registre est une configuration de confiance : le garde ne prouve ni la qualité scientifique d’une source ni l’authenticité d’un accord humain.

Tous les contrôles sont refaits à chaque appel ; un ancien rapport n’est jamais utilisé comme preuve. Le rapport est invalidé avant le début des vérifications, écrit de manière atomique et protégé contre deux exécutions simultanées. Une modification du registre pendant le contrôle est refusée.

Ce garde peut bloquer une **déclaration de clôture dans le protocole de travail** et une commande qui vérifie son code de sortie. Il n’a aucun accès au mécanisme de fin de tour de ChatGPT : il ne peut ni maintenir cette session ouverte ni garantir une rédaction autonome après sa fermeture. Il n’installe aucun démon et n’intercepte pas les demandes d’arrêt. Une réponse d’avancement ou une relève ne constitue pas la clôture du projet. Si Vial demande d’arrêter ou change la mission, sa demande prévaut.
