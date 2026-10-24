import json, sys, tempfile
from pathlib import Path
ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent)); sys.path.insert(0, str(ICI))
PROMPT = "/workspace/v7_tunder/PROMPT_ULTIME_PRODUCTION_LOTS_V7-Tunder.md"

def config_temp(racine, agent=1, **extra):
    racine = Path(racine)
    c = {"agent": agent, "lot_min": 227 if agent == 1 else 238, "lot_max": 237 if agent == 1 else 248,
         "cache_dir": str(racine / f"a{agent}" / "cache"), "output_dir": str(racine / f"a{agent}" / "retours"),
         "shared_state_dir": str(racine / "partage"), "prompt_path": PROMPT,
         "compteur": {"csv": str(racine / f"a{agent}" / "compteur.csv")}}
    c.update(extra)
    p = racine / f"config_{agent}.json"; p.write_text(json.dumps(c)); return p
