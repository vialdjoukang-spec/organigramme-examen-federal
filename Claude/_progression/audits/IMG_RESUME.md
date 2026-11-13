# Imagerie (EX-2) : résumé des verdicts, 13.11.2026

Source : `Claude/_progression/audits/img_*.audit.json`, champ `verification_1` (vérification indépendante de chaque groupe).
Les 10 groupes (53 fiches) portent audit-ok. Les 107 restants de l'audit sont levés ; la vérification signale encore
23 points mineurs (21 mineures, 2 notes), qui ne bloquent pas l'audit-ok mais restent à lever par un correcteur.

| Groupe | Fiches | Restants de l'audit | Verdict (vérification) | Restants mineurs après vérification |
|---|---|---|---|---|
| S1 | 5 | 7 | audit-ok (v1) | 1 (échographie transfontanellaire : grade III exige distension ET corne > 6 mm) |
| S2/S10 | 7 | 11 | audit-ok (v1) | 3 (Lugano : hausse absolue depuis le nadir ; EPOS 2020 : macrolide au long cours ; TEP-TDM : cote 3 redondante) |
| S3 | 5 | 8 | audit-ok (v1) | 2 notes (passerelle Stanford ; ESC 2024, ESVS 2024, ESC 2023 non mis en cache) |
| S4 | 6 | 13 | audit-ok (v1) | 2 (angio-TDM : 5 mSv répété ; haut risque ESC 2019 incomplet) |
| S5 | 5 | 12 | audit-ok (v1) | 3 (CA 19-9 « indications relatives » Gut 2018 ; BSG INR < 2,0 ; SSG Choosing Wisely) |
| S6 | 5 | 11 | audit-ok (v1) | 2 (passerelle Prélèvement vers cytologie urinaire ; source du 9,9 mL sus-pubien) |
| S7 | 4 | 9 | audit-ok (v1) | 4 (brochure Unisanté 2026.10 : 43 et 7 cas, mention « version antérieure » ; EUSOBI 2024 risque intermédiaire ; cible Prélèvement de l'outil) |
| S8 | 5 | 11 | audit-ok (v1) | 2 (règle de grossesse EANM 2021 étendue ; phrase alourdie) |
| S9 | 6 | 13 | audit-ok (v1) | 4 (HUG 2023 pour l'œdème STIR ; « tard » absent de HUG 2021 ; « tiers des cas » HUG 2019 ; redondance) |
| S11/T | 5 | 12 | audit-ok (v1) | 0 |

Assemblage du 13.11.2026 : controle.py VERT (409 fiches, 918 passerelles). La page `receptacle.py --audites 1-32`
ouvre la fiche EX-2-S4-angio-tdm-thoracique (Temps 1, 2 et 3 affichés, aucune case « — ») avec 0 erreur console
et sans défilement horizontal à 1280 et 390 px, parce que les polices `Claude/_polices` sont servies à côté de la page.
Capture : `Claude/_progression/captures/img_fiche_1280.png`.

Outil partagé : `charpente.py` écrit encore 1 fiche, car il ajoute à EX-2-S7-biopsie-guidee-sein une passerelle
« Prélèvement » vers EX-4-S7-frottis-cervico-uterin ; l'écriture a été annulée et le besoin revient au responsable de l'outil.
