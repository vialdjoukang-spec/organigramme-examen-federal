/**
 * Fiche détaillée (écran 2) dans un <dialog> natif : focus géré, Échap ferme.
 * Chaque affirmation affiche ses renvois de source ou un badge « À vérifier ».
 */
window.JEU = window.JEU || {};
JEU.ui = JEU.ui || {};
JEU.ui.fiche = (function () {
  const { h, $ } = JEU.dom;
  let retourFocus = null;

  function section(titre, claims, numeros) {
    if (!claims || !claims.length) return null;
    return h("section", { class: "fiche-section" },
      h("h3", {}, titre),
      h("ul", {}, claims.map(cl => h("li", { class: JEU.registry.isSourced(cl) ? "" : "non-source" },
        cl.t.replace(/\s*À vérifier.*$/, ""),
        JEU.registry.isSourced(cl)
          ? h("span", { class: "refs" }, cl.s.map(id => h("a", { href: `#src-${id}`, class: "ref", "aria-label": `Source ${numeros[id]}` }, `[${numeros[id]}]`)))
          : null,
        (!JEU.registry.isSourced(cl) || /À vérifier/.test(cl.t)) ? h("span", { class: "badge-verif" }, (cl.t.match(/À vérifier.*$/) || ["À vérifier"])[0]) : null
      ))));
  }

  function open(id, contexte) {
    const c = JEU.registry.card(id);
    if (!c) return;
    const dlg = $("#fiche");
    // Numérotation des sources : celles des affirmations, puis celles de la carte.
    const ids = [];
    ["mecanisme", "signes", "exploration", "premiere", "contre", "pieges"].forEach(k => (c[k] || []).forEach(cl => (cl.s || []).forEach(s => ids.includes(s) || ids.push(s))));
    (c.sources || []).forEach(s => ids.includes(s) || ids.push(s));
    (c.rareteNote && c.rareteNote.s || []).forEach(s => ids.includes(s) || ids.push(s));
    const num = {}; ids.forEach((s, i) => num[s] = i + 1);
    const r = JEU.ui.RARETES[c.rarete];
    const isPatho = c.type === "pathologie";
    const suisse = JEU.registry.hasSwissSource(c);

    const contenu = h("div", { class: "fiche-contenu" },
      h("header", { class: "fiche-entete" },
        h("p", { class: "fiche-sur" }, isPatho ? "Pathologie" : (c.classe || "Action"), " · ", JEU.registry.system(c.systeme).nom),
        h("h2", { id: "fiche-titre" }, c.nom),
        h("p", { class: "fiche-cle" }, h("strong", {}, "Signe clé : "), c.cle),
        h("p", { class: "fiche-rarete" }, h("strong", {}, `Rareté ${r.label}. `), c.rareteNote.t.replace(/\s*À vérifier.*$/, ""),
          JEU.registry.isSourced(c.rareteNote) ? h("a", { href: `#src-${c.rareteNote.s[0]}`, class: "ref" }, `[${num[c.rareteNote.s[0]]}]`) : h("span", { class: "badge-verif" }, "À vérifier")),
        suisse ? null : h("p", { class: "alerte-verif" }, "Cette fiche ne cite aucune source suisse lue. Tout son contenu reste « À vérifier ».")
      ),
      contexte ? h("div", { class: "fiche-erreur", role: "alert" }, h("strong", {}, "Ton erreur : "), contexte.replace(/^Erreur\.\s*/, "")) : null,
      section("Mécanisme", c.mecanisme, num),
      section(isPatho ? "Sémiologie · signes clés" : "Indication · quand y penser", c.signes, num),
      section("Exploration", c.exploration, num),
      section(isPatho ? "Prise en charge de 1re intention" : "Usage de 1re intention", c.premiere, num),
      section(isPatho ? "À éviter · contre-indications" : "Contre-indications", c.contre, num),
      section("Pièges d’examen", c.pieges, num),
      isPatho ? null : h("section", { class: "fiche-section" }, h("h3", {}, "Posologie"),
        h("p", {}, "Aucune dose n’est affichée. Lis l’information professionnelle suisse du produit exact (swissmedicinfo.ch). ",
          h("span", { class: "badge-verif" }, "À vérifier"))),
      h("section", { class: "fiche-section fiche-sources" }, h("h3", {}, "Sources"),
        h("ol", {}, ids.map(s => {
          const src = JEU.registry.source(s);
          return h("li", { id: `src-${s}` },
            h("a", { href: src.url, target: "_blank", rel: "noopener" }, src.titre), ". ", src.editeur,
            ". Lu le ", src.lu_le, ". ", h("span", { class: "src-portee" }, src.portee),
            src.type === "suisse" ? h("span", { class: "tag-suisse" }, `Source suisse · ${src.categorie || "—"}`) : h("span", { class: "tag-pharma" }, "Pharmacologie"));
        })))
    );

    const corps = $("#fiche-corps");
    corps.replaceChildren(contenu);
    corps.scrollTop = 0;
    retourFocus = document.activeElement;
    if (!dlg.open) dlg.showModal();
    $("#fiche-fermer").focus();
    document.dispatchEvent(new CustomEvent("fiche:ouverte", { detail: { id } }));
  }

  function init() {
    const dlg = $("#fiche");
    $("#fiche-fermer").addEventListener("click", () => dlg.close());
    dlg.addEventListener("click", e => { if (e.target === dlg) dlg.close(); });  // clic sur le fond
    dlg.addEventListener("close", () => {
      // Le plateau a pu être redessiné : on revient sur l’élément d’origine, sinon sur la main.
      const cible = retourFocus && document.contains(retourFocus) && retourFocus !== document.body ? retourFocus
        : ($("#btn-suivant") || $("#btn-rejouer") || $(".main .carte-action"));
      if (cible) cible.focus();
    });
  }
  return { open, init };
})();
