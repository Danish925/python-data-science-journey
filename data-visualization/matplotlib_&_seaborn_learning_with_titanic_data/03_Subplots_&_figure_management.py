import matplotlib.pyplot as plt
import pandas as pd

print("🎯 Creating your first subplots with pandas data...")

# Create comprehensive Titanic dataset
titanic_data = pd.DataFrame({
    'Age': [22, 38, 26, 35, 35, 54, 2, 27, 14, 4, 58, 20, 39, 14, 55, 2, 
            31, 25, 8, 19, 40, 66, 28, 42, 21, 18, 14, 40, 27, 3, 45, 33],
    'Fare': [7.25, 71.28, 7.92, 53.10, 8.05, 51.86, 21.08, 11.13, 30.07, 16.70,
             26.55, 8.05, 31.0, 7.85, 16.0, 29.12, 26.0, 7.90, 21.08, 7.25,
             227.52, 10.5, 26.0, 13.0, 7.74, 7.05, 46.90, 26.55, 7.23, 21.08, 26.25, 7.75],
    'Sex': ['male', 'female', 'female', 'female', 'male', 'male', 'male', 
            'male', 'female', 'female', 'male', 'male', 'female', 'female',
            'male', 'female', 'male', 'female', 'female', 'female', 'female',
            'male', 'female', 'male', 'female', 'female', 'female', 'male',
            'male', 'female', 'male', 'female'],
    'Pclass': [3, 1, 3, 1, 3, 1, 3, 3, 2, 3, 1, 3, 1, 3, 1, 3, 2, 3, 2, 3,
               1, 2, 2, 3, 3, 3, 1, 1, 3, 3, 2, 3],
    'Survived': [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0,
                 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1]
})

# Method 1: Simple 1x2 subplot (side by side)
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)  # 1 row, 2 columns, position 1
plt.hist(titanic_data['Age'], bins=15, color='skyblue', alpha=0.7)
plt.title('Age Distribution')
plt.xlabel('Age (Years)')
plt.ylabel('Count')

plt.subplot(1, 2, 2)  # 1 row, 2 columns, position 2
plt.hist(titanic_data['Fare'], bins=15, color='lightcoral', alpha=0.7)
plt.title('Fare Distribution')
plt.xlabel('Fare (£)')
plt.ylabel('Count')

plt.tight_layout()  # Prevents overlapping
plt.show()

print("✅ Created your first side-by-side subplots!")



print("🎯 Exploring different subplot grid arrangements...")

# 2x2 Grid (4 plots)

plt.figure(figsize=(14, 10))

# Top left: Age histogram
plt.subplot(2, 2, 1)
plt.hist(titanic_data['Age'], bins=12, color='lightblue', alpha=0.7)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')

# Top right: Survival counts
plt.subplot(2, 2, 2)
survival_counts = titanic_data['Survived'].value_counts().sort_index()
labels = survival_counts.index.map({0: "Did not survive", 1: "Survived"})
colors = ['red', 'green']
bars = plt.bar(labels, survival_counts.values, color=colors, alpha=0.7)
plt.title('Survival Counts')
plt.ylabel('Count')
for bar, value in zip(bars, survival_counts.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             int(value), ha='center', va='bottom', fontsize=11)

# Bottom left: Passenger class distribution
plt.subplot(2, 2, 3)
class_counts = titanic_data['Pclass'].value_counts().sort_index()
class_labels = ["1st Class", "2nd Class", "3rd Class"]
plt.bar(class_labels, class_counts.values, color=['gold', 'silver', 'brown'], alpha=0.7)
plt.title('Passenger Class Distribution')
plt.ylabel('Count')
for i, count in enumerate(class_counts.values):
    plt.text(i, count + 0.5, int(count), ha='center', va='bottom', fontsize=11)

# Bottom right: Age vs Fare scatter
plt.subplot(2, 2, 4)
plt.scatter(titanic_data['Age'], titanic_data['Fare'], alpha=0.6, color='purple')
plt.title('Age vs Fare')
plt.xlabel('Age (Years)')
plt.ylabel('Fare (£)')

plt.tight_layout()
plt.show()

print("📊 2x2 grid shows 4 different aspects of the data!")



print("🎯 Mastering the Object-Oriented (OO) interface...")

# OO Interface: More control and cleaner code
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Titanic Data Analysis - OO Interface', fontsize=16, fontweight='bold')

# Top left: Age histogram
axes[0, 0].hist(titanic_data['Age'], bins=12, color='lightblue', alpha=0.7, edgecolor='black')
axes[0, 0].set_title('Age Distribution')
axes[0, 0].set_xlabel('Age (Years)')
axes[0, 0].set_ylabel('Count')
axes[0, 0].grid(True, alpha=0.3)

# Top right: Survival by gender
male_survival = titanic_data[titanic_data['Sex'] == 'male']['Survived'].mean()
female_survival = titanic_data[titanic_data['Sex'] == 'female']['Survived'].mean()
axes[0, 1].bar(['Male', 'Female'], [male_survival, female_survival], 
               color=['lightblue', 'pink'], alpha=0.7, edgecolor='black')
axes[0, 1].set_title('Survival Rate by Gender')
axes[0, 1].set_ylabel('Survival Rate')
axes[0, 1].set_ylim(0, 1)
axes[0, 1].grid(True, alpha=0.3)

# Bottom left: Class survival rates
class_survival = titanic_data.groupby('Pclass')['Survived'].mean()
axes[1, 0].bar(['1st Class', '2nd Class', '3rd Class'], class_survival.values,
               color=['gold', 'silver', 'brown'], alpha=0.7, edgecolor='black')
axes[1, 0].set_title('Survival Rate by Class')
axes[1, 0].set_ylabel('Survival Rate')
axes[1, 0].set_ylim(0, 1)
axes[1, 0].grid(True, alpha=0.3)

# Bottom right: Age vs Fare colored by survival
survivors = titanic_data[titanic_data['Survived'] == 1]
non_survivors = titanic_data[titanic_data['Survived'] == 0]
axes[1, 1].scatter(survivors['Age'], survivors['Fare'], alpha=0.6, color='green', label='Survived')
axes[1, 1].scatter(non_survivors['Age'], non_survivors['Fare'], alpha=0.6, color='red', label='Did not survive')
axes[1, 1].set_title('Age vs Fare (by Survival)')
axes[1, 1].set_xlabel('Age (Years)')
axes[1, 1].set_ylabel('Fare (£)')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("🎉 OO Interface Benefits:")
print("• axes[0, 1] gives precise control over each subplot")
print("• fig.suptitle() adds overall title")
print("• More readable code for complex layouts")
print("• Better for programmatic plot generation")




print("🎯 Creating advanced subplot layouts...")

# Method 1: Unequal sized subplots using subplot2grid
fig = plt.figure(figsize=(15, 10))

# Large plot taking up top half
ax1 = plt.subplot2grid((3, 2), (0, 0), colspan=2, rowspan=2)
ax1.scatter(titanic_data['Age'], titanic_data['Fare'], 
           c=titanic_data['Survived'], cmap='RdYlGn', alpha=0.6, s=50)
ax1.set_title('Age vs Fare (Color = Survival Status)', fontsize=14)
ax1.set_xlabel('Age (Years)')
ax1.set_ylabel('Fare (£)')
ax1.grid(True, alpha=0.3)

# Small plot bottom left
ax2 = plt.subplot2grid((3, 2), (2, 0))
gender_counts = titanic_data['Sex'].value_counts()
ax2.pie(gender_counts.values, labels=gender_counts.index, autopct='%1.1f%%', 
        colors=['lightblue', 'pink'])
ax2.set_title('Gender Distribution')

# Small plot bottom right
ax3 = plt.subplot2grid((3, 2), (2, 1))
age_groups = pd.cut(titanic_data['Age'], bins=[0, 18, 35, 60, 100], 
                    labels=['Child', 'Young Adult', 'Adult', 'Senior'])
age_group_counts = age_groups.value_counts()
ax3.bar(age_group_counts.index, age_group_counts.values, 
        color=['yellow', 'orange', 'red', 'purple'], alpha=0.7)
ax3.set_title('Age Groups')
ax3.set_ylabel('Count')

plt.tight_layout()
plt.show()

print("📊 Advanced layout features:")
print("• subplot2grid() allows unequal sizes")
print("• colspan/rowspan control plot dimensions")
print("• Combines different plot types effectively")




print("🎯 Mastering figure size and spacing...")

# Experiment with different figure sizes
sizes = [(10, 6), (15, 8), (12, 10)]
size_names = ['Small', 'Wide', 'Square']

for i, (size, name) in enumerate(zip(sizes, size_names)):
    fig, axes = plt.subplots(1, 3, figsize=size)
    fig.suptitle(f'{name} Figure: {size[0]}x{size[1]} inches', fontsize=14)
    
    # Same plots in different sizes
    axes[0].hist(titanic_data['Age'], bins=10, color='skyblue', alpha=0.7)
    axes[0].set_title('Age')
    
    axes[1].hist(titanic_data['Fare'], bins=10, color='lightgreen', alpha=0.7)
    axes[1].set_title('Fare')
    
    axes[2].scatter(titanic_data['Age'], titanic_data['Fare'], alpha=0.6)
    axes[2].set_title('Age vs Fare')
    
    plt.tight_layout()
    plt.show()

# Spacing control comparison
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Spacing Control Demo', fontsize=16)

for i, ax in enumerate(axes.flat):
    ax.hist(titanic_data['Age'], bins=8, alpha=0.7)
    ax.set_title(f'Subplot {i+1}')

# Show without tight_layout first
plt.subplots_adjust(hspace=0.1, wspace=0.1)  # Very tight spacing
plt.show()

# Now show with proper spacing
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('With Proper Spacing', fontsize=16)

for i, ax in enumerate(axes.flat):
    ax.hist(titanic_data['Age'], bins=8, alpha=0.7)
    ax.set_title(f'Subplot {i+1}')

plt.tight_layout()  # Automatic optimal spacing
plt.show()

print("📏 Spacing control:")
print("• figsize=(width, height) in inches")
print("• plt.tight_layout() for automatic spacing")
print("• plt.subplots_adjust() for manual control")




print("🎯 PRACTICE PROJECT: Complete Titanic Analysis Dashboard")


fig = plt.figure(figsize=(16, 12))
fig.suptitle('Comprehensive Titanic Analysis Dashboard', fontsize=18, fontweight='bold')

# Plot 1: Age Distribution (top left, large)
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
ax1.hist(titanic_data['Age'], bins=15, color='steelblue', alpha=0.7, edgecolor='black')
ax1.set_title('Age Distribution of All Passengers', fontsize=12, fontweight='bold')
ax1.set_xlabel('Age (Years)')
ax1.set_ylabel('Number of Passengers')
ax1.grid(True, alpha=0.3)
mean_age = titanic_data['Age'].mean()
ax1.axvline(mean_age, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_age:.1f}')
ax1.legend()

# Plot 2: Survival Pie Chart (top right)
ax2 = plt.subplot2grid((3, 3), (0, 2))
survival_counts = titanic_data['Survived'].value_counts().sort_index()
pie_colors=['red','green']  # Pie colors for Did not survive & Survived
ax2.pie(survival_counts.values, 
        labels=['Did not survive', 'Survived'], 
        autopct='%1.1f%%', 
        colors=pie_colors)
ax2.set_title('Overall Survival Rate')

# Plot 3: Survival by class (middle left)
ax3 = plt.subplot2grid((3, 3), (1, 0))
class_survival = titanic_data.groupby('Pclass')['Survived'].mean().sort_index()
colors = ['gold', 'silver', 'brown']
bars = ax3.bar(['1st', '2nd', '3rd'], class_survival.values, color=colors, alpha=0.7, edgecolor='black')
ax3.set_title('Survival Rate by Class')
ax3.set_ylabel('Survival Rate')
ax3.set_ylim(0, 1)
ax3.grid(True, alpha=0.3)
for bar, value in zip(bars, class_survival.values):
    ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02, f'{value:.2f}', 
        ha='center', fontweight='bold')

# Plot 4: Gender survival (middle center)
ax4 = plt.subplot2grid((3, 3), (1, 1))
gender_survival = titanic_data.groupby('Sex')['Survived'].mean()
bars = ax4.bar(['Female', 'Male'], [gender_survival.get('female', 0), gender_survival.get('male', 0)],
               color=['pink', 'lightblue'], alpha=0.7, edgecolor='black')
ax4.set_title('Survival Rate by Gender')
ax4.set_ylabel('Survival Rate')
ax4.set_ylim(0, 1)
ax4.grid(True, alpha=0.3)
for bar, value in zip(bars, [gender_survival.get('female', 0), gender_survival.get('male', 0)]):
    ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02, 
             f'{value:.2f}', ha='center', fontweight='bold')

# Plot 5: Fare distribution (middle right)
ax5 = plt.subplot2grid((3, 3), (1, 2))
ax5.hist(titanic_data['Fare'], bins=12, color='orange', alpha=0.7, edgecolor='black')
ax5.set_title('Fare Distribution')
ax5.set_xlabel('Fare (£)')
ax5.set_ylabel('Count')
ax5.grid(True, alpha=0.3)

# Plot 6: Age vs Fare scatter (bottom, spanning all columns)
ax6 = plt.subplot2grid((3, 3), (2, 0), colspan=3)
survivors = titanic_data[titanic_data['Survived'] == 1]
non_survivors = titanic_data[titanic_data['Survived'] == 0]
ax6.scatter(non_survivors['Age'], non_survivors['Fare'], alpha=0.6, color='red', label='Did not survive', s=30)
ax6.scatter(survivors['Age'], survivors['Fare'], alpha=0.6, color='green', label='Survived', s=30)
ax6.set_title('Age vs Fare Relationship (Colored by Survival)', fontweight='bold')
ax6.set_xlabel('Age (Years)')
ax6.set_ylabel('Fare (£)')
ax6.legend()
ax6.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()




# Essential subplot commands with pandas:
subplot_commands = {
    'Basic Subplots': 'fig, axes = plt.subplots(2, 2, figsize=(12, 8))',
    'Access Specific Plot': 'axes[0, 1].hist(data)',
    'Single Row/Column': 'plt.subplot(1, 3, 1)',
    'Overall Title': 'fig.suptitle("Main Title")',
    'Automatic Spacing': 'plt.tight_layout()',
    'Manual Spacing': 'plt.subplots_adjust(hspace=0.3, wspace=0.3)',
    'Unequal Sizes': 'plt.subplot2grid((3, 2), (0, 0), colspan=2)',
    'Figure Size': 'plt.figure(figsize=(width, height))',
    'Grid Lines': 'ax.grid(True, alpha=0.3)',
    'Axis Limits': 'ax.set_ylim(0, 1)'
}

print("📚 SUBPLOT COMMANDS MASTERED:")
for concept, command in subplot_commands.items():
    print(f"• {concept:18}: {command}")


# Save your comprehensive dashboard
fig = plt.figure(figsize=(14, 10))
fig.suptitle('Titanic Analysis - Professional Dashboard', fontsize=16, fontweight='bold')

# Create a simplified version of your dashboard
ax1 = plt.subplot2grid((2, 3), (0, 0), colspan=2)
ax1.hist(titanic_data['Age'], bins=15, color='steelblue', alpha=0.7, edgecolor='black')
ax1.set_title('Age Distribution')
ax1.set_xlabel('Age (Years)')
ax1.set_ylabel('Count')
ax1.grid(True, alpha=0.3)

ax2 = plt.subplot2grid((2, 3), (0, 2))
survival_counts = titanic_data['Survived'].value_counts()
ax2.pie(survival_counts.values, labels=['Did not survive', 'Survived'], 
        autopct='%1.1f%%', colors=['red', 'green'])
ax2.set_title('Survival Rate')

ax3 = plt.subplot2grid((2, 3), (1, 0), colspan=3)
survivors = titanic_data[titanic_data['Survived'] == 1]
non_survivors = titanic_data[titanic_data['Survived'] == 0]
ax3.scatter(non_survivors['Age'], non_survivors['Fare'], alpha=0.6, color='red', label='Did not survive')
ax3.scatter(survivors['Age'], survivors['Fare'], alpha=0.6, color='green', label='Survived')
ax3.set_title('Age vs Fare by Survival Status')
ax3.set_xlabel('Age (Years)')
ax3.set_ylabel('Fare (£)')
ax3.legend()
ax3.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('part3_subplot_dashboard.png', dpi=300, bbox_inches='tight')
plt.show()

print("💾 Dashboard saved as 'part3_subplot_dashboard.png'")
print("🎯 Part 3 complete! Ready for pandas integration in part 4!")
