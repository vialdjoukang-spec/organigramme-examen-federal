# Références de rendu et outils récents — 6 novembre 2026

## Obsidian

- [Canvas — aide officielle](https://help.obsidian.md/plugins/canvas) : espace 2D ; cartes-texte, fichiers et groupes ; connexions orientées, étiquettes et flèches ; format `.canvas` JSON Canvas.
- [Graph view — aide officielle](https://help.obsidian.md/plugins/graph) : cercles pour les notes, traits pour les liens, tailles variables et forces de disposition.
- [JSON Canvas 1.0](https://jsoncanvas.org/spec/1.0/) : tableaux `nodes` et `edges`, positions et dimensions entières, `fromNode`, `toNode`, côtés et `toEnd: arrow`.

Conséquence : les 22 schémas Atelier gardent des cartes Markdown rectangulaires avec liens cubiques et flèches ; la vignette Graph conserve des cercles et traits. Un vrai vault lié et un `.canvas` conforme sont livrés dans `Vault_BacASable/`.

## Outils vérifiés sur GitHub et le web

- [Ollama](https://github.com/ollama/ollama) — serveur local de modèles ouverts.
- [llama.cpp](https://github.com/ggml-org/llama.cpp) — inférence C/C++ locale ; [tutoriel agent hors ligne](https://github.com/ggml-org/llama.cpp/discussions/14758).
- [OpenCode](https://github.com/anomalyco/opencode) — agent de codage open source ; une piste à tester en environnement borné.
- [Promptfoo](https://github.com/promptfoo/promptfoo) — tests de prompts, RAG et agents, assertions et CI.
- [Qwen3-Coder local — documentation Unsloth](https://unsloth.ai/docs/models/tutorials/qwen3-coder-how-to-run-locally) — exemples de déploiement local, à adapter au matériel.

## X : pistes publiques, non preuves

Lecture publique effectuée le 6 novembre 2026 :

- [Panoplie locale mentionnant Ollama, Open WebUI et LM Studio](https://x.com/swarogan/status/2114711685508354345), 26 octobre 2026 à 14:32 Europe/Zurich.
- [Retour d’usage OpenCode + Ollama insistant sur mémoire et temps](https://x.com/truefreedom84/status/2109633522809913547), 12 octobre 2026 à 14:13 Europe/Zurich.
- [OpenCode présenté comme agent local possible](https://x.com/thisdudelikesAI/status/2112479647468572950), 20 octobre 2026 à 11:42 Europe/Zurich.

Ces messages peuvent être promotionnels ou inexacts. Aucun chiffre de performance de l’atlas ne vient de X ; seuls les liens de projets ont été conservés pour vérification.

## Méthode des chiffres

Coût évité, performance, qualité et complexité sont des **estimations éditoriales** sur une échelle annoncée. « 0 € d’API » vaut uniquement pour les étapes 100 % scripts/local, hors matériel et électricité. Le circuit vise jusqu’à 99 % d’appels payants évités sur les flux répétitifs ; ce n’est ni une mesure ni une garantie de coût total. La référence reste un test avant/après sur le projet réel.
