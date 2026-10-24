"""
Practice: user input and conditional statements

Solve each problem using input() and if/elif/else. Convert input to int
where a problem asks for a number. Do not use loops or functions yet.
"""

# Problem 1: Personalized greeting
# Ask the user for their name, then print:
#     Hello, <name>!
# Replace <name> with the value they entered.
name = input("Enter your name: ")
print("Hello, ,{name}!")


# Problem 2: Voting eligibility
# Ask the user for their age as a whole number.
# Print "You can vote" if the age is 18 or older; otherwise print
# "You are not old enough to vote".
age = int(input("Enter your age: "))
if(age>=18):
    print("You can vote")
else:
    print("You are not old enough to vote")


# Problem 3: Number checker
# Ask the user for a whole number.
# Print whether it is "positive", "negative", or "zero".

number = int(input("Enter a number: "))
if(number > 0):
    print("Positive")
elif (number<0):
    print("Negative")
else:
    print("zero")


# Problem 4: Compare two numbers
# Ask the user for two whole numbers.
# Print which number is larger, or print "The numbers are equal" if they
# have the same value.

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
if(num1>num2):
    print(num1, " is greater")
elif(num2>num1):
    print(num2, " is greater")
else:
    print("Numbers are equal")


# Problem 5: Match result
# Ask the user to enter a match result: win, lose, or draw.
# Print a different message for each of those three results. For any other
# input, print "Invalid match result".

result=input("Enter the match result: ")

match result:
    case "win":
        print("win")
    case "lose":
        print("lose")
    case "draw":
        print("draw")
    case _:
        print("Invalid match result")