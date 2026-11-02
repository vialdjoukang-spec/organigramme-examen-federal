# Revue ciblée du contrôleur — 02.11.2026

Revue du fichier `controler.py` après ajout de l'aide, du contrôle de pause, du temporaire par PID et de l'heure Europe/Zurich. Aucun script modifié ; aucune veille lancée, arrêtée ou relancée. La session de veille annoncée par le responsable n'a pas été sollicitée.

| Contrôle | Résultat observé |
|---|---|
| Exécution réelle `python3 -B codex-LOTS-html/harness/controler.py --help` | Code 0 ; aide affichée avant tout appel à `controle()` |
| `ACTIVITE.json` avant/après l'aide | SHA-256 identique `49b7e2b236e30ce6a951841dbfd4326fdc68cf949ed97e8c78b18ab790ea0ca3`, 43 418 octets, mtime_ns identique `1793583494816821780` |
| État `actif`, dépendances simulées conformes | `pret_infrastructure=true`, aucune erreur |
| État `pause`, mêmes dépendances | `pret_infrastructure=false`, erreur `contrat-pause` |
| Horodatages produits en mémoire | UTC `2026-11-02T01:38:16.430549+00:00` ; Zurich `2026-11-02T02:38:16.430570+01:00` |
| Temporaire | `ACTIVITE.<PID>.tmp` puis remplacement : évite la collision de nom entre processus différents |

Les essais d'état ont exécuté le véritable corps de `controle()` en mémoire, avec lectures, Git et écritures remplacés par des doubles de test. Aucun état de production n'a été modifié. Ils ne constituent pas une réexécution complète du contrôle d'infrastructure réel.

## Défaut confirmé — priorité moyenne

`controler.py:16` : une lecture d'`ETAT_CONTINUITE.json` invalide ou momentanément tronqué déclenche une exception non interceptée. Reproduction en mémoire avec le contenu `{` : `JSONDecodeError`, aucune écriture d'activité. Dans la boucle `veille` (lignes 42–43), cette exception termine le processus et libère le verrou. Le dernier `ACTIVITE.json` reste disponible, éventuellement avec `pret_infrastructure=true`, sans nouvel événement expliquant l'arrêt.

Correction conseillée au responsable : intercepter les erreurs de lecture/JSON attendues, publier un résultat non prêt avec leur cause et conserver le rythme de contrôle pour une erreur transitoire. Les consommateurs doivent aussi contrôler la fraîcheur du dernier instantané. Ce défaut n'a pas été provoqué sur la veille réelle.

Aucun autre défaut démontré dans les quatre changements ciblés. Les deux horodatages diffèrent de quelques microsecondes parce qu'ils sont calculés séparément ; leur fuseau est correct. Le verrou de production est seulement signalé, ce qui correspond au champ `verrou_present` et ne prouve pas une activité de production.

## Contre-vérification après correction du responsable

**Défaut ci-dessus corrigé et vérifié.** Empreinte SHA-256 du script revu : `0be1bbca12640a814c62ba97387fe5407c5badec81210bb8fb9774066340dc0e`.

La nouvelle fonction `controle_surveille()` appelle le contrôle, intercepte son exception et publie un instantané non prêt. Le point d'entrée CLI et la boucle de veille passent désormais par cette fonction.

Reproduction avec le vrai corps de contrôle et un état JSON `{` simulé en mémoire : `JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)` capturée. L'écriture réelle dans un dossier temporaire sous `harness/` a produit `ACTIVITE.json` avec `pret_infrastructure=false`, identique au résultat retourné, puis remplacement atomique sans temporaire résiduel. Un appel suivant a pu retourner un contrôle réussi simulé ; l'exception initiale ne termine donc plus la fonction appelée par la boucle. Dossier de test supprimé après vérification, état et activité de production intacts.

La lecture du code confirme la poursuite de boucle ; aucune nouvelle veille ni attente de 60 secondes n'a été exécutée pour ce test. Le responsable redémarre séparément sa veille sur cette version. Aucun défaut restant démontré dans les changements ciblés.
