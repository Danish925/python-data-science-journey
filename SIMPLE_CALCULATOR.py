# Define function to add two numbers
def add(x, y):
    return x + y

# Define function to subtract two numbers
def subtract(x, y):
    return x - y

# Define function to multiply two numbers
def multiply(x, y):
    return x * y

# Define function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."  # Handle division by zero
    return x / y

print("Simple Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take user input for the operation choice
choice = input("Enter choice (1/2/3/4): ")

try:
    # Take user input for the numbers and convert them to floats
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter a number.")  # Handle invalid number input
    exit()

# Perform calculation based on user choice and display the result
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input. Please select 1, 2, 3, or 4.")  # Handle invalid operation choice
