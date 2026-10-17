---
name: ssp-posologie-suisse
description: >-
  Lis ce skill dès qu’un texte mentionne un médicament ou une dose : chaque dose
  renvoie à l’information professionnelle suisse en vigueur, extraite mot pour mot
  ou lue à la main, relue contre l’extrait et datée.
---
# But
Ce skill garantit que chaque dose renvoie à un texte suisse daté et validé par un humain.
# Déclencheur
Tu l’appliques dès qu’un texte mentionne un médicament, une dose, une voie ou un intervalle.
# Étapes
1. Tu vérifies la dose dans l’information professionnelle suisse (AIPS, swissmedicinfo.ch) du produit exact. L’extraction par script du texte AIPS officiel (téléchargement Swissmedic/Refdata, export autorisé) est permise : rubrique copiée mot pour mot, chaque ligne de dose relue à la main contre l’extrait (méthode approuvée par Vial le 17.10.2026).
2. Le Compendium se consulte à la main seulement, pour le produit exact ; tu notes la date de lecture.
3. Tu cites la source, la rubrique et la date à côté de la dose.
4. Une dose sans source suisse lue devient « À vérifier » et ouvre un ticket.
5. La dose reste marquée non validée tant qu’un médecin ne l’a pas confirmée.
# Interdits
Tu n’automatises jamais la lecture du Compendium, et tu ne contournes ni robots.txt ni les conditions d’un site.
# Règle universelle
Le projet cible doit avoir un résultat de HAUTE QUALITÉ. L’usage des jetons doit être raisonnable et optimisé, et tout gaspillage est formellement interdit. L’économie de jetons est autorisée si et seulement si elle ne dégrade pas la qualité du travail.
