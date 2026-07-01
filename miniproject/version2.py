#V2
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
c=input("Enter the operator: ")

def add(a, b):
        return a + b
result = add(a, b)
if c == '+':
    print(result)

def subtract(a, b):
        return a - b
result = subtract(a, b)
if c == '-':
    print(result)

def multiply(a, b):
        return a * b
result = multiply(a, b)
if c == '*':
    print(result)

def divide(a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        else:
            return a / b
result = divide(a, b)
if c == '/':
    print(result)