#1 Take input from the user
num = int(input("Enter an integer: "))

# Check if the number is even or odd
if num % 2 == 0:
    print("Even")
else:
    print("Odd")




    #2 Ask for the user's age
age = int(input("Please enter your age: "))

# Check if the user is 18 or older
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")




#4 Take two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the two numbers and print the result
if num1 > num2:
    print("The first number is greater.")
elif num1 < num2:
    print("The second number is greater.")
else:
    print("Both numbers are equal.")





#5 Take user input for two numbers and an operator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

# Perform the operation based on the operator provided
if operator == "+":
    result = num1 + num2
    print(f"The result is: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"The result is: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"The result is: {result}")
elif operator == "/":
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"The result is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator! Please enter one of +, -, *, or /.")



#6 Ask for the year input from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")



#7 Take input from the user
num = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


#8 Take input from the user
day_number = int(input("Enter a number (1-7): "))

# Check and print the corresponding day of the week
if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print("Invalid day")

#9 Take three numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest number
if num1 >= num2 and num1 >= num3:
    print(f"The largest number is: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is: {num2}")
else:
    print(f"The largest number is: {num3}")




    #10 Function to determine the winner
def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == "rock" and player2_choice == "scissors") or \
         (player1_choice == "scissors" and player2_choice == "paper") or \
         (player1_choice == "paper" and player2_choice == "rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

# Take input from both players
player1_choice = input("Player 1, enter your choice (rock, paper, or scissors): ").lower()
player2_choice = input("Player 2, enter your choice (rock, paper, or scissors): ").lower()

# Validate the choices
if player1_choice not in ["rock", "paper", "scissors"] or player2_choice not in ["rock", "paper", "scissors"]:
    print("Invalid input! Please choose 'rock', 'paper', or 'scissors'.")
else:
    # Determine the winner and print the result
    result = determine_winner(player1_choice, player2_choice)
    print(result)
