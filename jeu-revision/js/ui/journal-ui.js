/** Journal de progression (écran 3) : précision par système, erreurs, fiches à revoir. */
window.JEU = window.JEU || {};
JEU.ui = JEU.ui || {};
JEU.ui.journal = (function () {
  const { h, $, dateFr } = JEU.dom;

  function render() {
    const d = JEU.journal.get();
    const aRevoir = JEU.journal.fichesARevoir();
    const nomCarte = id => (JEU.registry.card(id) || { nom: id }).nom;
    const nomEtape = id => { for (const sv of JEU.services) for (const cs of sv.cas) for (const e of cs.etapes) if (e.id === id) return e.titre; return id; };

    $("#vue-journal").replaceChildren(h("div", { class: "page" },
      h("header", { class: "page-tete" },
        h("p", { class: "sur-titre" }, "Journal de progression"),
        h("h1", {}, "Tes systèmes."),
        h("p", {}, `Un système devient faible sous ${Math.round(JEU.journal.SEUIL_FAIBLE * 100)} % de bons réflexes, après ${JEU.journal.MIN_ESSAIS} coups jugés.`)),

      h("section", { class: "systemes", "aria-labelledby": "sys-titre" },
        h("h2", { id: "sys-titre", class: "bloc-titre" }, "Précision par système"),
        h("ul", { class: "systemes-liste" }, JEU.systems.map(s => {
          const st = JEU.journal.stats(s.id);
          const pct = st.precision === null ? null : Math.round(st.precision * 100);
          return h("li", { class: `systeme ${st.faible ? "systeme--faible" : ""} ${s.actif ? "" : "systeme--inactif"}`, "data-systeme": s.id },
            h("span", { class: "systeme-nom" }, s.nom),
            s.actif ? h("span", { class: "systeme-barre", role: "img", "aria-label": pct === null ? "Aucune donnée" : `${pct} % de bons réflexes` },
              h("span", { style: `width:${pct || 0}%` })) : h("span", { class: "systeme-barre vide" }),
            h("span", { class: "systeme-pct" }, !s.actif ? "Bientôt" : pct === null ? "—" : `${pct} %`),
            h("span", { class: "systeme-detail" }, s.actif ? `${st.bons} bons · ${st.erreurs} erreurs · ${st.neutres} infos` : "Service non ouvert"),
            st.faible ? h("span", { class: "tag-faible" }, "À renforcer") : null);
        }))),

      h("div", { class: "journal-colonnes" },
        h("section", { "aria-labelledby": "err-titre" },
          h("h2", { id: "err-titre", class: "bloc-titre" }, `Erreurs (${d.erreurs.length})`),
          d.erreurs.length ? h("ol", { class: "erreurs" }, d.erreurs.slice(0, 30).map(e => h("li", {},
            h("span", { class: "erreur-meta" }, dateFr(e.ts), " · ", nomEtape(e.etape)),
            h("span", { class: "erreur-carte" }, `Carte jouée : ${nomCarte(e.carte)}`),
            h("span", { class: "erreur-msg" }, e.msg),
            h("button", { type: "button", class: "btn btn-lien", onclick: () => JEU.ui.fiche.open(e.fiche, e.msg) }, `Fiche : ${nomCarte(e.fiche)}`))))
            : h("p", { class: "vide" }, "Aucune erreur enregistrée.")),
        h("section", { "aria-labelledby": "revoir-titre" },
          h("h2", { id: "revoir-titre", class: "bloc-titre" }, "Fiches à revoir"),
          aRevoir.length ? h("ol", { class: "revoir" }, aRevoir.map(([id, n]) => h("li", {},
            h("button", { type: "button", class: "btn btn-lien", onclick: () => JEU.ui.fiche.open(id) }, nomCarte(id)), ` · ${n} erreur${n > 1 ? "s" : ""}`)))
            : h("p", { class: "vide" }, "Rien à revoir pour l’instant."),
          h("h2", { class: "bloc-titre" }, "Parties"),
          d.parties.length ? h("ol", { class: "parties" }, d.parties.map(p => h("li", {},
            dateFr(p.ts), " · ", p.resultat === "victoire" ? "Cas résolu" : "Patient dégradé", ` · ${p.pv} PV · ${p.erreurs} erreur${p.erreurs > 1 ? "s" : ""}`)))
            : h("p", { class: "vide" }, "Aucune partie terminée."),
          h("button", { type: "button", class: "btn btn-danger", id: "btn-reset", onclick: demanderReset }, "Effacer le journal")))));
  }

  function demanderReset() {
    const dlg = $("#confirm");
    dlg.showModal();
    $("#confirm-non").focus();
  }
  function init() {
    const dlg = $("#confirm");
    $("#confirm-non").addEventListener("click", () => dlg.close());
    $("#confirm-oui").addEventListener("click", () => { JEU.journal.reset(); dlg.close(); render(); $("#btn-reset").focus(); });
  }
  return { render, init };
})();
