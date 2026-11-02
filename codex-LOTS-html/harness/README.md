# Harnais LOTS — état vérifiable

Branche `codex/lots` ; périmètre `codex-LOTS-html/` ; ordre LOT133 → LOT18.

- [Contrôle courant](ACTIVITE.json) : date, branche, borne, erreurs, taille et SHA de chaque HTML. Un contrôle vert ne valide pas la médecine.
- [Équipe et échéance](EQUIPE.json) : quatre agents GPT-6 Astra réellement exécutés.
- [Bracelet exécuté](PREUVE_EMBOITEMENT.jsonl) : sorties exactes, code retour, horodatage.
- [Guide du cache et commandes](GUIDE.md).
- [Audit médical133](../LOT_133/audits/MEDICAL_ASTRA.md) et [conformité133](../LOT_133/audits/CONFORMITE_ASTRA.md).
- [Recherche d’images133](../LOT_133/illustrations/RAPPORT_IMAGES.md) : candidats seulement, téléchargement bloqué.

Huit tests du cache réexécutés par l’orchestrateur le02.11.2026 : tous réussis. Ils prouvent la mécanique, pas la qualité clinique. `--help` corrigé pour ne plus écrire de contrôle. Horodatage Zurich ajouté ; fichiers temporaires de contrôle distincts par PID. Le contrôle vérifie aussi l’état actif/pause du contrat.

Veille locale : `python -B codex-LOTS-html/harness/controler.py veille`, contrôle toutes60s. Après arrêt du runtime, vérifier le PID avant de retirer un verrou de veille périmé. Le verrou de production est distinct et obligatoire.

GitHub héberge ces scripts et les instantanés poussés. **Aucun runner GitHub Actions déployé** : `.github/` est hors périmètre autorisé. La présence de fichiers sur GitHub ne constitue pas une exécution distante. Une reprise horaire du contrat et un bilan le03.11.2026 à08hZurich sont programmés séparément ; leur exécution reste tributaire du service.
