# Harnais + Bracelet — circuit proposé v4

**État : architecture documentée dans l’atlas ; les briques nouvelles sont à tester avant d’être imposées aux productions.** Le harnais existant dans `/workspace/grok/repo/` n’a pas été modifié.

## Ordre d’exécution

1. Geler la tâche, les fichiers permis, le budget et les critères d’arrêt.
2. Appeler le Bracelet : choisir **1 à 3 outils**, jamais tout le catalogue.
3. Relire seulement l’index du cerveau secondaire, puis extraire les sources utiles.
4. Exécuter les tests déterministes et les caches (0 token).
5. Faire un essai local avec Ollama ou llama.cpp si la tâche est simple.
6. Escalader vers un modèle expert uniquement sur défaut mesuré ou décision difficile.
7. Contrôler structure, sources, interactions et captures ; consigner le résultat.
8. Demander une validation humaine pour les actions sensibles et le fond médical.

## Outils ajoutés à l’essai, sources vérifiables

- **Ollama** — https://github.com/ollama/ollama : servir des modèles ouverts localement.
- **llama.cpp** — https://github.com/ggml-org/llama.cpp : inférence locale en C/C++.
- **OpenCode** — https://github.com/anomalyco/opencode : agent de codage open source, à isoler et tester.
- **Promptfoo** — https://github.com/promptfoo/promptfoo : évaluations, assertions et intégration CI.

Les publications X servent de pistes, jamais de preuve de performance. Les chiffres de l’atlas sont des estimations ; 99–100 % est une cible d’appels payants évités, pas une promesse de coût total ni de qualité.
