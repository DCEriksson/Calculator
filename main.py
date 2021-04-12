# MAIN FILE

def addition(*numbers):
    sumVar = sum(numbers)
    return sumVar

one = int(input("Enter a number: "))
two = int(input("Enter a number: "))
three = int(input("Enter a number: "))
print(addition(one, two, three))