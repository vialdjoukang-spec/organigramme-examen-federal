# JOURNAL_DX4 — LOT_017 — Phase B DX.4 Myasthénie oculaire et généralisée

Rédacteur Phase B, 30.10.2026 (Europe/Zurich). Fichier : `LOT_017_Phase_B_V0_DX.4.html`.

## Ce qui a été fait
- Lecture : LECONS_LOT_016, LECONS_LOT_015, LISTE_DX_CANONIQUE (titre repris mot pour mot), CORRECTIONS_AUDIT (corrections 1–16), evidence/INDEX, HELP, Prompt V0 §10–14 et §23, Phase A points 1–3 et lignes DX.4.
- Sources nouvelles lues en texte intégral (Europe PMC) : DGN 2023 (passages supplémentaires), Evoli 2020, Handzic 2026 (USZ), Grimm 2025 (USZ), Vissing 2026 (Delphi européen), Stetefeld 2019 (SOP crise), Dresser 2021 (S52), anatomie S47–S51 et S48 ; résumés : ABN 2025, Neumann 2020.
- AIPS relues dans le corpus local puis documents liés : Mestinon 19943, Prednisone Streuli 29349, Solu-MEDROL 35112, Imurek 31887, Privigen 58314, Soliris 59282, Ultomiris 67278, Vyvgart 69286/69725, Zilbrysq 69066, Rystiggo 69227, Atropinum Sintetica 56533, MabThera 54378, et 14 AIPS qui citent la myasthénie (magnésium, benzodiazépines, zolpidem, hydroxychloroquine, ciprofloxacine, macrolides, Botox, Keytruda). Kiovig, Octagam 10 %, Intratect : myasthénie absente des indications.
- Caches AIPS créés : `.cache/aips/59282.txt`, `67278.txt`, `69286.txt`, `69725.txt`, `69066.txt`, `69227.txt`, `56533.txt` (aucun cache existant modifié).
- Liste Swissmedic au 30.09.2026 relue par script : 19943 = Mestinon dragées 60 mg, 19945 = comprimés 10 mg, 56387 = retard ; ni édrophonium ni néostigmine seule. La LS (API OFSP) confirme 19943/19945.
- Extraits datés : `evidence/DX4_*.txt` (15 fichiers).
- Contrôles : `controle_lot.py verifier --sans-nom --json` → 0 critique, 0 avertissement pour DX.4 ; `audit_langue.py` → 0 critique ; avertissements restants : sigles des auteurs dans les Sources, énumérations à points-virgules, espaces insécables absentes (leçon 11 de LOT_015). Taille finale : environ 133 Ko.

## Hypothèses et choix
- Ordre E propre à la démarche de DX.4 (point 4) : crise imminente d'abord, puis III compressif, AVC du tronc, botulisme, Miller Fisher ; il ne remplace pas les rangs E de la Phase A (rappelés dans l'en-tête).
- Prednisone, azathioprine, IgIV, rituximab : usage hors information professionnelle en Suisse (indications AIPS lues), écrit en clair. L'azathioprine n'a pas la myasthénie dans l'AIPS Imurek (contrairement à l'Allemagne selon la DGN).
- Divergence corticothérapie : EFNS/ENS 2014 (un jour sur deux) contre ABN 2025 (quotidienne) ; la source la plus récente prime.
- Coûts : calculs dérivés recalculés par script à partir des prix publics LS (Soliris 1200 mg = 15 532,80 CHF ; 26 perfusions = 403 852,80 CHF ; IgIV 140 g = 10 244,85 CHF).
- Déductions signalées comme telles : pupille épargnée (muscles striés), réflexes conservés (marge de sécurité), pause de pyridostigmine et sécrétions, critères de sortie 6 (liste des médicaments, rendez-vous).
- Taille au-dessus de la cible 110–125 Ko mais sous le seuil de 135 Ko du brief ; densité conservée (point 11 = environ 46 Ko pour 9 classes de médicaments avec AIPS mot pour mot).
