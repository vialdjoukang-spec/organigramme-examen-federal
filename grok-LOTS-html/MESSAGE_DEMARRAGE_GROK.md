# Message de démarrage — Grok (chantier LOTS)

Grok (Grokbot dans Cursor, avec ordinateur virtuel), voici ta mission. Dépôt GitHub `vialdjoukang-spec/organigramme-examen-federal`, branche de départ `production-v2`.

1. Lis en entier `grok-LOTS-html/PROMPT_GROK.md`, puis `grok-LOTS-html/DEMARRAGE.md`, puis la section 12 de `PROMPT_PRODUCTION_V2.md` (norme de format V8). Ils priment pour ce chantier sur `AGENTS.md` et `CLAUDE.md`.
2. Crée ta branche : `git fetch --all && git checkout -b grok/lots origin/production-v2`.
3. Registre (bloquant) : `python3 grok-LOTS-html/registre_ia.py lire grok`, puis `signer grok <jeton>`, puis `installer grok`.
4. **Couple [Harnais + Routage] (bloquant)**, section 9 de ton prompt :
   - crée `grok-LOTS-html/ROUTAGE_GROK.json` (table poste → tes propres modèles, auditeur médical ≠ rédacteur) à partir de `harnais/modele_routage/ROUTAGE_MODELE.json` ;
   - crée `grok-LOTS-html/routage_grok.py` à partir de `harnais/modele_routage/routage_modele.py` ; `autotest` doit être VERT ;
   - lance sa veille en temps réel : `python3 grok-LOTS-html/routage_grok.py veille` (en arrière-plan, toute la session) ;
   - `python3 grok-LOTS-html/registre_ia.py pret grok` doit répondre « couple harnais + routage prêt ».
5. Seulement alors : `python3 grok-LOTS-html/registre_ia.py verifier grok LOT_134` doit répondre AUTORISÉ ; produis ce LOT au format V8 (modèle `harnais/modele_lecon/MODELE_DD_V8.html`), poste par poste, en consignant chaque passe (`routage_grok.py consigner …`). Ressources hors ligne : `ressources_ia/README.md`.
6. N'écris que dans `grok-LOTS-html/`. Pousse sur `grok/lots`. Ne fusionne jamais : seul Vial fusionne.
7. En fin de session : `python3 ressources_ia/outils/suivi_ia.py capture grok`, commit, push, puis dis-moi le LOT et le fichier en cours.

Tu travailles dans Cursor avec ton ordinateur virtuel : exécute toi-même chaque commande dans ton terminal (git, Python 3), garde la veille du routage en arrière-plan toute la session, et pousse sur `grok/lots`. Si le push est refusé faute d'identifiants GitHub dans ton ordinateur virtuel, dis-le-moi au lieu de contourner.
