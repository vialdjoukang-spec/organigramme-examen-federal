# Schéma d'enrichissement d'un diagnostic d'imagerie (un fichier JSON par lot : enrichi/<lot>.json = {"IMG-001": {...}, ...})
{
  "gold": {"examen": "formulation EXACTE de l'examen de référence (ex. « IRM cérébrale, séquence de diffusion »)",
           "pourquoi": ["puce verbale courte", "..."],
           "premiere_intention": "si différente du gold : examen exact + pourquoi en une phrase, sinon null"},
  "autres": [ {"examen": "formulation EXACTE", "rang": 2,
               "quand": ["cadre précis où on la réalise (puce verbale)"],
               "pourquoi_pas_gold": ["puce verbale"],
               "montre": ["signe vu avec cette technique"]} ],
  "images": {
    "normal": {"fichier": "img/IMG-001_normal.jpg", "technique": "TDM sans injection, coupe axiale", "credit": "Auteur", "licence": "CC BY-SA 4.0", "url": "https://commons.wikimedia.org/wiki/File:..."},
    "patho":  {"fichier": "img/IMG-001_patho.jpg", "technique": "...", "credit": "...", "licence": "...", "url": "...",
               "reperes": [ {"n": 1, "x": 42.5, "y": 31.0, "fx": 30.0, "fy": 20.0,
                            "lesion": "terme dédié de la lésion élémentaire", "semio": "description sémiologique en une phrase verbale"} ]}
  },
  "syndrome": ["regroupement syndromique, puce verbale"],
  "traitement": ["traitement EXACT, puce verbale : molécule + dose AIPS suisse + délai/geste ; « À vérifier » si non sourcé"],
  "sources": ["source datée"]
}
Coordonnées x,y = pointe de la flèche en % de la largeur/hauteur de l'image ; fx,fy = départ de la flèche (où s'affiche le numéro), en %.
Images : Wikimedia Commons seulement (domaine public, CC0, CC BY, CC BY-SA), téléchargées dans img/ (≤ 900 px de large, JPEG qualité 85). API : curl -A "ProgressionEdu/1.0 (educational)" "https://commons.wikimedia.org/w/api.php?..." (sans User-Agent : 429). Licence lue sur la page du fichier (extmetadata via prop=imageinfo&iiprop=url|extmetadata).
Si aucune image libre fiable n'existe : "images": {"manque": "raison"} — jamais d'image douteuse.
