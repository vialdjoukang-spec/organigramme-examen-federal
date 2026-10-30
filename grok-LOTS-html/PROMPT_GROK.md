# PROMPT_GROK — à l'attention de Grok (xAI), chantier LOTS

Grok, ce prompt t'est adressé personnellement par Vial (ordre du 30.10.2026). Il régit **uniquement** le chantier LOTS (leçons HTML par SSP) du dépôt `vialdjoukang-spec/organigramme-examen-federal`. Il prime pour toi sur `AGENTS.md` et `CLAUDE.md`, qui visent d'autres IA.

## 1. Ta place
Trois IA produisent en parallèle sans se gêner : Claude (branche `production-v2`, LOTS 001–017), Codex (branche `codex/lots`, LOTS 018–133), toi (branche `grok/lots`, dossier `grok-LOTS-html/`, LOTS 134–248).
**Si tu n'as pas de terminal ni d'accès git** : tu ne prétends jamais avoir exécuté une commande. Tu demandes à Vial d'exécuter `lire`/`signer`/`verifier` et de te coller la sortie ; tu produis chaque fichier HTML complet, par blocs numérotés, jusqu'à la ligne `FIN_FICHIER`, avec son chemin exact dans `grok-LOTS-html/LOT_XXX/` ; Vial le dépose et commite sur `grok/lots`. Sans sortie AUTORISÉ de `verifier` pour le LOT, tu n'écris rien.

## 2. Avant toute écriture : lire et signer le registre (bloquant)
Depuis la racine du dépôt :
```
git fetch --all && git checkout -B grok/lots origin/grok/lots 2>/dev/null || git checkout -b grok/lots origin/production-v2
python3 grok-LOTS-html/registre_ia.py lire grok          # lois + état de chaque LOT + jeton du jour
python3 grok-LOTS-html/registre_ia.py signer grok <jeton>
python3 grok-LOTS-html/registre_ia.py installer grok     # hook pre-commit qui bloque tout commit interdit
python3 grok-LOTS-html/registre_ia.py verifier grok LOT_XXX   # avant chaque LOT : doit répondre AUTORISÉ
```
Sans signature du jour, tout commit est refusé. `grok-LOTS-html/REGISTRE.md` donne l'état d'avancement de chaque LOT (déposé, amorcé, libre), l'IA qui le tient et la plage réservée à chacune.

## 3. Lois (extrait du registre, non négociables)
- Tu écris **uniquement** dans `grok-LOTS-html/` et sur la branche `grok/lots`. Tout le reste du dépôt est en lecture seule.
- Interdiction absolue de rédiger ou de modifier un LOT ou un chapitre déjà amorcé (un seul fichier suffit) par Claude, par l'autre IA ou par toi-même, sans validation écrite de Vial dans `IA_AUTORISATIONS.json`.
- Tu ne rédiges que les LOTS **libres** de ta plage (`IA_RESERVATIONS.json` : grok = LOT_134 à LOT_248), dans l'ordre croissant. Priorité : les LOTS jamais explorés.
- Ce qu'une autre IA a écrit est en lecture seule ; seul Vial lève ce verrou.
- Tu ne modifies jamais `registre_ia.py`, ses clones, `REGISTRE.*`, `IA_RESERVATIONS.json`, `IA_AUTORISATIONS.json`, ni aucun fichier de Claude (`harnais/`, `LOT_Claude_Finaux/`, `lot en cours de production/`, `LOTS_html/`, `.claude/`, `journal/`, `PROMPT_*.md` racine) ni de l'autre IA.
- Tu ne fusionnes rien sur `main` ni sur `production-v2`. Seul Vial fusionne.

## 4. Outils : chemins d'accès (lecture seule ; copie autorisée dans ton dossier)
Pour adapter un outil, copie-le dans `grok-LOTS-html/outils/` et modifie la copie ; ne touche jamais l'original.
| Besoin | Chemin | Usage |
|---|---|---|
| Règles de fond, format, chaîne, leçons | `PROMPT_PRODUCTION_V2.md` | à lire en entier (≈ 110 lignes) |
| Détail normatif | `PROMPT_Casern/PROMPT_ULTIME_PRODUCTION_LOTS_V0.md` | lecture ciblée §9–14, §16, §18–19 (`grep -n` puis `sed -n`) |
| Contrôle d'un LOT | `harnais/controle_lot.py` | `verifier grok-LOTS-html/LOT_XXX --sans-nom --json` ; `extraire <fichier> --points 2,3` ; `manifeste grok-LOTS-html/LOT_XXX` |
| Langue et forme | `harnais/audit_langue.py` | `<fichier> --json` avant chaque relecture |
| Rôles (rédacteur, auditeurs) | `.claude/agents/redacteur*.md`, `auditeur-medical.md`, `auditeur-conformite.md` | consignes de chaque poste ; tu les appliques toi-même, poste par poste |
| Briefs types | `harnais/briefs/AUDIT_MEDICAL.md`, `harnais/briefs/CONFORMITE.md`, `lot en cours de production/LOT_017/BRIEF_PHASE_B.md` | modèles à copier pour ton LOT |
| Leçons accumulées | `lot en cours de production/LOT_017/LECONS_LOT_016.md`, `lot en cours de production/LOT_016/LECONS_LOT_015.md` | obligatoires |
| Exemple de LOT achevé | `LOT_Claude_Finaux/LOT_016/` (11 HTML, `LISTE_DX_CANONIQUE.md`, `audits/`) | modèle de structure, jamais à copier comme contenu |
| Catalogue des 248 SSP | `LOT_Claude_Finaux/CATALOGUE_248.csv` | intitulé exact du SSP de chaque LOT |
| AIPS suisse (hors ligne, complète) | `ressources_ia/aips/` : index XML, 4 646 informations professionnelles françaises en texte intégral, extraits déjà lus | `python3 ressources_ia/outils/aips.py chercher <nom>` puis `lire <numéro> [motif]` ; jamais le Compendium |
| Listes Swissmedic et OFSP | `ressources_ia/swissmedic/` (conditionnements autorisés, médicaments humains), `ressources_ia/liste_specialites/` (liste des spécialités, limitations) | numéro par forme galénique ; remboursement ; voir `ressources_ia/README.md` |
| Démarrage pas à pas | `grok-LOTS-html/DEMARRAGE.md` | 8 étapes |

## 5. Structure de ton dossier
```
grok-LOTS-html/
  registre_ia.py  REGISTRE.md  REGISTRE.json  SIGNATURES.log   (registre ; seul SIGNATURES.log est écrit par toi, via `signer`)
  PROMPT_GROK.md                                           (ce prompt)
  LOT_XXX/                                                    (un LOT de ta plage)
    LOT_XXX_Phase_A_V0.html  LOT_XXX_Phase_B_V0_DX.1.html … DX.10.html
    LISTE_DX_CANONIQUE.md
    _travail/  HELP.md  JOURNAL.md  CORRECTIONS_AUDIT.md  evidence/ (extraits datés + INDEX.md)  audits/corrections.jsonl  audits/scores.jsonl
  outils/   (copies d'outils adaptées)   _cache/ (non commité)
ressources_ia/   (commun, lecture seule : AIPS, Swissmedic, liste des spécialités)
```

## 6. Production d'un LOT (même exigence que Claude)
1. `verifier grok LOT_XXX` → AUTORISÉ. Lis l'intitulé du SSP dans le catalogue et les leçons.
2. **Phase A** (poste rédacteur) : monographie du SSP en 14 points, 10 DD classés (prévalence, gravité E/🚩), tableau comparatif, algorithme ; 110–125 Ko ; fenêtres `popover` ; rappels de sciences fondamentales au point 3 quand le SSP l'exige ; `<!-- FIN_FICHIER LOT_XXX_Phase_A -->`.
3. **Audit médical de la Phase A** (poste auditeur, passe distincte — nouvelle conversation Grok, jamais dans la même passe que la rédaction) : vérifie chaque chiffre et dose à la source, corrige en place, **gèle** `LISTE_DX_CANONIQUE.md`, écrit `CORRECTIONS_AUDIT.md`, journalise.
4. **Phase B** : un fichier par DD (`<h2>DX.N — nom exact</h2>`, 14 points `dxN-p1…p14`), en héritant de `CORRECTIONS_AUDIT.md`. Puis, pour chaque fichier, audit médical, puis audit de conformité (`audit_langue.py` d'abord).
5. **Passe transversale** : cohérence des doses, seuils et rangs entre les 11 fichiers ; extraits `evidence/` manquants.
6. **Clôture** : `controle_lot.py verifier grok-LOTS-html/LOT_XXX --sans-nom` à 0 critique ; `manifeste` ; commit (le hook vérifie) ; push sur `grok/lots` ; une ligne dans `grok-LOTS-html/JOURNAL_GROK.md` (date, LOT, nombre de corrections, graves, critiques). Puis LOT suivant de ta plage.
Règles de fond : sources suisses puis européennes, lues et datées, sinon « À vérifier » ; doses AIPS suisses seulement, citées mot pour mot (grossesse, allaitement, enfant, contre-indications), usage hors information professionnelle écrit en clair ; aucune donnée personnelle ; n'affirme que ce que tu as fait ; mention finale « Contenu établi à partir des sources citées ; non validé cliniquement par un médecin. »

## 7. Fin de session
`python3 grok-LOTS-html/registre_ia.py etat`, commit, push. Signale à Vial : LOTS déposés, LOT en cours et fichier exact, questions ouvertes. Ne laisse jamais un fichier sans `FIN_FICHIER` sans le dire.

## 8. Norme de format obligatoire
Lis la section 12 de `PROMPT_PRODUCTION_V2.md` et reproduis exactement le modèle `harnais/modele_lecon/MODELE_DD_V8.html` (style `harnais/modele_lecon/style_lecon.css`). Mesure chaque fichier avec `python3 harnais/taille_xy.py <fichier> --inscrire` : fiche x ≤ 9 Ko pour un diagnostic différentiel ; **texte total x + y ≤ 100 Ko** pour toute leçon (Phase A comprise). Le fichier HTML peut dépasser 100 Ko à cause du balisage : c'est le texte qui compte, et l'information ne se perd jamais (on déplace en fenêtre, on ne compresse pas). Contrôle d'une refonte : `python3 harnais/verif_refonte.py <source> <sortie> [--ref <Phase A>]`.
