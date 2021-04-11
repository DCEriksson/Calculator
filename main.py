# MAIN FILE

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def additionMany(*numbers):
    sumVar = sum(numbers)
    return sumVar

one = int(input("Enter a number: "))
two = int(input("Enter a number: "))
three = int(input("Enter a number: "))
print(additionMany(one, two, three))

# numberOne = int(input("Put in a number: "))
# numberTwo = int(input("Put in a number: "))
# arithmetics = input("Write m for multiplication, a for addition or s for subtraction: ")
# if arithmetics == "m":
#     print(multiplication(numberOne, numberTwo))
# elif arithmetics == "a":
#     print(addition(numberOne, numberTwo))
# else:
#     print(subtraction(numberOne, numberTwo))