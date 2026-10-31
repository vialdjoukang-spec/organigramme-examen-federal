# Hooks — garde pre-commit — retour à [00 Accueil](00_ACCUEIL.md)

Le crochet installé par `registre_ia.py installer grok` (signature du jour, couple prêt, plage de LOTS) et, si lancé, par `garde_temps_reel.py installer` reste **inchangé**. La porte zéro jeton s'y ajoute comme un contrôle de plus, jamais à sa place.

Contrôle de ce qui est indexé (zéro jeton, lecture seule) :
```
python3 grok-LOTS-html/outils/porte_zero_jeton.py precommit
```
Code 1 = au moins un fichier de leçon indexé est ROUGE : taille x, FIN_FICHIER, ids V8 (ess, som, p1–p14, sources), balises, `<script>`, fenêtres popover, mention « non validé cliniquement », critique de langue absent du modèle V8, sceau SHA, fichier hors de `grok-LOTS-html/` sur une branche `grok/…`. ORANGE (n'empêche pas le commit, s'affiche ; bloque avec `--strict`) : citations « » non retrouvées dans les preuves, alertes de langue, passe précédente non consignée dans `ROUTAGE_GROK.jsonl`, doses sans mention AIPS, source étrangère.

Avant une passe de modèle (le vrai gain) : `python3 grok-LOTS-html/outils/porte_zero_jeton.py avant <poste> <fichier.html>` ; ROUGE = ne pas lancer la passe.

Ajout au crochet existant (à faire par la session qui commite, dans son `.git/hooks/pre-commit`, après les lignes existantes ; hors dépôt versionné) :
```
python3 grok-LOTS-html/outils/porte_zero_jeton.py precommit || exit 1
```
Hooks de session déjà décrits ailleurs (non refaits ici) : `suivi_ia.py capture grok` en fin de session, veille `routage_grok.py veille`.
