/**
 * Spécialité : cardiologie (lot A). Format d’auteur v2 – voir docs/FORMAT_AUTEUR.md.
 * Le corps entre JEU.specialite( … ) est du JSON strict : les outils le lisent sans exécuter de code.
 * Affirmation = { "t": "phrase", "s": ["id-source"] } ; sans source lue : « À vérifier » dans t.
 */
window.JEU = window.JEU || {};
JEU.specialite(
{
 "schema": 2,
 "id": "cardiologie",
 "nom": "Cardiologie",
 "lot": "A",
 "statut": "prototype",
 "catalogue": {
  "complet": false,
  "note": "Catalogue initial du prototype : 6 pathologies. À compléter en lot A depuis des sources suisses."
 },
 "pathologies": [
  {
   "id": "stemi",
   "nom": "Infarctus avec sus-décalage ST (STEMI)",
   "carte": "stemi",
   "ssp": [
    "S2.5",
    "S2.4",
    "F2.6",
    "F2.2"
   ],
   "frequente": "à vérifier",
   "grave": true,
   "justif": [
    {
     "t": "Le temps compte : chaque retard détruit du myocarde.",
     "s": [
      "kssg-acs"
     ]
    }
   ]
  },
  {
   "id": "infarctus-vd",
   "nom": "Infarctus du ventricule droit",
   "carte": "infarctus-vd",
   "ssp": [
    "S2.5",
    "F2.6",
    "F1.1"
   ],
   "frequente": false,
   "grave": "à vérifier",
   "justif": []
  },
  {
   "id": "nstemi",
   "nom": "Syndrome coronarien aigu sans sus-décalage ST",
   "carte": "nstemi",
   "ssp": [
    "S2.5",
    "S2.4",
    "F2.2",
    "F2.6"
   ],
   "frequente": "à vérifier",
   "grave": true,
   "justif": [
    {
     "t": "Les profils à haut risque rejoignent la mortalité du STEMI.",
     "s": [
      "kssg-acs"
     ]
    }
   ]
  },
  {
   "id": "dissection",
   "nom": "Dissection aortique aiguë",
   "carte": "dissection",
   "ssp": [
    "S2.5",
    "F1.1",
    "S5.2"
   ],
   "frequente": false,
   "grave": true,
   "justif": [
    {
     "t": "Le type A atteint une létalité de 1 % par heure pendant 48 h.",
     "s": [
      "kssg-aorte"
     ]
    }
   ]
  },
  {
   "id": "ep",
   "nom": "Embolie pulmonaire",
   "carte": "ep",
   "ssp": [
    "S2.5",
    "S2.7",
    "S2.6"
   ],
   "frequente": "à vérifier",
   "grave": true,
   "justif": [
    {
     "t": "Sans traitement, la mortalité avoisine 30 %.",
     "s": [
      "kssg-le"
     ]
    }
   ]
  },
  {
   "id": "pericardite",
   "nom": "Péricardite aiguë",
   "carte": "pericardite",
   "ssp": [
    "S2.5",
    "S2.10",
    "F2.6"
   ],
   "frequente": true,
   "grave": "à vérifier",
   "justif": [
    {
     "t": "Environ 1 douleur thoracique sur 20 aux urgences relève d’une péricardite.",
     "s": [
      "rms-pericarde-2016"
     ]
    }
   ]
  }
 ],
 "cartes": [
  {
   "id": "stemi",
   "specialite": "cardiologie",
   "type": "pathologie",
   "classe": null,
   "nom": "SCA avec sus-décalage ST",
   "court": "STEMI",
   "cle": "Sus-décalage ST persistant dans ≥ 2 dérivations contiguës",
   "contre": [
    {
     "t": "Les dérivés nitrés ne sont pas indiqués de routine dans le STEMI.",
     "s": [
      "hug-smur-sca"
     ]
    }
   ],
   "pieges": [
    {
     "t": "Le sus-décalage inférieur impose de chercher une extension au ventricule droit (V3R–V4R).",
     "s": [
      "hug-smur-sca"
     ]
    }
   ],
   "rubriques": {
    "fondamentaux": [
     {
      "t": "Un thrombus occlut une artère coronaire ; le myocarde d’aval souffre d’une ischémie transmurale. À vérifier.",
      "s": []
     },
     {
      "t": "Le temps compte : chaque retard détruit du myocarde (« Zeit ist Myokard »).",
      "s": [
       "kssg-acs"
      ],
      "quiz": false
     }
    ],
    "demarche": [
     {
      "t": "La douleur typique siège derrière le sternum, serre « en étau » et descend vers les bras ou monte vers la mâchoire.",
      "s": [
       "hug-smur-sca"
      ]
     }
    ],
    "differentiels": [
     {
      "dx": "Dissection aortique de type A",
      "tue": true,
      "t": "Une dissection aortique de type A peut atteindre la coronaire droite et mimer un STEMI inférieur.",
      "s": [
       "unige-daa-2009",
       "bs-algo-2026"
      ]
     },
     {
      "dx": "Péricardite aiguë",
      "tue": false,
      "t": "Le sus-décalage de la péricardite est diffus ; celui du STEMI suit un territoire coronaire.",
      "s": [
       "rms-pericarde-2016",
       "hug-smur-sca"
      ]
     }
    ],
    "exploration": [
     {
      "t": "Tu enregistres l’ECG 12 dérivations moins de 10 minutes après le premier contact médical.",
      "s": [
       "kssg-acs"
      ],
      "quiz": false
     },
     {
      "t": "Tu prélèves la troponine, mais tu n’attends pas son résultat pour décider de la reperfusion.",
      "s": [
       "kssg-acs"
      ]
     },
     {
      "t": "L’échocardiographie aide au diagnostic, mais elle ne doit pas retarder le transfert en coronarographie.",
      "s": [
       "kssg-acs"
      ],
      "quiz": false
     }
    ],
    "diagnostic": [
     {
      "t": "Le critère ECG exige un sus-décalage ST nouveau au point J dans ≥ 2 dérivations contiguës : ≥ 1 mm hors V2–V3 ; en V2–V3, ≥ 2,5 mm (homme < 40 ans), ≥ 2 mm (homme ≥ 40 ans), ≥ 1,5 mm (femme).",
      "s": [
       "hug-smur-sca"
      ]
     },
     {
      "t": "Un nouveau bloc de branche, droit ou gauche, chez un patient en ischémie active, vaut un STEMI.",
      "s": [
       "hug-smur-sca"
      ]
     }
    ],
    "priseEnCharge": [
     {
      "t": "L’intervention coronarienne percutanée (ICP) primaire constitue la reperfusion préférée.",
      "s": [
       "kssg-acs"
      ]
     },
     {
      "t": "Le délai entre le premier contact (hôpital externe ou ambulance) et l’ICP doit rester ≤ 90 min, acceptable jusqu’à 120 min.",
      "s": [
       "kssg-acs"
      ]
     },
     {
      "t": "La fibrinolyse se discute si l’ICP n’est pas réalisable dans les 120 min (âge < 75 ans, douleur < 3 h, sans choc, risque hémorragique bas).",
      "s": [
       "kssg-acs"
      ]
     },
     {
      "t": "Le protocole genevois associe l’acide acétylsalicylique et l’héparine dès le STEMI posé.",
      "s": [
       "hug-smur-sca"
      ]
     }
    ],
    "suivi": [
     {
      "t": "Tu transportes le patient vers un centre qui pratique l’ICP.",
      "s": [
       "bs-algo-2026"
      ]
     }
    ],
    "explication": []
   },
   "noteFrequence": {
    "t": "Aucune donnée suisse de fréquence n’a été lue. À vérifier.",
    "s": []
   },
   "sources": [
    "hug-smur-sca",
    "kssg-acs",
    "unige-daa-2009"
   ]
  },
  {
   "id": "nstemi",
   "specialite": "cardiologie",
   "type": "pathologie",
   "classe": null,
   "nom": "SCA sans sus-décalage ST",
   "court": "NSTEMI",
   "cle": "Troponine hs qui monte, sans sus-décalage ST",
   "contre": [
    {
     "t": "Le manuel saint-gallois ne donne pas de double antiagrégation systématique avant l’exploration invasive.",
     "s": [
      "kssg-acs"
     ]
    }
   ],
   "pieges": [
    {
     "t": "Origine coronarienne douteuse et aucune autre piste : tu traites comme un SCA.",
     "s": [
      "hug-smur-sca"
     ]
    }
   ],
   "rubriques": {
    "fondamentaux": [
     {
      "t": "Une ischémie myocardique non transmurale libère la troponine ; l’ECG ne montre pas de sus-décalage persistant.",
      "s": [
       "kssg-acs"
      ]
     }
    ],
    "demarche": [
     {
      "t": "Le pronostic varie beaucoup ; les profils à haut risque rejoignent la mortalité du STEMI.",
      "s": [
       "kssg-acs"
      ]
     }
    ],
    "differentiels": [
     {
      "dx": "Lésion myocardique sans infarctus",
      "tue": false,
      "t": "Une troponine élevée ne signe pas toujours un infarctus : le manuel distingue infarctus et lésion myocardique.",
      "s": [
       "kssg-acs"
      ]
     }
    ],
    "exploration": [
     {
      "t": "L’algorithme 0/1 h exige un dosage de troponine hs validé ; il classe le patient en exclusion, observation ou inclusion.",
      "s": [
       "kssg-acs"
      ]
     },
     {
      "t": "L’échocardiographie recherche une dysfonction ventriculaire gauche et un diagnostic différentiel.",
      "s": [
       "kssg-acs"
      ],
      "quiz": false
     }
    ],
    "diagnostic": [
     {
      "t": "Le diagnostic d’infarctus repose sur une troponine > 99e percentile avec au moins un critère d’ischémie (symptômes, ECG, onde Q, trouble de cinétique).",
      "s": [
       "kssg-acs"
      ],
      "quiz": false
     }
    ],
    "priseEnCharge": [
     {
      "t": "Une coronarographie en urgence (< 2 h) se discute si la douleur persiste, si le patient est instable, en insuffisance cardiaque aiguë ou en cas de sous-décalages diffus avec sus-décalage en aVR.",
      "s": [
       "kssg-acs"
      ]
     },
     {
      "t": "Sinon, l’équipe choisit une stratégie invasive précoce (< 24 h) ou différée avec le cardiologue.",
      "s": [
       "kssg-acs"
      ],
      "quiz": false
     },
     {
      "t": "Les nitrés traitent la douleur angineuse du SCA sans sus-décalage ST.",
      "s": [
       "hug-smur-sca"
      ],
      "quiz": false
     }
    ],
    "suivi": [
     {
      "t": "Critères d’hospitalisation et de suivi à sourcer. À vérifier.",
      "s": []
     }
    ],
    "explication": []
   },
   "noteFrequence": {
    "t": "Aucune donnée suisse de fréquence n’a été lue. À vérifier.",
    "s": []
   },
   "sources": [
    "kssg-acs",
    "hug-smur-sca"
   ]
  },
  {
   "id": "dissection",
   "specialite": "cardiologie",
   "type": "pathologie",
   "classe": null,
   "nom": "Dissection aortique aiguë",
   "court": "Dissection",
   "cle": "Douleur brutale déchirante + asymétrie tensionnelle entre les bras",
   "contre": [
    {
     "t": "Tu ne donnes ni antiagrégant, ni héparine, ni fibrinolyse tant que la dissection suspectée n’est pas exclue par l’imagerie. À vérifier : formulation explicite non trouvée dans une source suisse lue.",
     "s": []
    },
    {
     "t": "La thèse genevoise rapporte un décès après aspirine, clopidogrel et énoxaparine donnés sur une suspicion de SCA qui cachait une dissection de type A.",
     "s": [
      "unige-daa-2009"
     ]
    }
   ],
   "pieges": [
    {
     "t": "Hypotension, choc ou tamponnade prédisent la mortalité de la dissection de type A.",
     "s": [
      "unige-daa-2009"
     ]
    },
    {
     "t": "Un tiers seulement des ECG reste normal ; un sus-décalage ST apparaît dans environ 7 % des cas.",
     "s": [
      "unige-daa-2009"
     ]
    },
    {
     "t": "Des cas publiés décrivent une fibrinolyse donnée à tort sur un faux diagnostic de SCA.",
     "s": [
      "unige-daa-2009"
     ]
    },
    {
     "t": "Les D-dimères ne suffisaient pas, en 2009, à exclure la dissection en pratique clinique.",
     "s": [
      "unige-daa-2009"
     ]
    }
   ],
   "rubriques": {
    "fondamentaux": [
     {
      "t": "Une rupture de l’intima laisse le sang pénétrer dans la média et crée un faux chenal.",
      "s": [
       "kssg-aorte"
      ]
     },
     {
      "t": "Le type A (Stanford) touche l’aorte ascendante ; le type B l’épargne.",
      "s": [
       "kssg-aorte"
      ],
      "echelon": 1
     }
    ],
    "demarche": [
     {
      "t": "La douleur thoracique débute de façon suraiguë, déchirante ou poignardante, parfois migratrice (85 % des cas).",
      "s": [
       "kssg-aorte"
      ]
     },
     {
      "t": "La pression artérielle diffère entre les deux bras, ou entre membres supérieurs et inférieurs.",
      "s": [
       "kssg-aorte"
      ]
     },
     {
      "t": "Le patient peut être hypertendu ou hypotendu (tamponnade, atteinte des troncs supra-aortiques).",
      "s": [
       "kssg-aorte"
      ]
     },
     {
      "t": "La radiographie du thorax montre un élargissement du médiastin dans environ deux tiers des cas.",
      "s": [
       "unige-daa-2009"
      ]
     }
    ],
    "differentiels": [
     {
      "dx": "STEMI inférieur",
      "tue": true,
      "t": "Une dissection de type A peut comprimer l’ostium coronaire, surtout la coronaire droite, et mimer un STEMI inférieur.",
      "s": [
       "unige-daa-2009",
       "bs-algo-2026"
      ]
     }
    ],
    "exploration": [
     {
      "t": "L’angio-CT thoraco-abdominal injecté confirme ou exclut le diagnostic ; il reste disponible en permanence.",
      "s": [
       "kssg-aorte"
      ]
     },
     {
      "t": "L’échocardiographie transœsophagienne sert d’alternative ; elle visualise l’insuffisance aortique.",
      "s": [
       "kssg-aorte"
      ]
     },
     {
      "t": "Aucun élément clinique ni examen de base n’exclut à lui seul la dissection.",
      "s": [
       "unige-daa-2009"
      ]
     }
    ],
    "diagnostic": [
     {
      "t": "L’angio-CT thoraco-abdominal injecté confirme ou exclut le diagnostic ; il reste disponible en permanence.",
      "s": [
       "kssg-aorte"
      ]
     }
    ],
    "priseEnCharge": [
     {
      "t": "Une hypotension ou un choc évoque une complication : tamponnade par passage de sang dans le péricarde, ou rupture.",
      "s": [
       "unige-daa-2009",
       "kssg-aorte"
      ]
     },
     {
      "t": "En cas d’hypotension ou de bradycardie, tu ne baisses pas la TA et tu ne donnes pas de bêtabloquant.",
      "s": [
       "bs-algo-2026"
      ]
     },
     {
      "t": "L’algorithme préhospitalier suisse baisse la TA seulement si la TAS dépasse 120 mmHg, et réserve le bêtabloquant à une FC > 60/min.",
      "s": [
       "bs-algo-2026"
      ]
     },
     {
      "t": "Avec une TA normale ou haute, tu vises une TAS de 100–120 mmHg : bêtabloquant d’abord, vasodilatateur ensuite.",
      "s": [
       "kssg-aorte"
      ]
     },
     {
      "t": "Du liquide dans le péricarde, la plèvre ou le médiastin signe une urgence extrême : la mortalité dépasse 50 %.",
      "s": [
       "unige-daa-2009"
      ]
     },
     {
      "t": "Tu traites la douleur par opiacé, puis benzodiazépine si besoin.",
      "s": [
       "kssg-aorte"
      ]
     },
     {
      "t": "Le type A part en chirurgie cardiaque urgente : la létalité atteint 1 % par heure pendant les 48 premières heures.",
      "s": [
       "kssg-aorte"
      ]
     },
     {
      "t": "Le type B non compliqué reçoit un traitement médical ; le type B compliqué relève surtout de l’endovasculaire.",
      "s": [
       "kssg-aorte"
      ]
     }
    ],
    "suivi": [
     {
      "t": "Une suspicion typique (écart de TAS > 20 mmHg, douleur intense entre les omoplates) justifie un transport direct vers un centre de chirurgie cardiaque.",
      "s": [
       "bs-algo-2026"
      ]
     }
    ],
    "explication": []
   },
   "noteFrequence": {
    "t": "La dissection aortique reste rare : environ 6 / 100 000 personnes par an.",
    "s": [
     "kssg-aorte"
    ]
   },
   "sources": [
    "kssg-aorte",
    "unige-daa-2009",
    "bs-algo-2026"
   ]
  },
  {
   "id": "ep",
   "specialite": "cardiologie",
   "type": "pathologie",
   "classe": null,
   "nom": "Embolie pulmonaire",
   "court": "EP",
   "cle": "Choc ? Sinon : probabilité clinique, puis D-dimères ou CT",
   "contre": [],
   "pieges": [
    {
     "t": "Les biomarqueurs cardiaques (troponine, BNP) entrent dans la stratification du risque de l’EP.",
     "s": [
      "kssg-le"
     ]
    }
   ],
   "rubriques": {
    "fondamentaux": [
     {
      "t": "Environ 90 % des embolies pulmonaires proviennent d’une thrombose veineuse profonde (données d’autopsie).",
      "s": [
       "kssg-le"
      ]
     }
    ],
    "demarche": [
     {
      "t": "Le score de Genève modifié ou le score de Wells estiment la probabilité clinique.",
      "s": [
       "kssg-le"
      ]
     },
     {
      "t": "Sans traitement, la mortalité avoisine 30 % ; avec traitement, elle descend à 2–11 %.",
      "s": [
       "kssg-le"
      ]
     }
    ],
    "differentiels": [
     {
      "dx": "Diagnostics différentiels",
      "tue": false,
      "t": "Différentiels discriminants à sourcer (source suisse). À vérifier.",
      "s": []
     }
    ],
    "exploration": [
     {
      "t": "Tu évalues d’abord le choc : un patient instable suit l’algorithme dédié.",
      "s": [
       "kssg-le"
      ]
     },
     {
      "t": "Les D-dimères servent seulement à exclure ; le seuil peut s’ajuster à l’âge (âge × 10 µg/l après 50 ans).",
      "s": [
       "kssg-le"
      ]
     },
     {
      "t": "Avec une probabilité élevée, tu renonces aux D-dimères et tu demandes l’imagerie.",
      "s": [
       "kssg-le"
      ]
     },
     {
      "t": "L’angio-CT pulmonaire reste l’examen de référence ; la scintigraphie V/Q SPECT le remplace en cas de contre-indication ou de grossesse.",
      "s": [
       "kssg-le"
      ]
     }
    ],
    "diagnostic": [
     {
      "t": "L’angio-CT pulmonaire reste l’examen de référence ; la scintigraphie V/Q SPECT le remplace en cas de contre-indication ou de grossesse.",
      "s": [
       "kssg-le"
      ]
     },
     {
      "t": "Une probabilité élevée et des D-dimères positifs ne suffisent pas au diagnostic.",
      "s": [
       "kssg-le"
      ]
     }
    ],
    "priseEnCharge": [
     {
      "t": "En cas d’instabilité hémodynamique, tu rouvres l’artère : thrombolyse, fragmentation par cathéter ou embolectomie.",
      "s": [
       "kssg-le"
      ]
     },
     {
      "t": "Dans les formes moins graves, tu débutes vite l’anticoagulation.",
      "s": [
       "kssg-le"
      ]
     }
    ],
    "suivi": [
     {
      "t": "Critères d’hospitalisation ou de traitement ambulatoire à sourcer. À vérifier.",
      "s": []
     }
    ],
    "explication": []
   },
   "noteFrequence": {
    "t": "Aucune donnée suisse de fréquence n’a été lue. À vérifier.",
    "s": []
   },
   "sources": [
    "kssg-le"
   ]
  },
  {
   "id": "pericardite",
   "specialite": "cardiologie",
   "type": "pathologie",
   "classe": null,
   "nom": "Péricardite aiguë",
   "court": "Péricardite",
   "cle": "Douleur respiro-dépendante + sus-décalage ST diffus",
   "contre": [
    {
     "t": "Tu ne commences pas par un corticoïde.",
     "s": [
      "rms-pericarde-2016"
     ]
    }
   ],
   "pieges": [
    {
     "t": "La source lue date de 2016 ; vérifie la mise à jour européenne plus récente. À vérifier.",
     "s": []
    }
   ],
   "rubriques": {
    "fondamentaux": [
     {
      "t": "Une inflammation du péricarde, le plus souvent idiopathique ou virale dans les pays industrialisés, provoque la douleur.",
      "s": [
       "rms-pericarde-2016"
      ]
     }
    ],
    "demarche": [
     {
      "t": "La douleur respiro-dépendante apparaît dans plus de 85–90 % des cas ; le frottement dans moins d’un tiers.",
      "s": [
       "rms-pericarde-2016"
      ]
     },
     {
      "t": "La CRP, la VS ou les leucocytes renforcent le diagnostic.",
      "s": [
       "rms-pericarde-2016"
      ]
     }
    ],
    "differentiels": [
     {
      "dx": "STEMI",
      "tue": true,
      "t": "Le sus-décalage de la péricardite est diffus, alors que celui du STEMI suit un territoire coronaire.",
      "s": [
       "rms-pericarde-2016",
       "hug-smur-sca"
      ]
     }
    ],
    "exploration": [
     {
      "t": "Les experts préconisent une échocardiographie systématique.",
      "s": [
       "rms-pericarde-2016"
      ]
     }
    ],
    "diagnostic": [
     {
      "t": "Le diagnostic exige au moins 2 critères sur 4 : douleur respiro-dépendante, frottement, sus-décalage ST diffus ou sous-décalage PR, épanchement.",
      "s": [
       "rms-pericarde-2016"
      ]
     }
    ],
    "priseEnCharge": [
     {
      "t": "Dès la première poussée, tu associes la colchicine à l’AINS ou à l’aspirine.",
      "s": [
       "rms-pericarde-2016"
      ]
     }
    ],
    "suivi": [
     {
      "t": "Critères d’hospitalisation et de suivi à sourcer. À vérifier.",
      "s": []
     }
    ],
    "explication": []
   },
   "noteFrequence": {
    "t": "Environ 1 douleur thoracique sur 20 vue aux urgences relève d’une péricardite.",
    "s": [
     "rms-pericarde-2016"
    ]
   },
   "sources": [
    "rms-pericarde-2016"
   ]
  },
  {
   "id": "infarctus-vd",
   "specialite": "cardiologie",
   "type": "pathologie",
   "classe": null,
   "nom": "Infarctus du ventricule droit",
   "court": "Infarctus VD",
   "cle": "STEMI inférieur + sus-décalage en V3R–V4R",
   "contre": [
    {
     "t": "Les dérivés nitrés sont contre-indiqués en cas d’infarctus droit.",
     "s": [
      "hug-smur-sca"
     ]
    },
    {
     "t": "Les nitrés sont aussi contre-indiqués si la TA systolique < 110 mmHg ou après un inhibiteur de la PDE5 < 48 h.",
     "s": [
      "hug-smur-sca"
     ]
    }
   ],
   "pieges": [
    {
     "t": "Le manuel de pharmacologie range lui aussi l’infarctus du VD parmi les contre-indications des nitrés.",
     "s": [
      "os-nitres"
     ]
    }
   ],
   "rubriques": {
    "fondamentaux": [
     {
      "t": "L’occlusion proximale de la coronaire droite peut priver le ventricule droit de perfusion. À vérifier.",
      "s": []
     }
    ],
    "demarche": [
     {
      "t": "L’hypotension avec poumons clairs oriente vers une atteinte droite. À vérifier.",
      "s": []
     }
    ],
    "differentiels": [
     {
      "dx": "STEMI inférieur sans atteinte droite",
      "tue": false,
      "t": "Devant un STEMI inférieur douteux, tu ajoutes V3R et V4R, sans perdre de temps.",
      "s": [
       "hug-smur-sca"
      ]
     }
    ],
    "exploration": [
     {
      "t": "Devant un STEMI inférieur douteux, tu ajoutes V3R et V4R, sans perdre de temps.",
      "s": [
       "hug-smur-sca"
      ]
     }
    ],
    "diagnostic": [
     {
      "t": "Devant un STEMI inférieur douteux, tu ajoutes V3R et V4R, sans perdre de temps.",
      "s": [
       "hug-smur-sca"
      ]
     }
    ],
    "priseEnCharge": [
     {
      "t": "Tu reperfuses comme pour tout STEMI : ICP primaire préférée.",
      "s": [
       "kssg-acs"
      ]
     }
    ],
    "suivi": [
     {
      "t": "Tu transportes le patient vers un centre qui pratique l’ICP.",
      "s": [
       "bs-algo-2026"
      ]
     }
    ],
    "explication": []
   },
   "noteFrequence": {
    "t": "Aucune donnée suisse de fréquence n’a été lue. À vérifier.",
    "s": []
   },
   "sources": [
    "hug-smur-sca",
    "kssg-acs",
    "os-nitres"
   ]
  },
  {
   "id": "ecg",
   "specialite": "cardiologie",
   "type": "examen",
   "classe": "Examen",
   "nom": "ECG 12 dérivations",
   "court": "ECG 12 D",
   "cle": "Moins de 10 min après le premier contact",
   "contre": [
    {
     "t": "L’ECG n’a pas de contre-indication ; il ne doit jamais retarder un geste vital. À vérifier.",
     "s": []
    }
   ],
   "pieges": [
    {
     "t": "Un sous-décalage ST de V1 à V3 peut cacher un STEMI postérieur : pense aux dérivations postérieures.",
     "s": [
      "hug-smur-sca"
     ]
    }
   ],
   "rubriques": {
    "fondamentaux": [
     {
      "t": "L’ECG enregistre l’activité électrique du cœur. À vérifier.",
      "s": []
     },
     {
      "t": "Des modifications significatives du segment ST ou de l’onde T comptent parmi les critères d’ischémie.",
      "s": [
       "kssg-acs"
      ]
     }
    ],
    "demarche": [
     {
      "t": "Tu le fais chez tout patient avec une douleur thoracique, dès que possible.",
      "s": [
       "hug-smur-sca"
      ]
     }
    ],
    "differentiels": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "exploration": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "diagnostic": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "priseEnCharge": [
     {
      "t": "Tu l’obtiens en moins de 10 minutes et tu le répètes après 10 minutes.",
      "s": [
       "kssg-acs"
      ]
     },
     {
      "t": "Tu refais un ECG si la douleur s’améliore sous nitrés.",
      "s": [
       "hug-smur-sca"
      ]
     }
    ],
    "suivi": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "explication": []
   },
   "noteFrequence": {
    "t": "Chaque douleur thoracique reçoit son ECG 12 dérivations.",
    "s": [
     "hug-smur-sca"
    ]
   },
   "sources": [
    "hug-smur-sca",
    "kssg-acs"
   ]
  },
  {
   "id": "derivations-droites",
   "specialite": "cardiologie",
   "type": "examen",
   "classe": "Examen",
   "nom": "Dérivations droites V3R–V4R",
   "court": "V3R–V4R",
   "cle": "À faire devant tout STEMI inférieur douteux",
   "contre": [
    {
     "t": "Ce geste n’a pas de contre-indication connue. À vérifier.",
     "s": []
    }
   ],
   "pieges": [
    {
     "t": "Une extension droite interdit les nitrés.",
     "s": [
      "hug-smur-sca"
     ]
    }
   ],
   "rubriques": {
    "fondamentaux": [
     {
      "t": "Les électrodes placées à droite explorent la paroi du ventricule droit. À vérifier.",
      "s": []
     }
    ],
    "demarche": [
     {
      "t": "Tu les enregistres en cas de doute sur un STEMI inférieur.",
      "s": [
       "hug-smur-sca"
      ]
     }
    ],
    "differentiels": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "exploration": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "diagnostic": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "priseEnCharge": [
     {
      "t": "Tu les enregistres seulement si cela ne freine pas la suite.",
      "s": [
       "hug-smur-sca"
      ]
     }
    ],
    "suivi": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "explication": []
   },
   "noteFrequence": {
    "t": "Aucune donnée suisse de fréquence n’a été lue. À vérifier.",
    "s": []
   },
   "sources": [
    "hug-smur-sca"
   ]
  },
  {
   "id": "angio-ct",
   "specialite": "cardiologie",
   "type": "examen",
   "classe": "Imagerie",
   "nom": "Angio-CT aortique",
   "court": "Angio-CT",
   "cle": "Confirme ou exclut la dissection",
   "contre": [
    {
     "t": "L’angio-CT évalue mal l’insuffisance aortique d’une dissection de type A.",
     "s": [
      "kssg-aorte"
     ]
    }
   ],
   "pieges": [
    {
     "t": "Une suspicion suffit pour imager, même quand la probabilité clinique paraît basse.",
     "s": [
      "unige-daa-2009"
     ]
    }
   ],
   "rubriques": {
    "fondamentaux": [
     {
      "t": "Le produit de contraste opacifie la lumière aortique et révèle le voile intimal et le faux chenal. À vérifier.",
      "s": []
     }
    ],
    "demarche": [
     {
      "t": "Tu le demandes devant toute suspicion de syndrome aortique aigu.",
      "s": [
       "kssg-aorte"
      ]
     }
    ],
    "differentiels": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "exploration": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "diagnostic": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "priseEnCharge": [
     {
      "t": "L’angio-CT thoraco-abdominal injecté reste la première imagerie ; il est disponible en permanence.",
      "s": [
       "kssg-aorte"
      ]
     },
     {
      "t": "L’ETO sert d’alternative ; elle évalue mieux l’insuffisance aortique.",
      "s": [
       "kssg-aorte"
      ]
     }
    ],
    "suivi": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "explication": []
   },
   "noteFrequence": {
    "t": "Aucune donnée suisse de fréquence n’a été lue. À vérifier.",
    "s": []
   },
   "sources": [
    "kssg-aorte",
    "unige-daa-2009"
   ]
  },
  {
   "id": "troponine",
   "specialite": "cardiologie",
   "type": "examen",
   "classe": "Biologie",
   "nom": "Troponine hs (0/1 h)",
   "court": "Troponine hs",
   "cle": "Ne retarde jamais la reperfusion d’un STEMI",
   "contre": [
    {
     "t": "Tu n’attends pas le résultat pour décider la reperfusion d’un STEMI.",
     "s": [
      "kssg-acs"
     ]
    }
   ],
   "pieges": [
    {
     "t": "Les seuils dépendent du dosage utilisé ; chaque hôpital a ses valeurs.",
     "s": [
      "kssg-acs"
     ]
    }
   ],
   "rubriques": {
    "fondamentaux": [
     {
      "t": "Les dosages hs mesurent des traces de troponine, de l’ordre du ng/l ; ils rendent possibles des algorithmes d’exclusion rapides.",
      "s": [
       "sp-troponine"
      ]
     }
    ],
    "demarche": [
     {
      "t": "Tu prélèves les marqueurs cardiaques de routine devant une suspicion de SCA.",
      "s": [
       "kssg-acs"
      ]
     }
    ],
    "differentiels": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "exploration": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "diagnostic": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "priseEnCharge": [
     {
      "t": "L’algorithme 0/1 h s’applique seulement avec un dosage hs validé.",
      "s": [
       "kssg-acs"
      ]
     }
    ],
    "suivi": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "explication": []
   },
   "noteFrequence": {
    "t": "Le prélèvement reste systématique devant une suspicion de SCA.",
    "s": [
     "kssg-acs"
    ]
   },
   "sources": [
    "kssg-acs",
    "sp-troponine"
   ]
  },
  {
   "id": "aspirine",
   "specialite": "cardiologie",
   "type": "traitement",
   "classe": "Antiagrégant",
   "nom": "Acide acétylsalicylique",
   "court": "Aspirine",
   "cle": "Seulement après exclusion d’une dissection suspectée",
   "contre": [
    {
     "t": "L’allergie connue la contre-indique.",
     "s": [
      "hug-smur-sca"
     ]
    },
    {
     "t": "Une dissection suspectée et non exclue l’interdit. À vérifier : formulation explicite non trouvée dans une source suisse lue.",
     "s": []
    }
   ],
   "pieges": [
    {
     "t": "Le même blocage prive l’estomac de ses prostaglandines protectrices ; un ulcère peut saigner.",
     "s": [
      "os-antiplaquettaires"
     ]
    }
   ],
   "rubriques": {
    "fondamentaux": [
     {
      "t": "L’aspirine bloque de façon définitive une enzyme de la plaquette ; privée de thromboxane A2, la plaquette s’agrège moins pendant 7 à 10 jours.",
      "s": [
       "bs-algo-2026",
       "os-antiplaquettaires"
      ]
     }
    ],
    "demarche": [
     {
      "t": "Tu la donnes dans le STEMI et le SCA sans sus-décalage ST.",
      "s": [
       "hug-smur-sca"
      ]
     }
    ],
    "differentiels": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "exploration": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "diagnostic": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "priseEnCharge": [
     {
      "t": "Tu ne la redonnes pas si le patient en prend déjà.",
      "s": [
       "kssg-acs"
      ]
     },
     {
      "t": "La voie orale remplace la voie IV si la voie veineuse est impossible.",
      "s": [
       "hug-smur-sca"
      ]
     }
    ],
    "suivi": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "explication": []
   },
   "noteFrequence": {
    "t": "Le protocole genevois l’administre dans le STEMI et le SCA sans sus-décalage ST.",
    "s": [
     "hug-smur-sca"
    ]
   },
   "sources": [
    "hug-smur-sca",
    "kssg-acs",
    "os-antiplaquettaires"
   ]
  },
  {
   "id": "hnf",
   "specialite": "cardiologie",
   "type": "traitement",
   "classe": "Anticoagulant",
   "nom": "Héparine non fractionnée",
   "court": "HNF",
   "cle": "Pas de double dose : vérifie HBPM ou ACO déjà reçus",
   "contre": [
    {
     "t": "Patient déjà héparinisé, déjà chargé en HBPM ou sous anticoagulant oral : tu ne la donnes pas.",
     "s": [
      "hug-smur-sca"
     ]
    },
    {
     "t": "Une dissection suspectée et non exclue l’interdit. À vérifier : formulation explicite non trouvée dans une source suisse lue.",
     "s": []
    }
   ],
   "pieges": [
    {
     "t": "Un antécédent de TIH de type 2 impose un autre anticoagulant (argatroban).",
     "s": [
      "kssg-acs"
     ]
    }
   ],
   "rubriques": {
    "fondamentaux": [
     {
      "t": "L’héparine s’attache à l’antithrombine et renforce ce frein naturel ; plusieurs facteurs, dont la thrombine, cessent d’agir.",
      "s": [
       "bs-algo-2026",
       "os-anticoagulants"
      ]
     }
    ],
    "demarche": [
     {
      "t": "Tu la donnes dans le STEMI et le NSTEMI documenté.",
      "s": [
       "hug-smur-sca"
      ]
     }
    ],
    "differentiels": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "exploration": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "diagnostic": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "priseEnCharge": [
     {
      "t": "L’héparine non fractionnée accompagne le transfert vers l’ICP.",
      "s": [
       "kssg-acs"
      ]
     }
    ],
    "suivi": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "explication": []
   },
   "noteFrequence": {
    "t": "Le protocole genevois l’administre dans le STEMI et le NSTEMI.",
    "s": [
     "hug-smur-sca"
    ]
   },
   "sources": [
    "hug-smur-sca",
    "kssg-acs",
    "os-anticoagulants"
   ]
  },
  {
   "id": "p2y12",
   "specialite": "cardiologie",
   "type": "traitement",
   "classe": "Antiagrégant",
   "nom": "Inhibiteur P2Y12",
   "court": "P2Y12",
   "cle": "Moment de la charge : décision avec le cardiologue",
   "contre": [
    {
     "t": "Le prasugrel est contre-indiqué après un AVC ou un AIT.",
     "s": [
      "kssg-acs"
     ]
    },
    {
     "t": "Une dissection suspectée et non exclue l’interdit. À vérifier : formulation explicite non trouvée dans une source suisse lue.",
     "s": []
    }
   ],
   "pieges": [
    {
     "t": "Les recommandations ont évolué (ESC 2020 → 2023) : vérifie le protocole local actuel. À vérifier.",
     "s": []
    }
   ],
   "rubriques": {
    "fondamentaux": [
     {
      "t": "Ce médicament occupe le site de l’ADP sur la plaquette ; le signal d’activation ne passe plus.",
      "s": [
       "os-antiplaquettaires"
      ]
     }
    ],
    "demarche": [
     {
      "t": "Il complète l’aspirine (double antiagrégation) après un SCA.",
      "s": [
       "kssg-acs"
      ]
     }
    ],
    "differentiels": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "exploration": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "diagnostic": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "priseEnCharge": [
     {
      "t": "Le manuel saint-gallois privilégie le ticagrélor en phase aiguë ; prasugrel et clopidogrel servent d’alternatives.",
      "s": [
       "kssg-acs"
      ]
     },
     {
      "t": "Les HUG ont retiré la double antiagrégation de leur protocole préhospitalier SCA en décembre 2023.",
      "s": [
       "hug-smur-liste"
      ]
     }
    ],
    "suivi": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "explication": []
   },
   "noteFrequence": {
    "t": "Aucune donnée suisse de fréquence n’a été lue. À vérifier.",
    "s": []
   },
   "sources": [
    "kssg-acs",
    "hug-smur-liste",
    "os-antiplaquettaires"
   ]
  },
  {
   "id": "nitres",
   "specialite": "cardiologie",
   "type": "traitement",
   "classe": "Vasodilatateur",
   "nom": "Dérivés nitrés",
   "court": "Nitrés",
   "cle": "Interdits si TAS < 110, infarctus droit ou IPDE5 < 48 h",
   "contre": [
    {
     "t": "Ils sont contre-indiqués si la TA systolique < 110 mmHg, en cas d’infarctus droit ou après un IPDE5 < 48 h.",
     "s": [
      "hug-smur-sca"
     ]
    },
    {
     "t": "Avec un inhibiteur de la PDE5, les deux vasodilatations s’additionnent et la TA peut s’effondrer.",
     "s": [
      "os-nitres"
     ]
    }
   ],
   "pieges": [
    {
     "t": "Tu refais un ECG si la douleur s’améliore sous nitrés.",
     "s": [
      "hug-smur-sca"
     ]
    }
   ],
   "rubriques": {
    "fondamentaux": [
     {
      "t": "Les nitrés dilatent veines et artères : le cœur reçoit moins de sang, pompe contre une pression plus basse, et la TA chute.",
      "s": [
       "os-nitres"
      ]
     }
    ],
    "demarche": [
     {
      "t": "Ils traitent la douleur angineuse du SCA sans sus-décalage ST.",
      "s": [
       "hug-smur-sca"
      ]
     }
    ],
    "differentiels": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "exploration": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "diagnostic": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "priseEnCharge": [
     {
      "t": "Dans le STEMI, tu les considères seulement en cas d’hypertension ou d’insuffisance cardiaque sans choc.",
      "s": [
       "hug-smur-sca"
      ]
     }
    ],
    "suivi": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "explication": []
   },
   "noteFrequence": {
    "t": "Aucune donnée suisse de fréquence n’a été lue. À vérifier.",
    "s": []
   },
   "sources": [
    "hug-smur-sca",
    "os-nitres"
   ]
  },
  {
   "id": "oxygene",
   "specialite": "cardiologie",
   "type": "traitement",
   "classe": "Support",
   "nom": "Oxygène",
   "court": "O₂",
   "cle": "Seulement si SpO₂ < 90 %",
   "contre": [
    {
     "t": "Une SpO₂ ≥ 90 % ne justifie pas d’oxygène dans le SCA.",
     "s": [
      "kssg-acs"
     ]
    }
   ],
   "pieges": [
    {
     "t": "Le protocole HUG écrit « FiO₂ < 90 % » ; le sens clinique est la saturation (SpO₂). À vérifier auprès des HUG.",
     "s": [
      "hug-smur-sca"
     ]
    }
   ],
   "rubriques": {
    "fondamentaux": [
     {
      "t": "L’oxygène corrige l’hypoxémie ; il n’a pas d’intérêt démontré sans hypoxémie dans le SCA. À vérifier.",
      "s": []
     }
    ],
    "demarche": [
     {
      "t": "Tu le donnes seulement si la saturation reste < 90 %.",
      "s": [
       "kssg-acs",
       "hug-smur-sca"
      ]
     }
    ],
    "differentiels": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "exploration": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "diagnostic": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "priseEnCharge": [
     {
      "t": "En cas de dyspnée ou d’insuffisance cardiaque aiguë, tu relèves le buste à 30°.",
      "s": [
       "kssg-acs"
      ]
     }
    ],
    "suivi": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "explication": []
   },
   "noteFrequence": {
    "t": "Aucune donnée suisse de fréquence n’a été lue. À vérifier.",
    "s": []
   },
   "sources": [
    "kssg-acs",
    "hug-smur-sca"
   ]
  },
  {
   "id": "opioide",
   "specialite": "cardiologie",
   "type": "traitement",
   "classe": "Antalgique",
   "nom": "Antalgie opioïde titrée",
   "court": "Opioïde",
   "cle": "Titre si douleur persistante (EVA > 3)",
   "contre": [
    {
     "t": "Les contre-indications détaillées n’ont pas été lues dans une source suisse. À vérifier.",
     "s": []
    }
   ],
   "pieges": [
    {
     "t": "L’antalgie ne remplace pas la reperfusion. À vérifier.",
     "s": []
    }
   ],
   "rubriques": {
    "fondamentaux": [
     {
      "t": "L’opioïde agit sur ses récepteurs du système nerveux et atténue le message douloureux.",
      "s": [
       "os-opioides"
      ]
     }
    ],
    "demarche": [
     {
      "t": "Le protocole genevois prévoit du fentanyl IV si l’EVA dépasse 3.",
      "s": [
       "hug-smur-sca"
      ]
     },
     {
      "t": "Le manuel saint-gallois réserve la morphine, avec prudence, à la douleur persistante.",
      "s": [
       "kssg-acs"
      ]
     }
    ],
    "differentiels": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "exploration": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "diagnostic": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "priseEnCharge": [
     {
      "t": "Dans la dissection, l’opiacé fait partie du traitement initial.",
      "s": [
       "kssg-aorte"
      ]
     }
    ],
    "suivi": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "explication": []
   },
   "noteFrequence": {
    "t": "Aucune donnée suisse de fréquence n’a été lue. À vérifier.",
    "s": []
   },
   "sources": [
    "hug-smur-sca",
    "kssg-acs",
    "kssg-aorte",
    "os-opioides"
   ]
  },
  {
   "id": "betabloquant",
   "specialite": "cardiologie",
   "type": "traitement",
   "classe": "Bêtabloquant",
   "nom": "Bêtabloquant IV",
   "court": "Bêtabloquant",
   "cle": "Jamais en choc ou si TAS < 100 mmHg",
   "contre": [
    {
     "t": "Il est contre-indiqué en cas de choc, TAS < 100 mmHg, cocaïne, FC < 45/min, PQ > 0,24 s, asthme sévère ou décompensation cardiaque.",
     "s": [
      "kssg-acs"
     ]
    }
   ],
   "pieges": [
    {
     "t": "Un bêtabloquant chez un patient hypotendu risque d’aggraver le bas débit. À vérifier.",
     "s": []
    }
   ],
   "rubriques": {
    "fondamentaux": [
     {
      "t": "Le bêtabloquant occupe les récepteurs β1 du cœur : la FC ralentit, la contraction faiblit, la TA systolique baisse.",
      "s": [
       "os-betabloquants"
      ]
     }
    ],
    "demarche": [
     {
      "t": "Dans le SCA, il traite une tachyarythmie chez un patient stable.",
      "s": [
       "kssg-acs"
      ]
     },
     {
      "t": "Dans la dissection avec TA normale ou haute, il abaisse la TAS vers 100–120 mmHg en premier.",
      "s": [
       "kssg-aorte"
      ]
     },
     {
      "t": "L’algorithme préhospitalier suisse le réserve à une TAS > 120 mmHg et une FC > 60/min.",
      "s": [
       "bs-algo-2026"
      ]
     }
    ],
    "differentiels": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "exploration": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "diagnostic": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "priseEnCharge": [
     {
      "t": "Le traitement oral se poursuit chez tous les patients après un STEMI.",
      "s": [
       "kssg-acs"
      ]
     }
    ],
    "suivi": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "explication": []
   },
   "noteFrequence": {
    "t": "Aucune donnée suisse de fréquence n’a été lue. À vérifier.",
    "s": []
   },
   "sources": [
    "kssg-acs",
    "kssg-aorte",
    "os-betabloquants"
   ]
  },
  {
   "id": "icp",
   "specialite": "cardiologie",
   "type": "traitement",
   "classe": "Reperfusion",
   "nom": "Alarme STEMI → ICP primaire",
   "court": "ICP primaire",
   "cle": "Contact → ICP ≤ 90 min (max. 120)",
   "contre": [
    {
     "t": "Une douleur > 12 h, un bloc de branche nouveau ou une fragilité marquée demandent l’avis du médecin cadre.",
     "s": [
      "hug-smur-sca"
     ]
    }
   ],
   "pieges": [
    {
     "t": "Si l’ICP n’est pas possible en 120 min, la fibrinolyse se discute.",
     "s": [
      "kssg-acs"
     ]
    }
   ],
   "rubriques": {
    "fondamentaux": [
     {
      "t": "Le cathétérisme rouvre l’artère occluse par ballon et stent ; il limite la nécrose.",
      "s": [
       "kssg-acs"
      ]
     }
    ],
    "demarche": [
     {
      "t": "L’alarme STEMI exige des critères ECG de STEMI et des symptômes compatibles, par exemple une douleur typique > 20 min.",
      "s": [
       "hug-smur-sca"
      ]
     }
    ],
    "differentiels": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "exploration": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "diagnostic": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "priseEnCharge": [
     {
      "t": "Tu annonces les critères d’instabilité : œdème pulmonaire, choc cardiogène, troubles du rythme.",
      "s": [
       "hug-smur-sca"
      ]
     },
     {
      "t": "L’ICP constitue la reperfusion préférée du STEMI.",
      "s": [
       "kssg-acs"
      ]
     }
    ],
    "suivi": [
     {
      "t": "Sans objet pour une carte d’action.",
      "s": [],
      "na": true
     }
    ],
    "explication": []
   },
   "noteFrequence": {
    "t": "Aucune donnée suisse de fréquence n’a été lue. À vérifier.",
    "s": []
   },
   "sources": [
    "hug-smur-sca",
    "kssg-acs"
   ]
  }
 ],
 "cas": [
  {
   "id": "douleur-thoracique-74",
   "specialite": "cardiologie",
   "mode": "urgence",
   "chrono": 600,
   "pathologies": [
    "dissection",
    "stemi",
    "infarctus-vd"
   ],
   "titre": "Douleur thoracique, 74 ans",
   "intro": "Garde de nuit. Le 144 amène M. R., 74 ans. Il souffre depuis 45 minutes. Tu es l’interne de garde.",
   "patient": {
    "identite": "M. R., 74 ans",
    "motif": "Douleur thoracique brutale depuis 45 min, irradiant vers le dos",
    "atcd": "Hypertension, tabagisme ancien",
    "constantes": [
     {
      "id": "ta-d",
      "label": "TA bras droit",
      "valeur": "104/66",
      "alerte": false
     },
     {
      "id": "ta-g",
      "label": "TA bras gauche",
      "valeur": "82/50",
      "alerte": true
     },
     {
      "id": "fc",
      "label": "FC",
      "valeur": "58/min",
      "alerte": false
     },
     {
      "id": "spo2",
      "label": "SpO₂ (air)",
      "valeur": "95 %",
      "alerte": false
     },
     {
      "id": "fr",
      "label": "FR",
      "valeur": "20/min",
      "alerte": false
     },
     {
      "id": "eva",
      "label": "EVA",
      "valeur": "7/10",
      "alerte": false
     }
    ],
    "signes": [
     {
      "t": "Sueurs froides",
      "alerte": true
     },
     {
      "t": "Asymétrie tensionnelle de 22 mmHg",
      "alerte": true
     },
     {
      "t": "Radiographie au lit : médiastin à la limite haute",
      "alerte": false
     }
    ]
   },
   "dossier": {
    "ecg": {
     "titre": "ECG 12 dérivations",
     "texte": "Sus-décalage ST en DII, DIII et aVF. Miroir en DI et aVL.",
     "attente": "ECG en attente"
    },
    "ct": {
     "titre": "Angio-CT aortique",
     "texte": "Négatif : pas de dissection. Aorte de calibre normal.",
     "attente": "Imagerie non faite"
    },
    "v4r": {
     "titre": "Dérivations droites",
     "texte": "Sus-décalage ST en V4R : extension au ventricule droit.",
     "attente": "Non enregistrées"
    }
   },
   "etapes": [
    {
     "id": "e1-dissection",
     "titre": "Duel 1 · Exclure la dissection",
     "consigne": "La douleur irradie dans le dos et la TA diffère entre les bras. Exclus la dissection avant tout antithrombotique.",
     "adversaire": "dissection",
     "main": [
      "aspirine",
      "hnf",
      "ecg",
      "angio-ct",
      "p2y12",
      "betabloquant",
      "opioide",
      "oxygene",
      "nitres"
     ],
     "objectifs": [
      "ecg",
      "angio-ct"
     ],
     "regles": {
      "ecg": {
       "verdict": "bon",
       "revele": "ecg",
       "msg": "Bon réflexe. L’ECG se fait en moins de 10 min et ne retarde rien. Il montre un sus-décalage inférieur ; une dissection peut mimer cet aspect."
      },
      "angio-ct": {
       "verdict": "bon",
       "revele": "ct",
       "msg": "Bon réflexe. L’angio-CT exclut la dissection. La voie des antithrombotiques s’ouvre.",
       "avant": {
        "requiert": [
         "ecg"
        ],
        "verdict": "neutre",
        "msg": "L’imagerie exclut la dissection. Mais l’ECG passe d’abord : moins de 10 min après le contact."
       }
      },
      "aspirine": {
       "verdict": "erreur",
       "fiche": "dissection",
       "msg": "Erreur. L’aspirine avant d’exclure une dissection suspectée expose à l’hémorragie. Lis la fiche.",
       "gravite": "dangereuse"
      },
      "hnf": {
       "verdict": "erreur",
       "fiche": "dissection",
       "msg": "Erreur. L’héparine avant d’exclure une dissection suspectée expose à l’hémorragie. Lis la fiche.",
       "gravite": "dangereuse"
      },
      "p2y12": {
       "verdict": "erreur",
       "fiche": "dissection",
       "msg": "Erreur. Aucun antiagrégant tant que la dissection n’est pas exclue. Lis la fiche.",
       "gravite": "dangereuse"
      },
      "betabloquant": {
       "verdict": "erreur",
       "fiche": "dissection",
       "msg": "Erreur. TA basse et FC à 58/min : tu ne baisses pas la TA. Une hypotension évoque une complication.",
       "gravite": "dangereuse"
      },
      "opioide": {
       "verdict": "bon",
       "msg": "Bon réflexe. L’EVA vaut 7/10. L’opiacé fait partie du traitement initial de la dissection."
      },
      "oxygene": {
       "verdict": "erreur",
       "msg": "Erreur. La SpO₂ vaut 95 %. L’oxygène se réserve à une SpO₂ < 90 %.",
       "gravite": "mineure"
      },
      "nitres": {
       "verdict": "erreur",
       "msg": "Erreur. La TA systolique reste sous 110 mmHg. Les nitrés sont contre-indiqués.",
       "gravite": "dangereuse"
      }
     },
     "phase": "trier",
     "pathologie": "dissection"
    },
    {
     "id": "e2-diagnostic",
     "titre": "Duel 2 · Nommer la menace",
     "consigne": "L’angio-CT est négatif. Une dissection de type A peut atteindre la coronaire droite et mimer un STEMI inférieur. Lis l’ECG, puis nomme le diagnostic.",
     "adversaire": "ecg",
     "main": [
      "pericardite",
      "nstemi",
      "stemi",
      "ep",
      "dissection",
      "infarctus-vd"
     ],
     "objectifs": [
      "stemi"
     ],
     "regles": {
      "stemi": {
       "verdict": "bon",
       "msg": "Bon réflexe. Le sus-décalage suit le territoire inférieur avec miroir : c’est un STEMI inférieur."
      },
      "infarctus-vd": {
       "verdict": "neutre",
       "msg": "Possible, pas encore prouvé. Nomme d’abord le STEMI inférieur ; les dérivations droites trancheront."
      },
      "pericardite": {
       "verdict": "erreur",
       "msg": "Erreur. La péricardite donne un sus-décalage diffus. Ici, il suit un territoire coronaire avec miroir.",
       "gravite": "mineure",
       "mortel": true
      },
      "nstemi": {
       "verdict": "erreur",
       "msg": "Erreur. Le sus-décalage ST persiste dans 3 dérivations contiguës : c’est un STEMI.",
       "gravite": "mineure"
      },
      "ep": {
       "verdict": "erreur",
       "msg": "Erreur. Le sus-décalage inférieur avec miroir oriente vers un STEMI, pas vers une EP.",
       "gravite": "mineure"
      },
      "dissection": {
       "verdict": "erreur",
       "msg": "Erreur. L’angio-CT vient d’exclure la dissection.",
       "gravite": "mineure"
      }
     },
     "phase": "differencier",
     "pathologie": "stemi"
    },
    {
     "id": "e3-ventricule-droit",
     "titre": "Duel 3 · Chercher le ventricule droit",
     "consigne": "STEMI inférieur et TA basse. Cherche une extension droite avant tout vasodilatateur.",
     "adversaire": "infarctus-vd",
     "main": [
      "nitres",
      "derivations-droites",
      "betabloquant",
      "troponine",
      "oxygene",
      "opioide"
     ],
     "objectifs": [
      "derivations-droites"
     ],
     "regles": {
      "derivations-droites": {
       "verdict": "bon",
       "revele": "v4r",
       "msg": "Bon réflexe. V4R montre un sus-décalage : le ventricule droit souffre."
      },
      "nitres": {
       "verdict": "erreur",
       "msg": "Erreur. TAS < 110 mmHg et suspicion d’infarctus droit : les nitrés sont contre-indiqués.",
       "gravite": "dangereuse"
      },
      "betabloquant": {
       "verdict": "erreur",
       "msg": "Erreur. La TA systolique est < 100 mmHg à gauche. Le bêtabloquant est contre-indiqué.",
       "gravite": "dangereuse"
      },
      "oxygene": {
       "verdict": "erreur",
       "msg": "Erreur. La SpO₂ vaut 95 %. Pas d’oxygène sans hypoxémie.",
       "gravite": "mineure"
      },
      "troponine": {
       "verdict": "inutile",
       "msg": "Examen inutile à cette étape. La question porte sur le ventricule droit, et la reperfusion du STEMI n’attend pas la troponine."
      },
      "opioide": {
       "verdict": "bon",
       "msg": "Bon réflexe. Tu titres l’antalgie : la douleur persiste."
      }
     },
     "phase": "diagnostiquer",
     "pathologie": "infarctus-vd"
    },
    {
     "id": "e4-reperfusion",
     "titre": "Duel 4 · Reperfuser",
     "consigne": "STEMI inférieur étendu au VD, dissection exclue. Lance le traitement et la reperfusion.",
     "adversaire": "stemi",
     "main": [
      "oxygene",
      "aspirine",
      "nitres",
      "hnf",
      "p2y12",
      "icp",
      "betabloquant",
      "troponine"
     ],
     "objectifs": [
      "aspirine",
      "hnf",
      "icp"
     ],
     "regles": {
      "aspirine": {
       "verdict": "bon",
       "msg": "Bon réflexe. La dissection est exclue : l’aspirine s’impose."
      },
      "hnf": {
       "verdict": "bon",
       "msg": "Bon réflexe. Le patient n’a reçu ni HBPM ni anticoagulant oral : l’héparine part."
      },
      "icp": {
       "verdict": "bon",
       "msg": "Bon réflexe. Tu déclenches l’alarme STEMI et annonces l’hypotension. Cible : ICP en ≤ 90 min."
      },
      "p2y12": {
       "verdict": "neutre",
       "msg": "Décide le moment de la charge avec le cardiologue. Les protocoles suisses lus divergent."
      },
      "troponine": {
       "verdict": "neutre",
       "msg": "Le prélèvement part. La reperfusion n’attend pas son résultat."
      },
      "nitres": {
       "verdict": "erreur",
       "msg": "Erreur. Infarctus droit et TAS < 110 mmHg : les nitrés restent interdits.",
       "gravite": "dangereuse"
      },
      "oxygene": {
       "verdict": "erreur",
       "msg": "Erreur. La SpO₂ vaut 95 %. L’oxygène ne protège pas le myocarde ici.",
       "gravite": "mineure"
      },
      "betabloquant": {
       "verdict": "erreur",
       "msg": "Erreur. Patient hypotendu : le bêtabloquant est contre-indiqué.",
       "gravite": "dangereuse"
      }
     },
     "phase": "traiter",
     "pathologie": "stemi"
    }
   ],
   "debrief": [
    "Tu as exclu la dissection avant les antithrombotiques.",
    "Tu as reconnu un STEMI inférieur étendu au ventricule droit.",
    "Tu as évité les nitrés, l’oxygène réflexe et le bêtabloquant chez un patient hypotendu.",
    "Le patient part en salle de cathétérisme."
   ],
   "pvInitial": 100
  }
 ],
 "questions": []
}
);
