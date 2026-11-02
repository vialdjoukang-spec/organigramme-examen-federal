# Recherche de photographies cliniques — LOT 133

Date de consultation : 2026-11-02 UTC. Producteur : agent astra_images133.

**Résultat : aucune image acquise, aucune inspection visuelle des pixels, aucune annotation réalisée.** Les candidats ci-dessous proviennent des extraits textuels du moteur de recherche connecté. Leur licence autorise en principe les adaptations ; leur aptitude clinique et leur cadrage restent à vérifier sur le fichier réel. `validé_humain = false` pour tous.

| Priorité / signe | Titre et URL source | Auteur | Licence / URL | Métadonnées consultées et statut |
|---|---|---|---|---|
| 1 — Hippocratisme | [Clubbing fingers 2.jpg](https://commons.wikimedia.org/wiki/File:Clubbing_fingers_2.jpg) | Wesalius | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | Photographie annoncée de doigts hippocratiques, 3264 × 1836, 715 Ko ; adaptation sous même licence ; non téléchargée. |
| 2 — Ictère | [Scleral Icterus.jpg](https://commons.wikimedia.org/wiki/File:Scleral_Icterus.jpg) | Sheila J. Toro | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | 1600 × 894, 261 Ko ; description mentionnant l’autorisation du patient et une hépatite aiguë ; non téléchargée. |
| 3 — Purpura | [HSP Vasculitis.jpg](https://commons.wikimedia.org/wiki/File:HSP_Vasculitis.jpg) | Profrofrof | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | Photographie déclarée des propres pieds de l’auteur, 1080 × 1433, 216 Ko ; non téléchargée. |
| Alternative purpura | [Purpura Schonlein Henoch.JPG](https://commons.wikimedia.org/wiki/File:Purpura_Schonlein_Henoch.JPG) | Mnokel (Wikipédia arabe) | Domaine public, déclaration de l’auteur reproduite dans la page source | 800 × 533, 97 Ko ; non téléchargée. |
| Alternative purpura | [Purpura.jpg](https://commons.wikimedia.org/wiki/File:Purpura.jpg) | User:Hektor | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) | 751 × 626, 19 Ko ; non téléchargée. |

## Accès et exclusions

- Harnais `controler.py` : infrastructure prête, aucune erreur ; bracelet exécuté avec la tâche « recherche images inspection hippocratisme ictère purpura ». Le script a automatiquement mis à jour ACTIVITE.json et ajouté la preuve JSONL ; le responsable en a été informé. Aucun HTML ni Git modifié.
- Politique réseau et état cloud consultés : mode restreint appliqué, pas de VPN. Wikimedia/upload.wikimedia.org absents des destinations autorisées ; aucune nouvelle tentative de téléchargement de Clubbing1.JPG après le refus signalé par le responsable.
- GET de `https://www.europepmc.org/restful/search` avec requête `TITLE:"digital clubbing" AND OPEN_ACCESS:Y`, format JSON, pageSize 8 : HTTP 403 ; aucun résultat image reçu. Aucun changement de proxy ni contournement.
- HEAD de `https://academic.oup.com/` : HTTP 403, `cf-mitigated: challenge` ; aucune tentative de franchir le contrôle.
- La piste *Digital Clubbing Is Associated with Higher Serum KL-6 Levels and Lower Pulmonary Function in Patients with Interstitial Lung Disease*, Kazushige Shiraishi et al., DOI 10.1155/2018/3640967, PMC5828477, porte une licence CC BY dans les extraits ; présence d’une photo clinique utilisable non établie, donc non retenue comme image.
- Acta Dermato-Venereologica, DOI 10.2340/00015555-1288 : CC BY-NC 4.0, exclu des licences demandées. EyeRounds, atlas ictère de Zachary Q. Mortensen : BY-NC-ND 3.0, exclu. Pas d’image récupérée sur ces plateformes.

## Preuves et reprise

Les réponses structurées du moteur sont conservées dans `recherche_clubbing.json`, `recherche_search2.json` (ictère), `recherche_purpura.json` et `recherche_search.json` (pistes articles). Elles attestent une consultation de métadonnées textuelles, jamais une inspection de photographies.

Après acquisition par un accès autorisé : vérifier le contenu par outil de vision, contrôler le cadrage et toute identification personnelle, conserver auteur/source/licence/date, puis produire éventuellement un WebP ≤ 200 Ko sans modifier le signe. Toute annotation doit être déclarée comme adaptation ; aucune localisation de flèche proposée avant examen réel. Aucun fichier image fictif ou substitut généré.
