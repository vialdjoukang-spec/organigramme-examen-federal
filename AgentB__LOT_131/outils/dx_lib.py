"""Petites fonctions HTML. Le texte clinique vient des modules de contenu."""

def b(fid: str, label: str) -> str:
    return f'<button type="button" class="fen" popovertarget="{fid}">{label}</button>'


def w(fid: str, *paras: str) -> str:
    inner = "".join(f"<p>{p}</p>" for p in paras)
    return (
        f'<div id="{fid}" popover class="fenetre">'
        f'<button type="button" class="fermer" popovertarget="{fid}" popovertargetaction="hide">Fermer ✕</button>'
        f"{inner}</div>"
    )


def ilot(dx: int, n: int, titre: str, inner: str) -> str:
    return (
        f'<section class="ilot" id="dx{dx}-i{n}">'
        f'<h3 id="dx{dx}-p{n}"><strong>{n}. {titre}</strong></h3>'
        f"{inner}</section>"
    )


def tableau(rows: list[tuple[str, ...]]) -> str:
    head, *rest = rows
    th = "".join(f"<th>{c}</th>" for c in head)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rest)
    return f'<div class="defil"><table><tr>{th}</tr>{body}</table></div>'
