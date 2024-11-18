# 1. Odd or Even
# Write a Python program that takes an integer as input from the user and prints "Even" if the number is even, and "Odd" if it is odd.

x = int(input("Enter a number: "))

# Checking even or odd
if x % 2 == 0:
    print("Even number")
else:
    print("Odd number")

    

# 2. Voting Eligibility
# Write a program that asks for a user's age. If the user is 18 or older, print "You are eligible to vote." Otherwise, print "You are not eligible to vote yet."

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# 3. Number Comparison
# Write a program that takes two numbers as input and prints:
# "The first number is greater." if the first number is larger.
# "The second number is greater." if the second number is larger.
# "Both numbers are equal." if they are the same.

# Provide two numbers 
a = int(input("Enter first number: "))
b = int(input("Enter second number to compare: "))

# Comparing the two numbers
if a > b:
    print("The first number is greater.")
elif a < b:
    print("The second number is greater.")
else:
    print("Both numbers are equal.")
