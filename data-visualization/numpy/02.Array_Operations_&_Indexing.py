import numpy as np
import pandas as pd

print("🎯 Lab 1: Basic Array Indexing\n")

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
survived = titanic_df['Survived'].values

print("Age array:")
print(age)

# Access individual elements
print("\n1. Single Element Access:")
print(f"First passenger age: {age[0]}")
print(f"Last passenger age: {age[-1]}")
print(f"5th passenger age: {age[4]}")

# Access multiple elements
print("\n2. Multiple Element Access:")
print(f"First 3 ages: {age[:3]}")
print(f"Last 3 ages: {age[-3:]}")
print(f"Every 2nd age: {age[::2]}")

# Negative indexing
print("\n3. Negative Indexing:")
print(f"Index -1: {age[-1]} (Last)")
print(f"Index -2: {age[-2]} (Second last)")
print(f"Index -5 to -1: {age[-5:-1]}")

print("\n📚 Indexing Rules:")
print("• age[0]: First element (index starts at 0)")
print("• age[-1]: Last element")
print("• age[start:stop:step]: Slice notation")
print("• age[:3]: First 3 elements")
print("• age[::2]: Every 2nd element")

print("\n✅ Lab 1 Complete!")





print("🎯 Lab 2: Slicing Arrays\n")

print("Original Fare array:")
print(fare)

# Basic slicing
print("\n1. Basic Slicing:")
print(f"fare[0:3]: {fare[0:3]} (indices 0, 1, 2)")
print(f"fare[2:5]: {fare[2:5]} (indices 2, 3, 4)")
print(f"fare[5:]: {fare[5:]} (from index 5 to end)")

# Step slicing
print("\n2. Step Slicing:")
print(f"fare[::2]: {fare[::2]} (every 2nd element)")
print(f"fare[1::2]: {fare[1::2]} (every 2nd from index 1)")
print(f"fare[::-1]: {fare[::-1]} (reversed)")

# 2D array slicing
print("\n3. 2D Array Slicing:")
data_2d = np.column_stack((age, fare, survived))
print("2D Array (Age, Fare, Survived):")
print(data_2d)

print(f"\nFirst row: {data_2d[0]}")
print(f"First 3 rows: \n{data_2d[:3]}")
print(f"All rows, first column (Age): {data_2d[:, 0]}")
print(f"All rows, second column (Fare): {data_2d[:, 1]}")
print(f"First 5 rows, first 2 columns: \n{data_2d[:5, :2]}")

print("\n📚 Slicing Syntax:")
print("• array[start:stop:step]")
print("• array[:n]: First n elements")
print("• array[n:]: From nth element")
print("• array[::2]: Every 2nd element")
print("• array[::-1]: Reversed")
print("• array2d[row, col]: Specific element")
print("• array2d[:, col]: Entire column")

print("\n✅ Lab 2 Complete!")




print("🎯 Lab 3: Mathematical Operations\n")

print("Age array:", age)
print("Fare array:", fare)

# Arithmetic operations
print("\n1. Arithmetic Operations:")
print(f"Age + 5: {age + 5}")
print(f"Age * 2: {age * 2}")
print(f"Fare / 10: {fare / 10}")
print(f"Age - minimum age: {age - age.min()}")

# Operations between arrays
print("\n2. Operations Between Arrays:")
print(f"Age + Survived: {age + survived}")
print(f"Age * 2 + Fare: {age * 2 + fare}")
print(f"Fare / Age (normalized): {fare / age}")

# Power and square root
print("\n3. Power and Roots:")
print(f"Age squared: {age ** 2}")
print(f"Square root of Fare: {np.sqrt(fare)}")
print(f"Age to power 3: {age ** 3}")

# Absolute values
print("\n4. Absolute and Sign:")
differences = age - 30
print(f"Age - 30: {differences}")
print(f"Absolute differences: {np.abs(differences)}")

print("\n📚 Operations Examples:")
print("• array + 5: Add 5 to each element")
print("• array * 2: Multiply each element by 2")
print("• array1 + array2: Element-wise addition")
print("• np.sqrt(array): Square root")
print("• np.abs(array): Absolute value")
print("• np.power(array, 2): Power operation")

print("\n✅ Lab 3 Complete!")



print("🎯 Lab 4: Boolean Indexing\n")

print("Age array:", age)
print("Survived array:", survived)

# Create boolean arrays
print("\n1. Creating Boolean Masks:")
age_above_30 = age > 30
print(f"Age > 30: {age_above_30}")

survived_yes = survived == 1
print(f"Survived == 1: {survived_yes}")

fare_expensive = fare > 50
print(f"Fare > 50: {fare_expensive}")

# Filter using boolean arrays
print("\n2. Filtering with Boolean Arrays:")
expensive_fares = fare[fare_expensive]
print(f"Fares > 50: {expensive_fares}")

adult_ages = age[age > 30]
print(f"Ages > 30: {adult_ages}")

young_survivors = age[survived == 1]
print(f"Ages of survivors: {young_survivors}")

# Combine conditions
print("\n3. Combining Conditions:")
expensive_and_survived = fare[(fare > 50) & (survived == 1)]
print(f"Fare > 50 AND Survived: {expensive_and_survived}")

young_or_cheap = age[(age < 20) | (fare < 10)]
print(f"Age < 20 OR Fare < 10: {young_or_cheap}")

# Count filtered elements
print("\n4. Counting Filtered Elements:")
num_expensive = np.sum(fare > 50)
num_survivors = np.sum(survived == 1)
print(f"Number of expensive fares (>50): {num_expensive}")
print(f"Number of survivors: {num_survivors}")
print(f"Percentage survived: {(num_survivors / len(survived)) * 100:.1f}%")

print("\n📚 Boolean Indexing:")
print("• array > value: Create boolean mask")
print("• array[mask]: Filter by boolean mask")
print("• (condition1) & (condition2): AND")
print("• (condition1) | (condition2): OR")
print("• np.sum(mask): Count True values")

print("\n✅ Lab 4 Complete!")




print("🎯 PRACTICE PROJECT: Array Operations Summary\n")

print("=" * 60)
print("COMPREHENSIVE ARRAY OPERATIONS ANALYSIS")
print("=" * 60)

# 1. Indexing examples
print("\n1. INDEXING EXAMPLES:")
print(f"First 3 ages: {age[:3]}")
print(f"Last 2 fares: {fare[-2:]}")
print(f"Every 3rd age: {age[::3]}")

# 2. Mathematical operations
print("\n2. MATHEMATICAL OPERATIONS:")
age_normalized = (age - age.mean()) / age.std()
fare_doubled = fare * 2
print(f"Normalized ages: {age_normalized}")
print(f"Fares doubled: {fare_doubled}")

# 3. Boolean filtering
print("\n3. BOOLEAN FILTERING:")
children = age < 18
print(f"Children (Age < 18): {age[children]}")
print(f"Number of children: {np.sum(children)}")

adults = age >= 18
print(f"Adults (Age >= 18): {age[adults]}")
print(f"Number of adults: {np.sum(adults)}")

# 4. Complex filtering
print("\n4. COMPLEX FILTERING:")
expensive_adult = (age >= 18) & (fare > 30)
print(f"Expensive tickets (>30) for adults: {fare[expensive_adult]}")

young_cheap = (age < 20) | (fare < 15)
print(f"Young passengers OR cheap fares: {age[young_cheap]}")

# 5. Statistical insights
print("\n5. STATISTICAL INSIGHTS:")
print(f"Average age: {age.mean():.2f}")
print(f"Oldest passenger: {age.max()}")
print(f"Youngest passenger: {age.min()}")
print(f"Age range: {age.max() - age.min()}")

print(f"\nAverage fare: £{fare.mean():.2f}")
print(f"Most expensive: £{fare.max():.2f}")
print(f"Cheapest: £{fare.min():.2f}")

# 6. Survival analysis with filtering
print("\n6. SURVIVAL ANALYSIS:")
survivor_ages = age[survived == 1]
non_survivor_ages = age[survived == 0]

print(f"Average age of survivors: {survivor_ages.mean():.2f}")
print(f"Average age of non-survivors: {non_survivor_ages.mean():.2f}")

survivor_fares = fare[survived == 1]
non_survivor_fares = fare[survived == 0]

print(f"Average fare of survivors: £{survivor_fares.mean():.2f}")
print(f"Average fare of non-survivors: £{non_survivor_fares.mean():.2f}")

# Summary table
print("\n" + "=" * 60)
print("OPERATIONS MASTERED:")
print("=" * 60)

operations = {
    'Indexing': 'age[0], age[-1], age[:3]',
    'Slicing': 'age[start:stop:step]',
    'Arithmetic': 'age + 5, age * 2, age / 10',
    'Comparison': 'age > 30, fare < 50',
    'Boolean AND': '(age > 18) & (fare > 30)',
    'Boolean OR': '(age < 10) | (fare < 15)',
    'Functions': 'np.sqrt(), np.abs(), np.power()',
    'Filtering': 'age[age > 30], fare[survived == 1]'
}

for operation, example in operations.items():
    print(f"✓ {operation:15}: {example}")

print("\n💡 Key Insights:")
print(f"• Survived: {np.sum(survived)}/{len(survived)} passengers")
print(f"• Children: {np.sum(age < 18)}/{len(age)} passengers")
print(f"• Age difference: {age.max() - age.min()} years")

print("\n✅ Lab 5 Complete!")
print("🎉 Part 2 Complete: Array operations mastered!")




commands = {
    'Single element': 'array[0], array[-1]',
    'Slice': 'array[start:stop:step]',
    'First n': 'array[:n]',
    'Last n': 'array[-n:]',
    'Reverse': 'array[::-1]',
    'Every nth': 'array[::n]',
    '2D indexing': 'array[row, col]',
    '2D column': 'array[:, col]',
    '2D row': 'array[row, :]',
    'Add': 'array + value',
    'Multiply': 'array * value',
    'Power': 'array ** 2',
    'Boolean mask': 'array > value',
    'Filter': 'array[array > value]',
    'AND': '(cond1) & (cond2)',
    'OR': '(cond1) | (cond2)'
}

print("📚 ARRAY OPERATIONS COMMANDS:")
for concept, command in commands.items():
    print(f"• {concept:15}: {command}")




print("\n💾 Part 2 Summary:")
print("✅ What we learned:")
print("  • Index arrays with [index]")
print("  • Slice with [start:stop:step]")
print("  • Perform arithmetic operations")
print("  • Use boolean masks for filtering")
print("  • Combine conditions with & and |")
print("\n🎯 Next: Part 3 - Statistical calculations!")
