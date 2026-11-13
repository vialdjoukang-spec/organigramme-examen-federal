# Brief harnais — rédacteur d'un DX (remplace la lecture de MISSION_FICHIER_L1, CONSIGNES et des extraits du prompt L1)

**Avant tout (3 commandes, ≈ 6 Ko lus au lieu de ≈ 300 Ko)**
1. `python3 Claude/_harnais/memoire_agent.py lire <LOT> DX.<n>` — ton carnet (reprise sans relecture).
2. `sed -n '1,60p' Claude/LOT_0NN/MEMOIRE.md` — liste gelée, états, restants d'audit, sources déjà lues.
3. `python3 Claude/_harnais/sources_cache.py index <mot>` — une source déjà lue n'est jamais refetchée.
4. Doute, question, « déjà fait ? » : `python3 Claude/_harnais/cerveau.py cherche "<question>"` avant toute relecture.
Orientation : `python3 Claude/_harnais/bracelet.py "<tâche>"` → 1 à 3 outils, jamais plus.

**Écrire en peu de tours** : rédige le cours en UN fichier Python de contenu (modèle : gen.py + contenu.py du LOT_023/024/025),
génère, contrôle, corrige par remplacements groupés. Plusieurs appels d'outils indépendants dans le même tour.
**Jamais de lecture intégrale d'un cours** (première fuite mesurée) : `extrait.py plan|point N|cherche <motif>` ;
Read toujours avec `limit` ; une sortie d'outil > 20 000 caractères est une alerte du Gaspillon. Verdict d'audit réutilisé si le sha8 est inchangé. Une source : `sources_cache.py cherche <url> <mot>` (phrases verbatim).

**Ordre de Vial du 12.11.2026 (prioritaire)** : de la démarche diagnostique jusqu'à la prise en charge et au suivi, précision agressive — examen ciblé selon les sociétés suisses (indication, seuil, interprétation, conduite), traitement structuré (molécule AIPS, dose, durée, contrôle, critères d'échec), surveillance datée ; en tableaux dans les fenêtres, concision profonde ; puiser davantage dans la source lue en amont, sans perte de temps.
Couleurs plus vivantes, surtout le fond d'écran (palette propre à chaque cours, contraste AA conservé).

**Règles L1 (non négociables)** : 14 points ; point 1 = définition seule ; fenêtres `:target` non imbriquées ; 80–150 Ko hors images ;
phrases verbales 12–28 mots ; aucune redite ; sources suisses puis européennes lues et datées ; rien d'inventé ; déduction
écrite comme telle ; images réelles EN COULEURS d'abord (Blausen, OpenStax, PMC CC BY), repères vérifiés par superposition PIL ;
point 6 une fenêtre par région ; point 11 : 11.A but, 11.B moyens, 11.C surveillance, 11.D pronostic ; point 14 ≥ 6 questions.

**AIPS** : `aips_fiche.py trouve <nom|n°>` (corpus refdata hors ligne : n°, date, URL SmPC) puis `aips_fiche.py fiche <url SmPC>`.
Domaine en échec deux fois : disjoncteur, changer de source. Grossesse, allaitement,
contre-indications et date « mise à jour » recopiés MOT POUR MOT ; hors AIPS écrit « hors AIPS », sans dose.

**Portes gratuites avant de rendre (toutes vertes)**
`controle3.py --script-ok`, `verif_aips.py`, `aips_fiche.py verifier`, `abreviations.py`, `resumeur.py <LOT>`.

**Mémoire** : à chaque étape utile, `memoire_agent.py note <LOT> DX.<n> source|aips|decision|image|reste "<une ligne>"`.
**Le dépôt MEDINA est fermé** (verrou : tout accès refusé).
**Git** : tes fichiers seulement ; jamais --force, checkout, reset, stash. Rapport final ≤ 5 lignes.
