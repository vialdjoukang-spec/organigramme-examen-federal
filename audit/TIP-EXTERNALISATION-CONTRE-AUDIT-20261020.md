# Contre-audit indépendant de l'externalisation TIP

**Verdict : favorable documentaire et technique après correctifs ; CI et publication exactes encore requises.** Auteur initial : `/root/budget_script`, commit `fd5845ac1485209f1719851d6410239792c26f02`. Contre-auditeur distinct : `/root/audit_tip_asset`, GPT-6 Astra. Base examinée : `8aa1296`. Aucune validation médicale humaine déduite.

## Identité des données

Les 248 objets TIP, leurs 3 472 parties et leur ordre sont identiques à la base. Le littéral JSON de l'asset est identique octet pour octet à l'ancien littéral inline. La transformation inverse reconstitue exactement l'HTML initial. Le patch de migration a été exécuté puis rejoué en répertoire temporaire : résultats identiques et seconde exécution idempotente. Le reste de l'HTML, dont les autres constantes, est intégralement préservé.

Comparaisons indépendantes avant/après : 289 entrées de doses héritées identiques ; 18 484 chaînes TIP/NOT/GES du corpus Lyncée identiques ; 404 liens identiques ; 1 443 éléments d'inventaire « À vérifier » identiques après normalisation du seul emplacement TIP. Les empreintes intégrales sont dans le rapport JSON. Elles concernent cette migration initiale et ne sont pas imposées aux futurs lots.

App : 5 907 998 → 440 518 octets ; budget inchangé de 6 000 000. Asset TIP : 5 467 526 octets ; limite indépendante de 12 582 912. Aucun contenu clinique n'a été retiré pour réduire le poids de l'HTML.

## Défauts corrigés

1. **Preuve de publication trop permissive.** Le planificateur acceptait le tag présent sans vérifier qu'il serait réellement exécuté avant le consommateur. Le test positif initial ne comportait pas de véritable script principal. Le lecteur et le planificateur partagent maintenant une vérification des vrais scripts HTML. Les fixtures refusent tag tardif, commenté, asynchrone, redéclaration TIP, asset illisible et shard divergent, même quand les preuves HTTP et SHA correspondent exactement aux fichiers corrompus. Les erreurs de parsing refusent la preuve sans arrêter le planificateur.
2. **Structure quatorze parties insuffisamment typée.** Une chaîne de longueur quatorze pouvait passer le contrôle de longueur. Les shards et drafts exigent une liste de quatorze textes ; le refus d'injection intervient avant l'écriture et laisse asset/shards inchangés.
3. **Petit lecteur oublié.** `tools/audit_examen/analyse.py` lisait les brouillons extraits TIP/GES et écrivait dans un ancien chemin hors dépôt. Il lit désormais les données canoniques et produit `.cache/audit_examen/stats.json`. Exécution vérifiée : 22 régions, aucune partie d'examen vide.

Les scripts historiques de correction Galien/Asclépios qui éditent explicitement `data/TIP.json` demeurent des auteurs de brouillons dans le flux extract/inject ; ils ne sont pas traités comme des lecteurs de publication.

## Vérifications

150 contrôles réussis : TIP 7 ; mandat 22 ; fonctions 4 ; cours 13 ; injection 6 ; gardes 5 ; liens 7 ; migration Lyncée 4 ; socle CK/audit 82. G1, G3, Lyncée, compilation monographies, budgets, empreinte de l'original, contrôleur des cours et planificateur ont également réussi. Référence Lyncée inchangée, zéro terme nouveau ; contrôleur à 26 SSP/364 parties relus, zéro anomalie. Aucun garde existant n'a été assoupli.

Un ancien lot à quatorze empreintes appliqué aux fixtures inline et externalisée produit le même objet TIP final, DD et fondamentaux compris. L'injection refuse un conflit sur le même SSP et conserve deux modifications sur des SSP distincts. Les scripts classiques complets compilent avec Node 24 sans collision lexicale ; l'exécution isolée de l'asset suivie d'un consommateur lexical lit bien 248 SSP/3 472 parties.

Le workflow Pages copie récursivement `assets` dans `_site/assets` ; le déclencheur `assets/**` couvre TIP. La preuve demande HTTP/empreintes pour `app_v2.html` et `assets/config/tip.js`. Le shard est lu depuis Git au commit intégré et comparé au payload, sans exiger une URL de `data/tip` non déployée.

## Limites et suite requise

Aucun Chromium local exécuté. La compilation Node ne valide pas l'interface : parcours file://, bureau/mobile et visuel restent dus sur la CI de la tête exacte. Aucune fusion, aucun push ni publication HTTP réalisés par le contre-auditeur. Le mécanisme d'empreinte des drafts ne verrouille pas deux écritures simultanées dans le même worktree ; les agents doivent conserver leurs worktrees séparés et intégrer les lots séquentiellement. Aucun contenu médical ni réservation modifié.

## Automates actifs

Inventaire `checkpoint.py --inventaire` consulté : CI, visuel, Pages et dispositifs de garde existants. Aucun automate activé, désactivé ou modifié dans les correctifs de contre-audit. La fusion protégée et le contrôle de publication demeurent à la charge du responsable après CI verte.
