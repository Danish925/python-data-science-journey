import numpy as np
import pandas as pd

print("🎯 Lab 1: Feature Scaling & Normalization\n")

# Load Titanic data
titanic_df = pd.DataFrame({
    'Age': [22, 38, 26, 35, 54, 2, 27, 14, 58, 20],
    'Fare': [7.25, 71.28, 7.92, 53.10, 51.86, 21.08, 11.13, 30.07, 26.55, 8.05],
    'Pclass': [3, 1, 3, 1, 1, 3, 3, 2, 1, 3],
    'Survived': [0, 1, 1, 1, 0, 0, 0, 1, 0, 0]
})

age = titanic_df['Age'].values
fare = titanic_df['Fare'].values

print("Original Age:", age)
print("Original Fare:", fare)

# 1. Min-Max Normalization (0-1 scale)
print("\n1. MIN-MAX NORMALIZATION (0-1):")
age_min = np.min(age)
age_max = np.max(age)
age_normalized = (age - age_min) / (age_max - age_min)

print(f"Age min: {age_min}, max: {age_max}")
print(f"Normalized Age: {age_normalized}")
print(f"Range: {age_normalized.min():.2f} to {age_normalized.max():.2f}")

# Same for fare
fare_min = np.min(fare)
fare_max = np.max(fare)
fare_normalized = (fare - fare_min) / (fare_max - fare_min)

print(f"\nFare min: £{fare_min:.2f}, max: £{fare_max:.2f}")
print(f"Normalized Fare: {fare_normalized}")
print(f"Range: {fare_normalized.min():.2f} to {fare_normalized.max():.2f}")

# 2. Standardization (Z-score normalization)
print("\n2. STANDARDIZATION (Z-SCORE):")
age_mean = np.mean(age)
age_std = np.std(age)
age_standardized = (age - age_mean) / age_std

print(f"Age mean: {age_mean:.2f}, std: {age_std:.2f}")
print(f"Standardized Age: {age_standardized}")
print(f"Mean: {age_standardized.mean():.4f}, Std: {age_standardized.std():.4f}")

# Same for fare
fare_mean = np.mean(fare)
fare_std = np.std(fare)
fare_standardized = (fare - fare_mean) / fare_std

print(f"\nFare mean: £{fare_mean:.2f}, std: £{fare_std:.2f}")
print(f"Standardized Fare: {fare_standardized}")
print(f"Mean: {fare_standardized.mean():.4f}, Std: {fare_standardized.std():.4f}")

# 3. Robust Scaling (using median and IQR)
print("\n3. ROBUST SCALING (Median & IQR):")
age_median = np.median(age)
age_q1 = np.percentile(age, 25)
age_q3 = np.percentile(age, 75)
age_iqr = age_q3 - age_q1
age_robust = (age - age_median) / age_iqr

print(f"Age median: {age_median:.2f}, IQR: {age_iqr:.2f}")
print(f"Robust scaled Age: {age_robust}")

print("\n📚 Scaling Methods:")
print("• Min-Max: (x - min) / (max - min) → Range [0, 1]")
print("• Standardization: (x - mean) / std → Mean 0, Std 1")
print("• Robust: (x - median) / IQR → Resistant to outliers")

print("\n✅ Lab 1 Complete!")



print("🎯 Lab 2: Binning Continuous Variables\n")

print("Original Age:", age)

# 1. Equal-width binning using pandas
print("\n1. EQUAL-WIDTH BINNING:")
age_bins_equal = pd.cut(age, bins=3)
print(f"Age binned into 3 equal-width bins:")
print(age_bins_equal)

# Show bin edges
age_bins_equal, bin_edges = pd.cut(age, bins=3, retbins=True)
print(f"Bin edges: {bin_edges}")

# 2. Equal-frequency binning (quantile-based)
print("\n2. EQUAL-FREQUENCY BINNING (Quartiles):")
age_bins_quantile = pd.qcut(age, q=4, duplicates='drop')
print(f"Age binned into quartiles:")
print(age_bins_quantile)

# 3. Custom binning with pandas
print("\n3. CUSTOM BINNING:")
custom_bins = [0, 13, 18, 35, 60, 100]
bin_labels = ['Infant', 'Child', 'Teen', 'Adult', 'Senior']
age_bins_custom = pd.cut(age, bins=custom_bins, labels=bin_labels)
print(f"Age binned with custom labels:")
print(age_bins_custom)

# 4. Create binary features from binning (using NumPy)
print("\n4. BINARY FEATURES FROM BINNING (NumPy):")
is_child = (age < 18).astype(int)
is_adult = ((age >= 18) & (age < 60)).astype(int)
is_senior = (age >= 60).astype(int)

print(f"Is Child: {is_child}")
print(f"Is Adult: {is_adult}")
print(f"Is Senior: {is_senior}")

# 5. Fare binning using pandas
print("\n5. FARE BINNING:")
fare_bins = pd.cut(fare, bins=[0, 10, 30, 100, 300], 
                   labels=['Budget', 'Standard', 'Premium', 'Luxury'])
print(f"Fare categories:")
print(fare_bins)

# 6. NumPy-only approach: Create bins manually
print("\n6. PURE NUMPY BINNING (Manual):")
# Create custom bins for age
age_binned_numpy = np.zeros(len(age), dtype=int)
age_binned_numpy[age < 13] = 0  # Infant
age_binned_numpy[(age >= 13) & (age < 18)] = 1  # Child
age_binned_numpy[(age >= 18) & (age < 35)] = 2  # Teen/Young Adult
age_binned_numpy[(age >= 35) & (age < 60)] = 3  # Adult
age_binned_numpy[age >= 60] = 4  # Senior

bin_names = ['Infant', 'Child', 'Teen/YA', 'Adult', 'Senior']
print(f"Age bin indices: {age_binned_numpy}")
print(f"Bin mapping: 0=Infant, 1=Child, 2=Teen/YA, 3=Adult, 4=Senior")

for i, name in enumerate(bin_names):
    count = np.sum(age_binned_numpy == i)
    if count > 0:
        print(f"  {name}: {count} passengers")

print("\n📚 Binning Functions:")
print("• pd.cut(): Fixed-width bins (PANDAS)")
print("• pd.qcut(): Quantile-based bins (PANDAS)")
print("• Custom numpy: np.zeros() + boolean masking")
print("• .astype(int): Convert boolean to 0/1")

print("\n✅ Lab 2 Complete!")




print("🎯 Lab 3: Creating Interaction Features\n")

pclass = titanic_df['Pclass'].values
survived = titanic_df['Survived'].values

print("Age:", age)
print("Fare:", fare)
print("Pclass:", pclass)

# 1. Simple multiplication
print("\n1. MULTIPLICATION INTERACTION:")
age_fare_interaction = age * fare
print(f"Age × Fare: {age_fare_interaction}")

# 2. Polynomial features
print("\n2. POLYNOMIAL FEATURES:")
age_squared = age ** 2
age_cubed = age ** 3
fare_squared = fare ** 2

print(f"Age²: {age_squared}")
print(f"Age³: {age_cubed}")
print(f"Fare²: {fare_squared}")

# 3. Ratio features
print("\n3. RATIO FEATURES:")
fare_per_year = fare / (age + 1)  # +1 to avoid division by zero
print(f"Fare per year of age: {fare_per_year}")

# 4. Combined class features
print("\n4. CLASS-BASED FEATURES:")
class_age = pclass * age
class_fare = pclass * fare

print(f"Pclass × Age: {class_age}")
print(f"Pclass × Fare: {class_fare}")

# 5. Family size feature (simulated)
print("\n5. DERIVED FEATURES:")
# Simulate SibSp and Parch (siblings/spouse and parents/children)
sibsp = np.array([1, 1, 0, 1, 0, 0, 3, 0, 1, 1])
parch = np.array([0, 0, 0, 0, 0, 0, 1, 0, 0, 1])
family_size = 1 + sibsp + parch  # Include self

print(f"SibSp: {sibsp}")
print(f"Parch: {parch}")
print(f"Family Size: {family_size}")

# 6. Log transformation
print("\n6. LOG TRANSFORMATION (for skewed features):")
fare_log = np.log1p(fare)  # log1p = log(1 + x) to handle zeros
print(f"Original Fare: {fare}")
print(f"Log(Fare): {fare_log}")

print("\n📚 Feature Engineering:")
print("• Interaction: x1 * x2")
print("• Polynomial: x², x³, etc.")
print("• Ratio: x1 / x2")
print("• Log: np.log1p(x)")
print("• Binary flags: (x > threshold).astype(int)")

print("\n✅ Lab 3 Complete!")



print("🎯 Lab 4: Detecting and Handling Outliers\n")

print("Age:", age)
print("Fare:", fare)

# 1. Statistical method - Z-score
print("\n1. Z-SCORE METHOD:")
age_mean = np.mean(age)
age_std = np.std(age)
age_zscore = np.abs((age - age_mean) / age_std)
outlier_threshold = 3

print(f"Age mean: {age_mean:.2f}, std: {age_std:.2f}")
print(f"Z-scores: {age_zscore}")

age_outliers_zscore = age_zscore > outlier_threshold
print(f"Outliers (Z-score > 3): {age[age_outliers_zscore]}")
print(f"Outlier indices: {np.where(age_outliers_zscore)[0]}")

# 2. IQR method
print("\n2. IQR METHOD:")
q1 = np.percentile(age, 25)
q3 = np.percentile(age, 75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print(f"Q1: {q1:.2f}, Q3: {q3:.2f}, IQR: {iqr:.2f}")
print(f"Lower bound: {lower_bound:.2f}, Upper bound: {upper_bound:.2f}")

age_outliers_iqr = (age < lower_bound) | (age > upper_bound)
print(f"Outliers (IQR method): {age[age_outliers_iqr]}")
print(f"Outlier indices: {np.where(age_outliers_iqr)[0]}")

# 3. Handle outliers - Cap values
print("\n3. HANDLING OUTLIERS - CAP VALUES:")
age_capped = np.clip(age, lower_bound, upper_bound)
print(f"Original Age: {age}")
print(f"Capped Age: {age_capped}")

# Do the same for fare
print("\n4. HANDLE FARE OUTLIERS:")
fare_q1 = np.percentile(fare, 25)
fare_q3 = np.percentile(fare, 75)
fare_iqr = fare_q3 - fare_q1
fare_lower = fare_q1 - 1.5 * fare_iqr
fare_upper = fare_q3 + 1.5 * fare_iqr

print(f"Fare Q1: £{fare_q1:.2f}, Q3: £{fare_q3:.2f}")
print(f"Outlier range: £{fare_lower:.2f} to £{fare_upper:.2f}")

fare_outliers = (fare < fare_lower) | (fare > fare_upper)
print(f"Outlier fares: {fare[fare_outliers]}")
print(f"Outlier indices: {np.where(fare_outliers)[0]}")

fare_capped = np.clip(fare, fare_lower, fare_upper)
print(f"\nOriginal Fare: {fare}")
print(f"Capped Fare: {fare_capped}")

# 5. Remove outliers
print("\n5. REMOVE OUTLIERS:")
valid_mask = ~age_outliers_iqr
age_cleaned = age[valid_mask]
print(f"Original count: {len(age)}")
print(f"After removing outliers: {len(age_cleaned)}")
print(f"Cleaned Age: {age_cleaned}")

print("\n📚 Outlier Methods:")
print("• Z-score: |z| > 3 (or 2.5)")
print("• IQR: Outside [Q1 - 1.5×IQR, Q3 + 1.5×IQR]")
print("• Handling: Cap, remove, or transform")
print("• np.clip(): Cap values to range")
print("• Boolean masking: Filter outliers")

print("\n✅ Lab 4 Complete!")




print("🎯 PRACTICE PROJECT: Feature Engineering Summary\n")

print("=" * 70)
print("COMPREHENSIVE FEATURE ENGINEERING ANALYSIS")
print("=" * 70)

# 1. Original features
print("\n1. ORIGINAL FEATURES:")
print(f"Age: {age}")
print(f"Fare: {fare}")
print(f"Pclass: {pclass}")

# 2. Scaled features
print("\n2. NORMALIZED FEATURES (Min-Max):")
age_norm = (age - np.min(age)) / (np.max(age) - np.min(age))
fare_norm = (fare - np.min(fare)) / (np.max(fare) - np.min(fare))

print(f"Age (normalized): {age_norm}")
print(f"Fare (normalized): {fare_norm}")

# 3. Standardized features
print("\n3. STANDARDIZED FEATURES (Z-score):")
age_std = (age - np.mean(age)) / np.std(age)
fare_std = (fare - np.mean(fare)) / np.std(fare)

print(f"Age (standardized): {age_std}")
print(f"Fare (standardized): {fare_std}")

# 4. Binned features
print("\n4. BINNED FEATURES:")
age_binned = pd.cut(age, bins=[0, 13, 18, 35, 60, 100], 
                    labels=['Infant', 'Child', 'Teen', 'Adult', 'Senior'])
fare_binned = pd.cut(fare, bins=[0, 10, 30, 100, 300],
                     labels=['Budget', 'Standard', 'Premium', 'Luxury'])

print(f"Age categories: {list(age_binned)}")
print(f"Fare categories: {list(fare_binned)}")

# 5. Interaction features
print("\n5. INTERACTION FEATURES:")
age_fare_mult = age * fare
age_class_mult = age * pclass
fare_class_mult = fare * pclass

print(f"Age × Fare: {age_fare_mult}")
print(f"Age × Pclass: {age_class_mult}")
print(f"Fare × Pclass: {fare_class_mult}")

# 6. Polynomial features
print("\n6. POLYNOMIAL FEATURES:")
age_squared = age ** 2
fare_squared = fare ** 2

print(f"Age²: {age_squared}")
print(f"Fare²: {fare_squared}")

# 7. Log transformation
print("\n7. LOG TRANSFORMATION:")
age_log = np.log1p(age)
fare_log = np.log1p(fare)

print(f"Log(Age): {age_log}")
print(f"Log(Fare): {fare_log}")

# 8. Outlier detection
print("\n8. OUTLIER DETECTION:")
age_q1 = np.percentile(age, 25)
age_q3 = np.percentile(age, 75)
age_iqr = age_q3 - age_q1
age_lower = age_q1 - 1.5 * age_iqr
age_upper = age_q3 + 1.5 * age_iqr

age_outliers = (age < age_lower) | (age > age_upper)
print(f"Age outlier bounds: [{age_lower:.2f}, {age_upper:.2f}]")
print(f"Outlier flags: {age_outliers.astype(int)}")
print(f"Outlier values: {age[age_outliers]}")

# 9. Combine all engineered features
print("\n9. COMBINED FEATURE MATRIX:")
engineered_features = np.column_stack((
    age_norm,           # Normalized Age
    fare_norm,          # Normalized Fare
    age_std,            # Standardized Age
    fare_std,           # Standardized Fare
    age_fare_mult,      # Interaction
    age_squared,        # Polynomial
    fare_log            # Log transformation
))

print("Feature matrix (first 5 rows):")
print("Age_norm, Fare_norm, Age_std, Fare_std, Age×Fare, Age², Log(Fare)")
print(engineered_features[:5])

# 10. Feature statistics
print("\n10. FEATURE STATISTICS:")
print(f"{'Feature':<20} {'Mean':<12} {'Std':<12} {'Min':<12} {'Max':<12}")
print("=" * 56)

feature_names = ['Age', 'Fare', 'Age_norm', 'Fare_norm', 'Age_std', 'Fare_std']
feature_arrays = [age, fare, age_norm, fare_norm, age_std, fare_std]

for name, arr in zip(feature_names, feature_arrays):
    print(f"{name:<20} {np.mean(arr):<12.2f} {np.std(arr):<12.2f} {np.min(arr):<12.2f} {np.max(arr):<12.2f}")

# 11. Summary
print("\n" + "=" * 70)
print("FEATURE ENGINEERING TECHNIQUES MASTERED:")
print("=" * 70)

techniques = {
    'Min-Max Normalization': '(x - min) / (max - min)',
    'Standardization': '(x - mean) / std',
    'Binning (Equal-width)': 'np.cut()',
    'Binning (Quantile)': 'pd.qcut()',
    'Multiplication': 'x1 * x2',
    'Polynomial': 'x², x³, etc.',
    'Log Transform': 'np.log1p(x)',
    'Ratio': 'x1 / x2',
    'Z-score Outliers': '|(x - mean) / std| > 3',
    'IQR Outliers': 'Outside [Q1-1.5×IQR, Q3+1.5×IQR]',
    'Cap Values': 'np.clip()',
    'Remove Outliers': 'Boolean masking'
}

for technique, formula in techniques.items():
    print(f"✓ {technique:25}: {formula}")

# 12. Key insights
print("\n" + "=" * 70)
print("KEY INSIGHTS:")
print("=" * 70)

print(f"\n✓ Scaling Impact:")
print(f"  Age: Original range [{age.min()}, {age.max()}]")
print(f"       Normalized range [{age_norm.min():.2f}, {age_norm.max():.2f}]")
print(f"       Standardized mean: {age_std.mean():.4f}, std: {age_std.std():.4f}")

print(f"\n✓ Outlier Impact:")
print(f"  Age outliers detected: {np.sum(age_outliers)}")
print(f"  Original mean: {np.mean(age):.2f}")
print(f"  After capping: {np.mean(np.clip(age, age_lower, age_upper)):.2f}")

print(f"\n✓ Feature Transformations:")
print(f"  Original features: {len(feature_arrays)}")
print(f"  Engineered features: {engineered_features.shape[1]}")
print(f"  Total usable features: {len(feature_arrays) + engineered_features.shape[1]}")

print("\n✅ Lab 5 Complete!")
print("🎉 Part 5 Complete: Feature engineering mastered!")
print("🎊 WEEK 16 COMPLETE: NumPy fundamentals mastered!")



commands = {
    'Min-Max': '(x - x.min()) / (x.max() - x.min())',
    'Standardize': '(x - x.mean()) / x.std()',
    'Robust scale': '(x - median) / IQR',
    'Binning equal': 'np.cut(x, bins=5)',
    'Binning quantile': 'pd.qcut(x, q=4)',
    'Interaction': 'x1 * x2',
    'Polynomial': 'x ** 2',
    'Log transform': 'np.log1p(x)',
    'Z-score': '(x - mean) / std',
    'Clip values': 'np.clip(x, min, max)',
    'Detect outliers': '(x < lower) | (x > upper)',
    'Remove outliers': 'x[~outlier_mask]'
}

print("📚 FEATURE ENGINEERING COMMANDS:")
for concept, command in commands.items():
    print(f"• {concept:20}: {command}")



print("\n💾 Part 5 Summary:")
print("✅ What we learned:")
print("  • Min-Max normalization [0, 1]")
print("  • Standardization (Z-score)")
print("  • Binning continuous variables")
print("  • Creating interaction features")
print("  • Polynomial transformations")
print("  • Detecting outliers (Z-score & IQR)")
print("  • Handling outliers (cap, remove)")
print("  • Log transformations")
print("\n🎯 WEEK 16 COMPLETE - Ready for Week 17!")
