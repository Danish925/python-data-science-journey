print("LAB 1.1: ENVIRONMENT SETUP.")
# Step 1: Install matplotlib (run in terminal/command prompt)
# pip install matplotlib

# Step 2: Import conventions - only pandas and matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# Step 3: Jupyter notebook setup (if using Jupyter)
# %matplotlib inline

print("✅ Matplotlib and pandas imported successfully!")
print(f"Matplotlib version: {plt.matplotlib.__version__}")
print(f"Pandas version: {pd.__version__}\n")





print("LAB 1.2: FIRST PLOT WITH PANDAS DATA.")
print("🎯 Creating your first matplotlib plot using pandas...")

# Step 1: Create simple data using pandas
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [2, 4, 6, 8, 10]
})

# Step 2: Create the plot
plt.plot(data['x'], data['y'])

# Step 3: Display the plot
plt.show()

print("🎉 Congratulations! You've created your first matplotlib plot with pandas data!")


# Method 1: Using plt.show() - explicit display
data = pd.Series([1, 4, 9, 16, 25])
plt.plot(data)
plt.show()

print("Plot displayed above using plt.show()")

# Method 2: Using semicolon - suppresses output text
plt.plot(data);

print("Plot displayed above using semicolon")

# Method 3: In Jupyter - often no need for either
plt.plot(data)
# Jupyter automatically displays the plot

 


print(f"\nLAB 1.3: FIGURE VS AXES CONCEPTS WITH PANDAS.")
print("🎯 Understanding Figure vs Axes using pandas data...")

# Create sample pandas data
df = pd.DataFrame({
    'day': [1, 2, 3, 4],
    'value': [1, 4, 2, 3]
})

# Method 1: Simple pyplot interface
plt.figure(figsize=(8, 6))
plt.plot(df['day'], df['value'])
plt.title("This is a Figure with one Axes")
plt.show()

# Method 2: Object-oriented interface
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(df['day'], df['value'])
ax.set_title("Same plot using OO interface with pandas data")
plt.show()

print("📚 Key Concepts:")
print("• Figure = The entire window/canvas")
print("• Axes = The actual plot area with x and y axes")
print(f"• You can have multiple Axes in one Figure!\n")




print("LAB 1.4: LINE PLOT FUNDAMENTALS WITH PANDAS.")
print("🎯 Plotting pandas Series...")

# Create a pandas Series - like a single column from Excel
steps_data = pd.Series([10, 25, 30, 35, 20, 15, 25], 
                       name='Daily Steps (thousands)')

plt.figure(figsize=(8, 5))
plt.plot(steps_data)
plt.title("Single Series Plot (x-values auto-generated)")
plt.xlabel("Day Index")
plt.ylabel("Steps (thousands)")
plt.show()

print("📝 Notice: x-axis uses pandas Series index automatically!")


print("🎯 Plotting DataFrame columns...")

# Create a DataFrame - like a small Excel table
weekly_data = pd.DataFrame({
    'day': [1, 2, 3, 4, 5, 6, 7],
    'steps': [8000, 12000, 6000, 15000, 9000, 11000, 7000],
    'day_name': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
})

plt.figure(figsize=(10, 6))
plt.plot(weekly_data['day'], weekly_data['steps'])
plt.title("Daily Step Count Over a Week")
plt.xlabel("Day of Week")
plt.ylabel("Steps")
plt.grid(True)
plt.show()

print("📝 This uses DataFrame columns for x and y values!")
print("Data preview:")
print(weekly_data.head(3))




print(f"\nLAB 1.5: BASIC LINE CUSTOMIZATION WITH PANDAS DATA.")
print("🎯 Customizing line appearance using pandas data...")

# Use the same DataFrame from before
weekly_data = pd.DataFrame({
    'day': [1, 2, 3, 4, 5, 6, 7],
    'steps': [8000, 12000, 6000, 15000, 9000, 11000, 7000],
    'day_name': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
})

plt.figure(figsize=(12, 8))

# Different line styles and colors
plt.subplot(2, 2, 1)
plt.plot(weekly_data['day'], weekly_data['steps'], color='red')
plt.title("Red Line")

plt.subplot(2, 2, 2)
plt.plot(weekly_data['day'], weekly_data['steps'], color='blue', linestyle='--')
plt.title("Blue Dashed Line")

plt.subplot(2, 2, 3)
plt.plot(weekly_data['day'], weekly_data['steps'], color='green', marker='o')
plt.title("Green Line with Markers")

plt.subplot(2, 2, 4)
plt.plot(weekly_data['day'], weekly_data['steps'], color='purple', marker='s', linestyle='-.')
plt.title("Purple Line, Square Markers, Dash-dot")

plt.tight_layout()
plt.show()

print("🎨 Line customization options:")
print("• Colors: 'red', 'blue', 'green', 'purple', '#FF5733'")
print("• Line styles: '-' (solid), '--' (dashed), ':' (dotted), '-.' (dash-dot)")
print("• Markers: 'o' (circle), 's' (square), '^' (triangle)")





print("🎯 PRACTICE PROJECT: Titanic Age Visualization")
print("Using your pandas skills with matplotlib!")

# Load Titanic data (use your saved data from previous work)
# If you don't have it saved, create sample data:
titanic_sample = pd.DataFrame({
    'Age': [22, 38, 26, 35, 35, 54, 2, 27, 14, 4, 58, 20, 39, 14, 55, 2],
    'Survived': [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    'Pclass': [3, 1, 3, 1, 3, 1, 3, 3, 2, 3, 1, 3, 1, 3, 1, 3]
})

# Get first 10 passengers' ages for our line plot
ages_subset = titanic_sample['Age'].head(10)
passenger_numbers = pd.Series(range(1, 11))

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(passenger_numbers, ages_subset, color='steelblue', marker='o', 
         linewidth=2, markersize=8)

plt.title('First 10 Titanic Passengers - Age Profile', fontsize=16, fontweight='bold')
plt.xlabel('Passenger Number', fontsize=12)
plt.ylabel('Age (Years)', fontsize=12)

# Add grid for better readability
plt.grid(True, alpha=0.3)

# Find and annotate youngest passenger
youngest_idx = ages_subset.idxmin()
youngest_age = ages_subset.min()
youngest_passenger = passenger_numbers[youngest_idx]

plt.annotate(f'Youngest: {youngest_age} years', 
             xy=(youngest_passenger, youngest_age),
             xytext=(youngest_passenger + 1, youngest_age + 5),
             arrowprops=dict(arrowstyle='->', color='red'),
             fontsize=10, ha='center')

plt.tight_layout()
plt.show()

print("🎉 Project Complete!")
print("📊 Data used:")
print(titanic_sample[['Age', 'Survived', 'Pclass']].head())
print(f"📈 Youngest passenger in sample: {youngest_age} years old\n")





# Essential commands learned with pandas integration:
essential_commands = {
    'Import': 'import matplotlib.pyplot as plt, pandas as pd',
    'Plot DataFrame columns': 'plt.plot(df["x"], df["y"])',
    'Plot Series': 'plt.plot(series)',
    'Display': 'plt.show()',
    'Figure Size': 'plt.figure(figsize=(width, height))',
    'Title': 'plt.title("Your Title")',
    'Labels': 'plt.xlabel("X Label"), plt.ylabel("Y Label")',
    'Colors': 'plt.plot(x, y, color="red")',
    'Line Style': 'plt.plot(x, y, linestyle="--")',
    'Markers': 'plt.plot(x, y, marker="o")',
    'Grid': 'plt.grid(True)'
}

print("📚 ESSENTIAL MATPLOTLIB + PANDAS COMMANDS:")
for concept, command in essential_commands.items():
    print(f"• {concept:24}: {command}")




# Save your practice project plot
titanic_sample = pd.DataFrame({
    'Age': [22, 38, 26, 35, 35, 54, 2, 27, 14, 4],
    'PassengerId': range(1, 11)
})

plt.figure(figsize=(10, 6))
plt.plot(titanic_sample['PassengerId'], titanic_sample['Age'], 
         color='steelblue', marker='o', linewidth=2, markersize=8)
plt.title('Titanic Passengers - Age Profile', fontsize=16)
plt.xlabel('Passenger ID', fontsize=12)
plt.ylabel('Age (Years)', fontsize=12)
plt.grid(True, alpha=0.3)

plt.savefig('part1_practice_project.png', dpi=300, bbox_inches='tight')
plt.show()

print("💾 Plot saved as 'part1_practice_project.png'")
print("🎯 Part 1 complete! Ready for histograms and data distribution in part 2!")
