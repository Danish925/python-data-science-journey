import matplotlib.pyplot as plt
import pandas as pd

print("🎯 Discovering pandas built-in plotting capabilities...")

# Create comprehensive Titanic dataset
titanic_data = pd.DataFrame({
    'Age': [22, 38, 26, 35, 35, 54, 2, 27, 14, 4, 58, 20, 39, 14, 55, 2, 
            31, 25, 8, 19, 40, 66, 28, 42, 21, 18, 14, 40, 27, 3, 45, 33, 50, 47],
    'Fare': [7.25, 71.28, 7.92, 53.10, 8.05, 51.86, 21.08, 11.13, 30.07, 16.70,
             26.55, 8.05, 31.0, 7.85, 16.0, 29.12, 26.0, 7.90, 21.08, 7.25,
             227.52, 10.5, 26.0, 13.0, 7.74, 7.05, 46.90, 26.55, 7.23, 21.08, 
             26.25, 7.75, 13.0, 9.0],
    'Sex': ['male', 'female', 'female', 'female', 'male', 'male', 'male', 
            'male', 'female', 'female', 'male', 'male', 'female', 'female',
            'male', 'female', 'male', 'female', 'female', 'female', 'female',
            'male', 'female', 'male', 'female', 'female', 'female', 'male',
            'male', 'female', 'male', 'female', 'male', 'female'],
    'Pclass': [3, 1, 3, 1, 3, 1, 3, 3, 2, 3, 1, 3, 1, 3, 1, 3, 2, 3, 2, 3,
               1, 2, 2, 3, 3, 3, 1, 1, 3, 3, 2, 3, 1, 2],
    'Survived': [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0,
                 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    'Embarked': ['S', 'C', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'C', 'S',
                 'S', 'S', 'S', 'C', 'S', 'Q', 'S', 'S', 'S', 'S', 'S', 'S',
                 'Q', 'S', 'C', 'C', 'Q', 'S', 'S', 'Q', 'S', 'S']
})

# Method 1: DataFrame.plot() - The pandas way!
plt.figure(figsize=(15, 4))

# Subplot 1: Line plot using DataFrame.plot()
plt.subplot(1, 3, 1)
titanic_data['Age'].plot(kind='line', color='steelblue', title='Age Values (Line)')
plt.xlabel('Passenger Index')
plt.ylabel('Age')

# Subplot 2: Histogram using DataFrame.plot()
plt.subplot(1, 3, 2)
titanic_data['Age'].plot(kind='hist', bins=15, color='lightcoral', alpha=0.7, title='Age Distribution (Histogram)')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Subplot 3: Box plot using DataFrame.plot()
plt.subplot(1, 3, 3)
titanic_data[['Age', 'Fare']].plot(kind='box', title='Age and Fare Box Plots')
plt.ylabel('Values')

plt.tight_layout()
plt.show()

print("✅ Key pandas plotting syntax:")
print("• df['column'].plot(kind='hist')")
print("• df['column'].plot(kind='line')")  
print("• df[['col1', 'col2']].plot(kind='box')")
print("• Much shorter than plt.hist(df['column'])!")



print("🎯 Advanced pandas plotting techniques...")

# Create the figure and subplots first
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Advanced Pandas Plotting Techniques', fontsize=16, fontweight='bold')

# Subplot 1: Scatter plot using DataFrame.plot() with ax parameter
titanic_data.plot(kind='scatter', x='Age', y='Fare', c='Survived', 
                  colormap='RdYlGn', alpha=0.6, ax=axes[0, 0])
axes[0, 0].set_title('Age vs Fare (Color = Survival)')
axes[0, 0].set_xlabel('Age (Years)')
axes[0, 0].set_ylabel('Fare (£)')

# Subplot 2: Bar plot using value_counts().plot() with ax parameter
titanic_data['Pclass'].value_counts().sort_index().plot(kind='bar', 
                                                         color=['gold', 'silver', 'brown'],
                                                         ax=axes[0, 1])
axes[0, 1].set_title('Passengers by Class')
axes[0, 1].set_xlabel('Passenger Class')
axes[0, 1].set_ylabel('Count')
axes[0, 1].tick_params(axis='x', rotation=0)

# Subplot 3: Horizontal bar plot with ax parameter
titanic_data['Embarked'].value_counts().plot(kind='barh', 
                                              color=['skyblue', 'lightgreen', 'orange'],
                                              ax=axes[0, 2])
axes[0, 2].set_title('Embarkation Port')
axes[0, 2].set_xlabel('Count')
axes[0, 2].set_ylabel('Port')

# Subplot 4: Pie chart using plot() with ax parameter
titanic_data['Sex'].value_counts().plot(kind='pie', autopct='%1.1f%%', 
                                         colors=['lightblue', 'pink'],
                                         ax=axes[1, 0])
axes[1, 0].set_title('Gender Distribution')
axes[1, 0].set_ylabel('')  # Remove default ylabel

# Subplot 5: Multiple column histogram
ages_fares = titanic_data[['Age', 'Fare']].head(20)  # Use subset for cleaner area plot
ages_fares.plot(kind='line', alpha=0.7, ax=axes[1, 1], marker='o')
axes[1, 1].set_title('Age and Fare Trends (First 20 Passengers)')
axes[1, 1].set_xlabel('Passenger Index')
axes[1, 1].set_ylabel('Values')
axes[1, 1].legend(['Age', 'Fare'])

# Subplot 6: Survival rates comparison
survival_by_class = titanic_data.groupby('Pclass')['Survived'].mean()
survival_by_sex = titanic_data.groupby('Sex')['Survived'].mean()

# Create comparison data
class_labels = ['1st Class', '2nd Class', '3rd Class']
gender_labels = ['Female', 'Male']

# Plot class survival rates
x_pos = [0, 1, 2]
bars1 = axes[1, 2].bar(x_pos, survival_by_class.values, alpha=0.7, color=['gold', 'silver', 'brown'], width=0.4)
axes[1, 2].set_title('Survival Rates: Class vs Gender')
axes[1, 2].set_ylabel('Survival Rate')

# Add gender bars offset to the right
x_pos_gender = [3.5, 4.5]
bars2 = axes[1, 2].bar(x_pos_gender, [survival_by_sex.get('female', 0), survival_by_sex.get('male', 0)], 
                       alpha=0.7, color=['pink', 'lightblue'], width=0.4)

# Set x-axis labels and positions
all_positions = x_pos + x_pos_gender
all_labels = class_labels + gender_labels
axes[1, 2].set_xticks(all_positions)
axes[1, 2].set_xticklabels(all_labels, rotation=45, ha='right')
axes[1, 2].set_ylim(0, 1)

plt.tight_layout()
plt.show()

print("🎨 Advanced pandas plotting fixed:")
print("• Always use ax=axes[row, col] parameter with pandas .plot()")
print("• This prevents pandas from creating separate figures")
print("• df.plot(kind='scatter', x='col1', y='col2', ax=subplot)")
print("• df['col'].value_counts().plot(kind='bar', ax=subplot)")
print("• df.groupby('col').mean().plot(kind='line', ax=subplot)")




print("🎯 Working with time series data...")

# Create sample time series data (imagine daily passenger bookings)
dates = pd.date_range('2024-01-01', periods=30, freq='D')
daily_bookings = pd.DataFrame({
    'Date': dates,
    'Bookings': [15, 23, 18, 31, 27, 19, 8, 12, 35, 29, 22, 17, 25, 33, 19,
                 28, 24, 16, 21, 37, 26, 14, 20, 32, 18, 25, 29, 22, 17, 34],
    'Revenue': [1200, 1840, 1440, 2480, 2160, 1520, 640, 960, 2800, 2320,
                1760, 1360, 2000, 2640, 1520, 2240, 1920, 1280, 1680, 2960,
                2080, 1120, 1600, 2560, 1440, 2000, 2320, 1760, 1360, 2720]
})

# Set Date as index for time series plotting
daily_bookings.set_index('Date', inplace=True)

# Create figure and subplots properly
fig, axes = plt.subplots(2, 2, figsize=(15, 8))
fig.suptitle('Time Series Data Analysis', fontsize=16, fontweight='bold')

# Subplot 1: Basic time series plot with ax parameter
daily_bookings['Bookings'].plot(ax=axes[0, 0], color='steelblue', linewidth=2)
axes[0, 0].set_title('Daily Bookings Over Time')
axes[0, 0].set_ylabel('Number of Bookings')
axes[0, 0].grid(True, alpha=0.3)

# Subplot 2: Multiple time series with ax parameter
# Normalize to show both on same scale
normalized_data = daily_bookings / daily_bookings.max()
normalized_data.plot(ax=axes[0, 1], alpha=0.7)
axes[0, 1].set_title('Normalized Bookings and Revenue')
axes[0, 1].set_ylabel('Normalized Values')
axes[0, 1].legend(['Bookings', 'Revenue'])
axes[0, 1].grid(True, alpha=0.3)

# Subplot 3: Rolling average with ax parameter
daily_bookings['Bookings'].plot(ax=axes[1, 0], alpha=0.3, color='lightblue', label='Daily')
daily_bookings['Bookings'].rolling(window=7).mean().plot(ax=axes[1, 0], color='darkblue', linewidth=2, label='7-day Average')
axes[1, 0].set_title('Daily Bookings with 7-day Moving Average')
axes[1, 0].set_ylabel('Bookings')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# Subplot 4: Revenue vs Bookings scatter with ax parameter
daily_bookings.plot(kind='scatter', x='Bookings', y='Revenue', ax=axes[1, 1], alpha=0.6)
axes[1, 1].set_title('Revenue vs Bookings Relationship')
axes[1, 1].set_xlabel('Number of Bookings')
axes[1, 1].set_ylabel('Revenue (£)')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("📅 Time series features:")
print("• pd.date_range() creates date sequences")
print("• df.set_index('Date') makes dates the index")
print("• df['col'].rolling(window=7).mean() creates moving averages")
print("• Automatic date formatting on x-axis")
print("• ALWAYS use ax=axes[row, col] with pandas .plot() methods")



print("🎯 Advanced categorical data visualization...")

import pandas as pd
import matplotlib.pyplot as plt

# Sample Titanic-like data
titanic_data = pd.DataFrame({
    'Age': [22, 38, 26, 35, 35, 54, 2, 27, 14, 4, 58, 20, 39, 14, 55, 2,
            31, 25, 8, 19, 40, 66, 28, 42, 21, 18, 14, 40, 27, 3, 45, 33, 50, 47],
    'Fare': [7.25, 71.28, 7.92, 53.10, 8.05, 51.86, 21.08, 11.13, 30.07, 16.70,
             26.55, 8.05, 31.0, 7.85, 16.0, 29.12, 26.0, 7.90, 21.08, 7.25,
             227.52, 10.5, 26.0, 13.0, 7.74, 7.05, 46.90, 26.55, 7.23, 21.08,
             26.25, 7.75, 13.0, 9.0],
    'Sex': ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'male',
            'female', 'female', 'male', 'male', 'female', 'female', 'male', 'female',
            'male', 'female', 'female', 'female', 'female', 'male', 'female', 'male',
            'female', 'female', 'female', 'male', 'male', 'female', 'male', 'female',
            'male', 'female'],
    'Pclass': [3, 1, 3, 1, 3, 1, 3, 3, 2, 3, 1, 3, 1, 3, 1, 3, 2, 3, 2, 3,
               1, 2, 2, 3, 3, 3, 1, 1, 3, 3, 2, 3, 1, 2],
    'Survived': [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0,
                 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    'Embarked': ['S', 'C', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'C', 'S',
                 'S', 'S', 'S', 'C', 'S', 'Q', 'S', 'S', 'S', 'S', 'S', 'S',
                 'Q', 'S', 'C', 'C', 'Q', 'S', 'S', 'Q', 'S', 'S']
})

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('Categorical Data Visualization', fontsize=16, fontweight='bold')

# Plot 1: Stacked bar chart
survival_by_class_sex = titanic_data.groupby(['Pclass', 'Sex'])['Survived'].count().unstack()
survival_by_class_sex.plot(kind='bar', stacked=True, color=['lightblue', 'pink'],
                           title='Passenger Count by Class and Gender', ax=axes[0, 0])
axes[0, 0].set_xlabel('Passenger Class')
axes[0, 0].set_ylabel('Count')
axes[0, 0].set_xticklabels(['1st', '2nd', '3rd'])
axes[0, 0].legend(title='Gender')

# Plot 2: Grouped bar chart of survival rate
survival_rate_by_class_sex = titanic_data.groupby(['Pclass', 'Sex'])['Survived'].mean().unstack()
survival_rate_by_class_sex.plot(kind='bar', color=['lightblue', 'pink'], alpha=0.8,
                                title='Survival Rate by Class and Gender', ax=axes[0, 1])
axes[0, 1].set_xlabel('Passenger Class')
axes[0, 1].set_ylabel('Survival Rate')
axes[0, 1].set_xticklabels(['1st', '2nd', '3rd'])
axes[0, 1].legend(title='Gender')
axes[0, 1].set_ylim(0, 1)

# Plot 3: Cross-tabulation heatmap (manual, to work with matplotlib only)
crosstab = pd.crosstab(titanic_data['Pclass'], titanic_data['Survived'])
axes[0, 2].imshow(crosstab, cmap='Blues', alpha=0.3)
for i in range(crosstab.shape[0]):
    for j in range(crosstab.shape[1]):
        axes[0, 2].text(j, i, crosstab.iloc[i, j], ha='center', va='center', fontsize=12, fontweight='bold')
axes[0, 2].set_xticks([0, 1])
axes[0, 2].set_xticklabels(['No', 'Yes'])
axes[0, 2].set_yticks([0, 1, 2])
axes[0, 2].set_yticklabels(['1st', '2nd', '3rd'])
axes[0, 2].set_xlabel('Survived')
axes[0, 2].set_ylabel('Passenger Class')
axes[0, 2].set_title('Class vs Survival (Crosstab Heatmap)')

# Plot 4: Bar with age groups and gender
age_groups = pd.cut(titanic_data['Age'], bins=[0, 18, 35, 60, 100], 
                    labels=['Child', 'Young Adult', 'Adult', 'Senior'])
titanic_data['AgeGroup'] = age_groups
age_survival = titanic_data.groupby(['AgeGroup', 'Sex'])['Survived'].mean().unstack()
age_survival.plot(kind='bar', color=['lightblue', 'pink'], alpha=0.8,
                  title='Survival Rate by Age Group and Gender', ax=axes[1, 0])
axes[1, 0].set_xlabel('Age Group')
axes[1, 0].set_ylabel('Survival Rate')
axes[1, 0].legend(title='Gender')
axes[1, 0].set_ylim(0, 1)

# Plot 5: Fare distribution by class (boxplot)
fare_by_class = [titanic_data[titanic_data['Pclass'] == p]['Fare'] for p in [1, 2, 3]]
axes[1, 1].boxplot(fare_by_class)
axes[1, 1].set_title('Fare Distribution by Passenger Class')
axes[1, 1].set_ylabel('Fare (£)')
axes[1, 1].set_xticklabels(['1st', '2nd', '3rd'])
axes[1, 1].set_xlabel('Passenger Class')
axes[1, 1].legend()

# Plot 6: Embarkation analysis (grouped bar)
embarked_survival = titanic_data.groupby(['Embarked','Pclass'])['Survived'].mean().unstack()
embarked_survival.plot(kind='bar', color=['gold', 'silver', 'brown'], alpha=0.8,
                       title='Survival Rate by Embarkation Port and Class', ax=axes[1, 2])
axes[1, 2].set_xlabel('Embarkation Port')
axes[1, 2].set_ylabel('Survival Rate')
axes[1, 2].legend(title='Class', labels=['1st', '2nd', '3rd'])
axes[1, 2].set_ylim(0, 1)

plt.tight_layout()
plt.show()



# practice project

fig = plt.figure(figsize=(18, 12))
fig.suptitle('Advanced Pandas+Matplotlib Integration Dashboard', fontsize=18, fontweight='bold')

# 1. Monthly Trends plot (top row, spans all cols)
ax1 = plt.subplot2grid((3, 4), (0, 0), colspan=4)
months = pd.date_range('2023-01-01', periods=12, freq='M')
monthly_data = pd.DataFrame({
    'Month': months,
    'Survival_Rate': [0.38, 0.42, 0.35, 0.45, 0.39, 0.41, 0.37, 0.44, 0.40, 0.43, 0.36, 0.46],
    'Total_Passengers': [150, 180, 140, 200, 160, 175, 145, 190, 165, 185, 135, 205]
})
monthly_data.set_index('Month', inplace=True)
ax1_twin = ax1.twinx()
monthly_data['Survival_Rate'].plot(ax=ax1, color='b', linewidth=3, label='Survival Rate')
monthly_data['Total_Passengers'].plot(ax=ax1_twin, color='r', linestyle='--', linewidth=2, label='Total Passengers')
ax1.set_ylabel('Survival Rate', color='b', fontsize=12)
ax1_twin.set_ylabel('Total Passengers', color='r', fontsize=12)
ax1.set_title('Monthly Trends: Survival Rate and Passenger Volume', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax1_twin.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# 2. Categorical grouping analysis, age/gender/class (middle left, spans 2 cols)
ax2 = plt.subplot2grid((3, 4), (1, 0), colspan=2)
age_groups = pd.cut(titanic_data['Age'], bins=[0, 18, 35, 60, 100], 
                    labels=['Child', 'Young Adult', 'Adult', 'Senior'])
titanic_analysis = titanic_data.copy()
titanic_analysis['AgeGroup'] = age_groups
complex_analysis = titanic_analysis.groupby(['AgeGroup', 'Sex', 'Pclass'])['Survived'].mean().unstack(level=2)
complex_analysis.plot(kind='bar', ax=ax2, color=['gold', 'silver', 'brown'], alpha=0.8)
ax2.set_title('Survival Rate by Age, Gender, and Class', fontweight='bold')
ax2.set_xlabel('Age Group and Gender')
ax2.set_ylabel('Survival Rate')
ax2.legend(title='Class', labels=['1st', '2nd', '3rd'])
ax2.tick_params(axis='x', rotation=45)

# 3. Correlation matrix visualization (middle right, spans 2 cols)
ax3 = plt.subplot2grid((3, 4), (1, 2), colspan=2)
numeric_data = titanic_data[['Age', 'Fare', 'Pclass', 'Survived']].copy()
numeric_data['Class_Rank'] = 4 - numeric_data['Pclass'] 
numeric_data = numeric_data.drop('Pclass', axis=1)
correlation_matrix = numeric_data.corr()
im = ax3.imshow(correlation_matrix, cmap='RdYlBu', vmin=-1, vmax=1)
ax3.set_xticks(range(len(correlation_matrix.columns)))
ax3.set_yticks(range(len(correlation_matrix.columns)))
ax3.set_xticklabels(correlation_matrix.columns)
ax3.set_yticklabels(correlation_matrix.columns)
for i in range(len(correlation_matrix.columns)):
    for j in range(len(correlation_matrix.columns)):
        ax3.text(j, i, f'{correlation_matrix.iloc[i, j]:.2f}', 
                 ha='center', va='center', fontweight='bold')
ax3.set_title('Feature Correlation Matrix', fontweight='bold')
plt.colorbar(im, ax=ax3, shrink=0.8)

# 4. Fare distribution by survival (bottom left, spans 2 cols)
ax4 = plt.subplot2grid((3, 4), (2, 0), colspan=2)
survivors_fare = titanic_data[titanic_data['Survived'] == 1]['Fare']
non_survivors_fare = titanic_data[titanic_data['Survived'] == 0]['Fare']
survivors_fare.plot(kind='hist', bins=15, alpha=0.6, color='green', label='Survived', ax=ax4)
non_survivors_fare.plot(kind='hist', bins=15, alpha=0.6, color='red', label='Did not survive', ax=ax4)
ax4.set_title('Fare Distribution by Survival Status', fontweight='bold')
ax4.set_xlabel('Fare (£)')
ax4.set_ylabel('Frequency')
ax4.legend()
ax4.grid(True, alpha=0.3)

# 5. Advanced scatter (bottom right, spans 2 cols)
ax5 = plt.subplot2grid((3, 4), (2, 2), colspan=2)
titanic_analysis['Family_Size'] = 1  # Simplified for this example
scatter = ax5.scatter(
    titanic_analysis['Age'], titanic_analysis['Fare'],
    c=titanic_analysis['Survived'],
    s=titanic_analysis['Family_Size']*30,
    alpha=0.6, cmap='RdYlGn', edgecolors='black', linewidth=0.5
)
ax5.set_title('Age vs Fare (Color=Survival, Size=Family)', fontweight='bold')
ax5.set_xlabel('Age (Years)')
ax5.set_ylabel('Fare (£)')
ax5.grid(True, alpha=0.3)
plt.colorbar(scatter, ax=ax5, label='Survival Status')

plt.tight_layout()
plt.show()



# Essential pandas+matplotlib integration commands:
integration_commands = {
    'DataFrame Plotting': 'df.plot(kind="scatter", x="col1", y="col2")',
    'Value Counts Plot': 'df["col"].value_counts().plot(kind="bar")',
    'Time Series Plot': 'df.set_index("date").plot()',
    'Groupby Plotting': 'df.groupby("cat").mean().plot()',
    'Multi-level Groupby': 'df.groupby(["cat1","cat2"]).mean().unstack().plot()',
    'Cross-tabulation': 'pd.crosstab(df["col1"], df["col2"])',
    'Rolling Average': 'df["col"].rolling(window=7).mean().plot()',
    'Multiple Y-axes': 'ax2 = ax1.twinx(); ax2.plot(data)',
    'Age Groups': 'pd.cut(df["Age"], bins=[0,18,35,60,100])',
    'Correlation Matrix': 'df.corr()'
}

print("📚 PANDAS+MATPLOTLIB INTEGRATION MASTERED:")
for concept, command in integration_commands.items():
    print(f"• {concept:18}: {command}")



# Save your comprehensive integration analysis
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Pandas+Matplotlib Integration Summary', fontsize=16, fontweight='bold')

# Quick integration examples for saving
axes[0, 0].set_title('DataFrame Direct Plotting')
titanic_data['Age'].plot(kind='hist', bins=15, ax=axes[0, 0], color='steelblue', alpha=0.7)

axes[0, 1].set_title('Value Counts Plotting')
titanic_data['Pclass'].value_counts().sort_index().plot(kind='bar', ax=axes[0, 1], color=['gold', 'silver', 'brown'])

axes[1, 0].set_title('Groupby Visualization')
titanic_data.groupby('Sex')['Survived'].mean().plot(kind='bar', ax=axes[1, 0], color=['pink', 'lightblue'])

axes[1, 1].set_title('Scatter Plot Integration')
titanic_data.plot(kind='scatter', x='Age', y='Fare', c='Survived', ax=axes[1, 1], alpha=0.6, colormap='RdYlGn')

plt.tight_layout()
plt.savefig('part4_pandas_integration.png', dpi=300, bbox_inches='tight')
plt.show()

print("💾 Integration summary saved as 'part4_pandas_integration.png'")
print("🎯 Part 4 complete! Ready for professional styling in part 5!")
