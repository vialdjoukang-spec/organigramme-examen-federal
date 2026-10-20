# Pause utilisateur — état des lieux P1

Pause générale demandée le 2026-10-20T19:23:09.410Z. Aucun agent actif et aucune reprise automatique.

Main publié : `a02bc1cd18437a2d78db99b235b6496b1d196288`. P0 achevée. P1 : **48/113 cours S publiés, 672 parties des cours S**. CI main39477737794 et Pages39477748076 réussis ;114 fichiers publics contrôlés HTTP200/SHA256.

| Lot | Situation à la pause |
|---|---|
| PR179 S4.4–S4.5 | Non fusionnée. Ancienne tête c122 : tests/rendu réussis, liens échoué DOI FMS2003. Substitution primaire Liège2017 intégrée localement523f161 ; contre-audit final interrompu avant attestation et nouvelle CI. |
| PR180 S4.6–S4.7 | Deux contre-audits favorables documentaires, enregistrés09bd51d ; non intégrée/non publiée. |
| PR185 S4.8–S4.9 | Deux contre-audits favorables documentaires, enregistrés3d9acd0 ; non intégrée/non publiée. |
| PR188 S4.10–S4.11 | Cinq constats clos, deux contre-audits favorables documentaires conservés83f7560 ; registre/intégration/publication à faire. |
| PR191 S4.12–S4.13 | Travail auteur conservé6543d8e ; aucune attestation indépendante ni publication. |

Les lots préparés ne s’additionnent pas au compteur publié. Pas de validation médicale humaine attestée. Diagnostics différentiels et Gestes suspendus, P2–P4 non engagées. Les anciens travaux sont préservés.

Reprise exacte : terminer le contre-audit ciblé de la nouvelle source14 S4.5, mettre à jour attestations/empreintes puis relancer la CI179 et attendre tous contrôles verts. Fusion normale, CI main, Pages et contrôle public avant180. Propager la correction documentaire partagée aux lots suivants et recontrôler leur portée avant intégration.

`checkpoint.json` contient les chemins et SHA locaux exacts. `sources-et-rapports.zip` sauvegarde les patches canoniques et rapports contre le main indiqué, hors assets générés et images ; l’archive locale complète et les worktrees conservent aussi les captures. Cette branche de sauvegarde ne publie aucun nouveau contenu clinique sur main.
