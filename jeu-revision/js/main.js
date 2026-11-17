/**
 * Point d’entrée : registre, progression, vues et navigation par onglets (#hash).
 */
window.JEU = window.JEU || {};
JEU.app = (function () {
  const { $ } = JEU.dom;
  const VUES = ["parcours", "plateau", "quiz", "collection", "tableau", "regles"];
  const RENDUS = { parcours: () => JEU.ui.parcours.render(), collection: () => JEU.ui.collection.render(), tableau: () => JEU.ui.tableau.render(), regles: () => JEU.ui.regles.render(), quiz: () => JEU.ui.quiz.render() };

  /** sansRendu : la vue vient d’être dessinée par son module (plateau, quiz). */
  function montrer(vue, sansRendu) {
    if (!VUES.includes(vue)) vue = "parcours";
    document.body.dataset.vue = vue;
    VUES.forEach(v => { $(`#vue-${v}`).hidden = v !== vue; const t = $(`#onglet-${v}`); if (t) t.setAttribute("aria-current", v === vue ? "page" : "false"); });
    if (!sansRendu && RENDUS[vue]) RENDUS[vue]();
    if (location.hash !== `#${vue}`) history.replaceState(null, "", `#${vue}`);
  }
  function majSon() {
    const b = $("#btn-son"), on = JEU.son.actif();
    b.setAttribute("aria-pressed", String(!on));
    b.textContent = on ? "Son : activé" : "Son : coupé";
  }
  function init() {
    JEU.progression.charger();
    const pb = JEU.registry.init();
    if (pb.length) console.warn(`${pb.length} problème(s) de données détecté(s).`);
    JEU.ui.fiche.init(); JEU.ui.board.init(); JEU.ui.quiz.init();
    VUES.forEach(v => { const t = $(`#onglet-${v}`); if (t) t.addEventListener("click", () => montrer(v)); });
    $("#btn-son").addEventListener("click", () => { JEU.son.setActif(!JEU.son.actif()); majSon(); JEU.son.jouer("bip"); });
    majSon();
    montrer(location.hash.replace("#", "") || "parcours");
  }
  document.addEventListener("DOMContentLoaded", init);
  return { montrer };
})();
