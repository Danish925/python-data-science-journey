# 3 — Titanic: Column selection, filtering, sorting, and groupby basics

import pandas as pd
import os

# Load the Titanic dataset saved previously
titanic_df = pd.read_csv('titanic_data.csv')
# Alternatively, load from URL:
# titanic_df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

print("Data loaded successfully!")
print(f"Shape: {titanic_df.shape}")
print(f"Columns: {list(titanic_df.columns)}\n")

# Single column selection
names = titanic_df['Name']
print(f"Type: {type(names)}")  # Series
print("First 5 names:")
print(names.head())

ages = titanic_df.Age  # Dot notation for simple column names
print(f"\nFirst 5 ages:")
print(ages.head())

print(f"\nAge statistics:")
print(f"Average age: {titanic_df['Age'].mean():.1f}")
print(f"Youngest: {titanic_df['Age'].min()}")
print(f"Oldest: {titanic_df['Age'].max()}\n")

# Multiple columns selection
basic_info = titanic_df[['Name', 'Age', 'Sex', 'Survived']]
print(f"Type: {type(basic_info)}")  # DataFrame
print("Basic info (first 5 rows):")
print(basic_info.head())

numeric_cols = titanic_df[['Age', 'Fare', 'Pclass', 'Survived']]
print(f"\nNumeric data shape: {numeric_cols.shape}")
print(numeric_cols.describe())

important_cols = ['Name', 'Age', 'Sex', 'Pclass', 'Survived', 'Fare']
analysis_df = titanic_df[important_cols]
print(f"\nAnalysis dataset shape: {analysis_df.shape}\n")

# Select by data type
numeric_data = titanic_df.select_dtypes(include=['number'])
print("Numeric columns:")
print(numeric_data.dtypes)
print(numeric_data.head())

text_data = titanic_df.select_dtypes(include=['object'])
print(f"\nText columns: {list(text_data.columns)}")

mixed_data = titanic_df.select_dtypes(include=['number']).copy()
mixed_data['Sex'] = titanic_df['Sex']
print(f"\nMixed dataset columns: {list(mixed_data.columns)}\n")

# Single condition filtering
women = titanic_df[titanic_df['Sex'] == 'female']
print(f"Total passengers: {len(titanic_df)}")
print(f"Female passengers: {len(women)} ({len(women)/len(titanic_df)*100:.1f}%)")

older_passengers = titanic_df[titanic_df['Age'] > 30]
print(f"Passengers over 30: {len(older_passengers)}")

first_class = titanic_df[titanic_df['Pclass'] == 1]
print(f"First class passengers: {len(first_class)}")

survivors = titanic_df[titanic_df['Survived'] == 1]
print(f"Survivors: {len(survivors)} ({len(survivors)/len(titanic_df)*100:.1f}%)")

print("\nExample: First 5 female passengers")
print(women[['Name', 'Age', 'Pclass', 'Survived']].head())

# Multiple conditions filtering
young_women = titanic_df[(titanic_df['Sex'] == 'female') & (titanic_df['Age'] < 30)]
print(f"Young women (under 30): {len(young_women)}")

first_or_survivor = titanic_df[(titanic_df['Pclass'] == 1) | (titanic_df['Survived'] == 1)]
print(f"First class OR survivors: {len(first_or_survivor)}")

elite_survivors = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Age'] < 30) &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Survived'] == 1)
]
print(f"Young first-class women who survived: {len(elite_survivors)}")

print("\nExample: Elite survivors")
print(elite_survivors[['Name', 'Age', 'Pclass', 'Fare']].head())

died = titanic_df[titanic_df['Survived'] == 0]
print(f"\nDied: {len(died)} passengers\n")

# Basic sorting
by_age = titanic_df.sort_values(by='Age')
print("Youngest passengers:")
print(by_age[['Name', 'Age', 'Sex', 'Pclass']].head())

by_age_desc = titanic_df.sort_values(by='Age', ascending=False)
print("\nOldest passengers:")
print(by_age_desc[['Name', 'Age', 'Sex', 'Pclass']].head())

by_fare = titanic_df.sort_values(by='Fare', ascending=False)
print("\nMost expensive tickets:")
print(by_fare[['Name', 'Fare', 'Pclass', 'Survived']].head())

# Multi-column sorting
by_class_fare = titanic_df.sort_values(by=['Pclass', 'Fare'], ascending=[True, False])
print("Sorted by class (1→3), then by highest fare within class:")
print(by_class_fare[['Name', 'Pclass', 'Fare', 'Survived']].head(10))

by_survival_age = titanic_df.sort_values(by=['Survived', 'Age'], ascending=[False, True])
print("\nSurvivors first (by age), then non-survivors (by age):")
print(by_survival_age[['Name', 'Age', 'Sex', 'Survived']].head(10))

# GroupBy examples
gender_survival = titanic_df.groupby('Sex')['Survived'].mean()
print("Survival rate by gender:")
for gender, rate in gender_survival.items():
    print(f"  {gender.capitalize()}: {rate:.2%}")

class_survival = titanic_df.groupby('Pclass')['Survived'].mean()
print(f"\nSurvival rate by class:")
print(class_survival.round(1))
for pclass, rate in class_survival.items():
    print(f"  Class {pclass}: {rate:.2%}")

age_by_gender_class = titanic_df.groupby(['Sex', 'Pclass'])['Age'].mean()
print(f"\nAverage age by gender and class:")
print(age_by_gender_class.round(1))

embark_counts = titanic_df['Embarked'].value_counts()
print(f"\nPassengers by embarked port:")
print(embark_counts)

# Summary and export
summary = f"""
COLUMN SELECTION & FILTERING SUMMARY
====================================

Data loaded: {titanic_df.shape[0]} passengers, {titanic_df.shape[1]} columns

Column Selection Learned:
- Single column: df['Name'] → Series
- Multiple columns: df[['Name', 'Age']] → DataFrame
- By type: df.select_dtypes(include=['number']) → numeric only

Filtering Examples Applied:
- Female passengers: {len(women)}
- Passengers over 30: {len(older_passengers)}
- Young women: {len(young_women)}
- First class: {len(first_class)}

Key Insights Discovered:
- Female survival rate: {titanic_df[titanic_df['Sex'] == 'female']['Survived'].mean():.1%}
- Male survival rate: {titanic_df[titanic_df['Sex'] == 'male']['Survived'].mean():.1%}
- First class survival: {titanic_df[titanic_df['Pclass'] == 1]['Survived'].mean():.1%}
- Third class survival: {titanic_df[titanic_df['Pclass'] == 3]['Survived'].mean():.1%}

Next Steps:
- Handle missing Age and Cabin data properly
- Create new columns from existing data
- Learn advanced groupby operations
"""

print(f"\n{summary}")

# Save filtered datasets for further analysis
os.makedirs('data-visualization/data', exist_ok=True)
women.to_csv('data-visualization/data/titanic_women.csv', index=False)
complete_data = titanic_df.dropna(subset=['Age', 'Embarked'])
complete_data.to_csv('data-visualization/data/titanic_complete.csv', index=False)

print(f"\nSaved datasets:")
print(f"- Women passengers: data-visualization/data/titanic_women.csv ({len(women)} rows)")
print(f"- Complete data: data-visualization/data/titanic_complete.csv ({len(complete_data)} rows)")
