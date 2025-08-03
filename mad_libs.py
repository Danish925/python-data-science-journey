# --- Mad Libs Generator ---
# This script asks the user for different types of words
# and then creates a silly story using those words.

print("--- Welcome to the Mad Libs Generator! ---")
print("Please provide the following words:")

# 1. Get all the words from the user
adjective = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb_past_tense = input("Enter a verb (past tense): ")
adverb = input("Enter an adverb: ")
noun2 = input("Enter another noun: ")
verb_ending_in_ing = input("Enter a verb ending in 'ing': ")

# 2. Create the story using an f-string
story = (f"Today, I went to the zoo. I saw a(n) {adjective} \n"
         f"{noun1} jumping up and down in its tree. "
         f"It {verb_past_tense} {adverb} through the large tunnel that led to its {noun2}. "
         f"I got some peanuts and passed them to the gigantic gorilla who was {verb_ending_in_ing} "
         f"in a small puddle.")

# 3. Display the final story
print("\n--- Here is your story! ---")
print(story)
