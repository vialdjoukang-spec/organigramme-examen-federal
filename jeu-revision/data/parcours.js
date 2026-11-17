/**
 * Parcours : lots et spécialités, dans l’ordre du plan de production
 * (jeu-revision/docs/PLAN_PRODUCTION.md, Phase 1). Une salle par spécialité.
 * Une spécialité sans fichier data/specialites/<id>.js s’affiche « en préparation ».
 */
window.JEU = window.JEU || {};
JEU.parcours = [
  {
    "id": "A",
    "nom": "Médecine interne",
    "specialites": [
      {
        "id": "cardiologie",
        "nom": "Cardiologie"
      },
      {
        "id": "angiologie",
        "nom": "Angiologie"
      },
      {
        "id": "pneumologie",
        "nom": "Pneumologie"
      },
      {
        "id": "gastro-hepatologie",
        "nom": "Gastro-entérologie et hépatologie"
      },
      {
        "id": "nephrologie",
        "nom": "Néphrologie"
      },
      {
        "id": "endocrinologie-diabetologie",
        "nom": "Endocrinologie et diabétologie"
      },
      {
        "id": "hematologie",
        "nom": "Hématologie"
      },
      {
        "id": "oncologie",
        "nom": "Oncologie"
      },
      {
        "id": "infectiologie",
        "nom": "Infectiologie"
      },
      {
        "id": "rhumatologie",
        "nom": "Rhumatologie"
      },
      {
        "id": "immunologie-allergologie",
        "nom": "Immunologie et allergologie"
      },
      {
        "id": "geriatrie",
        "nom": "Gériatrie"
      }
    ]
  },
  {
    "id": "B",
    "nom": "Neurosciences et santé mentale",
    "specialites": [
      {
        "id": "neurologie",
        "nom": "Neurologie"
      },
      {
        "id": "psychiatrie",
        "nom": "Psychiatrie et psychothérapie"
      },
      {
        "id": "pedopsychiatrie",
        "nom": "Pédopsychiatrie"
      },
      {
        "id": "addictologie",
        "nom": "Addictologie"
      }
    ]
  },
  {
    "id": "C",
    "nom": "Mère et enfant",
    "specialites": [
      {
        "id": "pediatrie",
        "nom": "Pédiatrie"
      },
      {
        "id": "neonatologie",
        "nom": "Néonatologie"
      },
      {
        "id": "gynecologie",
        "nom": "Gynécologie"
      },
      {
        "id": "obstetrique",
        "nom": "Obstétrique"
      }
    ]
  },
  {
    "id": "D",
    "nom": "Chirurgie",
    "specialites": [
      {
        "id": "chirurgie-viscerale",
        "nom": "Chirurgie viscérale"
      },
      {
        "id": "traumatologie-orthopedie",
        "nom": "Traumatologie et orthopédie"
      },
      {
        "id": "urologie",
        "nom": "Urologie"
      },
      {
        "id": "chirurgie-vasculaire",
        "nom": "Chirurgie vasculaire"
      },
      {
        "id": "chirurgie-thoracique-cardiaque",
        "nom": "Chirurgie thoracique et cardiaque"
      },
      {
        "id": "neurochirurgie",
        "nom": "Neurochirurgie"
      }
    ]
  },
  {
    "id": "E",
    "nom": "Organes des sens et peau",
    "specialites": [
      {
        "id": "orl",
        "nom": "ORL"
      },
      {
        "id": "ophtalmologie",
        "nom": "Ophtalmologie"
      },
      {
        "id": "dermatologie-venereologie",
        "nom": "Dermatologie et vénéréologie"
      }
    ]
  },
  {
    "id": "F",
    "nom": "Aigu et fin de vie",
    "specialites": [
      {
        "id": "medecine-urgence",
        "nom": "Médecine d’urgence"
      },
      {
        "id": "anesthesiologie",
        "nom": "Anesthésiologie"
      },
      {
        "id": "medecine-intensive",
        "nom": "Médecine intensive"
      },
      {
        "id": "toxicologie",
        "nom": "Toxicologie"
      },
      {
        "id": "medecine-palliative",
        "nom": "Médecine palliative"
      }
    ]
  },
  {
    "id": "G",
    "nom": "Premier recours et société",
    "specialites": [
      {
        "id": "medecine-famille",
        "nom": "Médecine de famille"
      },
      {
        "id": "medecine-voyages",
        "nom": "Médecine des voyages et tropicale"
      },
      {
        "id": "medecine-travail",
        "nom": "Médecine du travail"
      },
      {
        "id": "medecine-physique",
        "nom": "Médecine physique et réadaptation"
      },
      {
        "id": "prevention-sante-publique",
        "nom": "Prévention et santé publique"
      },
      {
        "id": "medecine-legale",
        "nom": "Médecine légale"
      },
      {
        "id": "genetique-medicale",
        "nom": "Génétique médicale"
      }
    ]
  }
];
