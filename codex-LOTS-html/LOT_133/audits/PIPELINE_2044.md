# Correctif technique du pipeline — 02.11.2026

Périmètre : copie Codex de `illustrer.py`, `pipeline_images.py` et leurs tests existants. Aucun formateur, HTML de leçon, fichier commun ou état Git modifié par ce travail.

`illustrer.validate` accepte explicitement les hôtes HTTPS `medicaljournalssweden.se` (éditeur original) et `github.com` (page de provenance du dépôt original), en plus des hôtes existants. Aucune autorisation générique de domaines ou de sous-domaines ; `raw.githubusercontent.com` reste exclu de cette liste de pages de provenance. Les règles de licence ne changent pas : licence explicite admissible et URL Creative Commons cohérente ; NC, ND et licence inconnue refusées. L'autorisation d'un hôte ne constitue pas une preuve des droits propres d'une figure.

Le crédit ajouté à `images_et_schemas` conserve désormais l'`ancre` exacte du travail d'intégration et la cite dans `modifications`, sans attribuer systématiquement l'image à la section 9. Le contrôle d'accessibilité depuis la section 9 et ses fenêtres liées reste inchangé ; aucune extension à la partie 8 ni lien artificiel n'a été ajouté.

Validation exécutée : `python3 -B -m unittest discover -s codex-LOTS-html/outils/illustration -p 'test_*.py'` — 55 tests réussis. Couverture ajoutée : acceptation de CC BY sur les deux hôtes, refus NC/ND/inconnue, incohérence d'URL de licence, HTTPS et hôtes exacts, conservation de l'ancre dans les crédits sans numéro de partie inventé.

Ces tests utilisent des données locales et, pour l'intégration, des attestations explicitement simulées. Ils ne constituent ni une revue clinique, ni une inspection réelle des clichés candidats, ni une validation humaine. Acquisition, inspection des originaux, droits propres aux images, revue du rendu et intégration réelle relèvent du producteur principal et de leurs preuves distinctes.
