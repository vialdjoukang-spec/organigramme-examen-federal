# JOURNAL_DX3 — LOT_017 Phase B — DX.3 Accident vasculaire cérébral du tronc cérébral

30.10.2026, rédacteur Phase B (un seul fichier). Aucun score attribué.

## Fait
- Fichier écrit : `LOT_017_Phase_B_V0_DX.3.html` (14 points, 37 fenêtres popover, sources [S1]–[S48]).
- Extraits datés écrits : `evidence/DX3_E1` à `DX3_E7` (épidémiologie suisse, ESO thrombolyse/ténectéplase/occlusion basilaire/pression 2025, prévention secondaire, AIT, dysphagie, ELAN, AGLA, dépistage de la fibrillation auriculaire, circulation postérieure, anatomie oculomotrice du tronc, ESO 2025 vision, Fedlex LCR/OAC/LAI). S45, S46, S47, S48, S49, S50 et S51 de la Phase A ont leurs extraits dans DX3_E2 et DX3_E5.
- AIPS : `.cache/aips/69958.txt` créé (Metalyse 5000 U, ténectéplase 25 mg, AVC) ; compléments ajoutés à `48313.txt` (posologie de l'AVC, mécanisme), `51795`, `54509`, `54085`, `41529`, `44486` (mécanisme, SPARCL, CYP2C19). Numéros contrôlés dans la liste Swissmedic des conditionnements (30.09.2026) : 41529 = Trandate solution injectable, 41530 = comprimés ; 69958 = Metalyse 5000 U.

## Hypothèses et choix (à contrôler par l'audit)
- Antihypertenseur avant thrombolyse : l'ESO 2025 ne désigne aucun médicament ; Trandate® et Ebrantil® sont proposés d'après leurs AIPS (urgences hypertensives). Choix déduit des AIPS, écrit comme tel.
- Aspirine dans l'AVC constitué : l'AIPS Aspirine Cardio® nomme l'AIT ; la dose de 160–300 mg dans les 24–48 heures (revue d'Oxford) est signalée hors information professionnelle.
- Thrombolyse au-delà de 4,5 heures (occlusion basilaire, réveil avec décalage diffusion-FLAIR) : hors information professionnelle, écrit en clair.
- Critères de sortie : aucune source ; liste déduite et signalée comme telle.
- Calcul dérivé (≈ 1,9–2,4 AVC postérieurs avec diplopie / 100 000 / an) : populations différentes, présenté comme ordre de grandeur.
- Fenêtre « Urgence — conduite chronologique » : étapes ordonnées sans délais intermédiaires chiffrés (non trouvés).

## Contrôles
- `controle_lot.py verifier … --sans-nom --json` : aucune critique sur ce fichier.
- `audit_langue.py --json` : conforme ; avertissements restants = phrases longues et points-virgules dans les listes de contre-indications AIPS, espaces insécables (règle « aucune espace insécable », H17-14).
- Taille finale : 130 454 octets ; SHA-256 f89950dee3081405de451b81f1b6b67ab39536ad9a624694ee893d1f6b4daaa1 (30.10.2026). Au-dessus de la cible de 125 Ko, sous 135 Ko.
- Fichiers `.cache/aips/` existants (48313, 51795, 54509, 54085, 41529, 44486) : complément ajouté en fin de fichier, sans rien effacer.
