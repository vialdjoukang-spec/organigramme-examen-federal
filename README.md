# Organigramme · Examen fédéral

Cette application sert à préparer l’examen fédéral de médecine humaine : calendrier, 248 SSP avec leurs notions CK, fenêtres d’information au survol et au clic, catalogue des gestes d’examen (CS), mémorisation, calculs et exigences.

- **Application en ligne :** https://vialdjoukang-spec.github.io/organigramme-examen-federal/
- **Fichier de travail :** `app_v2.html` (un seul fichier, utilisable aussi hors ligne).
- **Référence en lecture seule :** `orig/app.html`, dont la CI contrôle l’empreinte.

La progression (coches, séances, réglages) reste enregistrée dans le navigateur de chaque utilisateur ; elle n’est jamais envoyée dans ce dépôt.

## Organisation

| Chemin | Contenu | Agent |
|---|---|---|
| `app_v2.html` | fichier de travail publié par Pages | tous, par patch ciblé |
| `orig/app.html` | copie de référence | personne |
| `data/` | constantes extraites (EXI, SESSION, MEM, TIP) | agent du chantier |
| `tools/` | scripts de patch, d’extraction et de garde | Héphaïstos |
| `tests/`, `qa/` | contrôles Playwright, gardes, rapports | Janus |
| `assets/cs/` | images cliniques réelles et `credits.json` | Asclépios |
| `veille/` | sources surveillées et empreintes | Argos |
| `journal/`, `HANDOFF.md`, `ETAT.md` | décisions, état, passation | Athéna |
| `skills/` | copie versionnée des procédures des agents | Athéna |
| `.github/` | CI, Pages, modèles de tickets | Héphaïstos |

## Règle universelle

Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.

## Avertissement

Les agents produisent et testent ; aucun contenu clinique ni aucune posologie n’est validé sans relecture humaine. Les posologies se vérifient dans l’information professionnelle suisse en vigueur.
