# Décision de séance — LOT_052 — 2026-11-10

Ordre écrit de Vial, médecin et propriétaire du dépôt, du 2026-11-10 : détruire le contenu de `Grokbot/LOT_052` et le refaire selon `PROMPT_Casern/PROMPT_LOTS_Lo_9.11.26.claude.md`, avec les images en paire brut / annotée de la version µ6 du 10.11.2026. Cet ordre prime, pour ce lot, sur les consignes plus anciennes du dépôt.

Branche imposée : `grok/refonte-lot-052`, prise sur `main` au commit `f5e8d76e4`. Pas de pull request, pas de fusion, pas d'auto-merge. Bitunder audite puis décide.

Collision lue, non modifiée : `origin/claude/lot-052` (autre dossier) et `origin/grok/lot-052-bande` (ancienne version d'environ 10 Ko). `outils/mere.py` n'a pas été lancé, parce qu'il écrit dans `outils/`.

Porte : la liste est écrite et hashée. `controle3.py` est vert sur la Phase A seule. Cela ne vaut ni audit indépendant, ni porte P3, ni porte P4. Deux fichiers sur onze seulement : la Phase A est livrée, DX.1 suit dans le commit suivant de cette même session, DX.2 à DX.10 attendent le feu vert explicite de Bitunder.

Définition retenue : il n'existe pas, dans les textes lus, de définition d'une société savante mondiale en une phrase pour « douleur abdominale ». La définition opératoire est celle de Sinz, Schmied et Ukegjini, Forum Médical Suisse, 2021, responsabilité scientifique Ukegjini, hôpital cantonal de Saint-Gall. Les bornes de durée viennent des Hôpitaux universitaires de Genève (aigu : moins de 7 jours, colloque du 11 octobre 2017 ; chronique : au moins 3 mois, stratégie 2023).

Image de Phase A : le cliché libre qui sépare la perforation (E2). Un cliché d'ischémie mésentérique (E1) sans légende déjà imprimée et sous licence libre n'a pas été obtenu. La latéralité « sous le diaphragme gauche » est celle de la description Commons ; le cours ne la recalcule pas.

Doses : seules les informations professionnelles ouvertes (Dafalgan oral 47503, Dafalgan intraveineux 66702, Algifor Liquid Caps 400, 65372). Aucun milligramme d'antibiotique, de métamizole ou de morphine.

## Correction de la Phase A — 2026-11-10, soir

Ordre de Vial (« Tu dois corriger ») : la Phase A est réécrite par Grok Bot lui-même, sans délégation, selon `CHARTE_VIAL_10.11.26.md` et `PROMPT_LOTS_Lo_10.11.26.claude.md`. Cette section remplace les décisions ci-dessus sur la liste, la définition, les images et les doses.

- Liste : celle de `LISTE_DX_CANONIQUE.md` déjà poussée sur la branche (commit af1c771c0, fréquence au cabinet, série HUG la plus récente), sans MICI ni hémorragie digestive. La Phase A la reprend telle quelle et y ajoute les rangs E du cours : E1 = GEU rompue, AAA rompu, ischémie mésentérique, occlusion ou hernie étranglée, infarctus inférieur ; E2 = perforation, angiocholite ; E3 = urgence chirurgicale sans choc (appendicite, pancréatite, diverticulite).
- Définition : HUG, colloque de médecine de premier recours du 11.10.2017 (moins de 7 jours) ; douleur chronique : HUG 2023 (au moins 3 mois) ; douleur : IASP, définition révisée.
- Sources suisses d'abord : RMS 2010 et 2006 (deux articles), HUG 2017 et 2023, smarter medicine (Société suisse de chirurgie), Forum Médical Suisse 2021 ; Börner 2025 en second. Extraits mot pour mot dans `_travail/evidence/`, indexés dans `_travail/PA/paquet.json`.
- Doses : Dafalgan® 47503, Dafalgan® i.v. 66702, Novalgin® 16950, Algifor® 65372, toutes depuis l'information professionnelle. Aucune dose d'opiacé ni d'antibiotique.
- Images : paire brute / annotée sur le cliché de Bill Rhodes ; cliché Cerevisae corrigé (repère 1 sur la clarté, 2 sur le L, 3 sur l'air libre et non sur l'estomac) et présenté comme déjà annoté par l'auteur.
- Phase B : DX.1 (douleur non spécifique) et DX.2 (gastroentérite) ont été réécrits sur la branche par un autre passage et ne sont pas touchés ici. DX.3 à DX.10 sont restaurés depuis `origin/main` (anciennes versions, ancienne liste) et restent à refaire.
- Toujours pas d'audit indépendant (Θ2-P3) : le rédacteur ne s'audite pas lui-même.
