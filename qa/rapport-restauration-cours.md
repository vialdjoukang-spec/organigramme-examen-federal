# Restauration des parties de cours SSP · 19.10.2026

Le routage des cours et des fiches éclair retrouve celui précédant #117. Les monographies DD restent inchangées ; aucun contenu clinique n’est réécrit.

Comparaison indépendante : 248 fiches et3472 parties identiques à l’historique ;673 régions d’examen et941renvois conservés.23tests de coordination/veille et5gardes locaux verts ; orig intacte, budgets inchangés. Patch0037 rejoué puis idempotence vérifiée.

Le navigateur local est bloqué (binaire Playwright absent puis file:// refusé pour le parcours ciblé). Les validations réelles ordinateur/tactile/clavier et Visuel sont requises dans la [CI de cette branche](https://github.com/vialdjoukang-spec/organigramme-examen-federal/actions?query=branch%3Afix%2Frestaurer-cours-ssp). La configuration des budgets visuels n’est pas modifiée.

Preuves et empreintes : audit/RESTAURATION-COURS-SSP-20261019.json. Ce correctif d’affichage ne constitue pas une relecture médicale des3472 contenus existants.

CI39229857547 :278/278 et parcours SSP/DD réussis. Les6écarts de fenêtres voulus ont été examinés (référence/actuel et rouge), puis adoptés par le workflow contrôlé39230372459. CLS clair ordinateur lent0,0358→0,0359 (+0,0001) accepté et justifié dans audit/RESTAURATION-VISUELLE-SSP-20261019.json ; autres plafonds et compteurs accessibilité inchangés. CI après adoption requise avant fusion.
