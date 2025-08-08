# --- Number Guessing Game ---
# This is the project for Week 2, focusing on Control Flow and Loops.

# 1. Import the 'random' module
# We need this module to generate a random number for the player to guess.
import random

def simple_guessing_game():
    """
    This function contains all the logic for our number guessing game.
    Wrapping the game in a function is good practice for organizing code.
    """
    
    # 2. Set up the game's initial state
    # Use random.randint() to pick a secret integer between 1 and 100 (inclusive).
    secret_number = random.randint(1, 100)
    
    # Initialize a counter to keep track of how many guesses the player has made.
    attempts = 0
    
    # Print a welcome message and instructions for the player.
    print("--- Simple Number Guessing Game ---")
    print("I'm thinking of a number between 1 and 100.")

    # 3. Start the main game loop
    # 'while True:' creates an infinite loop that will keep running until we
    # explicitly use the 'break' keyword to exit it.
    while True:
        # Use a 'try...except' block to handle potential user errors gracefully.
        try:
            # Prompt the player for their guess and store it as a string.
            guess_str = input("Enter your guess: ")
            # Convert the player's string input into an integer.
            # A ValueError will occur here if the input is not a number (e.g., "hello").
            guess = int(guess_str)
            
            # Increment the attempt counter after a valid guess has been made.
            # 'attempts += 1' is a shorthand for 'attempts = attempts + 1'.
            attempts += 1
            
            # 4. Check the guess against the secret number
            # This is the core logic of the game, using an if/elif/else block.
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                # This 'else' block runs only if the guess is not lower or higher,
                # meaning the player has guessed correctly.
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} tries.")
                # The 'break' keyword exits the 'while' loop, ending the game.
                break
                
        except ValueError:
            # This block of code runs ONLY if the int() conversion in the 'try' block fails.
            # It prevents the program from crashing and gives the user a helpful message.
            print("Invalid input. Please enter a number.")

# 5. Run the game
# This line calls the function we defined, which starts the game.
# Without this line, the code would be defined but never executed.
simple_guessing_game()
