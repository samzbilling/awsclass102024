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
