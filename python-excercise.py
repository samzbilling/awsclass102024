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

# 4. Simple Calculator
    # Write a program that asks the user to input two numbers and an operator (+, -, *, /). Based on 
    # the operator provided, calculate and print the result. Make sure to handle division by zero.




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

# 6. Leap Year Checker
    # Write a program that checks if a given year is a leap year. A leap year is divisible 
    # by 4 but not by 100, except when it is also divisible by 400.

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 7. Positive, Negative, or Zero
    # Write a program that takes a number as input and prints "Positive" if the number is greater than 
    # zero, "Negative" if it is less than zero, and "Zero" if it is exactly zero.
    
number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


#8. Day of the Week
    #Write a program that takes an integer (1 to 7) from the user and prints the corresponding day 
    #of the week (1 = Monday, 2 = Tuesday, etc.). If the number is not between 1 and 7, print "Invalid day".


#9. Largest of Three Numbers
    #Write a program that takes three numbers as input and prints the largest of the three. Make sure to 
    #handle cases where two or more numbers are equal.


#10. Rock, Paper, Scissors Game
    #Write a simple two-player Rock, Paper, Scissors game. Both players input their choice, 
    #and the program determines the winner (Rock beats Scissors, Scissors beats Paper, Paper beats Rock).


