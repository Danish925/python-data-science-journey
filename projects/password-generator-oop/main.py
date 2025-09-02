# --- Powerful Password Generator ---
# Project for Week 4: Functions and Code Organization

# 1. Import necessary modules
# 'random' is used for choosing characters randomly and shuffling the final password.
# 'string' provides convenient pre-made strings of character sets (e.g., lowercase letters, numbers).
import random
import string

# ---- FUNCTION DEFINITION ----
# We define the main "worker" function here. It is organized to be separate from the user interface code.
def generate_password(length, include_uppercase, include_numbers, include_symbols):
    """
    Generates a secure, random password based on user-specified criteria.

    Args:
        length (int): The desired length of the password.
        include_uppercase (bool): Whether to include uppercase letters.
        include_numbers (bool): Whether to include numbers.
        include_symbols (bool): Whether to include symbols.

    Returns:
        str: The generated password string.
    """
    
    # 2. Build the pool of available characters
    # Start with lowercase letters, which we will make mandatory.
    character_pool = string.ascii_lowercase
    
    # Add other character types to the pool based on the True/False arguments passed to the function.
    if include_uppercase:
        character_pool += string.ascii_uppercase # Adds "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if include_numbers:
        character_pool += string.digits         # Adds "0123456789"
    if include_symbols:
        character_pool += string.punctuation    # Adds "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        
    # 3. Generate the password from the character pool
    # We build the password in a list first, as it's easy to add to and shuffle.
    password_list = []
    
    # This loop runs for the number of times specified by 'length'.
    # We use '_' as the variable name because we don't need to use the loop counter itself.
    for _ in range(length):
        # random.choice() picks one single random character from our pool string.
        random_char = random.choice(character_pool)
        # We add (append) the chosen character to our list.
        password_list.append(random_char)
    
    # 4. Shuffle the password list to make it more secure and less predictable.
    # This ensures characters are not grouped by type (e.g., all letters first, then numbers).
    random.shuffle(password_list)
    
    # 5. Join the list of characters back into a single string and return it.
    # "".join(list) is the most efficient and standard way to convert a list of characters into a string.
    return "".join(password_list)


# --- MAIN PROGRAM EXECUTION BLOCK ---
# This is a standard Python convention. The code inside this 'if' statement
# will only run when the script is executed directly (e.g., 'python password_generator.py').
# It will NOT run if the script is imported as a module into another file.
if __name__ == "__main__":
    
    print("--- Welcome to the Powerful Password Generator! ---")

    # --- Get Password Length from User ---
    # Use a 'while True' loop for input validation. It will keep asking until valid input is given.
    while True:
        try:
            # Ask the user for a length and try to convert it to an integer.
            pwd_length = int(input("Enter the desired password length (e.g., 12): "))
            # Check if the number is positive.
            if pwd_length > 0:
                break # If valid, exit the loop.
            else:
                print("Please enter a positive number.")
        except ValueError:
            # This runs if int() fails because the user entered text instead of a number.
            print("Invalid input. Please enter a number.")

    # --- Get Character Type Preferences from User ---
    # For each option, we get the user's 'yes' or 'no' input, convert it to lowercase,
    # and then perform a comparison '== 'yes''. The result of this comparison is a
    # boolean value (True or False), which is stored directly in the variable.
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    # --- Generate the password by calling our function ---
    # We pass the user's choices as arguments to our 'generate_password' function.
    # The string that the function returns is stored in the 'final_password' variable.
    final_password = generate_password(pwd_length, use_uppercase, use_numbers, use_symbols)

    # --- Print the Final Result ---
    print("\n***--- Your Generated Password is: ---***")
    print(final_password)
    print("---------------------------------")
