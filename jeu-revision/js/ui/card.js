/**
 * Rendu d’une carte. Deux actions distinctes et accessibles au clavier :
 * – le bouton principal (toute la carte) : jouer la carte, ou ouvrir la fiche hors duel ;
 * – le bouton « Fiche » : ouvrir la fiche détaillée.
 */
window.JEU = window.JEU || {};
JEU.ui = JEU.ui || {};
JEU.ui.RARETES = {
  commune:  { label: "Commune",  pips: 1, def: "Geste ou situation de presque chaque douleur thoracique." },
  frequente:{ label: "Fréquente", pips: 2, def: "Diagnostic ou traitement courant aux urgences." },
  rare:     { label: "Rare",     pips: 3, def: "Situation rare, mais vitale à reconnaître." }
};

JEU.ui.renderCard = function (card, opts = {}) {
  const { h } = JEU.dom;
  const r = JEU.ui.RARETES[card.rarete];
  const isPatho = card.type === "pathologie";
  const pips = h("span", { class: "pips", "aria-hidden": "true" },
    [1, 2, 3].map(i => h("i", { class: i <= r.pips ? "on" : "" })));
  const nonValidee = !JEU.registry.hasSwissSource(card);

  const corps = [
    h("div", { class: "carte-entete" },
      h("span", { class: "carte-type" }, isPatho ? "Pathologie" : (card.classe || "Action")),
      h("span", { class: "carte-rarete", title: r.label }, pips, h("span", { class: "sr-only" }, `Rareté : ${r.label}`))),
    h("div", { class: "carte-nom" }, card.court),
    h("div", { class: "carte-sous" }, card.nom),
    h("div", { class: "carte-cle" }, h("span", { class: "sr-only" }, "Signe clé : "), card.cle),
    nonValidee ? h("span", { class: "badge-verif" }, "À vérifier") : null
  ];

  const principal = h("button", {
    type: "button", class: "carte-action",
    "aria-label": opts.mode === "main" ? `Jouer ${card.nom}` : `Ouvrir la fiche ${card.nom}`,
    onclick: () => (opts.onPlay && opts.mode === "main" ? opts.onPlay(card.id) : JEU.ui.fiche.open(card.id))
  });
  const btnFiche = h("button", {
    type: "button", class: "carte-fiche", "aria-label": `Fiche : ${card.nom}`,
    onclick: ev => { ev.stopPropagation(); JEU.ui.fiche.open(card.id); }
  }, "Fiche");

  return h("div", {
    class: `carte ${isPatho ? "carte--patho" : "carte--action"} rarete--${card.rarete} ${opts.extraClass || ""}`,
    "data-id": card.id, role: "group", "aria-label": `${card.nom}. ${card.cle}`,
    style: opts.delay !== undefined ? `--delay:${opts.delay}ms` : null
  }, corps, principal, btnFiche);
};
