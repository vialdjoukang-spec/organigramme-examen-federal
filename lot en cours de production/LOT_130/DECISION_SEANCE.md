# DECISION_SEANCE — LOT_130 — 9 novembre 2026, 18:10 Europe/Zurich

Décidé par : Vial, via la mission remise à l'agent A (consigne commune du 9 novembre 2026).
Consigné par : agent A, branche `agentA/lot-130-p1`.

Ressources du jour : dépôt local, harnais `controle_lot.py` (bande 100–200 Ko), prompt V0 rév. 9.11.2026 b (bande visée 100–150 Ko), sources ouvertes le 9 novembre 2026. Corpus XML `AipsDownload_20261008.xml` absent. Pas de pull request.

Découpage : Phase A et DX impairs sur cette branche. DX pairs réservés à l'autre agent sur `agentB/lot-130-p2`. Aucune écriture sur cette branche-là, ni sur `main`, ni dans `harnais/`, ni dans `LOT_Claude_Finaux/`.

| Producteur | Rôle du jour | Fichiers | Branche |
|------------|--------------|----------|---------|
| Agent A | Rédacteur Phase A et DX impairs | Phase A, DX.1, DX.3, DX.5, DX.7, DX.9 | agentA/lot-130-p1 |
| Agent B | Rédacteur DX pairs | DX.2, DX.4, DX.6, DX.8, DX.10 | agentB/lot-130-p2 |

Liste retenue, identique au gel du 9 novembre 2026 lu sur `agentB/lot-130` (commit 20722c68) : dix noms inchangés. Les fenêtres-gabarit de cette version (« part d'une cause ») ne sont pas reprises.

Écart au bracelet : RouteLLM, LiteLLM et Phoenix ont été suggérés. Ils ne sont pas installés et ne lisent pas les sources cliniques. À la place : lecture ciblée des extraits, cache dans `evidence/`, contrôle mécanique `controle_lot.py`.
