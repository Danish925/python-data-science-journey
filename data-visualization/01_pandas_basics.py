# 01 — Pandas basics (DataFrame vs Series)	

# Goals for Day 1:	
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

## Inspecting the table	
# - shape → (rows, columns)	
# - columns → column names	
# - dtypes → data types per column	

print('Shape:', df.shape)	
print('Columns:', list(df.columns))	
print('dtypes:\n', df.dtypes)	

## Series vs DataFrame	
# Selecting a single column returns a Series; the full table is a DataFrame.	

names_series = df['Name']	
print(type(names_series))  # <class 'pandas.core.series.Series'>	
print(names_series.head())	


# Day 1 summary and export	
summary_day1 = f"""	
PANDAS BASICS SUMMARY - Day 1	
=============================	

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
print(summary_day1)	

# Export the tiny demo table into the repo	

os.makedirs('data-visualization/data', exist_ok=True)	
df.to_csv('data-visualization/data/day1_demo_people.csv', index=False)	
print('Saved: data-visualization/data/day1_demo_people.csv')	


