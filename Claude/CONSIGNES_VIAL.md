# Consignes de Vial — recueil applicable (tenu par Claude ; lu par tout agent avant d'agir)

Mise à jour : 11.11.2026. Une consigne nouvelle s'ajoute ici le jour même.

## Communication
1. **Concision extrême pour tous (agents et Claude ; Vial exclu).** Rapports ≤ 5 lignes. À Vial : seulement ce qu'il doit décider, chaque question avec sa référence (lien, fichier, capture).
2. Montrer régulièrement le travail en images groupées (planches de 5 captures par cours, ébauches).

## Fond médical
3. Sources suisses, puis européennes, lues et datées ; aucune source seulement américaine en appui d'une décision ou d'un chiffre ; rien d'inventé ; une déduction n'est jamais présentée comme recommandation.
4. Doses : AIPS suisse de la molécule (jamais le Compendium) ; sinon société savante suisse (« hors AIPS ») ; divergence écrite.
5. Pareto : les 20 % d'information qui font 80 % de l'impact ; pas de bavardage ; structure systématique ; démarche et prise en charge locales suisses.
6. Précision, densité, clarté ; vital et crucial d'abord ; anticiper les diagnostics difficiles pour le médecin assistant débutant.
7. **Base anatomo-fonctionnelle obligatoire partout où le signe en dépend** (cours, examens, pharmacologie) : concise, puissante, du général vers le problème, expliquant le *pourquoi* du signe (ex. paralysie faciale : innervation corticale bilatérale du front → la lésion centrale épargne le front). Image réelle (coupe, schéma publié), jamais générée ni SVG dessiné ; puis autres formes, étiologies, traitements.
8. Images cliniques réelles et de qualité (licence vérifiée).
8 bis. **Images en couleurs de préférence** (12.11.2026) : photo clinique ou schéma publié en couleur (Blausen, OpenStax, PMC CC BY…) ; noir et blanc (Gray) seulement à défaut.
9. **Toujours dans des fenêtres** (centrales, occultantes) : ne jamais saturer la page active.

## Forme
10. Front-end : fonds blancs ou couleurs vivantes ultra-pâles (bleu ciel, vert, lilas…) ; **jamais ivoire, beige, crème** ; esthétique soignée, jauges colorées et oscillantes.
11. Cours : règles L1 (80–150 Ko, point 1 = définition seule, une fiche par molécule, phrases verbales, aucune redite).

## Réceptacle (page de progression)
12. Groupes PROFILES G, S, F, O avec dénomination exacte et icône ; boutons « Cours et diagnostics » et « Banque QCM et questions type examen ».
13. Nom réel du SSP (jamais « LOT », ni « Vue d'ensemble ») ; diagnostics numérotés, décalés ; bouton « Réflexe Gn » : raisonnement rapide étape par étape, prévalence en %, dénominateur en exposant rouge.
14. Examens complémentaires : par prélèvement (sang, urines, ponctions, LCR…), imagerie (IRM détaillée), explorations fonctionnelles ; indication de la demande en rouge gras ; rappel anatomo-physiologique en fenêtre.
14 bis. **Bilans biologiques : l'interprétation est obligatoire.** Tableau : colonne « anomalie », puis colonnes « à rechercher à l'anamnèse », « à la clinique », « examen de référence (gold standard) », et à droite « diagnostic ».
15. Pharmacologie : trois colonnes alignées (fonctionnement normal → altération et pathologies → classes) ; « Fonctionnement » = chaîne d'activation (stimulus, chaque produit, lieu, effet, rétrocontrôle), en étapes fléchées ; mnémotechnique sourcé.

16 bis. **Partout : structures dépliables vers le bas au clic** (repliées = titre + une ligne) et **bande latérale plus sombre portant le plan cliquable de la page active** (ex. pharmacologie : systèmes physiologiques et fonctionnements altérés) ; sur mobile, tiroir « Plan ».

## Méthode
16. Économie : rédiger seulement si vide ou ancienne architecture ; sinon retoucher ou auditer.
17. Tous les outils et connecteurs pour chercher au-delà du harnais, en restant suisse.
18. Exigences pédagogiques dès LOT_021, sans retour en arrière (sauf demande explicite, ex. LOT_020 DX.1).
19. Jamais --force ni suppression de branche ; rapport HTML de progression chaque matin à 8 h.

## Politique de production (ordre de Vial, 12.11.2026)
20. **Claude seul** fait la Phase A (renforce si elle existe, conçoit sinon), gèle la liste DX et passe d'un LOT au suivant.
21. Les 10 DX d'un LOT sont distribués à **5 agents seulement** (2 DX chacun), chacun sur sa branche ; Claude orchestre et fusionne.
22. **File active** = 10 LOTs menés en parallèle ; une seule file active à la fois ; la suivante commence quand la précédente est close.
23. Phase A du LOT n finie → Claude enchaîne la Phase A du LOT n+1 pendant que les agents avancent. Un agent performant est maintenu ; il est remplacé (gratuitement) après ≤ 10 chapitres cumulés ou plus tôt s'il faiblit.
24. La page de progression se met à jour seule (script gratuit) à chaque LOT fusionné avec son contre-audit.
