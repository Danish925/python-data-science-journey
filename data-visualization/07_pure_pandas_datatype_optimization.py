print("=== PURE PANDAS DATA TYPE OPTIMIZATION ===")
print("Session 2: Memory-efficient data with 100% pandas methods")
print("Date: Tuesday, October 21, 2025")

# Import ONLY pandas - no numpy!
import pandas as pd

# Set pandas display options
pd.set_option('display.max_columns', None)
pd.set_option('display.precision', 2)

print("\n🔧 Environment setup complete!")
print("🎯 Today's Goal: Master pandas-only data type optimization")
print("🚫 NO NUMPY: Pure pandas methods only!")



print("\n📊 1. Analyzing Current Data Types with Pure pandas")

# Load the Titanic dataset (continuing from Monday)
titanic_url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_df = pd.read_csv(titanic_url)

# Apply Monday's missing value fixes using pandas-only methods
age_by_group = titanic_df.groupby(['Pclass', 'Sex'])['Age'].transform('median')
titanic_df['Age'] = titanic_df['Age'].fillna(age_by_group)

embarked_mode = titanic_df['Embarked'].mode()[0]
titanic_df['Embarked'] = titanic_df['Embarked'].fillna(embarked_mode)

print("✅ Dataset loaded with Monday's missing value fixes applied")

# Analyze current data types using pure pandas
print("\n📋 Current Data Types:")
print(titanic_df.dtypes)

print(f"\n💾 Current Memory Usage: {titanic_df.memory_usage(deep=True).sum() / 1024:.2f} KB")

# Detailed memory analysis using pandas methods
print("\n📊 Detailed Memory Usage by Column:")
memory_usage = titanic_df.memory_usage(deep=True)
memory_df = pd.DataFrame({
    'Column': memory_usage.index,
    'Memory_Bytes': memory_usage.values,
    'Memory_KB': (memory_usage.values / 1024).round(3),
    'Data_Type': ['Index'] + [str(dtype) for dtype in titanic_df.dtypes]
})
print(memory_df)

# Identify optimization opportunities using pandas-only methods
print("\n🎯 Data Type Optimization Opportunities:")
print(f"• Pclass: {titanic_df['Pclass'].nunique()} unique values → Could be categorical")
print(f"• Sex: {titanic_df['Sex'].nunique()} unique values → Could be categorical") 
print(f"• Embarked: {titanic_df['Embarked'].nunique()} unique values → Could be categorical")
print(f"• Survived: {titanic_df['Survived'].nunique()} unique values → Could be boolean")



print("\n📊 2. Handling Messy Numeric Data with pandas-Only")

# Create a messy dataset to demonstrate pandas conversion techniques
messy_data = pd.DataFrame({
    'customer_id': ['001', '002', '003', '004', '005'],
    'age': ['25', '30', 'unknown', '35', '28'],
    'salary': ['50000', '60,000', '70000', 'confidential', '55000'],   # Has commas
    'score': ['8.5', '9.2', '7.8', '8.8', '9.1'],
    'department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'active': ['Yes', 'No', 'Yes', 'Yes', 'No'],
    'join_date': ['2023-01-15', '2023-02-20', 'invalid', '2023-03-10', '2023-04-05']
})

print("🔧 Created messy dataset for practice:")
print(messy_data)
print("\n📋 Original data types:") 
print(messy_data.dtypes)
print(f"💾 Original memory usage: {messy_data.memory_usage(deep=True).sum()} bytes")

print("\n🎯 Pure pandas Syntax: pd.to_numeric() with error handling")
print("• errors='coerce' → Invalid values become NaN")
print("• errors='ignore' → Invalid values remain as strings")
print("• errors='raise' → Raises exception on invalid values (default)")

# Demonstrate different error handling approaches using pandas-only
print("\n1. Converting Age Column:")
print("Original ages:", messy_data['age'].tolist())

# Method 1: Coerce errors to NaN (pandas-only)
messy_data['age_coerce'] = pd.to_numeric(messy_data['age'], errors='coerce')
print("With errors='coerce':", messy_data['age_coerce'].tolist())

# Method 2: Ignore errors (keeps original) - pandas-only
messy_data['age_ignore'] = pd.to_numeric(messy_data['age'], errors='ignore')
print("With errors='ignore':", messy_data['age_ignore'].tolist())

print("\n2. Converting Salary Column (with preprocessing):")
print("Original salaries:", messy_data['salary'].tolist())

# Clean salary data first using pandas string methods
messy_data['salary_clean'] = messy_data['salary'].str.replace(',', '')
print("After removing commas:", messy_data['salary_clean'].tolist())

# Convert to numeric using pandas
messy_data['salary_numeric'] = pd.to_numeric(messy_data['salary_clean'], errors='coerce')
print("Final numeric salaries:", messy_data['salary_numeric'].tolist())

print("\n3. Converting Score Column:")
# Should be straightforward conversion using pandas
messy_data['score_numeric'] = pd.to_numeric(messy_data['score'], errors='coerce')
print("Scores converted successfully:", messy_data['score_numeric'].tolist())



print("\n📊 3. Advanced Numeric Type Optimization with pandas-Only")

# Work with Titanic data for realistic optimization
print("🎯 Optimizing Titanic Dataset Numeric Types")

# Analyze integer ranges to choose optimal dtypes using pandas methods
print("\n1. Integer Column Analysis:")
integer_cols = ['PassengerId', 'SibSp', 'Parch']
for col in integer_cols:
    min_val = titanic_df[col].min()
    max_val = titanic_df[col].max()
    print(f"{col}: Range {min_val} to {max_val}")
    
    # Suggest optimal integer type using pandas logic
    if min_val >= 0 and max_val < 255:
        optimal_type = 'uint8'
    elif min_val >= -128 and max_val < 127:
        optimal_type = 'int8'  
    elif min_val >= 0 and max_val < 65535:
        optimal_type = 'uint16'
    elif min_val >= -32768 and max_val < 32767:
        optimal_type = 'int16'
    else:
        optimal_type = 'int32'
    
    print(f"   → Optimal type: {optimal_type}")

# Apply integer optimizations using pandas-only methods
print("\n2. Applying Integer Optimizations:")
titanic_optimized = titanic_df.copy()

# PassengerId can be uint16 (range 1-891)
original_pid_memory = titanic_optimized['PassengerId'].memory_usage(deep=True)
titanic_optimized['PassengerId'] = titanic_optimized['PassengerId'].astype('uint16')
optimized_pid_memory = titanic_optimized['PassengerId'].memory_usage(deep=True)
print(f"PassengerId: {original_pid_memory} → {optimized_pid_memory} bytes ({original_pid_memory - optimized_pid_memory} saved)")

# SibSp can be uint8 (range 0-8)
titanic_optimized['SibSp'] = titanic_optimized['SibSp'].astype('uint8')

# Parch can be uint8 (range 0-6)  
titanic_optimized['Parch'] = titanic_optimized['Parch'].astype('uint8')

print("✅ Integer optimizations applied!")

# Analyze float columns using pandas-only methods
print("\n3. Float Column Analysis:")
float_cols = ['Age', 'Fare']
for col in float_cols:
    print(f"{col}:")
    print(f"   Min: {titanic_optimized[col].min():.2f}")
    print(f"   Max: {titanic_optimized[col].max():.2f}")
    print(f"   Precision needed: Check decimal places")
    
    # Check if float32 is sufficient using pandas comparison
    original_memory = titanic_optimized[col].memory_usage(deep=True)
    test_float32 = titanic_optimized[col].astype('float32')
    
    # Check for precision loss using pandas operations
    # Calculate absolute difference and check if any are significant
    diff_series = (titanic_optimized[col] - test_float32).abs()
    precision_loss = (diff_series > 0.01).any()
    print(f"   Precision loss with float32: {precision_loss}")
    
    if not precision_loss:
        titanic_optimized[col] = test_float32
        new_memory = titanic_optimized[col].memory_usage(deep=True) 
        print(f"   Memory: {original_memory} → {new_memory} bytes")



print("\n📊 4. Categorical Data Optimization with Pure pandas")

print("🎯 Pure pandas Syntax: .astype('category')")
print("• Converts string data to categorical type")
print("• Stores unique values once + integer codes")
print("• Massive memory savings for repetitive data")

print("\n1. Categorical Conversion Analysis:")

# Analyze categorical opportunities using pandas-only methods
categorical_candidates = ['Pclass', 'Sex', 'Embarked', 'Cabin']

for col in categorical_candidates:
    if col == 'Cabin':
        # Skip cabin for now (many unique values)
        continue
        
    unique_count = titanic_optimized[col].nunique()
    total_count = len(titanic_optimized)
    unique_ratio = unique_count / total_count
    
    print(f"\n{col}:")
    print(f"   Unique values: {unique_count}")
    print(f"   Total values: {total_count}")
    print(f"   Uniqueness ratio: {unique_ratio:.3f}")
    print(f"   Values: {titanic_optimized[col].unique().tolist()}")
    
    # Memory comparison using pandas methods only
    original_memory = titanic_optimized[col].memory_usage(deep=True)
    categorical_memory = titanic_optimized[col].astype('category').memory_usage(deep=True)
    savings = original_memory - categorical_memory
    savings_pct = (savings / original_memory * 100)
    
    print(f"   Memory as object: {original_memory} bytes")
    print(f"   Memory as category: {categorical_memory} bytes")
    print(f"   Savings: {savings} bytes ({savings_pct:.1f}%)")

# Apply categorical conversions using pandas-only
print("\n2. Applying Categorical Conversions:")
categorical_cols = ['Pclass', 'Sex', 'Embarked']

for col in categorical_cols:
    original_memory = titanic_optimized[col].memory_usage(deep=True)
    titanic_optimized[col] = titanic_optimized[col].astype('category')
    new_memory = titanic_optimized[col].memory_usage(deep=True)
    
    print(f"✅ {col}: {original_memory} → {new_memory} bytes")

print("\n3. Understanding Categorical Data Structure:")
print("🔍 How categorical data works internally:")

sex_categorical = titanic_optimized['Sex']
print(f"Sex categories: {sex_categorical.cat.categories.tolist()}")
print(f"Sex codes (first 10): {sex_categorical.cat.codes[:10].tolist()}")

# Show the mapping using pandas methods
print("\nCategory mapping:")
for i, category in enumerate(sex_categorical.cat.categories):
    count = (sex_categorical.cat.codes == i).sum()
    print(f"   {i} → '{category}' ({count} occurrences)")



print("\n📊 5. Boolean Conversion with pandas-Only")

print("🎯 Converting binary data to boolean type")

# Convert Survived column to boolean using pandas-only
print("1. Survived Column Conversion:")
print(f"Original Survived values: {titanic_optimized['Survived'].unique().tolist()}")
print(f"Original dtype: {titanic_optimized['Survived'].dtype}")

original_memory = titanic_optimized['Survived'].memory_usage(deep=True)
titanic_optimized['Survived'] = titanic_optimized['Survived'].astype('bool')
new_memory = titanic_optimized['Survived'].memory_usage(deep=True)

print(f"✅ Survived converted to boolean")
print(f"New dtype: {titanic_optimized['Survived'].dtype}")
print(f"Memory: {original_memory} → {new_memory} bytes")

# Work with messy boolean data from our example using pandas-only
print("\n2. Messy Boolean Data Conversion:")
print("🎯 Pure pandas Syntax: .map() and .replace() for value mapping")

print("Original active values:", messy_data['active'].tolist())

# Method 1: Using map with dictionary (pandas-only)
boolean_mapping = {'Yes': True, 'No': False}
messy_data['active_bool_v1'] = messy_data['active'].map(boolean_mapping)
print("Method 1 (map):", messy_data['active_bool_v1'].tolist())

# Method 2: Using replace then astype (pandas-only)
messy_data['active_bool_v2'] = messy_data['active'].replace({'Yes': True, 'No': False}).astype(bool)
print("Method 2 (replace + astype):", messy_data['active_bool_v2'].tolist())

# Method 3: Using pandas comparison (pandas-only)
messy_data['active_bool_v3'] = messy_data['active'] == 'Yes'
print("Method 3 (comparison):", messy_data['active_bool_v3'].tolist())

print("✅ All three methods produce same result using pandas-only!")




print("\n📊 6. DateTime Conversion and Feature Extraction with pandas-Only")

print("🎯 Pure pandas Syntax: pd.to_datetime() with error handling")

# Work with messy date data using pandas-only methods
print("1. DateTime Conversion:")
print("Original join_date values:", messy_data['join_date'].tolist())

# Convert with error handling using pandas
messy_data['join_date_dt'] = pd.to_datetime(messy_data['join_date'], errors='coerce')
print("Converted to datetime:", messy_data['join_date_dt'].tolist())

print(f"✅ DateTime conversion complete")
print(f"New dtype: {messy_data['join_date_dt'].dtype}")

# Extract features from datetime using pandas .dt accessor
print("\n2. DateTime Feature Extraction:")
print("🎯 Pure pandas Syntax: .dt accessor for datetime operations")

# Extract various date components using pandas-only
messy_data['join_year'] = messy_data['join_date_dt'].dt.year
messy_data['join_month'] = messy_data['join_date_dt'].dt.month
messy_data['join_day'] = messy_data['join_date_dt'].dt.day
messy_data['join_weekday'] = messy_data['join_date_dt'].dt.weekday   # 0=Monday
messy_data['join_weekday_name'] = messy_data['join_date_dt'].dt.day_name()
messy_data['join_quarter'] = messy_data['join_date_dt'].dt.quarter
messy_data['join_is_weekend'] = messy_data['join_date_dt'].dt.weekday >= 5

print("📋 Extracted datetime features:")
datetime_features = ['join_date_dt', 'join_year', 'join_month', 'join_weekday', 
                     'join_weekday_name', 'join_quarter', 'join_is_weekend']
print(messy_data[datetime_features])

# More advanced datetime operations using pandas-only
print("\n3. Advanced DateTime Operations:")

# Days since first date using pandas operations
first_date = messy_data['join_date_dt'].min()
messy_data['days_since_first'] = (messy_data['join_date_dt'] - first_date).dt.days

# Time until end of year using pandas datetime operations
year_end = pd.to_datetime('2023-12-31')
messy_data['days_to_year_end'] = (year_end - messy_data['join_date_dt']).dt.days

print("📋 Advanced datetime features:")
advanced_features = ['join_date_dt', 'days_since_first', 'days_to_year_end']
print(messy_data[advanced_features])

print("✅ DateTime feature extraction complete using pandas-only!")



print("\n📊 7. Complete Titanic Dataset Optimization with pandas-Only")
print("🎯 Goal: Apply all optimization techniques using pure pandas methods")

# Start fresh for final optimization
titanic_final = titanic_df.copy()

print("\n1. BEFORE Optimization:")
print("=" * 40)
print(f"Shape: {titanic_final.shape}")
print(f"Memory usage: {titanic_final.memory_usage(deep=True).sum() / 1024:.2f} KB")
print("\nData types:")
print(titanic_final.dtypes.value_counts())

# Track memory savings using pandas operations
memory_tracker = []

def track_memory(step_name, df):
    memory_kb = df.memory_usage(deep=True).sum() / 1024
    memory_tracker.append({'Step': step_name, 'Memory_KB': memory_kb})
    print(f"📊 {step_name}: {memory_kb:.2f} KB")

track_memory('Original', titanic_final)

# Step 1: Optimize integer columns using pandas-only
print("\n2. Integer Optimization:")
titanic_final['PassengerId'] = titanic_final['PassengerId'].astype('uint16')
titanic_final['SibSp'] = titanic_final['SibSp'].astype('uint8')
titanic_final['Parch'] = titanic_final['Parch'].astype('uint8')
track_memory('After integer optimization', titanic_final)

# Step 2: Optimize categorical columns using pandas-only
print("\n3. Categorical Optimization:")
categorical_cols = ['Pclass', 'Sex', 'Embarked']
for col in categorical_cols:
    titanic_final[col] = titanic_final[col].astype('category')
track_memory('After categorical optimization', titanic_final)

# Step 3: Boolean conversion using pandas-only
print("\n4. Boolean Optimization:")
titanic_final['Survived'] = titanic_final['Survived'].astype('bool')
track_memory('After boolean optimization', titanic_final)

# Step 4: Float optimization using pandas-only (if safe)
print("\n5. Float Optimization:")
# Test Age for float32 compatibility using pandas comparison
age_float64 = titanic_final['Age'].copy()
age_float32 = age_float64.astype('float32')
precision_loss = ((age_float64 - age_float32).abs() > 0.01).any()

if not precision_loss:
    titanic_final['Age'] = age_float32
    print("✅ Age converted to float32")
else:
    print("❌ Age kept as float64 (precision loss detected)")

# Test Fare for float32 compatibility using pandas comparison  
fare_float64 = titanic_final['Fare'].copy()
fare_float32 = fare_float64.astype('float32')
precision_loss = ((fare_float64 - fare_float32).abs() > 0.01).any()

if not precision_loss:
    titanic_final['Fare'] = fare_float32
    print("✅ Fare converted to float32")
else:
    print("❌ Fare kept as float64 (precision loss detected)")

track_memory('After float optimization', titanic_final)

print("\n6. AFTER Optimization:")
print("=" * 40)
print(f"Shape: {titanic_final.shape}")
print(f"Memory usage: {titanic_final.memory_usage(deep=True).sum() / 1024:.2f} KB")
print("\nOptimized data types:")
print(titanic_final.dtypes)
print("\nData type distribution:")
print(titanic_final.dtypes.value_counts())



print("\n📊 8. Optimization Results Analysis with pandas-Only")

# Create memory tracking summary using pandas
memory_df = pd.DataFrame(memory_tracker)
memory_df['Memory_Saved_KB'] = memory_df['Memory_KB'].iloc[0] - memory_df['Memory_KB']
memory_df['Memory_Saved_Pct'] = (memory_df['Memory_Saved_KB'] / memory_df['Memory_KB'].iloc[0] * 100).round(1)

print("📋 Memory Optimization Tracking:")
print(memory_df)

# Final comparison using pandas calculations
original_memory = memory_df['Memory_KB'].iloc[0]
final_memory = memory_df['Memory_KB'].iloc[-1]
total_savings = original_memory - final_memory
savings_percentage = (total_savings / original_memory * 100)

print(f"\n🎯 OPTIMIZATION SUMMARY:")
print(f"Original memory: {original_memory:.2f} KB")
print(f"Final memory: {final_memory:.2f} KB")
print(f"Total savings: {total_savings:.2f} KB ({savings_percentage:.1f}%)")

# Detailed column-by-column analysis using pandas
print("\n📊 Detailed Memory Usage by Column:")
column_memory = titanic_final.memory_usage(deep=True)
column_analysis = pd.DataFrame({
    'Column': column_memory.index,
    'Memory_Bytes': column_memory.values,
    'Data_Type': ['Index'] + [str(dtype) for dtype in titanic_final.dtypes],
    'Unique_Values': [len(titanic_final)] + [titanic_final[col].nunique() 
                                             for col in titanic_final.columns]
}).sort_values('Memory_Bytes', ascending=False)

print(column_analysis)



print("\n" + "="*60)
print("📚 SUMMARY: Pure pandas Data Type Optimization")
print("="*60)

print("\n✅ SKILLS MASTERED TODAY (pandas-Only):")
print("1. Memory analysis with .memory_usage(deep=True)")
print("2. Numeric conversion with pd.to_numeric() error handling")
print("3. Categorical optimization with .astype('category')")
print("4. Boolean conversion using .map(), .replace(), and .astype()")
print("5. DateTime conversion with pd.to_datetime() and .dt accessor")
print("6. Integer/float type optimization with precision checking")
print("7. Complete dataset optimization workflow")

print("\n🎯 NEW PANDAS-ONLY SYNTAX LEARNED:")
print("• pd.to_numeric(series, errors='coerce')   # Convert with NaN for errors")
print("• df['col'].astype('category')   # Convert to categorical") 
print("• df['col'].astype('bool')   # Convert to boolean")
print("• df['col'].astype('uint8')   # Optimize integer storage")
print("• pd.to_datetime(series, errors='coerce')   # Convert dates")
print("• df['date_col'].dt.year   # Extract datetime features")
print("• df['col'].cat.categories   # View categorical values")
print("• ((ser1 - ser2).abs() > 0.01).any()   # Test precision loss")

print("\n🔥 POWER TECHNIQUE OF THE DAY:")
print("PURE PANDAS DATA TYPE OPTIMIZATION")
print(f"→ Achieved {savings_percentage:.1f}% memory reduction using pandas-only")
print("→ No external dependencies - 100% pandas methods")
print("→ Stores categorical data efficiently with integer codes")
print("→ Enables faster operations and reduced memory footprint")

print("\n💡 KEY INSIGHTS (pandas-Only):")
print("• pandas precision testing: ((original - converted).abs() > threshold).any()")
print("• Categorical optimization: Best when < 50% unique values")  
print("• Boolean conversion: Multiple pandas methods (.map, .replace, ==)")
print("• DateTime extraction: .dt accessor provides rich feature set")
print("• Memory monitoring: .memory_usage(deep=True) tracks optimization")

print("\n🚫 NUMPY ELIMINATED:")
print("• No np.log, np.sqrt - use pandas alternatives or defer to later")
print("• No numpy statistical functions - use pandas .describe(), .quantile()")
print("• Pure pandas operations ensure single-library dependency")
print("• All mathematical operations use pandas Series methods")

print("\n📝 HOMEWORK FOR TONIGHT:")
print("1. Practice pandas-only type optimization on other datasets")
print("2. Experiment with categorical vs object memory differences")
print("3. Test precision loss detection with various float conversions")

print("\n🚀 TOMORROW PREVIEW:")
print("Session 3: pandas String Processing & Feature Engineering")
print("→ Extract titles from names using .str.extract()")
print("→ Pattern matching with .str.contains()")
print("→ Text cleaning and standardization")
print("→ Create features from text data")

print(f"\n✓ Session 2 completed! Pure pandas optimization mastered - {savings_percentage:.1f}% memory saved!")
print("🐼 100% pandas-powered, zero external dependencies! 🐼")
