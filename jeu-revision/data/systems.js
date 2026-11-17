/**
 * Systèmes (axes du journal). Ajouter un système = ajouter une entrée ici.
 * "actif: false" affiche le système dans le journal comme « à venir ».
 */
window.JEU = window.JEU || {};
JEU.systems = [
  { id: "cardio", nom: "Cardiovasculaire", actif: true },
  { id: "neuro", nom: "Neurologie", actif: false },
  { id: "infectieux", nom: "Infectiologie", actif: false },
  { id: "pneumo", nom: "Pneumologie", actif: false }
];
