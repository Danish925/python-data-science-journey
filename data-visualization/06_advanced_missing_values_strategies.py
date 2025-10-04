print("=== ADVANCED MISSING VALUE STRATEGIES ===")
print("Session 1: Pure pandas missing data mastery")
print("Date: Monday, October 20, 2025")


# Import pandas and numpy only (no external libraries)
import pandas as pd



# Set pandas options for better output
pd.set_option('display.max_columns', None)
pd.set_option('display.precision', 2)


print("\n🔧 Environment setup complete!")


print("\n📊 1. Dataset Loading and Initial Inspection")


# Load the Titanic dataset
# url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
# titanic_df = pd.read_csv(url)
titanic_df = pd.read_csv('titanic_data.csv')


print(f"✅ Dataset loaded successfully!")
print(f"Shape: {titanic_df.shape[0]} rows × {titanic_df.shape[1]} columns")


# First look at the data
print("\n📋 First 5 rows:")
print(titanic_df.head())


print("\n📋 Column info:")
print(titanic_df.info())


print("\n📋 Data types:")
print(titanic_df.dtypes)



print("\n📊 2. Missing Data Pattern Analysis")


print("1. Missing Values Count:")
missing_summary = titanic_df.isnull().sum()
print(missing_summary)


print("\n2. Missing Values Percentage:")
missing_percentage = (titanic_df.isnull().sum() / len(titanic_df) * 100).round(2)
missing_analysis = pd.DataFrame({
    'Missing_Count': missing_summary,
    'Missing_Percentage': missing_percentage
}).sort_values('Missing_Percentage', ascending=False)


print(missing_analysis[missing_analysis['Missing_Count'] > 0])


print("\n3. Rows with Missing Values Analysis:")
# Count rows with any missing values
rows_with_missing = titanic_df.isnull().any(axis=1).sum()
rows_complete = len(titanic_df) - rows_with_missing


print(f"Rows with missing values: {rows_with_missing} ({rows_with_missing/len(titanic_df)*100:.1f}%)")
print(f"Complete rows: {rows_complete} ({rows_complete/len(titanic_df)*100:.1f}%)")


# Count completely empty rows
completely_empty = titanic_df.isnull().all(axis=1).sum()
print(f"Completely empty rows: {completely_empty}")



print("\n📊 3. Missing Data Patterns by Passenger Class")


# Analyze missing data patterns by passenger class
print("Missing data by Passenger Class:")
for col in ['Age', 'Cabin', 'Embarked']:
    if titanic_df[col].isnull().sum() > 0:
        print(f"\n{col} missing by class:")
        missing_by_class = titanic_df.groupby('Pclass')[col].apply(lambda x: x.isnull().sum())
        missing_pct_by_class = titanic_df.groupby('Pclass')[col].apply(lambda x: x.isnull().mean() * 100)
        
        class_analysis = pd.DataFrame({
            'Missing_Count': missing_by_class,
            'Missing_Percentage': missing_pct_by_class.round(1)
        })
        print(class_analysis)


print("\n🔍 Key Insight: Different missing patterns by passenger class reveal potential data collection biases!")



print("\n📊 4. Group-Based Imputation using .transform()")


# This is a powerful pandas technique!
print("🎯 New Syntax: df.groupby(['col1', 'col2'])['target'].transform('median')")
print("This creates a Series with the same index as original, filled with group-specific values")


# Strategy 1: Fill missing ages with median age by passenger class and gender
print("\nStep 1: Analyzing age patterns by class and gender")
age_stats = titanic_df.groupby(['Pclass', 'Sex'])['Age'].agg(['count', 'mean', 'median']).round(1)
print("Age statistics by Pclass and Sex:")
print(age_stats)


print("\nStep 2: Applying group-based imputation")
# Create group-based median ages
age_by_group = titanic_df.groupby(['Pclass', 'Sex'])['Age'].transform('median')


# Show what transform does
print("\nBefore imputation:")
sample_missing = titanic_df[titanic_df['Age'].isnull()].head(3)[['PassengerId', 'Pclass', 'Sex', 'Age']]
print(sample_missing)


print("\nGroup median values for these passengers:")
for idx in sample_missing.index:
    pclass = titanic_df.loc[idx, 'Pclass'] 
    sex = titanic_df.loc[idx, 'Sex']
    group_median = age_by_group.loc[idx]
    print(f"PassengerId {titanic_df.loc[idx, 'PassengerId']}: Class {pclass}, {sex} → median age = {group_median}")


# Apply the imputation
titanic_df['Age_group_filled'] = titanic_df['Age'].fillna(age_by_group)


print(f"\n✅ Imputation complete!")
print(f"Missing ages before: {titanic_df['Age'].isnull().sum()}")
print(f"Missing ages after: {titanic_df['Age_group_filled'].isnull().sum()}")




print("\n📊 5. Forward Fill and Backward Fill Methods")


print("🎯 New Syntax: df['column'].fillna(method='ffill') and fillna(method='bfill')")
print("These methods fill missing values based on adjacent non-null values")


# Work with Embarked column (only 2 missing values)
print(f"\nEmbarked column missing values: {titanic_df['Embarked'].isnull().sum()}")


# Sort by PassengerId to simulate ordered data
titanic_sorted = titanic_df.sort_values('PassengerId').copy()


# Show the missing Embarked values in context
embarked_missing_idx = titanic_sorted[titanic_sorted['Embarked'].isnull()].index
print("\nMissing Embarked values in context:")
for idx in embarked_missing_idx:
    start_idx = max(0, idx-2)
    end_idx = min(len(titanic_sorted), idx+3)
    context = titanic_sorted.iloc[start_idx:end_idx][['PassengerId', 'Pclass', 'Embarked']]
    print(f"\nContext around PassengerId {titanic_sorted.iloc[idx]['PassengerId']}:")
    print(context)


# Apply forward fill
titanic_sorted['Embarked_ffill'] = titanic_sorted['Embarked'].fillna(method='ffill')


# Apply backward fill  
titanic_sorted['Embarked_bfill'] = titanic_sorted['Embarked'].fillna(method='bfill')


print("\n📋 Forward/Backward Fill Results:")
fill_comparison = pd.DataFrame({
    'Original_Missing': titanic_sorted['Embarked'].isnull().sum(),
    'After_Forward_Fill': titanic_sorted['Embarked_ffill'].isnull().sum(),
    'After_Backward_Fill': titanic_sorted['Embarked_bfill'].isnull().sum()
}, index=[0])
print(fill_comparison)


# Show what happened to the missing values
print("\nWhat values were filled:")
for idx in embarked_missing_idx:
    original = titanic_sorted.iloc[idx]['Embarked']
    ffill = titanic_sorted.iloc[idx]['Embarked_ffill'] 
    bfill = titanic_sorted.iloc[idx]['Embarked_bfill']
    pid = titanic_sorted.iloc[idx]['PassengerId']
    print(f"PassengerId {pid}: Original={original}, FFill={ffill}, BFill={bfill}")




print("\n📊 6. Conditional Filling Strategies")


print("🎯 Advanced Technique: Custom filling logic using pandas operations")


# Strategy: Fill missing Embarked based on most common port for each class
print("\nStep 1: Find most common embarkation port by passenger class")
embarked_mode_by_class = titanic_df.groupby('Pclass')['Embarked'].apply(
    lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'S'
)
print("Most common Embarked port by class:")
print(embarked_mode_by_class)


# Show the distribution to understand the logic
print("\nEmbarked distribution by class:")
embarked_crosstab = pd.crosstab(titanic_df['Pclass'], titanic_df['Embarked'], margins=True)
print(embarked_crosstab)


# Method 1: Using apply() with custom function
def fill_embarked_by_class(row):
    if pd.isna(row['Embarked']):
        return embarked_mode_by_class[row['Pclass']]
    return row['Embarked']


titanic_df['Embarked_filled_v1'] = titanic_df.apply(fill_embarked_by_class, axis=1)


# Method 2: Using pandas map() - more efficient
# First create mapping dictionary
class_to_embarked = embarked_mode_by_class.to_dict()
print(f"\nClass to Embarked mapping: {class_to_embarked}")


# Fill missing values using pandas where()
titanic_df['Embarked_filled_v2'] = titanic_df['Embarked'].fillna(
    titanic_df['Pclass'].map(class_to_embarked)
)


# Verify both methods give same result
methods_match = (titanic_df['Embarked_filled_v1'] == titanic_df['Embarked_filled_v2']).all()
print(f"\n✅ Both filling methods match: {methods_match}")


print(f"Missing Embarked values after conditional filling: {titanic_df['Embarked_filled_v2'].isnull().sum()}")




print("\n" + "="*60)
print("📚 SUMMARY: Advanced Missing Value Strategies")
print("="*60)


print("\n✅ SKILLS MASTERED TODAY:")
print("1. Missing data pattern analysis with pandas")
print("2. Group-based imputation using .groupby().transform()")
print("3. Forward fill and backward fill methods")
print("4. Conditional filling with custom logic")
print("5. Strategy comparison and evaluation")


print("\n🎯 NEW PANDAS SYNTAX LEARNED:")
print("• df.groupby(['col1', 'col2'])['target'].transform('median')")
print("• df['column'].fillna(method='ffill')  # Forward fill")
print("• df['column'].fillna(method='bfill')  # Backward fill")
print("• df.apply(custom_function, axis=1)  # Row-wise operations")
print("• df['col'].map(dictionary)  # Value mapping")


print("\n🔥 POWER TECHNIQUE OF THE DAY:")
print("GROUP-BASED IMPUTATION with .transform()")
print("→ Fills missing values with group-specific statistics")
print("→ Preserves relationships between variables") 
print("→ More sophisticated than global mean/median filling")



print("\n" + "✓ Session 1 completed! Advanced missing value strategies mastered." + "\n")
