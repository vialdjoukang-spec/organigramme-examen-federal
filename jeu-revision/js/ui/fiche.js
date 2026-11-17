/**
 * Fiche (écran 2) : les 8 rubriques du schéma v2, dans un <dialog> natif.
 * Chaque affirmation affiche ses renvois de source ou un badge « À vérifier ».
 * La rubrique 8 rassemble les explications de coups tirées des cas.
 */
window.JEU = window.JEU || {};
JEU.ui = JEU.ui || {};
JEU.ui.fiche = (function () {
  const { h, $ } = JEU.dom;
  let retourFocus = null;
  const ECH_RUB = { fondamentaux: "1–2", demarche: "3", differentiels: "4", exploration: "5", diagnostic: "6", priseEnCharge: "7", suivi: "7" };

  function ligne(cl, num, extra) {
    if (cl.na) return h("li", { class: "na" }, cl.t);
    const src = JEU.registry.isSourced(cl);
    return h("li", { class: src ? "" : "non-source" },
      extra || null,
      cl.t.replace(/\s*À vérifier.*$/, ""),
      src ? h("span", { class: "refs" }, cl.s.map(id => h("a", { href: `#src-${id}`, class: "ref", "aria-label": `Source ${num[id]}` }, `[${num[id]}]`))) : null,
      (!src || /À vérifier/.test(cl.t)) ? h("span", { class: "badge-verif" }, (cl.t.match(/À vérifier.*$/) || ["À vérifier"])[0]) : null);
  }
  function bloc(titre, claims, num, opts = {}) {
    if (!claims || !claims.length) return null;
    return h("div", { class: "fiche-bloc" }, titre ? h("h4", {}, titre) : null,
      h("ul", {}, claims.map(cl => ligne(cl, num, opts.dx && cl.dx ? h("strong", { class: `dx ${cl.tue ? "dx--tue" : ""}` }, cl.dx, cl.tue ? h("span", { class: "tag-tue" }, "tue") : null, " : ") : null))));
  }
  /** Explications de coups : tous les messages de règles où la carte est jouée ou sert de fiche. */
  function explicationsCas(id) {
    const L = [];
    JEU.registry.tousLesCas().forEach(k => k.etapes.forEach(e => Object.entries(e.regles).forEach(([cid, r]) => {
      if (cid === id || r.fiche === id) L.push({ k, e, cid, r });
    })));
    return L;
  }

  function open(id, contexte) {
    const c = JEU.registry.card(id);
    if (!c) return;
    const dlg = $("#fiche");
    const R = c.rubriques;
    const ids = [];
    const push = cl => (cl && cl.s || []).forEach(s => ids.includes(s) || ids.push(s));
    JEU.schema.CLES.forEach(k => (R[k] || []).forEach(push));
    (c.contre || []).forEach(push); (c.pieges || []).forEach(push); push(c.noteFrequence);
    (c.sources || []).forEach(s => ids.includes(s) || ids.push(s));
    const num = {}; ids.forEach((s, i) => num[s] = i + 1);
    const r = JEU.ui.RARETES[c.rarete];
    const isPatho = c.type === "pathologie";
    const sp = JEU.registry.specialite(c.specialite);
    const exps = explicationsCas(id);
    const verdictTxt = { bon: "Bon réflexe", erreur: "Erreur", neutre: "Info", inutile: "Examen inutile" };

    const sections = JEU.schema.RUBRIQUES.map(([k, titre, aide], i) => {
      let contenu;
      if (k === "explication") {
        contenu = [bloc(null, R.explication, num),
          exps.length ? h("ul", { class: "fiche-coups" }, exps.map(x => h("li", { class: `coup coup--${x.r.verdict}` },
            h("span", { class: "coup-tag" }, verdictTxt[x.r.verdict] + (x.r.gravite ? ` · ${x.r.gravite}` : "")),
            h("span", { class: "coup-ctx" }, `${x.k.titre} · ${x.e.titre.replace(/^Duel \d · /, "")} · carte ${JEU.registry.card(x.cid).court}`),
            h("span", {}, x.r.msg)))) : (R.explication.length ? null : h("p", { class: "vide" }, "Aucun coup encore rédigé pour cette carte."))];
      } else {
        contenu = [bloc(null, R[k], num, { dx: k === "differentiels" })];
        if (k === "differentiels") contenu.push(bloc("Pièges", c.pieges, num));
        if (k === "priseEnCharge") {
          contenu.push(bloc(isPatho ? "À éviter" : "Contre-indications", c.contre, num));
          if (!isPatho && c.type === "traitement") contenu.push(h("div", { class: "fiche-bloc" }, h("h4", {}, "Posologie"),
            h("p", {}, "Aucune dose n’est affichée sans extrait daté de l’information professionnelle suisse (swissmedicinfo.ch). ", h("span", { class: "badge-verif" }, "À vérifier"))));
        }
      }
      return h("section", { class: `fiche-section rub rub--${k}`, "data-rubrique": k },
        h("h3", {}, h("span", { class: "rub-num" }, String(i + 1)), titre, ECH_RUB[k] ? h("span", { class: "rub-ech" }, `échelon ${ECH_RUB[k]}`) : null),
        h("p", { class: "rub-aide" }, aide), ...contenu);
    });

    const contenu = h("div", { class: "fiche-contenu" },
      h("header", { class: "fiche-entete" },
        h("p", { class: "fiche-sur" }, isPatho ? "Pathologie" : (c.classe || "Action"), " · ", sp ? sp.nom : ""),
        h("h2", { id: "fiche-titre" }, c.nom),
        h("p", { class: "fiche-cle" }, h("strong", {}, isPatho ? "Signe clé : " : "Règle d’usage : "), c.cle),
        h("p", { class: "fiche-rarete" }, h("strong", {}, `${r.label}. `), r.def, " ",
          c.noteFrequence ? ligne(c.noteFrequence, num) : null),
        JEU.registry.hasSwissSource(c) ? null : h("p", { class: "alerte-verif" }, "Cette fiche ne cite aucune source suisse lue. Son contenu clinique reste « À vérifier ».")),
      contexte ? h("div", { class: "fiche-erreur", role: "alert" }, h("strong", {}, "Ton erreur : "), contexte.replace(/^(Erreur|Examen inutile[^.]*)\.\s*/, "")) : null,
      ...sections,
      h("section", { class: "fiche-section fiche-sources" }, h("h3", {}, "Sources"),
        h("ol", {}, ids.map(s => {
          const src = JEU.registry.source(s);
          const compl = src.type === "suisse" && /cantonal/.test(src.categorie || "");
          return h("li", { id: `src-${s}` },
            h("a", { href: src.url, target: "_blank", rel: "noopener" }, src.titre), ". ", src.editeur,
            ". Lu le ", src.lu_le, ". ", h("span", { class: "src-portee" }, src.portee),
            src.type === "suisse" ? h("span", { class: "tag-suisse" }, `Source suisse · ${src.categorie}${compl ? " · complémentaire" : ""}`) : h("span", { class: "tag-pharma" }, "Pharmacologie · international"));
        }))));

    const corps = $("#fiche-corps");
    corps.replaceChildren(contenu);
    corps.scrollTop = 0;
    retourFocus = document.activeElement;
    if (!dlg.open) dlg.showModal();
    $("#fiche-fermer").focus();
  }

  function init() {
    const dlg = $("#fiche");
    $("#fiche-fermer").addEventListener("click", () => dlg.close());
    dlg.addEventListener("click", e => { if (e.target === dlg) dlg.close(); });
    dlg.addEventListener("close", () => {
      const cible = retourFocus && document.contains(retourFocus) && retourFocus !== document.body ? retourFocus
        : ($("#btn-suivant") || $("#btn-rejouer") || $("#btn-q-suivante") || $(".main .carte-action"));
      if (cible) cible.focus();
    });
  }
  return { open, init };
})();
