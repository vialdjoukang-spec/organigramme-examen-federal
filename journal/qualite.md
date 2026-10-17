# Journal · Qualité, régression et point de vérité · Janus

Chaque entrée porte une date (Europe/Zurich), une décision et les sources lues. Aucune donnée personnelle n’entre dans ce journal public.

- 17.10.2026 · La référence verte compte 43/43 contrôles Playwright (19 ordinateur, 19 mobile, 5 complémentaires) sans erreur de console, et 5/5 tests des gardes (qa/reference-verte.md).
- 17.10.2026 · Les contrôles de test_tip.py et de test_extra.py sont inchangés ; seuls les chemins passent par APP_FILE, CHROME_PATH et SHOTS_DIR.
- 17.10.2026 · tests/run_tests.py fixe les valeurs attendues : booléens vrais, aria-expanded « true », overflow-y « auto », fenêtre de taille non nulle.
