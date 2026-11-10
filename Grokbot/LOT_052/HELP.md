# HELP — LOT_052 — ce qui n'a pas été ouvert ou reste limité

Mise à jour : 2026-11-10, correction de la Phase A.

- Antibiotiques : aucune information professionnelle suisse d'antibiotique n'a été rapatriée. La Phase A ne donne ni molécule ni milligramme ; elle renvoie le choix à l'hôpital.
- Morphine et autres opiacés : aucun texte AIPS ouvert. La Phase A recommande l'analgésie précoce (RMS 2006, grade B) sans écrire de dose.
- Métamizole : l'information professionnelle Novalgin® solution injectable (Swissmedic 16950, mise à jour septembre 2025) a été ouverte ; extrait dans `_travail/evidence/aips-16950.txt`.
- Zahnd, Revue médicale suisse 2024 : seul le résumé public a été lu ; seuls ses chiffres sont cités.
- Forum Médical Suisse 2021 (Sinz) : texte repris depuis le rendu déjà obtenu ; licence CC BY-NC-ND, faits cités, figures non reproduites.
- RMS 2010 (référer aux urgences) : les tableaux 1, 2 et la figure 2 sont des images ; leur transcription est dans `_travail/evidence/rms_referer_2010_tableaux.txt`.
- IASP : le site bloque curl ; la page a été lue par un autre moyen de lecture web et l'extrait conservé dans `_travail/evidence/iasp_terminologie.txt`.
- Images : la paire brute / annotée de la Phase A utilise le cliché de Bill Rhodes (CC BY 2.0), sans mention de l'auteur hormis le repère L. Le second cliché (Cerevisae, CC BY-SA 4.0) porte déjà les mentions anglaises de l'auteur : il est présenté comme tel, pas comme cliché brut.
- L'échographie titrée « Appendicitis ultrasound » (62343b66aacf7581.png) a été refusée après inspection (vésicule lithiasique) et retirée du dépôt.
- Aucun cliché libre d'ischémie mésentérique (E1) sans mention imprimée n'a été obtenu.
- Catalogue de cas (liens seulement, aucune copie) : Radiopaedia, Radiology Assistant, Eurorad, Ultrasound Cases, Casimage.
- Passage fix052b : StatPearls « Embryology, Bowel » (NBK545247) refuse curl et la lecture web ; la limite embryologique est sourcée par TeachMeAnatomy (extrait dans `_travail/evidence/teachmeanatomy_ams.txt`). À remplacer par une source suisse ou un manuel si l'audit l'exige.
- Aucun extrait ne soutient Buscopan® en aigu ; il n'est pas cité.
- L'échographie d'AAA n'a pas d'échelle : aucun diamètre n'est donné.
- Passage fix052c : aucun extrait accessible de Larsen, Moore ou Langman n'a été trouvé. L'embryologie reste sourcée par TeachMeAnatomy, une citation par phrase : artère mésentérique supérieure, artère mésentérique inférieure et canal anal (ligne pectinée).
- Aucun extrait ne donne l'admission LAMal de la morphine ; rien n'est affirmé.
- Le seuil de l'AAA vient de deux articles de la Revue médicale suisse (2012, 2004), pas de l'ESC.
- Passage fix052d : l'AIPS de la morphine (51039) est lue sur arzneimittelinfo.ch, miroir de l'AIPS ; swissmedicinfo.ch exige JavaScript. Les contre-indications sont dans `_travail/evidence/morphine_51039.txt`.
- LAMal : ODDB et le portail de la liste des spécialités bloquent curl. La quote-part de 10 % et la mention LS viennent de compendium.ch (`_travail/evidence/compendium_morphine.txt`).
- Valeurs de référence : PDF du CHUV, extrait dans `_travail/evidence/chuv_valeurs_reference.txt`. La ligne de la lipase garde ses espaces multiples, sinon `controle3.py` lit « 13 60 » comme 1360.
- GEU : aucune version libre sans légende de l'image n'existe (seulement un SVG et une variante arménienne, légendés) ; la fiche 2 le dit dans le titre de l'image brute.
- `verif.py` exclut les citations entre guillemets « … » du contrôle des copies de 8 mots.
