# --- Dice Rolling Simulator ---
# This project reinforces Week 2 concepts: while loops and the random module.

# Import the 'random' module to allow us to generate random numbers.
import random

print("--- Welcome to the Dice Rolling Simulator! ---")

# This 'while True' loop will run forever until the user decides to quit.
while True:
    # Ask the user for their choice. .lower() converts their input to lowercase
    # so that "YES", "Yes", and "yes" are all treated the same.
    choice = input("Do you want to roll the die? (yes/no): ")

    # We use an if/elif/else block to handle the user's input.
    if choice.lower() == "yes":
        # This is the new part! We generate a random integer between 1 and 6.
        # As we discussed, random.randint() includes both endpoints.
        dice_roll = random.randint(1, 6)
        
        # We print the result to the user in a formatted string.
        print(f"\n>>> You rolled a {dice_roll}! <<<\n")
        
    elif choice.lower() == "no":
        # If the user says 'no', we print a goodbye message.
        print("Thanks for playing. Goodbye!")
        # The 'break' command stops the 'while' loop and ends the program.
        break
        
    else:
        # This handles any input that isn't 'yes' or 'no'.
        print("Invalid input. Please type 'yes' or 'no'.")

