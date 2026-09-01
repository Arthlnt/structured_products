import math

from marketing_production.theme import INK


def _polar(cx, cy, r, angle_deg):
    rad = math.radians(angle_deg - 90.0)
    return cx + r * math.cos(rad), cy + r * math.sin(rad)


def _pick_tick_indices(n, n_ticks):
    if n <= 1:
        return [0]
    step = max(1, round((n - 1) / (n_ticks - 1)))
    indices = list(range(0, n, step))
    if indices[-1] != n - 1:
        if len(indices) > 1 and (n - 1 - indices[-1]) < step / 2:
            indices[-1] = n - 1
        else:
            indices.append(n - 1)
    return indices


def donut_svg(
    segments,
    size=260,
    hole_ratio=0.62,
    center_label="",
    center_sublabel="",
):
    total = sum(max(value, 0.0) for _, value, _ in segments)
    cx = cy = size / 2
    outer_r = size / 2 - 4
    inner_r = outer_r * hole_ratio

    parts = [f'<svg viewBox="0 0 {size} {size}" width="{size}" height="{size}" role="img">']
    angle = 0.0
    for label, value, color in segments:
        if total <= 0 or value <= 0:
            continue
        sweep = 360.0 * value / total
        a0, a1 = angle, angle + sweep
        large_arc = 1 if sweep > 180 else 0
        p1 = _polar(cx, cy, outer_r, a0)
        p2 = _polar(cx, cy, outer_r, a1)
        p3 = _polar(cx, cy, inner_r, a1)
        p4 = _polar(cx, cy, inner_r, a0)
        path = (
            f"M {p1[0]:.1f},{p1[1]:.1f} "
            f"A {outer_r:.1f} {outer_r:.1f} 0 {large_arc} 1 {p2[0]:.1f},{p2[1]:.1f} "
            f"L {p3[0]:.1f},{p3[1]:.1f} "
            f"A {inner_r:.1f} {inner_r:.1f} 0 {large_arc} 0 {p4[0]:.1f},{p4[1]:.1f} Z"
        )
        pct = 100.0 * value / total
        parts.append(
            f'<path d="{path}" fill="{color}" stroke="{INK["surface"]}" stroke-width="2">'
            f"<title>{label}: {pct:.1f}%</title></path>"
        )
        if pct >= 6.0:
            mid_r = (outer_r + inner_r) / 2
            lx, ly = _polar(cx, cy, mid_r, (a0 + a1) / 2)
            parts.append(
                f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle" '
                f'dominant-baseline="middle" class="donut-label">{pct:.0f}%</text>'
            )
        angle = a1

    if center_label:
        parts.append(
            f'<text x="{cx}" y="{cy - 4}" text-anchor="middle" class="donut-center-value">{center_label}</text>'
        )
    if center_sublabel:
        parts.append(
            f'<text x="{cx}" y="{cy + 16}" text-anchor="middle" class="donut-center-sub">{center_sublabel}</text>'
        )
    parts.append("</svg>")
    return "".join(parts)


def stacked_area_svg(
    x_labels,
    layers,
    width=760,
    height=280,
    y_ticks=(0.0, 0.25, 0.5, 0.75, 1.0),
    y_fmt=lambda v: f"{v * 100:.0f}%",
    n_x_ticks=6,
):
    left, right, top, bottom = 46, 12, 14, 24
    plot_w = width - left - right
    plot_h = height - top - bottom
    n = len(x_labels)

    def x_of(i):
        return left + (plot_w * i / (n - 1) if n > 1 else plot_w / 2)

    def y_of(v):
        return top + plot_h * (1.0 - v)

    parts = [f'<svg viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img">']

    for tick in y_ticks:
        ty = y_of(tick)
        parts.append(
            f'<line x1="{left}" y1="{ty:.1f}" x2="{width - right}" y2="{ty:.1f}" '
            f'class="gridline" />'
            f'<text x="{left - 8}" y="{ty:.1f}" text-anchor="end" dominant-baseline="middle" '
            f'class="axis-label">{y_fmt(tick)}</text>'
        )

    baseline = [0.0] * n
    for label, color, values in layers:
        new_cum = [baseline[i] + values[i] for i in range(n)]
        bottom_pts = [(x_of(i), y_of(baseline[i])) for i in range(n)]
        top_pts = [(x_of(i), y_of(new_cum[i])) for i in range(n)]
        d = "M " + " L ".join(f"{px:.1f},{py:.1f}" for px, py in bottom_pts)
        d += " L " + " L ".join(f"{px:.1f},{py:.1f}" for px, py in reversed(top_pts)) + " Z"
        latest_pct = values[-1] * 100 if n else 0.0
        parts.append(
            f'<path d="{d}" fill="{color}" fill-opacity="0.88" stroke="{INK["surface"]}" '
            f'stroke-width="1"><title>{label}: {latest_pct:.1f}%</title></path>'
        )
        baseline = new_cum

    for i in _pick_tick_indices(n, n_x_ticks):
        parts.append(
            f'<text x="{x_of(i):.1f}" y="{height - 6}" text-anchor="middle" '
            f'class="axis-label">{x_labels[i]}</text>'
        )

    parts.append(
        f'<line x1="{left}" y1="{top + plot_h}" x2="{width - right}" y2="{top + plot_h}" class="axis-line" />'
    )
    parts.append("</svg>")
    return "".join(parts)


def line_svg(
    x_labels,
    values,
    color,
    width=760,
    height=240,
    y_fmt=lambda v: f"{v:.0f}",
    n_y_ticks=4,
    n_x_ticks=6,
):
    left, right, top, bottom = 46, 12, 20, 24
    plot_w = width - left - right
    plot_h = height - top - bottom
    n = len(values)

    v_min, v_max = min(values), max(values)
    pad = (v_max - v_min) * 0.12 or max(abs(v_max), 1.0) * 0.05
    v_min, v_max = v_min - pad, v_max + pad

    def x_of(i):
        return left + (plot_w * i / (n - 1) if n > 1 else plot_w / 2)

    def y_of(v):
        return top + plot_h * (1.0 - (v - v_min) / (v_max - v_min))

    parts = [f'<svg viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img">']

    for k in range(n_y_ticks + 1):
        tick_v = v_min + (v_max - v_min) * k / n_y_ticks
        ty = y_of(tick_v)
        parts.append(
            f'<line x1="{left}" y1="{ty:.1f}" x2="{width - right}" y2="{ty:.1f}" class="gridline" />'
            f'<text x="{left - 8}" y="{ty:.1f}" text-anchor="end" dominant-baseline="middle" '
            f'class="axis-label">{y_fmt(tick_v)}</text>'
        )

    pts = [(x_of(i), y_of(values[i])) for i in range(n)]
    line_d = "M " + " L ".join(f"{px:.1f},{py:.1f}" for px, py in pts)
    area_d = line_d + f" L {pts[-1][0]:.1f},{top + plot_h:.1f} L {pts[0][0]:.1f},{top + plot_h:.1f} Z"
    parts.append(f'<path d="{area_d}" fill="{color}" fill-opacity="0.12" stroke="none" />')
    parts.append(f'<path d="{line_d}" fill="none" stroke="{color}" stroke-width="2" />')

    for i in _pick_tick_indices(n, n_x_ticks):
        parts.append(
            f'<text x="{x_of(i):.1f}" y="{height - 6}" text-anchor="middle" '
            f'class="axis-label">{x_labels[i]}</text>'
        )

    start_x, start_y = pts[0]
    end_x, end_y = pts[-1]
    parts.append(f'<circle cx="{end_x:.1f}" cy="{end_y:.1f}" r="3.5" fill="{color}">'
                  f"<title>{x_labels[-1]}: {y_fmt(values[-1])}</title></circle>")
    label_dy = -10 if values[-1] >= values[0] else 14
    parts.append(
        f'<text x="{end_x:.1f}" y="{end_y + label_dy:.1f}" text-anchor="end" '
        f'class="line-end-label">{y_fmt(values[-1])}</text>'
    )
    start_dy = 14 if values[-1] >= values[0] else -10
    parts.append(
        f'<text x="{start_x:.1f}" y="{start_y + start_dy:.1f}" text-anchor="start" '
        f'class="line-start-label">{y_fmt(values[0])}</text>'
    )

    parts.append(
        f'<line x1="{left}" y1="{top + plot_h}" x2="{width - right}" y2="{top + plot_h}" class="axis-line" />'
    )
    parts.append("</svg>")
    return "".join(parts)
