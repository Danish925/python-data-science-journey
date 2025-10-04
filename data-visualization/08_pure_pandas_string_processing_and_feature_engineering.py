print("=== PURE PANDAS STRING PROCESSING & FEATURE ENGINEERING ===")
print("Session 3: Transform text into powerful features with 100% pandas methods")

# Import ONLY pandas and built-in Python libraries
import pandas as pd
import re  # Built-in Python regular expressions

# Set pandas display options for better output
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 50)

print("\n🔧 Environment setup complete!")
print("🎯 Today's Goal: Master pandas string methods for feature engineering")
print("🚫 NO NUMPY: Pure pandas methods only!")



print("\n📊 1. pandas String Accessor (.str) Basics - pandas-Only")

# Load our optimized Titanic dataset (from Tuesday)
titanic_url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_df = pd.read_csv(titanic_url)

# Apply all our Week 11 enhancements quickly using pandas-only methods
print("🔧 Applying Week 11 enhancements using pandas-only...")

# Monday: Missing value fixes (pandas-only)
age_by_group = titanic_df.groupby(['Pclass', 'Sex'])['Age'].transform('median')
titanic_df['Age'] = titanic_df['Age'].fillna(age_by_group)
titanic_df['Embarked'] = titanic_df['Embarked'].fillna(titanic_df['Embarked'].mode()[0])

# Tuesday: Data type optimizations (pandas-only)
titanic_df['Pclass'] = titanic_df['Pclass'].astype('category')
titanic_df['Sex'] = titanic_df['Sex'].astype('category')
titanic_df['Embarked'] = titanic_df['Embarked'].astype('category')
titanic_df['Survived'] = titanic_df['Survived'].astype('bool')

print("✅ Dataset enhanced with Week 11 improvements using pandas-only!")
print(f"Dataset shape: {titanic_df.shape}")

print("\n🎯 Pure pandas Syntax: .str accessor")
print("• df['col'].str.method() → Apply string methods to entire Series")
print("• Works element-wise on each string in the Series")
print("• Returns new Series with transformed values")

# Explore the Name column - our main string processing target
print("\n📋 Sample Names from Titanic:")
sample_names = titanic_df['Name'].head(10)
for i, name in enumerate(sample_names):
    print(f"{i+1:2d}. {name}")

print("\n1. Basic String Information using pandas-only:")
print(f"Total names: {len(titanic_df['Name'])}")
print(f"Unique names: {titanic_df['Name'].nunique()}")
print(f"Any duplicates: {titanic_df['Name'].nunique() < len(titanic_df['Name'])}")

# Basic string operations using pandas-only
print("\n2. String Length Analysis:")
titanic_df['Name_Length'] = titanic_df['Name'].str.len()
print("Name length statistics:")
print(titanic_df['Name_Length'].describe())

# Find shortest and longest names using pandas methods
shortest_idx = titanic_df['Name_Length'].idxmin()
longest_idx = titanic_df['Name_Length'].idxmax()
print(f"Shortest name: {titanic_df.loc[shortest_idx, 'Name']}")
print(f"Longest name: {titanic_df.loc[longest_idx, 'Name']}")

print("\n3. Case Operations using pandas string methods:")
# Convert to different cases using pandas .str methods
print("Original name:", titanic_df['Name'].iloc[0])
print("Lowercase:", titanic_df['Name'].str.lower().iloc[0])
print("Uppercase:", titanic_df['Name'].str.upper().iloc[0])
print("Title case:", titanic_df['Name'].str.title().iloc[0])



print("\n📊 2. Pattern Detection with Pure pandas .str Methods")

print("🎯 Pure pandas Syntax for Pattern Detection:")
print("• .str.contains('pattern') → Boolean Series for pattern matching")
print("• .str.startswith('pattern') → Check if strings start with pattern")
print("• .str.endswith('pattern') → Check if strings end with pattern")

# Pattern detection examples using pandas-only methods
print("\n1. Detecting Patterns in Names:")

# Check for parentheses (maiden names, nicknames) using pandas regex
titanic_df['Has_Parentheses'] = titanic_df['Name'].str.contains(r'\(.*\)', na=False, regex=True)
parentheses_count = titanic_df['Has_Parentheses'].sum()
print(f"Names with parentheses: {parentheses_count}")

# Show examples using pandas boolean indexing
if parentheses_count > 0:
    print("Examples with parentheses:")
    examples = titanic_df[titanic_df['Has_Parentheses']]['Name'].head(3)
    for name in examples:
        print(f"  • {name}")

# Check for quotes (nicknames) using pandas string methods
titanic_df['Has_Quotes'] = titanic_df['Name'].str.contains('"', na=False, regex=False)
quotes_count = titanic_df['Has_Quotes'].sum()
print(f"\nNames with quotes: {quotes_count}")

if quotes_count > 0:
    print("Examples with quotes:")
    examples = titanic_df[titanic_df['Has_Quotes']]['Name'].head(3)
    for name in examples:
        print(f"  • {name}")

# Check for specific titles using pandas string methods
common_titles = ['Mr.', 'Mrs.', 'Miss.', 'Master.']
print(f"\n2. Title Distribution using pandas:")
for title in common_titles:
    count = titanic_df['Name'].str.contains(title, na=False, regex=False).sum()
    percentage = (count / len(titanic_df) * 100)
    print(f"{title:<8}: {count:3d} ({percentage:5.1f}%)")

# Multiple pattern matching using pandas operations
print(f"\n3. Advanced Pattern Matching with pandas:")
# Names with multiple words (complex names)
titanic_df['Word_Count'] = titanic_df['Name'].str.split().str.len()
print("Word count in names:")
print(titanic_df['Word_Count'].value_counts().sort_index())

# Names starting with vowels using pandas string methods
titanic_df['Starts_Vowel'] = titanic_df['Name'].str.startswith(('A', 'E', 'I', 'O', 'U'), na=False)
vowel_start_count = titanic_df['Starts_Vowel'].sum()
print(f"\nNames starting with vowels: {vowel_start_count}")



print("\n📊 3. String Splitting and Component Extraction with pandas-Only")

print("🎯 Pure pandas Syntax for String Splitting:")
print("• .str.split() → Split strings into lists")
print("• .str.split(expand=True) → Split into separate columns")  
print("• .str.split().str[0] → Get first element after splitting")

# Analyze name structure using pandas methods
print("\n1. Understanding Name Structure:")
sample_names = titanic_df['Name'].head(5)
for i, name in enumerate(sample_names):
    print(f"{i+1}. {name}")
    # Use pandas string split method
    parts = name.split(', ')
    if len(parts) >= 2:
        print(f"   Last name: {parts[0]}")
        print(f"   Rest: {parts[1]}")
    print()

# Split names into components using pandas methods
print("2. Splitting Names into Components:")
# Most Titanic names follow pattern: "Lastname, Title Firstname"
name_parts = titanic_df['Name'].str.split(', ', expand=True, n=1)
name_parts.columns = ['Last_Name', 'First_Title']

print("📋 Name splitting results:")
print(name_parts.head(10))

# Extract family name using pandas
titanic_df['Family_Name'] = name_parts['Last_Name']
print(f"\n✅ Family names extracted using pandas")
print(f"Unique family names: {titanic_df['Family_Name'].nunique()}")

# Most common family names using pandas value_counts
print("\nMost common family names:")
print(titanic_df['Family_Name'].value_counts().head(10))

# Split first name and title part further using pandas
print("\n3. Advanced Name Parsing with pandas:")
first_title_parts = name_parts['First_Title'].str.split(' ', expand=True)
print("First name and title parts:")
print(first_title_parts.head(10))

# Extract just the first word after comma (usually title) using pandas
titanic_df['Title_Raw'] = name_parts['First_Title'].str.split(' ').str[0]
print("\nRaw titles extracted using pandas:")
print(titanic_df['Title_Raw'].value_counts().head(15))



print("\n📊 4. Regex Pattern Extraction with pandas-Only")

print("🎯 POWER TECHNIQUE: .str.extract() with Regular Expressions")
print("• .str.extract(r'pattern') → Extract first match using regex")
print("• .str.extractall(r'pattern') → Extract all matches")
print("• Uses parentheses () to define capture groups")
print("• Pure pandas - no external regex library needed!")

print("\n1. Title Extraction with Regex using pandas:")
# Extract titles using regex - more precise than splitting
# Pattern: comma, optional space, capture word(s), period
title_pattern = r', ([^.]*)\.'
titanic_df['Title'] = titanic_df['Name'].str.extract(title_pattern)

print("✅ Titles extracted using pandas regex!")
print("\n📋 Title distribution:")
title_counts = titanic_df['Title'].value_counts()
print(title_counts.head(15))

# Show examples of extraction using pandas indexing
print("\n🔍 Title Extraction Examples:")
sample_indices = [0, 1, 2, 50, 100]
for idx in sample_indices:
    name = titanic_df.loc[idx, 'Name']
    title = titanic_df.loc[idx, 'Title']
    print(f"'{name}' → Title: '{title}'")

print("\n2. Advanced Title Cleaning using pandas:")
print("🎯 Handling Special Cases and Variations")

# Some titles have extra spaces or variations - clean them using pandas
titanic_df['Title_Clean'] = titanic_df['Title'].str.strip()  # Remove extra spaces

# Map similar titles together using pandas map method
title_mapping = {
    'Mr': 'Mr',
    'Miss': 'Miss',
    'Mrs': 'Mrs', 
    'Master': 'Master',
    'Dr': 'Dr',
    'Rev': 'Rev',
    'Col': 'Officer',
    'Major': 'Officer',
    'Capt': 'Officer',
    'Countess': 'Royalty',
    'Lady': 'Royalty',
    'Sir': 'Royalty',
    'Don': 'Royalty',
    'Dona': 'Royalty',
    'Jonkheer': 'Royalty',
    'Mlle': 'Miss',  # Mademoiselle (French)
    'Ms': 'Miss',
    'Mme': 'Mrs'     # Madame (French)
}

titanic_df['Title_Grouped'] = titanic_df['Title_Clean'].map(title_mapping)
# Fill any unmapped titles as 'Other' using pandas fillna
titanic_df['Title_Grouped'] = titanic_df['Title_Grouped'].fillna('Other')

print("📋 Grouped title distribution:")
print(titanic_df['Title_Grouped'].value_counts())

print("\n3. First Name Extraction using pandas:")
# Extract first names - more complex regex using pandas
# Pattern: after title and optional spaces, capture word(s) before space or end
firstname_pattern = r', [^.]*\.\s+([A-Za-z]+)'
titanic_df['First_Name'] = titanic_df['Name'].str.extract(firstname_pattern)

print("✅ First names extracted using pandas!")
print(f"First names found: {titanic_df['First_Name'].notna().sum()}")

# Show examples using pandas boolean indexing
print("\n🔍 First Name Extraction Examples:")
has_firstname = titanic_df['First_Name'].notna()
sample_with_names = titanic_df[has_firstname].head(5)
for idx, row in sample_with_names.iterrows():
    print(f"'{row['Name']}' → First: '{row['First_Name']}'")



print("\n📊 5. Ticket Pattern Analysis with pandas-Only")

print("🎯 Analyzing Ticket Patterns for Hidden Information")

# Explore ticket structure using pandas methods
print("\n1. Ticket Pattern Exploration:")
sample_tickets = titanic_df['Ticket'].head(15)
print("Sample tickets:")
for i, ticket in enumerate(sample_tickets):
    print(f"{i+1:2d}. {ticket}")

print(f"\n📊 Ticket Statistics using pandas:")
print(f"Total tickets: {len(titanic_df['Ticket'])}")
print(f"Unique tickets: {titanic_df['Ticket'].nunique()}")
print(f"Duplicate tickets: {len(titanic_df['Ticket']) - titanic_df['Ticket'].nunique()}")

# Check if ticket is purely numeric using pandas
titanic_df['Ticket_Is_Numeric'] = titanic_df['Ticket'].str.isdigit()
numeric_count = titanic_df['Ticket_Is_Numeric'].sum()
print(f"Purely numeric tickets: {numeric_count}")

print("\n2. Ticket Prefix Extraction using pandas:")
# Extract non-numeric prefix from tickets using pandas string methods
def extract_ticket_prefix_pandas(ticket_series):
    """Extract non-numeric prefix from ticket using pandas methods"""
    # Remove all digits and clean up using pandas string methods
    prefix_series = ticket_series.str.replace(r'\d+', '', regex=True).str.strip()
    prefix_series = prefix_series.str.replace(r'[./\s]', '', regex=True).str.strip()
    # Replace empty strings with 'NONE' using pandas where
    prefix_series = prefix_series.where(prefix_series != '', 'NONE')
    return prefix_series

titanic_df['Ticket_Prefix'] = extract_ticket_prefix_pandas(titanic_df['Ticket'])

print("✅ Ticket prefixes extracted using pandas!")
print("\n📋 Ticket prefix distribution:")
print(titanic_df['Ticket_Prefix'].value_counts().head(15))

# Extract numeric part using pandas methods
print("\n3. Ticket Number Extraction with pandas:")
# Extract the numeric part of tickets using pandas regex
numeric_pattern = r'(\d+)'
titanic_df['Ticket_Number'] = titanic_df['Ticket'].str.extract(numeric_pattern)
titanic_df['Ticket_Number'] = pd.to_numeric(titanic_df['Ticket_Number'], errors='coerce')

print("✅ Ticket numbers extracted using pandas!")
print(f"Ticket numbers extracted: {titanic_df['Ticket_Number'].notna().sum()}")

# Analyze ticket number ranges using pandas statistical methods
numeric_tickets = titanic_df['Ticket_Number'].dropna()
if len(numeric_tickets) > 0:
    print(f"Ticket number range: {numeric_tickets.min()} to {numeric_tickets.max()}")
    print(f"Median ticket number: {numeric_tickets.median()}")

# Ticket length analysis using pandas
print("\n4. Ticket Length Patterns using pandas:")
titanic_df['Ticket_Length'] = titanic_df['Ticket'].str.len()
print("Ticket length distribution:")
print(titanic_df['Ticket_Length'].value_counts().sort_index())



print("\n📊 6. Cabin Analysis and Feature Engineering with pandas-Only")

print("🎯 Extracting Hidden Information from Cabin Data")

# Analyze cabin patterns using pandas methods
print("\n1. Cabin Pattern Analysis:")
cabin_available = titanic_df['Cabin'].notna()
print(f"Passengers with cabin info: {cabin_available.sum()}")
print(f"Missing cabin info: {(~cabin_available).sum()}")

# Show sample cabins using pandas boolean indexing
sample_cabins = titanic_df[cabin_available]['Cabin'].head(15)
print("\nSample cabins:")
for i, cabin in enumerate(sample_cabins):
    print(f"{i+1:2d}. {cabin}")

print("\n2. Cabin Deck Extraction using pandas:")
# Extract first character (deck) from cabin using pandas string methods
titanic_df['Cabin_Deck'] = titanic_df['Cabin'].str[0]
# Fill missing cabin deck as 'Unknown' using pandas fillna
titanic_df['Cabin_Deck'] = titanic_df['Cabin_Deck'].fillna('Unknown')

print("✅ Cabin decks extracted using pandas!")
print("\n📋 Cabin deck distribution:")
print(titanic_df['Cabin_Deck'].value_counts())

# Binary indicator for cabin availability using pandas
titanic_df['Has_Cabin'] = cabin_available.astype(int)

print("\n3. Cabin Number Extraction using pandas:")
# Extract cabin numbers using pandas regex
cabin_number_pattern = r'([A-Z])(\d+)'
cabin_parts = titanic_df['Cabin'].str.extract(cabin_number_pattern)
cabin_parts.columns = ['Deck_Letter', 'Cabin_Number']

titanic_df['Cabin_Number'] = pd.to_numeric(cabin_parts['Cabin_Number'], errors='coerce')
print("✅ Cabin numbers extracted using pandas!")
cabin_numbers = titanic_df['Cabin_Number'].dropna()
if len(cabin_numbers) > 0:
    print(f"Cabin numbers available: {len(cabin_numbers)}")
    print(f"Cabin number range: {cabin_numbers.min()} to {cabin_numbers.max()}")

print("\n4. Multiple Cabin Analysis using pandas:")
# Some passengers have multiple cabins
titanic_df['Multiple_Cabins'] = titanic_df['Cabin'].str.contains(' ', na=False)
multiple_cabin_count = titanic_df['Multiple_Cabins'].sum()

print(f"Passengers with multiple cabins: {multiple_cabin_count}")

if multiple_cabin_count > 0:
    # Count number of cabins per passenger using pandas string methods
    titanic_df['Cabin_Count'] = titanic_df['Cabin'].str.count(' ') + 1
    # Set cabin count to 0 for missing cabins using pandas loc
    titanic_df.loc[titanic_df['Cabin_Count'].isna(), 'Cabin_Count'] = 0
    
    print("Cabin count distribution:")
    print(titanic_df['Cabin_Count'].value_counts().sort_index())
    
    print("\nExamples of multiple cabins:")
    multiple_examples = titanic_df[titanic_df['Multiple_Cabins']]['Cabin'].head(5)
    for cabin in multiple_examples:
        print(f"  • {cabin}")



print("\n📊 7. Family and Social Feature Engineering with pandas-Only")

print("🎯 Creating Features from Family and Social Patterns")

print("\n1. Family Size and Structure using pandas:")
# Build on existing SibSp and Parch using pandas arithmetic
titanic_df['Family_Size'] = titanic_df['SibSp'] + titanic_df['Parch'] + 1
titanic_df['Is_Alone'] = (titanic_df['Family_Size'] == 1).astype(int)

# Family size categories using pandas apply
def categorize_family_size(size):
    if size == 1:
        return 'Solo'
    elif size <= 4:
        return 'Small'  # 2-4 people
    else:
        return 'Large'  # 5+ people

titanic_df['Family_Size_Category'] = titanic_df['Family_Size'].apply(categorize_family_size)

print("✅ Family features created using pandas!")
print("\n📋 Family size distribution:")
print(titanic_df['Family_Size_Category'].value_counts())

print("\n2. Family Name Analysis using pandas:")
# Analyze families traveling together using pandas groupby
family_name_stats = titanic_df.groupby('Family_Name').agg({
    'PassengerId': 'count',
    'Survived': ['sum', 'mean'],
    'Fare': 'mean',
    'Pclass': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else x.iloc[0]
}).round(3)

# Flatten column names using pandas
family_name_stats.columns = ['Family_Count', 'Family_Survived', 'Family_Survival_Rate', 'Family_Avg_Fare', 'Family_Class']

print("✅ Family statistics calculated using pandas!")
print(f"Unique family names: {len(family_name_stats)}")

# Find largest families using pandas sorting
largest_families = family_name_stats[family_name_stats['Family_Count'] > 1].sort_values('Family_Count', ascending=False)
print("\n📋 Largest families:")
print(largest_families.head(10))

# Merge family statistics back to main dataset using pandas merge
titanic_df = titanic_df.merge(family_name_stats, left_on='Family_Name', right_index=True, how='left')

print("\n3. Title-Based Social Analysis using pandas:")
# Analyze survival by title groups using pandas groupby
title_survival = titanic_df.groupby('Title_Grouped').agg({
    'Survived': ['count', 'sum', 'mean'],
    'Age': 'mean',
    'Fare': 'mean'
}).round(3)

title_survival.columns = ['Title_Count', 'Title_Survived', 'Title_Survival_Rate', 'Title_Avg_Age', 'Title_Avg_Fare']

print("📋 Survival by title group:")
print(title_survival)

# Create title-based features using pandas map
title_survival_rates = titanic_df.groupby('Title_Grouped')['Survived'].mean()
titanic_df['Title_Survival_Rate'] = titanic_df['Title_Grouped'].map(title_survival_rates)

print("✅ Title-based features created using pandas!")



print("\n📊 8. Text-Based Numeric Features with pandas-Only")

print("🎯 Converting text patterns to numeric features, and creating safe interaction features without arithmetic on categoricals")

# 1) Name complexity features (pure pandas)
titanic_df['Name_Word_Count'] = titanic_df['Name'].str.split().str.len()
titanic_df['Name_Character_Count'] = titanic_df['Name'].str.len()
titanic_df['Name_Capital_Count'] = titanic_df['Name'].str.count('[A-Z]')
titanic_df['Name_Punctuation_Count'] = titanic_df['Name'].str.count('[.,\"]')

print("✅ Name complexity features created (word/char/capital/punct counts)")

# 2) Ticket-based features (pure pandas)
titanic_df['Ticket_Letter_Count'] = titanic_df['Ticket'].str.count('[A-Za-z]')
titanic_df['Ticket_Digit_Count'] = titanic_df['Ticket'].str.count(r'\d')

# Ticket sharing (same ticket number across multiple passengers)
ticket_sharing = titanic_df.groupby('Ticket').size()
titanic_df['Shared_Ticket_Count'] = titanic_df['Ticket'].map(ticket_sharing)
titanic_df['Has_Shared_Ticket'] = (titanic_df['Shared_Ticket_Count'] > 1).astype('int8')

print("✅ Ticket-based features created (letter/digit count, shared-ticket flags)")

# 3) Cabin-based numeric features (pure pandas)
# Map deck letters to numeric codes; keep Unknown as 0 for interpretability
deck_mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'T': 8, 'Unknown': 0}
titanic_df['Cabin_Deck_Numeric'] = titanic_df['Cabin_Deck'].map(deck_mapping).astype('int8')

print("✅ Cabin numeric features created (deck mapped to integers)")

# 4) Interaction features (safe arithmetic with categoricals)
# IMPORTANT: Pclass is categorical after Tuesday; cast to int for arithmetic, but do NOT permanently change Pclass
# Defensive: ensure Age is numeric (it should be after Monday’s imputation)
titanic_df['Age'] = pd.to_numeric(titanic_df['Age'], errors='coerce')

# Create a temporary numeric Series for Pclass strictly for math
pclass_num = titanic_df['Pclass'].astype('int16')  # leaves the original categorical intact

# Create core interactions
titanic_df['Fare_Per_Person'] = (titanic_df['Fare'] / titanic_df['Family_Size']).astype('float32')

# Avoid division by zero (Pclass should be 1–3, but guard anyway)
safe_pclass_divisor = pclass_num.replace(0, pd.NA)
titanic_df['Age_Class_Ratio'] = (titanic_df['Age'] / safe_pclass_divisor).astype('float32')

# Title × Class interaction as string combo (no arithmetic)
titanic_df['Title_Class_Interaction'] = titanic_df['Title_Grouped'].astype('string') + '_Class' + pclass_num.astype('string')

print("✅ Interaction features created (Fare_Per_Person, Age_Class_Ratio, Title_Class_Interaction)")

# 5) Quick quality checks (pure pandas)
complexity_stats = titanic_df[['Name_Word_Count', 'Name_Character_Count', 
                               'Name_Capital_Count', 'Name_Punctuation_Count']].describe()
print("\n📊 Name complexity statistics:")
print(complexity_stats)

shared_count = titanic_df['Has_Shared_Ticket'].sum()
print(f"\n🔎 Passengers sharing tickets: {shared_count}")

print("\n📋 Cabin deck mapping counts:")
for deck, num in deck_mapping.items():
    count = (titanic_df['Cabin_Deck'] == deck).sum()
    print(f"Deck {deck} → {num} ({count} passengers)")

# 6) Correlations with survival (only for sensible numeric features)
numeric_features = [
    'Name_Length', 'Name_Word_Count', 'Family_Size',
    'Ticket_Letter_Count', 'Cabin_Deck_Numeric', 'Fare_Per_Person', 'Age_Class_Ratio'
]
corr = titanic_df[numeric_features].corrwith(titanic_df['Survived'].astype('int8')).sort_values(key=abs, ascending=False)
print("\n📈 Feature correlations with survival (abs-sorted):")
print(corr.round(3))

print("\n✅ Lab 3.8 (Revised) complete: pure pandas, safe arithmetic with categoricals, and robust guards in place.")



"""
Session 3 Summary (Labs 1–8)
Pure pandas string processing & feature engineering
"""

import pandas as pd

def session3_summary():
    lines = []

    # Header
    lines.append("=== Session 3 Summary: Pure pandas String Processing & Feature Engineering ===")
    lines.append("Scope: Labs 1 → 8")
    lines.append("Goal: Create interpretable, pandas-only features from Names, Tickets, and Cabins,")
    lines.append("      plus safe interactions that respect categorical dtypes.\n")

    # Lab 1
    lines.append("1. Setup & .str basics")
    lines.append("- Loaded Titanic data, applied Monday imputation (Age by Pclass×Sex median; Embarked mode).")
    lines.append("- Applied Tuesday dtype optimizations (Pclass/Sex/Embarked as category; Survived as bool).")
    lines.append("- Introduced pandas .str: length, case transforms, uniqueness checks.\n")

    # Lab 2
    lines.append("2. Pattern detection")
    lines.append("- Used .str.contains/.startswith/.endswith to flag parentheses, quotes, title keywords.")
    lines.append("- Added word-count and vowel-start indicators to capture name structure nuances.\n")

    # Lab 3
    lines.append("3. Splitting & components")
    lines.append("- Split 'Lastname, Title Firstname' → Last_Name, First_Title via .str.split(expand=True).")
    lines.append("- Extracted Family_Name and Title_Raw for standardized downstream use.\n")

    # Lab 4
    lines.append("4. Regex extraction")
    lines.append("- .str.extract to get Title precisely; cleaned and grouped to Title_Grouped")
    lines.append("  (Mr/Mrs/Miss/Master/Officer/Royalty/Other).")
    lines.append("- Extracted First_Name with a dedicated regex capture group.\n")

    # Lab 5
    lines.append("5. Ticket analysis")
    lines.append("- Counted letters/digits, detected purely numeric tickets.")
    lines.append("- Extracted Ticket_Prefix (non-numeric) and Ticket_Number via regex + pd.to_numeric.")
    lines.append("- Built Shared_Ticket_Count and Has_Shared_Ticket for group booking signals.\n")

    # Lab 6
    lines.append("6. Cabin parsing")
    lines.append("- Parsed Cabin_Deck (first char) with Unknown fill; extracted Cabin_Number via regex.")
    lines.append("- Flags for Multiple_Cabins and Cabin_Count from space counts; Has_Cabin indicator.")
    lines.append("- Prepared numeric deck mapping for later use.\n")

    # Lab 7
    lines.append("7. Family & social features")
    lines.append("- Family_Size = SibSp + Parch + 1; Is_Alone; Family_Size_Category (Solo/Small/Large).")
    lines.append("- Family-level stats via groupby(Family_Name): counts, survival rate, avg fare, dominant class; merged back.")
    lines.append("- Title_Survival_Rate mapped from grouped means (for EDA, avoid in modeling to prevent leakage).\n")

    # Lab 8
    lines.append("8. Text-to-numeric & interactions (safe with categoricals)")
    lines.append("- Name complexity: Name_Word_Count, Name_Character_Count, Name_Capital_Count, Name_Punctuation_Count.")
    lines.append("- Ticket features: Ticket_Letter_Count, Ticket_Digit_Count, Shared_Ticket_Count, Has_Shared_Ticket.")
    lines.append("- Cabin_Deck_Numeric: mapped from Cabin_Deck (Unknown→0).")
    lines.append("- Interactions:")
    lines.append("  • Fare_Per_Person = Fare / Family_Size (float32).")
    lines.append("  • Age_Class_Ratio uses a temporary numeric cast of Pclass for division to avoid arithmetic on categoricals.")
    lines.append("  • Title_Class_Interaction is string-based (Title_Grouped + class).")
    lines.append("- Ran corrwith(Survived) on numeric features to prioritize signals.\n")

    # Safeguards
    lines.append("Key safeguards")
    lines.append("- Pure pandas methods: .str.*, .str.extract, .str.count, .str.split, .map, .astype, pd.to_numeric.")
    lines.append("- No arithmetic on categorical columns: cast Pclass to an integer Series temporarily for ratios.")
    lines.append("- Defensive conversions for Age; division guards for potential zero divisors.\n")

    # Deliverables
    lines.append("Deliverables (feature set)")
    lines.append("- Core components: Last_Name, First_Title, Title, Title_Grouped, First_Name, Family_Name.")
    lines.append("- Name complexity: Name_Word_Count, Name_Character_Count, Name_Capital_Count, Name_Punctuation_Count.")
    lines.append("- Ticket: Ticket_Prefix, Ticket_Number, Ticket_Letter_Count, Ticket_Digit_Count, Shared_Ticket_Count, Has_Shared_Ticket, Ticket_Is_Numeric.")
    lines.append("- Cabin: Cabin_Deck, Has_Cabin, Multiple_Cabins, Cabin_Count, Cabin_Deck_Numeric, Cabin_Number.")
    lines.append("- Family/social: Family_Size, Is_Alone, Family_Size_Category, Title_Survival_Rate (+ family stats merged).")
    lines.append("- Interactions: Fare_Per_Person, Age_Class_Ratio (safe), Title_Class_Interaction.\n")

    # What this enables
    lines.append("What this enables next")
    lines.append("- High-signal EDA slices by title, family, deck, and ticket patterns.")
    lines.append("- Quick prioritization by correlation to Survived for Week 12 visuals.")
    lines.append("- Reusable, pandas-only feature engineering scaffold for future tabular projects.\n")

    return "\n".join(lines)

if __name__ == "__main__":
    print(session3_summary())
