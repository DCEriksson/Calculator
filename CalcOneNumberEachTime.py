class Calculator:

    @staticmethod
    def addition(num1, num2):
        return num1 + num2

    @staticmethod
    def subtract(num1, num2):
        return num1 - num2

    @staticmethod
    def multiplication(num1, num2):
        return num1 * num2
    
    @staticmethod
    def division(num1, num2):
        return float(num1 / num2)

total = 0
i = 0
while True:
    if i == 0:
        num1 = int(input("Enter a number: "))
        inputAri = input("+, -, * or /: ")
        num2 = int(input("Enter a number: "))
        if inputAri == '+':
            total = Calculator.addition(num1, num2)
        elif inputAri == '-':
            total = Calculator.subtract(num1, num2)
        elif inputAri == '*':
            total = Calculator.multiplication(num1, num2)
        elif inputAri == '/':
            total = Calculator.division(num1, num2)
    else:
        inputAri = input("+, -, *, / or enter to calculate: ")
        if inputAri == '':
            print(total)
            break
        inputVal = int(input("Enter a number: "))
        if inputAri == '+':
            total = Calculator.addition(total, inputVal)
        elif inputAri == '-':
            total = Calculator.subtract(total, inputVal)
        elif inputAri == '*':
            total = Calculator.multiplication(total, inputVal)  
        elif inputAri == '/':
            total = Calculator.division(total, inputVal)
    i += 1