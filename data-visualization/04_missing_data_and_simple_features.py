# 04 — Missing data and simple feature creation

# Goals for Day 4:
# - Load our cleaned dataset from Day 3 and examine missing data patterns
# - Master finding missing values: isnull(), isna(), sum(), info()
# - Learn strategic approaches: dropna() vs fillna() with their trade-offs
# - Practice different filling strategies: constant values, mean/median, mode, forward/backward fill
# - Create simple new features from existing columns (basic feature engineering)
# - Understand data cleaning decisions and their impact on analysis
# - Export multiple cleaned versions for Day 5

# **Key concept**: Real data is messy! Every cleaning choice affects your analysis:
# - Dropping data = losing information (but keeping quality high)
# - Filling data = keeping all rows (but making assumptions about missing values)
# - Each approach has trade-offs - there's no single "right" way



import pandas as pd
import numpy as np

# Load our work from Day 3 - try multiple sources for flexibility
try:
    titanic_df = pd.read_csv('titanic_data.csv')
    print("✅ Loaded titanic_data.csv")
except FileNotFoundError:
    # Fallback to original dataset
    url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
    titanic_df = pd.read_csv(url)
    print("📥 Loaded fresh Titanic data from web")

print(f"Dataset shape: {titanic_df.shape}")
print(f"Columns: {list(titanic_df.columns)}")



print(f"\n=== MISSING DATA ANALYSIS ===")

# Method 1: Count missing values per column
missing_counts = titanic_df.isnull().sum()
print("Missing values per column:")
print(missing_counts[missing_counts > 0])  # Only show columns with missing data

# Method 2: Percentage of missing data
total_rows = len(titanic_df)
missing_percentages = (missing_counts / total_rows) * 100
print(f"\nMissing data percentages (out of {total_rows} total rows):")
for column, percentage in missing_percentages[missing_percentages > 0].items():
    print(f"  {column}: {percentage:.1f}%")

# Method 3: Quick overview with info()
print(f"\n=== DATA INFO OVERVIEW ===")
titanic_df.info()

# Method 4: See actual missing data patterns
print("\n=== SAMPLE OF MISSING DATA ===")
# Show rows where Age is missing
age_missing = titanic_df[titanic_df['Age'].isnull()]
print(f"Sample passengers with missing age (showing 5 of {len(age_missing)}):")
print(age_missing[['Name', 'Sex', 'Age', 'Pclass', 'Survived']].head())

print(f"\n=== IMPACT OF MISSING DATA ===")

# How much data would we lose if we drop all rows with ANY missing value?
complete_rows = titanic_df.dropna()
print(f"Complete rows (no missing values): {len(complete_rows)}")
print(f"Rows with missing data: {len(titanic_df) - len(complete_rows)}")
print(f"Data loss if we drop all: {((len(titanic_df) - len(complete_rows)) / len(titanic_df)) * 100:.1f}%")

# What if we only care about specific columns?
essential_cols = ['Age', 'Sex', 'Pclass', 'Survived']
essential_complete = titanic_df[essential_cols].dropna()
print(f"\nRows with complete essential data: {len(essential_complete)}")
print(f"Data loss for essential columns only: {((len(titanic_df) - len(essential_complete)) / len(titanic_df)) * 100:.1f}%")

# Show the trade-off clearly
print(f"\n📊 KEY INSIGHT:")
print(f"Dropping ANY missing → Keep {len(complete_rows)} rows ({len(complete_rows)/len(titanic_df)*100:.1f}%)")
print(f"Dropping only essential missing → Keep {len(essential_complete)} rows ({len(essential_complete)/len(titanic_df)*100:.1f}%)")



print(f"\n=== DROPPING STRATEGIES ===")

# Strategy 1A: Drop rows with missing Age (most common missing value)
no_missing_age = titanic_df.dropna(subset=['Age'])
print(f"Original: {len(titanic_df)} → After dropping missing Age: {len(no_missing_age)}")

# Strategy 1B: Drop rows missing ANY essential information
essential_cols = ['Age', 'Sex', 'Pclass', 'Survived'] 
clean_essential = titanic_df.dropna(subset=essential_cols)
print(f"Original: {len(titanic_df)} → After dropping missing essential data: {len(clean_essential)}")

# Strategy 1C: Drop columns with too much missing data
# Cabin is missing for most passengers - might not be useful
cabin_missing_pct = (titanic_df['Cabin'].isnull().sum() / len(titanic_df)) * 100
print(f"\nCabin column missing: {cabin_missing_pct:.1f}%")

if cabin_missing_pct > 70:  # If more than 70% missing
    df_no_cabin = titanic_df.drop(['Cabin'], axis=1)
    print(f"Dropped Cabin column - now have {df_no_cabin.shape[1]} columns instead of {titanic_df.shape[1]}")
else:
    print("Cabin column has acceptable missing data, keeping it")

# Strategy 1D: Require minimum data completeness
# Keep only rows with at least 8 out of ~11 columns filled
min_data_required = titanic_df.dropna(thresh=8)  
print(f"Rows with at least 8 non-null values: {len(min_data_required)}")


print(f"\n=== FILLING STRATEGIES ===")

# Create a working copy so we don't modify the original
df_filled = titanic_df.copy()

# Strategy 2A: Fill Age with median (robust to outliers)
median_age = df_filled['Age'].median()
df_filled['Age_filled_median'] = df_filled['Age'].fillna(median_age)
print(f"Filled Age missing values with median: {median_age:.1f}")


# Strategy 2B: Fill Age with mean by gender and class (more sophisticated)
# This assumes people of similar gender/class have similar ages
age_by_group = df_filled.groupby(['Sex', 'Pclass'])['Age'].median()
print("\nAge patterns by Sex and Class:")
print(age_by_group.round(1))

# Apply group-based filling
df_filled['Age_filled_smart'] = df_filled['Age']
for (sex, pclass), median_age in age_by_group.items():
    mask = (df_filled['Sex'] == sex) & (df_filled['Pclass'] == pclass) & (df_filled['Age'].isnull())
    df_filled.loc[mask, 'Age_filled_smart'] = median_age
    
# Strategy 2C: Fill Embarked with most common port
most_common_port = df_filled['Embarked'].mode()[0] # mode() returns a series, take first
df_filled['Embarked_filled'] = df_filled['Embarked'].fillna(most_common_port)
print(f"\nFilled Embarked missing values with most common: '{most_common_port}'")

# Strategy 2D: Fill Cabin with "Unknown" 
df_filled['Cabin_filled'] = df_filled['Cabin'].fillna('Unknown')

# Compare different Age filling strategies
print(f"\n=== AGE FILLING COMPARISON ===")
sample_missing_age = titanic_df[titanic_df['Age'].isnull()].iloc[0:3]  # First 3 missing
sample_indices = sample_missing_age.index

print("Sample passengers with missing age:")
comparison_cols = ['Name', 'Sex', 'Pclass', 'Age', 'Age_filled_median', 'Age_filled_smart']
print(df_filled.loc[sample_indices, comparison_cols])



print(f"\n=== CREATING NEW FEATURES ===\n")

# Work with our filled dataset
df_features = df_filled.copy()

# Feature 1: Age Groups (life stages)
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

# Feature 2: Family size (combining SibSp + Parch)
df_features['FamilySize'] = df_features['SibSp'] + df_features['Parch'] + 1  # +1 for passenger themselves
print(f"\nFamily size range: {df_features['FamilySize'].min()} to {df_features['FamilySize'].max()}")

# Feature 3: Traveling alone indicator
df_features['IsAlone'] = (df_features['FamilySize'] == 1).astype(int)
print(f"Passengers traveling alone: {df_features['IsAlone'].sum()}")

# Feature 4: Extract title from name
df_features['Title'] = df_features['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
print(f"\nTitles found: {sorted(df_features['Title'].value_counts().index)}")

# Simplify rare titles
title_mapping = {
    'Mr': 'Mr', 'Miss': 'Miss', 'Mrs': 'Mrs', 'Master': 'Master'
}
df_features['Title_simple'] = df_features['Title'].map(title_mapping)
df_features['Title_simple'] = df_features['Title_simple'].fillna('Other')
print("Simplified title distribution:")
print(df_features['Title_simple'].value_counts())

# Feature 5: Fare per person (for group bookings)
df_features['FarePerPerson'] = df_features['Fare'] / df_features['FamilySize']
print(f"\nFare per person - Mean: ${df_features['FarePerPerson'].mean():.2f}")

# Feature 6: Cabin deck (first letter of cabin)
df_features['Deck'] = df_features['Cabin'].str[0]
df_features['Deck'] = df_features['Deck'].fillna('Unknown')
print(f"Deck distribution:")
print(df_features['Deck'].value_counts())



print(f"\n=== COMPARING CLEANING STRATEGIES ===")

# Create different cleaned versions
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

# Quick insight: Does our cleaning affect key findings?
print(f"\n=== IMPACT ON KEY INSIGHTS ===")
for name, df in datasets.items():
    if 'Survived' in df.columns and 'Sex' in df.columns:
        gender_survival = df.groupby('Sex')['Survived'].mean()
        print(f"{name}:")
        for gender, rate in gender_survival.items():
            print(f"  {gender.capitalize()} survival: {rate:.1%}")
        print()



# Keep rows that have essential info; adjust the subset if needed
essential_cols = ['Survived', 'Sex', 'Pclass']
minimal_clean = titanic_df.dropna(subset=essential_cols)
minimal_clean.to_csv('titanic_minimal_clean.csv', index=False)
print("Saved: data-visualization/data/titanic_minimal_clean.csv")


# Assume df_filled exists from Day 4 (Age_filled_smart, Embarked_filled created)
smart_clean = df_filled[['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex',
                         'Age_filled_smart', 'SibSp', 'Parch', 'Fare', 'Embarked_filled']].copy()
smart_clean.columns = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex',
                       'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
smart_clean.to_csv('titanic_smart_filled.csv', index=False)
print("Saved: data-visualization/data/titanic_smart_filled.csv")


# Assume df_features exists from Day 4 (AgeGroup, FamilySize, IsAlone, Title_simple, FarePerPerson, Deck created)
feature_columns = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex',
                   'Age_filled_smart', 'SibSp', 'Parch', 'Fare', 'Embarked_filled',
                   'AgeGroup', 'FamilySize', 'IsAlone', 'Title_simple', 'FarePerPerson', 'Deck']
featured_data = df_features[feature_columns].copy()
# Optional: rename Age_filled_smart/Embarked_filled to simpler names
featured_data = featured_data.rename(columns={'Age_filled_smart': 'Age', 'Embarked_filled': 'Embarked'})
featured_data.to_csv('titanic_with_features.csv', index=False)
print("Saved: data-visualization/data/titanic_with_features.csv")




# Day 4 summary and exports
summary = f"""
MISSING DATA & FEATURE CREATION SUMMARY - Day 4
===============================================

Original Dataset: {len(titanic_df)} rows, {titanic_df.shape[1]} columns

Missing Data Found:
- Age: {titanic_df['Age'].isnull().sum()} missing ({titanic_df['Age'].isnull().sum()/len(titanic_df)*100:.1f}%)
- Cabin: {titanic_df['Cabin'].isnull().sum()} missing ({titanic_df['Cabin'].isnull().sum()/len(titanic_df)*100:.1f}%)
- Embarked: {titanic_df['Embarked'].isnull().sum()} missing

Cleaning Strategies Applied:
1. Dropped rows: Age missing → {len(titanic_df.dropna(subset=['Age']))} rows remaining
2. Smart filling: Age by Sex+Class groups, Embarked with mode
3. Feature creation: AgeGroup, FamilySize, IsAlone, Title, Deck

New Features Created: {len([col for col in df_features.columns if col not in titanic_df.columns])}

Key Insights:
- Family survival patterns: Larger families had different survival rates
- Title importance: Social status (Mr/Mrs/Miss) correlates with survival  
- Age groups: Children had higher survival rates

Next Steps (Day 5):
- Advanced GroupBy operations with clean data
- Statistical summaries by multiple categories
- Correlation analysis between new features
"""
print(summary)

# Export different cleaned versions for Day 5
import os
os.makedirs('data-visualization/data', exist_ok=True)

# Version 1: Minimal cleaning (just drop extreme missing)
minimal_clean = titanic_df.dropna(subset=['Survived', 'Sex', 'Pclass'])  # Keep essential columns
minimal_clean.to_csv('data-visualization/data/titanic_minimal_clean.csv', index=False)

# Version 2: Smart filled
smart_clean = df_filled[['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 
                        'Age_filled_smart', 'SibSp', 'Parch', 'Fare', 'Embarked_filled']]
smart_clean.columns = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 
                      'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']  # Rename for simplicity
smart_clean.to_csv('data-visualization/data/titanic_smart_filled.csv', index=False)

# Version 3: Full featured dataset
feature_columns = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age_filled_smart', 
                  'SibSp', 'Parch', 'Fare', 'Embarked_filled',
                  'AgeGroup', 'FamilySize', 'IsAlone', 'Title_simple', 'FarePerPerson', 'Deck']
featured_data = df_features[feature_columns].copy()
featured_data.to_csv('data-visualization/data/titanic_with_features.csv', index=False)

print(f"\n📁 Exported datasets:")
print(f"- titanic_minimal_clean.csv: {len(minimal_clean)} rows, basic cleaning")
print(f"- titanic_smart_filled.csv: {len(smart_clean)} rows, smart missing data handling") 
print(f"- titanic_with_features.csv: {len(featured_data)} rows, {len(featured_data.columns)} columns with new features")

print(f"\n🎯 KEY LEARNING:")
print(f"Data cleaning isn't just about removing problems—it's about making strategic choices that shape your analysis!")
