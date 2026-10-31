# ADR-003 — Pas de regroupement des DD (1 fichier = 1 run) (2026-10-31) — [Accueil](../00_ACCUEIL.md)

**Contexte.** Regrouper les DD économise le démarrage et le paquet, mais chaque DD V8 pèse ≈ 56 000 jetons de sortie (178 Ko de HTML, mesure) : le contexte porté grossit à chaque DD ajouté et les erreurs se corrèlent.
**Résultat de la simulation** (`etude/resultats.json`, HYPOTHÈSES de coût, E[C] en forme close) : 2 DD par run = +0,89 u/LOT (+4,5 %) ; 5 DD = +4,9 u ; 10 DD = +12,0 u. Conformité 2 par run = +0,32 u/LOT. Le regroupement à 2 DD ne devient rentable que si le surcoût de tours par DD ajouté (τ_k) tombe sous ≈ 0,35 (hypothèse : 0,6) ou si le démarrage d'un run dépasse ≈ 194 000 jetons (hypothèse : 15 000).
**Décision.** 1 DD par run en rédaction, 1 fichier par run en audit médical ET en conformité. Le regroupement reste hors de S2.
**Conséquences.** Révisable : si `couts.py bilan` montre un démarrage de run mesuré > 190 000 jetons, refaire la simulation avec les valeurs réelles.
