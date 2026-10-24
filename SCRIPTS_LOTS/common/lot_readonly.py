"""Accès STRICTEMENT EN LECTURE SEULE aux fichiers de LOT.
Seul module autorisé à toucher un fichier de LOT ; il n'ouvre qu'en O_RDONLY.
Toute écriture des scripts passe par ecrire_sortie(), qui refuse tout chemin situé dans un dossier de LOT."""
import hashlib, os, re
from pathlib import Path

class ViolationLectureSeule(Exception):
    """Levée dès qu'une opération risque de modifier un LOT."""

RE_LOT = re.compile(r"LOT_(\d{3})")

def numero_lot(chemin):
    m = RE_LOT.search(Path(chemin).name) or RE_LOT.search(str(Path(chemin).parent))
    return int(m.group(1)) if m else None

def lire_octets(chemin):
    fd = os.open(str(chemin), os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
    try:
        morceaux = []
        while True:
            b = os.read(fd, 1 << 20)
            if not b:
                break
            morceaux.append(b)
        return b"".join(morceaux)
    finally:
        os.close(fd)

def ouvrir_lecture(chemin):
    """Descripteur en lecture seule (utilisé par les tests pour prouver qu'aucune écriture n'est possible)."""
    return os.open(str(chemin), os.O_RDONLY)

def empreintes(dossier):
    res = {}
    for p in sorted(Path(dossier).rglob("*")):
        if p.is_file() and not p.is_symlink():
            res[str(p.relative_to(dossier))] = hashlib.sha256(lire_octets(p)).hexdigest()
    return res

def _dedans(enfant, parent):
    enfant, parent = os.path.realpath(enfant), os.path.realpath(parent)
    return os.path.commonpath([enfant, parent]) == parent

def verifier_isolation(dossier_sortie, dossiers_lot):
    """Refuse de fonctionner si la sortie est dans un dossier de LOT, ou un dossier de LOT dans la sortie."""
    for d in dossiers_lot:
        if d and (_dedans(dossier_sortie, d) or _dedans(d, dossier_sortie)):
            raise ViolationLectureSeule(f"dossier de sortie {dossier_sortie} non isolé du dossier de LOT {d}")

def verifier_droits_os(dossier_lot):
    """Mode strict : le processus ne doit avoir AUCUN droit d'écriture sur le dossier du LOT."""
    if os.access(dossier_lot, os.W_OK):
        raise ViolationLectureSeule(f"le processus peut écrire dans {dossier_lot} : lancez-le sous l'utilisateur relecteur (droits en lecture seule)")

def ecrire_sortie(chemin, contenu, dossier_sortie, dossiers_lot):
    chemin = Path(chemin)
    if not _dedans(chemin, dossier_sortie):
        raise ViolationLectureSeule(f"écriture hors du dossier de sortie refusée : {chemin}")
    for d in dossiers_lot:
        if d and _dedans(chemin, d):
            raise ViolationLectureSeule(f"écriture dans un dossier de LOT refusée : {chemin}")
    chemin.parent.mkdir(parents=True, exist_ok=True)
    tmp = chemin.with_name(chemin.name + ".tmp")
    tmp.write_text(contenu, "utf-8"); os.replace(tmp, chemin)
