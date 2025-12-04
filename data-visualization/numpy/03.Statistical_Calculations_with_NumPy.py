import numpy as np
import pandas as pd

print("🎯 Lab 1: Basic Statistical Functions\n")

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

print("Age array:", age)
print("Fare array:", fare)

# Basic statistics for Age
print("\n1. AGE STATISTICS:")
print(f"Mean age: {np.mean(age):.2f} years")
print(f"Median age: {np.median(age):.2f} years")
print(f"Minimum age: {np.min(age)} years")
print(f"Maximum age: {np.max(age)} years")
print(f"Range: {np.max(age) - np.min(age)} years")

# Basic statistics for Fare
print("\n2. FARE STATISTICS:")
print(f"Mean fare: £{np.mean(fare):.2f}")
print(f"Median fare: £{np.median(fare):.2f}")
print(f"Minimum fare: £{np.min(fare):.2f}")
print(f"Maximum fare: £{np.max(fare):.2f}")
print(f"Range: £{np.max(fare) - np.min(fare):.2f}")

# Sum and count
print("\n3. AGGREGATES:")
print(f"Sum of ages: {np.sum(age)} years")
print(f"Count of passengers: {np.size(age)}")
print(f"Total fare collected: £{np.sum(fare):.2f}")

print("\n📚 Basic Functions:")
print("• np.mean(array): Average value")
print("• np.median(array): Middle value")
print("• np.min(array): Smallest value")
print("• np.max(array): Largest value")
print("• np.sum(array): Sum of all values")
print("• np.size(array): Number of elements")

print("\n✅ Lab 1 Complete!")




print("🎯 Lab 2: Understanding Spread and Variability\n")

print("Age array:", age)

# Standard deviation and variance
std_age = np.std(age)
var_age = np.var(age)

print("\n1. AGE VARIABILITY:")
print(f"Standard deviation: {std_age:.2f} years")
print(f"Variance: {var_age:.2f}")

print(f"\nMean: {np.mean(age):.2f}")
print(f"Std Dev: {std_age:.2f}")
print(f"Range (Mean ± Std): {np.mean(age) - std_age:.2f} to {np.mean(age) + std_age:.2f}")

# For Fare
std_fare = np.std(fare)
var_fare = np.var(fare)

print("\n2. FARE VARIABILITY:")
print(f"Standard deviation: £{std_fare:.2f}")
print(f"Variance: £{var_fare:.2f}")

print(f"\nMean: £{np.mean(fare):.2f}")
print(f"Std Dev: £{std_fare:.2f}")
print(f"Range (Mean ± Std): £{np.mean(fare) - std_fare:.2f} to £{np.mean(fare) + std_fare:.2f}")

# Comparing variability
print("\n3. COMPARING VARIABILITY:")
age_cv = (std_age / np.mean(age)) * 100  # Coefficient of variation
fare_cv = (std_fare / np.mean(fare)) * 100

print(f"Age CV: {age_cv:.2f}% (relative variability)")
print(f"Fare CV: {fare_cv:.2f}% (relative variability)")
print(f"Fare has {'more' if fare_cv > age_cv else 'less'} relative variability than Age")

print("\n📚 Variability Functions:")
print("• np.std(array): Standard deviation")
print("• np.var(array): Variance")
print("• Coefficient of Variation: (std/mean)*100")
print("• Higher std = More spread out data")
print("• Lower std = Data clustered around mean")

print("\n✅ Lab 2 Complete!")




print("🎯 Lab 3: Percentiles and Quartiles\n")

print("Age array:", np.sort(age))

# Percentiles
p25 = np.percentile(age, 25)
p50 = np.percentile(age, 50)
p75 = np.percentile(age, 75)
p90 = np.percentile(age, 90)

print("\n1. AGE PERCENTILES:")
print(f"25th percentile (Q1): {p25:.2f} years")
print(f"50th percentile (Q2/Median): {p50:.2f} years")
print(f"75th percentile (Q3): {p75:.2f} years")
print(f"90th percentile: {p90:.2f} years")

# Quantiles (similar to percentiles but use 0-1 scale)
print("\n2. AGE QUANTILES:")
print(f"0.25 quantile: {np.quantile(age, 0.25):.2f} years")
print(f"0.50 quantile: {np.quantile(age, 0.50):.2f} years")
print(f"0.75 quantile: {np.quantile(age, 0.75):.2f} years")

# IQR (Interquartile Range)
iqr = p75 - p25
print(f"\n3. INTERQUARTILE RANGE (IQR):")
print(f"IQR (Q3 - Q1): {iqr:.2f} years")
print(f"Q1: {p25:.2f}, Q3: {p75:.2f}")

# For Fare
print("\n4. FARE PERCENTILES:")
fare_p25 = np.percentile(fare, 25)
fare_p50 = np.percentile(fare, 50)
fare_p75 = np.percentile(fare, 75)
fare_iqr = fare_p75 - fare_p25

print(f"25th percentile: £{fare_p25:.2f}")
print(f"50th percentile: £{fare_p50:.2f}")
print(f"75th percentile: £{fare_p75:.2f}")
print(f"IQR: £{fare_iqr:.2f}")

print("\n📚 Percentile Functions:")
print("• np.percentile(array, q): Value at qth percentile")
print("• np.quantile(array, q): Same as percentile but 0-1 scale")
print("• Q1 = 25th percentile, Q2 = median, Q3 = 75th")
print("• IQR = Q3 - Q1 (middle 50% spread)")

print("\n✅ Lab 3 Complete!")




print("🎯 Lab 4: Grouped Statistics\n")

survived = titanic_df['Survived'].values
pclass = titanic_df['Pclass'].values

print("Age array:", age)
print("Survived array:", survived)
print("Pclass array:", pclass)

# Statistics by survival
print("\n1. AGE STATISTICS BY SURVIVAL:")
survivor_ages = age[survived == 1]
non_survivor_ages = age[survived == 0]

print(f"\nSurvivors (Survived=1):")
print(f"  Count: {len(survivor_ages)}")
print(f"  Mean age: {np.mean(survivor_ages):.2f} years")
print(f"  Median age: {np.median(survivor_ages):.2f} years")
print(f"  Std dev: {np.std(survivor_ages):.2f} years")

print(f"\nNon-survivors (Survived=0):")
print(f"  Count: {len(non_survivor_ages)}")
print(f"  Mean age: {np.mean(non_survivor_ages):.2f} years")
print(f"  Median age: {np.median(non_survivor_ages):.2f} years")
print(f"  Std dev: {np.std(non_survivor_ages):.2f} years")

# Fare statistics by passenger class
print("\n2. FARE STATISTICS BY PASSENGER CLASS:")
for pc in np.unique(pclass):
    class_fares = fare[pclass == pc]
    print(f"\nClass {int(pc)}:")
    print(f"  Count: {len(class_fares)}")
    print(f"  Mean fare: £{np.mean(class_fares):.2f}")
    print(f"  Median fare: £{np.median(class_fares):.2f}")
    print(f"  Min fare: £{np.min(class_fares):.2f}")
    print(f"  Max fare: £{np.max(class_fares):.2f}")

# Age by passenger class
print("\n3. AGE STATISTICS BY PASSENGER CLASS:")
for pc in np.unique(pclass):
    class_ages = age[pclass == pc]
    print(f"\nClass {int(pc)}:")
    print(f"  Count: {len(class_ages)}")
    print(f"  Mean age: {np.mean(class_ages):.2f} years")
    print(f"  Std dev: {np.std(class_ages):.2f} years")

print("\n📚 Grouped Statistics Pattern:")
print("• Filter by condition: array[condition]")
print("• Calculate stats on filtered data")
print("• Use np.unique() to find groups")
print("• Loop through groups for summary stats")

print("\n✅ Lab 4 Complete!")




print("🎯 PRACTICE PROJECT: Complete Statistical Analysis\n")

print("=" * 70)
print("COMPREHENSIVE STATISTICAL SUMMARY - TITANIC DATASET")
print("=" * 70)

# 1. Overall statistics
print("\n1. OVERALL DATASET STATISTICS:")
print(f"Total passengers: {len(age)}")
print(f"Survived: {np.sum(survived)} ({(np.sum(survived)/len(survived)*100):.1f}%)")
print(f"Non-survived: {len(survived) - np.sum(survived)} ({((len(survived)-np.sum(survived))/len(survived)*100):.1f}%)")

# 2. Age analysis
print("\n2. AGE ANALYSIS:")
print(f"Mean: {np.mean(age):.2f} years")
print(f"Median: {np.median(age):.2f} years")
print(f"Std Dev: {np.std(age):.2f} years")
print(f"Min: {np.min(age)} years")
print(f"Max: {np.max(age)} years")
print(f"Range: {np.max(age) - np.min(age)} years")
print(f"Q1: {np.percentile(age, 25):.2f}, Q3: {np.percentile(age, 75):.2f}")

# 3. Fare analysis
print("\n3. FARE ANALYSIS:")
print(f"Mean: £{np.mean(fare):.2f}")
print(f"Median: £{np.median(fare):.2f}")
print(f"Std Dev: £{np.std(fare):.2f}")
print(f"Min: £{np.min(fare):.2f}")
print(f"Max: £{np.max(fare):.2f}")
print(f"Range: £{np.max(fare) - np.min(fare):.2f}")
print(f"Q1: £{np.percentile(fare, 25):.2f}, Q3: £{np.percentile(fare, 75):.2f}")

# 4. Survival comparison
print("\n4. AGE BY SURVIVAL STATUS:")
print("\nSurvivors:")
print(f"  Mean age: {np.mean(age[survived==1]):.2f} years")
print(f"  Count: {np.sum(survived==1)}")
print(f"  Std dev: {np.std(age[survived==1]):.2f} years")

print("\nNon-survivors:")
print(f"  Mean age: {np.mean(age[survived==0]):.2f} years")
print(f"  Count: {np.sum(survived==0)}")
print(f"  Std dev: {np.std(age[survived==0]):.2f} years")

age_diff = np.mean(age[survived==1]) - np.mean(age[survived==0])
print(f"\nAge difference: {age_diff:.2f} years")

# 5. Fare by class
print("\n5. FARE BY PASSENGER CLASS:")
for pc in sorted(np.unique(pclass)):
    class_fare = fare[pclass == pc]
    print(f"\nClass {int(pc)}:")
    print(f"  Count: {len(class_fare)}")
    print(f"  Mean: £{np.mean(class_fare):.2f}")
    print(f"  Median: £{np.median(class_fare):.2f}")
    print(f"  Std dev: £{np.std(class_fare):.2f}")

# 6. Key findings
print("\n" + "=" * 70)
print("KEY STATISTICAL FINDINGS:")
print("=" * 70)

print(f"\n✓ Survival Rate: {(np.sum(survived)/len(survived)*100):.1f}%")
print(f"✓ Average Age: {np.mean(age):.2f} years (Std: {np.std(age):.2f})")
print(f"✓ Average Fare: £{np.mean(fare):.2f} (Std: £{np.std(fare):.2f})")
print(f"✓ Age range: {np.min(age)}-{np.max(age)} years")
print(f"✓ Fare range: £{np.min(fare):.2f}-£{np.max(fare):.2f}")

# 7. Insights
print("\n" + "=" * 70)
print("STATISTICAL INSIGHTS:")
print("=" * 70)

avg_survivor_age = np.mean(age[survived==1])
avg_nonsurvivor_age = np.mean(age[survived==0])

if avg_survivor_age < avg_nonsurvivor_age:
    print(f"\n✓ Survivors were younger on average ({avg_survivor_age:.2f} vs {avg_nonsurvivor_age:.2f} years)")
else:
    print(f"\n✓ Survivors were older on average ({avg_survivor_age:.2f} vs {avg_nonsurvivor_age:.2f} years)")

avg_survivor_fare = np.mean(fare[survived==1])
avg_nonsurvivor_fare = np.mean(fare[survived==0])

if avg_survivor_fare > avg_nonsurvivor_fare:
    print(f"✓ Survivors paid higher fares (£{avg_survivor_fare:.2f} vs £{avg_nonsurvivor_fare:.2f})")
else:
    print(f"✓ Survivors paid lower fares (£{avg_survivor_fare:.2f} vs £{avg_nonsurvivor_fare:.2f})")

# 8. Summary table
print("\n" + "=" * 70)
print("FUNCTIONS MASTERED:")
print("=" * 70)

functions = {
    'Mean': 'np.mean(array)',
    'Median': 'np.median(array)',
    'Std Dev': 'np.std(array)',
    'Variance': 'np.var(array)',
    'Min': 'np.min(array)',
    'Max': 'np.max(array)',
    'Sum': 'np.sum(array)',
    'Percentile': 'np.percentile(array, q)',
    'Quantile': 'np.quantile(array, q)',
    'Unique': 'np.unique(array)'
}

for func, code in functions.items():
    print(f"✓ {func:15}: {code}")

print("\n✅ Lab 5 Complete!")
print("🎉 Part 3 Complete: Statistical calculations mastered!")




commands = {
    'Mean': 'np.mean(array)',
    'Median': 'np.median(array)',
    'Std Dev': 'np.std(array)',
    'Variance': 'np.var(array)',
    'Min': 'np.min(array)',
    'Max': 'np.max(array)',
    'Sum': 'np.sum(array)',
    'Count': 'len(array) or np.size(array)',
    'Percentile': 'np.percentile(array, 25)',
    'Quantile': 'np.quantile(array, 0.25)',
    'Unique values': 'np.unique(array)',
    'Sort': 'np.sort(array)',
    'Argmin': 'np.argmin(array)',
    'Argmax': 'np.argmax(array)'
}

print("📚 STATISTICAL FUNCTIONS:")
for concept, command in commands.items():
    print(f"• {concept:15}: {command}")





print("\n💾 Part 3 Summary:")
print("✅ What we learned:")
print("  • Calculate mean, median, std dev")
print("  • Find min, max, range")
print("  • Use percentiles and quantiles")
print("  • Calculate statistics by groups")
print("  • Analyze data distributions")
print("\n🎯 Next: Part 4 - Array reshaping and broadcasting!")

