# Reprise — pause ordonnée par Vial le 28.10.2026 à ~23:05 UTC

État : tout est arrêté (circuits, agents, détective, veille). Rien n'est promu vers `LOT_Claude_Finaux` (porte non verte, Opus suspendus).
- essai_lot001 : 16/16 leçons rédigées (Flash, fragmentées, sans professeur Opus).
- essai_lot002 : 9/16 ; essai_lot003 : 0/14 ; essai_lot004 : 0/12 (relance reprend les non finies).
- Ordres en vigueur : fiches 100–200 Ko (cible 150, bande 100–298 bloquant au-delà) ; professeurs/auditeurs Opus SUSPENDUS jusqu'après le LOT 248 (fichier `.cache/brain/sans_professeur`) ; assembleur Sonnet 5.5 à la sortie ; capacité Sonnet `.cache/brain/sonnet_max` (48).
- Fichier AIPS à remettre dans `.cache/aips/AipsDownload_20261008.xml` si le conteneur est neuf (reçu de Vial par envoi direct ; zip dans son Drive).
- Relancer : `bash harnais/brain/relance_tout.sh` (idempotent) ; état : `python3 harnais/brain/radar.py` ; suivi : `python3 harnais/brain/suivi_html.py`.
- À faire ensuite : captures + tableau des fautes restantes du LOT_001 pour Vial ; promotion vers `LOT_Claude_Finaux` uniquement si porte et pré-commit passent.
- Le conteneur redémarre souvent : les leçons finies sont enregistrées (`journal/*.fait.json`), rien n'est perdu.

## Fichier à garder jalousement
`harnais/etat/LOTS_248_DD.md` : les 248 LOT (SSP du catalogue PROFILES 2023), statut FAIT/NON FAIT et listes de DD (LOT 001–022). Reçu de Vial le 28.10.2026.
