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
    print(result)


#V3
print("===== Simple Calculator =====")

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

print("Thank you for using the calculator!")'''


#V4

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

    print("===== Simple Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter the operator (1, 2, 3, 4) or '5' to exit: ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
    
    elif choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        print("Result:", result)

    else:
        print("Error: Invalid choice. Please select a valid operator (1, 2, 3, 4) or '5' to exit.")

    continue_choice = input("Do you want to perform another calculation? (yes/no): ")