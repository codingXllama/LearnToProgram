# This calculator only that does 4 operations .... R.I.P :(

def NoobOperations(num1, operation, num2):
    if operation == "+":
        print("{} + {} = {}".format(num1, num2, num1 + num2))
    elif operation == "-":
        print("{} - {}= {}".format(num1, num2, num1 - num2))
    elif operation == "*":
        print("{} * {} = {}".format(num1, num2, num1 * num2))
    elif operation == "/":
        print("{} / {} = {}".format(num1, num2, num1, num1 / num2))
    else:
        print("Invalid Operation , please use one of the following operations (+,-,*,/)")


# UserPrompt
for i in range(1):
    print("_ _ _" * 6)
print(
    "Welcome to the Noob Calculator!\nWe currently can only computer 2 numbers with the following operations (+,-,*,/)")
for i in range(1):
    print("_ _ _" * 6)

# Getitng userInput
num1, operation, num2 = input("Enter an expression to calculate: ").split()
# Changing the string input numbers to type int numebers
num1 = int(num1)
num2 = int(num2)

NoobOperations(num1, operation, num2)
