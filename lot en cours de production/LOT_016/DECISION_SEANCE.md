# DECISION_SEANCE — LOT_016 — 2026-10-30 10:18 Europe/Zurich
Décidé par : Vial (ordre écrit du 30.10.2026, chantier `production-v2`), consigné par le chef de production (session principale Claude Code)
SSP : G16 — Perte de poids, perte d’appétit | weight loss, loss of appetite — LOT VIDE (dossier d'archive vide) → fabrication complète
Nature : SSP clinique : 10 causes ou diagnostics différentiels de la perte de poids et de la perte d’appétit, gravité explicite (Prompt V0 §9)
Ressources du jour : sous-agents Claude Code (`.claude/agents/`), corpus AIPS local `.cache/aips/AipsDownload_20261008.xml`, accès web via proxy
Découpage Phase B : fixe — 10 fichiers, un par DD (DX.1 → DX.10), bande 80–150 Ko, fenêtres `popover`
| Producteur | Rôle du jour | Fichiers | Branche |
|------------|--------------|----------|---------|
| redacteur-phase-a (opus, xhigh) | Rédacteur | Phase A + liste provisoire | production-v2 |
| redacteur ×10 (opus, xhigh), en parallèle après gel de la liste | Rédacteur | B DX.1 … DX.10 (un fichier par agent) | production-v2 |
| auditeur-medical (opus, xhigh) | Auditeur médical, corrige en place, gèle la liste | chaque fichier, en premier | production-v2 |
| auditeur-conformite (sonnet, high) | Auditeur conformité, corrige en place | chaque fichier, en second | production-v2 |
Commit et push par la session principale après chaque fichier (P12). Aucun refus (Prompt V0 §16.1).
Changement en cours de journée : uniquement sur nouvel ordre de Vial, consigné ici.
