# Import libraries
import matplotlib.pyplot as plt
import pandas as pd

print("🎯 Creating histograms to analyze data distributions...")

# Load or create Titanic sample data
titanic_data = pd.DataFrame({
    'Age': [22, 38, 26, 35, 35, 54, 2, 27, 14, 4, 58, 20, 39, 14, 55, 2, 
            31, 25, 8, 19, 40, 66, 28, 42, 21, 18, 14, 40, 27, 3],
    'Sex': ['male', 'female', 'female', 'female', 'male', 'male', 'male', 
            'male', 'female', 'female', 'male', 'male', 'female', 'female',
            'male', 'female', 'male', 'female', 'female', 'female', 'female',
            'male', 'female', 'male', 'female', 'female', 'female', 'male',
            'male', 'female'],
    'Survived': [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0,
                 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1]
})

# Basic histogram
plt.figure(figsize=(8, 6))
plt.hist(titanic_data['Age'])
plt.title('Age Distribution of Titanic Passengers')
plt.xlabel('Age (Years)')
plt.ylabel('Number of Passengers')
plt.show()

print("📊 Your first histogram shows the distribution of passenger ages!")
print(f"Data sample: {len(titanic_data)} passengers")




print("🎯 Experimenting with different bin sizes...")

# Create subplots to compare different bin sizes
plt.figure(figsize=(15, 5))

# 10 bins
plt.subplot(1, 3, 1)
plt.hist(titanic_data['Age'], bins=10, color='lightblue', edgecolor='black')
plt.title('10 Bins')
plt.xlabel('Age')
plt.ylabel('Count')

# 20 bins (default-ish)
plt.subplot(1, 3, 2) 
plt.hist(titanic_data['Age'], bins=20, color='lightgreen', edgecolor='black')
plt.title('20 Bins')
plt.xlabel('Age')

# 5 bins (very coarse)
plt.subplot(1, 3, 3)
plt.hist(titanic_data['Age'], bins=5, color='lightcoral', edgecolor='black')
plt.title('5 Bins')
plt.xlabel('Age')

plt.tight_layout()
plt.show()

print("📚 Key Learning:")
print("• More bins = more detail, but can look noisy")
print("• Fewer bins = smoother, but might hide patterns")
print("• 15-30 bins usually work well for most data")



print("🎯 Customizing histogram appearance...")

plt.figure(figsize=(12, 8))

# Subplot 1: Basic color
plt.subplot(2, 2, 1)
plt.hist(titanic_data['Age'], bins=20, color='steelblue')
plt.title('Solid Blue Histogram')
plt.xlabel('Age')
plt.ylabel('Count')

# Subplot 2: With transparency (alpha)
plt.subplot(2, 2, 2)
plt.hist(titanic_data['Age'], bins=20, color='red', alpha=0.7)
plt.title('Semi-transparent Red (alpha=0.7)')
plt.xlabel('Age')

# Subplot 3: With edge color
plt.subplot(2, 2, 3)
plt.hist(titanic_data['Age'], bins=20, color='green', alpha=0.6, edgecolor='black')
plt.title('Green with Black Edges')
plt.xlabel('Age')
plt.ylabel('Count')

# Subplot 4: Custom color using hex code
plt.subplot(2, 2, 4)
plt.hist(titanic_data['Age'], bins=20, color='#FF6B35', alpha=0.8)
plt.title('Custom Hex Color (#FF6B35)')
plt.xlabel('Age')

plt.tight_layout()
plt.show()

print("🎨 Color options:")
print("• Named colors: 'red', 'blue', 'green', 'steelblue'")
print("• Hex colors: '#FF6B35', '#4ECDC4', '#45B7D1'")
print("• Alpha: 0.0 (transparent) to 1.0 (solid)")
print("• edgecolor: adds borders to bars")



print("🎯 Comparing age distributions by gender...")

# Method 1: Side by side subplots
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
male_ages = titanic_data[titanic_data['Sex'] == 'male']['Age']
plt.hist(male_ages, bins=15, color='lightblue', alpha=0.7, edgecolor='black')
plt.title('Age Distribution - Male Passengers')
plt.xlabel('Age (Years)')
plt.ylabel('Count')

plt.subplot(1, 2, 2)
female_ages = titanic_data[titanic_data['Sex'] == 'female']['Age']
plt.hist(female_ages, bins=15, color='pink', alpha=0.7, edgecolor='black')
plt.title('Age Distribution - Female Passengers')
plt.xlabel('Age (Years)')

plt.tight_layout()
plt.show()

# Method 2: Overlapping histograms
plt.figure(figsize=(10, 6))
plt.hist(male_ages, bins=15, alpha=0.5, label='Male', color='blue')
plt.hist(female_ages, bins=15, alpha=0.5, label='Female', color='red')
plt.title('Age Distribution Comparison: Male vs Female')
plt.xlabel('Age (Years)')
plt.ylabel('Count')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print("📊 Analysis:")
print(f"• Male passengers: {len(male_ages)} people")
print(f"• Female passengers: {len(female_ages)} people")
print(f"• Male average age: {male_ages.mean():.1f} years")
print(f"• Female average age: {female_ages.mean():.1f} years")



print("🎯 Advanced histogram customization...")

plt.figure(figsize=(12, 8))

# Subplot 1: Density plot (normalized)
plt.subplot(2, 2, 1)
plt.hist(titanic_data['Age'], bins=20, density=True, color='skyblue', alpha=0.7)
plt.title('Normalized Histogram (Density)')
plt.xlabel('Age')
plt.ylabel('Density')

# Subplot 2: Cumulative histogram
plt.subplot(2, 2, 2)
plt.hist(titanic_data['Age'], bins=20, cumulative=True, color='orange', alpha=0.7)
plt.title('Cumulative Histogram')
plt.xlabel('Age')
plt.ylabel('Cumulative Count')

# Subplot 3: Horizontal histogram
plt.subplot(2, 2, 3)
plt.hist(titanic_data['Age'], bins=15, orientation='horizontal', color='lightgreen', alpha=0.7)
plt.title('Horizontal Histogram')
plt.ylabel('Age')
plt.xlabel('Count')

# Subplot 4: With statistics annotations
plt.subplot(2, 2, 4)
plt.hist(titanic_data['Age'], bins=20, color='purple', alpha=0.7)
plt.title('Histogram with Statistics')
plt.xlabel('Age')
plt.ylabel('Count')

# Add mean line
mean_age = titanic_data['Age'].mean()
plt.axvline(mean_age, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_age:.1f}')
plt.legend()

plt.tight_layout()
plt.show()

print("📊 Advanced features:")
print("• density=True: Shows proportion instead of counts")
print("• cumulative=True: Shows running total") 
print("• orientation='horizontal': Flips the histogram")
print("• axvline(): Adds vertical reference lines")



print("🎯 PRACTICE PROJECT: Complete Age Analysis Dashboard")

# Create a comprehensive analysis using pandas grouping
survivors = titanic_data[titanic_data['Survived'] == 1]['Age']
non_survivors = titanic_data[titanic_data['Survived'] == 0]['Age']

# Create dashboard
plt.figure(figsize=(14,10))
plt.suptitle('Titanic Age Analysis Dashboard', fontsize=16, fontweight='bold')

# Plot 1: Overall distribution
plt.subplot(2,2,1)
plt.hist(titanic_data['Age'], bins=20, color='steelblue', alpha=0.7, edgecolor='black')
plt.title('Overall Age Distribution')
plt.xlabel('Age (Years)')
plt.ylabel('Count')
plt.grid(True, alpha=0.3)

# Plot 2: Survival comparison
plt.subplot(2, 2, 2)
plt.hist(survivors, bins=15, alpha=0.6, label='Survived', color='green')
plt.hist(non_survivors, bins=15, alpha=0.6, label='Did not survive', color='red')
plt.xlabel('Age (Years)')
plt.ylabel('Count')
plt.title('Age Distribution by Survival')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 3: Gender comparison  
plt.subplot(2, 2, 3)
male_ages = titanic_data[titanic_data['Sex'] == 'male']['Age']
female_ages = titanic_data[titanic_data['Sex'] == 'female']['Age']
plt.hist(male_ages, bins=15, alpha=0.6, label='Male', color='blue')
plt.hist(female_ages, bins=15, alpha=0.6, label='Female', color='pink')
plt.title('Age Distribution by Gender')
plt.xlabel('Age (Years)')
plt.ylabel('Count')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 4: Age statistics summary
plt.subplot(2, 2, 4)
plt.hist(titanic_data['Age'], bins=20, color='gold', alpha=0.7)
plt.title('Age Distribution with Key Statistics')
plt.xlabel('Age (Years)')
plt.ylabel('Count')

# Add statistical lines
mean_age = titanic_data['Age'].mean()
median_age = titanic_data['Age'].median()
plt.axvline(mean_age, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_age:.1f}')
plt.axvline(median_age, color='blue', linestyle='--', linewidth=2, label=f'Median: {median_age:.1f}')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("🎉 Dashboard Complete!")
print("📊 Key Insights:")
print(f"• Average age: {titanic_data['Age'].mean():.1f} years")
print(f"• Median age: {titanic_data['Age'].median():.1f} years")
print(f"• Age range: {titanic_data['Age'].min():.0f} - {titanic_data['Age'].max():.0f} years")
print(f"• Survival rate by age group:")
young = titanic_data[titanic_data['Age'] < 18]['Survived'].mean()
adult = titanic_data[titanic_data['Age'] >= 18]['Survived'].mean()
print(f"  - Children (<18): {young:.1%}")
print(f"  - Adults (18+): {adult:.1%}")



# Essential histogram commands with pandas:
histogram_commands = {
    'Basic Histogram': 'plt.hist(df["column"])',
    'Custom Bins': 'plt.hist(data, bins=20)',
    'Colors & Alpha': 'plt.hist(data, color="blue", alpha=0.7)',
    'Edge Colors': 'plt.hist(data, edgecolor="black")',
    'Overlapping Plots': 'plt.hist(data1, alpha=0.5, label="Group1")',
    'Density Plot': 'plt.hist(data, density=True)',
    'Cumulative': 'plt.hist(data, cumulative=True)',
    'Horizontal': 'plt.hist(data, orientation="horizontal")',
    'Statistical Lines': 'plt.axvline(mean_value, color="red", linestyle="--")',
    'Legends': 'plt.legend()'
}

print("📚 HISTOGRAM COMMANDS MASTERED:")
for concept, command in histogram_commands.items():
    print(f"• {concept:18}: {command}")



# Save your best histogram
plt.figure(figsize=(10, 6))
plt.hist(titanic_data['Age'], bins=20, color='steelblue', alpha=0.7, edgecolor='black')
plt.title('Titanic Passenger Age Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Age (Years)', fontsize=12)
plt.ylabel('Number of Passengers', fontsize=12)
plt.grid(True, alpha=0.3)

# Add statistical information
mean_age = titanic_data['Age'].mean()
plt.axvline(mean_age, color='red', linestyle='--', linewidth=2, 
            label=f'Average Age: {mean_age:.1f} years')
plt.legend()

plt.tight_layout()
plt.savefig('part2_age_histogram.png', dpi=300, bbox_inches='tight')
plt.show()

print("💾 Histogram saved as 'part2_age_histogram.png'")
print("🎯 Part 2 complete! Ready for bar charts and categorical data in part 3!")

