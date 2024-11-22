# CLASSWORK

# 1. Odd or Even
# Write a Python program that takes an integer as input from the user and prints "Even" if the number is even, and "Odd" if it is odd.

x = int(input("Please enter a number: "))
if x%2 == 0:
    print('Even')
else:
    print('Odd')
    
#    ................................................................................................

# 2. Voting Eligibility
# Write a program that asks for a user's age. If the user is 18 or older, print "You are eligible to vote." Otherwise, print "You are not eligible to vote yet."
y = int(input("What is your age: "))
if y >= 18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote yet.')


#    ................................................................................................

# 3. Number Comparison
# Write a program that takes two numbers as input and prints:
# "The first number is greater." if the first number is larger.
# "The second number is greater." if the second number is larger.
# "Both numbers are equal." if they are the same.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print('First number is greater!')
elif b > a:
    print('Second nunber is greater!')
else:
    print('both numbers are equal!')

#    ................................................................................................

# 4. Simple Calculator
# Write a program that asks the user to input two numbers and an operator (+, -, *, /). Based on the operator provided, calculate and print the result. Make sure to handle division by zero.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
Operator = input("Enter Operator (+, -, *, /): ")

if Operator == "+":
    print (a + b)
elif Operator == "-":
    print (a - b)
elif Operator == "*":
    print (a * b)
elif Operator == "/" and b !=0:
    print (a/b)
else: print ("Enter number different than Zero!")

#    ................................................................................................

# 5. Grade Calculator
# Create a program that asks for a student's score (0–100).
# If the score is 90 or above, print "A".
# If the score is between 80 and 89, print "B".
# If the score is between 70 and 79, print "C".
# If the score is between 60 and 69, print "D".
# If the score is below 60, print "F".

Score = int(input("Enter Student's Score: "))

if Score >= 90:
    print('A')
elif Score >= 80:
    print('B')
elif Score >= 70:
    print('C')
elif Score >= 60:
    print('D')
else:
    print('F')
    
#    ................................................................................................

# 6. Leap Year Checker
# Write a program that checks if a given year is a leap year. A leap year is divisible by 4 but not by 100, except when it is also divisible by 400.

Year = int(input("Please enter year: "))

if (Year %4 == 0 and Year %100 !=0) or Year %400 ==0:
    print('Leap Year')
else:
    print('NOT Leap Year')

#    ................................................................................................

# 7. Positive, Negative, or Zero
# Write a program that takes a number as input and prints "Positive" if the number is greater than zero, "Negative" if it is less than zero, and "Zero" if it is exactly zero.

Num = int(input('Please Enter Number: '))

if Num > 0:
    print('Positive')
elif Num < 0:
    print('Negative')
else:
    print('Zero')

#    ................................................................................................

# 8. Day of the Week
# Write a program that takes an integer (1 to 7) from the user and prints the corresponding day of the week (1 = Monday, 2 = Tuesday, etc.). If the number is not between 1 and 7, print "Invalid day".

Day = int(input('Please Enter number 1 to 7: '))

if Day == 1:
    print('Monday')
elif Day == 2:
    print('Tuesday')
elif Day == 3:
    print('Wednesday')
elif Day == 4:
    print('Thursday')
elif Day == 5:
    print('Friday')
elif Day == 6:
    print('Saturday')
elif Day == 7:
    print('Sudnay')
else:
    print('Invalid day!')

#    ................................................................................................

# 9. Largest of Three Numbers
# Write a program that takes three numbers as input and prints the largest of the three. Make sure to handle cases where two or more numbers are equal.

Num1 = float(input('Please Enter First number: '))
Num2 = float(input('Please Enter Second number: '))
Num3 = float(input('Please Enter Third number: '))
        
if Num1 >= Num2 and Num1 >= Num3:
    print(f'Largest Numberr is {Num1}')
elif Num2 >= Num1 and Num2 >= Num3:
    print(f'Largest Number is {Num2}')
else:
    print(f'Largest Number is {Num3}')

#    ................................................................................................

# 10. Rock, Paper, Scissors Game
# Write a simple two-player Rock, Paper, Scissors game. Both players input their choice, and the program determines the winner (Rock beats Scissors, Scissors beats Paper, Paper beats Rock).

Player1 = input('PLAYER 1: Enter Rock, Paper, or Scissors: ')
Player2 = input('PLAYER 2: Enter Rock, Paper, or Scissors: ')

if Player1 == Player2:
    print('No Winner!')

elif Player1 == 'Rock':
    if Player2 == 'Scissors':
        print('PLAYER 1 is the Winner!')
    elif Player2 == 'Paper':
        print('PLAYER 2 is the Winner!')

elif Player1 == 'Paper':
    if Player2 == 'Rock':
        print('PLAYER 1 is the Winner!')
    elif Player2 == 'Scissors':
        print('PLAYER 2 is the Winner!')
        
elif Player1 == 'Scissors':
    if Player2 == 'Paper':
        print('PLAYER 1 is the Winner!')
    elif Player2 == 'Rock':
        print('PLAYER 2 is the Winner!')
        
else:
    print('Invalid Input!')

#    ................................................................................................
