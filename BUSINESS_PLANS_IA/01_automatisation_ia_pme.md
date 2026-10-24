# Plan 01 : Automatisations IA « clé en main » pour petites entreprises et cabinets (hors données de patients)

> **Capital :** 0 à 50 CHF. **Temps :** 8 à 15 h/semaine.
> **Compatibilité avec le permis B :** voie **salariée** possible (employé à temps partiel d'une agence ou d'une PME informatique). La voie **indépendante** n'est possible que si votre permis l'autorise (§ 9.2).

---

## 1. Résumé

Vous mettez en place, pour des microentreprises de Suisse romande, **une ou deux automatisations simples et mesurables** reposant sur l'IA. Les clients visés : fiduciaires, artisans, agences immobilières, commerces, physiothérapies pour la seule partie administrative non médicale. Exemples d'automatisations :

- tri et brouillons de réponse aux e-mails ;
- extraction de données de factures fournisseurs vers un tableur ;
- formulaire de demande qui produit un devis préformaté ;
- FAQ chatbot sur le site, sans données sensibles.

Vous travaillez avec des outils no-code dont l'offre gratuite suffit pour démarrer (Make, Zapier, n8n, Botpress). Vous vendez un **forfait de mise en place** et, en option, un **petit abonnement de maintenance**.

## 2. Pour qui, prérequis et temps hebdomadaire

| Élément | Détail |
|---|---|
| Profil | Logique, à l'aise avec les tableurs et capable d'apprendre un outil no-code en 2 semaines |
| Prérequis | Ordinateur, connexion. Aucune compétence de programmation obligatoire |
| Temps | 8 à 15 h/semaine : il faut de la prospection en personne et du support |
| Atout médical | Compréhension des contraintes de confidentialité. **Vous n'automatisez rien qui touche aux données de patients** |

## 3. Marché et demande (sources vérifiées)

1. **Tissu de PME :** en 2023, 624'219 des 626'033 entreprises suisses étaient des PME (plus de 99 %). On comptait 561'952 microentreprises, dont 333'297 entreprises d'un seul emploi ([Portail PME](https://www.kmu.admin.ch/fr/chiffres-sur-les-pme-entreprises-et-emplois) ; [OFS](https://www.bfs.admin.ch/bfs/fr/home/statistiques/industrie-services/entreprises-emplois/structure-economie-entreprises/pme.html)).
2. **Adoption encore faible dans les petites entreprises :** selon le KOF (EPF Zurich), un peu plus de 8 % des petites entreprises utilisaient l'IA, contre plus d'un tiers des grandes ([KOF, 20.02.2025](https://kof.ethz.ch/en/publications-data/publications/kof-insights/articles/2025/02/digital-technology-are-small-firms-being-left-behind.html)).
3. **Adoption en hausse :** selon l'étude PME 2025 d'AXA (sondage Sotomo auprès de 300 PME, mars 2025) :
   - 37 % des PME utilisent l'IA ;
   - la part de celles qui l'intègrent dans leurs processus est passée de 22 % à 34 % ;
   - les usages principaux sont la traduction (52 %) et la correspondance (47 %) ;
   - l'étude relève des lacunes en matière de protection des données.
   - Source : [AXA, 08.10.2025](https://www.axa.ch/fr/aproposdaxa/medias/communiques-presse/derniers-communiques-presse/2025/20251008-etude-sur-le-marche-du-travail-pme-2025-ia.html).
4. **Prix internationaux :** Upwork indique un tarif médian d'environ 30 à 61 USD/h pour les développeurs de chatbots ([Upwork](https://www.upwork.com/hire/chatbot-developers/cost/), marché mondial). Le marché local suisse paie en général davantage, mais aucune statistique officielle de tarif n'a été trouvée.

> **Lecture :** il y a beaucoup de petites structures, peu équipées. Les usages « correspondance » et « traduction » dominent : ce sont précisément les automatisations simples que vous proposez.

## 4. Offre exacte et prix (CHF)

| Offre | Contenu | Prix | Justification |
|---|---|---|---|
| **Diagnostic IA (1 h 30)** | Entretien, cartographie des tâches répétitives, 3 recommandations chiffrées en heures gagnées | **190 CHF** (offert si une mise en place suit) | Environ 1,5 h de rendez-vous et 1 h de rapport ; prix d'entrée bas |
| **Automatisation Starter** | 1 flux (par exemple e-mail → tri → brouillon de réponse), documentation et 30 minutes de formation | **590 CHF** | Environ 8 h × 70 CHF/h. Supérieur au haut de la fourchette médiane d'Upwork (61 USD/h), parce que le service est local, en français et accompagné |
| **Pack PME** | 2 à 3 flux et une FAQ chatbot sur le site (sans données sensibles) | **1'290 CHF** | Environ 18 h |
| **Maintenance** | Surveillance mensuelle, correctifs, 1 petite modification par mois | **49 CHF/mois** | Couvre environ 45 min/mois |

> Les abonnements aux outils (Make, Zapier, etc.) sont **au nom du client** et payés par lui. Vous ne revendez pas de licences, ce qui limite votre risque et respecte les conditions des éditeurs.

<details>
<summary><b>Trois flux « vitrines » à savoir construire avant de vendre (cliquer)</b></summary>

1. **E-mail → brouillon :** un nouvel e-mail dans une boîte « info@ » est classé par un LLM en 4 catégories. Un brouillon de réponse est créé dans la boîte (jamais envoyé automatiquement), puis une notification est envoyée.
2. **Facture PDF → tableur :** une pièce jointe est déposée dans un dossier, ses champs (fournisseur, date, montant, TVA) sont extraits, une ligne est ajoutée au tableur et une alerte est envoyée en cas d'anomalie.
3. **Formulaire → devis :** un formulaire Tally est rempli, un modèle de devis est complété, il est envoyé au patron pour validation, puis au client.

Règle d'or : **un humain valide toujours** avant tout envoi externe.
</details>

## 5. Outils

| Outil | Offre gratuite (relevée sur la page tarifaire) | Lien |
|---|---|---|
| Make | 1'000 crédits/mois | <https://www.make.com/en/pricing> |
| Zapier | 100 tâches/mois, Zaps illimités | <https://zapier.com/pricing> |
| n8n | Community Edition auto-hébergée gratuite ; cloud payant | <https://n8n.io/pricing/> |
| Botpress | 100 conversations/mois, 3 sièges ; Plus à 150 USD/mois | <https://botpress.com/pricing> |
| Voiceflow | offre gratuite limitée | <https://www.voiceflow.com/pricing> |
| Tally | formulaires gratuits | <https://tally.so/pricing> |
| API LLM | Gemini API (offre gratuite limitée), Mistral | <https://ai.google.dev/gemini-api/docs/pricing> · <https://www.mistral.ai/pricing> |
| Page vitrine | Carrd | <https://carrd.co/pro> |
| Rendez-vous | Cal.com | <https://cal.com/pricing> |

> **Données :** les offres gratuites de certaines API d'IA peuvent utiliser vos données pour améliorer les modèles. Vérifiez les conditions en vigueur sur la page de Google avant d'y faire passer des données de clients. Pour un client, utilisez **son** compte payant, avec un accord de traitement des données (nLPD, annexe 09, § 5).

## 6. Plan d'action

### Jours 1 à 30

| Jour | Tâche | Livrable ou checklist |
|---|---|---|
| 1 | LISEZMOI, § 0 : identifier votre cas de permis ; envoyer la question écrite | ☐ Demande envoyée |
| 2 | Créer des comptes gratuits Make, Zapier et Tally **pour vous** (usage d'apprentissage) | ☐ Comptes |
| 3–4 | Suivre les tutoriels officiels de Make (scénarios, routeurs, gestion d'erreurs) | ☐ 3 scénarios test |
| 5–6 | Construire le flux vitrine n° 1 (e-mail → brouillon) sur **votre** boîte de test | ☐ Flux 1 et vidéo de démonstration de 2 min |
| 7–8 | Flux vitrine n° 2 (facture PDF → tableur) avec de fausses factures que vous créez | ☐ Flux 2 et vidéo |
| 9–10 | Flux vitrine n° 3 (formulaire → devis) | ☐ Flux 3 et vidéo |
| 11 | FAQ chatbot Botpress sur une page Carrd de démonstration | ☐ Chatbot de démonstration |
| 12 | Mesurer : temps de construction, coût mensuel en crédits, taux d'erreur sur 20 essais | ☐ Fiche technique par flux |
| 13 | Rédiger les modèles : offre, devis, contrat de mandat (périmètre, exclusions, responsabilité, nLPD), procès-verbal de livraison | ☐ 4 modèles |
| 14 | Rédiger la checklist nLPD « avant automatisation » (quelles données, quel fournisseur, quel pays, quel accord de traitement des données) | ☐ Checklist |
| 15 | Page Carrd (brouillon) : 3 vidéos, prix, FAQ | ☐ Brouillon |
| 16–17 | Lister 60 microentreprises locales (local.ch, Zefix) : nom, secteur, e-mail public, tâche probable à automatiser | ☐ Tableur de prospects |
| 18 | Préparer un « mini-audit » écrit type (1 page) | ☐ Modèle |
| 19 | **Point de contrôle permis.** Sans réponse : relance téléphonique | ☐ Relance |
| 20 | Si seule la voie salariée est ouverte : postuler auprès de 10 agences ou PME informatiques (employé à 15 h/semaine au maximum) et joindre le portfolio vidéo | ☐ 10 candidatures |
| 21–27 | Si l'activité indépendante est autorisée : 10 contacts personnalisés par jour ouvrable et 2 visites en personne par semaine | ☐ 50 contacts |
| 28 | Relances (une seule fois, à J+5) | ☐ |
| 29 | 2 à 3 diagnostics réalisés | ☐ Rapports |
| 30 | Bilan : taux de réponse, rendez-vous, devis | ☐ Bilan |

### Semaines 5 à 12

| Semaine | Objectif | Livrables |
|---|---|---|
| 5 | 1er devis signé | Contrat signé |
| 6 | Livraison du 1er flux et formation du client | Procès-verbal de livraison, documentation |
| 7 | Mesure du temps gagné chez le client (avant/après) | Étude de cas chiffrée (avec son accord) |
| 8 | Proposer la maintenance | 1 abonnement |
| 9 | Partenariat avec 1 fiduciaire, qui vous recommande à ses clients | Accord de recommandation |
| 10 | Standardiser : modèles de scénarios réutilisables | Bibliothèque |
| 11 | 2e et 3e clients | 2 contrats |
| 12 | Bilan à 3 mois (§ 11) | Décision |

## 7. Acquisition des premiers clients

- **Canaux :**
  1. visites et réseau local (commerces, fiduciaires) ;
  2. e-mails individuels ;
  3. LinkedIn, à la main ;
  4. événements de la chambre de commerce et des associations de PME.
- **Volume :** 10 contacts par jour ouvrable pendant 3 semaines, puis 5 par jour. Visez 2 visites par semaine.
- **Règles :** messages personnalisés ; aucun envoi de masse ; lien ou phrase de refus ([LCD art. 3 al. 1 let. o](https://www.fedlex.admin.ch/eli/cc/1988/223_223_223/fr)) ; pas d'automatisation LinkedIn ([LinkedIn User Agreement](https://www.linkedin.com/legal/user-agreement)).

<details>
<summary><b>Modèle d'e-mail à une microentreprise (cliquer)</b></summary>

> **Objet :** 3 h par semaine de moins sur vos e-mails « info@ » ?
>
> Bonjour Madame [Nom],
>
> J'ai vu sur votre site que vous recevez les demandes de devis via [formulaire / adresse info@].
>
> Je mets en place pour de petites entreprises de la région des automatisations simples. Par exemple : chaque demande reçue est classée et un brouillon de réponse est préparé. **Vous validez toujours avant l'envoi.** Démonstration de 2 minutes : [lien vidéo].
>
> Un diagnostic de 1 h 30 coûte 190 CHF ; il est offert si vous décidez ensuite d'une mise en place. Seriez-vous disponible 15 minutes la semaine prochaine pour en parler ?
>
> Meilleures salutations,
> [Prénom Nom], [téléphone]
>
> *Si ce n'est pas pour vous, répondez simplement « non merci » et je ne vous recontacterai pas.*
</details>

<details>
<summary><b>Modèle d'e-mail à une fiduciaire, pour un partenariat (cliquer)</b></summary>

> **Objet :** Automatiser la saisie des factures fournisseurs de vos petits clients
>
> Bonjour Monsieur [Nom],
>
> De nombreuses microentreprises vous transmettent encore leurs factures en vrac. Je construis des flux simples (PDF → tableau structuré) qui vous font gagner du temps à la saisie. Démonstration : [lien]. Je serais heureux de vous montrer la démonstration en 20 minutes, et de vous proposer ce service pour vos clients si vous le jugez utile.
>
> Bien à vous, [Prénom Nom]
</details>

<details>
<summary><b>Script de visite en personne, 60 secondes (cliquer)</b></summary>

« Bonjour, je m'appelle [Prénom]. J'aide les petits commerces du quartier à gagner du temps sur les e-mails et les devis, grâce à des outils simples et à l'IA. Je ne vends pas de logiciel. Je vous montre en 2 minutes sur mon téléphone ? … Si cela vous intéresse, je laisse ma carte : le diagnostic est offert si nous travaillons ensemble. »
</details>

## 8. Modèle financier (estimations, non garanties)

**Hypothèses :**

- Panier moyen de 590 CHF par mise en place.
- Maintenance à 49 CHF/mois.
- Coûts : Carrd environ 9 USD/an. Outils de test gratuits. Éventuellement une assurance responsabilité civile professionnelle (prix à demander à un assureur, non sourcé).

| Scénario | Mois 3 | Mois 6 | Mois 12 | Cumul sur 12 mois | Hypothèse |
|---|---|---|---|---|---|
| **Bas** | 0 CHF | 590 CHF (1 client) | 49 à 640 CHF/mois | ≈ 2'000 CHF | 3 clients par an, 1 maintenance |
| **Médian** | 590 CHF | 1'200 CHF/mois | 1'500 CHF/mois | ≈ 12'000 CHF | 1 à 2 mises en place par mois dès le mois 4 ; 5 maintenances au mois 12 |
| **Haut** | 1'290 CHF | 2'500 CHF/mois | 3'500 CHF/mois | ≈ 30'000 CHF | 3 à 4 projets par mois ; 15 maintenances. **Dépasse probablement 15 h/semaine** |

- **AVS :** au-delà de 10'100 CHF de revenu net, le barème dégressif s'applique à partir de 5,371 % ([Mémento 2.02](https://www.ahv-iv.ch/p/2.02.f)).
- **TVA et registre du commerce :** pas concernés en dessous de 100'000 CHF de chiffre d'affaires.

> **Il n'existe aucune garantie de revenu.** Ces projections sont des hypothèses à confronter à vos taux réels de conversion.

## 9. Cadre légal et fiscal suisse

Règles communes : **`09_ANNEXE_cadre_legal_suisse.md`**.

### 9.1 Points spécifiques

- **nLPD :** quand vous configurez un flux qui traite des données personnelles des clients de votre client, vous agissez comme **sous-traitant**. Il faut un contrat écrit qui précise les finalités, la sécurité et les fournisseurs, avec leur pays. Les éditeurs américains supposent une analyse de la communication de données à l'étranger ([nLPD](https://www.fedlex.admin.ch/eli/cc/2022/491/fr) ; [PFPDT, IA](https://www.edoeb.admin.ch/fr/ia-et-protection-des-donnees)).
- **Refus systématique :** données de santé (patients), données bancaires détaillées, décisions automatisées sans humain dans la boucle.
- **Conditions des outils :** respectez les conditions de Make, Zapier, Botpress et des fournisseurs d'IA. Les abonnements sont au nom du client.
- **Responsabilité :** contrat de mandat ; périmètre précis ; pas de garantie de résultat ; limitation de responsabilité au montant du mandat, dans les limites légales.

### 9.2 Compatibilité avec le permis B

| Cas | Ce plan |
|---|---|
| **(a)** B pour études, État tiers | **Indépendant : non réaliste.** L'activité indépendante d'un ressortissant d'État tiers suppose notamment un intérêt économique global, un plan d'affaires et un capital suffisant ([ZH](https://www.zh.ch/de/wirtschaft-arbeit/erwerbstaetigkeit-auslaender/drittstaaten-angehoerige.html)) ; le portage ne change pas le statut ([OFAS](https://sozialversicherungen.admin.ch/fr/d/21762/download)). **Salarié : oui**, comme employé à temps partiel d'une agence ou d'une PME, 15 h/semaine au maximum en semestre, au plus tôt 6 mois après le début des études, sur demande de l'employeur et avec l'attestation de la haute école (art. 38 OASA ; [Directives LEI, ch. 4.4.3](https://www.sem.admin.ch/dam/sem/fr/data/rechtsgrundlagen/weisungen/auslaender/weisungen-aug-kap4-f.pdf) ; [ZH, Studierende](https://www.zh.ch/de/wirtschaft-arbeit/erwerbstaetigkeit-auslaender/studierende-und-praktikanten.html)) |
| **(b)** B pour études, UE/AELE | Activité accessoire de 15 h/semaine au maximum ([OLCP, ch. 4.7](https://www.sem.admin.ch/dam/sem/fr/data/rechtsgrundlagen/weisungen/fza/weisungen-fza-f.pdf.download.pdf/weisungen-fza-f.pdf) ; [ZH FZA, ch. 5.1](https://www.zh.ch/content/dam/zhweb/bilder-dokumente/themen/migration-integration/einreise-aufenthalt/weisungen/Freiz%C3%BCgigkeitsabkommen%20EU-26%2C%20EFTA-Staaten_IW.pdf)). **Faites confirmer par écrit** que cela couvre une activité indépendante accessoire |
| **(c)** B avec activité salariée | État tiers : autorisation préalable pour une activité indépendante ([Directives LEI, ch. 4.5.3.2](https://www.sem.admin.ch/dam/sem/fr/data/rechtsgrundlagen/weisungen/auslaender/weisungen-aug-kap4-f.pdf)). UE/AELE : annonce et nouveau livret B ([SEM, FAQ](https://www.sem.admin.ch/sem/fr/home/themen/fza_schweiz-eu-efta/eu-efta_buerger_schweiz/faq.html)) |
| **(d)** B par regroupement familial | **Oui**, sans procédure supplémentaire (art. 46 LEI ; art. 27 OASA) |

**Préparable légalement en attendant :**

- l'apprentissage ;
- les flux de démonstration sur **vos** comptes, avec des données fictives ;
- les modèles de documents.

Ne prospectez pas et ne publiez pas d'offre avant la réponse écrite.

## 10. Risques

| Risque | Mitigation |
|---|---|
| Panne d'un flux chez le client | Gestion d'erreurs, alertes, maintenance, documentation |
| Violation de données | Checklist nLPD ; pas de données sensibles ; comptes au nom du client |
| Hallucination de l'IA dans une réponse | Brouillons uniquement ; validation humaine obligatoire |
| Changement de prix ou de conditions d'un outil | Outils au nom du client ; flux portables (n8n en solution de repli) |
| Temps de support sous-estimé | Périmètre écrit ; maintenance payante |
| Permis | Voie salariée ou attente de l'autorisation |

## 11. Indicateurs de succès et critères d'abandon

- **Succès à 3 mois :** au moins 1 client payant ou 1 emploi salarié ; au moins 1 étude de cas avec le temps gagné mesuré.
- **Succès à 6 mois :** au moins 3 clients ; au moins 3 maintenances ; au moins 70 % des diagnostics convertis en mise en place.
- **Abandon :**
  - 0 client après 150 contacts et 10 visites ;
  - ou support supérieur à 30 % du temps facturé ;
  - ou refus de l'office sans voie salariée.

## 12. Sources

- Portail PME et OFS (chiffres des PME) : <https://www.kmu.admin.ch/fr/chiffres-sur-les-pme-entreprises-et-emplois> · <https://www.bfs.admin.ch/bfs/fr/home/statistiques/industrie-services/entreprises-emplois/structure-economie-entreprises/pme.html>
- KOF : <https://kof.ethz.ch/en/publications-data/publications/kof-insights/articles/2025/02/digital-technology-are-small-firms-being-left-behind.html>
- AXA, étude PME 2025 : <https://www.axa.ch/fr/aproposdaxa/medias/communiques-presse/derniers-communiques-presse/2025/20251008-etude-sur-le-marche-du-travail-pme-2025-ia.html>
- Upwork : <https://www.upwork.com/hire/chatbot-developers/cost/>
- Outils : <https://www.make.com/en/pricing> · <https://zapier.com/pricing> · <https://n8n.io/pricing/> · <https://botpress.com/pricing> · <https://www.voiceflow.com/pricing> · <https://tally.so/pricing> · <https://ai.google.dev/gemini-api/docs/pricing> · <https://carrd.co/pro> · <https://cal.com/pricing>
- Annuaires : <https://www.local.ch/fr> · <https://www.zefix.ch/fr/search/entity/welcome>
- Droit : LCD, nLPD, PFPDT, LinkedIn (liens ci-dessus) ; permis B : voir le LISEZMOI, § 0
