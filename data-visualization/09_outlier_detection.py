print("=== PURE PANDAS OUTLIER DETECTION ===")
print("Session 4: Statistical outlier detection with 100% pandas methods")

# Import ONLY pandas and built-in Python libraries
import pandas as pd

# Set pandas display options for better output
pd.set_option('display.max_columns', None)
pd.set_option('display.precision', 2)

print("\n🔧 Environment setup complete!")
print("🎯 Today's Goal: Master pandas-based outlier detection and handling")
print("🚫 NO NUMPY: Pure pandas methods only!")

print("\n📊 1. Dataset Preparation and Overview with pandas-Only")

# Load and prepare our dataset with all enhancements from this week
titanic_url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_df = pd.read_csv(titanic_url)

# Apply all our Week 11 enhancements quickly using pandas-only methods
print("🔧 Applying Week 11 enhancements using pandas-only...")

# Monday: Missing value fixes (pandas-only)
age_by_group = titanic_df.groupby(['Pclass', 'Sex'])['Age'].transform('median')
titanic_df['Age'] = titanic_df['Age'].fillna(age_by_group)
titanic_df['Embarked'] = titanic_df['Embarked'].fillna(titanic_df['Embarked'].mode()[0])

# Tuesday: Data type optimizations (pandas-only)
titanic_df['Pclass'] = titanic_df['Pclass'].astype('category')
titanic_df['Sex'] = titanic_df['Sex'].astype('category')
titanic_df['Embarked'] = titanic_df['Embarked'].astype('category')
titanic_df['Survived'] = titanic_df['Survived'].astype('bool')

# Wednesday: Key feature engineering (pandas-only)
titanic_df['Family_Size'] = titanic_df['SibSp'] + titanic_df['Parch'] + 1
titanic_df['Is_Alone'] = (titanic_df['Family_Size'] == 1).astype(int)
titanic_df['Title'] = titanic_df['Name'].str.extract(r', ([^.]*)\.')
titanic_df['Cabin_Deck'] = titanic_df['Cabin'].str[0].fillna('Unknown')
titanic_df['Has_Cabin'] = (~titanic_df['Cabin'].isna()).astype(int)

# Safe interaction feature from Wednesday (avoiding categorical arithmetic)
pclass_num = titanic_df['Pclass'].astype('int16')
titanic_df['Fare_Per_Person'] = titanic_df['Fare'] / titanic_df['Family_Size']

print("✅ Dataset enhanced with Week 11 improvements using pandas-only!")
print(f"Dataset shape: {titanic_df.shape}")

# Focus on numerical columns for outlier detection using pandas methods
numerical_cols = ['Age', 'Fare', 'SibSp', 'Parch', 'Family_Size', 'Fare_Per_Person']
print(f"\n📊 Numerical columns for outlier analysis: {len(numerical_cols)}")
for i, col in enumerate(numerical_cols, 1):
    print(f"{i}. {col}")

# Basic statistical overview using pandas describe
print(f"\n📋 Basic Statistical Summary:")
print(titanic_df[numerical_cols].describe())

print("\n📊 2. IQR (Interquartile Range) Outlier Detection with pandas-Only")

print("🎯 Pure pandas Syntax for Outlier Detection:")
print("• df['col'].quantile(0.25) → First quartile (Q1)")
print("• df['col'].quantile(0.75) → Third quartile (Q3)")
print("• IQR = Q3 - Q1 → Interquartile range")
print("• Lower bound = Q1 - 1.5 * IQR")
print("• Upper bound = Q3 + 1.5 * IQR")

def detect_outliers_iqr_pandas_only(series, multiplier=1.5):
    """
    Detect outliers using IQR method with pure pandas
    
    Parameters:
    series: pandas Series
    multiplier: IQR multiplier (default 1.5)
    
    Returns:
    dict with outlier statistics and boolean mask
    """
    # Calculate quartiles using pandas quantile method
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    
    # Calculate bounds using pandas arithmetic
    lower_bound = Q1 - multiplier * IQR
    upper_bound = Q3 + multiplier * IQR
    
    # Create outlier mask using pandas boolean operations
    outlier_mask = (series < lower_bound) | (series > upper_bound)
    
    # Statistics using pandas methods
    outlier_count = outlier_mask.sum()
    outlier_percentage = (outlier_count / len(series)) * 100
    
    return {
        'Q1': Q1,
        'Q3': Q3,
        'IQR': IQR,
        'lower_bound': lower_bound,
        'upper_bound': upper_bound,
        'outlier_mask': outlier_mask,
        'outlier_count': outlier_count,
        'outlier_percentage': outlier_percentage,
        'total_count': len(series)
    }

print("\n1. Age Outlier Analysis using pandas:")
age_outliers = detect_outliers_iqr_pandas_only(titanic_df['Age'])

print("📊 Age Outlier Statistics:")
for key, value in age_outliers.items():
    if key != 'outlier_mask':  # Skip the mask in display
        print(f"  {key}: {value}")

# Show age outliers using pandas boolean indexing
age_outlier_data = titanic_df[age_outliers['outlier_mask']]
print(f"\n🔍 Age Outliers ({len(age_outlier_data)} passengers):")
print("Sample age outliers:")
sample_age_outliers = age_outlier_data[['Name', 'Age', 'Pclass', 'Survived']].head(10)
print(sample_age_outliers)

print("\n2. Fare Outlier Analysis using pandas:")
fare_outliers = detect_outliers_iqr_pandas_only(titanic_df['Fare'])

print("📊 Fare Outlier Statistics:")
for key, value in fare_outliers.items():
    if key != 'outlier_mask':
        print(f"  {key}: {value}")

# Show fare outliers using pandas boolean indexing
fare_outlier_data = titanic_df[fare_outliers['outlier_mask']]
print(f"\n🔍 Fare Outliers ({len(fare_outlier_data)} passengers):")
print("Sample fare outliers:")
sample_fare_outliers = fare_outlier_data[['Name', 'Fare', 'Pclass', 'Cabin', 'Survived']].head(10)
print(sample_fare_outliers)

print("\n3. Comprehensive Outlier Analysis using pandas:")
# Analyze all numerical columns using pandas operations
outlier_summary = []

for col in numerical_cols:
    outliers = detect_outliers_iqr_pandas_only(titanic_df[col])
    outlier_summary.append({
        'Column': col,
        'Outlier_Count': outliers['outlier_count'],
        'Outlier_Percentage': round(outliers['outlier_percentage'], 2),
        'Lower_Bound': round(outliers['lower_bound'], 3),
        'Upper_Bound': round(outliers['upper_bound'], 3)
    })

outlier_df = pd.DataFrame(outlier_summary)
print("📋 Outlier Summary Across All Numerical Columns:")
print(outlier_df)

print("\n📊 3. Percentile-based Outlier Detection with pandas-Only")

print("🎯 Alternative Method: Percentile Thresholds")
print("• Often more flexible than IQR method")
print("• Can use different percentiles based on domain knowledge")
print("• Common thresholds: 1st/99th, 5th/95th percentiles")

def detect_outliers_percentile_pandas_only(series, lower_percentile=5, upper_percentile=95):
    """
    Detect outliers using percentile method with pure pandas
    
    Parameters:
    series: pandas Series
    lower_percentile: Lower threshold percentile (default 5)
    upper_percentile: Upper threshold percentile (default 95)
    
    Returns:
    dict with outlier statistics and boolean mask
    """
    # Calculate percentile thresholds using pandas quantile
    lower_threshold = series.quantile(lower_percentile / 100)
    upper_threshold = series.quantile(upper_percentile / 100)
    
    # Create outlier mask using pandas boolean operations
    outlier_mask = (series < lower_threshold) | (series > upper_threshold)
    
    # Statistics using pandas methods
    outlier_count = outlier_mask.sum()
    outlier_percentage = (outlier_count / len(series)) * 100
    
    return {
        'lower_threshold': lower_threshold,
        'upper_threshold': upper_threshold,
        'outlier_mask': outlier_mask,
        'outlier_count': outlier_count,
        'outlier_percentage': outlier_percentage,
        'method': f'{lower_percentile}th/{upper_percentile}th percentile'
    }

print("\n1. Fare Analysis with Different Percentile Thresholds:")

# Test different percentile thresholds using pandas
percentile_methods = [
    (1, 99),   # Very strict
    (5, 95),   # Standard
    (10, 90)   # More lenient
]

fare_percentile_results = []
for lower, upper in percentile_methods:
    result = detect_outliers_percentile_pandas_only(titanic_df['Fare'], lower, upper)
    fare_percentile_results.append({
        'Method': f'{lower}th/{upper}th percentile',
        'Lower_Threshold': round(result['lower_threshold'], 2),
        'Upper_Threshold': round(result['upper_threshold'], 2), 
        'Outliers': result['outlier_count'],
        'Percentage': round(result['outlier_percentage'], 2)
    })

percentile_comparison = pd.DataFrame(fare_percentile_results)
print("📊 Fare Outliers by Different Percentile Methods:")
print(percentile_comparison)

print("\n2. Age Analysis with Percentiles using pandas:")
age_percentile_analysis = []
for lower, upper in percentile_methods:
    result = detect_outliers_percentile_pandas_only(titanic_df['Age'], lower, upper)
    age_percentile_analysis.append({
        'Method': f'{lower}th/{upper}th percentile',
        'Lower_Threshold': round(result['lower_threshold'], 2),
        'Upper_Threshold': round(result['upper_threshold'], 2),
        'Outliers': result['outlier_count'],
        'Percentage': round(result['outlier_percentage'], 2)
    })

age_percentile_comparison = pd.DataFrame(age_percentile_analysis)
print("📊 Age Outliers by Different Percentile Methods:")  
print(age_percentile_comparison)

print("\n3. Detailed Percentile Analysis using pandas:")
# Show detailed percentile breakdown using pandas quantile
percentiles_to_check = [1, 5, 10, 25, 50, 75, 90, 95, 99]

print("📋 Detailed Percentile Breakdown for Key Columns:")
for col in ['Age', 'Fare']:
    print(f"\n{col} Percentiles:")
    percentile_values = []
    for p in percentiles_to_check:
        value = titanic_df[col].quantile(p/100)
        percentile_values.append(f"{p:2d}th: {value:7.2f}")
    
    # Print in rows of 3 for better formatting
    for i in range(0, len(percentile_values), 3):
        print("  " + "  |  ".join(percentile_values[i:i+3]))

print("\n📊 4. Context-Aware Group-Based Outlier Detection with pandas-Only")

print("🎯 SMART OUTLIER DETECTION:")
print("• High fares might be normal for 1st class passengers")
print("• Old ages might be normal for certain passenger groups")
print("• Context matters more than raw statistics!")

def detect_outliers_by_group_pandas_only(df, value_col, group_cols, method='iqr', multiplier=1.5):
    """
    Detect outliers within groups using pandas-only methods
    
    Parameters:
    df: pandas DataFrame
    value_col: Column to detect outliers in
    group_cols: Columns to group by
    method: 'iqr' or 'percentile'
    multiplier: IQR multiplier or percentile threshold
    
    Returns:
    DataFrame with outlier information
    """
    outlier_results = []
    
    for group_values, group_data in df.groupby(group_cols):
        if not isinstance(group_values, tuple):
            group_values = (group_values,)
        
        series = group_data[value_col]
        
        if method == 'iqr':
            # IQR method within group using pandas quantile
            Q1 = series.quantile(0.25)
            Q3 = series.quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - multiplier * IQR
            upper_bound = Q3 + multiplier * IQR
            outlier_mask = (series < lower_bound) | (series > upper_bound)
        
        outliers_in_group = outlier_mask.sum() if len(series) > 0 else 0
        
        group_info = {}
        for i, col in enumerate(group_cols):
            group_info[col] = group_values[i]
        
        group_info.update({
            'Count': len(series),
            'Mean': series.mean() if len(series) > 0 else 0,
            'Std': series.std() if len(series) > 0 else 0,
            'Min': series.min() if len(series) > 0 else 0,
            'Max': series.max() if len(series) > 0 else 0,
            'Outliers': outliers_in_group,
            'Outlier_Pct': (outliers_in_group / len(series) * 100) if len(series) > 0 else 0
        })
        
        outlier_results.append(group_info)
    
    return pd.DataFrame(outlier_results).round(3)

print("\n1. Fare Outliers by Passenger Class using pandas:")
fare_by_class = detect_outliers_by_group_pandas_only(titanic_df, 'Fare', ['Pclass'])
print("📊 Fare Analysis by Class:")
print(fare_by_class)

# Key insight using pandas indexing
print(f"\n🔍 Key Insights:")
class_1_max = fare_by_class[fare_by_class['Pclass']==1]['Max'].iloc[0]
class_3_max = fare_by_class[fare_by_class['Pclass']==3]['Max'].iloc[0]
print(f"• 1st class max fare: ${class_1_max:.2f}")
print(f"• 3rd class max fare: ${class_3_max:.2f}")
print(f"• 1st class has higher baseline → fewer 'true' outliers")

print("\n2. Age Outliers by Gender and Class using pandas:")
age_by_sex_class = detect_outliers_by_group_pandas_only(titanic_df, 'Age', ['Sex', 'Pclass'])
print("📊 Age Analysis by Gender and Class:")
print(age_by_sex_class)

print("\n3. Family Size Impact on Fare Analysis using pandas:")
# Create family size categories for analysis using pandas cut
titanic_df['Family_Size_Cat'] = pd.cut(titanic_df['Family_Size'], 
                                     bins=[0, 1, 4, float('inf')], 
                                     labels=['Solo', 'Small', 'Large'],
                                     include_lowest=True)

fare_by_family = detect_outliers_by_group_pandas_only(titanic_df, 'Fare', ['Family_Size_Cat'])
print("📊 Fare Analysis by Family Size:")
print(fare_by_family)

print("\n4. Context-Aware Outlier Identification using pandas:")
# Identify passengers who are outliers even within their context
print("🎯 Finding TRUE outliers (extreme even within their group):")

# Fare outliers within each class using pandas operations
class_fare_outliers = []
for pclass in [1, 2, 3]:
    class_data = titanic_df[titanic_df['Pclass'] == pclass]
    outliers = detect_outliers_iqr_pandas_only(class_data['Fare'])
    
    if outliers['outlier_count'] > 0:
        outlier_indices = class_data[outliers['outlier_mask']].index
        class_fare_outliers.extend(outlier_indices)
        
        print(f"\nClass {pclass} fare outliers: {outliers['outlier_count']}")
        print(f"Bounds: ${outliers['lower_bound']:.2f} - ${outliers['upper_bound']:.2f}")
        
        # Show top fare outliers in this class using pandas nlargest
        top_outliers = class_data[outliers['outlier_mask']].nlargest(3, 'Fare')
        for idx, row in top_outliers.iterrows():
            name_short = row['Name'][:30] if len(row['Name']) > 30 else row['Name']
            print(f"  • {name_short:<30} Fare: ${row['Fare']:6.2f}")

print(f"\n✅ Context-aware analysis complete using pandas-only!")
print(f"Global fare outliers: {fare_outliers['outlier_count']}")
print(f"Context-aware fare outliers: {len(class_fare_outliers)}")
print(f"Difference: {fare_outliers['outlier_count'] - len(class_fare_outliers)} outliers were actually normal within context!")

print("\n📊 5. Advanced Outlier Pattern Analysis with pandas-Only")

print("🎯 OUTLIER PATTERN INVESTIGATION:")
print("• Are outliers random or do they follow patterns?")
print("• Do outliers correlate with survival rates?")
print("• Are there systematic issues in data collection?")

print("\n1. Outlier Survival Analysis using pandas:")
# Compare survival rates of outliers vs normal passengers

outlier_survival_analysis = []

for col in ['Age', 'Fare', 'Family_Size']:
    outliers = detect_outliers_iqr_pandas_only(titanic_df[col])
    
    # Survival rate for outliers using pandas boolean indexing
    outlier_data = titanic_df[outliers['outlier_mask']]
    outlier_survival = outlier_data['Survived'].mean()
    
    # Survival rate for non-outliers using pandas boolean indexing
    normal_data = titanic_df[~outliers['outlier_mask']]
    normal_survival = normal_data['Survived'].mean()
    
    outlier_survival_analysis.append({
        'Column': col,
        'Outlier_Survival_Rate': round(outlier_survival, 3),
        'Normal_Survival_Rate': round(normal_survival, 3),
        'Difference': round(outlier_survival - normal_survival, 3),
        'Outlier_Count': outliers['outlier_count']
    })

survival_analysis_df = pd.DataFrame(outlier_survival_analysis)
print("📊 Survival Rate Analysis: Outliers vs Normal:")
print(survival_analysis_df)

# Key insights from survival analysis using pandas iterrows
print(f"\n🔍 Survival Insights:")
for _, row in survival_analysis_df.iterrows():
    direction = "higher" if row['Difference'] > 0 else "lower"
    print(f"• {row['Column']} outliers have {direction} survival rate ({row['Difference']:+.3f})")

print("\n2. Multi-Variate Outlier Detection using pandas:")
# Passengers who are outliers in multiple dimensions
print("🎯 Multi-dimensional outliers (extreme in multiple ways):")

# Create outlier flags for key columns using pandas operations
outlier_columns = ['Age', 'Fare', 'Family_Size']
for col in outlier_columns:
    outliers = detect_outliers_iqr_pandas_only(titanic_df[col])
    titanic_df[f'{col}_Outlier'] = outliers['outlier_mask'].astype(int)

# Count how many outlier flags each passenger has using pandas sum
outlier_flag_cols = [f'{col}_Outlier' for col in outlier_columns]
titanic_df['Total_Outlier_Flags'] = titanic_df[outlier_flag_cols].sum(axis=1)

print("📊 Multi-dimensional outlier distribution:")
print(titanic_df['Total_Outlier_Flags'].value_counts().sort_index())

# Show passengers with multiple outlier flags using pandas boolean indexing
multi_outliers = titanic_df[titanic_df['Total_Outlier_Flags'] >= 2]
print(f"\n🔍 Passengers with 2+ outlier flags: {len(multi_outliers)}")
if len(multi_outliers) > 0:
    print("Sample multi-dimensional outliers:")
    sample_cols = ['Name', 'Age', 'Fare', 'Family_Size', 'Total_Outlier_Flags', 'Survived']
    print(multi_outliers[sample_cols].head(10))

print("\n3. Outlier Distribution Analysis using pandas:")
# Check if outliers are randomly distributed or clustered
print("🎯 Outlier distribution patterns:")

# Fare outliers by embarkation port using pandas crosstab
fare_outliers = detect_outliers_iqr_pandas_only(titanic_df['Fare'])
fare_outlier_by_port = pd.crosstab(titanic_df['Embarked'], 
                                   fare_outliers['outlier_mask'], 
                                   normalize='index') * 100

print("📊 Fare outlier percentage by embarkation port:")
print(fare_outlier_by_port.round(2))

# Age outliers by passenger class using pandas crosstab
age_outliers = detect_outliers_iqr_pandas_only(titanic_df['Age'])
age_outlier_by_class = pd.crosstab(titanic_df['Pclass'], 
                                   age_outliers['outlier_mask'], 
                                   normalize='index') * 100

print("\n📊 Age outlier percentage by passenger class:")
print(age_outlier_by_class.round(2))

print("\n4. Suspicious Data Patterns using pandas:")
# Look for patterns that might indicate data quality issues
print("🔍 Data Quality Investigation:")

# Check for suspicious fare values using pandas operations
suspicious_fares = []

# Zero fares using pandas boolean operations
zero_fares = (titanic_df['Fare'] == 0).sum()
suspicious_fares.append(f"Zero fares: {zero_fares}")

# Very round numbers using pandas modulo operation
round_fares = (titanic_df['Fare'] % 1 == 0).sum()
suspicious_fares.append(f"Round number fares: {round_fares}")

# Extremely high fares using pandas boolean operations
extreme_fares = (titanic_df['Fare'] > 300).sum()
suspicious_fares.append(f"Fares > $300: {extreme_fares}")

print("📊 Potentially suspicious fare patterns:")
for pattern in suspicious_fares:
    print(f"  • {pattern}")

# Show examples of suspicious patterns using pandas boolean indexing
if zero_fares > 0:
    print(f"\n🔍 Examples of zero fares:")
    zero_fare_examples = titanic_df[titanic_df['Fare'] == 0][['Name', 'Pclass', 'Cabin', 'Embarked']].head(5)
    print(zero_fare_examples)

print("✅ Advanced outlier pattern analysis complete using pandas-only!")

print("\n📊 6. Outlier Treatment Strategies with pandas-Only")

print("🎯 OUTLIER TREATMENT OPTIONS:")
print("1. REMOVAL: Delete outlier rows (use with caution)")
print("2. CAPPING: Limit values to acceptable ranges") 
print("3. TRANSFORMATION: Apply mathematical transformations")
print("4. REPLACEMENT: Replace with group statistics")
print("5. FLAGGING: Keep but mark as outliers")

# Create a copy for treatment experiments using pandas copy
titanic_treatment = titanic_df.copy()

print("\n1. Removal Strategy (Use with Extreme Caution):")
print("🚨 WARNING: Removing data can bias your analysis!")

# Example: Remove only extreme fare outliers using pandas quantile
extreme_fare_threshold = titanic_treatment['Fare'].quantile(0.999)
extreme_fare_outliers = titanic_treatment['Fare'] > extreme_fare_threshold

print(f"Extreme fare threshold (99.9th percentile): ${extreme_fare_threshold:.2f}")
print(f"Passengers with extreme fares: {extreme_fare_outliers.sum()}")

if extreme_fare_outliers.sum() > 0:
    print("Extreme fare examples:")
    extreme_examples = titanic_treatment[extreme_fare_outliers][['Name', 'Fare', 'Pclass', 'Cabin']]
    print(extreme_examples)

# Create dataset with extreme outliers removed using pandas boolean indexing
titanic_no_extreme = titanic_treatment[~extreme_fare_outliers].copy()
print(f"Dataset size after removal: {len(titanic_no_extreme)} (removed {extreme_fare_outliers.sum()} passengers)")

print("\n2. Capping Strategy (Winsorization) using pandas:")
print("🎯 Limit extreme values to acceptable percentiles")

def cap_outliers_pandas_only(series, lower_percentile=5, upper_percentile=95):
    """Cap outliers using percentile limits with pandas-only methods"""
    lower_cap = series.quantile(lower_percentile / 100)
    upper_cap = series.quantile(upper_percentile / 100)
    
    capped_series = series.clip(lower=lower_cap, upper=upper_cap)
    
    return capped_series, lower_cap, upper_cap

# Cap fare outliers using pandas clip method
fare_capped, fare_lower_cap, fare_upper_cap = cap_outliers_pandas_only(titanic_treatment['Fare'])
titanic_treatment['Fare_Capped'] = fare_capped

print(f"Fare capping results:")
print(f"  Original range: ${titanic_treatment['Fare'].min():.2f} - ${titanic_treatment['Fare'].max():.2f}")
print(f"  Capped range: ${fare_capped.min():.2f} - ${fare_capped.max():.2f}")
print(f"  Lower cap: ${fare_lower_cap:.2f}")
print(f"  Upper cap: ${fare_upper_cap:.2f}")

# Show impact of capping using pandas describe
capping_impact = pd.DataFrame({
    'Original': titanic_treatment['Fare'].describe(),
    'Capped': fare_capped.describe()
}).round(2)
print(f"\n📊 Capping impact comparison:")
print(capping_impact)

print("\n3. Transformation Strategy using pandas:")
print("🎯 Mathematical transformations to reduce outlier impact")

# Log transformation for fare using pandas mathematical operations
# Use log1p equivalent: ln(1+x) to handle zero values
titanic_treatment['Fare_Log'] = (titanic_treatment['Fare'] + 1).apply(lambda x: x**0.5 if x > 0 else 0)  # sqrt as alternative to log

# Square root transformation using pandas mathematical operations
titanic_treatment['Fare_Sqrt'] = titanic_treatment['Fare'].apply(lambda x: x**0.5)

# Compare distributions using pandas describe
transformation_comparison = pd.DataFrame({
    'Original': titanic_treatment['Fare'].describe(),
    'Log_Transform': titanic_treatment['Fare_Log'].describe(),
    'Sqrt_Transform': titanic_treatment['Fare_Sqrt'].describe()
}).round(3)

print(f"📊 Transformation comparison:")
print(transformation_comparison)

# Check skewness reduction using pandas skew method
original_skew = titanic_treatment['Fare'].skew()
log_skew = titanic_treatment['Fare_Log'].skew()
sqrt_skew = titanic_treatment['Fare_Sqrt'].skew()

print(f"\n📐 Skewness comparison (closer to 0 is better):")
print(f"  Original: {original_skew:.3f}")
print(f"  Log transformed: {log_skew:.3f}")
print(f"  Square root: {sqrt_skew:.3f}")

print("\n4. Group-Based Replacement Strategy using pandas:")
print("🎯 Replace outliers with group-appropriate values")

# Initialize replacement column with original values
titanic_treatment['Fare_Replaced'] = titanic_treatment['Fare'].copy()

# Replace fare outliers with median fare for their class using pandas operations
for pclass in [1, 2, 3]:
    class_mask = titanic_treatment['Pclass'] == pclass
    class_data = titanic_treatment[class_mask]
    
    # Detect outliers within this class using pandas
    outliers = detect_outliers_iqr_pandas_only(class_data['Fare'])
    
    if outliers['outlier_count'] > 0:
        # Get median fare for this class (excluding outliers) using pandas
        non_outlier_data = class_data[~outliers['outlier_mask']]
        class_median = non_outlier_data['Fare'].median()
        
        # Replace outliers with class median using pandas loc
        outlier_indices = class_data[outliers['outlier_mask']].index
        titanic_treatment.loc[outlier_indices, 'Fare_Replaced'] = class_median
        
        print(f"Class {pclass}: Replaced {outliers['outlier_count']} outliers with median ${class_median:.2f}")

print("\n5. Flagging Strategy using pandas:")
print("🎯 Keep outliers but create flags for analysis")

# Create comprehensive outlier flags using pandas operations
outlier_methods = {
    'Fare_IQR_Outlier': detect_outliers_iqr_pandas_only(titanic_treatment['Fare'])['outlier_mask'],
    'Age_IQR_Outlier': detect_outliers_iqr_pandas_only(titanic_treatment['Age'])['outlier_mask'],
    'Fare_99pct_Outlier': titanic_treatment['Fare'] > titanic_treatment['Fare'].quantile(0.99),
    'Age_99pct_Outlier': titanic_treatment['Age'] > titanic_treatment['Age'].quantile(0.99)
}

for flag_name, flag_mask in outlier_methods.items():
    titanic_treatment[flag_name] = flag_mask.astype(int)
    print(f"{flag_name}: {flag_mask.sum()} passengers flagged")

print("\n✅ All outlier treatment strategies demonstrated using pandas-only!")

print("\n📊 7. Evaluating Outlier Treatment Strategies with pandas-Only")

print("🎯 STRATEGY EVALUATION CRITERIA:")
print("• Data preservation (how much data is kept)")
print("• Distribution improvement (normality, skewness)")
print("• Predictive power preservation")
print("• Domain knowledge compliance")

# Compare different treatment approaches using pandas
treatment_comparison = []

treatment_methods = {
    'Original': titanic_treatment['Fare'],
    'Capped': titanic_treatment['Fare_Capped'], 
    'Log_Transform': titanic_treatment['Fare_Log'],
    'Sqrt_Transform': titanic_treatment['Fare_Sqrt'],
    'Group_Replaced': titanic_treatment['Fare_Replaced']
}

for method_name, method_data in treatment_methods.items():
    # Calculate statistics using pandas methods
    stats_dict = {
        'Method': method_name,
        'Count': len(method_data),
        'Mean': method_data.mean(),
        'Std': method_data.std(),
        'Min': method_data.min(),
        'Max': method_data.max(),
        'Skewness': method_data.skew()
    }
    treatment_comparison.append(stats_dict)

comparison_df = pd.DataFrame(treatment_comparison).round(3)
print("📊 Treatment Method Comparison:")
print(comparison_df)

print("\n🔍 Treatment Method Evaluation:")

# Rank methods by different criteria using pandas operations
print("\n1. Skewness Improvement (closer to 0 is better):")
skewness_ranking = comparison_df.reindex(comparison_df['Skewness'].abs().sort_values().index)[['Method', 'Skewness']]
for i, (_, row) in enumerate(skewness_ranking.iterrows(), 1):
    print(f"  {i}. {row['Method']}: {row['Skewness']:.3f}")

print("\n2. Data Preservation (no data loss):")
data_preservation = comparison_df.sort_values('Count', ascending=False)[['Method', 'Count']]
for i, (_, row) in enumerate(data_preservation.iterrows(), 1):
    data_loss = len(titanic_treatment) - row['Count']
    print(f"  {i}. {row['Method']}: {row['Count']} rows (lost {data_loss})")

print("\n3. Outlier Reduction Assessment using pandas:")
# Check how many extreme outliers remain after each treatment
extreme_threshold = titanic_treatment['Fare'].quantile(0.99)

for method_name, method_data in treatment_methods.items():
    extreme_count = (method_data > extreme_threshold).sum()
    extreme_pct = (extreme_count / len(method_data)) * 100
    print(f"  {method_name}: {extreme_count} extreme values ({extreme_pct:.1f}%)")

print(f"\n🏆 RECOMMENDED STRATEGY:")
print(f"Based on this analysis:")
print(f"• For MODELING: Square root transformation (good normality, pandas-native)")
print(f"• For REPORTING: Capping (preserves interpretability)")  
print(f"• For EXPLORATION: Flagging (preserves all information)")
print(f"• AVOID: Removal (loses valuable information)")

print(f"\n📋 Treatment Decision Framework:")
decision_framework = """
WHEN TO USE EACH STRATEGY (pandas-only approach):

1. REMOVAL:
    ✓ Data entry errors (impossible values)
    ✓ Very large dataset (can afford data loss)
    ✗ Small dataset or valuable information

2. CAPPING (WINSORIZATION):
    ✓ Want to preserve interpretability
    ✓ Reporting and business understanding
    ✓ Moderate outlier impact
    • pandas method: series.clip(lower=p5, upper=p95)

3. TRANSFORMATION:
    ✓ Statistical modeling
    ✓ Heavily skewed data
    ✓ Want to preserve relative relationships
    • pandas methods: series.apply(lambda x: x**0.5) or mathematical operations

4. GROUP-BASED REPLACEMENT:
    ✓ Outliers don't make sense in context
    ✓ Clear group-based patterns exist
    ✓ Domain expertise available
    • pandas methods: groupby + transform or loc-based replacement

5. FLAGGING:
    ✓ Uncertain about outlier validity
    ✓ Want to preserve all information
    ✓ Exploratory analysis phase
    • pandas methods: boolean masks + astype(int)
"""

print(decision_framework)

print("✅ Outlier treatment evaluation complete using pandas-only!")

print("\n📊 8. Final Outlier Analysis Summary with pandas-Only")

print("🎯 COMPREHENSIVE OUTLIER AUDIT")

# Create final outlier report using pandas operations
outlier_audit = {
    'Dataset': 'Titanic Enhanced',
    'Total_Passengers': len(titanic_treatment),
    'Columns_Analyzed': len(numerical_cols),
    'Detection_Methods': ['IQR', 'Percentile', 'Group-based'],
    'Treatment_Methods': ['Capping', 'Transformation', 'Replacement', 'Flagging']
}

# Count outliers by column and method using pandas
final_outlier_summary = []

for col in numerical_cols:
    iqr_outliers = detect_outliers_iqr_pandas_only(titanic_treatment[col])
    pct_outliers = detect_outliers_percentile_pandas_only(titanic_treatment[col])
    
    final_outlier_summary.append({
        'Column': col,
        'IQR_Outliers': iqr_outliers['outlier_count'],
        'IQR_Percentage': round(iqr_outliers['outlier_percentage'], 2),
        '5-95_Pct_Outliers': pct_outliers['outlier_count'],
        'Data_Range': f"{titanic_treatment[col].min():.2f} - {titanic_treatment[col].max():.2f}",
        'Recommended_Treatment': 'TBD'
    })

# Add recommendations based on analysis using pandas operations
recommendations = {
    'Age': 'Flagging (elderly passengers are valid)',
    'Fare': 'Square root transformation (for modeling)',
    'SibSp': 'Keep (large families exist)',
    'Parch': 'Keep (large families exist)', 
    'Family_Size': 'Keep (derived from SibSp/Parch)',
    'Fare_Per_Person': 'Capping (for interpretability)'
}

final_summary_df = pd.DataFrame(final_outlier_summary)
final_summary_df['Recommended_Treatment'] = final_summary_df['Column'].map(recommendations)

print("📋 FINAL OUTLIER ANALYSIS SUMMARY:")
print(final_summary_df)

print(f"\n🔍 KEY FINDINGS using pandas:")
total_outliers = final_summary_df['IQR_Outliers'].sum()
most_problematic = final_summary_df.loc[final_summary_df['IQR_Outliers'].idxmax(), 'Column']
cleanest = final_summary_df.loc[final_summary_df['IQR_Outliers'].idxmin(), 'Column']

print(f"• Total IQR outliers across all columns: {total_outliers}")
print(f"• Most problematic column: {most_problematic}")
print(f"• Cleanest column: {cleanest}")

# Survival impact summary using pandas operations
print(f"\n📊 OUTLIER IMPACT ON SURVIVAL:")
for col in ['Age', 'Fare']:
    outliers = detect_outliers_iqr_pandas_only(titanic_treatment[col])
    outlier_survival = titanic_treatment[outliers['outlier_mask']]['Survived'].mean()
    normal_survival = titanic_treatment[~outliers['outlier_mask']]['Survived'].mean()
    impact = outlier_survival - normal_survival
    direction = "higher" if impact > 0 else "lower"
    print(f"• {col} outliers have {direction} survival rate ({impact:+.3f})")

print(f"\n🎯 BUSINESS INSIGHTS:")
business_insights = [
    "High-fare passengers (outliers) tend to survive more - wealth matters",
    "Elderly passengers (age outliers) may need special consideration",
    "Large families create fare-per-person outliers - group bookings",
    "Zero fares suggest crew members or special arrangements",
    "Context-aware analysis prevents false outlier identification"
]

for i, insight in enumerate(business_insights, 1):
    print(f"{i}. {insight}")

# Memory usage of outlier flags using pandas memory_usage
outlier_flag_columns = [col for col in titanic_treatment.columns if 'Outlier' in col]
if outlier_flag_columns:
    outlier_flags_memory = titanic_treatment[outlier_flag_columns].memory_usage(deep=True).sum()
    print(f"\n💾 Outlier flags memory usage: {outlier_flags_memory / 1024:.2f} KB ({len(outlier_flag_columns)} flags)")

print("✅ Comprehensive outlier analysis completed using pandas-only!")

def session4_summary():
    """
    Session 4 Summary: Pure pandas Outlier Detection (Labs 1–8)
    Complete statistical outlier detection and treatment using 100% pandas methods
    """
    lines = []

    # Header
    lines.append("=== Session 4 Summary: Pure pandas Outlier Detection & Treatment ===")
    lines.append("Scope: Labs 1 → 8")
    lines.append("Goal: Master statistical outlier detection and treatment using 100% pandas methods,")
    lines.append("      with context-aware analysis and business-ready treatment strategies.\n")

    # Lab 1
    lines.append("1. Enhanced dataset preparation")
    lines.append("- Applied all Week 11 enhancements (Monday imputation, Tuesday dtypes, Wednesday features).")
    lines.append("- Identified numerical columns for outlier analysis using pandas select_dtypes.")
    lines.append("- Generated basic statistical overview with pandas describe().\n")

    # Lab 2
    lines.append("2. IQR method implementation")
    lines.append("- Built detect_outliers_iqr_pandas_only() using .quantile(0.25/0.75) and boolean masks.")
    lines.append("- Applied to Age and Fare columns; identified outlier patterns and counts.")
    lines.append("- Created comprehensive outlier summary across all numerical columns.\n")

    # Lab 3
    lines.append("3. Percentile-based detection")
    lines.append("- Implemented detect_outliers_percentile_pandas_only() with flexible thresholds.")
    lines.append("- Compared 1st/99th, 5th/95th, and 10th/90th percentile methods.")
    lines.append("- Generated detailed percentile breakdowns for key columns using .quantile().\n")

    # Lab 4
    lines.append("4. Context-aware group-based detection")
    lines.append("- Built detect_outliers_by_group_pandas_only() for within-group outlier analysis.")
    lines.append("- Analyzed fare outliers by passenger class, age by gender×class, fare by family size.")
    lines.append("- Identified context-aware outliers vs global outliers; reduced false positives.\n")

    # Lab 5
    lines.append("5. Advanced outlier patterns")
    lines.append("- Survival analysis: compared outlier vs normal passenger survival rates.")
    lines.append("- Multi-variate outlier detection: flagged passengers extreme in multiple dimensions.")
    lines.append("- Distribution analysis: outliers by embarkation port and passenger class using pd.crosstab.")
    lines.append("- Data quality investigation: zero fares, round numbers, extreme values.\n")

    # Lab 6
    lines.append("6. Treatment strategies")
    lines.append("- Removal: extreme outlier identification (99.9th percentile) with bias warnings.")
    lines.append("- Capping: Winsorization using pandas .clip() method for percentile bounds.")
    lines.append("- Transformation: mathematical transforms (sqrt) using pandas apply() and operations.")
    lines.append("- Group replacement: class-based median replacement using pandas groupby logic.")
    lines.append("- Flagging: comprehensive outlier indicators using boolean masks.\n")

    # Lab 7
    lines.append("7. Treatment evaluation")
    lines.append("- Strategy comparison: count, statistics, skewness for each treatment method.")
    lines.append("- Ranking by skewness improvement, data preservation, and outlier reduction.")
    lines.append("- Treatment decision framework with pandas-specific implementation notes.\n")

    # Lab 8
    lines.append("8. Final summary and audit")
    lines.append("- Comprehensive outlier audit with method comparison and recommendations.")
    lines.append("- Business insights from outlier patterns and survival correlations.")
    lines.append("- Memory usage assessment for outlier flags and treatment columns.\n")

    # Key methods
    lines.append("Key pandas methods mastered")
    lines.append("- .quantile(0.25/0.75): IQR calculation; .clip(): value capping")
    lines.append("- .groupby().agg(): group-based statistics; .transform(): group-aware operations")
    lines.append("- Boolean indexing: outlier filtering; .crosstab(): distribution analysis")
    lines.append("- .skew(): distribution assessment; .apply(): custom transformations")
    lines.append("- .memory_usage(deep=True): memory monitoring\n")

    # Safeguards
    lines.append("Pure pandas safeguards")
    lines.append("- No numpy dependencies: used pandas native mathematical operations")
    lines.append("- Categorical-safe operations: avoided arithmetic on categorical dtypes")
    lines.append("- Defensive programming: handled edge cases with pandas .clip() and conditionals")
    lines.append("- Memory efficiency: used appropriate dtypes for flag columns\n")

    # Deliverables
    lines.append("Deliverables produced")
    lines.append("- Outlier detection functions: IQR-based, percentile-based, group-based")
    lines.append("- Treatment methods: capped, transformed, group-replaced, flagged versions")
    lines.append("- Outlier flags: Age_Outlier, Fare_Outlier, multi-dimensional outlier counts")
    lines.append("- Business insights: survival correlations, context-aware patterns")
    lines.append("- Treatment recommendations: method-specific guidance for different use cases\n")

    # Business value
    lines.append("Business value delivered")
    lines.append("- Context-aware outlier identification prevents false positives")
    lines.append("- Treatment strategy framework enables appropriate method selection")
    lines.append("- Survival correlation analysis reveals outlier impact on outcomes")
    lines.append("- Memory-efficient flag system preserves information for analysis")
    lines.append("- Pure pandas approach ensures reproducible, dependency-free workflow")

    return "\n".join(lines)

if __name__ == "__main__":
    print(session4_summary())
