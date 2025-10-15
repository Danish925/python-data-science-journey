import matplotlib.pyplot as plt
import pandas as pd

print("🎯 Exploring matplotlib styles and themes...")

# Sample Titanic data
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
                 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1]
})

# Check available styles
print("📊 Available matplotlib styles:")
print(plt.style.available[:10])  # Show first 10

# Compare different styles
styles_to_try = ['default', 'seaborn-v0_8', 'ggplot', 'classic']
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Matplotlib Style Comparison', fontsize=16, fontweight='bold')

for i, style in enumerate(styles_to_try):
    row, col = i // 2, i % 2
    
    plt.style.use(style)
    
    # Create age histogram with current style
    titanic_data['Age'].plot(kind='hist', bins=15, ax=axes[row, col], alpha=0.7)
    axes[row, col].set_title(f'Style: {style}', fontsize=12, fontweight='bold')
    axes[row, col].set_xlabel('Age (Years)')
    axes[row, col].set_ylabel('Count')

plt.tight_layout()
plt.show()

# Reset to default for next labs
plt.style.use('default')

print("✅ Styles allow instant professional theming!")
print("• 'seaborn-v0_8' - Clean, academic look")
print("• 'ggplot' - R's ggplot2 style")
print("• 'classic' - Traditional matplotlib")






print("🎯 Mastering color palettes and advanced customization...")

# Set a professional style
plt.style.use('seaborn-v0_8-whitegrid')

fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle('Professional Color Palettes and Customization', fontsize=18, fontweight='bold')

# Define professional color palettes
colors_corporate = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D']
colors_academic = ['#264653', '#2A9D8F', '#E9C46A', '#F4A261', '#E76F51']
colors_pastel = ['#FFB3BA', '#FFDFBA', '#FFFFBA', '#BAFFC9', '#BAE1FF']

# Plot 1: Professional histogram with custom colors
age_bins = [0, 18, 30, 50, 100]
age_groups = pd.cut(titanic_data['Age'], bins=age_bins, labels=['Child', 'Young', 'Adult', 'Senior'])
age_counts = age_groups.value_counts().sort_index()

bars = axes[0, 0].bar(age_counts.index, age_counts.values, color=colors_corporate[:len(age_counts)], 
                      edgecolor='white', linewidth=1.2)
axes[0, 0].set_title('Age Group Distribution - Corporate Theme', fontsize=14, fontweight='bold')
axes[0, 0].set_xlabel('Age Groups', fontsize=12)
axes[0, 0].set_ylabel('Number of Passengers', fontsize=12)

# Add value labels on bars
for bar, value in zip(bars, age_counts.values):
    axes[0, 0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                    int(value), ha='center', va='bottom', fontsize=11, fontweight='bold')

# Plot 2: Gradient scatter plot
scatter = axes[0, 1].scatter(titanic_data['Age'], titanic_data['Fare'], 
                            c=titanic_data['Survived'], s=80, alpha=0.7,
                            cmap='RdYlGn', edgecolors='black', linewidth=0.5)
axes[0, 1].set_title('Age vs Fare - Survival Gradient', fontsize=14, fontweight='bold')
axes[0, 1].set_xlabel('Age (Years)', fontsize=12)
axes[0, 1].set_ylabel('Fare (£)', fontsize=12)
cbar = plt.colorbar(scatter, ax=axes[0, 1])
cbar.set_label('Survival Status', fontsize=10)
cbar.set_ticks([0, 1])
cbar.set_ticklabels(['Did not survive', 'Survived'])

# Plot 3: Multi-series line plot with custom styling
class_survival_by_age = []
ages_range = list(range(0, 80, 5))
for pclass in [1, 2, 3]:
    survival_rates = []
    for age in ages_range:
        subset = titanic_data[(titanic_data['Age'] >= age) & 
                             (titanic_data['Age'] < age + 5) & 
                             (titanic_data['Pclass'] == pclass)]
        if len(subset) > 0:
            survival_rates.append(subset['Survived'].mean())
        else:
            survival_rates.append(0)
    
    axes[1, 0].plot(ages_range, survival_rates, marker='o', linewidth=2.5, 
                   markersize=6, label=f'{pclass}st Class' if pclass == 1 
                   else f'{pclass}nd Class' if pclass == 2 else f'{pclass}rd Class',
                   color=colors_academic[pclass-1])

axes[1, 0].set_title('Survival Rate by Age and Class', fontsize=14, fontweight='bold')
axes[1, 0].set_xlabel('Age (Years)', fontsize=12)
axes[1, 0].set_ylabel('Survival Rate', fontsize=12)
axes[1, 0].legend(fontsize=10, framealpha=0.9)
axes[1, 0].set_ylim(0, 1)
axes[1, 0].grid(True, alpha=0.3)

# Plot 4: Enhanced pie chart with professional styling
survival_counts = titanic_data['Survived'].value_counts().sort_index()
wedges, texts, autotexts = axes[1, 1].pie(survival_counts.values,
                                         labels=['Did not survive', 'Survived'],
                                         colors=['#E74C3C', '#27AE60'],
                                         autopct='%1.1f%%',
                                         startangle=90,
                                         explode=(0, 0.1),
                                         shadow=True,
                                         textprops={'fontsize': 12})

# Style the percentage text
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

axes[1, 1].set_title('Survival Distribution - Enhanced Styling', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()

print("🎨 Professional color techniques:")
print("• Custom color palettes for brand consistency")
print("• Gradient colormaps for continuous data")
print("• Strategic use of transparency (alpha)")
print("• Professional edge styling and shadows")






print("🎯 Mastering professional typography and text formatting...")

# Custom font settings
plt.rcParams.update({
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 16
})

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Professional Typography and Text Formatting', 
             fontsize=20, fontweight='bold', y=0.98)

# Plot 1: Enhanced histogram with detailed annotations
ages_hist = axes[0, 0].hist(titanic_data['Age'], bins=15, color='#3498DB', 
                           edgecolor='white', alpha=0.8, linewidth=1.2)
axes[0, 0].set_title('Age Distribution with Statistical Annotations', 
                    fontsize=14, fontweight='bold', pad=20)
axes[0, 0].set_xlabel('Age (Years)', fontsize=12, fontweight='bold')
axes[0, 0].set_ylabel('Number of Passengers', fontsize=12, fontweight='bold')

# Add statistical annotations
mean_age = titanic_data['Age'].mean()
median_age = titanic_data['Age'].median()
axes[0, 0].axvline(mean_age, color='red', linestyle='--', linewidth=2, alpha=0.8)
axes[0, 0].axvline(median_age, color='orange', linestyle='--', linewidth=2, alpha=0.8)

# Professional text box with statistics
stats_text = f'Mean: {mean_age:.1f} years\nMedian: {median_age:.1f} years\nN = {len(titanic_data)}'
axes[0, 0].text(0.7, 0.85, stats_text, transform=axes[0, 0].transAxes,
               bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgray', alpha=0.8),
               fontsize=10, fontweight='bold', verticalalignment='top')

# Plot 2: Bar chart with value labels and formatting
class_counts = titanic_data['Pclass'].value_counts().sort_index()
bars = axes[0, 1].bar(['First Class', 'Second Class', 'Third Class'], 
                     class_counts.values, color=['#F39C12', '#95A5A6', '#8B4513'],
                     edgecolor='black', linewidth=1, alpha=0.9)

axes[0, 1].set_title('Passenger Distribution by Class\n(with Value Labels)', 
                    fontsize=14, fontweight='bold', pad=20)
axes[0, 1].set_ylabel('Number of Passengers', fontsize=12, fontweight='bold')

# Add value labels with professional formatting
for i, (bar, value) in enumerate(zip(bars, class_counts.values)):
    percentage = (value / len(titanic_data)) * 100
    axes[0, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                   f'{value}\n({percentage:.1f}%)', ha='center', va='bottom',
                   fontsize=11, fontweight='bold')

axes[0, 1].set_ylim(0, max(class_counts.values) * 1.15)

# Plot 3: Scatter plot with professional legend and annotations
survivors = titanic_data[titanic_data['Survived'] == 1]
non_survivors = titanic_data[titanic_data['Survived'] == 0]

scatter1 = axes[1, 0].scatter(non_survivors['Age'], non_survivors['Fare'], 
                             alpha=0.6, color='#E74C3C', s=50, label='Did not survive',
                             edgecolors='black', linewidth=0.5)
scatter2 = axes[1, 0].scatter(survivors['Age'], survivors['Fare'], 
                             alpha=0.6, color='#27AE60', s=50, label='Survived',
                             edgecolors='black', linewidth=0.5)

axes[1, 0].set_title('Age vs Fare Relationship by Survival Status', 
                    fontsize=14, fontweight='bold', pad=20)
axes[1, 0].set_xlabel('Age (Years)', fontsize=12, fontweight='bold')
axes[1, 0].set_ylabel('Fare (£)', fontsize=12, fontweight='bold')

# Professional legend with custom styling
legend = axes[1, 0].legend(loc='upper right', frameon=True, fancybox=True, 
                          shadow=True, ncol=1, fontsize=10)
legend.get_frame().set_facecolor('white')
legend.get_frame().set_alpha(0.9)

# Add correlation annotation
correlation = titanic_data['Age'].corr(titanic_data['Fare'])
axes[1, 0].text(0.05, 0.95, f'Age-Fare Correlation: {correlation:.3f}', 
               transform=axes[1, 0].transAxes,
               bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
               fontsize=10, fontweight='bold', verticalalignment='top')

# Plot 4: Multi-category comparison with FIXED professional formatting
survival_by_class = titanic_data.groupby('Pclass')['Survived'].mean()
survival_by_gender = titanic_data.groupby('Sex')['Survived'].mean()

# Create separate grouped bars with proper spacing
x_pos_class = [0, 1, 2]
x_pos_gender = [4, 5]

bars1 = axes[1, 1].bar(x_pos_class, survival_by_class.values, 
                      color=['#F39C12', '#95A5A6', '#8B4513'], alpha=0.8,
                      label='By Class', width=0.6)
bars2 = axes[1, 1].bar(x_pos_gender, survival_by_gender.values, 
                      color=['#E91E63', '#2196F3'], alpha=0.8,
                      label='By Gender', width=0.6)

# FIXED: Set ticks and labels properly
all_positions = x_pos_class + x_pos_gender  # [0, 1, 2, 4, 5]
all_labels = ['1st Class', '2nd Class', '3rd Class', 'Female', 'Male']  # 5 labels for 5 positions

axes[1, 1].set_xticks(all_positions)  # Set 5 tick positions
axes[1, 1].set_xticklabels(all_labels, fontsize=10, fontweight='bold')  # Set 5 labels

axes[1, 1].set_title('Survival Rates: Multiple Category Analysis', 
                    fontsize=14, fontweight='bold', pad=20)
axes[1, 1].set_ylabel('Survival Rate', fontsize=12, fontweight='bold')
axes[1, 1].set_ylim(0, 1)

# Add value labels on bars
all_bars = list(bars1) + list(bars2)
all_values = list(survival_by_class.values) + list(survival_by_gender.values)
for bar, value in zip(all_bars, all_values):
    axes[1, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                   f'{value:.2f}', ha='center', va='bottom',
                   fontsize=10, fontweight='bold')

axes[1, 1].legend(loc='upper right', fontsize=10, framealpha=0.9)
axes[1, 1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

print("📝 Professional typography features:")
print("• Consistent font sizes and weights")
print("• Strategic use of bold text for emphasis")
print("• Professional text boxes with rounded corners")
print("• Clear value labels and statistical annotations")
print("• Enhanced legends with shadows and transparency")
print("• FIXED: Proper x-tick and label matching")







print("🎯 Mastering export formats and high-quality output...")

# Create a publication-ready visualization for export testing
plt.style.use('seaborn-v0_8-white')

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Titanic Analysis - Publication Ready Export', 
             fontsize=18, fontweight='bold', y=0.98)

# High-quality plots for export
# Plot 1: Age distribution with ax parameter
titanic_data['Age'].plot(kind='hist', bins=15, ax=axes[0, 0], 
                        color='#2E86AB', alpha=0.8, edgecolor='white')
axes[0, 0].set_title('Age Distribution', fontsize=14, fontweight='bold')
axes[0, 0].set_xlabel('Age (Years)')
axes[0, 0].set_ylabel('Count')
axes[0, 0].grid(axis='y', alpha=0.3)

# Plot 2: Survival by class with ax parameter
survival_by_class = titanic_data.groupby('Pclass')['Survived'].mean()
survival_by_class.plot(kind='bar', ax=axes[0, 1], color=['#FFD700', '#C0C0C0', '#CD7F32'],
                      edgecolor='black')
axes[0, 1].set_title('Survival Rate by Class', fontsize=14, fontweight='bold')
axes[0, 1].set_xlabel('Passenger Class')
axes[0, 1].set_ylabel('Survival Rate')
axes[0, 1].set_xticklabels(['1st', '2nd', '3rd'], rotation=0)
axes[0, 1].set_ylim(0, 1)

# Add value labels on bars
for i, (idx, value) in enumerate(survival_by_class.items()):
    axes[0, 1].text(i, value + 0.02, f'{value:.2f}', ha='center', va='bottom', 
                   fontsize=10, fontweight='bold')

# Plot 3: Gender survival with ax parameter
gender_survival = titanic_data.groupby('Sex')['Survived'].mean()
gender_survival.plot(kind='bar', ax=axes[1, 0], color=['#FF69B4', '#4169E1'],
                    edgecolor='black')
axes[1, 0].set_title('Survival Rate by Gender', fontsize=14, fontweight='bold')
axes[1, 0].set_xlabel('Gender')
axes[1, 0].set_ylabel('Survival Rate')
axes[1, 0].set_xticklabels(['Female', 'Male'], rotation=0)
axes[1, 0].set_ylim(0, 1)

# Add value labels on bars
for i, (idx, value) in enumerate(gender_survival.items()):
    axes[1, 0].text(i, value + 0.02, f'{value:.2f}', ha='center', va='bottom', 
                   fontsize=10, fontweight='bold')

# Plot 4: Age vs Fare scatter
scatter = axes[1, 1].scatter(titanic_data['Age'], titanic_data['Fare'], 
                           c=titanic_data['Survived'], cmap='RdYlGn', 
                           alpha=0.7, edgecolors='black', linewidth=0.3)
axes[1, 1].set_title('Age vs Fare by Survival', fontsize=14, fontweight='bold')
axes[1, 1].set_xlabel('Age (Years)')
axes[1, 1].set_ylabel('Fare (£)')
axes[1, 1].grid(True, alpha=0.3)

# Add colorbar with proper positioning
cbar = plt.colorbar(scatter, ax=axes[1, 1], shrink=0.8)
cbar.set_label('Survival Status', fontsize=10)
cbar.set_ticks([0, 1])
cbar.set_ticklabels(['Did not survive', 'Survived'])

plt.tight_layout()

# Export in multiple formats with different settings
print("📁 Exporting in multiple formats...")

try:
    # High-resolution PNG for presentations
    plt.savefig('titanic_analysis_presentation.png', 
               dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    print("✅ High-res PNG saved: titanic_analysis_presentation.png")
    
    # PDF for publications
    plt.savefig('titanic_analysis_publication.pdf', 
               dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    print("✅ Publication PDF saved: titanic_analysis_publication.pdf")
    
    # SVG for web/scalable graphics
    plt.savefig('titanic_analysis_web.svg', 
               bbox_inches='tight', facecolor='white', edgecolor='none')
    print("✅ Scalable SVG saved: titanic_analysis_web.svg")
    
    # Low-res PNG for web
    plt.savefig('titanic_analysis_web.png', 
               dpi=150, bbox_inches='tight', facecolor='white', edgecolor='none')
    print("✅ Web-optimized PNG saved: titanic_analysis_web.png")
    
except Exception as e:
    print(f"⚠️ Export error: {e}")
    print("Files will be saved to current directory")

plt.show()

print("💾 Export format comparison:")
print("• PNG (high-res): Best for presentations, posters")
print("• PDF: Best for publications, print materials")
print("• SVG: Best for web, scalable graphics")
print("• PNG (low-res): Best for web, email attachments")

print("\n📊 Export settings explained:")
print("• dpi=300: High resolution for print quality")
print("• dpi=150: Medium resolution for web use")
print("• bbox_inches='tight': Removes extra whitespace")
print("• facecolor='white': Sets background color")
print("• edgecolor='none': Removes border")

print("\n🎯 Lab 5.4 completed successfully!")







print("🎯 PRACTICE PROJECT: Complete Professional Titanic Analysis Report")

# Professional styling setup
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.titlesize': 16
})

# Create comprehensive professional report
fig = plt.figure(figsize=(20, 14))
fig.suptitle('Titanic Disaster Analysis - Professional Research Report', 
             fontsize=22, fontweight='bold', y=0.98)

# Layout: Complex grid for professional report
# Top row: 3 plots
ax1 = plt.subplot2grid((4, 6), (0, 0), colspan=2)  # Age distribution
ax2 = plt.subplot2grid((4, 6), (0, 2), colspan=2)  # Survival overview
ax3 = plt.subplot2grid((4, 6), (0, 4), colspan=2)  # Class distribution

# Second row: 2 plots
ax4 = plt.subplot2grid((4, 6), (1, 0), colspan=3)  # Survival by demographics
ax5 = plt.subplot2grid((4, 6), (1, 3), colspan=3)  # Fare analysis

# Third row: 2 plots  
ax6 = plt.subplot2grid((4, 6), (2, 0), colspan=3)  # Age vs Fare relationship
ax7 = plt.subplot2grid((4, 6), (2, 3), colspan=3)  # Multi-factor analysis

# Bottom row: Summary statistics
ax8 = plt.subplot2grid((4, 6), (3, 0), colspan=6)   # Summary table/text

# Plot 1: Age Distribution with Statistics
titanic_data['Age'].plot(kind='hist', bins=20, ax=ax1, color='#3498DB', 
                        alpha=0.7, edgecolor='white')
ax1.set_title('Age Distribution of Passengers', fontweight='bold')
ax1.set_xlabel('Age (Years)')
ax1.set_ylabel('Count')
ax1.grid(axis='y', alpha=0.3)

mean_age = titanic_data['Age'].mean()
ax1.axvline(mean_age, color='red', linestyle='--', linewidth=2, alpha=0.8)
ax1.text(0.7, 0.8, f'Mean Age: {mean_age:.1f}', transform=ax1.transAxes,
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Plot 2: Overall Survival Rate
survival_counts = titanic_data['Survived'].value_counts().sort_index()
colors = ['#E74C3C', '#27AE60']
wedges, texts, autotexts = ax2.pie(survival_counts.values, 
                                  labels=['Perished', 'Survived'],
                                  colors=colors, autopct='%1.1f%%',
                                  startangle=90, textprops={'fontweight': 'bold'})
ax2.set_title('Overall Survival Rate', fontweight='bold')

# Plot 3: Class Distribution
class_counts = titanic_data['Pclass'].value_counts().sort_index()
bars = ax3.bar(['First', 'Second', 'Third'], class_counts.values,
               color=['#F39C12', '#95A5A6', '#8B4513'], alpha=0.8, edgecolor='black')
ax3.set_title('Passengers by Class', fontweight='bold')
ax3.set_ylabel('Count')
for bar, count in zip(bars, class_counts.values):
    ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             str(count), ha='center', va='bottom', fontweight='bold')

# Plot 4: Survival Rates by Demographics
demographics = ['Overall', 'Male', 'Female', '1st Class', '2nd Class', '3rd Class']
survival_rates = [
    titanic_data['Survived'].mean(),
    titanic_data[titanic_data['Sex'] == 'male']['Survived'].mean(),
    titanic_data[titanic_data['Sex'] == 'female']['Survived'].mean(),
    titanic_data[titanic_data['Pclass'] == 1]['Survived'].mean(),
    titanic_data[titanic_data['Pclass'] == 2]['Survived'].mean(),
    titanic_data[titanic_data['Pclass'] == 3]['Survived'].mean()
]

bars = ax4.bar(demographics, survival_rates, 
               color=['gray', '#2E86AB', '#A23B72', '#F39C12', '#95A5A6', '#8B4513'],
               alpha=0.8, edgecolor='black')
ax4.set_title('Survival Rates by Demographics', fontweight='bold')
ax4.set_ylabel('Survival Rate')
ax4.set_ylim(0, 1)
ax4.tick_params(axis='x', rotation=45)
ax4.grid(axis='y', alpha=0.3)
for bar, rate in zip(bars, survival_rates):
    ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
             f'{rate:.2f}', ha='center', va='bottom', fontweight='bold')

# Plot 5: Fare Analysis by Class (using matplotlib boxplot, not pandas)
fare_data = [titanic_data[titanic_data['Pclass'] == i]['Fare'] for i in [1, 2, 3]]
bp = ax5.boxplot(fare_data, labels=['1st Class', '2nd Class', '3rd Class'],
                patch_artist=True)
colors_box = ['#FFD700', '#C0C0C0', '#CD7F32']
for patch, color in zip(bp['boxes'], colors_box):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
ax5.set_title('Fare Distribution by Class', fontweight='bold')
ax5.set_ylabel('Fare (£)')
ax5.grid(axis='y', alpha=0.3)

# Plot 6: Age vs Fare Relationship
scatter = ax6.scatter(titanic_data['Age'], titanic_data['Fare'], 
                     c=titanic_data['Pclass'], cmap='viridis', 
                     alpha=0.6, s=30, edgecolors='black', linewidth=0.3)
ax6.set_title('Age vs Fare by Passenger Class', fontweight='bold')
ax6.set_xlabel('Age (Years)')
ax6.set_ylabel('Fare (£)')
ax6.grid(True, alpha=0.3)
cbar = plt.colorbar(scatter, ax=ax6, shrink=0.8)
cbar.set_label('Class')
cbar.set_ticks([1, 2, 3])

# Plot 7: Multi-factor Survival Analysis
age_groups = pd.cut(titanic_data['Age'], bins=[0, 18, 35, 60, 100], 
                    labels=['Child', 'Young', 'Adult', 'Senior'])
multi_factor = titanic_data.copy()
multi_factor['AgeGroup'] = age_groups
survival_matrix = multi_factor.groupby(['AgeGroup', 'Sex'])['Survived'].mean().unstack()

# Use ax parameter with pandas plot
survival_matrix.plot(kind='bar', ax=ax7, color=['#E91E63', '#2196F3'], alpha=0.8)
ax7.set_title('Survival Rate by Age Group and Gender', fontweight='bold')
ax7.set_xlabel('Age Group')
ax7.set_ylabel('Survival Rate')
ax7.legend(title='Gender', labels=['Female', 'Male'])
ax7.set_ylim(0, 1)
ax7.tick_params(axis='x', rotation=45)
ax7.grid(axis='y', alpha=0.3)

# Plot 8: Summary Statistics Table
ax8.axis('off')
summary_text = f"""
KEY FINDINGS - TITANIC DISASTER ANALYSIS
═══════════════════════════════════════════════════════════════════════════════════════════

PASSENGER DEMOGRAPHICS:
• Total Passengers Analyzed: {len(titanic_data)}
• Average Age: {titanic_data['Age'].mean():.1f} years
• Age Range: {titanic_data['Age'].min():.0f} - {titanic_data['Age'].max():.0f} years
• Gender Split: {len(titanic_data[titanic_data['Sex']=='male'])} Male, {len(titanic_data[titanic_data['Sex']=='female'])} Female

SURVIVAL STATISTICS:
• Overall Survival Rate: {titanic_data['Survived'].mean():.1%}
• Female Survival Rate: {titanic_data[titanic_data['Sex']=='female']['Survived'].mean():.1%}
• Male Survival Rate: {titanic_data[titanic_data['Sex']=='male']['Survived'].mean():.1%}
• 1st Class Survival: {titanic_data[titanic_data['Pclass']==1]['Survived'].mean():.1%}
• 3rd Class Survival: {titanic_data[titanic_data['Pclass']==3]['Survived'].mean():.1%}

ECONOMIC FACTORS:
• Average Fare: £{titanic_data['Fare'].mean():.2f}
• 1st Class Avg Fare: £{titanic_data[titanic_data['Pclass']==1]['Fare'].mean():.2f}
• 3rd Class Avg Fare: £{titanic_data[titanic_data['Pclass']==3]['Fare'].mean():.2f}

ANALYSIS METHODOLOGY:
• Data visualized using matplotlib and pandas
• Professional styling applied throughout
• Statistical measures include mean, correlation, and distribution analysis
• Export formats: High-resolution PNG and PDF for publication
"""

ax8.text(0.05, 0.95, summary_text, transform=ax8.transAxes, fontsize=10,
         verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round,pad=1', facecolor='lightgray', alpha=0.8))

plt.tight_layout()

# Export the complete report with error handling
try:
    plt.savefig('titanic_complete_professional_report.png', dpi=300, bbox_inches='tight')
    print("✅ High-res PNG saved: titanic_complete_professional_report.png")
    
    plt.savefig('titanic_complete_professional_report.pdf', dpi=300, bbox_inches='tight')
    print("✅ Publication PDF saved: titanic_complete_professional_report.pdf")
    
except Exception as e:
    print(f"⚠️ Export error: {e}")
    print("Report will be displayed but files may not be saved")

plt.show()

print("🎉 PROFESSIONAL REPORT COMPLETE!")
print("📊 Report features:")
print("• 8 different visualization types")
print("• Professional color schemes and typography")
print("• Statistical annotations and value labels")
print("• Comprehensive summary statistics")
print("• High-resolution export capabilities")
print("\n✅ Part 5 Practice Project completed successfully!")
print("🚀 You now have publication-ready matplotlib mastery!")

# Additional: Create a summary skills chart
plt.style.use('default')
fig, ax = plt.subplots(figsize=(12, 8))

skills = ['Basic Plots', 'Customization', 'Subplots', 'Pandas Integration', 'Professional Styling']
proficiency = [100, 100, 100, 100, 100]

bars = ax.bar(skills, proficiency, color=['#3498DB', '#E74C3C', '#2ECC71', '#F39C12', '#9B59B6'],
              alpha=0.8, edgecolor='black', linewidth=1)

ax.set_title('Matplotlib Mastery - Part 5 Complete!', fontsize=18, fontweight='bold', pad=20)
ax.set_ylabel('Proficiency Level (%)', fontsize=14)
ax.set_ylim(0, 120)

for bar, skill in zip(bars, skills):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
            '✓ MASTERED!', ha='center', va='bottom', 
            fontsize=12, fontweight='bold', color='darkgreen')

ax.grid(axis='y', alpha=0.3)
plt.tight_layout()

try:
    plt.savefig('matplotlib_mastery_complete.png', dpi=300, bbox_inches='tight')
    print("💾 Skills summary saved: matplotlib_mastery_complete.png")
except:
    print("💾 Skills summary displayed")

plt.show()

print("🎯 CONGRATULATIONS! You've completed the entire matplotlib foundations series!")







# Create a final summary visualization
plt.style.use('seaborn-v0_8-white')
fig, ax = plt.subplots(figsize=(12, 8))

# Summary of your matplotlib journey
skills = ['Basic Plots', 'Customization', 'Subplots', 'Pandas Integration', 'Professional Styling']
proficiency = [100, 100, 100, 100, 100]  # You've mastered them all!

bars = ax.bar(skills, proficiency, color=['#3498DB', '#E74C3C', '#2ECC71', '#F39C12', '#9B59B6'],
              alpha=0.8, edgecolor='black', linewidth=1)

ax.set_title('Matplotlib Mastery - Week 12 Complete!', fontsize=18, fontweight='bold', pad=20)
ax.set_ylabel('Proficiency Level (%)', fontsize=14)
ax.set_ylim(0, 120)

# Add congratulatory labels
for bar, skill in zip(bars, skills):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
            '✓ MASTERED!', ha='center', va='bottom', 
            fontsize=12, fontweight='bold', color='darkgreen')

ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('matplotlib_mastery_complete.png', dpi=300, bbox_inches='tight')
plt.show()

print("💾 Final summary saved as 'matplotlib_mastery_complete.png'")
print("🎯 Part 5 complete! You've mastered professional matplotlib!")
