"""Besoins des introuvables : modalité, région, côté, MIN puis CIBLE."""
import json
import sys
from pathlib import Path

from portes import modalite_de, plan_de

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "harnais" / "scripts" / "legion"))
import socle

# Table du catalogue, sources de niveau A seulement. Les exclues n'y figurent pas.
ROUTES = {
    "RX": ["nih_cxr14", "vindr", "commons", "europepmc", "pmc_oa", "medpix2", "openi"],
    "TDM": ["idc", "tcia", "medpix2", "commons", "europepmc", "pmc_oa", "openi"],
    "IRM": ["openneuro", "idc", "medpix2", "commons", "europepmc", "pmc_oa", "openi"],
    "US": ["commons", "europepmc", "pmc_oa", "medpix2", "openi"],
    "MN": ["idc", "commons", "europepmc", "pmc_oa", "medpix2"],
    "DERM": ["isic", "europepmc", "pmc_oa"],
    "FO": ["odir", "europepmc", "pmc_oa"],
    "ENDO": ["kvasir", "zenodo_figshare", "europepmc", "pmc_oa"],
    "ECG": ["ptbxl", "europepmc", "pmc_oa"],
    "EEG": ["openneuro", "europepmc", "pmc_oa"],
    "PSG": ["sleep_edf", "europepmc", "pmc_oa"],
    "CTG": ["ctu_uhb", "europepmc", "pmc_oa"],
    "AUTRE": ["commons", "europepmc", "pmc_oa", "openi", "zenodo_figshare"],
}


def charger():
    diagnostics = socle.diagnostics()
    besoins = []
    for m in socle.introuvables():
        dx = diagnostics.get(m["id"], {})
        cliche = m.get("cliche") or dx.get("cliche") or ""
        region = dx.get("region") or ""
        modalite = modalite_de(f"{cliche} {m.get('dx') or ''}")
        cote = "normal" if m["id"].startswith("FTE-") else "patho"
        besoins.append({
            "id": m["id"],
            "dx": m.get("dx") or dx.get("dx") or "",
            "cliche": cliche,
            "region": region,
            "niveau": dx.get("niveau") or "CIBLE",
            "modalite": modalite or "AUTRE",
            "plan": plan_de(cliche),
            "cote": cote,
            "queries": m.get("queries") or [],
            "sources": ROUTES.get(modalite or "AUTRE", ROUTES["AUTRE"]),
        })
    besoins.sort(key=lambda b: (0 if b["niveau"] == "MIN" else 1, b["id"]))
    return besoins
