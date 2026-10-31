# Reprise LOTS — 31.10.2026

Branche `codex/lots` ; écritures uniquement dans `codex-LOTS-html/`. Borne fraîchement vérifiée : LOT_133. Ne pas reprendre LOT_018. LOT_033 terminé au commit `eb08d21a`. LOT_034 terminé en production : 11 HTML, 154 questions, 275/275 contrôles V8, 20 citations AIPS et quatre groupes de corrections réelles ; commit en préparation.

Nouvel ordre explicite de Vial : deux lots en parallèle. LOT_034 est produit par la session principale et LOT_035 par l’agent `/root/lot035`, qui écrit exclusivement dans son dossier. Ses onze HTML sont rédigés, mais sa relecture et ses contrôles sont encore en cours. Ne pas ouvrir LOT_036 avant la clôture du LOT_035. Le coordinateur détient le verrou global : ne pas lancer un producteur concurrent. Vérifier `ETAT_CONTINUITE.json` et l’activité réelle avant toute reprise.

Aucun audit indépendant, score, test navigateur ou validation clinique. Modèle confirmé par Vial : GPT-6 Astra, ultra ; high recommandé, réglage non modifié. Les veilles locales du contrat et du routage tournent chaque minute tant que l’environnement existe ; elles ne rédigent pas. L’automate existant reste inchangé.

`ETAT_DES_LIEUX.html` reste l’instantané des 170 HTML précédant les dernières leçons du LOT_033. Il n’est pas actualisé automatiquement. Les preuves finales de chaque lot donnent l’état plus récent.
