# Décision de séance — LOT_103

- Date : 2026-11-15, Europe/Zurich.
- SSP : S7.9 Troubles de la sensibilité.
- Branche : `grok/lot-103-l1`, créée depuis `origin/main`.
- Rôle : Phase A seulement. Liste non gelée.
- La Phase A V0 (hors bande, point 1 « Définition et sémantique ») est remplacée par `LOT_103_Phase_A_V0.html`.
- La liste V0 est révisée : la SEP, l'ischémie cérébrale sensitive et le Guillain-Barré entrent ; l'alcool est séparé de la chimiothérapie ; la vasculite passe en E4.
- Sources lues ce jour : IASP (taxonomie 2011), Obsan/OFS (diabète 2022, attaques 2023 et 2019-2023), Société suisse de la SEP (27.01.2024), Atroshi 1999 (population suédoise), European Journal of Neurology 2024 (Espagne), fiche EAN sur l'incidence britannique 2016-2019, OpenStax CC BY 4.0. Les extraits RMS 2015 et 2019 et le cours de Liège étaient déjà dans le dossier.
- Corpus AIPS absent : aucune dose en milligrammes.
- Contrôle après correction 1 (audit médical 1, 9c87e815) : `controle3.py --script-ok` VERT ; `verif_aips.py` OK ; `aips_fiche.py verifier` 0 ; `abreviations.py` 0 ; `restaurer_fond.py --verifier` 0. Liste non gelée.
- Les scripts `gen_phase_a.py` et `phrases_suite.py` sont retirés. Le « car » mécanique ne sert plus de connecteur.
