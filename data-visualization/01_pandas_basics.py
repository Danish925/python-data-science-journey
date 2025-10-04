# 1. Pandas basics (DataFrame vs Series)

# Goals:
# - Create a small DataFrame from a Python dict
# - Inspect shape, columns, and dtypes
# - See the difference between Series (1D) and DataFrame (2D)

import pandas as pd
import os

# Build a tiny table from a Python dict
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NY', 'LDN', 'TOK']
}
df = pd.DataFrame(data)
print(df)

# Inspecting the table
print('Shape:', df.shape)
print('Columns:', list(df.columns))
print('dtypes:\n', df.dtypes)

# Series vs DataFrame
names_series = df['Name']
print(type(names_series))  # <class 'pandas.core.series.Series'>
print(names_series.head())

# Summary and export
summary = f"""
PANDAS BASICS SUMMARY
=====================
Objective: Install pandas, create a small DataFrame, and learn quick inspection.
Rows × Columns: {df.shape[0]} × {df.shape[1]}
Column Names: {list(df.columns)}
Data Types:
{df.dtypes.to_string()}

Key Concepts:
- DataFrame (2D table) vs Series (single column)
- Quick structure checks: df.shape, df.columns, df.dtypes
- Preview with df.head()

Next Steps:
- Load a real dataset with read_csv and perform first-look analysis
"""
print(summary)

os.makedirs('data-visualization/data', exist_ok=True)
df.to_csv('data-visualization/data/part1_demo_people.csv', index=False)
print('Saved: data-visualization/data/part1_demo_people.csv')
