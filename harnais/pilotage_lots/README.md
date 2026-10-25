# Préparation du pilotage V0 — non déployée

Cette adaptation remplace, dans la présente branche de préparation, le prototype V8 conservé sur `infra/production-inverse-v8-20261025`. Elle ne modifie aucun workflow existant. Aucun registre distant de production et aucune tâche GPT ne sont créés. Le registre livré reste arrêté (`paused`, `stop_requested:true`, `deployment_enabled:false`).

Le mandat de pilotage vient de la demande de Vial « Prends le contrôle et pilote ton projet ». Les choix de la séance sont consignés dans `lot en cours de production/LOT_226/DECISION_SEANCE.md`, avec une transcription structurée dans `DECISION_SEANCE.json`. Seul LOT_226 est attribué. Les autres lots, branches historiques et vagues restent hors périmètre.

## Ce que le contrôleur vérifie

Le lecteur fixe un commit avant chaque série de lectures. La décision lisible, sa transcription, les preuves runtime, les HTML et les rapports sont liés par empreintes. Une attribution divergente ou une modification sans mise à jour bloque l'évaluation. Ces liens détectent des incohérences ; ils ne constituent pas une signature de Vial et ne prouvent pas la sincérité d'une attestation.

Le découpage B provient de la décision, sans nombre de fichiers fixe : les plages doivent couvrir DX.1 à DX.10 dans l'ordre, sans trou ni chevauchement. `advance` refuse toute attribution automatique. Le programme ne cherche jamais un numéro de lot libre.

La Phase A doit franchir les portes médicales, linguistiques et visuelles avant toute recommandation de rédaction B. Le gel exige l'empreinte de A, la date de validation et celle du gel, les dix noms exacts, ainsi que l'empreinte de `CORRECTIONS_AUDIT.md`. Un changement de A ou des corrections bloque la suite. Les noms affichés dans A et les titres B sont comparés à cette liste ; les dates déclarées de début de B doivent suivre le gel.

Les deux audits portent chacun sur les octets exacts du fichier, avec rapport daté et empreinté, auteur distinct, lecture complète, score >= 90, zéro critique et `final_question:"oui"`. Chaque monographie dispose aussi de sa note et de sa réponse finale ; la moyenne d'un fichier ne peut masquer une entité insuffisante. Un même auditeur peut tenir les deux grilles séparées. Pour le rôle médical, la lecture des sources critiques doit être attestée. Aucun champ JSON ne remplace la lecture effective des sources et du cours.

La QA390 requiert une preuve obtenue dans un environnement autorisé. La livraison Drive n'est examinée qu'après validation de tous les fichiers et exige un reçu HTML, l'identité de l'empreinte distante, le nombre exact d'octets et une date postérieure aux validations du lot complet. Le contrôleur ne rend aucun HTML, ne dépose rien et ne fusionne aucune PR.

## Densifier avant de condenser

La précision de Vial reçue pendant la séance impose la séquence : dossier exhaustif sans plafond intermédiaire, puis reformulation sans perte, puis vérification V0 ligne par ligne, puis fichier final de 150–200 Ko par entité. Un brouillon de plus de 200 Ko appelle `condense_preserving_data`, pas une suppression aveugle. Sous 150 Ko, le contrôleur demande de compléter le dossier exhaustif. Les critères, doses et adaptations AIPS, alertes, rangs d'exclusion, seuils et examens discriminants doivent être conservés et reliés à leurs sources.

Les deux grilles finales attestent explicitement `v0_line_by_line_complete:true` et `condensation_preserves_clinical_data:true`, avec leurs preuves dans le rapport. Le contrôleur exige ces attestations ; leur véracité et l'absence d'omission ne peuvent être établies par la seule taille ni par un script.

## Mesure du contenu propre et balisage de contrôle

Les Ko sont décimaux : 150 000 à 200 000 octets UTF-8 par SSP ou DD. Le contrôleur mesure le texte de la monographie, fenêtres et tableaux inclus, après normalisation des espaces. Il exclut les balises, attributs, commentaires, CSS, scripts et contenu partagé extérieur. Le poids total du HTML est indiqué séparément et n'a aucun plafond de 200 Ko. Le jugement sur l'utilité du texte, les répétitions, la conformité des quatorze rubriques et la sécurité reste celui des auditeurs.

Le gabarit contrôlé utilise `<details open id="ssp">` pour la monographie SSP et `id="dx1"` à `id="dx10"` pour B. Chaque entité contient ses quatorze `<section id="ssp-p1">` ou `<section id="dx1-p1">`, dans l'ordre. Les sous-fenêtres restent imbriquées. Ce balisage relie les mesures aux monographies ; une présence structurelle ne prouve pas la conformité médicale.

Chaque entrée affichée de la liste A possède un élément court de cette forme : `<strong data-dx="DX.1" data-name="Nom exact">DX.1 — Nom exact</strong>`. Le `<summary>` principal de B reprend exactement `DX.1 — Nom exact`. Le gel de `LISTE_DX_CANONIQUE.md` contient un seul bloc JSON avec `phase_a_sha256`, `frozen_at`, `corrections_sha256` et `diagnoses:[{"code":"DX.1","name":"Nom exact"}, ...]`. Aucun de ces fichiers n'est généré avant la validation réelle de A.

## Usage local et limites

Après commit des pièces à inspecter :

```bash
python3 -m unittest discover -s tests/pilotage_lots -p 'test_*.py' -v
python3 harnais/pilotage_lots/cli.py --registry-ref HEAD
```

Le CLI lit uniquement des objets Git locaux déjà présents. Il n'effectue aucun appel réseau, renouvellement de bail, lancement GPT ou écriture GitHub. Son résultat conserve `clinical_validation:false` : des portes documentaires réussies ne sont pas une certification par un médecin. La reprise du 25 octobre a obtenu une preuve individuelle canonique verte ; le refus antérieur est conservé séparément. Le contrôle refuse les preuves de plus d’une heure. Les autres lacunes restent décrites dans `LOT_226/HELP.md`.

Avant tout déploiement restent nécessaires : contre-audit indépendant du moteur et de ses transitions, harnais individuel vert, vérification des connecteurs requis, réconciliation de la décision du jour et preuves de fonctionnement de la cadence retenue. Une limite de forfait ou un refus réseau n'est jamais contourné.

## Index AIPS Medina

`aips_index.py` inventorie le ZIP annoncé par Vial sans appel réseau et permet une recherche de titre limitée, par défaut, aux informations professionnelles françaises (`SmPC`, `fr`). Il sépare les notices patient (`PIL`) des informations professionnelles, conserve les identifiants d'autorisation lus directement dans le XML et restitue les liens sans déduire de numéro depuis leur URL. Il ne prétend jamais avoir lu la fiche ou validé une dose.

```bash
python3 harnais/pilotage_lots/aips_index.py /chemin/AipsDownload_20261008.zip
python3 harnais/pilotage_lots/aips_index.py /chemin/AipsDownload_20261008.zip --query 'nom exact'
```

Le ZIP réel est conservé hors dépôt dans `/tmp/aips-medina/` ; sa source GitHub et ses empreintes sont consignées dans le lot. Les liens du 8 octobre doivent être vérifiés au moment de la rédaction. La copie Drive annoncée n'a pas été confirmée par le connecteur : la liste visible de `PROMPT_Casern` ne contenait que ses treize documents de prompts ; les archives ZIP ne figurent pas parmi les formats documentaires exposés par ce connecteur. Cette limite ne prouve pas l'absence du ZIP dans Drive.

## Corrections de la reprise du 25 octobre

`decision_ready` et `harness_ready` exposent séparément les prérequis vérifiés sur l’instantané. `may_execute` exige désormais un registre actif, le déploiement demandé, l’absence d’arrêt et ces deux prérequis pour tous les lots affectés. Un registre vide ne donne aucun feu vert. Ce champ décrit les prérequis techniques ; il ne franchit pas les portes d’audit du fichier, ne valide pas un lot et ne lance aucune action. Le registre livré reste arrêté.

La preuve runtime doit contenir les versions canoniques du watcher existant, un identifiant d’exécution et les résultats mesurés de découpage, cache et compression. Trois simples booléens `ok` ne suffisent plus. Les tests synthétiques restent distincts d’une preuve runtime réelle.

Le contrôle HTML vérifie la marque de fin portant le nom exact du fichier, refuse les identifiants de monographies étrangères, les attributs événementiels, les URL actives et les ressources CSS incorporées ou externes détectées. Il s’agit d’un contrôle de conformité complémentaire, pas d’un assainisseur HTML général ni d’un substitut à la QA390 et aux lectures indépendantes.
