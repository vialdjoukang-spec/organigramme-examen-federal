# Recherche et insertion des illustrations

La chaîne est disponible dans le périmètre Codex. Elle ne rédige pas en arrière-plan et ne prend pas la place de la veille de contrat. Exécution par le producteur qui détient déjà le verrou officiel ; les commandes contrôlent la branche, la réservation fraîche et le registre. Aucun autre producteur n’est modifié.

## Recherche web réelle

`rechercher_web.js` est un adaptateur pour **functions.exec**, qui expose le connecteur `search_service_web_run`. Ce n’est pas un programme Node : il nécessite la session Codex et son outil web. Il lit les requêtes du plan, interroge le connecteur, conserve les titres et URL dans `RESULTATS_WEB.json`, puis lance le traitement documentaire Python. Le premier plan est `LOT_019/illustrations/recherche_web/PLAN.json`. Le second argument de l’adaptateur permet de choisir le plan d’un autre lot ; la branche, la borne et le dossier sont contrôlés avant la recherche ; aucune recherche permanente n’est prétendue.

Le script Python utilise les API publiques Europe PMC pour obtenir les XML et les métadonnées des figures repérées. Il conserve URL, date et empreintes, refuse les licences NC/ND/inconnues et signale les organigrammes PRISMA. Une licence d’article admissible ne valide pas automatiquement les droits propres de chaque figure ni sa pertinence médicale. Les figures candidates restent à relire. Le script existant `acquerir_commons.py` reste disponible pour les notices Wikimedia documentées ; cette nouvelle chaîne ne prétend pas avoir un importeur Open-i.

Le sélecteur distingue le paragraphe JATS standard qui réserve explicitement la CC0 aux seuls fichiers de métadonnées de la licence du contenu de l’article. Il conserve cette distinction dans `perimetres_exclus_du_contenu`. Cette règle étroite ne permet ni d’attribuer la CC0 aux figures, ni d’accepter une double licence de portée indéterminée. Une mention CC BY sans version ou URL explicite reste en réserve. Les légendes et crédits propres des figures doivent toujours être relus.

Les trois URL de recherche REST essayées sur europepmc.org ont répondu 404 dans cet environnement. La recherche effective utilise donc le connecteur web, puis les deux API documentaires `/api/fulltextXmlRepo` et `/api/fulltextRepo`, réellement fonctionnelles. Aucun contournement de politique réseau, aucune clé inventée.

## Dossiers et étapes

Les chemins JSON internes sont relatifs à `codex-LOTS-html/`. L’argument CLI du plan est relatif au répertoire courant ou absolu. Depuis la racine du dépôt :

```sh
python3 -B codex-LOTS-html/outils/illustration/pipeline_images.py rechercher codex-LOTS-html/LOT_019/illustrations/recherche_web/PLAN.json
python3 -B codex-LOTS-html/outils/illustration/pipeline_images.py acquerir codex-LOTS-html/LOT_019/illustrations/recherche_web/PLAN_DX9.json
python3 -B codex-LOTS-html/outils/illustration/pipeline_images.py preparer codex-LOTS-html/LOT_019/illustrations/recherche_web/PLAN_DX9.json
python3 -B codex-LOTS-html/outils/illustration/pipeline_images.py integrer codex-LOTS-html/LOT_019/illustrations/recherche_web/PLAN_DX9.json
```

1. **Rechercher** : traiter les résultats web et enregistrer les figures candidates, leurs légendes originales et les preuves de droits. Pas d’intégration automatique d’un résultat de moteur.
2. **Acquérir** : après lecture de la figure et de ses crédits, remplir `SELECTION.json`. Téléchargement dans `LOT_019/illustrations/DX9-papillomatose/`, contrôle MIME, dimensions, empreinte MD5 annoncée et SHA-256 local. Les redirections sont refusées. Un domaine exclu produit un blocage explicite et un code de sortie 2, sans requête image.
3. **Préparer** : après examen visuel de l’original, créer la spécification du dessinateur/annotateur, avec contours et repères réellement placés, légende et pièges. `revue_original` contient `inspecte: true`, l’empreinte `sha256` observée et les observations réelles. Le script appelle `illustrer.py` en mode comparaison et crée un aperçu complet de la leçon sans changer la leçon publiée.
4. **Intégrer** : après inspection du rendu, `REVUE_RENDU.json` contient `sha256_apercu`, `inspecte`, `observations`, et `captures` avec `fichier` et `sha256`. Le script refuse une revue périmée, une source ou une leçon modifiée. Il conserve la sauvegarde avant insertion, ajoute les crédits à `SOURCES.json` sans effacer les précédents, puis insère la fenêtre et journalise les empreintes. Il ne commit ni ne push : contrôles de langue, de structure et revue finale restent à faire par le producteur.

La cible DX9 déjà préparée est l’expression **« lésions muqueuses »**, dans `dx9-detail9`, fenêtre issue de la section 9. Le clic ouvrira directement la comparaison, sans passer par une galerie. Aucun fichier de spécification clinique n’a été inventé tant que les images ne sont pas acquises.

Le premier candidat et sa copie annotée utilisent le même cadrage et les mêmes pixels de fond. Les pointillés sont rouges avec un halo blanc, les repères numérotés sont cliquables ; la légende reste sous les images. Sur écran étroit, les vues s’empilent avec leurs titres. Le mode historique du renderer reste disponible lorsque `comparaison` est absent.

## Preuves et limites au 01.11.2026

Trois recherches via le connecteur, 26 résultats enregistrés ; trois articles traités, six figures endoscopiques repérées, un organigramme PRISMA écarté et une source NC/ND rejetée. Les deux clichés sélectionnés restent bloqués par la politique réseau sur cdn.ncbi.nlm.nih.gov. Aucun nouveau cliché clinique intégré.

`imagerie_20261101/pipeline/DEMONSTRATION.html` montre le clic et la comparaison avec une illustration d’anatomie normale déjà présente, clairement identifiée. Ce n’est pas une nouvelle image de patient ni une leçon clinique. Tests Python : données locales et attestations simulées explicitement réservées aux tests ; navigateur : démonstration réelle, 12 interactions sur ordinateur et mobile émulé, quatre captures. Les preuves de revue visuelle sont distinctes des tests mécaniques.
