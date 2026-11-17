# PROMPT PROJET · INTERNAT, le jeu de révision médicale

**Administrateur : Grok Bot. Production : Eta_Bot et les agents qu'il désigne. Dépôt : `jeu-revision/` sur `main` de `vialdjoukang-spec/organigramme-examen-federal`.**

## Question unique
Pose-toi une seule question à chaque carte, chaque cas et chaque écran : **à la fin de cette leçon, l'interne renforce-t-il ses sciences fondamentales, sa clinique, sa démarche diagnostique, sa finesse, son exploration ciblée, son diagnostic, sa prise en charge et les diagnostics différentiels à évoquer ABSOLUMENT ?** Si la réponse est non, refais le travail.

## Mission
Étends le prototype « Urgences cardio » à toutes les spécialités, aux disciplines transversales, aux disciplines paracliniques et aux sciences fondamentales utiles à l'examen fédéral (PROFILES) et à la pratique courante en Suisse. Donne à chaque spécialité un **mode Urgence** et un **mode Consultation non urgente**.

## Contenu exigé pour chaque pathologie
1. **Fondamentaux** : rappelle l'anatomie, la physiologie et la physiopathologie qui expliquent les signes.
2. **Démarche diagnostique** : enseigne la méthode (anamnèse ciblée, examen ciblé, drapeaux rouges, probabilité avant test).
3. **Diagnostics différentiels** : liste ceux à évoquer ABSOLUMENT, en commençant par ceux qui tuent, et donne le signe qui discrimine chacun.
4. **Exploration ciblée** : justifie chaque examen par la question qu'il tranche ; signale les examens inutiles (Smarter Medicine Suisse).
5. **Diagnostic** : donne les critères retenus et leur source.
6. **Prise en charge** : va des mesures générales aux mesures spécifiques. Personnalise la prescription au tableau clinique, sans abus de bilan ni de traitement.
7. **Suivi et critères d'orientation** : précise quand hospitaliser, adresser ou revoir.
8. **Explication clarissime** : explique chaque bon coup et chaque erreur en 1 à 3 phrases verbales, puis ouvre la fiche.

## Sources
- Clinique, diagnostic, traitement et protocoles : appuie-toi seulement sur les sociétés savantes suisses, les facultés et hôpitaux universitaires suisses (CHUV, HUG, Insel, USZ, USB, Fribourg, Neuchâtel), smartermedicine.ch et l'OFSP. Traduis au besoin. Signale tout hôpital cantonal comme source complémentaire.
- Sciences fondamentales et pharmacologie : utilise des références internationales en accès libre.
- Doses : n'affiche une dose qu'après citation mot pour mot de l'information professionnelle suisse (swissmedicinfo), avec sa date.
- Marque « À vérifier » toute affirmation sans source lue et datée. N'invente rien.
- **INTERDIT : n'ouvre aucun cours ni aucun LOT produit du dépôt** (`data/tip/`, `data/ck/`, `LOT_*`, `grok-LOTS-html`, etc.). Construis tout le contenu clinique depuis les sociétés savantes, universités et facultés de médecine suisses.

## Règles du jeu (à implémenter et afficher dans un écran « Règles »)
- Chaque cas compte 3 à 5 duels dans l'ordre clinique : trier, explorer, différencier, diagnostiquer, traiter.
- Le patient a des PV : une erreur dangereuse coûte 30 PV, une erreur mineure 10 PV, un examen inutile 5 PV et 1 minute de temps patient.
- Le joueur gagne des étoiles (1 à 3) selon les PV restants, le nombre d'examens inutiles et le temps en mode Urgence.
- Le mode Urgence impose un chronomètre ; le mode Consultation ne l'impose pas mais pénalise l'excès d'examens.
- La rareté d'une carte suit le poids de l'objectif à l'examen PROFILES, et non une impression.
- Le joueur débloque une spécialité après 2 étoiles de moyenne sur la précédente ou par choix libre en mode Entraînement.
- Le journal signale tout système sous 70 % de bons réflexes et propose une révision ciblée (cartes ratées d'abord, répétition espacée).
- Un mode Fondamentaux pose des duels courts (mécanisme ↔ signe, structure ↔ fonction).

## Ambiance
- Garde le design sobre, clinique et lisible ; rends-le original et attrayant par le mouvement et le son, pas par le décor.
- Ajoute des effets légers : retournement de carte, flash vert ou rouge, barre de PV animée, étoiles finales.
- Synthétise les sons avec la Web Audio API (aucun fichier, aucune licence) : bip de moniteur, validation, alerte, victoire. Fournis un bouton muet, mémorisé, et respecte le mouvement réduit.

## Technique
- Garde le HTML, CSS et JS purs, sans build, ouverts par double-clic.
- Mets un fichier de données par spécialité (`data/specialites/<id>.js`) pour que plusieurs agents travaillent sans conflit.
- Valide chaque fichier par script (schéma, sources, « À vérifier », absence de dose non citée) et étends `tests/audit.js`.
- Rédige toutes les phrases visibles en style verbal et concis, jamais nominal.

## Livraison
- Pousse chaque spécialité terminée sur `main` dans `jeu-revision/`, avec captures et rapport d'audit.
- Annonce à Grok Bot la fin de chaque spécialité : commit, nombre de cas et de cartes, taux « À vérifier », failles.
- Ne déclare jamais une spécialité finie sans audit indépendant. La relecture médicale finale revient à Vial.
