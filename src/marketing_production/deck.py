import base64
from pathlib import Path

from marketing_production.theme import BRAND, INK

SLIDE_W = 1280
SLIDE_H = 720

PROJECT_ROOT = Path(__file__).resolve().parents[2]
LOGO_PATH = PROJECT_ROOT / "logo-transparent.png"


def _logo_data_uri():
    if not LOGO_PATH.exists():
        return ""
    encoded = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def image_data_uri(image_path):
    path = Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"Image introuvable: {path}")
    mime_type = "image/png" if path.suffix.lower() == ".png" else "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def brand_logo_html(size="lg"):
    cls = "brand-logo brand-logo-lg" if size == "lg" else "brand-logo brand-logo-sm"
    return f'<div class="{cls}" role="img" aria-label="Logo"></div>'


def pill_tag_html(text):
    return f'<span class="pill-tag">{text}</span>'


def footer_html(page_number, classification=""):
    return (
        '<div class="reference-footer">'
        f'<span class="reference-footer-page">{page_number}</span>'
        '<span class="reference-footer-rule">|</span>'
        f"<span>{classification}</span>"
        "</div>"
        f'<div class="reference-footer-logo">{brand_logo_html("sm")}</div>'
    )


def _css():
    return f"""
* {{ box-sizing: border-box; }}
html, body {{
  margin: 0; padding: 0; min-height: 100%;
  background: #1b1e24;
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  color: {INK["primary"]};
  overflow: auto;
}}
body {{
  padding: 28px 0;
}}
.deck-toolbar {{
  position: fixed; top: 18px; right: 18px; z-index: 20;
  display: flex; align-items: center; gap: 8px;
}}
.deck-toolbar button {{
  border: 1px solid {BRAND["secondary"]}; border-radius: 4px;
  padding: 10px 12px; font-size: 13px; font-weight: 750;
  font-family: inherit; box-shadow: 0 10px 24px rgba(0,0,0,0.22);
  background: {BRAND["primary"]}; color: {BRAND["white"]}; cursor: pointer;
}}
.deck-toolbar button:hover {{ background: {BRAND["secondary"]}; }}
.deck {{
  width: {SLIDE_W}px; margin: 0 auto;
  display: flex; flex-direction: column; gap: 28px;
}}
.slide {{
  position: relative;
  width: {SLIDE_W}px; height: {SLIDE_H}px;
  min-width: {SLIDE_W}px; max-width: {SLIDE_W}px;
  min-height: {SLIDE_H}px; max-height: {SLIDE_H}px;
  flex: 0 0 {SLIDE_H}px;
  display: flex; flex-direction: column;
  background: {BRAND["card_bg"]};
  box-shadow: 0 24px 70px rgba(0,0,0,0.35);
  overflow: hidden;
}}
.slide.active {{ display: flex; }}

.brand-logo {{
  background: url("{_logo_data_uri()}") center / contain no-repeat;
}}
.brand-logo-lg {{ width: 320px; height: 104px; }}
.brand-logo-sm {{ width: 96px; height: 40px; }}

.slide-reference-cover,
.slide-reference-section {{ background: {BRAND["white"]}; position: relative; }}

.reference-frame {{
  position: absolute; left: 44px; right: 44px; top: 101px; bottom: 44px;
  border: 4px solid {BRAND["secondary"]};
}}

.reference-logo-plate {{
  position: absolute; top: 150px; left: 0; right: 0; height: 104px;
  display: flex; align-items: center; justify-content: center;
}}
.cover-kicker {{
  position: absolute; left: 137px; right: 137px; top: 312px;
  margin: 0; text-align: center; text-transform: uppercase; letter-spacing: 5px;
  font-size: 13px; font-weight: 750; color: {BRAND["secondary"]}; opacity: 0.72;
}}
.reference-title {{
  position: absolute; left: 137px; right: 137px; top: 355px;
  margin: 0; font-size: 76px; font-weight: 850; line-height: 1.05;
  letter-spacing: -0.5px; text-align: center; color: {BRAND["secondary"]};
}}
.cover-rule {{
  position: absolute; left: 50%; top: 465px; transform: translateX(-50%);
  width: 140px; height: 3px; border-radius: 2px;
  background: linear-gradient(90deg, transparent, {BRAND["secondary"]}, transparent);
  opacity: 0.65;
}}
.section-frame {{
  position: absolute; left: 51px; right: 42px; top: 134px; height: 407px;
  border: 4px solid {BRAND["secondary"]};
}}
.section-number {{
  position: absolute; left: 176px; top: 255px;
  color: {BRAND["secondary"]}; font-size: 166px; font-weight: 800; line-height: 1;
}}
.section-divider {{
  position: absolute; left: 366px; top: 248px;
  width: 10px; height: 173px; background: {BRAND["secondary"]};
}}
.section-title {{
  position: absolute; left: 430px; right: 92px; top: 292px;
  margin: 0; color: {BRAND["primary"]}; font-size: 76px; font-weight: 850;
  line-height: 1.02; letter-spacing: 0; text-align: center;
}}
.section-subtitle {{
  position: absolute; left: 443px; right: 86px; top: 404px;
  margin: 0; color: {BRAND["secondary"]}; font-size: 25px; font-weight: 650;
  line-height: 1.18;
}}
.reference-footer {{
  position: absolute; left: 56px; bottom: 27px;
  color: {BRAND["primary"]}; font-size: 12px; font-weight: 650;
}}
.reference-footer-page {{ margin-right: 15px; }}
.reference-footer-rule {{ margin: 0 13px 0 0; }}
.reference-footer-logo {{ position: absolute; right: 56px; bottom: 20px; }}

.slide-content {{ background: {BRAND["page_bg"]}; padding: 34px 64px 0; }}
.product-terms-figure {{
  display: flex; flex-direction: column; align-items: center; gap: 16px;
}}
.product-terms-image-row {{
  width: 100%; display: flex; justify-content: center;
}}
.product-terms-image {{
  display: block; width: 880px; max-width: 100%; height: auto;
}}
.content-topbar {{ display: flex; justify-content: flex-end; }}
.pill-tag {{
  background: {BRAND["secondary_pale"]}; color: {BRAND["primary"]}; font-size: 11px; font-weight: 700;
  letter-spacing: 0.5px; text-transform: uppercase; padding: 6px 14px; border-radius: 3px;
}}
.content-title {{ margin: 14px 0 0; font-size: 26px; font-weight: 800; color: {BRAND["primary"]}; }}
.content-subtitle {{ margin: 5px 0 0; font-size: 14.5px; font-weight: 700; color: {BRAND["secondary"]}; }}
.slide-body {{ flex: 1; padding: 18px 0 14px; display: flex; gap: 24px; min-height: 0; }}
.slide-body.stacked {{ display: block; padding-top: 24px; }}

.panel-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 24px; flex: 1; min-height: 0; }}
.panel {{
  border: 1px solid {BRAND["border"]}; border-top: 3px solid {BRAND["secondary"]};
  border-radius: 6px; padding: 20px 24px; background: {BRAND["card_bg"]};
}}
.panel-lead {{ margin: 0 0 15px; color: {BRAND["primary"]}; font-size: 20px; line-height: 1.28; font-weight: 850; }}
.panel-copy {{ margin: 0 0 12px; color: {INK["secondary"]}; font-size: 13.3px; line-height: 1.48; }}
.panel-copy b {{ color: {BRAND["primary"]}; }}
.panel-note {{ margin-top: 14px; color: {INK["secondary"]}; font-size: 12.5px; line-height: 1.45; }}

.facts-grid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; margin: 16px 0 14px; }}
.fact-item {{
  min-height: 76px; border-left: 3px solid {BRAND["secondary"]}; background: {BRAND["secondary_pale"]};
  padding: 12px 14px; display: flex; flex-direction: column; justify-content: center;
}}
.fact-label {{ color: {INK["muted"]}; font-size: 10.5px; font-weight: 750; letter-spacing: 0.45px; text-transform: uppercase; }}
.fact-value {{ margin-top: 6px; color: {BRAND["primary"]}; font-size: 18px; font-weight: 850; line-height: 1.12; }}

.bullet-list {{ margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 10px; }}
.bullet-list li {{ display: grid; grid-template-columns: 9px 1fr; gap: 10px; color: {INK["secondary"]}; font-size: 13px; line-height: 1.42; }}
.bullet-list b {{ color: {BRAND["primary"]}; }}
.bullet-dot {{ width: 9px; height: 9px; margin-top: 5px; background: {BRAND["secondary"]}; border-radius: 2px; }}
.bullet-list.numbered li {{ grid-template-columns: 26px 1fr; gap: 10px; }}
.bullet-num {{
  width: 26px; height: 26px; display: inline-flex; align-items: center; justify-content: center;
  background: {BRAND["secondary_pale"]}; color: {BRAND["primary"]}; border-radius: 3px; font-weight: 850; font-size: 12px;
}}

.info-table {{ width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px; color: {INK["primary"]}; }}
.info-table th {{
  text-align: left; background: {BRAND["secondary_pale"]}; color: {BRAND["primary"]};
  font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px;
  padding: 11px 12px; border-bottom: 2px solid {BRAND["secondary"]};
}}
.info-table td {{ padding: 16px 12px; border-bottom: 1px solid {BRAND["border"]}; vertical-align: top; line-height: 1.35; }}
.info-note {{ margin-top: 14px; font-size: 12px; color: {INK["muted"]}; line-height: 1.4; }}

.card {{
  background: {BRAND["card_bg"]}; border-radius: 6px; border: 1px solid {BRAND["border"]};
  padding: 16px 20px; box-shadow: 0 1px 3px rgba(10,34,64,0.05);
}}
.card h3 {{
  margin: 0 0 14px; font-size: 13.5px; font-weight: 800; color: {BRAND["primary"]};
  text-transform: uppercase; letter-spacing: 0.5px; padding-bottom: 8px;
  border-bottom: 2px solid {BRAND["secondary"]}; display: inline-block;
}}
.col {{ display: flex; flex-direction: column; gap: 16px; min-height: 0; }}
.card svg {{ max-width: 100%; height: auto; display: block; }}

.method-list {{ margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 12px; }}
.method-list li {{ display: flex; gap: 10px; font-size: 14px; line-height: 1.45; color: {INK["secondary"]}; }}
.method-list .bullet {{ color: {BRAND["secondary"]}; font-weight: 800; }}
.method-list b {{ color: {INK["primary"]}; }}

.legend {{ display: flex; flex-wrap: wrap; gap: 6px 18px; margin-top: 10px; }}
.legend-item {{ display: flex; align-items: center; gap: 7px; font-size: 12.5px; color: {INK["secondary"]}; }}
.legend-swatch {{ width: 10px; height: 10px; border-radius: 2px; flex: none; }}
.legend-value {{ font-weight: 700; color: {INK["primary"]}; margin-left: 2px; }}

.gridline {{ stroke: {INK["gridline"]}; stroke-width: 1; }}
.axis-line {{ stroke: {INK["baseline"]}; stroke-width: 1; }}
.axis-label {{ fill: {INK["muted"]}; font-size: 10.5px; }}
.donut-label {{ fill: {BRAND["white"]}; font-size: 12px; font-weight: 700; }}
.donut-center-value {{ fill: {INK["primary"]}; font-size: 22px; font-weight: 800; }}
.donut-center-sub {{ fill: {INK["muted"]}; font-size: 11px; }}
.line-end-label {{ fill: {INK["primary"]}; font-size: 12px; font-weight: 800; }}
.line-start-label {{ fill: {INK["muted"]}; font-size: 11px; font-weight: 600; }}

.kpi-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }}
.kpi-tile {{
  background: {BRAND["card_bg"]}; border: 1px solid {BRAND["border"]}; border-top: 3px solid {BRAND["secondary"]};
  border-radius: 6px; padding: 13px 15px; display: flex; flex-direction: column; gap: 6px;
}}
.kpi-label {{ font-size: 11px; color: {INK["muted"]}; text-transform: uppercase; letter-spacing: 0.4px; font-weight: 700; }}
.kpi-value {{ font-size: 21px; font-weight: 800; color: {INK["primary"]}; }}
.kpi-value.kpi-good {{ color: #0CA30C; }}
.kpi-value.kpi-critical {{ color: #D03B3B; }}

.mini-table {{ width: 100%; border-collapse: collapse; font-size: 12.5px; }}
.mini-table th {{
  text-align: left; color: {INK["muted"]}; font-weight: 700; text-transform: uppercase;
  font-size: 10.5px; letter-spacing: 0.4px; padding: 4px 8px; border-bottom: 1px solid {BRAND["border"]};
}}
.mini-table td {{ padding: 5px 8px; border-bottom: 1px solid {BRAND["border"]}; color: {INK["secondary"]}; }}
.mini-table td.num {{ text-align: right; font-variant-numeric: tabular-nums; color: {INK["primary"]}; font-weight: 600; }}

.placeholder-note {{
  color: {INK["muted"]}; font-style: italic; font-size: 13px;
}}

@media print {{
  html, body {{
    width: auto; margin: 0; padding: 0; background: #fff; overflow: visible;
    -webkit-print-color-adjust: exact; print-color-adjust: exact;
  }}
  .deck-toolbar {{ display: none; }}
  .deck {{ display: block; width: auto; height: auto; margin: 0; gap: 0; }}
  .slide {{
    display: flex !important; position: relative;
    width: {SLIDE_W}px; height: {SLIDE_H}px; margin: 0; box-shadow: none;
    page-break-after: always; break-after: page;
    page-break-inside: avoid; break-inside: avoid;
  }}
  .slide:last-of-type {{ page-break-after: auto; break-after: auto; }}
  @page {{ size: {SLIDE_W}px {SLIDE_H}px; margin: 0; }}
}}
"""


def _toolbar_html():
    return (
        '<div class="deck-toolbar">'
        '<button id="pdf-export-button" class="pdf-export-button" type="button" '
        'aria-label="Exporter la presentation en PDF">Exporter PDF</button>'
        "</div>"
    )


def _pdf_export_script_html(document_title):
    safe_filename = "".join(ch if ch.isalnum() or ch in ("-", "_") else "_" for ch in document_title).strip("_")
    return f"""
<script>
(function () {{
  const exportButton = document.getElementById("pdf-export-button");
  const pdfBaseName = "{safe_filename or 'presentation'}";

  function exportSlidesAsPdf() {{
    window.print();
  }}

  exportButton.addEventListener("click", exportSlidesAsPdf);
}}());
</script>
"""


def build_deck_html(document_title, slides):
    slides_html = "\n".join(slides)
    toolbar_html = _toolbar_html()
    pdf_export_script_html = _pdf_export_script_html(document_title)
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{document_title}</title>
<style>{_css()}</style>
</head>
<body>
{toolbar_html}
<div class="deck" id="deck">
{slides_html}
</div>
{pdf_export_script_html}
</body>
</html>
"""
