# Journal · Nerfs crâniens et partie CK (plan du 17.10.2026)

Chaque agent ajoute ses entrées datées (Europe/Zurich) : ce qui est fait, sources lues, « À vérifier », prochaine action.

## Atlas et Janus · NC-0 socle et contrôles · 17.10.2026, Europe/Zurich

### Décisions
- 14:00 · Atlas et Janus livrent ensemble sur une seule branche, feat/ck-socle (au lieu de feat/ck-socle + qa/ck-controles), pour que les contrôles et le socle qu’ils vérifient entrent dans main en même temps.
- 14:05 · Lyncée reste déterministe en CI : aucune liste externe n’est téléchargée. Le MeSH bilingue (CC BY-NC) et Lexique 3.83 (CC BY-SA) deviennent des aides au tri local. Motif : lexique.org a renvoyé HTTP 200 sans corps, puis 503, depuis le box le 17.10.2026 ; un gate dépendant d’un site lent rendrait la CI instable.
- 14:09 · La liste des formes conjuguées de G6 (tools/audit/verbes_conjugues.txt.gz, 83 502 formes) vient d’un conjugueur interne appliqué à 1 681 lemmes VERB/AUX relevés par spaCy fr_core_news_sm dans TIP, NOT et GES, plus une table d’irréguliers. tools/audit/verbes_gen.py bascule sur Lexique 3.83 dès que .cache/lexique/Lexique383.tsv existe.
- 14:10 · Dans syn.json, les hypothèses d’orientation s’appellent `hyp` (identifiants de hyp.json) au lieu de `orientation`, pour ne pas mélanger un champ de texte (glo.orientation) et une liste d’identifiants. Le schéma sig = entrée de glo de type « signe » avec `recherche` obligatoire.
- 14:11 · Les définitions du glossaire se publient par tranches (glo-<première lettre>.js) ; l’index glo-index.js porte [id, type, libellé, formes, tranche] pour le lieur d’Hermès.
- 14:13 · Référence de Lyncée créée : 3 868 candidats, 19 exclusions motivées (mots de la langue générale), 3 849 termes non définis. Elle ne peut que baisser (contrôle --diff contre la branche de base).
- 14:13 · Référence des doses héritées (TIP, NOT, GES) : 297 clés, 473 mentions ; une dose nouvelle dans ce contenu exige une source suisse ou la mention « À vérifier » dans le même texte.
- 14:15 · G7 porte sur les données CK et sur les règles CSS `.ck-…` seulement, pour ne pas bloquer la refonte d’Apollon sur le reste de l’application.
- 14:16 · Décision de Vial du 17.10.2026 appliquée mécaniquement : une faute critique de qa/audit/fautes.jsonl sans `accord_vial` daté fait échouer la CI (rapport_fautes.py --check).
- 14:17 · Décision de Vial du 17.10.2026 appliquée : une vue dérivée de assets/nc exige `licence_derivee` CC BY-SA dans credits.json (nc_svg_check.py).

### Sources lues
- Plan Nerfs crâniens et CK, sections 3, 4, 8 et 9, et propositions/audit-medical.yml, propositions/domaines.yml (local, 17.10.2026).
- MDN, requestIdleCallback et HTMLScriptElement (comportement de <script src> en file://), connus et vérifiés par test Playwright le 17.10.2026.

### À vérifier
- Lexique 3.83 : régénérer la liste G6 à partir de Lexique dès que lexique.org livre le fichier (Janus).
- MeSH bilingue de l’Inserm : brancher le filtre de tri en cache local (Janus, avec Hippocrate).
- Domaines escardio.org, has-sante.fr et escmid.org : confirmation manuelle (Argos).

- 14:45 · Fusion de main (PR #18 et #19) : Hermès a pris le numéro 0010 (bandes du calendrier) ; le patch d’Atlas devient 0011, rejoué sur l’app_v2.html de main (ssp-fusion-patch). tests/test_audit.py devient tests/test_ck.py (Janus : données, schémas, contrôles) ; Hermès garde tests/test_ck_ui.py.
- 14:46 · Les cinq skills du chantier et ssp-images-licence amendé sont copiés dans skills/.

### Prochaine action
- Hippocrate : premier lot de 50 entrées dans data/ck/glo.json ; `python3 tools/lyncee.py --json .cache/lyncee.json` donne les candidats par fréquence ; `--update` resserre la référence.
- Hermès : brancher tipFor (glo|id, syn|id, hyp|id, nc|id|vue, loc|module|A ou B) sur ckLoad() et ckGlo(), et gloLink() sur window.CK_GLO_INDEX.
- Galien : remplir data/ck/doses_ch.json et qa/audit/fautes.jsonl ; la revue de niveau 2 part de l’artefact audit-flags et de l’étiquette audit:galien.
