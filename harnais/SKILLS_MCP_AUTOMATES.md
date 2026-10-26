# HARNAIS — inventaire gratuit (scripts · automates · MCP · skills)

| Famille | Élément | Rôle |
|---|---|---|
| Prompt | `prompt_projet.py` (444, SHA-256) · `prompt_expert.py` | Mission en lecture seule · exigences du Prompt ULTIME extraites par rôle |
| Tâches | `tableau_taches.py` · `verrou.py` | Distribution atomique des fichiers (blocs de 5 chapitres) · non-collision |
| Sources | `aips_texte.py` (AIPS, Symbol µ/≥) · `pubmed.py` · `controle_sources.py` | Texte AIPS officiel · PubMed · chiffre retrouvé dans sa source (résumé, page, PDF) |
| Contrôles | `controle_lot.py` · `controle_medical.py` · `controle_langue.py` (LanguageTool + spaCy) · `auditeur_script.py` | Forme · médical d'ancrage · langue et phrases verbales · liens/DOI |
| Porte | `audit_lot.py` · `audit_sortie.py` · hook `pre-commit` | Audit du LOT · audit avant sortie : aucun commit hors seuil |
| Veille | `dispositif/veille.py` (1 s) · `sentinelle.py` · `dashboard.py` | Santé du Harnais · effectifs · direct (tokens, agents, jauges) |
| Mémoire | `rappel_memoire.py` + `rappel/G_data.py` · `LECONS/` (5 max) | Onglet Rappel mémoire · leçons par rôle |
| MCP | PubMed (search, metadata, citation) · GitHub (PR, CI, fusion) · Google Drive (archives, lecture) | Gratuits, déjà branchés |
| Skills du dépôt | ssp-verite · ssp-posologie-suisse · ssp-aips-verbatim · ssp-audit-medical · ssp-prevalences-automates | Règles de vérité, doses, prévalences |
| Skills Harnais | harnais-lot · controle-medical · controle-langue · sources-pubmed | Procédures des agents |
| Limite | Aucun script ne juge la justesse clinique ni la pertinence pédagogique | Il détecte l'invention, l'écart à la source, l'omission, la faute de langue |
