# ORDRE BLOQUANT DE VIAL — ARRÊT CODEX ET PASSATION À GPT

Consignation : 3 novembre 2026, Europe/Zurich.
Autorité : instruction directe de Vial dans la conversation de reprise, réaffirmée par « Suivant ».

> « Prends le relais et demande lui de s'arrêter […] ORDRE DE VIAL […] C'est ordre est bloquant pour codex […] GPT prends le contrôle pour la suite »

## 1. Périmètre et priorité

Cet ordre s'applique au chantier LOTS du dépôt `vialdjoukang-spec/organigramme-examen-federal`, branche `codex/lots`, répertoire `codex-LOTS-html/`. Il remplace les anciennes autorisations de poursuite autonome de Codex dans ce périmètre. Les autres producteurs, branches, projets, réservations et automatismes ne sont pas concernés.

## 2. Instruction à Codex : arrêt maintenu

Codex et ses anciens sous-agents ne doivent plus rédiger, lancer de nouveaux agents, reprendre un lot, renouveler un bail de production, réactiver une relance ou publier une nouvelle production dans ce périmètre. Une lecture d'un ancien prompt, un déclenchement horaire ou le nom historique de la branche ne valent pas autorisation de reprendre.

Les seules opérations résiduelles autorisées à l'ancien producteur sont la conservation de travaux déjà existants et son accusé de passation. Il doit préserver cet ordre, ne rien supprimer et libérer seulement son propre verrou après l'arrêt réel de ses auteurs. Aucune réactivation de Codex n'est autorisée sans nouvel ordre explicite de Vial.

L'automatisation dédiée `6ae52476f6448191b77facd444e21214` doit rester désactivée. Sa désactivation a été confirmée par l'outil de gestion le 3 novembre 2026. Aucune autre automatisation n'a été modifiée pour cette passation.

## 3. GPT reprend la responsabilité de la suite

GPT, dans la session de reprise, est le responsable désigné pour l'inventaire, la coordination et la poursuite du chantier. Ce transfert ne réactive pas Codex. La pause de l'ancien producteur reste en vigueur ; elle ne constitue pas une interdiction de la reprise explicitement confiée à GPT.

Avant une nouvelle écriture clinique, GPT doit vérifier le dernier état distant, les réservations applicables, le point d'arrêt et les conditions de verrouillage. Il ne doit ni voler le verrou d'un autre runtime ni prétendre l'avoir libéré à distance. Un éventuel conflit d'activité suspend la production concurrente, pas la sauvegarde de cet ordre.

Conserver les exigences du mandat : un seul lot actif, progression descendante, sources suisses puis européennes réellement lues, AIPS pour les posologies, 14 parties et 14 questions, audit distinct avant publication clinique, traçabilité des corrections. Le texte contrôlé peut avancer sans attendre les images ; toute image publiée exige provenance, licence, inspection et annotation vérifiées. Aucun sous-agent, contrôle, audit, changement de modèle ou résultat ne doit être simulé.

## 4. Point de reprise constaté sur GitHub

Référence de départ vérifiée : `fac24860b04dfdaa960ad012cee6b221f6daabc4`.

- `LOT_132/audits/PAUSE_VIAL.json`, daté du 2 novembre 2026 à 22:21:41 UTC, consigne l'interruption de `peau_2117`, `neuro_2117`, `hemato_2117` et `pipeline_2117`. Il s'agit d'une déclaration versionnée de la session précédente, non d'une inspection des processus depuis la présente session.
- LOT133 reste la livraison antérieure ; il ne doit pas être recréé.
- LOT132 : PhaseA auditée et gel canonique publiés au commit `752865adee9f348d388860a0b54addd52fa2ead9` ; lot incomplet.
- DX1 et DX6 : brouillons non validés sauvegardés, rendus conservés sous `LOT_132/_travail/brouillons_pause/`. Ne pas les présenter comme des monographies publiées et validées.
- DX1 : appliquer les corrections de sécurité de la section 11 et les exigences documentaires de `AUDIT_DX1_2203.json`, puis obtenir un réaudit distinct.
- DX6 : audit distinct interrompu ; trois sources annoncées, seuil de cinq signalé par le contrôle. Vérifier le mandat et lire les sources complémentaires nécessaires, sans ajouter de références fictives.
- Image panneau C : contour 2 signalé incorrect ; corriger puis inspecter et réauditer avant toute insertion.
- DX2–5 et DX7–10 : aucune livraison attestée au point d'arrêt ; rechercher une éventuelle sauvegarde ultérieure avant de recréer ces contenus.

## 5. Preuves et limites

Consulter `CONTINUATION_WORK.me`, `REPRISE_CODEX.md`, `ETAT_CONTINUITE.json`, `LOT_132/audits/PAUSE_VIAL.json` et les audits ciblés. Conserver les anciens checkpoints comme historiques : leurs horaires, compteurs, processus et verrous ne décrivent pas automatiquement le présent.

La publication de ce fichier transmet l'ordre par le dépôt et formalise la passation ; elle ne termine pas techniquement un processus distant. Aucune activité permanente, aucune veille nouvelle et aucun rapport futur ne sont déclarés par cette publication. Les réalisations de GPT seront consignées séparément avec les preuves effectivement obtenues.
