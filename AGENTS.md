# Lecture obligatoire : lis CONTINUATION.md en entier, puis exécute l'Étape 0 avant tout

Ordre de Vial, pour Codex et tout agent IA :

1. Lis **`PROCHAINE_ACTION.md`** (ordre de relance écrit par la veille) et `python3 tools/porte.py etat`.
2. Lis **`CONTINUATION.md` en entier** : feuille de route Étape 0 → Étape 17, règles R1–R15, état, outils.
3. Tant que `python3 tools/porte.py verifier0` n'est pas vert, **tu ne fais que l'Étape 0** (catalogue, propose_skills, veille de relance, droits de fusion). `python3 tools/porte.py commencer N` refuse sinon.
4. **Début de session : affiche `python tools/garde/checkpoint.py --inventaire`** (automates actifs) ; chaque PR contient une section « Automates actifs ». Travaille sur l'étape courante seulement ; à la fin : `python3 tools/porte.py terminer`. La veille permanente est GitHub Actions (`garde-progres.yml`, 10 min, `@codex` sur la PR « Pilote Codex ») : « Codex doit être libre, indépendant de tout PC ». `tools/veille_relance.sh` est facultatif.
4 bis. **R15 Garde-fous** : un relevé seul ne termine jamais une étape en boucle ; rédige du contenu. Décision de Vial requise → étiquette `attente-vial` (il reçoit un courriel) et continue ailleurs, sans jamais attendre.
5. Ne t'arrête jamais devant un obstacle : consigne-le (`journal/echecs_fusion.md`, ETAT.md) et continue.

Règles minimales, même si tu ne lis rien d'autre : sources suisses/européennes lues et datées, sinon « À vérifier » ; doses AIPS suisse seulement (jamais le Compendium) ; audit agressif derrière chaque lot avant `audit-ok` ; fusion par commit de fusion après CI verte ; ne jamais modifier `/workspace/ssp/app.html` ; aucune donnée personnelle dans ce dépôt public ; tâches répétitives avec GPT 6 Luna ; concision.

Ordre actualisé de Vial : reprendre le découpage d’origine de CONTINUATION.md, sans protocole Gardien v1.0 ni passage obligatoire par fin.py. Ce script reste disponible comme outil facultatif. La sentinelle assiste la reprise ; les preuves de travail restent les lots de contenu audités et intégrés.

Ordre Vial actualisé : veille active toutes les10min, étape9 prioritaire et étape8 liée via tools/coordination. Recherches espacées, reprise des PR actives, temporisations distinctes des notifications ; voir docs/coordination-8-9.md. Après les tâches d’outillage, reprendre le lot clinique conservé.
