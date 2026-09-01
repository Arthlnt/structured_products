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

INK = {
    "surface": "#FCFCFB",
    "primary": "#0B0B0B",
    "secondary": "#52514E",
    "muted": "#898781",
    "gridline": "#E1E0D9",
    "baseline": "#C3C2B7",
}

CATEGORICAL = ["#2A78D6", "#EB6834", "#1BAF7A", "#EDA100"]

STATUS = {
    "good": "#0CA30C",
    "critical": "#D03B3B",
}


def fmt_pct(value, decimals=1, signed=False):
    if value is None or value != value:
        return "n/d"
    sign = "+" if signed and value > 0 else ""
    return f"{sign}{value * 100:.{decimals}f}%".replace(".", ",")


def fmt_eur(value, decimals=0):
    if value is None or value != value:
        return "n/d"
    formatted = f"{value:,.{decimals}f}"
    formatted = formatted.replace(",", " ").replace(".", ",")
    return f"{formatted} €"


def fmt_num(value, decimals=2):
    if value is None or value != value:
        return "n/d"
    return f"{value:.{decimals}f}".replace(".", ",")


def fmt_date_fr(ts):
    months = [
        "janvier", "février", "mars", "avril", "mai", "juin",
        "juillet", "août", "septembre", "octobre", "novembre", "décembre",
    ]
    return f"{ts.day} {months[ts.month - 1]} {ts.year}"


def status_of(value):
    return "good" if value is not None and value == value and value >= 0 else "critical"


def signed_kpi_value(value, decimals=1, is_pct=True):
    status = status_of(value)
    arrow = "&#9652;" if status == "good" else "&#9662;"
    text = fmt_pct(value, decimals=decimals, signed=False) if is_pct else fmt_num(value, decimals=decimals)
    return f'<span class="kpi-value kpi-{status}">{arrow} {text}</span>'


def legend_html(items):
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
