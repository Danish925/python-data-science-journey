import numpy as np
import pandas as pd

print("🎯 Lab 1: Reshaping Arrays\n")

# Load Titanic data
titanic_df = pd.DataFrame({
    'Age': [22, 38, 26, 35, 54, 2, 27, 14, 58, 20],
    'Fare': [7.25, 71.28, 7.92, 53.10, 51.86, 21.08, 11.13, 30.07, 26.55, 8.05],
    'Pclass': [3, 1, 3, 1, 1, 3, 3, 2, 1, 3],
    'Survived': [0, 1, 1, 1, 0, 0, 0, 1, 0, 0]
})

# Convert to arrays
age = titanic_df['Age'].values
fare = titanic_df['Fare'].values

print("Original 1D Age array:")
print(age)
print(f"Shape: {age.shape}")

# Reshape to 2D (2 rows, 5 columns)
print("\n1. RESHAPE TO 2D (2, 5):")
age_2d = age.reshape(2, 5)
print(age_2d)
print(f"Shape: {age_2d.shape}")

# Reshape to 2D (5 rows, 2 columns)
print("\n2. RESHAPE TO 2D (5, 2):")
age_2d_alt = age.reshape(5, 2)
print(age_2d_alt)
print(f"Shape: {age_2d_alt.shape}")

# Reshape with -1 (automatic calculation)
print("\n3. RESHAPE WITH -1 (Auto-calculate):")
age_2d_auto = age.reshape(2, -1)  # -1 means "calculate this dimension"
print(age_2d_auto)
print(f"Shape: {age_2d_auto.shape}")

# Another example with -1
age_2d_auto2 = age.reshape(-1, 5)  # Calculate rows automatically
print(f"\nReshape to (-1, 5):")
print(age_2d_auto2)
print(f"Shape: {age_2d_auto2.shape}")

print("\n📚 Reshaping Rules:")
print("• Total elements must stay the same")
print("• reshape(2, 5) = 10 elements")
print("• Use -1 to auto-calculate one dimension")
print("• reshape(-1, 1) = Convert to column vector")
print("• reshape(1, -1) = Convert to row vector")

print("\n✅ Lab 1 Complete!")




print("🎯 Lab 2: Flattening Arrays\n")

# Create 2D array
print("Original 2D array:")
age_2d = age.reshape(2, 5)
print(age_2d)
print(f"Shape: {age_2d.shape}")

# Flatten to 1D
print("\n1. FLATTENING TO 1D:")
age_flat = age_2d.flatten()
print(age_flat)
print(f"Shape: {age_flat.shape}")

# Alternative: Using reshape(-1)
print("\n2. ALTERNATIVE: RESHAPE(-1):")
age_flat_alt = age_2d.reshape(-1)
print(age_flat_alt)
print(f"Shape: {age_flat_alt.shape}")

# Create 3D array
print("\n3. 3D ARRAY EXAMPLE:")
data_3d = np.arange(24).reshape(2, 3, 4)
print("3D Array (2, 3, 4):")
print(data_3d)
print(f"Shape: {data_3d.shape}")

# Flatten 3D to 1D
print("\n4. FLATTEN 3D TO 1D:")
data_3d_flat = data_3d.flatten()
print(data_3d_flat)
print(f"Shape: {data_3d_flat.shape}")

# Reshape back to 3D
print("\n5. RESHAPE FLAT BACK TO 3D:")
data_3d_restored = data_3d_flat.reshape(2, 3, 4)
print(data_3d_restored)
print(f"Shape: {data_3d_restored.shape}")

print("\n📚 Flattening Functions:")
print("• array.flatten(): Convert to 1D (copy)")
print("• array.reshape(-1): Convert to 1D (view)")
print("• Both return 1D array, but different memory usage")

print("\n✅ Lab 2 Complete!")



print("🎯 Lab 3: Transposing Arrays\n")

# Create 2D array
print("Original 2D array (2, 5):")
age_2d = age.reshape(2, 5)
print(age_2d)
print(f"Shape: {age_2d.shape}")

# Transpose
print("\n1. TRANSPOSE (.T):")
age_transposed = age_2d.T
print(age_transposed)
print(f"Shape: {age_transposed.shape}")

# Transpose method
print("\n2. TRANSPOSE METHOD:")
age_transposed2 = np.transpose(age_2d)
print(age_transposed2)
print(f"Shape: {age_transposed2.shape}")

# Create combined 2D array
print("\n3. REAL EXAMPLE - COMBINE FEATURES:")
combined = np.column_stack((age, fare))
print("Age and Fare combined (10, 2):")
print(combined[:5])  # Show first 5 rows
print(f"Shape: {combined.shape}")

# Transpose combined
print("\n4. TRANSPOSE COMBINED ARRAY:")
combined_T = combined.T
print("Transposed (2, 10):")
print(combined_T)
print(f"Shape: {combined_T.shape}")

# Axis swapping for 3D
print("\n5. SWAPPING AXES IN 3D ARRAY:")
data_3d = np.arange(24).reshape(2, 3, 4)
print("Original shape (2, 3, 4):")
print(data_3d.shape)

data_3d_swapped = np.swapaxes(data_3d, 0, 2)
print("After swapping axes 0 and 2:")
print(f"New shape: {data_3d_swapped.shape}")

print("\n📚 Transpose Functions:")
print("• array.T: Quick transpose")
print("• np.transpose(array): Explicit transpose")
print("• np.swapaxes(array, axis1, axis2): Swap specific axes")
print("• Useful for reshaping data for algorithms")

print("\n✅ Lab 3 Complete!")




print("🎯 Lab 4: Broadcasting\n")

print("Age array:", age)
print("Shape:", age.shape)

# Broadcasting with scalar
print("\n1. SCALAR BROADCASTING:")
age_plus_10 = age + 10
print(f"Age + 10: {age_plus_10}")
print("The scalar 10 was broadcast to all elements")

# Broadcasting with 1D array
print("\n2. 1D ARRAY OPERATIONS:")
ages_2d = age.reshape(2, 5)
print("Ages (2, 5):")
print(ages_2d)

# Add a 1D array to each row
row_values = np.array([1, 2, 3, 4, 5])
print(f"\nRow values (5,): {row_values}")
print("\n2D + 1D (broadcasting):")
result = ages_2d + row_values
print(result)
print("The 1D array was broadcast to each row")

# Broadcasting example 2
print("\n3. BROADCASTING WITH COLUMN:")
column_values = np.array([[10], [20]])
print("Column values (2, 1):")
print(column_values)
print("\n2D + Column (broadcasting):")
result2 = ages_2d + column_values
print(result2)
print("The column was broadcast to each column")

# Real example: Normalize data
print("\n4. NORMALIZATION EXAMPLE:")
print("Original data (Age, Fare):")
data = np.column_stack((age, fare))
print(data[:3])

# Calculate mean of each column
col_means = np.mean(data, axis=0)
print(f"\nColumn means: {col_means}")
print(f"Shape of means: {col_means.shape}")

# Subtract means (broadcasting)
normalized = data - col_means
print(f"\nNormalized data (first 3 rows):")
print(normalized[:3])

print("\n📚 Broadcasting Rules:")
print("• When shapes don't match, expand smaller to match larger")
print("• Scalar can broadcast to any shape")
print("• Dimension size 1 can broadcast to any larger size")
print("• Dimensions must be compatible or one must be 1")

print("\n✅ Lab 4 Complete!")




print("🎯 PRACTICE PROJECT: Reshaping & Broadcasting Summary\n")

print("=" * 70)
print("RESHAPING & BROADCASTING COMPREHENSIVE ANALYSIS")
print("=" * 70)

# 1. Original data
print("\n1. ORIGINAL DATA:")
print(f"Age shape: {age.shape}")
print(f"Fare shape: {fare.shape}")
print(f"Age values: {age}")
print(f"Fare values: {fare}")

# 2. Reshape examples
print("\n2. RESHAPING EXAMPLES:")
age_2d = age.reshape(2, 5)
print(f"\nAge reshaped to (2, 5):")
print(age_2d)

age_col = age.reshape(-1, 1)
print(f"\nAge reshaped to column (-1, 1):")
print(age_col)

age_row = age.reshape(1, -1)
print(f"\nAge reshaped to row (1, -1):")
print(age_row)

# 3. Transpose
print("\n3. TRANSPOSE OPERATIONS:")
print(f"Original shape: {age_2d.shape}")
print(f"Transposed shape: {age_2d.T.shape}")
print("Original (2, 5):")
print(age_2d)
print("\nTransposed (5, 2):")
print(age_2d.T)

# 4. Combine data
print("\n4. COMBINING FEATURES:")
combined = np.column_stack((age, fare, titanic_df['Survived'].values))
print(f"Combined shape: {combined.shape}")
print("Combined data (Age, Fare, Survived) - first 5 rows:")
print(combined[:5])

# 5. Broadcasting examples
print("\n5. BROADCASTING OPERATIONS:")
print(f"\nOriginal combined (10, 3):")
print(combined[:5])

# Normalize each column
means = np.mean(combined, axis=0)
print(f"\nColumn means: {means}")

normalized = combined - means
print(f"Normalized (broadcasting) - first 5 rows:")
print(normalized[:5])

# Scale by standard deviation
stds = np.std(combined, axis=0)
print(f"\nColumn std devs: {stds}")

standardized = (combined - means) / stds
print(f"Standardized (z-score) - first 5 rows:")
print(standardized[:5])

# 6. Flatten and reshape
print("\n6. FLATTEN & RESHAPE CYCLE:")
print(f"Original combined shape: {combined.shape}")
flattened = combined.flatten()
print(f"Flattened shape: {flattened.shape}")
print(f"Flattened values (first 5): {flattened[:5]}")

reshaped_back = flattened.reshape(combined.shape)
print(f"Reshaped back shape: {reshaped_back.shape}")
print(f"Values match original: {np.allclose(reshaped_back, combined)}")

# 7. Advanced reshaping - FIXED
print("\n7. ADVANCED RESHAPING:")
print(f"Combined data has shape: {combined.shape} (10 rows × 3 columns)")

# Create 3D array - CORRECT CALCULATION
# We have 10 elements per feature, so we can reshape to (2, 5, 3)
# Or reshape age alone to (2, 5, 1) then add others
print("\nOption 1: Reshape age to 3D (2, 5, 1):")
age_3d = age.reshape(2, 5, 1)
print(f"Shape: {age_3d.shape}")
print(age_3d)

print("\nOption 2: Reshape combined to 3D (2, 5, 3):")
# Take only first 10 rows (or we already have 10), reshape to (2, 5, 3)
combined_3d = combined.reshape(2, 5, 3)
print(f"Shape: {combined_3d.shape}")
print(combined_3d)

print("\nOption 3: Expand dimensions (add new dimension):")
combined_expanded = np.expand_dims(combined, axis=0)
print(f"Original shape: {combined.shape}")
print(f"After expand_dims: {combined_expanded.shape}")

print("\nOption 4: Squeeze (remove dimension of size 1):")
single_col = combined[:, 0:1]  # Take first column as (10, 1)
print(f"Single column shape: {single_col.shape}")
squeezed = np.squeeze(single_col)
print(f"After squeeze: {squeezed.shape}")

# 8. Summary
print("\n" + "=" * 70)
print("OPERATIONS MASTERED:")
print("=" * 70)

operations = {
    'Reshape': 'array.reshape(new_shape)',
    'Reshape auto': 'array.reshape(2, -1)',
    'Flatten': 'array.flatten() or array.reshape(-1)',
    'Transpose': 'array.T or np.transpose(array)',
    'Swap axes': 'np.swapaxes(array, 0, 2)',
    'Stack columns': 'np.column_stack((arr1, arr2))',
    'Stack rows': 'np.vstack((arr1, arr2))',
    'Stack horizontal': 'np.hstack((arr1, arr2))',
    'Expand dims': 'np.expand_dims(array, axis)',
    'Squeeze': 'np.squeeze(array)',
    'Broadcasting': 'array1 + array2 (auto expand)',
    'Normalize': '(array - mean) / std'
}

for operation, example in operations.items():
    print(f"✓ {operation:20}: {example}")

# 9. Key insights
print("\n" + "=" * 70)
print("KEY INSIGHTS:")
print("=" * 70)

print(f"\n✓ Original 1D array (10,) can be reshaped to:")
print(f"  - (2, 5): 2 rows × 5 columns = 10 elements ✓")
print(f"  - (5, 2): 5 rows × 2 columns = 10 elements ✓")
print(f"  - (10, 1): Column vector = 10 elements ✓")
print(f"  - (1, 10): Row vector = 10 elements ✓")
print(f"  - (2, 5, 1): 3D array = 10 elements ✓")
print(f"  - (2, 2, 3): Would need 12 elements ✗")

print(f"\n✓ Combined (10, 3) can be reshaped to:")
print(f"  - (2, 5, 3): 2×5×3 = 30 elements ✓")
print(f"  - (5, 2, 3): 5×2×3 = 30 elements ✓")
print(f"  - (2, 3, 5): 2×3×5 = 30 elements ✓")
print(f"  - (2, 15): 2×15 = 30 elements ✓")

print(f"\n✓ Broadcasting example:")
print(f"  Shape (10,) + Shape (10,) = Shape (10,)")
print(f"  Shape (2, 5) + Shape (5,) = Shape (2, 5) (broadcast column)")
print(f"  Shape (2, 5) + Shape (1, 5) = Shape (2, 5) (broadcast row)")

print(f"\n✓ Normalization pattern:")
print(f"  1. Calculate mean and std of each feature")
print(f"  2. Subtract mean (broadcasting to all rows)")
print(f"  3. Divide by std (broadcasting to all rows)")
print(f"  4. Result: Standardized data (mean≈0, std≈1)")

print(f"\n✓ Important Rule:")
print(f"  Total elements must match!")
print(f"  10 elements can reshape to: (2,5), (5,2), (10,1), (1,10), (2,5,1)")
print(f"  30 elements can reshape to: (2,15), (5,6), (2,3,5), (2,5,3), etc.")

print("\n✅ Lab 5 Complete!")
print("🎉 Part 4 Complete: Reshaping & broadcasting mastered!")



commands = {
    'Reshape': 'array.reshape(2, 5)',
    'Reshape auto': 'array.reshape(-1, 5)',
    'Flatten': 'array.flatten()',
    'Reshape flatten': 'array.reshape(-1)',
    'Transpose': 'array.T',
    'Transpose function': 'np.transpose(array)',
    'Swap axes': 'np.swapaxes(array, 0, 1)',
    'Stack columns': 'np.column_stack((a, b))',
    'Stack vertical': 'np.vstack((a, b))',
    'Stack horizontal': 'np.hstack((a, b))',
    'Concatenate': 'np.concatenate((a, b))',
    'Expand dims': 'np.expand_dims(array, axis)',
    'Squeeze': 'np.squeeze(array)',
    'Normalize': '(array - mean) / std'
}

print("📚 RESHAPING & BROADCASTING COMMANDS:")
for concept, command in commands.items():
    print(f"• {concept:20}: {command}")



print("\n💾 Part 4 Summary:")
print("✅ What we learned:")
print("  • Reshape arrays to different dimensions")
print("  • Use -1 for automatic calculation")
print("  • Flatten arrays to 1D")
print("  • Transpose with .T")
print("  • Broadcasting for combining arrays")
print("  • Normalize data using broadcasting")
print("\n🎯 Next: Part 5 - Feature engineering with NumPy!")
