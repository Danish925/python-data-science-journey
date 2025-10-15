# 2 — Titanic: loading and first look

# Goals:
# - Load the Titanic dataset from a URL with read_csv
# - Do a first look: head/tail, shape, columns
# - Inspect structure: info(), describe()
# - Simple counts: value_counts on Survived and Pclass (sorted by label)
# - Missing-data scan per column
# - Print a summary and export a snapshot for next steps

import os
import pandas as pd

# Load Titanic dataset from a reliable URL
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_df = pd.read_csv(url)

# Quick confirmation
print(titanic_df.head())

# First look
print("=== FIRST 5 ROWS ===")
print(titanic_df.head())

print("\n=== LAST 5 ROWS ===")
print(titanic_df.tail())

print("\n=== SHAPE (rows, columns) ===")
print(titanic_df.shape)

print("\n=== COLUMNS ===")
print(list(titanic_df.columns))

# Structure and basic stats
print("=== INFO ===")
titanic_df.info()

print("\n=== DESCRIBE (numeric) ===")
print(titanic_df.describe())

# Simple counts
print("=== Survived counts ===")
print(titanic_df['Survived'].value_counts())

print("\n=== Pclass counts (sorted by class) ===")
print(titanic_df['Pclass'].value_counts().sort_index())

# Missing-data scan
missing_data = titanic_df.isnull().sum()
print("=== Missing values per column (only > 0) ===")
print(missing_data[missing_data > 0])

# Summary
summary = f"""
TITANIC DATASET SUMMARY
=======================

Dataset Size: {titanic_df.shape[0]} passengers, {titanic_df.shape[1]} columns
Survival Rate: {titanic_df['Survived'].mean():.2%}
Average Age: {titanic_df['Age'].mean():.1f} years
Most Common Class: Class {titanic_df['Pclass'].mode()[0]}
Missing Data: Age ({titanic_df['Age'].isnull().sum()}) and Cabin ({titanic_df['Cabin'].isnull().sum()})

Next Steps:
- Filter rows with multiple conditions (e.g., female & Age < 30)
- GroupBy for survival rates by Sex and Pclass
"""
print(summary)

# Save snapshot for next steps
os.makedirs('data-visualization/data', exist_ok=True)
titanic_df.to_csv('data-visualization/data/titanic_snapshot.csv', index=False)
print("Saved: data-visualization/data/titanic_snapshot.csv")
