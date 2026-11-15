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
- Correction 2 après l'audit médical 2 (c0a2a8f2, 75/100, 0 C, 3 G, 5 m). Le rapport est versé tel quel dans `audits/AUDIT_PHASE_A_2.md`. Liste non gelée. Pas de PR. Le rédacteur ne s'auto-audite pas.
- Correction 3 après l'audit médical 3 (23fe9596, 68/100, 0 C, 5 G, 4 m). Le rapport est versé tel quel dans `audits/AUDIT_PHASE_A_3.md`. Liste non gelée. Pas de PR. Le quatrième audit doit être fait par un auditeur neuf.
- Correction 4 après l'audit médical 4 (0efce002, 82/100, 0 C, 3 G, 5 m). Le rapport est versé tel quel dans `audits/AUDIT_PHASE_A_4.md`. Liste non gelée. Pas de PR. Le rédacteur ne s'auto-audite pas.
- Correction 5 après l'audit médical 5 (08c7a58b, 79/100, 1 C, 1 G, 3 m). Le rapport est versé tel quel dans `audits/AUDIT_PHASE_A_5.md`. C1 : réponse « Oui ». G1 : IRM cervicale si le signe de moelle est cervical ; la revue de 2015 ne décrit pas un niveau sous le cou. m1 : Campylobacter sous Keddie. m2 : Hughes supérieur à 4, ou ventilation qui approche. m3 : liens Eurorad, sans dessin nouveau. Liste non gelée. Pas de PR.
- Correction 6 après l'audit médical 6 (d9dd846f, 96/100, 0 C, 1 G, 2 m). Le rapport est versé tel quel dans `audits/AUDIT_PHASE_A_6.md`. G1 : grade de Hughes supérieur à 4, mEGRIS d'au moins 3, ou mEGOS à 4. m1 : l'aréflexie achilléenne ne suffit pas seule. m2 : les trois questions du point 14 ne sont plus répétées dans le tableau. La ligne EAN du point 11 reste. Liste non gelée. Pas de PR.
