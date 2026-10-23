> **Consigne humaine prioritaire, mise à jour le 24.10.2026 :** Thunder est l’utilisateur humain (compte GitHub vialdjoukang-spec), et non une IA Grok. ChatGPT rédige A et B. Rien n’est transmis, déposé ou publié sans sa validation humaine explicite du livrable concerné. Les rédactions restent locales jusque-là. LOT_Tunder, sur main, sert à la réception pour relecture après fusion effective de la PR272 et autorisation de transmission. LOT_Finaux_Audités reste réservé aux cours acceptés. Aucun agent ne fabrique une approbation humaine ni ne l’infère d’un commit sur le compte partagé. Les anciennes mentions d’un compte externe/IA ou d’une publication automatique ci-dessous sont remplacées par cette consigne.

# Mandat Phase LOT — 24.10.2026

La demande utilisateur courante définit un chantier autonome de production HTML. Elle remplace ici les anciennes priorités Alpha/Beta de l'application, sans modifier leurs fichiers ni leurs automates.

1. Lire `instructions/MANDAT.md`, le prompt V7, la grille exacte et la sélection du LOT actif.
2. Une seule production de LOT à la fois, ordre 001 à 010. A doit être entièrement terminé avant B. Aucun audit à cette porte.
3. A sélectionne dix diagnostics. B1..B5 reçoivent respectivement 1–2, 3–4, 5–6, 7–8, 9–10. Chaque diagnostic et le SSP suivent les quatorze points du V7.
4. Recherche GPT-6.1 Sol high ; rédaction medium par seconde invocation du même rôle, avec fichier de preuves. Le moteur ne permet pas de changer le raisonnement d'un sous-agent en cours : journaliser les deux invocations et leurs identifiants réels. Ne pas prétendre à une bascule automatique.
5. Chaque agent a une branche/worktree et un préfixe de sortie exclusif. Aucun agent auteur ne modifie file.json, scripts, registre partagé, final ou fichier d'un autre agent. Le coordinateur seul intègre par copie explicite des chemins autorisés, avec contrôles d'empreintes.
6. Les scripts détectent la structure et les lacunes ; ils ne donnent jamais une note clinique ni ne remplacent Tunder. Corriger le médical seulement avec une source primaire réellement lue.
7. Thunder est l’utilisateur humain, seul auditeur médical, des 14 parties et linguistique. Son compte GitHub vialdjoukang-spec a les droits admin vérifiés. Aucun score, audit, accès, source lue ou réveil IA fictif.
8. Les candidats restent sur leurs branches, hors destination finale. Final uniquement après rapport externe sur SHA exact. La fin de production active le LOT suivant ; l'audit reste une file distincte.
9. Aucune suppression, déplacement d'archives, fusion clinique dans main ou publication de l'application dans ce mandat initial. Préserver tous les contrôles et protections existants.
10. Sources CH puis UE, internationales applicables en Suisse. AIPS pour les doses, numéros Swissmedic vérifiés, aucun Compendium, aucune fréquence inventée. Une lacune reste dans HELP et empêche d'affirmer la conformité totale.
11. Avant de reprendre comme coordinateur, acquérir `scripts/lease.py --owner <identifiant-unique>` sur `lot-pilotage/etat`. Refuser un bail concurrent non expiré. Le renouveler seulement pendant le travail réel, toutes les quelques minutes, jamais depuis une sonde. Libérer en fin de session. Les auteurs B n'écrivent pas ce bail.
