# Plan 04 : Micro-SaaS no-code de rédaction de certificats de travail en français pour très petites structures romandes

> **Capital :** 0 à 100 CHF. **Temps :** 8 à 12 h/semaine.
> **Compatibilité avec le permis B :** faible. Exploiter un SaaS est une activité **indépendante** : ce plan n'est possible que si votre permis l'autorise (§ 9.2). La construction du prototype, elle, peut se faire à titre d'apprentissage.
>
> ⚠️ **Avertissement honnête :** le marché est **déjà occupé**, y compris en français (voir § 3). Ce plan ne se justifie que si vous trouvez un angle différenciant **validé par des clients**. Il est classé en dernière position dans le LISEZMOI.

---

## 1. Résumé

En Suisse, l'employé peut demander en tout temps un certificat de travail. Ce certificat porte sur la nature et la durée des rapports de travail, ainsi que sur la qualité du travail et la conduite. L'employé peut aussi demander une simple attestation limitée à la nature et à la durée ([art. 330a CO](https://www.fedlex.admin.ch/eli/cc/27/317_321_377/fr)).

Les très petites structures n'ont souvent pas de service RH : associations, cabinets, commerces, crèches, fiduciaires d'une personne. Vous construisez avec des outils no-code un service simple :

1. un **formulaire guidé** en français ;
2. une **génération assistée par IA** à partir d'une bibliothèque de formulations neutres et bienveillantes ;
3. la **relecture humaine** du résultat, en option ;
4. la **livraison** du document au format Word.

## 2. Pour qui, prérequis et temps hebdomadaire

| Élément | Détail |
|---|---|
| Profil | Intérêt pour le no-code, sens de la rédaction, rigueur |
| Prérequis | Compréhension de l'art. 330a CO et des usages. Relecture de la bibliothèque de formulations par une personne compétente en droit du travail (à payer ou à trouver) |
| Temps | 8 à 12 h/semaine pendant 2 mois pour construire et tester, puis 3 à 5 h/semaine |

## 3. Marché, demande et concurrence (sources vérifiées)

- **Demande structurelle :** 333'297 entreprises suisses ne comptent qu'un seul emploi, et 561'952 sont des microentreprises ([Portail PME, chiffres 2023](https://www.kmu.admin.ch/fr/chiffres-sur-les-pme-entreprises-et-emplois)). Tout employeur est concerné par l'art. 330a CO.
- **Concurrence relevée le 24.10.2026 :**

| Offre | Prix | Langues | Source |
|---|---|---|---|
| ZeugnisPilot | CHF 5 par certificat ; Starter CHF 29/mois (10 certificats) ; Professional CHF 49/mois | DE-CH ; la page indique que **FR, IT et EN sont « en préparation »** ; une page française existe | [Générateur](https://zeugnispilot.ch/de-CH/arbeitszeugnis-generator) · [Tarifs FR](https://zeugnispilot.ch/fr-CH/tarifs) |
| ARKI | à partir de CHF 5 par certificat ; abonnement annuel pour les PME | DE | [arbeitszeugnis-ki.ch](https://arbeitszeugnis-ki.ch/) |
| Experzo | CHF 9.99 par certificat ; CHF 69.90 les 10 (hors TVA) | DE | [experzo.ch](https://www.experzo.ch/arbeitszeugnis-erstellen) |
| WEKA, Manager de certificats | à partir de CHF 298/an (1 à 25 employés), hors TVA | FR, DE, IT, EN | [weka.ch](https://www.weka.ch/fr/ressources-humaines/licenciement-et-certificat-de-travail/manager-de-certificats-de-travail.html) |
| MyCerty | CHF 99 par certificat selon l'extrait de recherche (non confirmé sur la page, rendue en JavaScript) | FR, DE, IT, EN | [mycerty.ch](https://mycerty.ch/de/angebot/) |

> **Conclusion :** un produit purement « générateur » ne serait **pas différenciant**. Les seuls angles possibles sont :
> 1. un service **hybride** (outil, puis relecture humaine en français) à un prix intermédiaire ;
> 2. une **verticale** que vous connaissez : structures de santé non hospitalières (cabinets, physiothérapies, EMS), avec des formulations adaptées aux fonctions d'assistant médical ou de soins, **sans aucune donnée de patient** ;
> 3. ou l'abandon après validation, ce qui est un résultat acceptable.

## 4. Offre exacte et prix (CHF) : hypothèse à valider

| Offre | Contenu | Prix | Justification |
|---|---|---|---|
| **Certificat guidé** | Formulaire, brouillon généré, document Word | **19 CHF** | Au-dessus de ZeugnisPilot et Experzo (5 à 10 CHF) parce que le service est en français et adapté à la verticale santé ; bien en dessous de MyCerty (environ 99 CHF selon l'extrait) |
| **Certificat avec relecture** | Le précédent et une relecture humaine sous 48 h | **59 CHF** | Environ 45 minutes de travail |
| **Pack cabinet** | 5 certificats avec relecture | **229 CHF** | Remise de volume ; reste en dessous de WEKA à 298 CHF/an |

## 5. Outils (pile no-code)

| Brique | Outil | Coût de départ | Lien |
|---|---|---|---|
| Formulaire | Tally | gratuit | <https://tally.so/pricing> |
| Orchestration | Make (1'000 crédits/mois gratuits) ou n8n | gratuit | <https://www.make.com/en/pricing> · <https://n8n.io/pricing/> |
| Génération | API Gemini ou Mistral | offre gratuite ou paiement à l'usage (vérifier les conditions sur les données) | <https://ai.google.dev/gemini-api/docs/pricing> · <https://www.mistral.ai/pricing> |
| Interface ou portail (optionnel) | Softr, Glide | offres gratuites limitées | <https://www.softr.io/pricing> · <https://www.glideapps.com/pricing> |
| Base de données (optionnel) | Supabase (offre gratuite) | gratuit | <https://supabase.com/pricing> |
| Paiement | Lemon Squeezy (5 % + 0,50 USD) ou Stripe (2,9 % + 0,30 CHF) | commission seulement | <https://www.lemonsqueezy.com/pricing> · <https://stripe.com/ch/pricing> |
| Page | Carrd | environ 9 à 19 USD/an | <https://carrd.co/pro> |

<details>
<summary><b>Architecture minimale, sans code (cliquer)</b></summary>

1. Tally recueille : fonction, dates, tâches, et des évaluations sur une échelle de 1 à 5 par critère (qualité, quantité, comportement envers la hiérarchie, les collègues et les clients). Il recueille aussi le motif de départ, en option, et le choix « certificat complet » ou « attestation ».
2. Make reçoit les réponses, puis construit un prompt contraint : utiliser **uniquement** la bibliothèque de formulations validée, interdire tout terme négatif codé, respecter la vérité et la bienveillance.
3. Le LLM produit le texte. Make insère le texte dans un modèle Google Docs ou Word, puis l'envoie à l'employeur.
4. En option, si l'utilisateur a choisi la relecture : une tâche vous est créée.
5. **Données :** les réponses sont supprimées après 30 jours (scénario de purge dans Make). Aucune donnée de santé n'est collectée. Le formulaire porte un avertissement : « Ne saisissez aucune information médicale. »
</details>

## 6. Plan d'action

### Jours 1 à 30 (apprentissage, puis validation de la demande)

| Jour | Tâche | Livrable ou checklist |
|---|---|---|
| 1 | LISEZMOI, § 0 ; question écrite à l'office | ☐ |
| 2 | Lire l'art. 330a CO et la documentation gratuite du Portail PME et des cantons sur le certificat de travail | ☐ Fiche de synthèse |
| 3 | Tester **chaque** concurrent (essais gratuits) et noter les forces et faiblesses, notamment en français | ☐ Tableau de concurrence |
| 4–5 | **10 entretiens de découverte** avec des gérants de petites structures (amis, famille, réseau). Sans rien vendre. Question clé : « Comment avez-vous rédigé votre dernier certificat, et combien de temps cela vous a-t-il pris ? » | ☐ 10 notes d'entretien |
| 6 | Décision intermédiaire : au moins 4 personnes sur 10 décrivent-elles un vrai problème ? Si non, **arrêter ici** | ☐ Décision |
| 7–9 | Construire la bibliothèque de formulations FR (environ 150 phrases par critère et par niveau) | ☐ Bibliothèque v1 |
| 10 | Faire relire la bibliothèque par une personne compétente en droit du travail | ☐ Relecture planifiée |
| 11–13 | Construire le formulaire Tally et le scénario Make, avec des données fictives | ☐ Prototype |
| 14 | 20 tests avec des profils fictifs : vérifier qu'aucune formulation hors bibliothèque n'apparaît | ☐ Rapport de test |
| 15 | Construire la purge à 30 jours et l'avertissement « pas de données médicales » | ☐ |
| 16 | Rédiger les conditions générales, la politique de confidentialité nLPD et la mention « outil d'aide, l'employeur reste responsable du contenu » | ☐ |
| 17 | Page Carrd (brouillon) | ☐ |
| 18 | **Point de contrôle permis** | ☐ |
| 19–20 | Démonstration gratuite du prototype aux 10 personnes interrogées, sans paiement | ☐ Retours |
| 21 | Ajustements | ☐ v2 |
| 22–28 | Si l'activité est autorisée : lancement, avec 10 contacts par jour ouvrable (fiduciaires, cabinets, associations) | ☐ 50 contacts |
| 29 | Premières ventes ? Analyse | ☐ |
| 30 | **Critère de poursuite :** au moins 3 ventes **ou** au moins 1 partenaire fiduciaire intéressé ; sinon, arrêter | ☐ Décision |

### Semaines 5 à 12

| Semaine | Objectif |
|---|---|
| 5–6 | 10 ventes ; mesure du temps de relecture |
| 7 | Partenariat avec une fiduciaire, qui propose votre service à ses clients |
| 8 | Fiches pratiques gratuites (SEO) : « Certificat de travail : 7 erreurs à éviter » |
| 9–10 | Verticale santé : formulations pour assistant médical, assistant en soins, réception |
| 11 | Ajustement des prix |
| 12 | Bilan : abandon ou poursuite |

## 7. Acquisition des premiers clients

- **Canaux :** fiduciaires (prescripteurs) ; associations professionnelles de petites structures ; référencement naturel (SEO) avec des articles pratiques ; réseau personnel.
- **Volume :** 10 contacts par jour ouvrable pendant 2 semaines.
- **Règles :** voir l'annexe 09, § 6.

<details>
<summary><b>Modèle d'e-mail à une fiduciaire (cliquer)</b></summary>

> **Objet :** Certificats de travail en français pour vos petits clients employeurs, en 10 minutes
>
> Bonjour Madame [Nom],
>
> Vos clients employeurs vous demandent-ils parfois de l'aide pour rédiger un certificat de travail ?
>
> J'ai développé un outil simple, en français : un formulaire guidé produit un brouillon conforme aux usages (art. 330a CO), avec une relecture humaine en option. Le certificat guidé coûte 19 CHF, ou 59 CHF avec relecture.
>
> Je vous propose de le tester gratuitement sur un cas fictif : [lien].
>
> Meilleures salutations, [Prénom Nom]
>
> *Si ce n'est pas pertinent, un simple « non merci » suffit.*
</details>

## 8. Modèle financier (estimations, non garanties)

**Hypothèses :**

- Panier moyen de 35 CHF (mélange de certificats guidés et relus).
- Coûts : environ 2 CHF de commission et 0,05 à 0,20 CHF d'API par certificat (à mesurer).
- Carrd environ 19 USD/an.
- Relecture juridique de la bibliothèque : 0 à 300 CHF (hypothèse ; à demander à un juriste).

| Scénario | Mois 3 | Mois 6 | Mois 12 | Cumul sur 12 mois | Hypothèse |
|---|---|---|---|---|---|
| **Bas** | 0 CHF | 35 CHF/mois | 70 CHF/mois | ≈ 400 CHF | 1 à 2 ventes par mois ; probablement abandon |
| **Médian** | 70 CHF | 250 CHF/mois | 500 CHF/mois | ≈ 3'000 CHF | environ 14 ventes par mois au mois 12, grâce à 2 fiduciaires partenaires |
| **Haut** | 200 CHF | 700 CHF/mois | 1'500 CHF/mois | ≈ 9'000 CHF | environ 40 ventes par mois ; SEO efficace |

> **Il n'existe aucune garantie de revenu.** La concurrence peut lancer le français à tout moment ; ZeugnisPilot l'annonce déjà.

## 9. Cadre légal et fiscal suisse

Règles communes : **`09_ANNEXE_cadre_legal_suisse.md`**.

### 9.1 Points spécifiques

- **Art. 330a CO :** un certificat doit être véridique et complet. Votre outil aide l'employeur, qui **reste responsable** du contenu. Écrivez-le dans vos conditions générales ([CO](https://www.fedlex.admin.ch/eli/cc/27/317_321_377/fr)).
- **nLPD :** les évaluations d'un employé sont des données personnelles. Il faut une politique de confidentialité, une durée de conservation courte, un fournisseur d'IA dont les conditions sur les données sont vérifiées, et une analyse des transferts à l'étranger ([nLPD](https://www.fedlex.admin.ch/eli/cc/2022/491/fr) ; [PFPDT, IA](https://www.edoeb.admin.ch/fr/ia-et-protection-des-donnees)).
- **Ne pas donner de conseil juridique individuel :** l'outil fournit des formulations, pas un avis de droit.
- **CGV des plateformes :** Lemon Squeezy ou Stripe ; conditions d'utilisation des API d'IA.

### 9.2 Compatibilité avec le permis B

| Cas | Ce plan |
|---|---|
| **(a)** B pour études, État tiers | **Exploitation : non**, car c'est une activité indépendante ([ZH, Drittstaatsangehörige](https://www.zh.ch/de/wirtschaft-arbeit/erwerbstaetigkeit-auslaender/drittstaaten-angehoerige.html) ; [Directives LEI, ch. 4.4.3 et 4.5.3.2](https://www.sem.admin.ch/dam/sem/fr/data/rechtsgrundlagen/weisungen/auslaender/weisungen-aug-kap4-f.pdf)). **Apprentissage :** un prototype avec des données fictives, non publié, reste à faire confirmer par l'office avant toute démonstration à des tiers |
| **(b)** B pour études, UE/AELE | Activité accessoire de 15 h/semaine au maximum ([OLCP, ch. 4.7](https://www.sem.admin.ch/dam/sem/fr/data/rechtsgrundlagen/weisungen/fza/weisungen-fza-f.pdf.download.pdf/weisungen-fza-f.pdf)). **Faites confirmer par écrit** qu'une activité indépendante est couverte |
| **(c)** B avec activité salariée | État tiers : autorisation (ch. 4.5.3.2). UE/AELE : annonce et nouveau livret B ([SEM, FAQ](https://www.sem.admin.ch/sem/fr/home/themen/fza_schweiz-eu-efta/eu-efta_buerger_schweiz/faq.html)) |
| **(d)** B par regroupement familial | **Oui** (art. 46 LEI ; art. 27 OASA) |

## 10. Risques

| Risque | Mitigation |
|---|---|
| Concurrence déjà en place (élevée) | Validation à J6 et J30, avec des critères d'arrêt stricts |
| Formulation inexacte ou codée | Bibliothèque fermée, relue par une personne compétente, et relecture humaine |
| Données personnelles | Purge à 30 jours, aucune donnée médicale, fournisseur vérifié |
| Coûts d'API | Mesure par certificat ; prix plancher |
| Permis | Ne rien publier ni vendre avant la réponse écrite |

## 11. Indicateurs de succès et critères d'abandon

- **J6 :** au moins 4 personnes interrogées sur 10 décrivent un problème réel.
- **J30 :** au moins 3 ventes ou 1 fiduciaire partenaire.
- **Mois 6 :** au moins 20 ventes par mois.
- **Abandon :** l'un des seuils n'est pas atteint, ou un concurrent sort une offre française équivalente à moins de 10 CHF.

## 12. Sources

- Art. 330a CO : <https://www.fedlex.admin.ch/eli/cc/27/317_321_377/fr>
- Portail PME, chiffres : <https://www.kmu.admin.ch/fr/chiffres-sur-les-pme-entreprises-et-emplois>
- Concurrents : <https://zeugnispilot.ch/de-CH/arbeitszeugnis-generator> · <https://zeugnispilot.ch/fr-CH/tarifs> · <https://arbeitszeugnis-ki.ch/> · <https://www.experzo.ch/arbeitszeugnis-erstellen> · <https://www.weka.ch/fr/ressources-humaines/licenciement-et-certificat-de-travail/manager-de-certificats-de-travail.html> · <https://mycerty.ch/de/angebot/>
- Outils : Tally, Make, n8n, Gemini API, Mistral, Softr, Glide, Supabase, Lemon Squeezy, Stripe, Carrd (liens dans le § 5)
- nLPD, PFPDT ; permis B : voir le LISEZMOI, § 0, et l'annexe 09
