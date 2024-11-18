# 1. Odd or Even
# Write a Python program that takes an integer as input from the user and prints "Even" if 
# the number is even, and "Odd" if it is odd.

number = int(input("Enter a number: "))
if number % 2:
    print("Odd")
else:
    print("Even")

#2. Voting Eligibility
# Write a program that asks for a user's age. If the user is 18 or older, 
# print "You are eligible to vote." Otherwise, print "You are not eligible to vote yet."

age = int(input("Please enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print ("You are not eligible to vote yet.")

# 3. Number Comparison
# Write a program that takes two numbers as input and prints:
# "The first number is greater." if the first number is larger.
# "The second number is greater." if the second number is larger.
# "Both numbers are equal." if they are the same.
    
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
if num1 > num2:
    print("The first number is greater.")
elif num1 < num2:
    print("The second number is greater.")
elif num1 == num2:
    print("Both numbers are equal.")

# 5. Grade Calculator
# Create a program that asks for a student's score (0–100).
# If the score is 90 or above, print "A".
# If the score is between 80 and 89, print "B".
# If the score is between 70 and 79, print "C".
# If the score is between 60 and 69, print "D".
# If the score is below 60, print "F". 

score = int(input("Please enter the student's score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


