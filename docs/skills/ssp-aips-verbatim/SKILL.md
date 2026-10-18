---
name: ssp-aips-verbatim
description: Vérifier des extraits de doses contre les téléchargements officiels Refdata, sans confondre conformité documentaire et validation clinique.
---
# Vérification des extraits AIPS
1. Lire CONTINUATION.md R1/R2/R13 et ssp-posologie-suisse. Compendium est exclu. Garder les documents bruts hors git ; utiliser uniquement les URL officielles Swissmedic/Refdata.
2. Télécharger les informations professionnelles liées à chaque ligne, puis lancer `python3 tools/aips_verbatim.py data/ck/doses_ch.json --cache prive/aips`. Le cache conserve les octets originaux et leurs SHA-256.
3. Relire chaque dose, voie, indication, population et limite contre le passage officiel et ses en-têtes. Le comparateur ne le fait pas : il cherche chaque ligne citée, en normalisant seulement les espaces et la police Symbol (`m` → `µ`, `³` → `≥`). Vérifier les unités dans une seconde occurrence ou le tableau officiel. Aucune conversion supposée.
4. Écrire les corrections et leur rapport, avec URL, version et date de lecture. Un mois de version ne prouve pas un jour exact de publication : signaler toute normalisation au jour 01. Ne jamais déclarer une validation par Vial ou un médecin sans preuve.
5. Relancer `python3 tools/doses_check.py`, puis le comparateur `--hors-ligne` sur le cache lu et les tests `python3 -m unittest discover -s tests -p test_aips_verbatim.py`. Construire CK et lancer les contrôles du lot.
6. Une discordance d’indication ou une unité ambiguë reste « À vérifier ». Une faute potentiellement critique suit R13 : rapport rouge et attente-vial ; la conformité verbatim ne lève pas cette attente.
