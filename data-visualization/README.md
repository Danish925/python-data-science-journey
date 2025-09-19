Data Visualization
Beginner‑friendly pandas practice with the Titanic dataset. Each notebook is self‑contained and ends with a short summary and exported CSV for continuity.

Notebooks
01_pandas_basics.ipynb
Create a small DataFrame from a Python dict, inspect shape/columns/dtypes, and contrast Series (1D) vs DataFrame (2D). Ends with a Day 1 summary and a tiny CSV export.

02_titanic_loading_and_inspection.ipynb
Load the Titanic dataset with read_csv, run first‑look checks (head/tail, shape, columns), inspect structure (info, describe), count key categories (Survived, Pclass), and scan missing data. Ends with a Day 2 summary and a CSV snapshot for Day 3.

03_column_selection_and_filtering.ipynb
Practice column selection (single, multiple, by dtype), boolean filtering (single/multiple conditions with & and |), sorting (single/multiple columns), and quick groupby insights (survival by Sex and Pclass). Exports filtered datasets for Day 4.

Artifacts
data/day1_demo_people.csv — Exported from 01_pandas_basics.ipynb

data/titanic_day2.csv — Exported from 02_titanic_loading_and_inspection.ipynb

data/titanic_women.csv — Exported from 03_column_selection_and_filtering.ipynb (female subset)

data/titanic_complete.csv — Exported from 03_column_selection_and_filtering.ipynb (rows with non‑missing Age and Embarked)

How to run locally
Create and activate a virtual environment, then install pandas.

Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate
pip install pandas

macOS/Linux (bash/zsh)
python -m venv .venv
source .venv/bin/activate
pip install pandas

Open the notebooks in Jupyter or VS Code. Run cells top‑to‑bottom so outputs render correctly when viewed on GitHub.

Tips
Keep URLs to datasets inside the notebooks so runs are reproducible.

Restart & Run All before committing so the outputs match the code.

Keep outputs concise; show head() for large tables and rely on describe()/value_counts().

Roadmap
Day 4: Handling missing data (drop vs fill), simple feature creation

Day 5: GroupBy deep dive and basic statistics (aggregations, multi‑index)

Day 6+: Visualization primers (hist, box, count plots) and simple feature engineering

Related
How can I improve my README for Python projects in space
What are best practices for updating technical documentation
How to include project visuals in my README effectively
What templates are recommended for space-related bookmarks
How to ensure reproducibility in project documentation





