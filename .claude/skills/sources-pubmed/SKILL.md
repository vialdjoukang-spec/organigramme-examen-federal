---
name: sources-pubmed
description: Lis ce skill avant de citer une source : PubMed (script ou MCP), Suisse d'abord, chiffre retrouvé dans la source, jamais d'URL déduite.
---
`python3 harnais/pubmed.py chercher "<requête>" 8` puis `verifier <PMID>` ; MCP : mcp__PubMed__search_articles / get_article_metadata / lookup_article_by_citation. Une citation [Sn] liste le titre, la revue, l'année, PMID ou URL réellement ouverte et la date de lecture ; le chiffre cité doit figurer dans le résumé ou la page (contrôlé par `harnais/controle_sources.py`). Ordre : Suisse (OFSP, OFS, Obsan, sociétés suisses), Europe, international. Liste : harnais/SOURCES_AUTORISEES.md.
