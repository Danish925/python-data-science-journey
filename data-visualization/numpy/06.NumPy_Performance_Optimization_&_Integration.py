import numpy as np
import pandas as pd
import time

print("🎯 Lab 1: Performance Comparison - NumPy vs Python Lists\n")

# Load Titanic data
titanic_df = pd.DataFrame({
    'Age': [22, 38, 26, 35, 54, 2, 27, 14, 58, 20],
    'Fare': [7.25, 71.28, 7.92, 53.10, 51.86, 21.08, 11.13, 30.07, 26.55, 8.05],
    'Pclass': [3, 1, 3, 1, 1, 3, 3, 2, 1, 3],
    'Survived': [0, 1, 1, 1, 0, 0, 0, 1, 0, 0]
})

age = titanic_df['Age'].values
age_list = list(age)

print("Dataset size: 10 passengers")
print(f"Python list: {age_list}")
print(f"NumPy array: {age}")

# 1. Simple addition
print("\n1. ADDING 5 TO EACH VALUE:")

# Python list approach
start = time.time()
result_list = [x + 5 for x in age_list]
python_time = time.time() - start

# NumPy approach
start = time.time()
result_numpy = age + 5
numpy_time = time.time() - start

print(f"Python list result: {result_list}")
print(f"NumPy result: {result_numpy}")
print(f"Time - Python: {python_time*1000:.4f}ms, NumPy: {numpy_time*1000:.4f}ms")
print(f"NumPy is {python_time/numpy_time:.1f}x faster")

# 2. Calculate mean
print("\n2. CALCULATING MEAN:")

# Python approach
start = time.time()
python_mean = sum(age_list) / len(age_list)
python_time = time.time() - start

# NumPy approach
start = time.time()
numpy_mean = np.mean(age)
numpy_time = time.time() - start

print(f"Python result: {python_mean:.2f}")
print(f"NumPy result: {numpy_mean:.2f}")
print(f"Time - Python: {python_time*1000:.4f}ms, NumPy: {numpy_time*1000:.4f}ms")

# 3. Filtering
print("\n3. FILTERING (Age > 30):")

# Python approach
start = time.time()
result_list = [x for x in age_list if x > 30]
python_time = time.time() - start

# NumPy approach
start = time.time()
result_numpy = age[age > 30]
numpy_time = time.time() - start

print(f"Python result: {result_list}")
print(f"NumPy result: {result_numpy}")
print(f"Time - Python: {python_time*1000:.4f}ms, NumPy: {numpy_time*1000:.4f}ms")

print("\n📚 Performance Summary:")
print("• NumPy is typically 10-100x faster")
print("• Speed increases with larger datasets")
print("• NumPy uses optimized C code")
print("• Python loops are slow for big data")

print("\n✅ Lab 1 Complete!")



print("🎯 Lab 2: Vectorization - Avoiding Python Loops\n")

age = titanic_df['Age'].values
fare = titanic_df['Fare'].values

print("Age:", age)
print("Fare:", fare)

# 1. Avoid loops - Use vectorization
print("\n1. AVOIDING LOOPS (Normalize Age):")

# SLOW - Using a loop
print("Slow approach (loop):")
start = time.time()
age_normalized_slow = []
for a in age:
    normalized = (a - age.min()) / (age.max() - age.min())
    age_normalized_slow.append(normalized)
age_normalized_slow = np.array(age_normalized_slow)
slow_time = time.time() - start

# FAST - Using vectorization
print("Fast approach (vectorization):")
start = time.time()
age_normalized_fast = (age - age.min()) / (age.max() - age.min())
fast_time = time.time() - start

print(f"Results match: {np.allclose(age_normalized_slow, age_normalized_fast)}")
print(f"Slow time: {slow_time*1000:.4f}ms")
print(f"Fast time: {fast_time*1000:.4f}ms")
print(f"Speedup: {slow_time/fast_time:.1f}x")

# 2. Apply multiple operations at once
print("\n2. CHAINED OPERATIONS:")
# Normalize age, add bonus, apply discount
result = ((age - age.mean()) / age.std()) * 10 + 100
print(f"Complex formula result: {result}")
print("All operations done in one line!")

# 3. Conditional operations without loops
print("\n3. CONDITIONAL OPERATIONS (No if-else loop):")

# SLOW - Using loop
print("Slow approach:")
start = time.time()
is_young_slow = []
for a in age:
    if a < 25:
        is_young_slow.append(1)
    else:
        is_young_slow.append(0)
is_young_slow = np.array(is_young_slow)
slow_time = time.time() - start

# FAST - Using where
print("Fast approach:")
start = time.time()
is_young_fast = np.where(age < 25, 1, 0)
fast_time = time.time() - start

print(f"Results: {is_young_fast}")
print(f"Slow time: {slow_time*1000:.4f}ms, Fast time: {fast_time*1000:.4f}ms")

# 4. Multiple conditions
print("\n4. MULTIPLE CONDITIONS (np.select):")
age_category = np.select(
    [age < 13, (age >= 13) & (age < 18), (age >= 18) & (age < 60), age >= 60],
    [0, 1, 2, 3],
    default=-1
)
print(f"Age categories: {age_category}")
print("0=Child, 1=Teen, 2=Adult, 3=Senior, -1=Unknown")

# 5. Broadcasting operations
print("\n5. BROADCASTING OPERATIONS:")
# Add fare to all ages (creates (10, 10) matrix)
combined_matrix = age[:, np.newaxis] + fare[np.newaxis, :]
print(f"Age + each Fare (shape {combined_matrix.shape}):")
print(combined_matrix)

print("\n📚 Vectorization Tips:")
print("• Replace loops with array operations")
print("• Use np.where() for if-else")
print("• Use np.select() for multiple conditions")
print("• Chain operations together")
print("• Use broadcasting instead of loops")

print("\n✅ Lab 2 Complete!")





print("🎯 Lab 3: Memory Efficiency\n")

import sys

print("Memory comparison:")

# Python list
age_list = list(age)
list_size = sys.getsizeof(age_list) + sum(sys.getsizeof(x) for x in age_list)

# NumPy array
age_numpy = age
numpy_size = age_numpy.nbytes

print(f"\n1. SIZE COMPARISON:")
print(f"Python list size: {list_size} bytes")
print(f"NumPy array size: {numpy_size} bytes")
print(f"NumPy uses {list_size / numpy_size:.1f}x less memory")

# 2. Data type matters
print(f"\n2. DATA TYPE IMPACT:")
age_int32 = age.astype(np.int32)
age_int64 = age.astype(np.int64)
age_float32 = age.astype(np.float32)
age_float64 = age.astype(np.float64)

print(f"int32: {age_int32.nbytes} bytes")
print(f"int64: {age_int64.nbytes} bytes")
print(f"float32: {age_float32.nbytes} bytes")
print(f"float64: {age_float64.nbytes} bytes")
print(f"float64 uses {age_float64.nbytes / age_int32.nbytes:.1f}x more memory than int32")

# 3. Array views vs copies
print(f"\n3. VIEWS VS COPIES:")
original = age.copy()
view = original[:]  # View (shares memory)
copy = original.copy()  # Copy (separate memory)

# Modify original
original[0] = 999

print(f"Original: {original}")
print(f"View (should be modified): {view}")
print(f"Copy (should NOT be modified): {copy}")

# 4. Memory-efficient calculations
print(f"\n4. MEMORY-EFFICIENT OPERATIONS:")
print(f"Original array: {age}")

# In-place operations (more efficient)
age_copy = age.copy()
age_copy += 10  # In-place addition
print(f"After +=10 (in-place): {age_copy}")

# Regular operations (creates new array)
age_new = age + 10
print(f"After +10 (new array): {age_new}")

print("\n📚 Memory Tips:")
print("• NumPy arrays use much less memory")
print("• Choose appropriate dtype (int32 vs float64)")
print("• Use views for large arrays")
print("• Use in-place operations when possible")
print("• Be careful with copies vs views")

print("\n✅ Lab 3 Complete!")



print("🎯 Lab 4: NumPy Integration with Other Libraries\n")

import matplotlib.pyplot as plt

age = titanic_df['Age'].values
fare = titanic_df['Fare'].values
survived = titanic_df['Survived'].values

# 1. NumPy to Pandas
print("\n1. NUMPY TO PANDAS:")
age_array = age
age_series = pd.Series(age_array, name='Age')
print(f"NumPy array: {age_array}")
print(f"Pandas Series: {age_series}")

# 2. Pandas to NumPy
print("\n2. PANDAS TO NUMPY:")
age_series = titanic_df['Age']
age_array = age_series.values
print(f"Pandas Series: {age_series.values}")
print(f"NumPy array: {age_array}")

# 3. NumPy calculations for visualization
print("\n3. CALCULATIONS FOR VISUALIZATION:")
# Calculate statistics
survivors_age = age[survived == 1]
non_survivors_age = age[survived == 0]

print(f"Survivors - Mean: {survivors_age.mean():.2f}, Std: {survivors_age.std():.2f}")
print(f"Non-survivors - Mean: {non_survivors_age.mean():.2f}, Std: {non_survivors_age.std():.2f}")

# 4. Create visualization
print("\n4. PLOTTING WITH NUMPY DATA:")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Histogram with NumPy calculated bins
ages_sorted = np.sort(age)
axes[0].hist(age, bins=5, alpha=0.7, color='blue', edgecolor='black')
axes[0].axvline(np.mean(age), color='red', linestyle='--', linewidth=2, label=f'Mean: {np.mean(age):.1f}')
axes[0].set_title('Age Distribution')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Count')
axes[0].legend()

# Scatter with color coding
colors = np.where(survived == 1, 'green', 'red')
axes[1].scatter(age, fare, c=colors, alpha=0.6, s=100)
axes[1].set_title('Age vs Fare (Green=Survived, Red=Died)')
axes[1].set_xlabel('Age')
axes[1].set_ylabel('Fare')

plt.tight_layout()
plt.show()

print("Visualization created using NumPy calculations!")

# 5. Statistical summary using NumPy
print("\n5. STATISTICAL SUMMARY:")
print(f"Age - Mean: {np.mean(age):.2f}, Median: {np.median(age):.2f}, Std: {np.std(age):.2f}")
print(f"Fare - Mean: £{np.mean(fare):.2f}, Median: £{np.median(fare):.2f}, Std: £{np.std(fare):.2f}")
print(f"Survival rate: {np.sum(survived)/len(survived)*100:.1f}%")

print("\n📚 Integration Tips:")
print("• .values converts pandas to NumPy")
print("• pd.Series/DataFrame accept NumPy arrays")
print("• Use NumPy for calculations")
print("• Pass results to matplotlib for plotting")
print("• Combine strengths of both libraries")

print("\n✅ Lab 4 Complete!")




print("🎯 PRACTICE PROJECT: Complete NumPy Data Pipeline\n")

print("=" * 70)
print("COMPREHENSIVE NUMPY OPTIMIZATION & INTEGRATION PIPELINE")
print("=" * 70)

# 1. Load and prepare data
print("\n1. DATA PREPARATION:")
age = titanic_df['Age'].values
fare = titanic_df['Fare'].values
pclass = titanic_df['Pclass'].values
survived = titanic_df['Survived'].values

print(f"Dataset loaded: {len(age)} passengers")
print(f"Data types: Age={age.dtype}, Fare={fare.dtype}")

# 2. Performance comparison
print("\n2. PERFORMANCE COMPARISON:")
# Standardize age (slow way)
start = time.time()
age_std_slow = []
for a in age:
    std = (a - age.mean()) / age.std()
    age_std_slow.append(std)
age_std_slow = np.array(age_std_slow)
time_slow = time.time() - start

# Standardize age (fast way)
start = time.time()
age_std_fast = (age - age.mean()) / age.std()
time_fast = time.time() - start

print(f"Slow (loop): {time_slow*1000:.4f}ms")
print(f"Fast (vectorized): {time_fast*1000:.4f}ms")
print(f"Speedup: {time_slow/time_fast:.1f}x")

# 3. Feature engineering pipeline
print("\n3. FEATURE ENGINEERING PIPELINE:")

# Normalize features
age_norm = (age - age.min()) / (age.max() - age.min())
fare_norm = (fare - fare.min()) / (fare.max() - fare.min())

# Create derived features
age_squared = age ** 2
fare_log = np.log1p(fare)
age_fare_interaction = age * fare

# Bin age
age_binned = np.select(
    [age < 13, (age >= 13) & (age < 18), (age >= 18) & (age < 35), age >= 35],
    [0, 1, 2, 3]
)

print(f"Features created: {4 + 3}")  # 4 engineered + 3 base = 7
print(f"Normalization: ✓")
print(f"Log transformation: ✓")
print(f"Interaction features: ✓")
print(f"Binning: ✓")

# 4. Build feature matrix
print("\n4. FEATURE MATRIX:")
feature_matrix = np.column_stack((
    age,                    # 1. Original age
    fare,                   # 2. Original fare
    age_norm,              # 3. Normalized age
    fare_norm,             # 4. Normalized fare
    age_squared,           # 5. Age²
    fare_log,              # 6. Log(fare)
    age_fare_interaction   # 7. Age × Fare
))

print(f"Feature matrix shape: {feature_matrix.shape}")
print(f"First 5 rows:")
print(feature_matrix[:5])

# 5. Statistical analysis
print("\n5. STATISTICAL ANALYSIS:")
print(f"\nOverall Statistics:")
print(f"{'Feature':<15} {'Mean':<12} {'Std':<12} {'Min':<12} {'Max':<12}")
print("=" * 51)

feature_names = ['Age', 'Fare', 'Age_norm', 'Fare_norm', 'Age²', 'Log(Fare)', 'Age×Fare']
for i, name in enumerate(feature_names):
    col = feature_matrix[:, i]
    print(f"{name:<15} {np.mean(col):<12.2f} {np.std(col):<12.2f} {np.min(col):<12.2f} {np.max(col):<12.2f}")

# 6. Survival analysis
print("\n6. SURVIVAL ANALYSIS:")
survivor_mask = survived == 1
non_survivor_mask = survived == 0

print(f"\nSurvivors ({np.sum(survivor_mask)}):")
print(f"  Mean age: {age[survivor_mask].mean():.2f}")
print(f"  Mean fare: £{fare[survivor_mask].mean():.2f}")
print(f"  Class distribution: {pd.Series(pclass[survivor_mask]).value_counts().to_dict()}")

print(f"\nNon-survivors ({np.sum(non_survivor_mask)}):")
print(f"  Mean age: {age[non_survivor_mask].mean():.2f}")
print(f"  Mean fare: £{fare[non_survivor_mask].mean():.2f}")
print(f"  Class distribution: {pd.Series(pclass[non_survivor_mask]).value_counts().to_dict()}")

# 7. Outlier detection and handling
print("\n7. OUTLIER DETECTION & HANDLING:")
q1_age = np.percentile(age, 25)
q3_age = np.percentile(age, 75)
iqr_age = q3_age - q1_age

outlier_threshold_low = q1_age - 1.5 * iqr_age
outlier_threshold_high = q3_age + 1.5 * iqr_age

age_outliers = (age < outlier_threshold_low) | (age > outlier_threshold_high)
print(f"Age outliers detected: {np.sum(age_outliers)}")
print(f"Outlier values: {age[age_outliers]}")

# Cap outliers
age_capped = np.clip(age, outlier_threshold_low, outlier_threshold_high)
print(f"Original age range: [{age.min()}, {age.max()}]")
print(f"After capping: [{age_capped.min():.2f}, {age_capped.max():.2f}]")

# 8. Memory efficiency summary
print("\n8. MEMORY EFFICIENCY:")
list_size = sys.getsizeof(list(age)) + sum(sys.getsizeof(x) for x in age)
array_size = age.nbytes
print(f"Python list: {list_size} bytes")
print(f"NumPy array: {array_size} bytes")
print(f"Memory saved: {(1 - array_size/list_size)*100:.1f}%")

# 9. Final summary
print("\n" + "=" * 70)
print("PIPELINE SUMMARY:")
print("=" * 70)

print(f"\n✓ Performance optimizations applied")
print(f"✓ Vectorized all calculations")
print(f"✓ Created 7 engineered features")
print(f"✓ Standardized features")
print(f"✓ Detected and handled outliers")
print(f"✓ Built feature matrix ({feature_matrix.shape})")
print(f"✓ Memory efficient (~{array_size/1024:.1f} KB)")

print(f"\n✓ Key Metrics:")
print(f"  - Survival rate: {(np.sum(survived)/len(survived)*100):.1f}%")
print(f"  - Average age: {age.mean():.1f} years")
print(f"  - Average fare: £{fare.mean():.2f}")
print(f"  - Features engineered: 7")
print(f"  - Data points: {len(age)}")

print("\n✅ Lab 5 Complete!")
print("🎉 Part 6 Complete: NumPy optimization & integration mastered!")
print("🎊 WEEK 16 FULLY COMPLETE!")



commands = {
    'Vectorize': 'array + 5 (instead of loop)',
    'Conditional': 'np.where(condition, value_if_true, value_if_false)',
    'Multiple conditions': 'np.select([cond1, cond2], [val1, val2])',
    'In-place op': 'array += 5',
    'View': 'array[:]',
    'Copy': 'array.copy()',
    'Data type': 'array.astype(np.float32)',
    'Memory size': 'array.nbytes',
    'Array size': 'sys.getsizeof(array)',
    'Performance': 'time.time() for timing'
}

print("📚 OPTIMIZATION COMMANDS:")
for concept, command in commands.items():
    print(f"• {concept:20}: {command}")



print("\n💾 Part 6 Summary:")
print("✅ What we learned:")
print("  • NumPy is 10-100x faster than lists")
print("  • Vectorization replaces loops")
print("  • Memory efficiency with arrays")
print("  • In-place operations save memory")
print("  • Integration with Pandas & Matplotlib")
print("  • Complete data pipeline")
print("\n🎊 WEEK 16 COMPLETE - Ready for Week 17!")
