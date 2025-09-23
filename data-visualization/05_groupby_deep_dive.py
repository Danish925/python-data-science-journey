import pandas as pd
import numpy as np

print("=== DAY 5: GROUPBY DEEP DIVE ===")

# Load our cleaned data from Day 4
# (You can use any of the three CSV exports we created)
titanic_df = pd.read_csv('titanic_with_features.csv')

print("Dataset loaded successfully!")
print(f"Shape: {titanic_df.shape}")
print(f"Columns: {list(titanic_df.columns)}")



print("=== SECTION 1: UNDERSTANDING GROUPBY ===")

# First, let's see what groupby actually returns
grouped = titanic_df.groupby('Sex')
print(f"Type of groupby object: {type(grouped)}")

# This is a GroupBy object, not a DataFrame!
# To see the actual groups, we need to iterate or apply a function

print(f"Number of groups: {grouped.ngroups}")
print(f"Group sizes:")
print(grouped.size())



print("\n=== SECTION 2: BASIC GROUPBY OPERATIONS ===")

# Most common aggregations
print("Survival rate by gender:")
gender_survival = titanic_df.groupby('Sex')['Survived'].mean()
print(gender_survival)
print(f"Type: {type(gender_survival)}")  # This returns a Series

print("\nPassenger count by gender:")
gender_count = titanic_df.groupby('Sex').size()
print(gender_count)

print("\nMultiple statistics at once:")
gender_stats = titanic_df.groupby('Sex')['Age'].describe()
print(gender_stats)



print("\n=== SECTION 3: MULTIPLE COLUMN GROUPING ===")

# Group by multiple columns
print("Survival rate by Sex AND Passenger Class:")
multi_group = titanic_df.groupby(['Sex', 'Pclass'])['Survived'].mean()
print(multi_group)

print("\nThis creates a hierarchical index (MultiIndex)")
print(f"Index levels: {multi_group.index.names}")

# Convert to regular DataFrame for easier viewing
multi_df = multi_group.reset_index()
print("\nAs a regular DataFrame:")
print(multi_df)

# Alternative: unstack to create a pivot-like view
print("\nUnstacked view (like a pivot table):")
pivot_view = multi_group.unstack()
print(pivot_view)



print("\n=== SECTION 4: ADVANCED AGGREGATION ===")

# Single column, multiple functions
print("Age statistics by gender:")
age_stats = titanic_df.groupby('Sex')['Age'].agg(['mean', 'median', 'std', 'min', 'max'])
print(age_stats)

# Multiple columns, different functions for each
print("\nDifferent functions for different columns:")
complex_agg = titanic_df.groupby('Sex').agg({
    'Age': ['mean', 'median'],
    'Fare': ['mean', 'max'],
    'Survived': 'sum'  # Total survivors
})
print(complex_agg)

# Named aggregations (cleaner column names)
print("\nNamed aggregations:")
named_agg = titanic_df.groupby('Sex').agg(
    avg_age=('Age', 'mean'),
    median_age=('Age', 'median'),
    avg_fare=('Fare', 'mean'),
    total_survivors=('Survived', 'sum'),
    passenger_count=('PassengerId', 'count')
)
print(named_agg)



print("\n=== SECTION 5: CUSTOM FUNCTIONS WITH APPLY ===")

# Custom function to get age range in each group
def age_range(series):
    """Calculate the range (max - min) of ages"""
    if series.isna().all():  # Handle all-NaN case
        return np.nan
    return series.max() - series.min()

print("Age range by passenger class:")
age_ranges = titanic_df.groupby('Pclass')['Age'].apply(age_range)
print(age_ranges)

# More complex custom function
def survival_summary(group):
    """Create a custom summary for each group"""
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

print("\nCustom survival summary by passenger class:")
custom_summary = titanic_df.groupby('Pclass').apply(survival_summary)
print(custom_summary)



print("\n=== SECTION 6: TRANSFORM VS AGGREGATE ===")

# Aggregate: Reduces each group to a single value
print("Aggregate example - mean age by class:")
agg_result = titanic_df.groupby('Pclass')['Age'].mean()
print(f"Shape: {agg_result.shape}")
print(agg_result)

# Transform: Keeps the same shape as original DataFrame
print("\nTransform example - subtract group mean from each value:")
titanic_df['Age_minus_class_mean'] = titanic_df.groupby('Pclass')['Age'].transform(lambda x: x - x.mean())
print("First 10 rows showing original Age and Age minus class mean:")
print(titanic_df[['PassengerId', 'Pclass', 'Age', 'Age_minus_class_mean']].head(10))

print(f"Original DataFrame shape: {titanic_df.shape}")
print("Transform kept the same number of rows!")



print("\n=== SECTION 7: FILTERING GROUPS ===")

# Filter groups based on group characteristics
print("Only show passenger classes with more than 100 passengers:")
large_classes = titanic_df.groupby('Pclass').filter(lambda x: len(x) > 100)
print(f"Original shape: {titanic_df.shape}")
print(f"Filtered shape: {large_classes.shape}")
print("Passenger counts by class in filtered data:")
print(large_classes['Pclass'].value_counts().sort_index())

# Filter based on group statistics
print("\nOnly show groups where survival rate > 50%:")
high_survival = titanic_df.groupby('Sex').filter(lambda x: x['Survived'].mean() > 0.5)
print("Gender distribution in high-survival groups:")
print(f"{high_survival}")
print(high_survival['Sex'].value_counts())



print("\n=== SECTION 8: REAL-WORLD ANALYSIS ===")

# Question 1: Which passenger class had the highest survival rate?
print("1. Survival rate by passenger class:")
class_survival = titanic_df.groupby('Pclass')['Survived'].agg(['count', 'sum', 'mean'])
class_survival.columns = ['Total_Passengers', 'Survivors', 'Survival_Rate']
class_survival = class_survival.round(3)
print(class_survival)

highest_survival_class = class_survival['Survival_Rate'].idxmax()
print(f"Answer: Class {highest_survival_class} had the highest survival rate")

# Question 2: What was the average age of survivors vs non-survivors by gender?
print("\n2. Average age of survivors vs non-survivors by gender:")
age_by_survival = titanic_df.groupby(['Sex', 'Survived'])['Age'].mean().unstack()
age_by_survival.columns = ['Non_Survivors', 'Survivors']
print(age_by_survival.round(1))

# Question 3: Which title (Mr, Mrs, Miss, etc.) had the best survival chances?
print("\n3. Survival rate by title:")
title_survival = titanic_df.groupby('Title_simple')['Survived'].agg(['count', 'mean'])
title_survival.columns = ['Count', 'Survival_Rate']
title_survival = title_survival.sort_values('Survival_Rate', ascending=False)
print(title_survival.round(3))

# Question 4: How did family size affect survival?
print("\n4. Survival rate by family size:")
family_survival = titanic_df.groupby('FamilySize')['Survived'].agg(['count', 'mean'])
family_survival.columns = ['Count', 'Survival_Rate']
print(family_survival.round(3))



print("\n=== SECTION 9: ADVANCED TECHNIQUES ===")

# Multiple groupby operations in sequence
print("Complex analysis: Age groups by gender and class")
age_group_analysis = (titanic_df.groupby(['Sex', 'Pclass', 'AgeGroup']).agg({
                         'PassengerId': 'count',
                         'Survived': ['sum', 'mean'],
                         'Fare': 'mean'
                     })
                     .round(2))

# Flatten column names for easier reading
age_group_analysis.columns = ['_'.join(col).strip() for col in age_group_analysis.columns]
print("First 10 rows of complex analysis:")
print(age_group_analysis.head(10))

# Percentile calculations
print("\nFare percentiles by passenger class:")
fare_percentiles = titanic_df.groupby('Pclass')['Fare'].quantile([0.25, 0.5, 0.75]).unstack()
fare_percentiles.columns = ['25th_Percentile', 'Median', '75th_Percentile']
print(fare_percentiles.round(2))



print("\n=== SECTION 10: PERFORMANCE TIPS ===")

# Tip 1: Use categorical data for frequent grouping
print("Converting Sex to categorical for better performance:")
titanic_df['Sex_cat'] = titanic_df['Sex'].astype('category')
print(f"Memory usage - original: {titanic_df['Sex'].memory_usage(deep=True)} bytes")
print(f"Memory usage - categorical: {titanic_df['Sex_cat'].memory_usage(deep=True)} bytes")

# Tip 2: Use .agg() instead of multiple separate operations
print("\nCompare these approaches:")
print("Inefficient (multiple operations):") 
inefficient_start = pd.Timestamp.now()
mean_age = titanic_df.groupby('Pclass')['Age'].mean()
std_age = titanic_df.groupby('Pclass')['Age'].std()
min_age = titanic_df.groupby('Pclass')['Age'].min()
inefficient_time = pd.Timestamp.now() - inefficient_start

print("Efficient (single .agg() call):")
efficient_start = pd.Timestamp.now()
all_stats = titanic_df.groupby('Pclass')['Age'].agg(['mean', 'std', 'min'])
efficient_time = pd.Timestamp.now() - efficient_start

print(f"Inefficient approach took: {inefficient_time}")
print(f"Efficient approach took: {efficient_time}")



print("\n=== DAY 5 PRACTICE QUESTIONS ===")

# 1. Find the oldest and youngest passengers
print("1. Oldest and youngest passengers:")
age_extremes = titanic_df.groupby('Sex')['Age'].agg(['min', 'max'])
print(age_extremes)

oldest_passenger = titanic_df.loc[titanic_df['Age'].idxmax()]
youngest_passenger = titanic_df.loc[titanic_df['Age'].idxmin()]
print(f"Oldest: {oldest_passenger['Name']}, Age: {oldest_passenger['Age']}")
print(f"Youngest: {youngest_passenger['Name']}, Age: {youngest_passenger['Age']}")

# 2. Calculate average fare by passenger class
print("\n2. Average fare by passenger class:")
avg_fare_by_class = titanic_df.groupby('Pclass')['Fare'].mean()
print(avg_fare_by_class.round(2))

# 3. Find families (same last name) and see their survival rates
print("\n3. Family survival analysis:")
# Extract last name from full name
titanic_df['LastName'] = titanic_df['Name'].str.extract(r'([^,]+),')

# Find families with 2+ members
family_sizes = titanic_df['LastName'].value_counts()
families = family_sizes[family_sizes >= 2].index

family_survival = (titanic_df[titanic_df['LastName'].isin(families)]
                  .groupby('LastName')
                  .agg({
                      'PassengerId': 'count',
                      'Survived': ['sum', 'mean']
                  }))

family_survival.columns = ['Family_Size', 'Survivors', 'Survival_Rate']
family_survival = family_survival.sort_values('Survival_Rate', ascending=False)
print("Top 10 families by survival rate:")
print(family_survival.head(10).round(3))



print("\n=== SECTION 11: BUILDING ON DAY 4 ===")

print("Day 4 vs Day 5 - Evolution of our analysis:")
print("\nDay 4: We cleaned data and created features")
print("- Filled missing values")
print("- Created AgeGroup, FamilySize, etc.")
print("- Basic feature engineering")

print("\nDay 5: We're analyzing patterns in the cleaned data")
print("- Grouping by the features we created")
print("- Finding statistical relationships")
print("- Answering business questions")

# Show how our Day 4 features enable Day 5 analysis
print("\nUsing Day 4 features for Day 5 analysis:")
feature_analysis = titanic_df.groupby(['AgeGroup', 'FamilySize']).agg({
    'Survived': ['count', 'sum', 'mean']
}).round(3)
print("Sample of feature-based analysis:")
print(feature_analysis.head())



print("\n=== DAY 5 SUMMARY ===")

key_findings = {
    'Gender': f"Female survival rate: {titanic_df[titanic_df['Sex']=='female']['Survived'].mean():.1%}, Male: {titanic_df[titanic_df['Sex']=='male']['Survived'].mean():.1%}",
    'Class': f"1st class survival: {titanic_df[titanic_df['Pclass']==1]['Survived'].mean():.1%}",
    'Age': f"Children (<18) survival: {titanic_df[titanic_df['Age']<18]['Survived'].mean():.1%}",
    'Family': f"Optimal family size for survival: {titanic_df.groupby('FamilySize')['Survived'].mean().idxmax()} people"
}

print("Key findings from our analysis:")
for category, finding in key_findings.items():
    print(f"- {category}: {finding}")

print(f"\nToday we learned:")
print("1. groupby() splits data into groups based on column values")
print("2. .agg() allows multiple aggregation functions at once")
print("3. .apply() lets us use custom functions on groups")
print("4. .transform() keeps the original DataFrame shape")
print("5. .filter() removes entire groups based on conditions")


