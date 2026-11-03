# Instruction prioritaire du chantier LOTS — 3 novembre 2026

Lire d'abord `ORDRE_VIAL_PASSATION_GPT.md` dans ce répertoire. Cet ordre direct de Vial prime sur les anciens prompts de poursuite du chantier LOTS. Il ne modifie ni les autres producteurs ni les autres branches.

## Codex : arrêt bloquant maintenu

Codex et ses anciens sous-agents ne reprennent aucune production, ne lancent aucun agent et ne réactivent aucun automate dans `codex-LOTS-html/`. Le nom historique `codex/lots` n'autorise pas leur reprise. L'automatisation `6ae52476f6448191b77facd444e21214` doit rester désactivée. Les seules opérations résiduelles autorisées sont la conservation de travaux déjà existants et l'accusé de passation ; aucun effacement ni remplacement des travaux de GPT.

## GPT : responsable désigné pour la suite

Vial confie la reprise à GPT dans la session de passation. Ce transfert ne lève pas le STOP de Codex. Lire le point d'arrêt dans `LOT_132/audits/PAUSE_VIAL.json`, puis `CONTINUATION_WORK.me`, `REPRISE_CODEX.md`, `ETAT_CONTINUITE.json`, `CONTRAT_CONTINUITE.md` et les guides du harnais avant production. Les déclarations datées de l'ancien runtime ne prouvent pas une activité actuelle.

Vérifier le dépôt frais, les réservations et l'absence de conflit d'activité avant les écritures de production. Ne jamais voler un verrou d'un autre runtime. Le statut `pause` historique est conservé comme protection de l'ancien producteur tant que la reprise technique de GPT n'est pas effectivement établie ; ne pas le convertir en `actif` pour suggérer fictivement un démarrage.

La première unité à reprendre est LOT132, sans recréer LOT133. PhaseA et liste canonique sont conservées. DX1 et DX6 restent des brouillons non validés, avec corrections/audit à terminer avant toute publication clinique. Aucun des huit autres diagnostics n'est réputé livré sur la seule foi d'une délégation passée.

Conserver toutes les exigences scientifiques, documentaires et techniques : sources réellement lues, AIPS exact pour les doses, 14 parties/14 questions, audit distinct, contrôles reproductibles et réserves explicites. Ne pas inventer d'agents, d'audits ou de tests. Les images ne bloquent pas le texte contrôlé, mais aucune image ne peut être insérée sans droits et inspection vérifiés.

Seul le responsable de la session intègre les modifications globales et Git. Écritures exclusivement dans `codex-LOTS-html/`, sans force-push ni modification d'autres automates ou producteurs. Ne promettre aucune activité après la fin de l'exécution.
