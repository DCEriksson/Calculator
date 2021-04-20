class Calculator:

    def addition(self, num1, num2):
        # return self.num1 + self.num2
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2
    
    def division(self, num1, num2):
        return float(num1 / num2)

total = 0
i = 0
arithmetic = Calculator()
while True:
    if i == 0:
        num1 = int(input("Enter a number: "))
        inputAri = input("+, -, * or /: ")
        num2 = int(input("Enter a number: "))
        if inputAri == '+':
            total = arithmetic.addition(num1, num2)
        elif inputAri == '-':
            total = arithmetic.subtract(num1, num2)
        elif inputAri == '*':
            total = arithmetic.multiplication(num1, num2)
        elif inputAri == '/':
            total = arithmetic.division(num1, num2)
    else:
        inputAri = input("+, -, *, / or enter to calculate: ")
        if inputAri == '':
            print(total)
            break
        inputVal = int(input("Enter a number: "))
        if inputAri == '+':
            total = arithmetic.addition(total, inputVal)
        elif inputAri == '-':
            total = arithmetic.subtract(total, inputVal)
        elif inputAri == '*':
            total = arithmetic.multiplication(total, inputVal)  
        elif inputAri == '/':
            total = arithmetic.division(total, inputVal)
    i += 1