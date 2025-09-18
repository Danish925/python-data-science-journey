# Data Visualization

This section contains beginner-friendly notebooks to learn pandas and exploratory analysis step by step.

## Notebooks
- 01_pandas_basics.ipynb  
  Create a small DataFrame from a Python dict, inspect shape/columns/dtypes, and see the difference between a Series (1D) and a DataFrame (2D). Ends with a short summary and a tiny CSV export for reference.

- 02_titanic_loading_and_inspection.ipynb  
  Load the Titanic dataset with read_csv, get a first look (head/tail, shape, columns), inspect structure (info, describe), run simple counts (Survived and Pclass sorted by label), and perform a missing‑data scan. Ends with a summary and an exported working CSV for Day 3.

## Artifacts
- data/day1_demo_people.csv — Exported from 01_pandas_basics.ipynb
- data/titanic_day2.csv — Exported from 02_titanic_loading_and_inspection.ipynb

## How to run locally
1) Set up a virtual environment and install pandas:
   - Windows (PowerShell):
     python -m venv .venv
     .venv\Scripts\Activate
     pip install pandas
   - macOS/Linux (bash/zsh):
     python -m venv .venv
     source .venv/bin/activate
     pip install pandas

2) Open notebooks in Jupyter or VS Code and run all cells (top to bottom).

## Next steps
- Day 3: Selecting columns, filtering rows with multiple conditions
- Day 4: Handling missing data (drop vs fill), basic strategies
- Day 5: GroupBy for quick statistics and simple insights
