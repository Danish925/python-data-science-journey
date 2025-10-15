# --- User Profile Creator ---
# This script collects basic user information and displays it back to them.

print("--- Welcome to the User Profile Creator! ---")
print("Please enter your details below.")

# 1. Get user input and store it in variables
name = input("What is your name? ")
age = input("What is your age? ")
city = input("What city do you live in? ")

# 2. Display the collected information in a formatted summary
print("\n----------********************----------")
print("Thank you! Your profile has been created:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Location: {city}")
print("----------********************----------")
