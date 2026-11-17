/** Collection : toutes les cartes, la légende de rareté et l’accès aux fiches. */
window.JEU = window.JEU || {};
JEU.ui = JEU.ui || {};
JEU.ui.collection = (function () {
  const { h, $ } = JEU.dom;
  function render() {
    const cartes = JEU.registry.cards();
    const groupe = (titre, type) => h("section", { class: "collection-groupe", "aria-labelledby": `col-${type}` },
      h("h2", { id: `col-${type}`, class: "bloc-titre" }, titre),
      h("div", { class: "collection-grille" }, cartes.filter(c => c.type === type).map(c => JEU.ui.renderCard(c, { mode: "lecture" }))));
    $("#vue-collection").replaceChildren(
      h("div", { class: "page" },
        h("header", { class: "page-tete" },
          h("p", { class: "sur-titre" }, "Collection · Cardiovasculaire"),
          h("h1", {}, `${cartes.length} cartes.`),
          h("p", {}, "Clique une carte pour ouvrir sa fiche.")),
        h("section", { class: "legende", "aria-labelledby": "legende-titre" },
          h("h2", { id: "legende-titre", class: "bloc-titre" }, "Rareté = fréquence clinique"),
          h("ul", {}, Object.values(JEU.ui.RARETES).map(r => h("li", {},
            h("span", { class: "pips", "aria-hidden": "true" }, [1, 2, 3].map(i => h("i", { class: i <= r.pips ? "on" : "" }))),
            h("strong", {}, r.label), " : ", r.def))),
          h("p", { class: "aide" }, "Chaque fiche justifie sa rareté par une donnée sourcée, ou l’affiche « À vérifier ». Aucun poids d’examen PROFILES n’est affirmé.")),
        groupe("Pathologies", "pathologie"),
        groupe("Actions et médicaments", "action")));
  }
  return { render };
})();
