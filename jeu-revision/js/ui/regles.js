/** Écran « Règles » : règles du jeu, étoiles, modes, confiance, Leitner, maîtrise, grades. */
window.JEU = window.JEU || {};
JEU.ui = JEU.ui || {};
JEU.ui.regles = (function () {
  const { h, $ } = JEU.dom;
  function render() {
    const R = JEU.REGLES, P = JEU.progression;
    const li = t => h("li", {}, t);
    $("#vue-regles").replaceChildren(h("section", { class: "page regles", "aria-labelledby": "regles-titre" },
      h("header", { class: "page-tete" }, h("p", { class: "sur-titre" }, "Internat · Règles"), h("h1", { id: "regles-titre" }, "Joue comme en garde.")),
      h("div", { class: "regles-grille" },
        h("section", { class: "tb-bloc" }, h("h2", {}, "Un cas"), h("ul", {},
          li("Chaque cas compte 3 à 5 duels, dans l’ordre clinique : trier, explorer, différencier, diagnostiquer, traiter."),
          li("Choisis une carte, puis ta confiance : Sûr (S), Hésitant (H) ou Au hasard (A). Le coup part seulement alors."),
          li(`Le patient a des PV. Une erreur dangereuse coûte ${R.dangereuse} PV, une erreur mineure ${R.mineure} PV, un examen inutile ${R.inutile} PV et 1 minute de temps patient.`),
          li("Chaque erreur ou examen inutile ouvre sa fiche, avec l’explication du coup."))),
        h("section", { class: "tb-bloc" }, h("h2", {}, "Étoiles"), h("ul", {},
          li("Tu pars de 3 étoiles à la victoire."), li("Tu en perds une sous 80 % de PV, et une autre sous 50 %."),
          li("Tu en perds une pour tout examen inutile."), li("En Urgence, tu en perds une si le chrono est dépassé."), li("Une victoire vaut au moins 1 étoile ; une défaite, 0."))),
        h("section", { class: "tb-bloc" }, h("h2", {}, "Modes"), h("ul", {},
          li("Fondamentaux : duels courts sur les échelons 1 et 2 (mécanisme ↔ signe, structure ↔ fonction)."),
          li("Consultation : sans chronomètre ; l’excès d’examens coûte des PV et une étoile."),
          li("Urgence : chronomètre imposé ; objectif de réponse sous 20 s."),
          li("Cas final : plusieurs pathologies et comorbidités, sous chronomètre, avec un piège."),
          li("Entraînement : toutes les salles ouvertes, sans chronomètre."),
          li("Ronde : 20 minutes par jour, bâties sur tes points faibles."),
          li("Examen blanc PROFILES : cas mêlés, chronométrés, notés (structure ; contenu à venir)."))),
        h("section", { class: "tb-bloc" }, h("h2", {}, "Progression"), h("ul", {},
          li("Chaque pathologie gravit 7 échelons : " + P.ECHELONS.map(e => `${e[0]}. ${e[1]}`).join(", ") + "."),
          li("Maîtrisée : les 7 échelons réussis « sûr » à J0, puis à J+1 et à J+7 ; rappel à J+30."),
          li(`Leitner, 5 boîtes : ${P.LEITNER.map((j, i) => `boîte ${i + 1} = ${j ? "J+" + j : "même jour"}`).join(", ")}. Juste au hasard = non maîtrisé.`),
          li("Une salle s’ouvre après 2 étoiles de moyenne sur la précédente, ou en Entraînement."),
          li("Grades : " + P.GRADES.map(g => `${g[1]} (${Math.round(g[0] * 100)} %)`).join(" → ") + " des pathologies maîtrisées. Seuils à confirmer par Vial."))))));
  }
  return { render };
})();
