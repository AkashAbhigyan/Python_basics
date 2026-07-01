'''#V1
in1 = float(input("Enter the first number: "))
in2 = float(input("Enter the second number: "))
operator = input("Enter the operator: ")

if operator == '+':
    print(in1 + in2)
elif operator == '-':
    print(in1 - in2)
elif operator == '*':
    print(in1 * in2)
elif operator == '/':
    if in2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(in1 / in2)
else:
    print("Error: Invalid operator. Please use +, -, *, or /.")


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
    print(result)'''


#V3
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")


if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
else:
    result = "Error: Invalid operator. Please use +, -, *, or /."

print("Result:", result)