import numpy as np
import pandas as pd

print("🎯 Lab 1: NumPy Basics\n")

# Check NumPy version
print(f"NumPy version: {np.__version__}")

# Load Titanic data
titanic_df = pd.DataFrame({
    'Age': [22, 38, 26, 35, 54, 2, 27, 14, 58, 20],
    'Fare': [7.25, 71.28, 7.92, 53.10, 51.86, 21.08, 11.13, 30.07, 26.55, 8.05],
    'Survived': [0, 1, 1, 1, 0, 0, 0, 1, 0, 0]
})

print("📊 Original DataFrame:")
print(titanic_df.head())

print("\n🚀 Why NumPy?")
print("• 10-100x faster than Python lists")
print("• Less memory usage")
print("• Powerful mathematical functions")
print("• Foundation for pandas, matplotlib, seaborn")

print("\n✅ Lab 1 Complete!")



print("🎯 Lab 2: Creating NumPy Arrays\n")

# Method 1: From Python list
ages_list = [22, 38, 26, 35, 54]
ages_array = np.array(ages_list)

print("From list:")
print(f"List: {ages_list}")
print(f"Array: {ages_array}")
print(f"Type: {type(ages_array)}")

# Method 2: From pandas Series
ages_series = titanic_df['Age']
ages_np = ages_series.values  # Convert to NumPy array

print("\nFrom pandas:")
print(f"Array: {ages_np}")
print(f"Type: {type(ages_np)}")

# Method 3: Direct creation functions
zeros = np.zeros(5)
ones = np.ones(5)
range_array = np.arange(0, 10, 2)
linspace = np.linspace(0, 100, 5)

print("\nDirect creation:")
print(f"Zeros: {zeros}")
print(f"Ones: {ones}")
print(f"Range: {range_array}")
print(f"Linspace: {linspace}")

print("\n✅ Lab 2 Complete!")



print("🎯 Lab 3: Understanding Array Attributes\n")

# Convert all numeric columns to arrays
age_array = titanic_df['Age'].values
fare_array = titanic_df['Fare'].values
survived_array = titanic_df['Survived'].values

print("Age Array:")
print(f"Values: {age_array}")
print(f"Shape: {age_array.shape}")
print(f"Data type: {age_array.dtype}")
print(f"Dimensions: {age_array.ndim}")
print(f"Size: {age_array.size}")

# 2D array example
data_2d = np.array([[22, 7.25], [38, 71.28], [26, 7.92]])
print("\n2D Array (Age, Fare):")
print(data_2d)
print(f"Shape: {data_2d.shape}")
print(f"Dimensions: {data_2d.ndim}")

print("\n📊 Key Attributes:")
print("• shape: Dimensions of array (rows, columns)")
print("• dtype: Data type (int64, float64, etc.)")
print("• ndim: Number of dimensions (1D, 2D, 3D...)")
print("• size: Total number of elements")

print("\n✅ Lab 3 Complete!")




print("🎯 Lab 4: Pandas ↔ NumPy Conversion\n")

# Pandas to NumPy
print("1. DataFrame to NumPy array:")
df_array = titanic_df.values
print(df_array)
print(f"Shape: {df_array.shape}")

# Single column to array
age_col = titanic_df['Age'].values
print(f"\nAge column as array: {age_col}")

# NumPy to Pandas
print("\n2. NumPy array to DataFrame:")
new_array = np.array([[25, 10.5, 1], [30, 15.0, 0]])
new_df = pd.DataFrame(new_array, columns=['Age', 'Fare', 'Survived'])
print(new_df)

# NumPy to Series
print("\n3. NumPy array to Series:")
age_series = pd.Series(age_col, name='Age')
print(age_series)

print("\n🔄 Conversion Summary:")
print("• df.values → NumPy array")
print("• df['col'].values → 1D array")
print("• pd.DataFrame(array) → DataFrame")
print("• pd.Series(array) → Series")

print("\n✅ Lab 4 Complete!")




print("🎯 PRACTICE PROJECT: NumPy Array Creation Summary\n")

# Create comprehensive array summary
print("=" * 50)
print("TITANIC DATASET - NUMPY ARRAYS")
print("=" * 50)

# Convert all columns
age = titanic_df['Age'].values
fare = titanic_df['Fare'].values
survived = titanic_df['Survived'].values

print("\n1. AGE ARRAY:")
print(f"   Values: {age}")
print(f"   Shape: {age.shape}")
print(f"   Type: {age.dtype}")

print("\n2. FARE ARRAY:")
print(f"   Values: {fare}")
print(f"   Shape: {fare.shape}")
print(f"   Type: {fare.dtype}")

print("\n3. SURVIVED ARRAY:")
print(f"   Values: {survived}")
print(f"   Shape: {survived.shape}")
print(f"   Type: {survived.dtype}")

# Create 2D array combining features
titanic_array = np.column_stack((age, fare, survived))
print("\n4. COMBINED 2D ARRAY:")
print(titanic_array)
print(f"   Shape: {titanic_array.shape}")
print(f"   (10 passengers × 3 features)")

# Array creation methods summary
print("\n" + "=" * 50)
print("ARRAY CREATION METHODS PRACTICED:")
print("=" * 50)
methods = {
    'From DataFrame': 'df.values',
    'From Series': 'df["col"].values',
    'From list': 'np.array([1, 2, 3])',
    'Zeros': 'np.zeros(5)',
    'Ones': 'np.ones(5)',
    'Range': 'np.arange(0, 10, 2)',
    'Stack columns': 'np.column_stack((arr1, arr2))'
}

for method, code in methods.items():
    print(f"✓ {method:20}: {code}")

print("\n💡 Key Learnings:")
print("• NumPy arrays are faster than lists")
print("• Easy conversion between pandas and NumPy")
print("• Arrays have shape, dtype, ndim attributes")
print("• Multiple ways to create arrays")

print("\n✅ Lab 5 Complete!")
print("🎉 Part 1 Complete: NumPy basics mastered!")



commands = {
    'Import NumPy': 'import numpy as np',
    'Create array': 'np.array([1, 2, 3])',
    'From pandas': 'df["col"].values',
    'Create zeros': 'np.zeros(10)',
    'Create ones': 'np.ones(10)',
    'Range': 'np.arange(0, 10, 2)',
    'Linspace': 'np.linspace(0, 100, 5)',
    'Check shape': 'array.shape',
    'Check dtype': 'array.dtype',
    'Stack arrays': 'np.column_stack((arr1, arr2))'
}

print("📚 NUMPY COMMANDS LEARNED:")
for concept, command in commands.items():
    print(f"• {concept:15}: {command}")



print("\n💾 Part 1 Summary:")
print("✅ What we learned:")
print("  • NumPy is faster and more efficient")
print("  • Arrays are created with np.array()")
print("  • Easy conversion: df.values")
print("  • Arrays have shape, dtype, ndim, size")
print("  • Multiple creation methods available")
print("\n🎯 Next: Part 2 - Array operations and indexing!")
