# Contre-audit technique · infobulles prototype 6

Relecture statique du patch 0033, du rendu/compilateur mono, du calculateur, de l’ordonnanceur, des workflows et du checkpoint. Tests exécutés : `test_mono_prototype.py` (9), `test_prevalence_classement.py` (7), `test_coordination_crise.py` (7) — tous passent.

## Défauts à traiter

1. **Bloquant doses — `data/ck/mono_ssp.json` échappe au checkpoint.** `tools/garde/checkpoint.py:ctrl_doses` ne parcourt que `data/ck/mono/*.json` et `data/ck/prev.json`. Les nouvelles fiches SSP peuvent pourtant contenir une posologie. Le contrôle propre au compilateur ne vérifie qu’une mention textuelle « AIPS » ; il ne lie pas la dose à `data/ck/doses_ch.json`. Une dose ajoutée dans une fiche SSP n’est donc pas couverte par le garde-fou de fusion. Ajouter ce fichier au parcours et au test du checkpoint avant d’y intégrer des doses.

2. **Blocage de recherche contournable sur un ancien ref.** Le job `perimetre` lit `tools/coordination/config.json` du ref sélectionné pour le `workflow_dispatch` (`checkout` sans `ref`). Un lancement manuel sur une branche antérieure à `mission_exclusive` obtient `autorise=true` et lance les recherches transversales. Vérifier la mission sur le ref principal autoritatif ou refuser les dispatchs hors `main`.

3. **La jauge ne montre pas la prochaine fiche SSP absente.** `calculer()` renvoie `plan.prochaines_fiches_ssp` (avec la source absente, `['G1','G2','G3']`), mais `page()` n’affiche que `prochain_lot9`, la file des DD. J’ai reproduit la sortie actuelle : 0/248 fiches structurées, mais aucun code SSP dans la liste du lot prioritaire. Ajouter cette file au HTML pour que le travail SSP soit visible.

## Vérifications sans défaut reproduit

Le chemin infobulle réessaie l’affichage après chargement de `mono-ssp.js`; la fiche DD garde le `pv` imbriqué. Le lecteur utilise bien `CK_PREV[SSP].classement`, produit par `detail()`. L’ordre G1 reste stable avant les SSP suivants, et le calculateur maintient le dénominateur des 248 SSP même quand `mono_ssp.json` manque. L’ordonnanceur refuse aussi un plan périmé dès que la configuration locale marque la mission exclusive.


Corrections du parent : garde dose étendue à mono_ssp.json ; gate de recherche lit main ; file SSP affichée ; anciennes veilles transversales suspendues pendant la mission. Tests et CI restent requis.

Dernier ordre de Vial : suppression du survol. Le patch0034 retire les ouvertures automatiques globales, les aperçus de repères au survol/focus, les titres natifs des termes et l’appui long des infobulles. Les activations clic/toucher/clavier et les gestes de déplacement du calendrier sont conservés. Les tests vérifient dorénavant que le survol reste silencieux.
