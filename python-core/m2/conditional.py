print("checking")

# conditional statements
# elif = else if in java and javascript

a = 20
b = 10

if a<b:
    print("a is less than b")
if b<a:
    print("b is less than a")
else:
    print(a+b)



match_result = input("Enter the match result: ")

match match_result:
    case "win":
        print("You won the match")
    case "lose":
        print("You lost the match")
    case "draw":
        print("The match was a draw")
    case _:
        print("Invalid match result")