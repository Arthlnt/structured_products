# Autocall France Juillet 2018

Chaîne de production (calcul, reporting et présentation marketing) **Autocall France Juillet 2018**. Les données historiques sont fictives. Ce projet vise à démontrer la construction de slides automatisés avec mise à jour des données sur le produit. Visualisation de la présentation en format .HTML et en .PDF apprès exportation.

## Structure du dépôt

```
structured_products/
├── data/
│   └── reporting.xlsx                  # Base de données Excel
├── notebooks/
│   ├── 0_evaluation_date_calendar.ipynb    # Calendrier de constatation
│   ├── 01_reporting_database.ipynb         # Indicateurs de suivi (sous-jacent, autocall, protection)
│   ├── 02_reporting_elements.ipynb         # Graphiques et tableaux de reporting (PNG)
│   └── 03_marketing_production.ipynb       # Génération de la présentation finale
├── src/marketing_production/
│   ├── 0_product_terms_instrument.ipynb    # Tableaux des termes du produit (termsheet)
│   ├── theme.py                            # charte graphique (couleurs, formats)
│   ├── deck.py                             # structure HTML/CSS commune des slides
│   ├── charts.py                           # graphiques SVG inline (non utilisés par défaut)
│   ├── build_presentation.py               # assemblage des 12 slides et écriture du HTML final
│   └── assets/                             # images PNG générées (graphiques + tableaux)
├── docs & output/
│   ├── Autocall_France_Juillet_2018.html   # Présentation finale HMTL
│   ├── logo-transparent.png / logo.png     # Logo de la société
│   └── tsheet.pdf                          # Term sheet du produit
│   └── Autocall_France_Juillet_2018.pdf    # Export présentation en PDF
└── README.md
```

## Chaîne de traitement

Les notebooks sont numérotés dans leur ordre d'exécution ; chaque étape lit/écrit dans `data/reporting.xlsx` :

1. **`notebooks/0_evaluation_date_calendar.ipynb`** — Concevoir la table des dates de constatation et de remboursement anticipé (minimum un an après l'émission, fréquence semestrielle).
   - Le résultat est écrit dans l'excel reporting.xlsx page `Calendar`.
2. **`notebooks/01_reporting_database.ipynb`** — Calculer à partir de la timesérie du sous-jacent l'ensemble des indicateurs de suivi du produit:
   - **Sous-jacent** : base 100, performance, drawdown, volatilité depuis l'émission, niveaux min/max ;
   - **Autocall** : niveau et distance de déclenchement, prochaine date d'observation, montant et coupon potentiels ;
   - **Protection** : niveau et distance de la barrière de capital, niveau de protection du nominal.
   - Le résultat est écrit dans l'excel reporting.xlsx page `Reporting`.
3. **`notebooks/02_reporting_elements.ipynb`** — Construire les graphiques (performance base 100 et drawdown du sous-jacent) et les tableaux de synthèse (sous-jacent, autocall, barrière de capital, suivi de l'autocall), puis exporter les images PNG dans `src/marketing_production/assets/`.
4. **`src/marketing_production/0_product_terms_instrument.ipynb`** — Génèrer les tableaux statiques des termes du produit (émetteur, garant, sous-jacent, dates, niveaux de remboursement) issus de la termsheet, sous forme d'images PNG.
5. **`notebooks/03_marketing_production.ipynb`** — Générer la présentation marketing avec mise à jour des tableaux / graphiques de reporting selon la date de reporting.

## Génération de la présentation

Pipeline complet, depuis la racine du projet :

```bash
jupyter nbconvert --to notebook --execute --inplace notebooks/03_marketing_production.ipynb
```

Le fichier produit est écrit dans `docs & output/Autocall_France_Juillet_2018.html` : consultable directement dans un navigateur, imprimable/exportable en PDF via le bouton « Exporter PDF ».

## Prérequis

- Python 3.12
- `pandas`, `numpy`, `openpyxl`, `matplotlib`, `plotly` (+ `kaleido`), `jupyter`/`nbconvert`
