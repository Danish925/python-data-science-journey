import pandas as pd
import numpy as np

# Load our cleaned data 
# (You can use any of the three CSV exports we created)
titanic_df = pd.read_csv('titanic_with_features.csv')

print("Dataset loaded successfully!")
print(f"Shape: {titanic_df.shape}")
print(f"Columns: {list(titanic_df.columns)}")

# SECTION 1: UNDERSTANDING GROUPBY

grouped = titanic_df.groupby('Sex')
print(f"Type of groupby object: {type(grouped)}")
print(f"Number of groups: {grouped.ngroups}")
print(f"Group sizes:")
print(grouped.size())

# SECTION 2: BASIC GROUPBY OPERATIONS

print("Survival rate by gender:")
gender_survival = titanic_df.groupby('Sex')['Survived'].mean()
print(gender_survival)
print(f"Type: {type(gender_survival)}")

print("Passenger count by gender:")
gender_count = titanic_df.groupby('Sex').size()
print(gender_count)

print("Multiple statistics at once:")
gender_stats = titanic_df.groupby('Sex')['Age'].describe()
print(gender_stats)

# SECTION 3: MULTIPLE COLUMN GROUPING

print("Survival rate by Sex AND Passenger Class:")
multi_group = titanic_df.groupby(['Sex', 'Pclass'])['Survived'].mean()
print(multi_group)

print("This creates a hierarchical index (MultiIndex)")
print(f"Index levels: {multi_group.index.names}")

multi_df = multi_group.reset_index()
print("As a regular DataFrame:")
print(multi_df)

print("Unstacked view (like a pivot table):")
pivot_view = multi_group.unstack()
print(pivot_view)

# SECTION 4: ADVANCED AGGREGATION

print("Age statistics by gender:")
age_stats = titanic_df.groupby('Sex')['Age'].agg(['mean', 'median', 'std', 'min', 'max'])
print(age_stats)

print("Different functions for different columns:")
complex_agg = titanic_df.groupby('Sex').agg({
    'Age': ['mean', 'median'],
    'Fare': ['mean', 'max'],
    'Survived': 'sum'
})
print(complex_agg)

print("Named aggregations:")
named_agg = titanic_df.groupby('Sex').agg(
    avg_age=('Age', 'mean'),
    median_age=('Age', 'median'),
    avg_fare=('Fare', 'mean'),
    total_survivors=('Survived', 'sum'),
    passenger_count=('PassengerId', 'count')
)
print(named_agg)

# SECTION 5: CUSTOM FUNCTIONS WITH APPLY

def age_range(series):
    """Calculate the range (max - min) of ages"""
    if series.isna().all():
        return np.nan
    return series.max() - series.min()

print("Age range by passenger class:")
age_ranges = titanic_df.groupby('Pclass')['Age'].apply(age_range)
print(age_ranges)

def survival_summary(group):
    total = len(group)
    survivors = group['Survived'].sum()
    survival_rate = survivors / total if total > 0 else 0
    avg_age = group['Age'].mean()
    return pd.Series({
        'total_passengers': total,
        'survivors': int(survivors),
        'survival_rate': round(survival_rate, 3),
        'avg_age': round(avg_age, 1)
    })

print("Custom survival summary by passenger class:")
custom_summary = titanic_df.groupby('Pclass').apply(survival_summary)
print(custom_summary)

# SECTION 6: TRANSFORM VS AGGREGATE

print("Aggregate example - mean age by class:")
agg_result = titanic_df.groupby('Pclass')['Age'].mean()
print(f"Shape: {agg_result.shape}")
print(agg_result)

print("Transform example - subtract group mean from each value:")
titanic_df['Age_minus_class_mean'] = titanic_df.groupby('Pclass')['Age'].transform(lambda x: x - x.mean())
print("First 10 rows showing original Age and Age minus class mean:")
print(titanic_df[['PassengerId', 'Pclass', 'Age', 'Age_minus_class_mean']].head(10))

print(f"Original DataFrame shape: {titanic_df.shape}")
print("Transform kept the same number of rows!")

# SECTION 7: FILTERING GROUPS

print("Only show passenger classes with more than 100 passengers:")
large_classes = titanic_df.groupby('Pclass').filter(lambda x: len(x) > 100)
print(f"Original shape: {titanic_df.shape}")
print(f"Filtered shape: {large_classes.shape}")
print("Passenger counts by class in filtered data:")
print(large_classes['Pclass'].value_counts().sort_index())

print("Only show groups where survival rate > 50%:")
high_survival = titanic_df.groupby('Sex').filter(lambda x: x['Survived'].mean() > 0.5)
print("Gender distribution in high-survival groups:")
print(high_survival['Sex'].value_counts())

# SECTION 8: REAL-WORLD ANALYSIS

print("1. Survival rate by passenger class:")
class_survival = titanic_df.groupby('Pclass')['Survived'].agg(['count', 'sum', 'mean'])
class_survival.columns = ['Total_Passengers', 'Survivors', 'Survival_Rate']
class_survival = class_survival.round(3)
print(class_survival)
highest_survival_class = class_survival['Survival_Rate'].idxmax()
print(f"Answer: Class {highest_survival_class} had the highest survival rate")

print("2. Average age of survivors vs non-survivors by gender:")
age_by_survival = titanic_df.groupby(['Sex', 'Survived'])['Age'].mean().unstack()
age_by_survival.columns = ['Non_Survivors', 'Survivors']
print(age_by_survival.round(1))

print("3. Survival rate by title:")
title_survival = titanic_df.groupby('Title_simple')['Survived'].agg(['count', 'mean'])
title_survival.columns = ['Count', 'Survival_Rate']
title_survival = title_survival.sort_values('Survival_Rate', ascending=False)
print(title_survival.round(3))

print("4. Survival rate by family size:")
family_survival = titanic_df.groupby('FamilySize')['Survived'].agg(['count', 'mean'])
family_survival.columns = ['Count', 'Survival_Rate']
print(family_survival.round(3))

# SECTION 9: ADVANCED TECHNIQUES

print("Complex analysis: Age groups by gender and class")
age_group_analysis = titanic_df.groupby(['Sex', 'Pclass', 'AgeGroup']).agg({
    'PassengerId': 'count',
    'Survived': ['sum', 'mean'],
    'Fare': 'mean'
}).round(2)

age_group_analysis.columns = ['_'.join(col).strip() for col in age_group_analysis.columns]
print(age_group_analysis.head(10))

print("Fare percentiles by passenger class:")
fare_percentiles = titanic_df.groupby('Pclass')['Fare'].quantile([0.25, 0.5, 0.75]).unstack()
fare_percentiles.columns = ['25th_Percentile', 'Median', '75th_Percentile']
print(fare_percentiles.round(2))

# SECTION 10: PERFORMANCE TIPS

print("Converting Sex to categorical for better performance:")
titanic_df['Sex_cat'] = titanic_df['Sex'].astype('category')
print(f"Memory usage - original: {titanic_df['Sex'].memory_usage(deep=True)} bytes")
print(f"Memory usage - categorical: {titanic_df['Sex_cat'].memory_usage(deep=True)} bytes")

print("Compare these approaches:")
print("Inefficient (multiple operations):") 

import time
inefficient_start = time.time()
mean_age = titanic_df.groupby('Pclass')['Age'].mean()
std_age = titanic_df.groupby('Pclass')['Age'].std()
min_age = titanic_df.groupby('Pclass')['Age'].min()
inefficient_time = time.time() - inefficient_start

print("Efficient (single .agg() call):")
efficient_start = time.time()
all_stats = titanic_df.groupby('Pclass')['Age'].agg(['mean', 'std', 'min'])
efficient_time = time.time() - efficient_start

print(f"Inefficient approach took: {inefficient_time:.4f} seconds")
print(f"Efficient approach took: {efficient_time:.4f} seconds")

# Practice Questions

print("1. Oldest and youngest passengers:")
age_extremes = titanic_df.groupby('Sex')['Age'].agg(['min', 'max'])
print(age_extremes)

oldest_passenger = titanic_df.loc[titanic_df['Age'].idxmax()]
youngest_passenger = titanic_df.loc[titanic_df['Age'].idxmin()]
print(f"Oldest: {oldest_passenger['Name']}, Age: {oldest_passenger['Age']}")
print(f"Youngest: {youngest_passenger['Name']}, Age: {youngest_passenger['Age']}")

print("2. Average fare by passenger class:")
avg_fare_by_class = titanic_df.groupby('Pclass')['Fare'].mean()
print(avg_fare_by_class.round(2))

print("3. Family survival analysis:")
titanic_df['LastName'] = titanic_df['Name'].str.extract(r'([^,]+),')
family_sizes = titanic_df['LastName'].value_counts()
families = family_sizes[family_sizes >= 2].index

family_survival = titanic_df[titanic_df['LastName'].isin(families)].groupby('LastName').agg({
    'PassengerId': 'count',
    'Survived': ['sum', 'mean']
})
family_survival.columns = ['Family_Size', 'Survivors', 'Survival_Rate']
family_survival = family_survival.sort_values('Survival_Rate', ascending=False)
print("Top 10 families by survival rate:")
print(family_survival.head(10).round(3))

print("Building on previous steps:")
print("Cleaned data enables detailed grouping, feature-based analysis, and answering key business questions.")
print("We learned grouping, aggregation, transformation, filtering, and performance tips with pandas.")
