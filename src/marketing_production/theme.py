"""Color theme, chart palette and formatting helpers shared by every
slide deck built with this package.

Two color roles are kept deliberately separate:

- ``BRAND`` -- chrome colors (brand primary + secondary) used for
  backgrounds, headers, buttons and accents. These never encode data.
- ``CATEGORICAL`` -- the data-series palette used by charts. It is a
  four-hue, fixed-order slice of a CVD-validated categorical palette
  (blue, orange, aqua, yellow), so adjacent series in a stacked/area/
  donut chart stay distinguishable under color-vision deficiency. Never
  reassign or reorder these per chart -- the order is the safety
  mechanism.
"""

from __future__ import annotations

from typing import Sequence

# ---------------------------------------------------------------------------
# Brand chrome -- never used to encode data.
# ---------------------------------------------------------------------------
BRAND = {
    "primary": "#754927",
    "secondary": "#703205",
    "secondary_pale": "#F1EAE6",
    "white": "#FFFFFF",
    "page_bg": "#FFFFFF",
    "card_bg": "#FFFFFF",
    "border": "#E5DAD2",
    "disclaimer": "#6B6B6B",
}

# ---------------------------------------------------------------------------
# Chart chrome & ink (light surface only -- this deck is a fixed-design,
# print-oriented document, not a theme-adaptive artifact).
# ---------------------------------------------------------------------------
INK = {
    "surface": "#FCFCFB",
    "primary": "#0B0B0B",
    "secondary": "#52514E",
    "muted": "#898781",
    "gridline": "#E1E0D9",
    "baseline": "#C3C2B7",
}

# ---------------------------------------------------------------------------
# Categorical data palette -- fixed order, validated for CVD separation
# (worst adjacent CVD delta-E 9.1, worst adjacent normal-vision delta-E
# 19.6).
# ---------------------------------------------------------------------------
CATEGORICAL: list[str] = ["#2A78D6", "#EB6834", "#1BAF7A", "#EDA100"]

# Status colors -- reserved meaning, always paired with an icon + label.
STATUS = {
    "good": "#0CA30C",
    "critical": "#D03B3B",
}


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------


def fmt_pct(value: float, decimals: int = 1, signed: bool = False) -> str:
    if value is None or value != value:  # NaN check without importing numpy
        return "n/d"
    sign = "+" if signed and value > 0 else ""
    return f"{sign}{value * 100:.{decimals}f}%".replace(".", ",")


def fmt_eur(value: float, decimals: int = 0) -> str:
    if value is None or value != value:
        return "n/d"
    formatted = f"{value:,.{decimals}f}"
    formatted = formatted.replace(",", " ").replace(".", ",")
    return f"{formatted} €"


def fmt_num(value: float, decimals: int = 2) -> str:
    if value is None or value != value:
        return "n/d"
    return f"{value:.{decimals}f}".replace(".", ",")


def fmt_date_fr(ts) -> str:
    months = [
        "janvier", "février", "mars", "avril", "mai", "juin",
        "juillet", "août", "septembre", "octobre", "novembre", "décembre",
    ]
    return f"{ts.day} {months[ts.month - 1]} {ts.year}"


def status_of(value: float) -> str:
    return "good" if value is not None and value == value and value >= 0 else "critical"


def signed_kpi_value(value: float, decimals: int = 1, is_pct: bool = True) -> str:
    """The KPI's headline figure itself, colored and arrow-prefixed by
    sign (icon + color together, never color alone) -- used instead of
    a separate "delta" line so the number is never printed twice."""
    status = status_of(value)
    arrow = "&#9652;" if status == "good" else "&#9662;"
    text = fmt_pct(value, decimals=decimals, signed=False) if is_pct else fmt_num(value, decimals=decimals)
    return f'<span class="kpi-value kpi-{status}">{arrow} {text}</span>'


def legend_html(items: Sequence[tuple[str, str, str]]) -> str:
    """Render a row of legend swatches. ``items`` is a sequence of
    ``(label, color, value_label)``."""
    rows = []
    for label, color, value_label in items:
        rows.append(
            '<div class="legend-item">'
            f'<span class="legend-swatch" style="background:{color}"></span>'
            f'<span class="legend-label">{label}</span>'
            f'<span class="legend-value">{value_label}</span>'
            "</div>"
        )
    return '<div class="legend">' + "".join(rows) + "</div>"
