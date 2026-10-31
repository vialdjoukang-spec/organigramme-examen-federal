# Pièges et leçons (mémoire persistante) — retour à [00 Accueil](00_ACCUEIL.md)

Format : `P-xx` · symptôme · cause · parade (outil ou règle) · preuve. Ajouter en tête, ne jamais supprimer sans ADR.

**P-01 · Faux critiques du harnais sur le format V8.** Symptôme : `audit_langue.py` et `controle_lot.py` signalent « title= interdit », « bande 80–150 Ko », « externe », « h2 », « h3_14 », « section Sources absente » sur des fichiers V8 corrects. Cause : outils écrits pour le format V0 ; le modèle validé `MODELE_DD_V8.html` déclenche les mêmes codes (mesure du 31.10.2026 : title 653, bande 1, externe 1, h2 1, h3_14 1 ; `controle_lot verifier LOTS_V8/LOT_016` = 66 critiques). Parade : ne jamais « corriger » ces codes (retirer `<abbr title>` casserait V8) ; passer par `outils/porte_zero_jeton.py`, qui ne signale que les codes absents du modèle validé. Harnais immuable : ne pas le modifier.

**P-02 · Plafond de taille mal lu.** Le plafond vise x (texte de la fiche : DD ≤ 9 Ko, Phase A ≤ 100 Ko), pas les octets du fichier HTML (médiane V8 : 178 Ko). Parade : `harnais/taille_xy.py <fichier>` ; la porte lit « T = x Ko (+ y Ko) ».

**P-03 · On déplace, on ne compresse jamais.** Pour réduire x : passer le détail en fenêtre ou sous-fenêtre. Une version réduite repasse un second audit médical (PROMPT_PRODUCTION_V2 §12). Parade : corriger la taille AVANT l'audit médical (la porte le force), pas après.

**P-04 · FIN_FICHIER.** Dernière ligne du fichier : `<!-- FIN_FICHIER LOT_XXX_… -->`. Absent = fichier tronqué. Parade : la porte vérifie la dernière ligne non vide.

**P-05 · Titre du DD.** `<h1>`/titre = nom exact de `LISTE_DX_CANONIQUE.md` (gelée après l'audit médical de la Phase A). Parade : copier le nom mot pour mot.

**P-06 · Citations AIPS.** Dose, contre-indications, grossesse, allaitement, enfant : citées mot pour mot, sans adoucir. Mesure LOT_016 : 850 citations « … » sur 908 (93,6 %) se retrouvent mot pour mot dans `evidence/` + `ressources_ia/aips/extraits/`. Parade : la porte liste les citations non retrouvées ; l'auditeur médical les vérifie en premier. Toute citation doit avoir son extrait daté dans `evidence/`.

**P-07 · Dose hors information professionnelle suisse.** Cas réel (commit LOT_011 DX.3) : « doses prégabaline Cl cr < 30 retirées (contraires à l'AIPS) ». Parade : `ressources_ia/outils/aips.py lire <numéro> <motif>` avant d'écrire une dose ; hors AIPS = écrit en clair.

**P-08 · Où vont les corrections (LOT_013 à 016, 3 794 lignes).** langue 57 % · omission 12 % · source 10 % · critère 7 % · conduite 5 % · dose 4 % · format 3,5 % · seuil 2 %. Leçon : plus de la moitié des corrections est de la langue ; `audit_langue.py --corriger` (sur copie) règle les espaces insécables avant tout modèle.

**P-09 · Indépendance.** Un auditeur n'audite jamais ce qu'il a rédigé : rédacteur grok-4.7, auditeur médical grok-4.6, autre run, contexte vierge. Parade : `routage_grok.py consigner` à chaque passe ; ordre rédacteur → médical → conformité → transversale.

**P-10 · Reprendre un run recharge tout son historique.** Parade : nouveau run avec message constant + état disque (PROMPT_PRODUCTION_V2 §5) ; ne jamais continuer une conversation longue.

**P-11 · Redémarrage de conteneur.** Cas réel (commit « Relance des 5 refontes interrompues par le redémarrage ») : des runs s'arrêtent sans dernier fichier. Parade : `ressources_ia/outils/suivi_ia.py capture grok`, `REPRISE_GROK.md`, vérifier le disque avant toute relance ; un run sans retour sur disque est « probablement interrompu ».

**P-12 · Note orpheline.** Le graphe Obsidian étudié a un nœud isolé (« Idées en vrac ») : connaissance morte. Parade : `outils/vault_lint.py` refuse toute note sans lien entrant depuis l'accueil.

**P-13 · Veille et horloge.** Pouls de veille > 30 min = production bloquée (PROMPT_GROK §9.2). Le workflow GitHub de 5 min ne tourne que depuis `main` : activation manuelle par Vial ; en attendant, boucle sur la machine.
