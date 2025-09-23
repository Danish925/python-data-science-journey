# Data Visualization Journey

This repository contains a step-by-step learning journey exploring the Titanic dataset using Python and pandas. Each script builds meaningful data science skills — from initial loading and cleaning to advanced groupby analysis — paired with exporting clean data files.

---

## Contents

### Day 1 — Setup and first look
- Environment preparation, loading CSV, initial exploration.
- Script: `01_pandas_basics.py`

### Day 2 — Loading and inspection
- Deeper data inspection, types, missing values, and visuals.
- Script: `02_titanic_loading_and_inspection.py`

### Day 3 — Column selection and filtering
- Selecting subsets of columns, boolean filtering, and queries.
- Script: `03_column_selection_and_filtering.py`

### Day 4 — Missing data and simple features
- Handling missing values (drop vs fill), group-based fill.
- Feature engineering: AgeGroup, FamilySize, IsAlone, Titles, etc.
- Script: `04_missing_data_and_simple_features.py`
- Data exports:
  - `data/titanic_minimal_clean.csv`
  - `data/titanic_smart_filled.csv`
  - `data/titanic_with_features.csv`

### Groupby Deep Dive and Advanced Statistics
- Advanced usage of `.groupby()`, custom aggregation with `.apply()`.
- Performance optimizations using categorical data.
- Business questions on survival related to gender, class, family, age.
- Script: `groupby_deep_dive.py`
- Data exports:
  - `data/survival_analysis.csv`
  - `data/detailed_groupby_analysis.csv`

---

## How to Use This Repository

- Install dependencies via:
