# 4 — Missing data and simple feature creation

import pandas as pd
import numpy as np
import os

# Load previously saved Titanic data or fallback to URL
try:
    titanic_df = pd.read_csv('titanic_data.csv')
    print("✅ Loaded titanic_data.csv")
except FileNotFoundError:
    url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
    titanic_df = pd.read_csv(url)
    print("📥 Loaded fresh Titanic data from web")

print(f"Dataset shape: {titanic_df.shape}")
print(f"Columns: {list(titanic_df.columns)}")

print(f"\n=== MISSING DATA ANALYSIS ===")

# Count missing values per column
missing_counts = titanic_df.isnull().sum()
print("Missing values per column:")
print(missing_counts[missing_counts > 0])

# Missing data percentages
total_rows = len(titanic_df)
missing_percentages = (missing_counts / total_rows) * 100
print(f"\nMissing data percentages:")
for column, percentage in missing_percentages[missing_percentages > 0].items():
    print(f"  {column}: {percentage:.1f}%")

print(f"\n=== DATA INFO OVERVIEW ===")
titanic_df.info()

print("\n=== SAMPLE OF MISSING DATA ===")
age_missing = titanic_df[titanic_df['Age'].isnull()]
print(f"Sample passengers with missing age (showing 5 of {len(age_missing)}):")
print(age_missing[['Name', 'Sex', 'Age', 'Pclass', 'Survived']].head())

print(f"\n=== IMPACT OF MISSING DATA ===")

# Drop rows with ANY missing value
complete_rows = titanic_df.dropna()
print(f"Complete rows (no missing values): {len(complete_rows)}")
print(f"Rows with missing data: {len(titanic_df) - len(complete_rows)}")
print(f"Data loss if dropping all missing: {(len(titanic_df) - len(complete_rows)) / len(titanic_df) * 100:.1f}%")

# Drop rows missing essential columns only
essential_cols = ['Age', 'Sex', 'Pclass', 'Survived']
essential_complete = titanic_df[essential_cols].dropna()
print(f"\nRows with complete essential data: {len(essential_complete)}")
print(f"Data loss for essential only: {(len(titanic_df) - len(essential_complete)) / len(titanic_df) * 100:.1f}%")

print(f"\n📊 KEY INSIGHT:")
print(f"Dropping ANY missing → Keep {len(complete_rows)} rows ({len(complete_rows) / len(titanic_df) * 100:.1f}%)")
print(f"Dropping essential only → Keep {len(essential_complete)} rows ({len(essential_complete) / len(titanic_df) * 100:.1f}%)")

print(f"\n=== DROPPING STRATEGIES ===")

no_missing_age = titanic_df.dropna(subset=['Age'])
print(f"Original: {len(titanic_df)} → After dropping missing Age: {len(no_missing_age)}")

clean_essential = titanic_df.dropna(subset=essential_cols)
print(f"Original: {len(titanic_df)} → After dropping missing essential data: {len(clean_essential)}")

cabin_missing_pct = (titanic_df['Cabin'].isnull().sum() / len(titanic_df)) * 100
print(f"\nCabin column missing: {cabin_missing_pct:.1f}%")

if cabin_missing_pct > 70:
    df_no_cabin = titanic_df.drop(['Cabin'], axis=1)
    print(f"Dropped Cabin column - now have {df_no_cabin.shape[1]} columns instead of {titanic_df.shape[1]}")
else:
    print("Cabin column has acceptable missing data, keeping it")

min_data_required = titanic_df.dropna(thresh=8)
print(f"Rows with at least 8 non-null values: {len(min_data_required)}")

print(f"\n=== FILLING STRATEGIES ===")

df_filled = titanic_df.copy()

median_age = df_filled['Age'].median()
df_filled['Age_filled_median'] = df_filled['Age'].fillna(median_age)
print(f"Filled Age missing values with median: {median_age:.1f}")

age_by_group = df_filled.groupby(['Sex', 'Pclass'])['Age'].median()
print("\nAge patterns by Sex and Class:")
print(age_by_group.round(1))

df_filled['Age_filled_smart'] = df_filled['Age']
for (sex, pclass), median_age in age_by_group.items():
    mask = (df_filled['Sex'] == sex) & (df_filled['Pclass'] == pclass) & (df_filled['Age'].isnull())
    df_filled.loc[mask, 'Age_filled_smart'] = median_age

most_common_port = df_filled['Embarked'].mode()[0]
df_filled['Embarked_filled'] = df_filled['Embarked'].fillna(most_common_port)
print(f"\nFilled Embarked missing values with most common: '{most_common_port}'")

df_filled['Cabin_filled'] = df_filled['Cabin'].fillna('Unknown')

print(f"\n=== AGE FILLING COMPARISON ===")
sample_missing_age = titanic_df[titanic_df['Age'].isnull()].iloc[0:3]
sample_indices = sample_missing_age.index

print("Sample passengers with missing age:")
comparison_cols = ['Name', 'Sex', 'Pclass', 'Age', 'Age_filled_median', 'Age_filled_smart']
print(df_filled.loc[sample_indices, comparison_cols])

print(f"\n=== CREATING NEW FEATURES ===\n")

df_features = df_filled.copy()

def categorize_age(age):
    if pd.isnull(age):
        return 'Unknown'
    elif age < 12:
        return 'Child'
    elif age < 20:
        return 'Teen'
    elif age < 65:
        return 'Adult'
    else:
        return 'Elder'

df_features['AgeGroup'] = df_features['Age_filled_smart'].apply(categorize_age)
print("Age group distribution:")
print(df_features['AgeGroup'].value_counts())

df_features['FamilySize'] = df_features['SibSp'] + df_features['Parch'] + 1
print(f"\nFamily size range: {df_features['FamilySize'].min()} to {df_features['FamilySize'].max()}")

df_features['IsAlone'] = (df_features['FamilySize'] == 1).astype(int)
print(f"Passengers traveling alone: {df_features['IsAlone'].sum()}")

df_features['Title'] = df_features['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
print(f"\nTitles found: {sorted(df_features['Title'].value_counts().index)}")

title_mapping = {
    'Mr': 'Mr', 'Miss': 'Miss', 'Mrs': 'Mrs', 'Master': 'Master'
}
df_features['Title_simple'] = df_features['Title'].map(title_mapping)
df_features['Title_simple'] = df_features['Title_simple'].fillna('Other')
print("Simplified title distribution:")
print(df_features['Title_simple'].value_counts())

df_features['FarePerPerson'] = df_features['Fare'] / df_features['FamilySize']
print(f"\nFare per person - Mean: ${df_features['FarePerPerson'].mean():.2f}")

df_features['Deck'] = df_features['Cabin'].str[0].fillna('Unknown')
print(f"Deck distribution:")
print(df_features['Deck'].value_counts())

print(f"\n=== COMPARING CLEANING STRATEGIES ===")

datasets = {
    'Original': titanic_df,
    'Dropped_Age_Missing': titanic_df.dropna(subset=['Age']),
    'Filled_Simple': df_filled,
    'With_Features': df_features
}

print("Dataset size comparison:")
for name, df in datasets.items():
    survival_rate = df['Survived'].mean() if 'Survived' in df.columns else 'N/A'
    print(f"  {name}: {len(df)} rows, Survival rate: {survival_rate:.1%}" if survival_rate != 'N/A' else f"  {name}: {len(df)} rows")

print(f"\n=== IMPACT ON KEY INSIGHTS ===")
for name, df in datasets.items():
    if 'Survived' in df.columns and 'Sex' in df.columns:
        gender_survival = df.groupby('Sex')['Survived'].mean()
        print(f"{name}:")
        for gender, rate in gender_survival.items():
            print(f"  {gender.capitalize()} survival: {rate:.1%}")
        print()

# Export cleaned datasets
os.makedirs('data-visualization/data', exist_ok=True)

minimal_clean = titanic_df.dropna(subset=['Survived', 'Sex', 'Pclass'])
minimal_clean.to_csv('data-visualization/data/titanic_minimal_clean.csv', index=False)

smart_clean = df_filled[['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex',
                         'Age_filled_smart', 'SibSp', 'Parch', 'Fare', 'Embarked_filled']].copy()
smart_clean.columns = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex',
                       'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
smart_clean.to_csv('data-visualization/data/titanic_smart_filled.csv', index=False)

feature_columns = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age_filled_smart',
                   'SibSp', 'Parch', 'Fare', 'Embarked_filled',
                   'AgeGroup', 'FamilySize', 'IsAlone', 'Title_simple', 'FarePerPerson', 'Deck']
featured_data = df_features[feature_columns].copy()
featured_data = featured_data.rename(columns={'Age_filled_smart': 'Age', 'Embarked_filled': 'Embarked'})
featured_data.to_csv('data-visualization/data/titanic_with_features.csv', index=False)

print(f"\n📁 Exported datasets:")
print(f"- titanic_minimal_clean.csv: {len(minimal_clean)} rows, basic cleaning")
print(f"- titanic_smart_filled.csv: {len(smart_clean)} rows, advanced filling")
print(f"- titanic_with_features.csv: {len(featured_data)} rows, {len(featured_data.columns)} columns")

print(f"\n🎯 KEY LEARNING:")
print("Strategic cleaning choices affect analysis and interpretation profoundly!")
