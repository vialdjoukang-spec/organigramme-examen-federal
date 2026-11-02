#!/usr/bin/env python3
"""Bracelet d'optimisation — catalogue + suggestion d'outil (harness Grok Bot)."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

CATALOG = {
    "filtrage_nettoyage": [
        {"name": "Crawl4AI", "repo": "unclecode/crawl4ai", "use": "pages web → Markdown propre"},
        {"name": "Firecrawl", "repo": "firecrawl/firecrawl", "use": "collecte web Markdown/JSON ciblée"},
        {"name": "Chonkie", "repo": "feynic/chonkie", "use": "découper longs documents"},
        {"name": "FlagEmbedding", "repo": "FlagOpen/FlagEmbedding", "use": "rerank passages / preuves"},
        {"name": "LLMLingua", "repo": "microsoft/LLMLingua", "use": "compresser entrées longues"},
        {"name": "RTK", "repo": "rtk-ai/rtk", "use": "compresser sorties de commandes"},
    ],
    "memoire_persistante": [
        {"name": "Mem0", "repo": "mem0ai/mem0", "use": "faits persistants entre exécutions"},
        {"name": "Graphiti", "repo": "getzep/graphiti", "use": "graphe de faits évolutifs"},
    ],
    "reutilisation_cache": [
        {"name": "GPTCache", "repo": "zilliztech/GPTCache", "use": "cache réponses similaires"},
        {"name": "Portkey Gateway", "repo": "Portkey-AI/gateway", "use": "cache passerelle partagée"},
        {"name": "Prefect", "repo": "PrefectHQ/prefect", "use": "cache résultats de tâches workflow"},
        {"name": "requests-cache", "repo": "requests-cache/requests-cache", "use": "cache HTTP requests"},
        {"name": "Hishel", "repo": "karpetrosyan/hishel", "use": "cache HTTP + revalidation"},
    ],
    "planification_orchestration": [
        {"name": "APScheduler", "repo": "agronholm/apscheduler", "use": "planification légère Python"},
        {"name": "Celery", "repo": "celery/celery", "use": "jobs arrière-plan workers"},
    ],
    "protection_routage_observation": [
        {"name": "PyBreaker", "repo": "danielm/pybreaker", "use": "circuit breaker services foireux"},
        {"name": "LiteLLM", "repo": "BerriAI/litellm", "use": "budgets / tracking API"},
        {"name": "RouteLLM", "repo": "lm-sys/RouteLLM", "use": "router tâches simples → modèle cheap"},
        {"name": "Semantic Router", "repo": "aurelio-labs/semantic-router", "use": "routage local par embeddings"},
        {"name": "Phoenix", "repo": "Arize-ai/phoenix", "use": "traces / coûts / qualité"},
    ],
}

KEYWORDS = {
    "filtrage_nettoyage": r"crawl|scrape|web|html|markdown|page|document|pdf|long|chunk|compress|rerank|passage|log|shell|commande",
    "memoire_persistante": r"m[eé]moire|remember|fait|session|historique|graph|persist",
    "reutilisation_cache": r"cache|rejeu|identique|http|t[eé]l[eé]charg|workflow|pr[eé]fect|r[eé]utiliser",
    "planification_orchestration": r"cron|planif|schedule|queue|worker|batch|arri[eè]re.?plan",
    "protection_routage_observation": r"budget|token|co[uû]t|route|mod[eè]le|breaker|trace|observ|litellm|phoenix|fail",
}

ROOT = Path(__file__).resolve().parent


def suggest(task: str, top: int = 3) -> list[dict]:
    task_l = task.lower()
    scores: list[tuple[float, str, dict]] = []
    for cat, tools in CATALOG.items():
        kw = KEYWORDS.get(cat, "")
        cat_hit = 1.0 if (kw and re.search(kw, task_l, re.I)) else 0.2
        for t in tools:
            blob = f"{t['name']} {t['repo']} {t['use']}".lower()
            name_hit = 2.0 if t["name"].lower() in task_l else 0.0
            word_hits = sum(1 for w in re.findall(r"[a-zàâäéèêëïîôùûüç0-9]{4,}", task_l) if w in blob)
            score = cat_hit + name_hit + 0.3 * word_hits
            scores.append((score, cat, t))
    scores.sort(key=lambda x: (-x[0], x[1], x[2]["name"]))
    out = []
    seen = set()
    for score, cat, t in scores:
        key = t["repo"]
        if key in seen:
            continue
        seen.add(key)
        out.append({"category": cat, "score": round(score, 2), **t})
        if len(out) >= top:
            break
    return out


def main(argv: list[str]) -> int:
    if len(argv) >= 2 and argv[1] in ("--dump", "dump"):
        print(json.dumps(CATALOG, ensure_ascii=False, indent=2))
        return 0
    task = " ".join(argv[1:]) if len(argv) > 1 else ""
    if not task:
        print("usage: bracelet_suggest.py <description de tâche> | --dump", file=sys.stderr)
        return 2
    for i, s in enumerate(suggest(task), 1):
        print(f"{i}. [{s['category']}] {s['name']} ({s['repo']}) — {s['use']}  score={s['score']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
