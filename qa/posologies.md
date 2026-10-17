# Posologies suisses de la phase NC-0 (table pour Vial)

Galien a lu ces doses à la main le 17.10.2026 dans l’information professionnelle suisse (AIPS, swissmedicinfo-pro.ch), une page par produit ; aucune extraction automatique du Compendium ni de Swissmedic n’a été faite. Les lignes vérifiées vivent dans `data/ck/doses_ch.json`. La contre-lecture indépendante par Asclépios reste à faire, car Galien n’audite pas son propre texte.

## Doses vérifiées dans l’AIPS (3)

| Identifiant | Produit | Dose | Voie | Population | Rubrique AIPS |
|---|---|---|---|---|---|
| `valaciclovir-po-adulte-zona` | Valtrex® comprimés pelliculés 250 mg et 500 mg (Swissmedic 53116) | 1000 mg 3×/j, 7 jours, à débuter au plus tard dans les 72 heures suivant l’éruption | PO | adulte, clairance de la créatinine ≥ 50 ml/min | Posologie/Mode d’emploi, zona y compris zona ophtalmique (information mise à jour en décembre 2025) |
| `valaciclovir-po-adulte-zona-ir` | Valtrex® comprimés pelliculés 250 mg et 500 mg (Swissmedic 53116) | clairance 30–49 ml/min : 1000 mg 2×/j ; 10–29 ml/min : 1000 mg 1×/j ; < 10 ml/min : 500 mg 1×/j, 7 jours | PO | adulte avec insuffisance rénale, zona | Posologie/Mode d’emploi, instructions posologiques particulières, insuffisance rénale (décembre 2025) |
| `prednisone-po-adulte-aigu` | Prednisone Streuli® comprimés sécables 5, 20 et 50 mg (Swissmedic 29349) | 15–30 mg/j | PO | adulte, maladie aiguë ne compromettant pas le pronostic vital | Posologie/Mode d’emploi (information mise à jour en juin 2026) : posologie initiale habituelle 5–60 mg/j ; réduction progressive si le traitement dépasse quelques jours ; seuil de Cushing 7,5 mg |

## Doses « À vérifier » (2), hors de doses_ch.json

Le schéma de doses_ch.json n’admet que des doses lues dans l’AIPS. Ces deux doses du protocole des HUG décrivent un usage hors étiquette ; elles restent ici, marquées **À vérifier**, jusqu’à la décision de Vial.

| Identifiant proposé | Substance, produit | Dose | Indication | Motif |
|---|---|---|---|---|
| `prednisone-po-adulte-bell` | prednisone, Prednisone Streuli® | 1 mg/kg/j PO pendant 7 jours, puis arrêt | paralysie de Bell (paralysie faciale périphérique idiopathique) | **À vérifier** : La dose vient du protocole des HUG (v1.2 du 04.04.2023, § 5 Traitement) ; l’information professionnelle de Prednisone Streuli® ne cite pas cette indication (usage hors étiquette). |
| `valaciclovir-po-adulte-bell-severe` | valaciclovir, Valtrex® | 1000 mg 3×/j PO pendant 7 jours | syndrome de Ramsay-Hunt (systématique) ; paralysie de Bell seulement si atteinte sévère (House-Brackmann IV–VI) ou arguments pour une infection à VZV | **À vérifier** : La dose et l’indication viennent du protocole des HUG (§ 5 Traitement) ; l’information professionnelle de Valtrex® ne cite que le zona ; Vial confirme si le syndrome de Ramsay-Hunt relève du zona de l’AIPS. |
