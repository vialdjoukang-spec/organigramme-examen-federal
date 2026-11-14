# Audit V2 : anamnèse A-TRAME, A-SPE-1a à 1g, A-MOT-1 à 25

J'ai mené ce tour de vérification le 14.11.2026 sur CORRECTIONS_ANAMNESE_01_25.md. Je n'ai modifié aucune fiche, sans commit ni push.

## Méthode

J'ai d'abord rechargé les 33 JSON avec json.load : tous se chargent. J'ai ensuite relu les champs touchés par les patchs n° 1 à 22 et cherché toute trace résiduelle de « 72 h », de « déduction », de « 5e éd. » et de lettre d'hypothèse hors schéma. Enfin, j'ai vérifié Orfiril avec `aips_fiche.py trouve Orfiril`, puis `aips_fiche.py fiche <URL refdata>`.

## 1. Les corrections des patchs n° 1 à 10 tiennent

| # | Contrôle | Résultat |
|---|---|---|
| 1 | A-SPE-1f, PEP | Corrigé. La question porte sur les « 48 dernières heures » et la conduite fixe un début idéal dans les 4 heures, sans PEP après 48 heures. La source CFIST du 7.11.2025 est en place et aucun « 72 h » de PEP ne reste dans les 33 fiches. Le « 72 h » encore présent concerne le lévonorgestrel, ce qui est juste. |
| 2 | A-SPE-1d, AES | Corrigé et conforme à CFIST 2025. |
| 3 | A-SPE-1f et A-MOT-22, contraception d'urgence | Corrigé et conforme à IENK 2026 : DIU au cuivre et ulipristal jusqu'à 120 h, lévonorgestrel jusqu'à 72 h, seuil > 70 kg ou IMC > 26. |
| 4 | A-SPE-1b, développement | Le contenu est corrigé et conforme aux check-lists de la SSP. La correction introduit toutefois une **erreur nouvelle** de polarité (voir le n° V2-1). |
| 5 | A-MOT-23, ménopause | Corrigé. Le seuil reste honnêtement « à vérifier ». |
| 6 | A-MOT-22, OMS | Corrigé : la fiche cite le MEC 6e éd. (3.11.2025) en dernier recours, après IENK. |
| 7 | A-SPE-1c, question discriminante | Corrigé. |
| 8 | Lettres VITE DIT CAFé | Corrigé : la seule lettre hors schéma restante est celle de A-TRAME, qui décrit la méthode, comme prévu. |
| 9 | Ordre gravité puis fréquence | Corrigé dans MOT-8, 9, 13, 15 et 17 et dans A-SPE-1c. |
| 10 | A-SPE-1a, groupes A et T | Ajoutés avec l'étiquette « déduction ». |

Les patchs légers n° 11 à 20 et n° 22 sont aussi appliqués. J'ai vérifié Baveno VII, EAU, ESHRE, les SSP 182, 192 et 195, S-17 et S-26, la limite d'âge de 30 ans retirée et les âges 55 et 65 ans dans A-TRAME.

## 2. Patch 21 tranché : Orfiril

Le n° 43225 est confirmé par l'outil. `aips_fiche.py trouve Orfiril` renvoie : « 43225 · SmPC Orfiril® solution buvable · https://files.refdata.ch/simis-public-prod/MedicinalDocuments/8e83164d4e084d67b3e0f55b1beacf04-fr.html ». La commande `fiche` sur cette URL renvoie « N° 43225 · mise à jour : Septembre 2025 ». Les autres formes portent d'autres numéros : 54331 pour la solution injectable et 54268 pour Orfiril long. La fiche AIPS est désormais dans le cache de `aips_fiche.py`.

La phrase des fiches reprend le texte de l'AIPS sans l'adoucir : « Assurez-vous que les femmes en âge de procréer utilisent une méthode de contraception efficace pendant toute la durée du traitement. » **Le patch 21 est clos.**

## 3. Défauts restants ou nouveaux et patchs exacts

| # | Gravité | Fiche › champ | Extrait | PATCH exact |
|---|---|---|---|---|
| V2-1 | Moyen (erreur nouvelle) | A-SPE-1b › drapeaux_rouges[1] et [2] | question « À 18 mois (âge corrigé), marche-t-il seul ? » ; si_oui « Si la réponse est non, retard moteur… » | Le champ `si_oui` s'affiche quand la réponse est « oui ». Ici, il décrit la réponse « non » : l'affichage inverse donc le sens. [1] question → « À 18 mois (âge corrigé), ne marche-t-il toujours pas seul ? » ; si_oui → « Retard moteur : la check-list suisse de 18 mois attend une marche autonome, en avant et en arrière ; examen neurologique (S-33) et orientation spécialisée. » [2] question → « À 18 mois, dit-il moins de 10 mots ou ne réagit-il pas à son nom ? » ; si_oui → « Retard de langage ou trouble auditif : la check-list attend 10 à 20 mots à 18 mois et 20 à 50 mots à 24 mois ; demander une audiométrie et une évaluation du développement. » |
| V2-2 | Léger (même défaut) | A-SPE-1c › drapeaux_rouges[4].question | « Quel jour sommes-nous ? Où sommes-nous ? (observer…) » | Formuler une question qui déclenche le si_oui : « Se trompe-t-il sur le jour ou le lieu ? (demander : quel jour sommes-nous, où sommes-nous ; observer la vigilance et ses fluctuations) » |
| V2-3 | Léger (erreur nouvelle) | A-MOT-24 › pieges[3] | « …terme le 17.12.2026. ; soit environ DDR + 280 jours… » | Remplacer « 17.12.2026. ; soit » par « 17.12.2026, soit ». Les calculs restent justes : Naegele donne le 17.12.2026 et 10.03.2026 + 280 j donne le 15.12.2026, recalculé avec Python. |
| V2-4 | Léger | A-MOT-8 › hypotheses[1] et [2] | La torsion d'annexe figure dans « V — Gynéco-obstétrical » et dans « Tr/D — Obstructif et mécanique » | Dans [2], remplacer « torsion d'annexe ou testiculaire » par « torsion testiculaire ». |
| V2-5 | Léger | A-MOT-24 › drapeaux_rouges (valproate) | « Avis spécialisé urgent : ne pas arrêter brutalement un antiépileptique sans avis » | Ajouter : « L'AIPS Orfiril (n° 43225, sept. 2025) contre-indique le valproate “chez les femmes enceintes, sauf si aucune alternative thérapeutique ne rentre en ligne de compte et après avoir informé la patiente de manière détaillée sur les risques encourus”. » |
| V2-6 | Léger | A-MOT-4 et A-MOT-6 › si_oui | « Cardiopathie structurelle sévère ou coronarienne : critère de haut risque. » ; « Red flag HUG 2025 : bronchectasies, déficit immunitaire… » | Rendre ces phrases verbales. Exemples : « Une cardiopathie structurelle ou coronarienne sévère classe la syncope à haut risque : ECG et monitorage. » ; « Rechercher des bronchectasies, un déficit immunitaire ou une obstruction bronchique (red flag HUG 2025). » |

## 4. Verdict

**Publication : oui, sous réserve du patch V2-1.** Le seul défaut Grave, la PEP, est corrigé sans erreur nouvelle, et les neuf défauts Moyens sont corrigés. La correction du n° 4 a pourtant créé une inversion de sens dans A-SPE-1b (V2-1, Moyen) : elle doit être corrigée avant la publication. Les patchs V2-2 à V2-6 sont légers et ne bloquent pas la publication.

## Clôture
V2-1 et les légers V2-2 à V2-6 appliqués mot pour mot : **audit-ok** pour A-TRAME, A-SPE et A-MOT-1 à 25.
