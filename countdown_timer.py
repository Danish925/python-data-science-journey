# --- Simple Countdown Timer ---
# A bonus project to reinforce core Python skills like loops, functions, and error handling.
# This project also introduces the built-in 'time' module.

# 1. Import necessary modules
# 'time' is a built-in Python module that provides various time-related functions.
# We need it specifically for the 'sleep()' function to pause our program.
import time

# ---- FUNCTION DEFINITION ----
# We place the core logic into a function to keep our code organized and reusable.
def countdown(seconds):
    """
    Counts down from a given number of seconds, printing the time remaining each second.

    Args:
        seconds (int): The total number of seconds to count down from.
    """
    
    # 2. The main countdown loop
    # This 'while' loop will continue to run as long as the 'seconds' variable is greater than 0.
    # When 'seconds' becomes 0, the loop's condition will be false, and it will stop.
    while seconds > 0:
        
        # 3. Display the remaining time
        # We use an f-string to create a clean output message.
        # The 'end='\r'' argument is a special instruction for the print function.
        # '\r' (Carriage Return) tells the cursor to go back to the start of the current line
        # instead of moving to a new line. This creates a "live update" effect.
        print(f"Time remaining: {seconds} second(s)", end='\r')
        
        # 4. Pause the execution
        # time.sleep(1) is the core of the timer. It tells the program to pause
        # everything it's doing for exactly 1 second.
        time.sleep(1)
        
        # 5. Decrement the counter
        # This is shorthand for 'seconds = seconds - 1'. It subtracts 1 from the
        # 'seconds' variable in each iteration of the loop.
        seconds -= 1
        
    # 6. Final message
    # This line runs only after the 'while' loop has finished.
    # The extra spaces at the end ensure that the previous "Time remaining..." line
    # is completely overwritten, leaving a clean final message.
    print("Time's up!                   ")

# --- MAIN PROGRAM EXECUTION BLOCK ---
# This standard Python convention ensures that the code inside this block
# only runs when the script is executed directly by the user.
if __name__ == "__main__":
    
    print("--- Welcome to the Simple Countdown Timer! ---")
    
    # 7. Get valid user input
    # We use a 'while True' loop to keep asking the user for input until they provide a valid number.
    while True:
        try:
            # Ask the user for the countdown duration.
            user_input = input("Enter the countdown time in seconds: ")
            # Try to convert the user's string input into an integer.
            # If the user enters text like "hello", this will raise a ValueError.
            duration = int(user_input)
            
            # We also check if the number is positive, as a negative countdown isn't logical.
            if duration > 0:
                break # If the input is a valid positive number, we exit the loop.
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            # This block of code runs ONLY if the 'int()' conversion failed.
            print("Invalid input. Please enter a whole number.")
            
    # 8. Start the countdown
    # After successfully getting a valid duration from the user, we call our
    # 'countdown' function and pass the user's number to it to start the timer.
    countdown(duration)

