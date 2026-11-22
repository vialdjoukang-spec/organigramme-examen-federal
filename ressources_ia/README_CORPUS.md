# Corpus local de référence — doses suisses et sources

Relevé du 9 novembre 2026 (Europe/Zurich). **Non validé cliniquement** : c'est une source documentaire officielle, pas une validation des doses dans un contexte clinique donné.

## 1. Ce que contient `ressources_ia/`

| Chemin | Contenu |
|---|---|
| `aips/AipsDownload_20261008.xml` | index officiel AIPS (Swissmedic/Refdata), édition du 8.10.2026, 25 255 915 octets : numéro Swissmedic, titulaire, type (SmPC = information professionnelle, PIL = notice patient), URL `files.refdata.ch` |
| `aips/fi_fr/<n° Swissmedic>.txt.gz` | 4631 informations professionnelles en français, texte intégral, une par numéro Swissmedic ; en-tête : nom, numéro, titulaire, URL Refdata |
| `aips/extraits/<n°>.txt` | 330 extraits ciblés déjà lus (SOURCE, CORPUS, URL, passages cités) |
| `aips/erreurs_telechargement.log` | numéros dont la page Refdata répondait 404 au téléchargement |
| `sources_suisses/` | registre des 238 URL des 45 spécialités, référentiels NEO, documents officiels suisses ; voir `sources_suisses/INDEX.md` |

## 2. Règle d'extraction ciblée (bloquante)

1. **Ne jamais ouvrir le XML entier** (25 Mo). Pour trouver un numéro : `grep -i -m5 '<Description>NomDuProduit' aips/AipsDownload_20261008.xml`, puis lire le `<RegulatedAuthorization><Identifier>` du bloc `<Type>SmPC</Type>` ; ou `zgrep -l -i 'nom' aips/fi_fr/*.txt.gz`.
2. Lire uniquement la section utile :
   `zcat aips/fi_fr/<n°>.txt.gz | sed -n '/^Posologie/,/^Contre-indications/p'`
   (même principe pour « Contre-indications », « Grossesse, allaitement », « Mises en garde »).
3. **Citer la dose mot pour mot**, avec le numéro Swissmedic, la forme galénique, l'indication et la population (adulte, enfant, insuffisance rénale ou hépatique) telles qu'écrites dans la section « Posologie/Mode d'emploi ». Pas de paraphrase, pas d'arrondi.
4. La mention « à vérifier » est interdite quand le médicament est dans le corpus. Un usage hors information professionnelle est écrit en clair comme tel, avec sa source.
5. Les doses ne viennent jamais du Compendium ni d'une source non suisse.

## 3. Midodrine (Gutron)

Correction du 9.11.2026 : la midodrine **est présente** dans le corpus. Le numéro 44976 cité auparavant n'existe pas dans l'index AIPS du 8.10.2026 ; les informations professionnelles disponibles sont :
- **Gutron®**, n° Swissmedic **44977**, Cheplapharm Schweiz GmbH : `aips/fi_fr/44977.txt.gz` (section « Posologie/Mode d'emploi », ligne 24) ;
- **MIDODRIN SUBSTIPHARM**, n° Swissmedic **69384**, Leman SKL SA : `aips/fi_fr/69384.txt.gz`.

## 4. Contrôle croisé (miroir Medina)

Le dépôt https://github.com/vialdjoukang-spec/Medina contient, sur la branche `claude/cool-bohr-kcji9o`, le dossier `ref/fi/` : 4 644 informations professionnelles en Markdown (nom de fichier : code ATC, nom, n° Swissmedic ; en-tête : titulaire, substances, date de version, lien Refdata). En cas de doute sur une extraction, comparer la section « Posologie/Mode d'emploi » des deux copies ; si elles divergent, rouvrir l'URL Refdata de l'en-tête.
