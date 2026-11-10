# BRIEF — rédaction d'une leçon Claude (prompt Lo_9.11.26, chaîne M5 E2→E8)

Référence : `PROMPT_Casern/PROMPT_LOTS_Lo_9.11.26.claude.md` (branche `reference/prompts-9.11.26`), copie lisible :
`$OUTILS_REF/../PROMPT_Casern/PROMPT_LOTS_Lo_9.11.26.claude.md` — lire µ3 (14 points), µ4 (langue), µ5 (fenêtres), µ7 (gabarit), M2 (lois de vérité).

## Environnement (à exporter dans chaque commande Bash)
```bash
export PAQUET_CACHE=/tmp/claude_paquet_cache
L=/home/user/organigramme-examen-federal/Claude/_outils/lecon.py
cd <WORKTREE>      # donné dans ta mission ; toutes les commandes partent de là
```
Tu n'écris QUE dans `Claude/LOT_XXX/` de ton worktree, et seulement dans tes chemins (`_travail/<CIBLE>/` et ton HTML final).
Tu ne fais ni commit, ni push, ni branche : le chef de production s'en charge.
Tes scripts et fichiers temporaires vont dans `_travail/<CIBLE>/` (jamais dans un dossier partagé : d'autres rédacteurs tournent en parallèle).
Chaque phrase factuelle, y compris de physiopathologie, cite un extrait (LV1) : une phrase « de manuel » sans source est interdite.

## Étapes
1. **Sources (E2).** Trouve 6 à 15 sources lisibles, Suisse d'abord puis Europe (LV5) : HUG « stratégies » (PDF, hug.ch),
   Revue Médicale Suisse (revmed.ch), Forum Médical Suisse, OFSP/OFS/Obsan, Swissmedic, sociétés suisses ; puis ESC, ERS, EASL,
   ESGE, ESHRE, EAU, ESCMID, KDIGO, NICE, HAS, AWMF ; textes intégraux PMC (`https://pmc.ncbi.nlm.nih.gov/articles/PMCxxxx/`)
   et résumés PubMed pour les chiffres d'épidémiologie. Jamais une recommandation exclusivement américaine.
   Vérifie la version la plus récente (LV8). Mets une URL par ligne dans `Claude/LOT_XXX/_travail/<CIBLE>/urls.txt`.
   (academic.oup.com et europepmc.org renvoient 403. Si la page PMC renvoie un reCAPTCHA, utilise le texte intégral
   `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=<n° PMC sans « PMC »>` ; résumé PubMed :
   `…/efetch.fcgi?db=pubmed&id=<PMID>&rettype=abstract&retmode=text`. Erreur 429 : relance une fois.)
2. **Paquet.** `python3 $L prep --lot XXX --cible <CIBLE> --entite "<nom>" --ssp <code> --urls Claude/LOT_XXX/_travail/<CIBLE>/urls.txt --dci <racines DCI des médicaments du point 11>`
   (`<CIBLE>` = `PA` pour la Phase A, `DX.i` pour un DX ; DCI en racine courte : `colchic ibuprofen amoxicill`).
   Relance avec `--ajouter` pour compléter. Une URL en ECHEC ou vide (< 2 passages) se remplace par une autre.
3. **Lecture ciblée.** `python3 $L extraire --lot XXX --cible <CIBLE> --motif "regex"` (ajoute `--prefixe aips` pour l'AIPS).
   Ne lis jamais le paquet entier d'un bloc ; tu ne rédiges qu'à partir de passages lus (LV1).
4. **Rédaction (E6).** Écris `Claude/LOT_XXX/_travail/<CIBLE>/fragments/p01.html` … `p14.html` (fragment HTML seul, sans titre de point :
   l'assembleur ajoute `<section>` et `<h3>`). Contenu exigé : µ3 / `contrat.json`. Forme :
   - `<div class="p">phrases…</div>` ; sous-titres `<h4><em>9.a Gold standard</em></h4>` ; tableaux `<div class="t"><table>…</table></div>` ;
     listes `<ul><li>…</li></ul>` ; fenêtres `<button class="w" popovertarget="PREFIX-pN-fK">libellé</button>` dans une phrase complète,
     et `<div id="PREFIX-pN-fK" popover class="fenetre">…</div>` placé APRÈS le paragraphe (PREFIX = `pa` ou `dxi`, ex. `dx3`).
   - Citation : `<sup class="r"><a href="#sb-ID">ID</a></sup>` en fin de phrase factuelle, ID exact du paquet.
   - **Chaque nombre** (y compris âges, pourcentages, doses, seuils, années, « 1re », « 24 h ») d'une phrase citée doit figurer
     dans l'extrait cité dans cette même phrase ; sinon ROUGE. Écrire un nombre factuel ou une unité (« milligrammes ») en toutes lettres pour échapper
     au contrôle est interdit (LV3, LV6) : le nombre figure dans l'extrait cité, la dose dans un extrait `aips-*`. Attention : « COVID-19 », « SpO2 » isolé, « 3e » sont des nombres pour le contrôle.
   - Une phrase avec dose (mg, µg, UI) cite un extrait `aips-…` ; doses, voies, durées, grossesse/allaitement recopiés de l'AIPS,
     sans adoucir ; numéro Swissmedic lu dans la source AIPS (5 chiffres). Si une société savante diverge de l'AIPS
     (dose, contre-indication, grossesse), la conduite enseignée suit l'AIPS ; la recommandation divergente est citée comme telle,
     hors AIPS, sans jamais être présentée comme une option équivalente.
   - Langue µ4 : phrase verbale 12–28 mots (jamais > 32), connecteur logique dans chaque paragraphe > 40 mots,
     ≥ 35 % de phrases avec connecteur (car, donc, ainsi, en effet, dès lors, cependant, en revanche, lorsque, si, ce qui, d'où…),
     abréviation développée à la 1re occurrence, normal avant pathologique, grave avant fréquent. Aucune formule de lacune
     (« à vérifier », « non trouvé ») : une lacune va dans `_travail/<CIBLE>/HELP.md`.
   - Cellules de tableau (`td`) : courtes ; elles échappent au contrôle de citation, mais leurs nombres doivent rester exacts.
   - Interdits : `title=`, `<script>`, images, `<html>`, ligne > 3 000 caractères, phrase recopiée d'un autre fichier du LOT.
   - Volume : HTML final 100 000–200 000 octets (viser 120–170 Ko) par des faits distincts, jamais du remplissage.
5. **Assemblage et contrôle (E8).** `python3 $L finir --lot XXX --cible <CIBLE> --titre "<titre exact>"`
   Titre : Phase A `LOT_XXX — <code SSP> — <intitulé SSP>` ; DX `DX.i — <nom exact de LISTE_DX_CANONIQUE.md>`.
   Corrige les fragments puis relance jusqu'à **zéro défaut A_*, zéro B_phrase_partagee, C_* nul, bande respectée** ;
   vise VERT (B_phrase_nominale/longue = 0, paragraphes_sans_connecteur = 0, connecteur% ≥ 35). Au plus 6 relances.
6. **Rendu.** Réponds en ≤ 12 lignes : verdict, octets, connecteur%, défauts restants, molécules sans AIPS (HELP), sources principales.

## Question finale (M1.3)
« Ce cours, lu seul avec ses fenêtres, suffit-il pour gagner 90 à 100 % des points sur ce sujet et pour traiter ce patient en sécurité ? »
