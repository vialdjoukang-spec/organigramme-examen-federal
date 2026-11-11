# MISSION — rédiger UNE fiche de référence (onglets Examens complémentaires et Pharmacologie du réceptacle)

Ta mission te donne l'identifiant de la fiche (`id`) et son titre. Tu écris UN fichier : `Claude/_reference/fiches/<id>.json`
(et, s'il y a une image, ses fichiers dans `Claude/_reference/images/`). Rien d'autre. Jamais de checkout, reset, stash,
`git add -A` ; valide par chemin puis `git push origin HEAD`.

## But
Une fiche de révision pour l'examen fédéral suisse de médecine humaine, lue sur téléphone : **précise, dense, claire, courte**.
Chaque phrase porte un fait utile. À information égale, la phrase la plus courte gagne. Phrases verbales complètes.

## Loi de Pareto (ordre de Vial du 11.11.2026)
Ces fiches remplacent les manuels trop vastes : elles gardent les 20 % d'information qui font 80 % des décisions et des
questions d'examen, et permettent de **tout revoir, vite**.
- **Tri sévère.** Avant d'écrire, liste ce qu'un médecin assistant doit savoir pour décider ; écarte le reste (historique,
  raretés sans conséquence, mécanismes sans effet sur la conduite). Aucun bavardage, aucune phrase d'introduction.
- **Structure identique d'une fiche à l'autre**, dans le même ordre, pour que l'œil sache où chercher : c'est ce qui rend
  la révision rapide. Tableaux et cases plutôt que paragraphes ; un paragraphe ne dépasse pas trois phrases.
- **Systématique.** Chaque examen : quand le demander, comment le lire dans l'ordre, que conclure, que faire. Chaque
  classe : ce qu'elle corrige, comment la retenir, qui sont les chefs de file, comment on les prescrit en Suisse, ce qui tue.
- **Démarche diagnostique et prise en charge locales** : la conduite enseignée est celle des sources suisses lues (guides
  des hôpitaux universitaires, sociétés suisses, OFSP, AIPS) ; la source est citée à chaque décision.
- Taille : vise le bas de la fourchette. Une fiche de 6 000 octets qui dit tout l'essentiel vaut mieux qu'une de 14 000.

## Véracité (non négociable)
- Chaque valeur, seuil, dose et affirmation de décision vient d'une source **lue pendant ta mission**, suisse d'abord
  (sociétés suisses de discipline, Swiss Medical Forum, Revue Médicale Suisse, guides HUG, CHUV, Inselspital, USZ, USB, OFSP,
  Swissmedic, smarter medicine), puis européenne. Aucune source seulement américaine en appui d'une décision. Rien de mémoire.
- Médicament : indications, posologie, contre-indications, grossesse et allaitement, cinétique viennent de l'**AIPS suisse** de
  la molécule, lue sur refdata (index : `/home/user/Medina/AipsDownload_20261008.zip`, XML lu en flux → URL
  `https://files.refdata.ch/…-fr.html`). Jamais le Compendium. Si l'AIPS ne porte pas une dose, une société savante suisse lue
  fait foi et la phrase écrit « hors AIPS ».
- Charge les connecteurs par `ToolSearch` (pubmed, consensus, elicit, web) pour trouver les sources suisses.
- Valeurs de laboratoire : unités SI, avec l'origine de la norme (laboratoire universitaire suisse ou source citée) ; écris
  que la norme varie selon le laboratoire quand c'est le cas.
- Image : réelle, prise ailleurs (Wikimedia Commons ou source ouverte, licence vérifiée, `Claude/_outils/cliche.py`), jamais un
  SVG dessiné ni une image générée ; légende qui dit quoi regarder. Pas d'image plutôt qu'une image douteuse.

## Format JSON (lu par `outils/receptacle.py`)
```json
{
 "titre": "…",
 "rappel": [{"texte": "Le général : organe, fonction normale [n]", "src": [1]}, {"texte": "…", "src": [2]}, {"texte": "Le problème : ce qui se dérègle et que l'examen mesure ou que la classe corrige", "src": [3]}],
 "indication": ["Quand demander l'examen (ou : indications du médicament), en 2 à 5 lignes"],
 "sections": [
  {"titre": "…", "texte": "paragraphe" },
  {"titre": "…", "texte": ["puce", "puce"]},
  {"titre": "…", "tableau": [{"Paramètre": "…", "Norme": "…", "À retenir": "…"}]},
  {"titre": "Raisonnement par cases", "algorithme": {"question": "…", "branches": [{"si": "…", "alors": {"question": "…", "branches": [{"si": "…", "alors": "conclusion et conduite"}]}}]}}
 ],
 "images": [{"fichier": "Claude/_reference/images/<nom>.webp", "legende": "…", "source": "auteur, licence, URL"}],
 "sources": ["[1] Auteur ou organisme. Titre. Année. URL (lu le JJ.MM.AAAA)"]
}
```
- `rappel` (obligatoire, ordre de Vial du 11.11.2026) : rappel anatomo-physiologique **concis**, 3 à 6 étapes d'une ou deux phrases
  verbales, qui part du général (organe, fonction normale) et aboutit au problème (dernière étape : ce qui se dérègle, que l'examen
  mesure ou que la classe corrige). Chaque étape cite ses sources par leur numéro dans `sources` (`src`), rien de mémoire. Le
  réceptacle l'ouvre dans une fenêtre centrale par le bouton « Rappel anatomo-physiologique », jamais directement sur la page.
- `indication` s'affiche en **rouge gras** : c'est l'indication de la demande (examen) ou les indications actuelles (médicament).
- Dans les textes, cite la source par son numéro entre crochets : « … [2] ».
- Examen : sections conseillées — Principe en une phrase ; Réalisation et conditions de prélèvement ; Valeurs et unités
  (tableau) ; Lecture systématique ; **Raisonnement par cases** (algorithme cliquable, 2 à 4 niveaux) ; Pièges ; Ce qui est
  vital (résultat qui impose un geste immédiat, avec le délai).
- Classe ou médicament : sections conseillées — Logique de la classe (quelle fonction altérée elle corrige, moyen de la
  retenir) ; Chefs de file en Suisse (tableau : molécule, spécialité, n° AIPS) ; Posologie (AIPS) ; **Le voyage du
  médicament** — pharmacocinétique (absorption, distribution, métabolisme, élimination, demi-vie, adaptation rénale et
  hépatique) ; Pharmacodynamie (cible, effet, délai) ; Contre-indications et interactions qui tuent ; Grossesse et
  allaitement ; Surveillance ; Pièges d'examen.
- Taille visée : 6 000 à 14 000 octets. Vérifie : `python3 -c "import json;json.load(open('<fichier>'))"`, puis
  `python3 outils/receptacle.py --audites 1-16 --sortie /tmp/essai.html` (la fiche doit être intégrée sans erreur).

## Fin
Valide `Claude/_reference/fiches/<id>.json` (et ses images) par chemin, message terminé par les lignes de ta mission, puis
pousse. Rapport en 6 lignes : sources lues (suisses / européennes), AIPS lues, ce qui manque, doutes médicaux.
