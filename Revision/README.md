# Revision — QCM Type A « Réflexe SSP » (Temps 1)

But : connaître **comme sa poche** tous les diagnostics différentiels (DD) de chaque situation/symptôme (SSP) du catalogue, avec une gradation **EX → AP → SPE**. La médecine d'abord ; l'examen fédéral CK n'en est qu'une partie.
**GitHub uniquement** — dépôt `vialdjoukang-spec/organigramme-examen-federal`, branche `grok/revision`. **Jamais Google Drive**, jamais force-push, jamais `main`, pas de PR sans ordre de Vial.

## Arborescence
```
Revision/
├─ README.md · ETAT_DES_LIEUX_QCM.md (généré) · RESUME_JOUR.md (généré)
├─ _index/       MAP_G1_G16.json (LOT, dossier, titre, liste DX)  ·  REGISTRE.csv (généré)
├─ _outils/      CHARTE_REDACTION.md · NIVEAUX.md · question.schema.json · PEDAGOGIE_… · PROFIL_…
│  ├─ templates/ _ssp_reflexe.html · _ssp_script.js · _fonts.css (Atkinson intégrée, hors ligne)
│  └─ scripts/   init_ssp.py · build_ssp.py · couverture_dd.py · etat_lieux.py · resume_jour.py · _commun.py
├─ G_symptomes_generaux/  GNN_slug/ : _bank_GNN.py → LOT_0NN_GN_TypeA_Reflexe.{json,html,pdf} · COUVERTURE_DD.md · CHANGELOG.md
├─ S_symptomes_systemes/  F_fonctions/  O_situations/   (réservés : Temps 1 après G)
```

## Conventions
- Type A fédéral : 5 options, **une seule** clé, règles IML anti-indices (voir `_outils/CHARTE_REDACTION.md`).
- Blocs R (Raisonner) · D (Discriminer) · P (Pièges & alarmes). Niveaux EX noir · AP bleu · SPE violet + spécialité + 🔥 (`_outils/NIVEAUX.md`).
- Champ `dx` : le premier `DX.n` est la **cible** ; les suivants = discrimination croisée. Règle : **≥ 2 EX cibles par DX**.
- Feedback 💡 en 4 blocs (pourquoi juste · pourquoi pas les autres · perle · source), **fermé par défaut** : un choix verrouille et marque juste/faux sans ouvrir le commentaire ; seul 💡 ou le **mode révision (avec confirmation)** l'ouvre. Aucun `<details open>` (contrôlé par le build).
- Sources : **uniquement** le LOT audité `repo/LOT_Claude_Finaux/LOT_0NN/` (ancres vérifiées). **Aucune image inventée.**
- HTML prioritaire ; JSON = contrat (source de vérité, rendu intégré) ; PDF facultatif (questions puis corrigé).
- Clés équilibrées A–E, jamais 3 identiques d'affilée, et **stables** : une question publiée garde sa lettre (progression localStorage préservée).

## Commandes (depuis `/workspace/grok/Revision`)
```bash
python3 _outils/scripts/init_ssp.py G3                                  # canevas _bank_G03.py + checklist DD + CHANGELOG (n'écrase rien)
python3 _outils/scripts/build_ssp.py G_symptomes_generaux/G03_soif_polydipsie   # contrôles + JSON + HTML (--print : _print.html ; --json : HTML depuis JSON)
python3 _outils/scripts/couverture_dd.py G3                             # COUVERTURE_DD.md ; code 1 s'il reste un gap
python3 _outils/scripts/etat_lieux.py                                   # ETAT_DES_LIEUX_QCM.md + _index/REGISTRE.csv
python3 _outils/scripts/resume_jour.py --write                          # RESUME_JOUR.md (+ appelle etat_lieux.py)
```
