# Reprise Codex — LOT_226 — 25 octobre 2026

## Résultat

La PR453 a été reprise à son dernier commit publié, `6e7ab4381fd68b4df4c39fcb8f2509d9b1197d11`. Le harnais individuel canonique fonctionne désormais dans ce nouvel environnement. La préparation technique est renforcée et huit pages primaires suisses ont été ouvertes pour la Phase A. Aucun cours achevé, score médical, audit indépendant ou lot complet n’est revendiqué.

## Défauts reproduits puis corrigés

1. Un registre actif avec `deployment_enabled:true` rendait `may_execute:true` malgré une preuve runtime échouée. La décision et le harnais doivent maintenant être prêts pour toutes les affectations ; un registre vide ne donne aucun GO. Ce résultat demeure un prérequis technique, sans exécution et sans franchissement des portes documentaires du fichier.
2. Trois booléens `ok:true` suffisaient au contrôle du harnais. Les versions du watcher existant, l’identifiant de l’exécution, la reconstruction des segments, les opérations du cache et les mesures de compression canonique sont maintenant exigés.
3. Du code actif dans un attribut HTML passait sans balise script. Les attributs événementiels, les URL actives détectées, les éléments SVG et les ressources CSS détectées sont maintenant refusés. Ce contrôle n’est pas un assainisseur universel.
4. Une marque de fin indiquant un autre lot ou une autre partie était acceptée. Elle doit maintenant identifier exactement le fichier.
5. Une monographie étrangère imbriquée pouvait contribuer au poids du SSP. Les identifiants réservés des entités doivent désormais correspondre exactement au découpage attendu.

## Vérifications réelles

- Avant correction, les 38 tests de pilotage et les 27 tests existants de surveillance réussissaient malgré ces lacunes. Les reproductions ciblées exposaient les faux positifs.
- Après correction, les 45 tests de pilotage et les 27 tests de surveillance réussissent. Les fixtures sont synthétiques ; elles ne produisent aucun cours et ne constituent aucune preuve clinique.
- Le probe `harnais/surveillance/runtime_probe.py` est inchangé. La seconde exécution utilise les versions canoniques, dont torch 2.14.1+cpu. Chonkie reconstruit sept segments ; GPTCache vérifie écriture/lecture et clé distincte ; LLMLingua mesure 97 puis 54 tokens sur texte synthétique. Aucun document médical n’est comprimé.
- Le premier essai de cette reprise utilisait torch 2.14.1 sans suffixe CPU ; il n’est pas utilisé comme preuve canonique. La version CPU a ensuite été installée par la commande du workflow existant, via son index officiel.
- Le refus réseau de la session antérieure ne se reproduit plus. La preuve d’échec historique reste conservée séparément ; aucun changement de proxy, aucune URL de secours et aucun assouplissement du probe ne sont utilisés.

## Sources et reprise clinique

`evidence/REGISTRE_SOURCES_PHASE_A_V0_REPRISE.json` contient les huit pages primaires réellement relues, leurs extraits brefs, leurs emplacements, leurs dates et leurs limites. Le référentiel confirme O7.4 ; les pages OFSP/Obsan/ASSM couvrent l’autogestion, la solitude, le consentement, l’interprétariat, les proches aidants et les obstacles financiers. Les documents PDF liés ne sont pas réputés lus. Le guide de qualité est annoncé comme actualisé en octobre 2023 et mis en ligne en mai 2024 ; ces deux dates ne sont pas confondues.

Les dénominateurs des indicateurs diffèrent. Ils ne permettent pas de classer statistiquement dix scénarios chez les malades chroniques. La liste canonique reste donc non gelée. Aucun chiffre de fréquence, aucune loi et aucune posologie n’est inventé. La rédaction B reste fermée.

## Prochaine action exacte

Lire les documents primaires de qualité et de discernement, les bases légales applicables et les références des expositions environnementales ; poursuivre le dossier exhaustif de Phase A du LOT_226, puis condenser sans perdre de données et obtenir les deux grilles indépendantes. Renouveler la preuve runtime si elle dépasse une heure. Le contrôleur reste en lecture seule, le registre reste arrêté, le déploiement reste désactivé. Le contre-audit indépendant du moteur et la QA390 autorisée restent à obtenir.

La présente vérification est une relecture technique du repreneur ; elle n’est pas déclarée contre-audit indépendant de l’ensemble de la PR. Aucun workflow, aucune tâche GPT, aucun autre lot et aucun fichier clinique historique ne sont modifiés. `tools/arsenal/pr.sh` n’est pas exécuté.
