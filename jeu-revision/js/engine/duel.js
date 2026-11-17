/**
 * Moteur de duel v2 (sans DOM) : règles de docs/PROMPT_PROJET.md.
 * – erreur dangereuse −30 PV, erreur mineure −10 PV, examen inutile −5 PV et +1 min de temps patient ;
 * – mode urgence : chronomètre (cas.chrono, en s) ; consultation : sans chronomètre ;
 * – étoiles 1 à 3 à la victoire selon PV, examens inutiles et temps.
 * Chaque coup exige une confiance (sur | hesitant | hasard).
 */
window.JEU = window.JEU || {};
JEU.REGLES = { dangereuse: 30, mineure: 10, inutile: 5, inutileTempsS: 60 };
/** Échelon de maîtrise travaillé par chaque phase clinique (PROGRESSION.md § 1). */
JEU.ECHELON_PHASE = { trier: 3, explorer: 5, differencier: 4, diagnostiquer: 6, traiter: 7 };

JEU.Duel = class Duel {
  /** @param cas  cas v2 ; @param opts { mode: "urgence"|"consultation"|"final"|"entrainement"|"examen" } */
  constructor(cas, opts = {}) {
    this.cas = cas;
    this.mode = opts.mode || cas.mode;
    this.chronoActif = (cas.mode === "urgence" || cas.mode === "final") && this.mode !== "entrainement";
    this.reset();
  }
  reset() {
    this.indexEtape = 0;
    this.pv = this.cas.pvInitial;
    this.revele = new Set();
    this.jouees = [];
    this.erreursPartie = 0;
    this.inutiles = 0;
    this.penaliteS = 0;
    this.t0 = JEU.horloge.now();
    this.tFin = null;
    this.statut = "en-cours";
  }
  get etape() { return this.cas.etapes[this.indexEtape]; }
  get echelon() { const e = this.etape; return e.echelon || JEU.ECHELON_PHASE[e.phase] || null; }
  get main() { const j = new Set(this.jouees.map(x => x.carte)); return this.etape.main.filter(id => !j.has(id)); }
  get objectifsRestants() { const ok = new Set(this.jouees.filter(j => j.compteObjectif).map(j => j.carte)); return this.etape.objectifs.filter(id => !ok.has(id)); }
  /** Temps patient écoulé (s) : horloge + pénalités d’examens inutiles. */
  tempsS() { return Math.round(((this.tFin || JEU.horloge.now()) - this.t0) / 1000) + this.penaliteS; }
  tempsRestantS() { return this.chronoActif ? this.cas.chrono - this.tempsS() : null; }

  play(idCarte, confiance) {
    if (this.statut !== "en-cours" || !this.main.includes(idCarte)) return null;
    if (!JEU.progression.CONFIANCES[confiance]) throw new Error("Choisis une confiance avant de jouer.");
    const e = this.etape;
    let r = Object.assign({ verdict: "neutre", msg: "Ce geste ne change rien à ce stade." }, e.regles[idCarte] || {});
    if (r.avant && !r.avant.requiert.every(id => this.jouees.some(j => j.carte === id))) r = Object.assign({}, r, { verdict: r.avant.verdict, msg: r.avant.msg });
    const compteObjectif = e.objectifs.includes(idCarte) && r.verdict !== "erreur" && r.verdict !== "inutile";
    let perte = 0;
    if (r.verdict === "erreur") { perte = JEU.REGLES[r.gravite] || JEU.REGLES.mineure; this.erreursPartie++; }
    if (r.verdict === "inutile") { perte = JEU.REGLES.inutile; this.inutiles++; this.penaliteS += JEU.REGLES.inutileTempsS; }
    this.pv = Math.max(0, this.pv - perte);
    if (r.revele) this.revele.add(r.revele);
    this.jouees.push({ carte: idCarte, verdict: r.verdict, compteObjectif, confiance });
    const res = { carte: idCarte, verdict: r.verdict, gravite: r.gravite || null, msg: r.msg, perte, confiance,
      fiche: r.verdict === "erreur" || r.verdict === "inutile" ? (r.fiche || idCarte) : null,
      revele: r.revele || null, etape: e.id, echelon: this.echelon, pathologie: e.pathologie, mortel: !!r.mortel,
      etapeGagnee: false, statut: this.statut, etoiles: null };
    if (this.pv <= 0) { this.statut = "defaite"; this.tFin = JEU.horloge.now(); res.statut = "defaite"; res.etoiles = 0; return res; }
    if (!this.objectifsRestants.length) {
      res.etapeGagnee = true;
      if (this.indexEtape >= this.cas.etapes.length - 1) { this.statut = "victoire"; this.tFin = JEU.horloge.now(); res.statut = "victoire"; res.etoiles = this.etoiles(); }
    }
    return res;
  }
  /**
   * Étoiles (victoire seulement) : 3 au départ ; −1 si PV < 80 ; −1 encore si PV < 50 ;
   * −1 si au moins un examen inutile ; −1 si le chrono est dépassé (urgence) ; minimum 1.
   */
  etoiles() {
    if (this.statut !== "victoire") return 0;
    let n = 3;
    const pct = this.pv / this.cas.pvInitial * 100;
    if (pct < 80) n--; if (pct < 50) n--;
    if (this.inutiles > 0) n--;
    if (this.chronoActif && this.tempsS() > this.cas.chrono) n--;
    return Math.max(1, n);
  }
  suivante() { if (this.indexEtape < this.cas.etapes.length - 1) { this.indexEtape++; this.jouees = []; return true; } return false; }
};
