/**
 * Tableau de bord (PROGRESSION.md § 2–3) : grade, préparation par domaine PROFILES,
 * carte de chaleur spécialité × échelon, calibration, angles morts, vitesse, Leitner,
 * Ronde, spécialités faibles, parties, export / import JSON, remise à zéro.
 */
window.JEU = window.JEU || {};
JEU.ui = JEU.ui || {};
JEU.ui.tableau = (function () {
  const { h, $, pct, dateFr } = JEU.dom;
  const P = () => JEU.progression;
  const TYPES = { "sur": "Erreur « sûr »", "drapeau-rouge": "Drapeau rouge manqué", "differentiel-mortel": "Différentiel mortel oublié" };
  let message = null;

  const niveau = p => p === null || p === undefined ? "vide" : p >= 0.85 ? "fort" : p >= 0.7 ? "moyen" : p >= 0.5 ? "faible" : "critique";

  function render() {
    const pr = P(), patho = JEU.registry.pathologies();
    const g = pr.grade(patho), cal = pr.calibration(), am = pr.anglesMorts(), vit = pr.vitesse(), ch = pr.chaleur();
    const it = Object.values(pr.items()), dues = pr.dues(), prep = pr.preparation(patho, JEU.profiles);
    const sps = JEU.registry.ordreParcours().filter(s => JEU.registry.specialite(s.id));
    const ronde = pr.rondeDuJour();
    const root = $("#vue-tableau");
    root.replaceChildren(h("section", { class: "page tableau", "aria-labelledby": "tb-titre" },
      h("header", { class: "page-tete" }, h("p", { class: "sur-titre" }, "Internat · Tableau de bord"), h("h1", { id: "tb-titre" }, "Mesure ta progression réelle."),
        h("p", {}, "Chaque coup compte : échelon, réponse, confiance, temps, gravité. Rien ne quitte ton navigateur sans export.")),
      message ? h("p", { class: `msg msg--${message.type}`, role: "status", id: "tb-message" }, message.t) : null,
      h("div", { class: "tb-grille" },
        h("section", { class: "tb-bloc", id: "tb-grade" }, h("h2", {}, "Grade"),
          h("p", { class: "grade" }, h("strong", {}, g.grade)),
          h("div", { class: "systeme-barre", role: "progressbar", "aria-valuemin": "0", "aria-valuemax": "100", "aria-valuenow": String(Math.round(g.part * 100)), "aria-label": "Pathologies maîtrisées" }, h("span", { style: `width:${Math.round(g.part * 100)}%` })),
          h("p", {}, `${g.n}/${g.total} pathologies maîtrisées. Une pathologie est maîtrisée quand ses 7 échelons sont réussis « sûr » à J0, J+1 et J+7.`)),
        h("section", { class: "tb-bloc", id: "tb-ronde" }, h("h2", {}, "Ronde du jour · 20 min"),
          h("p", {}, ronde.length ? `Faite aujourd’hui : ${ronde.reduce((a, r) => a + r.n, 0)} question(s).` : "Pas encore faite aujourd’hui."),
          h("p", {}, `${dues.length} échelon(s) à revoir, dont ${dues.filter(x => x.angleMort).length} angle(s) mort(s).`),
          h("button", { type: "button", class: "btn btn-primaire", id: "btn-ronde", onclick: () => JEU.ui.quiz.demarrer("ronde") }, "Lancer la Ronde"))),
      h("section", { class: "tb-bloc", id: "tb-chaleur" }, h("h2", {}, "Carte de chaleur · spécialité × échelon"),
        h("div", { class: "table-defile" }, h("table", { class: "chaleur" },
          h("thead", {}, h("tr", {}, h("th", { scope: "col" }, "Spécialité"), pr.ECHELONS.map(([n, t]) => h("th", { scope: "col", title: t }, `${n}. ${t}`)))),
          h("tbody", {}, sps.map(s => {
            const st = pr.parSpecialite(s.id);
            return h("tr", { "data-specialite": s.id }, h("th", { scope: "row" }, s.nom, st.faible ? h("span", { class: "tag-faible" }, "< 70 %") : null),
              pr.ECHELONS.map(([n]) => { const c = ch[`${s.id}|${n}`]; const p = c ? c.precision : null;
                return h("td", { class: `cellule cellule--${niveau(p)}`, "data-echelon": String(n) }, c ? `${pct(p)} (${c.n})` : "—"); }));
          })))),
        h("p", { class: "aide" }, "Rouge : moins de 50 %. Orange : moins de 70 %. Vert : 85 % et plus. Entre parenthèses : nombre de coups jugés.")),
      h("div", { class: "tb-grille" },
        h("section", { class: "tb-bloc", id: "tb-calibration" }, h("h2", {}, "Calibration"),
          h("table", { class: "calib" }, h("thead", {}, h("tr", {}, h("th", { scope: "col" }, "Confiance"), h("th", { scope: "col" }, "Coups"), h("th", { scope: "col" }, "Réussite"))),
            h("tbody", {}, Object.entries(pr.CONFIANCES).map(([k, t]) => h("tr", { "data-conf": k }, h("th", { scope: "row" }, t), h("td", {}, String(cal[k].n)), h("td", { class: "calib-pct" }, pct(cal[k].precision)))))),
          cal.exces ? h("p", { class: "alerte-verif", id: "exces-confiance" }, "Excès de confiance : tu réussis moins de 80 % de tes coups « sûr », ou moins bien qu’en « hésitant ».") : h("p", { class: "aide" }, "Bien calibré : « sûr » ≥ 80 % et au-dessus de « hésitant »."),
          h("p", { class: "aide" }, "Un coup juste « au hasard » ne compte pas comme maîtrisé.")),
        h("section", { class: "tb-bloc", id: "tb-vitesse" }, h("h2", {}, "Vitesse"),
          h("ul", { class: "vitesse" }, pr.ECHELONS.map(([n, t]) => h("li", {}, `${n}. ${t} : `, vit[n].median ? `${Math.round(vit[n].median / 100) / 10} s (${vit[n].n})` : "—"))),
          h("p", { id: "vitesse-urgence", class: vit.urgence.atteint === false ? "alerte-verif" : "" }, `Urgence : temps médian ${vit.urgence.median ? Math.round(vit.urgence.median / 100) / 10 + " s" : "—"} · objectif < 20 s${vit.urgence.atteint === null ? "" : vit.urgence.atteint ? " : atteint." : " : pas encore."}`))),
      h("section", { class: "tb-bloc", id: "tb-angles" }, h("h2", {}, "Angles morts"),
        am.length ? h("ul", { class: "erreurs angles-morts" }, am.map(x => { const c = JEU.registry.card(x.carte); const k = x.cas && JEU.registry.cas(x.cas);
          return h("li", { "data-carte": x.carte },
            h("span", { class: "erreur-meta" }, dateFr(x.dernier), " · ", k ? k.titre : x.src === "ronde" ? "Ronde" : "Fondamentaux", " · ", h("strong", { class: "am-n" }, `${x.n}×`)),
            h("span", { class: "erreur-carte" }, c ? c.court : x.carte, " ", x.types.map(t => h("span", { class: `tag-am tag-am--${t}` }, TYPES[t]))),
            h("button", { type: "button", class: "btn btn-lien", onclick: () => JEU.ui.fiche.open(x.fiche) }, "Ouvrir la fiche")); }))
          : h("p", { class: "vide" }, "Aucun angle mort. Une erreur commise « sûr » apparaîtra ici en premier.")),
      h("div", { class: "tb-grille" },
        h("section", { class: "tb-bloc", id: "tb-leitner" }, h("h2", {}, "Répétition espacée · Leitner"),
          h("ol", { class: "leitner" }, pr.LEITNER.map((j, i) => h("li", { "data-boite": String(i + 1) }, h("strong", {}, `Boîte ${i + 1}`), ` · ${j ? "J+" + j : "même jour"} · `,
            h("span", { class: "leitner-n" }, String(it.filter(x => x.boite === i + 1).length))))),
          h("p", { class: "aide" }, "Juste et sûr ou hésitant : boîte suivante. Juste au hasard ou faux : boîte 1. Faux et sûr : angle mort, revu en premier.")),
        h("section", { class: "tb-bloc", id: "tb-preparation" }, h("h2", {}, "Préparation par domaine PROFILES"),
          h("table", { class: "calib" }, h("thead", {}, h("tr", {}, h("th", { scope: "col" }, "Domaine"), h("th", { scope: "col" }, "Maîtrisées"), h("th", { scope: "col" }, "SSP touchées"))),
            h("tbody", {}, Object.entries(prep).map(([k, x]) => h("tr", { "data-domaine": k }, h("th", { scope: "row" }, `${k} · ${x.label}`),
              h("td", {}, x.total ? `${x.maitrisees}/${x.total} (${pct(x.part)})` : "—"), h("td", {}, `${x.sspTouchees}/${x.sspTotal}`))))),
          h("p", { class: "aide" }, "Seules les pathologies maîtrisées comptent."))),
      h("section", { class: "tb-bloc", id: "tb-donnees" }, h("h2", {}, "Sauvegarde"),
        h("p", {}, "Le navigateur seul peut perdre tes données. Exporte-les ; l’import fusionne sans rien écraser."),
        h("div", { class: "debrief-actions" },
          h("button", { type: "button", class: "btn btn-primaire", id: "btn-export", onclick: exporter }, "Exporter (JSON)"),
          h("label", { class: "btn", for: "fichier-import" }, "Importer (JSON)"),
          h("input", { type: "file", id: "fichier-import", accept: "application/json,.json", class: "sr-only", onchange: ev => importerFichier(ev.target.files[0]) }),
          h("button", { type: "button", class: "btn btn-danger", id: "btn-reset", onclick: confirmerReset }, "Tout effacer")),
        h("p", { class: "aide" }, `Schéma ${pr.SCHEMA} · version ${pr.VERSION} · ${pr.get().coups.length} coup(s) enregistrés.`))));
  }

  function exporter() {
    const blob = new Blob([P().exporter()], { type: "application/json" });
    const a = h("a", { href: URL.createObjectURL(blob), download: `internat-progression-${P().jourDe(JEU.horloge.now())}.json` });
    document.body.append(a); a.click(); a.remove();
    message = { type: "ok", t: "Export prêt : garde ce fichier en lieu sûr." }; render();
  }
  function importerTexte(t) {
    const r = P().importer(t);
    message = r.ok ? { type: "ok", t: `Import réussi : ${r.ajoutes} élément(s) ajouté(s), rien d’écrasé.` } : { type: "ko", t: "Import refusé : " + r.erreurs.join(" ") };
    render(); return r;
  }
  function importerFichier(f) { if (!f) return; const rd = new FileReader(); rd.onload = () => importerTexte(rd.result); rd.readAsText(f); }
  function confirmerReset() {
    const dlg = $("#confirm"); dlg.showModal(); $("#confirm-non").focus();
    $("#confirm-oui").onclick = () => { P().reset(); dlg.close(); message = { type: "ok", t: "Progression effacée." }; render(); $("#btn-reset").focus(); };
    $("#confirm-non").onclick = () => dlg.close();
  }
  return { render, importerTexte };
})();
