/** Collection : toutes les cartes par spécialité, la légende du poids PROFILES et l’accès aux fiches. */
window.JEU = window.JEU || {};
JEU.ui = JEU.ui || {};
JEU.ui.collection = (function () {
  const { h, $ } = JEU.dom;
  const TYPES = [["pathologie", "Pathologies"], ["examen", "Examens"], ["traitement", "Traitements"], ["geste", "Gestes"], ["fondamental", "Fondamentaux"]];
  function render() {
    const cartes = JEU.registry.cards();
    $("#vue-collection").replaceChildren(h("div", { class: "page" },
      h("header", { class: "page-tete" }, h("p", { class: "sur-titre" }, "Collection"), h("h1", {}, `${cartes.length} cartes.`), h("p", {}, "Clique une carte pour ouvrir sa fiche en 8 rubriques.")),
      h("section", { class: "legende", "aria-labelledby": "legende-titre" },
        h("h2", { id: "legende-titre", class: "bloc-titre" }, "Rareté = poids PROFILES"),
        h("ul", {}, Object.values(JEU.ui.RARETES).map(r => h("li", {}, h("span", { class: "pips", "aria-hidden": "true" }, [1, 2, 3].map(i => h("i", { class: i <= r.pips ? "on" : "" }))), h("strong", {}, r.label), " : ", r.def))),
        h("p", { class: "aide" }, "PROFILES ne publie pas de pondération par objectif. Le poids compte les SSP rattachées à la pathologie ; il reste provisoire. ", h("span", { class: "badge-verif" }, "À vérifier"))),
      JEU.specialites.map(sp => h("section", { class: "collection-groupe", "aria-labelledby": `col-${sp.id}` },
        h("h2", { id: `col-${sp.id}`, class: "bloc-titre" }, sp.nom),
        TYPES.map(([t, lib]) => { const L = cartes.filter(c => c.specialite === sp.id && c.type === t); return L.length ? [h("h3", { class: "zone-label" }, lib), h("div", { class: "collection-grille" }, L.map(c => JEU.ui.renderCard(c, { mode: "lecture" })))] : null; })))));
  }
  return { render };
})();
