/* Moteur d'illustrations médicales, planches anatomiques et courbes physiologiques annotées — Édition Haute Horlogerie Suisse */
window.MEDICAL_VISUALS = (function () {
  const CS_PLATES = {
    peau: { img: "assets/cs/ex-peau.webp", title: "Coupe anatomique de la peau & glandes sudoripares", note: "Épiderme, derme, glande eccrine (ACh/M3) et follicule pilo-sébacé (Gray)." },
    thorax: { img: "assets/cs/ex-thorax.webp", title: "Repères topographiques thoraciques & pleuro-pulmonaires", note: "Projection antérieure des plèvres (bleu) et des poumons (violet) pour l'auscultation et la percussion." },
    coeur: { img: "assets/cs/ex-coeur-vaisseaux.webp", title: "Foyers d'auscultation cardiaque & gros vaisseaux", note: "Repères aortique, pulmonaire, tricuspide et mitral + axes vasculaires." },
    abdomen: { img: "assets/cs/ex-abdomen.webp", title: "Topographie abdominale (9 quadrants & viscères)", note: "Projection pariétale des organes digestifs, hépatobiliaires et rétropéritonéaux." },
    neuro_nc: { img: "assets/cs/ex-neuro-nc.webp", title: "Base du crâne & émergence des nerfs crâniens (I–XII)", note: "Repères anatomiques des paires crâniennes et syndromes du tronc cérébral." },
    neuro_mot: { img: "assets/cs/ex-neuro-moteur.webp", title: "Voies motrices, réflexes & systématisation médullaire", note: "Distinction syndrome pyramidal (central) vs atteinte du motoneurone périphérique." },
    meninge: { img: "assets/cs/ex-meninge-gcs.webp", title: "Signes méningés & Échelle de coma de Glasgow (GCS)", note: "Raideur de nuque, signes de Kernig/Brudzinski et cotation E+V+M." },
    tete_cou: { img: "assets/cs/ex-tete-cou.webp", title: "Repères cervicaux, thyroïde & aires ganglionnaires", note: "Triangles antérieur/postérieur du cou, loge thyroïdienne et chaînes lymphatiques." },
    epaule: { img: "assets/cs/ex-epaule.webp", title: "Anatomie fonctionnelle de l'épaule & coiffe des rotateurs", note: "Repères osseux, espace sous-acromial et tests de conflit/rupture." },
    coude: { img: "assets/cs/ex-coude-main.webp", title: "Anatomie du coude, poignet & territoires nerveux de la main", note: "Nerfs médian, ulnaire et radial ; canal carpien et loge de Guyon." },
    hanche: { img: "assets/cs/ex-hanche.webp", title: "Articulation coxo-fémorale & repères pelviens", note: "Vascularisation de la tête fémorale et examen orthopédique de la hanche." },
    genou: { img: "assets/cs/ex-genou.webp", title: "Anatomie du genou (ménisques & ligaments croisés)", note: "Tests de Lachman, tiroirs et recherche de choc rotulien." },
    cheville: { img: "assets/cs/ex-cheville-pied.webp", title: "Cheville & pied (critères d'Ottawa & ligaments)", note: "Malléoles, ligament talo-fibulaire antérieur et arches plantaires." },
    rachis: { img: "assets/cs/ex-rachis.webp", title: "Rachis & dermatomes / racines nerveuses", note: "Drapeaux rouges rachidiens (queue de cheval) et manoeuvre de Lasègue." },
    seins: { img: "assets/cs/ex-seins.webp", title: "Glande mammaire & drainage lymphatique axillaire", note: "Quadrants mammaires, prolongement axillaire et ganglions sentinelles." },
    genital: { img: "assets/cs/ex-tr-genital.webp", title: "Anatomie pelvienne, urogénitale & toucher rectal", note: "Repères prostatiques, pelviens et urgences ischémiques/infectieuses." },
    pediatrie: { img: "assets/cs/ex-pediatrie.webp", title: "Repères pédiatriques, fontanelles & développement", note: "Constantes pédiatriques selon l'âge, courbes de croissance et signes de gravité." },
    geriatrie: { img: "assets/cs/ex-geriatrie.webp", title: "Évaluation gériatrique multidimensionnelle", note: "Fragilité, iatrogénie (STOPP/START), état confusionnel aigu et risque de chute." },
    psy: { img: "assets/cs/ex-psychiatrie.webp", title: "Examen du statut psychiatrique & tri du risque suicidaire", note: "Critères cliniques d'urgence psychiatrique et exclusion d'une cause organique." }
  };

  function detectDomain(code, title) {
    const t = (code + " " + title).toLowerCase();
    if (/peau|prurit|sudation|éruption|exanth|urticaire|ongle|cheveu|ulcère|plaie|brûlure/.test(t)) return { plate: "peau", curve: "autonome" };
    if (/ecg|cardia|palpit|thorac|syncope|pression artér|hypertens|choc|œdème|vein|artéri|souffle|lipothym/.test(t)) return { plate: "coeur", curve: "ecg" };
    if (/dyspn|toux|respir|asthme|bronch|hémoptys|pneumo|cyanose|expector|stridor|ronfl|apnée|satur/.test(t)) return { plate: "thorax", curve: "spiro" };
    if (/abdom|diarrh|constip|vomiss|nausée|ictère|hépat|digest|dysphag|hémorragie dig|ascite|périton|rect|méléna/.test(t)) return { plate: "abdomen", curve: "parcours" };
    if (/diplopie|vision|oeil|œil|vertige|céphal|coma|conscience|convuls|paralys|faiblesse|engourd|trembl|marche|mémoire|confus|parole|aphas/.test(t)) return { plate: "neuro_nc", curve: "davenport" };
    if (/méning|nuque/.test(t)) return { plate: "meninge", curve: "parcours" };
    if (/motric|réflex|parésie|sensibil|atax/.test(t)) return { plate: "neuro_mot", curve: "ecg" };
    if (/cou|thyro|goitre|voix|dysphon|gorge|odynoph|ganglion|adénopath|oreille|surdité|acouph|nez|épistaxis/.test(t)) return { plate: "tete_cou", curve: "autonome" };
    if (/épaule/.test(t)) return { plate: "epaule", curve: "parcours" };
    if (/coude|poignet|main|doigt/.test(t)) return { plate: "coude", curve: "parcours" };
    if (/hanche|bassin/.test(t)) return { plate: "hanche", curve: "parcours" };
    if (/genou/.test(t)) return { plate: "genou", curve: "parcours" };
    if (/cheville|pied/.test(t)) return { plate: "cheville", curve: "parcours" };
    if (/dos|rachis|lomb|cervic/.test(t)) return { plate: "rachis", curve: "parcours" };
    if (/sein|mamma/.test(t)) return { plate: "seins", curve: "parcours" };
    if (/urin|hématur|dysur|miction|rénal|polyur|oligur|génital|vaginal|pelv|grossesse|accouch|aménorrh|testic|scrot|prostat/.test(t)) return { plate: "genital", curve: "davenport" };
    if (/enfant|pédiatr|nourrisson|néonatal|prématur|croissance/.test(t)) return { plate: "pediatrie", curve: "oxy" };
    if (/âgé|gériatr|chute|démence/.test(t)) return { plate: "geriatrie", curve: "parcours" };
    if (/anxi|dépress|suicid|psych|hallucin|sommeil|dépendance|alcool|addict|panique/.test(t)) return { plate: "psy", curve: "autonome" };
    if (/glycém|diab|soif|poids|obés|fièvre|hypotherm|acide|ion|kaliém|natrém|anémie|coagul/.test(t)) return { plate: "coeur", curve: "davenport" };
    return { plate: "thorax", curve: "oxy" };
  }

  function svgECG() {
    return `
    <svg viewBox="0 0 460 175" width="100%" style="background:#fff;border-radius:12px;border:1px solid #cbd5e1;box-shadow:inset 0 1px 3px rgba(15,23,42,0.04);">
      <defs>
        <pattern id="ecgGrid" width="20" height="20" patternUnits="userSpaceOnUse">
          <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#fee2e2" stroke-width="1"/>
        </pattern>
      </defs>
      <rect width="460" height="175" fill="url(#ecgGrid)"/>
      <text x="12" y="18" font-size="10.8" font-weight="800" fill="#0f172a">Tracé ECG annoté : Rythme sinusal normal (bleu) vs Sus-décalage ST / STEMI (rouge)</text>
      <!-- Normal PQRST -->
      <path d="M 18 115 L 45 115 Q 55 98 65 115 L 82 115 L 88 125 L 98 48 L 108 134 L 116 115 L 145 115 Q 165 88 185 115 L 220 115" fill="none" stroke="#1d4ed8" stroke-width="2.6"/>
      <!-- STEMI PQRST -->
      <path d="M 235 115 L 260 115 Q 270 98 280 115 L 295 115 L 300 124 L 310 48 L 320 120 L 328 84 Q 355 72 385 95 L 405 115 L 442 115" fill="none" stroke="#dc2626" stroke-width="2.8"/>
      <text x="51" y="94" font-size="10" font-weight="700" fill="#1d4ed8">P</text>
      <text x="92" y="42" font-size="10" font-weight="700" fill="#1d4ed8">QRS</text>
      <text x="162" y="88" font-size="10" font-weight="700" fill="#1d4ed8">T</text>
      <text x="122" y="133" font-size="9" fill="#1e40af">ST isoélectrique</text>
      <circle cx="348" cy="81" r="4" fill="#dc2626"/>
      <text x="298" y="65" font-size="9.4" font-weight="800" fill="#b91c1c">Sus-décalage ST (onde de Pardee)</text>
      <text x="206" y="156" font-size="8.6" font-weight="700" fill="#7f1d1d">Urgence : ECG &lt; 10 min dès le 1er contact · Coronarographie si STEMI</text>
    </svg>`;
  }

  function svgSpiro() {
    return `
    <svg viewBox="0 0 460 175" width="100%" style="background:#fff;border-radius:12px;border:1px solid #cbd5e1;box-shadow:inset 0 1px 3px rgba(15,23,42,0.04);">
      <text x="12" y="18" font-size="10.8" font-weight="800" fill="#0f172a">Courbe Débit-Volume (Spirométrie) : Normal vs Obstructif vs Restrictif</text>
      <line x1="50" y1="138" x2="430" y2="138" stroke="#475569" stroke-width="1.5"/>
      <line x1="50" y1="30" x2="50" y2="155" stroke="#475569" stroke-width="1.5"/>
      <text x="14" y="42" font-size="9.5" fill="#475569">Débit</text>
      <text x="385" y="152" font-size="9.5" fill="#475569">Volume (L)</text>
      <!-- Normal -->
      <path d="M 65 138 L 105 42 L 320 138" fill="none" stroke="#16a34a" stroke-width="2.8"/>
      <!-- Obstructif (concave) -->
      <path d="M 65 138 L 115 80 Q 175 128 320 138" fill="none" stroke="#dc2626" stroke-width="2.6" stroke-dasharray="5,3"/>
      <!-- Restrictif (miniature) -->
      <path d="M 135 138 L 165 68 L 265 138" fill="none" stroke="#2563eb" stroke-width="2.4"/>
      <text x="120" y="46" font-size="9.5" font-weight="700" fill="#15803d">Normal (VEMS/CVF ≥ 0.70)</text>
      <text x="180" y="106" font-size="9.5" font-weight="700" fill="#b91c1c">Obstructif (aspect concave · VEMS/CVF &lt; 0.70)</text>
      <text x="268" y="88" font-size="9.5" font-weight="700" fill="#1d4ed8">Restrictif (CPT &lt; 80 %)</text>
      <text x="58" y="166" font-size="8.8" fill="#334155">Asthme : réversibilité ≥ +12 % et +200 mL après bronchodilatateur · BPCO : persistance post-BD</text>
    </svg>`;
  }

  function svgDavenport() {
    return `
    <svg viewBox="0 0 460 175" width="100%" style="background:#fff;border-radius:12px;border:1px solid #cbd5e1;box-shadow:inset 0 1px 3px rgba(15,23,42,0.04);">
      <text x="12" y="18" font-size="10.8" font-weight="800" fill="#0f172a">Diagramme de Davenport (Gazométrie : pH / HCO₃⁻ / PaCO₂)</text>
      <line x1="55" y1="145" x2="425" y2="145" stroke="#334155" stroke-width="1.5"/>
      <line x1="55" y1="30" x2="55" y2="145" stroke="#334155" stroke-width="1.5"/>
      <!-- Isobars PaCO2 -->
      <path d="M 90 135 Q 240 105 390 42" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4,3"/>
      <path d="M 90 112 Q 240 82 390 25" fill="none" stroke="#0f172a" stroke-width="1.8"/>
      <path d="M 90 148 Q 250 125 405 70" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4,3"/>
      <!-- Normal point -->
      <circle cx="240" cy="84" r="6" fill="#16a34a"/>
      <text x="249" y="82" font-size="9.5" font-weight="800" fill="#15803d">Normal (pH 7.40 · HCO₃⁻ 24 · PaCO₂ 40)</text>
      <rect x="65" y="36" width="132" height="32" rx="6" fill="#fee2e2" stroke="#fca5a5"/>
      <text x="72" y="50" font-size="9" font-weight="700" fill="#991b1b">Acidose respiratoire</text>
      <text x="72" y="62" font-size="8.5" fill="#7f1d1d">PaCO₂ ↑, pH &lt; 7.35</text>
      <rect x="65" y="106" width="132" height="32" rx="6" fill="#fef3c7" stroke="#fcd34d"/>
      <text x="72" y="120" font-size="9" font-weight="700" fill="#92400e">Acidose métabolique</text>
      <text x="72" y="132" font-size="8.5" fill="#78350f">HCO₃⁻ ↓, trou anionique ?</text>
      <rect x="292" y="106" width="128" height="32" rx="6" fill="#dbeafe" stroke="#93c5fd"/>
      <text x="298" y="120" font-size="9" font-weight="700" fill="#1e40af">Alcalose respiratoire</text>
      <text x="298" y="132" font-size="8.5" fill="#1e3a8a">PaCO₂ ↓, hyperventilation</text>
      <text x="58" y="164" font-size="8.8" fill="#334155">Axe X : pH (7.10 → 7.60) · Axe Y : Bicarbonates [HCO₃⁻] (mmol/L) · Courbe centrale = isobare PaCO₂ 40 mmHg</text>
    </svg>`;
  }

  function svgOxy() {
    return `
    <svg viewBox="0 0 460 175" width="100%" style="background:#fff;border-radius:12px;border:1px solid #cbd5e1;box-shadow:inset 0 1px 3px rgba(15,23,42,0.04);">
      <text x="12" y="18" font-size="10.8" font-weight="800" fill="#0f172a">Courbe de dissociation Hb-O₂ (Effet Bohr) &amp; Cibles SpO₂ (Smarter Medicine CH)</text>
      <line x1="55" y1="142" x2="430" y2="142" stroke="#334155" stroke-width="1.5"/>
      <line x1="55" y1="28" x2="55" y2="142" stroke="#334155" stroke-width="1.5"/>
      <!-- Plateau target highlight -->
      <rect x="295" y="29" width="128" height="16" rx="4" fill="#dcfce7" opacity="0.65"/>
      <!-- Sigmoid Normal -->
      <path d="M 55 142 C 110 140, 145 70, 225 48 C 295 36, 360 34, 420 33" fill="none" stroke="#1d4ed8" stroke-width="2.8"/>
      <!-- Right shift (Bohr: acidose, fièvre, ↑2,3-BPG) -->
      <path d="M 55 142 C 130 140, 180 85, 265 55 C 325 42, 375 37, 420 35" fill="none" stroke="#dc2626" stroke-width="2.2" stroke-dasharray="5,3"/>
      <text x="72" y="68" font-size="8.8" font-weight="700" fill="#1e40af">Normale (P50 ≈ 27 mmHg)</text>
      <text x="225" y="92" font-size="8.6" font-weight="700" fill="#b91c1c">Déviation droite : pH ↓, T° ↑, PaCO₂ ↑ → O₂ libéré ↑</text>
      <!-- Clean non-overlapping target pill -->
      <rect x="172" y="112" width="248" height="20" rx="5" fill="#dcfce7" stroke="#86efac"/>
      <text x="180" y="125" font-size="8.6" font-weight="800" fill="#14532d">Cible aiguë : SpO₂ 90–94 % (BPCO : 88–92 %)</text>
      <text x="55" y="164" font-size="8.5" fill="#334155">Axe X : PaO₂ (mmHg) · Axe Y : SaO₂ (%) · Smarter Medicine : éviter O₂ libérale si SpO₂ ≥ 94 %</text>
    </svg>`;
  }

  function svgAutonome() {
    return `
    <svg viewBox="0 0 460 175" width="100%" style="background:#fff;border-radius:12px;border:1px solid #cbd5e1;box-shadow:inset 0 1px 3px rgba(15,23,42,0.04);">
      <text x="12" y="18" font-size="10.8" font-weight="800" fill="#0f172a">Système nerveux autonome, neurotransmetteurs &amp; cibles pharmacologiques (AIPS)</text>
      <rect x="16" y="34" width="114" height="44" rx="10" fill="#dbeafe" stroke="#3b82f6"/>
      <text x="24" y="53" font-size="9.2" font-weight="800" fill="#1e3a8a">Hypothalamus / SNC</text>
      <text x="24" y="67" font-size="8.2" fill="#1e40af">Thermostat &amp; stress</text>
      <line x1="130" y1="56" x2="162" y2="56" stroke="#475569" stroke-width="2"/>
      <rect x="162" y="31" width="134" height="50" rx="10" fill="#fef3c7" stroke="#f59e0b"/>
      <text x="170" y="48" font-size="9.2" font-weight="800" fill="#92400e">Voie Sympathique</text>
      <text x="170" y="61" font-size="8.2" fill="#78350f">Prégangl. : ACh (N)</text>
      <text x="170" y="73" font-size="8.2" fill="#78350f">Eccrine : ACh (M3)</text>
      <line x1="296" y1="47" x2="328" y2="47" stroke="#16a34a" stroke-width="2"/>
      <line x1="296" y1="68" x2="328" y2="108" stroke="#dc2626" stroke-width="2"/>
      <rect x="328" y="28" width="118" height="42" rx="9" fill="#dcfce7" stroke="#16a34a"/>
      <text x="335" y="45" font-size="8.8" font-weight="800" fill="#14532d">Glande eccrine (M3)</text>
      <text x="335" y="58" font-size="7.8" fill="#166534">Tox. botulique / Anti-M</text>
      <rect x="328" y="84" width="118" height="48" rx="9" fill="#fee2e2" stroke="#dc2626"/>
      <text x="335" y="101" font-size="8.8" font-weight="800" fill="#7f1d1d">Vaisseaux / Cœur</text>
      <text x="335" y="114" font-size="7.8" fill="#991b1b">α1 (vasoconstr.), β1/β2</text>
      <text x="335" y="125" font-size="7.8" fill="#991b1b">Phéo : α-bloquant d'abord</text>
      <rect x="16" y="96" width="298" height="62" rx="10" fill="#f8fafc" stroke="#cbd5e1"/>
      <text x="24" y="113" font-size="8.8" font-weight="800" fill="#0f172a">Pièges majeurs Examen fédéral :</text>
      <text x="24" y="127" font-size="8" fill="#334155">1. Hypoglycémie sous β-bloquant : sueurs M3 conservées.</text>
      <text x="24" y="140" font-size="8" fill="#334155">2. Phéochromocytome : bloquer α1 (7–14 j) AVANT β-bloquant.</text>
      <text x="24" y="152" font-size="7.8" fill="#475569">3. Syndrome sérotoninergique : clonus spontané (Hunter).</text>
    </svg>`;
  }

  function svgParcours() {
    return `
    <svg viewBox="0 0 460 175" width="100%" style="background:#fff;border-radius:12px;border:1px solid #cbd5e1;box-shadow:inset 0 1px 3px rgba(15,23,42,0.04);">
      <text x="12" y="18" font-size="10.8" font-weight="800" fill="#0f172a">Parcours clinique suisse complet : Urgence → Bilan ciblé → Traitement → Sortie</text>
      <rect x="14" y="36" width="98" height="62" rx="10" fill="#fee2e2" stroke="#dc2626" stroke-width="1.8"/>
      <text x="22" y="54" font-size="9.5" font-weight="800" fill="#991b1b">1. Tri &amp; ABCDE</text>
      <text x="22" y="68" font-size="8.2" fill="#7f1d1d">Drapeaux rouges</text>
      <text x="22" y="80" font-size="8.2" fill="#7f1d1d">Stabiliser AVANT</text>
      <text x="22" y="92" font-size="8.2" fill="#7f1d1d">confirmation</text>
      <path d="M 112 67 L 128 67" stroke="#475569" stroke-width="2"/>
      <rect x="128" y="36" width="100" height="62" rx="10" fill="#dbeafe" stroke="#2563eb" stroke-width="1.8"/>
      <text x="136" y="54" font-size="9.5" font-weight="800" fill="#1e3a8a">2. Bilan gradué</text>
      <text x="136" y="68" font-size="8.2" fill="#1e40af">1re intention ciblée</text>
      <text x="136" y="80" font-size="8.2" fill="#1e40af">2e int. (confirme)</text>
      <text x="136" y="92" font-size="8.2" fill="#1e40af">Smarter Medicine</text>
      <path d="M 228 67 L 244 67" stroke="#475569" stroke-width="2"/>
      <rect x="244" y="36" width="100" height="62" rx="10" fill="#dcfce7" stroke="#16a34a" stroke-width="1.8"/>
      <text x="252" y="54" font-size="9.5" font-weight="800" fill="#14532d">3. PEC Suisse</text>
      <text x="252" y="68" font-size="8.2" fill="#166534">Compendium / AIPS</text>
      <text x="252" y="80" font-size="8.2" fill="#166534">Guidelines SSI/SGAIM</text>
      <text x="252" y="92" font-size="8.2" fill="#166534">Ambulat. vs Hôpital</text>
      <path d="M 344 67 L 360 67" stroke="#475569" stroke-width="2"/>
      <rect x="360" y="36" width="88" height="62" rx="10" fill="#fef3c7" stroke="#d97706" stroke-width="1.8"/>
      <text x="367" y="54" font-size="9.5" font-weight="800" fill="#92400e">4. Sortie</text>
      <text x="367" y="68" font-size="8.2" fill="#78350f">Ordonnance revue</text>
      <text x="367" y="80" font-size="8.2" fill="#78350f">Signes d'alerte</text>
      <text x="367" y="92" font-size="8.2" fill="#78350f">Suivi médecin (OFSP)</text>
      <rect x="14" y="112" width="434" height="48" rx="10" fill="#f8fafc" stroke="#cbd5e1"/>
      <text x="22" y="130" font-size="8.8" font-weight="800" fill="#0f172a">Règle d'or Examen fédéral (PROFILES / CanMEDS) :</text>
      <text x="22" y="145" font-size="7.9" fill="#334155">Hiérarchiser : Très fréquentes → Fréquentes → Peu fréquentes → Rares → « À ne pas manquer ».</text>
    </svg>`;
  }

  const SVG_BUILDERS = {
    ecg: svgECG,
    spiro: svgSpiro,
    davenport: svgDavenport,
    oxy: svgOxy,
    autonome: svgAutonome,
    parcours: svgParcours
  };

  function formatCausesByTier(mastery) {
    if (!mastery || !mastery.causes || !mastery.causes.length) return "";
    const urg = mastery.causes.filter(c => c.urg);
    const tiers = ["Très fréquente", "Fréquente", "Peu fréquente", "Moins fréquente", "Rare"];
    const tierColors = {
      "Très fréquente": { bg: "#ecfdf5", bd: "#a7f3d0", tx: "#065f46" },
      "Fréquente": { bg: "#eff6ff", bd: "#bfdbfe", tx: "#1e40af" },
      "Peu fréquente": { bg: "#fefce8", bd: "#fde68a", tx: "#92400e" },
      "Moins fréquente": { bg: "#f8fafc", bd: "#cbd5e1", tx: "#334155" },
      "Rare": { bg: "#f5f3ff", bd: "#ddd6fe", tx: "#5b21b6" }
    };
    const tierLines = tiers.map(t => {
      const items = mastery.causes.filter(c => !c.urg && (c.tier || "Fréquente") === t);
      if (!items.length) return "";
      const st = tierColors[t] || tierColors["Fréquente"];
      const names = items.map(c => typeof c.pct === "number" ? `${c.n} <b>(${c.pct}%)</b>` : c.n).join(" · ");
      return `<div style="margin-top:4px;line-height:1.42;">
        <span style="display:inline-block;background:${st.bg};border:1px solid ${st.bd};color:${st.tx};font-weight:800;font-size:0.67rem;padding:1px 7px;border-radius:999px;margin-right:6px;vertical-align:baseline;">${t}</span><span style="color:#1e293b;">${names}</span>
      </div>`;
    }).filter(Boolean).join("");
    const urgStr = urg.map(c => typeof c.pct === "number" ? `${c.n} <b>(${c.pct}%)</b>` : c.n).join(" · ");
    return `
      <div style="background:linear-gradient(145deg,#ffffff,#f8fafc);border:1.5px solid #cbd5e1;border-radius:14px;padding:9px 12px;margin-top:8px;font-size:0.75rem;line-height:1.38;box-shadow:0 4px 12px rgba(15,23,42,0.03);">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:4px;">
          <span style="font-weight:800;color:#0f172a;font-size:0.78rem;letter-spacing:-0.01em;">🗺️ Stratification panoramique des causes</span>
          <span style="background:#0f172a;color:#fff;font-size:0.66rem;font-weight:800;padding:1px 8px;border-radius:999px;">${mastery.causes.length} DD répertoriés</span>
        </div>
        ${urg.length ? `<div style="background:#fef2f2;border:1px solid #fecaca;border-radius:8px;padding:4px 8px;color:#991b1b;margin-bottom:4px;"><strong style="color:#b91c1c;">🚨 À ne pas manquer :</strong> ${urgStr}</div>` : ""}
        <div>${tierLines}</div>
      </div>`;
  }

  function renderVisualBlock(code, title, mastery) {
    const dom = detectDomain(code, title);
    const plate = CS_PLATES[dom.plate] || CS_PLATES.thorax;
    const svgFn = SVG_BUILDERS[dom.curve] || svgParcours;
    const causesHtml = formatCausesByTier(mastery);

    return `
      <div style="display:grid;grid-template-columns:122px 1fr;gap:10px;align-items:center;background:linear-gradient(145deg,#ffffff,#f8fafc);border:1.5px solid #cbd5e1;border-radius:14px;padding:8px 10px;margin-top:8px;box-shadow:0 4px 14px rgba(15,23,42,0.04);">
        <div style="text-align:center;background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:6px 4px;box-shadow:inset 0 1px 2px rgba(0,0,0,0.02);">
          <img src="${plate.img}" alt="${plate.title}" style="width:108px;height:90px;object-fit:contain;display:block;margin:0 auto;" />
          <div style="font-size:0.66rem;font-weight:800;color:#334155;margin-top:4px;line-height:1.15;">${plate.title}</div>
        </div>
        <div>
          ${svgFn()}
        </div>
      </div>
      ${causesHtml}
    `;
  }

  function renderCombatPanoramique(code, title, mastery) {
    const dom = detectDomain(code, title);
    const plate = CS_PLATES[dom.plate] || CS_PLATES.thorax;
    const causesHtml = formatCausesByTier(mastery);
    return `
      <details style="background:linear-gradient(145deg,#ffffff,#f8fafc);border:1.5px solid #cbd5e1;border-radius:16px;padding:12px 16px;margin-bottom:18px;box-shadow:0 8px 24px rgba(15,23,42,0.04);">
        <summary style="cursor:pointer;font-weight:800;font-size:0.92rem;color:#0f172a;display:flex;align-items:center;justify-content:space-between;gap:10px;">
          <span>🩺 Panoramique clinique ${code} : Causes par fréquence (Très fréquentes → Rares), Urgences « À ne pas manquer » &amp; Repères anatomiques</span>
          <span style="font-size:0.74rem;font-weight:700;color:#2563eb;background:#eff6ff;border:1px solid #bfdbfe;padding:3px 10px;border-radius:999px;flex-shrink:0;">Déployer l'atlas ▾</span>
        </summary>
        <div style="display:grid;grid-template-columns:150px 1fr;gap:16px;align-items:start;margin-top:12px;padding-top:10px;border-top:1px solid #e2e8f0;">
          <div style="text-align:center;background:#fff;border:1px solid #cbd5e1;border-radius:12px;padding:8px;">
            <img src="${plate.img}" alt="${plate.title}" style="width:132px;height:112px;object-fit:contain;display:block;margin:0 auto;" />
            <div style="font-size:0.72rem;font-weight:800;color:#334155;margin-top:6px;line-height:1.2;">${plate.title}</div>
            <div style="font-size:0.65rem;color:#64748b;margin-top:3px;line-height:1.2;">${plate.note}</div>
          </div>
          <div>
            ${svgParcours()}
            ${causesHtml}
          </div>
        </div>
      </details>
    `;
  }

  return { renderVisualBlock, renderCombatPanoramique, CS_PLATES };
})();
