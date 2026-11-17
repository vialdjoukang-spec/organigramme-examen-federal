/**
 * Point d’entrée : initialise le registre, les vues et la navigation par onglets.
 */
window.JEU = window.JEU || {};
JEU.app = (function () {
  const { $ } = JEU.dom;
  const VUES = ["plateau", "collection", "journal"];

  function montrer(vue) {
    if (!VUES.includes(vue)) vue = "plateau";
    document.body.dataset.vue = vue;
    VUES.forEach(v => {
      $(`#vue-${v}`).hidden = v !== vue;
      const t = $(`#onglet-${v}`);
      t.setAttribute("aria-current", v === vue ? "page" : "false");
    });
    if (vue === "journal") JEU.ui.journal.render();
    if (vue === "collection") JEU.ui.collection.render();
    if (location.hash !== `#${vue}`) history.replaceState(null, "", `#${vue}`);
  }

  function init() {
    const pb = JEU.registry.init();
    if (pb.length) console.warn(`${pb.length} problème(s) de données détecté(s).`);
    JEU.ui.fiche.init();
    JEU.ui.journal.init();
    JEU.ui.board.init();
    VUES.forEach(v => $(`#onglet-${v}`).addEventListener("click", () => montrer(v)));
    montrer(location.hash.replace("#", "") || "plateau");
  }
  document.addEventListener("DOMContentLoaded", init);
  return { montrer };
})();
