# --- Simple Quiz Game ---
# This project reinforces Week 2 concepts: if/elif/else and variables.

print("--- Welcome to the Simple Quiz Game! ---")

# 1. Initialize variables
# We need a variable to keep track of the player's score. It starts at 0.
score = 0
# We also use a variable to keep track of the current question number.
question_number = 1

# --- Question 1 ---
print(f"\nQuestion {question_number}: What is the capital of India?")
# Get the user's answer from the keyboard.
answer1 = input("Your answer: ")

# Check if the answer is correct. .lower() makes the check case-insensitive.
if answer1.lower() == "delhi":
    print("Correct! You've earned a point.")
    # If correct, increment the score. 'score += 1' is shorthand for 'score = score + 1'.
    score += 1 
else:
    print("Incorrect. The correct answer is Paris.")

# Increment the question number for the next question.
question_number += 1


# --- Question 2 ---
print(f"\nQuestion {question_number}: Which planet is known as the Red Planet?")
answer2 = input("Your answer: ")

if answer2.lower() == "mars":
    print("Correct! Excellent knowledge.")
    score += 1
else:
    print("Incorrect. The correct answer is Mars.")

question_number += 1


# --- Question 3 ---
print(f"\nQuestion {question_number}: What is 12 * 12?")
answer3 = input("Your answer: ")

# For numerical answers, we compare the string directly.
if answer3 == "144":
    print("Correct! You're a math whiz.")
    score += 1
else:
    print("Incorrect. The correct answer is 144.")

# question_number += 1


# --- Final Score ---
# After all questions are asked, display the final results.
print(f"\n--- Quiz Over! ---")
# We subtract 1 from question_number because it was incremented one last time after the final question.
# total_questions = question_number - 1
print(f"Your final score is {score} out of {question_number}.")

# Add a final message based on performance.
if score == question_number:
    print("Perfect score! You're a genius!")
elif score >= question_number / 2:
    print("Good job! You know your stuff.")
else:
    print("Better luck next time!")

