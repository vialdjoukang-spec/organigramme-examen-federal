# Prompts qui marchent — retour à [00 Accueil](00_ACCUEIL.md)

Principe n° 1 : le **premier message d'un run est identique pour tous les runs d'un même poste** (le numéro de leçon vient après, dans un second message ou dans le fichier de tâche). Un préfixe identique permet au cache du fournisseur, s'il existe, de servir le paquet. Principe n° 2 : un run = un poste = une ou plusieurs leçons selon `ADR-003`.

| Poste | Message constant (copier tel quel) |
|---|---|
| redacteur-phase-a | « Poste redacteur-phase-a (grok-4.7 xhigh). Lis `grok-LOTS-html/_cache/contexte/<LOT>/redacteur-phase-a.md`, puis `TACHE.md` du même dossier. Écris la Phase A. Avant de rendre la main : `python3 grok-LOTS-html/outils/porte_zero_jeton.py avant auditeur-medical <fichier>` doit répondre VERT. 10 lignes de réponse au plus. » |
| redacteur | « Poste redacteur (grok-4.7 xhigh). Lis le paquet `redacteur.md` puis `TACHE.md`. Écris le DD indiqué. Porte zéro jeton VERT avant de rendre la main. 10 lignes au plus. » |
| auditeur-medical | « Poste auditeur-medical (grok-4.6 xhigh, run distinct du rédacteur). Lis le paquet `auditeur-medical.md` puis `TACHE.md`. Vérifie d'abord les citations listées « non retrouvées » par la porte, puis doses, seuils, conduite, ordre et gravité. Corrige en place, journalise. 15 lignes au plus. » |
| auditeur-conformite | « Poste auditeur-conformite (grok-4.5). Lis le paquet `auditeur-conformite.md` puis `TACHE.md` : la porte a déjà corrigé les espaces et listé les alertes de langue ; traite ces alertes, rien d'autre. Fond médical interdit : tu ne le touches pas. » |
| transversale | « Poste transversale (grok-4.6). Lis le paquet `transversale.md`. Cohérence des doses, seuils, rangs entre les 11 fichiers ; `evidence/` manquants. » |

Lecture d'un HTML V8 (rédacteur, audit, reprise) : `python3 grok-LOTS-html/outils/extraire_v8.py <fichier> --points N,N`. Ne pas utiliser `harnais/controle_lot.py extraire` sur ces fichiers : il renvoie 0 octet (P-21). Jamais un HTML de plus de 50 Ko en entier.

Gabarit de `TACHE.md` (écrit par Tunder, 5 lignes) : LOT · fichier · numéro DX · nom exact (liste canonique) · SHA-256 du fichier à auditer (si audit).

Mesure à tenir à jour : durée, octets lus, coût relatif de chaque run (`outils/couts.py noter`).
