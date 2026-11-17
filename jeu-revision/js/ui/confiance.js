/**
 * Choix de confiance avant chaque coup : Sûr / Hésitant / Au hasard.
 * Trois boutons compacts, touches S, H, A ; aucun choix présélectionné (pas d’ancrage) ;
 * le coup n’est validé qu’après la confiance. Échap annule la sélection.
 */
window.JEU = window.JEU || {};
JEU.ui = JEU.ui || {};
JEU.ui.confiance = (function () {
  const { h } = JEU.dom;
  const TOUCHES = { s: "sur", h: "hesitant", a: "hasard" };
  const LIB = [["sur", "Sûr", "S"], ["hesitant", "Hésitant", "H"], ["hasard", "Au hasard", "A"]];

  /** Panneau de confiance. onChoix(conf) valide ; onAnnuler() retire la sélection. */
  function panneau(libelle, onChoix, onAnnuler) {
    return h("div", { class: "confiance", id: "confiance", role: "group", "aria-labelledby": "confiance-q", tabindex: "-1" },
      h("p", { id: "confiance-q", class: "confiance-q" }, h("strong", {}, libelle), " · Ta confiance ?"),
      h("div", { class: "confiance-boutons" }, LIB.map(([k, t, key]) =>
        h("button", { type: "button", class: `btn-conf btn-conf--${k}`, "data-conf": k, "aria-keyshortcuts": key, onclick: () => onChoix(k) },
          t, h("kbd", { "aria-hidden": "true" }, key)))),
      h("button", { type: "button", class: "btn btn-lien confiance-annuler", onclick: onAnnuler }, "Annuler (Échap)"));
  }
  /** Traduit une touche en confiance, ou null. */
  const touche = ev => (ev.ctrlKey || ev.metaKey || ev.altKey) ? null : TOUCHES[(ev.key || "").toLowerCase()] || null;
  return { panneau, touche, LIB };
})();
