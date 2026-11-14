a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

try:
    result = a/b
    print("result: ", int(result),result)
except Exception as error:
    print("Divison error")
    print("Error is: ",error)
