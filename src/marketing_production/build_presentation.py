import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from marketing_production import deck
from marketing_production.deck import brand_logo_html, footer_html, image_data_uri, pill_tag_html

PRODUCT_NAME = "Autocall France Juillet 2018"
OUTPUT_PATH = PROJECT_ROOT / "docs & output" / "Autocall_France_Juillet_2018.html"
FOOTER_CLASSIFICATION = "Communication &agrave; caract&egrave;re promotionnel - R&eacute;serv&eacute; aux clients priv&eacute;s"
PRODUCT_TERMS_IMAGE_PATH = PROJECT_ROOT / "src" / "marketing_production" / "assets" / "product_terms_snapshot.png"
PRODUCT_REFERENCE_IMAGE_PATH = PROJECT_ROOT / "src" / "marketing_production" / "assets" / "product_reference_snapshot.png"
PRODUCT_DATES_IMAGE_PATH = PROJECT_ROOT / "src" / "marketing_production" / "assets" / "product_dates_snapshot.png"
UNDERLYING_PERFORMANCE_IMAGE_PATH = PROJECT_ROOT / "src" / "marketing_production" / "assets" / "underlying_performance_snapshot.png"
DRAWDOWN_IMAGE_PATH = PROJECT_ROOT / "src" / "marketing_production" / "assets" / "drawdown_snapshot.png"
UNDERLYING_SNAPSHOT_IMAGE_PATH = PROJECT_ROOT / "src" / "marketing_production" / "assets" / "underlying_snapshot.png"
AUTOCALL_SNAPSHOT_IMAGE_PATH = PROJECT_ROOT / "src" / "marketing_production" / "assets" / "autocall_snapshot.png"
CAPITAL_BARRIER_SNAPSHOT_IMAGE_PATH = PROJECT_ROOT / "src" / "marketing_production" / "assets" / "capital_barrier_snapshot.png"
AUTOCALL_MONITORING_IMAGE_PATH = PROJECT_ROOT / "src" / "marketing_production" / "assets" / "autocall_monitoring_snapshot.png"


def _footer_html(page_number):
    return footer_html(page_number, FOOTER_CLASSIFICATION)


def _build_cover_slide():
    return f"""
<section class="slide slide-reference-cover active">
  <div class="reference-frame"></div>
  <div class="reference-logo-plate">
    {brand_logo_html("lg")}
  </div>
  <p class="cover-kicker">Produit Structur&eacute; &middot; EMTN</p>
  <h1 class="reference-title">{PRODUCT_NAME}</h1>
  <div class="cover-rule"></div>
</section>
"""


def _build_section_slide(number, title, page_number, title_style=""):
    style_attr = f' style="{title_style}"' if title_style else ""
    return f"""
<section class="slide slide-reference-section">
  <div class="section-frame"></div>
  <div class="section-number">{number}</div>
  <div class="section-divider"></div>
  <h2 class="section-title"{style_attr}>{title}</h2>
  <div class="reference-footer">
    <span class="reference-footer-page">{page_number}</span>
    <span class="reference-footer-rule">|</span>
    <span>{FOOTER_CLASSIFICATION}</span>
  </div>
  <div class="reference-footer-logo">{brand_logo_html("sm")}</div>
</section>
"""


def _build_product_terms_slide(page_number):
    product_terms_image_src = image_data_uri(PRODUCT_TERMS_IMAGE_PATH)
    product_reference_image_src = image_data_uri(PRODUCT_REFERENCE_IMAGE_PATH)
    return f"""
<section class="slide slide-content">
  <div class="content-topbar">{pill_tag_html("01 &mdash; Termes du produit")}</div>
  <h2 class="content-title">Caract&eacute;ristiques de l'&eacute;mission et du sous-jacent</h2>
  <p class="content-subtitle">Autocall &ndash; BNP Paribas Issuance B.V. &ndash; Solactive France 40 Equal Weight NTR 5% AR</p>
  <div class="slide-body stacked">
    <div class="product-terms-figure">
      <div class="product-terms-image-row">
        <img class="product-terms-image" src="{product_terms_image_src}" alt="Product Terms">
      </div>
      <div class="product-terms-image-row">
        <img class="product-terms-image" src="{product_reference_image_src}" alt="Product Reference and Underlying">
      </div>
    </div>
  </div>
  {_footer_html(page_number)}
</section>
"""


def _build_underlying_performance_slide(page_number):
    underlying_performance_image_src = image_data_uri(UNDERLYING_PERFORMANCE_IMAGE_PATH)
    return f"""
<section class="slide slide-content">
  <div class="content-topbar">{pill_tag_html("04 &mdash; Performance du sous-jacent")}</div>
  <h2 class="content-title">Performance historique du sous-jacent</h2>
  <p class="content-subtitle">Solactive France 40 Equal Weight NTR 5% AR &middot; depuis le 2 juillet 2018</p>
  <div class="slide-body stacked">
    <img src="{underlying_performance_image_src}" alt="Performance base 100 du sous-jacent" style="display: block; margin: 0 auto; max-width: 100%; max-height: 540px; width: auto; height: auto;">
  </div>
  {_footer_html(page_number)}
</section>
"""


def _build_product_dates_slide(page_number):
    product_dates_image_src = image_data_uri(PRODUCT_DATES_IMAGE_PATH)
    return f"""
<section class="slide slide-content">
  <div class="content-topbar">{pill_tag_html("02 &mdash; Constatation &amp; Remboursement")}</div>
  <h2 class="content-title">Dates de constatation et niveaux de remboursement</h2>
  <div class="slide-body stacked">
    <div class="panel-grid" style="grid-template-columns: 1.55fr 0.85fr; align-items: start;">
      <img class="product-terms-image" src="{product_dates_image_src}" alt="Product Dates and Levels" style="display: block; width: 100%; height: auto; margin-top: 20px;">
      <div class="panel">
        <p class="panel-lead">Montant de remboursement anticip&eacute; automatique</p>
        <p class="panel-copy">Si, &agrave; l'une des dates d'&eacute;valuation, l'Indice cl&ocirc;ture &agrave; un niveau sup&eacute;rieur ou &eacute;gal au niveau de remboursement anticip&eacute;, l'&Eacute;metteur rembourse automatiquement chaque EMTN selon la formule suivante :</p>
        <div class="fact-item">
          <span class="fact-value">D &times; [103,50% + n &times; 3,50%]</span>
        </div>
        <p class="panel-note">avec n = 1, 2, &hellip;, 18</p>
      </div>
    </div>
  </div>
  {_footer_html(page_number)}
</section>
"""


def _build_final_redemption_scenarios_slide(page_number):
    return f"""
<section class="slide slide-content">
  <div class="content-topbar">{pill_tag_html("03 &mdash; Sc&eacute;narios de Remboursement Final")}</div>
  <h2 class="content-title">Trois sc&eacute;narios possibles &agrave; la date de remboursement final</h2>
  <div class="slide-body stacked">
    <div class="panel-grid" style="grid-template-columns: 1fr 1fr 1fr; align-items: stretch;">
      <div class="panel" style="display: flex; flex-direction: column; min-height: 260px;">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
          <span class="bullet-num">1</span>
          <span class="panel-lead" style="margin: 0; font-size: 14.5px;">Indice Final &ge; 80% &times; Indice Initial</span>
        </div>
        <p class="panel-copy">Remboursement de la valeur nominale et d'une prime &eacute;gale &agrave; 20 coupons de 3,50%, soit 70% de la valeur nominale.</p>
        <div class="fact-item" style="margin-top: auto;">
          <span class="fact-label">Formule</span>
          <span class="fact-value">D &times; 170%</span>
        </div>
      </div>
      <div class="panel" style="display: flex; flex-direction: column; min-height: 260px;">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
          <span class="bullet-num">2</span>
          <span class="panel-lead" style="margin: 0; font-size: 14.5px;">60% &le; Indice Final &lt; 80%</span>
        </div>
        <p class="panel-copy">Barri&egrave;re de protection du capital non franchie : remboursement int&eacute;gral de la valeur nominale, sans prime.</p>
        <div class="fact-item" style="margin-top: auto;">
          <span class="fact-label">Formule</span>
          <span class="fact-value">D &times; 100%</span>
        </div>
      </div>
      <div class="panel" style="display: flex; flex-direction: column; min-height: 260px;">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
          <span class="bullet-num">3</span>
          <span class="panel-lead" style="margin: 0; font-size: 14.5px;">Indice Final &lt; 60% &times; Indice Initial</span>
        </div>
        <p class="panel-copy">Barri&egrave;re de protection du capital franchie : perte en capital partielle, voire totale si l'Indice a diminu&eacute; de l'int&eacute;gralit&eacute; de sa valeur initiale.</p>
        <div class="fact-item" style="margin-top: auto;">
          <span class="fact-label">Formule</span>
          <span class="fact-value">N &times; (Indice Final / Indice Initial)</span>
        </div>
      </div>
    </div>
    <p class="panel-note" style="margin-top: 20px; display: grid; grid-template-columns: max-content 1fr; column-gap: 4px; row-gap: 2px;">
      <span>Avec</span>
      <span>Indice Initial : niveau de cl&ocirc;ture officiel de l'Indice &agrave; la Date de Constatation Initiale</span>
      <span></span>
      <span>Indice Final : niveau de cl&ocirc;ture officiel de l'Indice &agrave; la Date de Constatation Finale.</span>
    </p>
  </div>
  {_footer_html(page_number)}
</section>
"""


def _build_risk_snapshot_slide(page_number):
    drawdown_image_src = image_data_uri(DRAWDOWN_IMAGE_PATH)
    underlying_snapshot_image_src = image_data_uri(UNDERLYING_SNAPSHOT_IMAGE_PATH)
    return f"""
<section class="slide slide-content">
  <div class="content-topbar">{pill_tag_html("05 &mdash; Position, Performance &amp; Risque")}</div>
  <h2 class="content-title">Suivi du risque et indicateurs cl&eacute;s du sous-jacent</h2>
  <p class="content-subtitle">reporting au 24 ao&ucirc;t 2026</p>
  <div class="slide-body stacked">
    <div style="display: flex; flex-direction: column; align-items: center; gap: 0;">
      <img src="{drawdown_image_src}" alt="Drawdown du sous-jacent" style="display: block; margin: 0 auto; width: auto; height: auto; max-width: 100%; max-height: 350px;">
      <img src="{underlying_snapshot_image_src}" alt="Sous-Jacent Snapshot" style="display: block; margin: -58px auto 0; width: auto; height: auto; max-width: 100%; max-height: 160px;">
    </div>
  </div>
  {_footer_html(page_number)}
</section>
"""


def _build_autocall_barrier_snapshot_slide(page_number):
    autocall_snapshot_image_src = image_data_uri(AUTOCALL_SNAPSHOT_IMAGE_PATH)
    capital_barrier_snapshot_image_src = image_data_uri(CAPITAL_BARRIER_SNAPSHOT_IMAGE_PATH)
    return f"""
<section class="slide slide-content">
  <div class="content-topbar">{pill_tag_html("06 &mdash; Position, Performance &amp; Risque")}</div>
  <h2 class="content-title">Positionnement vis-&agrave;-vis des barri&egrave;res de remboursement</h2>
  <p class="content-subtitle">reporting au 24 ao&ucirc;t 2026</p>
  <div class="slide-body stacked">
    <div class="panel-grid" style="align-items: start;">
      <img src="{autocall_snapshot_image_src}" alt="Autocall Snapshot" style="display: block; width: 100%; height: auto;">
      <img src="{capital_barrier_snapshot_image_src}" alt="Capital Barrier Snapshot" style="display: block; width: 100%; height: auto;">
    </div>
  </div>
  {_footer_html(page_number)}
</section>
"""


def _build_autocall_monitoring_slide(page_number):
    autocall_monitoring_image_src = image_data_uri(AUTOCALL_MONITORING_IMAGE_PATH)
    return f"""
<section class="slide slide-content">
  <div class="content-topbar">{pill_tag_html("07 &mdash; Suivi de l'Autocall")}</div>
  <h2 class="content-title">Suivi des dates de constatation et du r&eacute;sultat Autocall</h2>
  <p class="content-subtitle">reporting au 24 ao&ucirc;t 2026</p>
  <div class="slide-body stacked">
    <img src="{autocall_monitoring_image_src}" alt="Autocall Monitoring" style="display: block; margin: 0 auto; max-width: 100%; max-height: 500px; width: auto; height: auto;">
  </div>
  {_footer_html(page_number)}
</section>
"""


def generate(output_path=None, overwrite=True):
    out_path = Path(output_path) if output_path is not None else OUTPUT_PATH

    if out_path.exists() and not overwrite:
        print(f"{out_path} existe deja -- non regenere (passer overwrite=True pour forcer).")
        return out_path

    out_path.parent.mkdir(parents=True, exist_ok=True)

    slides = [
        _build_cover_slide(),
        _build_section_slide(1, "Termes du produit", page_number=2),
        _build_product_terms_slide(page_number=3),
        _build_product_dates_slide(page_number=4),
        _build_section_slide(
            2, "Sc&eacute;narios de remboursement final", page_number=5,
            title_style="font-size: 52px; line-height: 1.15; top: 276px;",
        ),
        _build_final_redemption_scenarios_slide(page_number=6),
        _build_section_slide(
            3, "Position, Performance &amp; Risque", page_number=7,
            title_style="font-size: 52px; line-height: 1.15; top: 276px;",
        ),
        _build_underlying_performance_slide(page_number=8),
        _build_risk_snapshot_slide(page_number=9),
        _build_autocall_barrier_snapshot_slide(page_number=10),
        _build_section_slide(4, "Suivi de l'Autocall", page_number=11),
        _build_autocall_monitoring_slide(page_number=12),
    ]
    html = deck.build_deck_html(PRODUCT_NAME, slides)

    out_path.write_text(html, encoding="utf-8")
    return out_path


def _parse_args():
    parser = argparse.ArgumentParser(description=f"Build the {PRODUCT_NAME} HTML presentation.")
    parser.add_argument("--output-path", type=str, default=None)
    parser.add_argument("--no-overwrite", action="store_true", help="Leave an existing HTML file untouched.")
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    written_path = generate(output_path=args.output_path, overwrite=not args.no_overwrite)
    print(f"Presentation ecrite dans {written_path}")
