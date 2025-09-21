Data Visualization Journey (Days 1–4)
This repository documents a progressive, hands-on journey through data analysis and visualization with Python and pandas, using the Titanic dataset as a running example. Each “Day” adds skills and artifacts that build toward robust, reproducible analysis.

Day 1 — Setup and first look

  • Goals: Environment setup, load CSV, peek at rows, basic summary stats.
  • Artifacts: 01_pandas_basics.ipynb / .py, initial dataset copy.

Day 2 — Loading and inspection

  • Goals: Robust loading, dtypes, basic cleaning, descriptive stats, value_counts, simple visuals.
  • Artifacts: 02_titanic_loading_and_inspection.ipynb / .py.

Day 3 — Column selection and filtering

  • Goals: Column subsetting, boolean masks, chained conditions, query patterns, safe .loc usage.
  • Artifacts: 03_column_selection_and_filtering.ipynb / .py.
  • Highlights: Clear patterns by Sex and Pclass, careful boolean indexing to avoid SettingWithCopy issues.

Day 4 — Missing data and simple features

  • Goals: Detect missingness, compare drop vs fill strategies, group-aware imputations, and create basic engineered features.
  • Key techniques:
     • Finding missing data: isnull/isna, sum, info, and percentages.
     • Cleaning approaches: dropna with subset and thresh; fillna with constants, mode, medians; groupby-based median fills (e.g., by Sex×Pclass).
     • Feature engineering: AgeGroup (life stages), FamilySize, IsAlone, Title extraction and simplification, FarePerPerson, Deck from Cabin.
  • Artifacts: 04_missing_data_and_simple_features.ipynb / .py.

Exported datasets (Day 4)
CSV exports are saved under data-visualization/data to snapshot different cleaned states:

   • data-visualization/data/titanic_minimal_clean.csv
     Essential columns present (e.g., Survived, Sex, Pclass); rows missing critical fields dropped.

   • data-visualization/data/titanic_smart_filled.csv
     “Smart-filled” version where Age is imputed by group medians (Sex×Pclass) and Embarked is filled with the overall mode; columns aligned back to standard names      (Age, Embarked).

   • data-visualization/data/titanic_with_features.csv
     Feature-rich version including engineered fields: AgeGroup, FamilySize, IsAlone, Title_simple, FarePerPerson, Deck (and cleaned Age/Embarked).

How to run
   • Python 3.9+ recommended.

   • Install dependencies: pandas, numpy, (optional) jupyter, seaborn, matplotlib.

   • Run notebooks with Jupyter or run the .py scripts from the project root.

   • Outputs: The three CSVs listed above are produced by Day 4 cells near the end of that notebook/script.
