import random # This module lets us make random choices

# 1. Setup the game
print("--- Let's Play Rock, Paper, Scissors! ---")
options = ["rock", "paper", "scissors"] # A list of possible choices

# 2. Get choices from player and computer
user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
computer_choice = random.choice(options) # The computer picks a random item from the list

# 3. Display the choices
print(f"\nYou chose: {user_choice}")
print(f"The computer chose: {computer_choice}\n")

# 4. Determine the winner using if/elif/else logic
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "scissors" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "rock"):
    print("You win!")
else:
    # If it's not a tie and the user didn't win, the computer must have won.
    # We also add a check to ensure the user entered a valid option.
    if user_choice in options:
        print("You lose!")
    else:
        print("Invalid choice. You must choose rock, paper, or scissors.")

