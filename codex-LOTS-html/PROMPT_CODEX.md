# PROMPT_CODEX — à l'attention de Codex (OpenAI), chantier LOTS

Codex, ce prompt t'est adressé personnellement par Vial (ordre du 30.10.2026). Il régit **uniquement** le chantier LOTS (leçons HTML par SSP). Pour ce chantier, il prime sur `AGENTS.md` et `CLAUDE.md` : la procédure `porte.py` / `checkpoint.py` / PR « Pilote Codex » ne s'applique pas ici. Les autres mandats de `AGENTS.md` (cours S, P1…) ne sont ni modifiés ni concernés.

## 1. Ta place
Trois IA produisent en parallèle sans se gêner : Claude (branche `production-v2`, LOTS 001–017), toi (branche `codex/lots`, dossier `codex-LOTS-html/`, LOTS 018–133), Grok (branche `grok/lots`, dossier `grok-LOTS-html/`, LOTS 134–248). Tu disposes d'un terminal et de git : tu exécutes toi-même les commandes ci-dessous, tu ne prétends jamais avoir exécuté une commande que tu n'as pas lancée.

## 2. Avant toute écriture : lire et signer le registre (bloquant)
Depuis la racine du dépôt :
```
git fetch --all && git checkout -B codex/lots origin/codex/lots 2>/dev/null || git checkout -b codex/lots origin/production-v2
python3 codex-LOTS-html/registre_ia.py lire codex          # lois + état de chaque LOT + jeton du jour
python3 codex-LOTS-html/registre_ia.py signer codex <jeton>
python3 codex-LOTS-html/registre_ia.py installer codex     # hook pre-commit qui bloque tout commit interdit
python3 codex-LOTS-html/registre_ia.py verifier codex LOT_XXX   # avant chaque LOT : doit répondre AUTORISÉ
```
Sans signature du jour, tout commit est refusé. `codex-LOTS-html/REGISTRE.md` donne l'état d'avancement de chaque LOT (déposé, amorcé, libre), l'IA qui le tient et la plage réservée à chacune.

## 3. Lois (extrait du registre, non négociables)
- Tu écris **uniquement** dans `codex-LOTS-html/` et sur la branche `codex/lots`. Tout le reste du dépôt est en lecture seule.
- Interdiction absolue de rédiger ou de modifier un LOT ou un chapitre déjà amorcé (un seul fichier suffit) par Claude, par l'autre IA ou par toi-même, sans validation écrite de Vial dans `IA_AUTORISATIONS.json`.
- Tu ne rédiges que les LOTS **libres** de ta plage (`IA_RESERVATIONS.json` : codex = LOT_018 à LOT_133), dans l'ordre croissant. Priorité : les LOTS jamais explorés.
- Ce qu'une autre IA a écrit est en lecture seule ; seul Vial lève ce verrou.
- Tu ne modifies jamais `registre_ia.py`, ses clones, `REGISTRE.*`, `IA_RESERVATIONS.json`, `IA_AUTORISATIONS.json`, ni aucun fichier de Claude (`harnais/`, `LOT_Claude_Finaux/`, `lot en cours de production/`, `LOTS_html/`, `.claude/`, `journal/`, `PROMPT_*.md` racine) ni de l'autre IA.
- Tu ne fusionnes rien sur `main` ni sur `production-v2`. Seul Vial fusionne.

## 4. Outils : chemins d'accès (lecture seule ; copie autorisée dans ton dossier)
Pour adapter un outil, copie-le dans `codex-LOTS-html/outils/` et modifie la copie ; ne touche jamais l'original.
| Besoin | Chemin | Usage |
|---|---|---|
| Règles de fond, format, chaîne, leçons | `PROMPT_PRODUCTION_V2.md` | à lire en entier (≈ 110 lignes) |
| Détail normatif | `PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V0.md` | lecture ciblée §9–14, §16, §18–19 (`grep -n` puis `sed -n`) |
| Contrôle d'un LOT | `harnais/controle_lot.py` | `verifier codex-LOTS-html/LOT_XXX --sans-nom --json` ; `extraire <fichier> --points 2,3` ; `manifeste codex-LOTS-html/LOT_XXX` |
| Langue et forme | `harnais/audit_langue.py` | `<fichier> --json` avant chaque relecture |
| Rôles (rédacteur, auditeurs) | `.claude/agents/redacteur*.md`, `auditeur-medical.md`, `auditeur-conformite.md` | consignes de chaque poste ; tu les appliques toi-même, poste par poste |
| Briefs types | `harnais/briefs/AUDIT_MEDICAL.md`, `harnais/briefs/CONFORMITE.md`, `lot en cours de production/LOT_017/BRIEF_PHASE_B.md` | modèles à copier pour ton LOT |
| Leçons accumulées | `lot en cours de production/LOT_017/LECONS_LOT_016.md`, `lot en cours de production/LOT_016/LECONS_LOT_015.md` | obligatoires |
| Exemple de LOT achevé | `LOT_Claude_Finaux/LOT_016/` (11 HTML, `LISTE_DX_CANONIQUE.md`, `audits/`) | modèle de structure, jamais à copier comme contenu |
| Catalogue des 248 SSP | `LOT_Claude_Finaux/CATALOGUE_248.csv` | intitulé exact du SSP de chaque LOT |
| AIPS suisse (hors ligne, complète) | `ressources_ia/aips/` : index XML, 4 646 informations professionnelles françaises en texte intégral, extraits déjà lus | `python3 ressources_ia/outils/aips.py chercher <nom>` puis `lire <numéro> [motif]` ; jamais le Compendium |
| Listes Swissmedic et OFSP | `ressources_ia/swissmedic/` (conditionnements autorisés, médicaments humains), `ressources_ia/liste_specialites/` (liste des spécialités, limitations) | numéro par forme galénique ; remboursement ; voir `ressources_ia/README.md` |
| Démarrage pas à pas | `codex-LOTS-html/DEMARRAGE.md` | 8 étapes |

## 5. Structure de ton dossier
```
codex-LOTS-html/
  registre_ia.py  REGISTRE.md  REGISTRE.json  SIGNATURES.log   (registre ; seul SIGNATURES.log est écrit par toi, via `signer`)
  PROMPT_CODEX.md                                           (ce prompt)
  LOT_XXX/                                                    (un LOT de ta plage)
    LOT_XXX_Phase_A_V0.html  LOT_XXX_Phase_B_V0_DX.1.html … DX.10.html
    LISTE_DX_CANONIQUE.md
    _travail/  HELP.md  JOURNAL.md  CORRECTIONS_AUDIT.md  evidence/ (extraits datés + INDEX.md)  audits/corrections.jsonl  audits/scores.jsonl
  outils/   (copies d'outils adaptées)   _cache/ (non commité)
ressources_ia/   (commun, lecture seule : AIPS, Swissmedic, liste des spécialités)
```

## 6. Production d'un LOT (même exigence que Claude)
1. `verifier codex LOT_XXX` → AUTORISÉ. Lis l'intitulé du SSP dans le catalogue et les leçons.
2. **Phase A** (poste rédacteur) : monographie du SSP en 14 points, 10 DD classés (prévalence, gravité E/🚩), tableau comparatif, algorithme ; 110–125 Ko ; fenêtres `popover` ; rappels de sciences fondamentales au point 3 quand le SSP l'exige ; `<!-- FIN_FICHIER LOT_XXX_Phase_A -->`.
3. **Audit médical de la Phase A** (poste auditeur, passe distincte — nouvelle tâche Codex ou nouvelle session, jamais dans la même passe que la rédaction) : vérifie chaque chiffre et dose à la source, corrige en place, **gèle** `LISTE_DX_CANONIQUE.md`, écrit `CORRECTIONS_AUDIT.md`, journalise.
4. **Phase B** : un fichier par DD (`<h2>DX.N — nom exact</h2>`, 14 points `dxN-p1…p14`), en héritant de `CORRECTIONS_AUDIT.md`. Puis, pour chaque fichier, audit médical, puis audit de conformité (`audit_langue.py` d'abord).
5. **Passe transversale** : cohérence des doses, seuils et rangs entre les 11 fichiers ; extraits `evidence/` manquants.
6. **Clôture** : `controle_lot.py verifier codex-LOTS-html/LOT_XXX --sans-nom` à 0 critique ; `manifeste` ; commit (le hook vérifie) ; push sur `codex/lots` ; une ligne dans `codex-LOTS-html/JOURNAL_CODEX.md` (date, LOT, nombre de corrections, graves, critiques). Puis LOT suivant de ta plage.
Règles de fond : sources suisses puis européennes, lues et datées, sinon « À vérifier » ; doses AIPS suisses seulement, citées mot pour mot (grossesse, allaitement, enfant, contre-indications), usage hors information professionnelle écrit en clair ; aucune donnée personnelle ; n'affirme que ce que tu as fait ; mention finale « Contenu établi à partir des sources citées ; non validé cliniquement par un médecin. »

## 7. Fin de session
`python3 codex-LOTS-html/registre_ia.py etat`, commit, push. Signale à Vial : LOTS déposés, LOT en cours et fichier exact, questions ouvertes. Ne laisse jamais un fichier sans `FIN_FICHIER` sans le dire.
