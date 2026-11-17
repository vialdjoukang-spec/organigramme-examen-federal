/**
 * Registre central des sources.
 * Chaque carte et chaque étape de cas renvoie à ces identifiants.
 * Champs : titre, editeur, url, type ("suisse" pour la clinique, "pharmaco" pour les sciences
 * fondamentales), lu_le (date de lecture, ISO), portee (ce qui a été lu réellement).
 * Règle : une affirmation clinique sans source "suisse" s'affiche « À vérifier ».
 */
window.JEU = window.JEU || {};
JEU.sources = {
  "hug-smur-sca": {
    categorie: "hôpital universitaire",
    titre: "Protocole SMUR 5.1.1 « Syndrome coronarien aigu », version 1.7b (15.12.2023)",
    editeur: "HUG – Brigade sanitaire cantonale, Genève (références : ESC 2023 ACS)",
    url: "https://www.hug.ch/sites/interhug/files/structures/smur/protocoles/2023.12.15_visio_sca_bg.pdf",
    type: "suisse", lu_le: "2026-11-17",
    portee: "PDF intégral lu (2 pages)."
  },
  "hug-smur-liste": {
    categorie: "hôpital universitaire",
    titre: "Protocoles SMUR – Brigade sanitaire cantonale (journal des modifications)",
    editeur: "HUG, Genève",
    url: "https://www.hug.ch/brigade-sanitaire-cantonale/protocoles",
    type: "suisse", lu_le: "2026-11-17",
    portee: "Page lue : protocole SCA v1.7b du 20.12.2023, « retrait de la double anti-agrégation »."
  },
  "kssg-acs": {
    categorie: "hôpital cantonal",
    titre: "Kardiovaskuläres Manual 2023 – Akutes Koronarsyndrom (ACS)",
    editeur: "Kantonsspital St.Gallen, hôpital cantonal (CC BY 4.0) – bâti sur ESC 2017/2018/2020",
    url: "https://pressbooks.delivros.ch/kvmanual2023/chapter/71-autosave-v1/",
    type: "suisse", lu_le: "2026-11-17",
    portee: "Chapitre lu en entier, y compris l’algorithme 0/1 h (traduit de l’allemand)."
  },
  "kssg-aorte": {
    categorie: "hôpital cantonal",
    titre: "Kardiovaskuläres Manual 2023 – Akutes Aortensyndrom",
    editeur: "Kantonsspital St.Gallen, hôpital cantonal (CC BY 4.0)",
    url: "https://pressbooks.delivros.ch/kvmanual2023/chapter/73-revision-v1/",
    type: "suisse", lu_le: "2026-11-17",
    portee: "Chapitre et algorithme lus (traduit de l’allemand)."
  },
  "kssg-le": {
    categorie: "hôpital cantonal",
    titre: "Kardiovaskuläres Manual 2023 – Tiefe Venenthrombose und Lungenembolie",
    editeur: "Kantonsspital St.Gallen, hôpital cantonal (CC BY 4.0)",
    url: "https://pressbooks.delivros.ch/kvmanual2023/chapter/77-revision-v1/",
    type: "suisse", lu_le: "2026-11-17",
    portee: "Partie « Lungenembolie » lue (traduit de l’allemand)."
  },
  "rms-pericarde-2016": {
    categorie: "revue suisse",
    titre: "Maladies du péricarde : quoi de neuf en 2016 ? (Rev Med Suisse 2016;12:1475-8)",
    editeur: "Revue Médicale Suisse – Service de cardiologie, Hôpital du Valais (Sion)",
    url: "https://www.revmed.ch/view/451280/3831615/RMS_529_1475.pdf",
    type: "suisse", lu_le: "2026-11-17",
    portee: "PDF lu. Attention : article fondé sur ESC 2015 ; une mise à jour ESC existe (À vérifier)."
  },
  "unige-daa-2009": {
    categorie: "faculté de médecine",
    titre: "Approche diagnostique et prise en charge de la dissection aortique aiguë aux urgences (thèse, 2009)",
    editeur: "Université de Genève – Archive ouverte UNIGE (M. Blondon)",
    url: "https://archive-ouverte.unige.ch/unige:2442",
    type: "suisse", lu_le: "2026-11-17",
    portee: "Thèse lue (introduction, clinique, ECG, radiographie, traitement). Source datée."
  },
  "rms-sca-2024": {
    categorie: "revue suisse",
    titre: "Prise en charge du SCA. Recommandations 2023 de la Société européenne de cardiologie (Rev Med Suisse 2024;20:1026-31)",
    editeur: "Revue Médicale Suisse – HUG (Planchat, Musayeb, Degrauwe, Iglesias, Roffi)",
    url: "https://www.revmed.ch/revue-medicale-suisse/2024/revue-medicale-suisse-875/prise-en-charge-du-syndrome-coronarien-aigu.-recommandations-2023-de-la-societe-europeenne-de-cardiologie",
    type: "suisse", lu_le: "2026-11-17",
    portee: "Résumé seul lu (texte intégral réservé aux abonnés)."
  },
  "bs-algo-2026": {
    categorie: "services de sauvetage (hôpitaux cantonaux)",
    titre: "Algorithmen für die präklinische Notfallmedizin, version 2.0 (01.11.2026) – C6 SCA, C7 Aortendissektion",
    editeur: "Rettungsdienst Kantonsspital Baselland, Rettungsdienste NordWestSchweiz, Sanität Basel, Rettungsdienst Winterthur, Einsiedeln (publié par le canton de Bâle-Ville)",
    url: "https://media.bs.ch/original_file/c1c87e093d53450b61e0c7499d06a49fc5476b48/algorithmen-fuer-die-praeklinische-notfallmedizin.pdf",
    type: "suisse", lu_le: "2026-11-17",
    portee: "Chapitres C6, C7 et fiches pharmacologiques ASS et héparine lus (traduit de l’allemand). Doses non reprises."
  },
  "os-antiplaquettaires": {
    titre: "Pharmacology for Nurses – 20.3 Antiplatelets",
    editeur: "OpenStax (CC BY-NC-SA 4.0)",
    url: "https://openstax.org/books/pharmacology/pages/20-3-antiplatelets",
    type: "pharmaco", lu_le: "2026-11-17", portee: "Section lue."
  },
  "os-anticoagulants": {
    titre: "Pharmacology for Nurses – 20.2 Anticoagulants",
    editeur: "OpenStax (CC BY-NC-SA 4.0)",
    url: "https://openstax.org/books/pharmacology/pages/20-2-anticoagulants",
    type: "pharmaco", lu_le: "2026-11-17", portee: "Section lue."
  },
  "os-nitres": {
    titre: "Pharmacology for Nurses – 18.7 Nitrates",
    editeur: "OpenStax (CC BY-NC-SA 4.0)",
    url: "https://openstax.org/books/pharmacology/pages/18-7-nitrates",
    type: "pharmaco", lu_le: "2026-11-17", portee: "Section lue."
  },
  "os-betabloquants": {
    titre: "Pharmacology for Nurses – 18.4 Beta-Adrenergic Blockers",
    editeur: "OpenStax (CC BY-NC-SA 4.0)",
    url: "https://openstax.org/books/pharmacology/pages/18-4-beta-adrenergic-blockers",
    type: "pharmaco", lu_le: "2026-11-17", portee: "Section lue."
  },
  "os-opioides": {
    titre: "Pharmacology for Nurses – 14.3 Opioid Agonists and Antagonists",
    editeur: "OpenStax (CC BY-NC-SA 4.0)",
    url: "https://openstax.org/books/pharmacology/pages/14-3-opioid-agonists-and-antagonists",
    type: "pharmaco", lu_le: "2026-11-17", portee: "Section lue."
  },
  "sp-troponine": {
    titre: "StatPearls – Analytical and Clinical Aspects of Troponin Testing (PMID 29939582)",
    editeur: "StatPearls / NCBI Bookshelf – résumé lu via Europe PMC",
    url: "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:29939582%20AND%20SRC:MED&resultType=core",
    type: "pharmaco", lu_le: "2026-11-17", portee: "Résumé seul lu (NCBI bloque la lecture automatisée)."
  }
};
