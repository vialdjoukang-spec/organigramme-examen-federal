# Message de démarrage — Codex (chantier LOTS)

Codex, voici ta mission. Dépôt GitHub `vialdjoukang-spec/organigramme-examen-federal`, branche de départ `production-v2`.

1. Lis en entier `codex-LOTS-html/PROMPT_CODEX.md`, puis `codex-LOTS-html/DEMARRAGE.md`, puis la section 12 de `PROMPT_PRODUCTION_V2.md` (norme de format V8). Ils priment pour ce chantier sur `AGENTS.md` et `CLAUDE.md`.
2. Crée ta branche : `git fetch --all && git checkout -b codex/lots origin/production-v2`.
3. Registre (bloquant) : `python3 codex-LOTS-html/registre_ia.py lire codex`, puis `signer codex <jeton>`, puis `installer codex`.
4. **Couple [Harnais + Routage] (bloquant)**, section 9 de ton prompt :
   - crée `codex-LOTS-html/ROUTAGE_CODEX.json` (table poste → tes propres modèles, auditeur médical ≠ rédacteur) à partir de `harnais/modele_routage/ROUTAGE_MODELE.json` ;
   - crée `codex-LOTS-html/routage_codex.py` à partir de `harnais/modele_routage/routage_modele.py` ; `autotest` doit être VERT ;
   - lance sa veille en temps réel : `python3 codex-LOTS-html/routage_codex.py veille` (en arrière-plan, toute la session) ;
   - `python3 codex-LOTS-html/registre_ia.py pret codex` doit répondre « couple harnais + routage prêt ».
5. Seulement alors : `python3 codex-LOTS-html/registre_ia.py verifier codex LOT_018` doit répondre AUTORISÉ ; produis ce LOT au format V8 (modèle `harnais/modele_lecon/MODELE_DD_V8.html`), poste par poste, en consignant chaque passe (`routage_codex.py consigner …`). Ressources hors ligne : `ressources_ia/README.md`.
6. N'écris que dans `codex-LOTS-html/`. Pousse sur `codex/lots`. Ne fusionne jamais : seul Vial fusionne.
7. En fin de session : `python3 ressources_ia/outils/suivi_ia.py capture codex`, commit, push, puis dis-moi le LOT et le fichier en cours.
