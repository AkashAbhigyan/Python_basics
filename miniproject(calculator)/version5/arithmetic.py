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

while True:
    print("===== Simple Arithmetic Calculator =====")

    print()

    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Quit")

    print()
    
    choice = input("Enter your choice (1-5): ")

    print()

    if choice == '5':
        print("Thank you for using the Arithmetic Calculator!")
        break

    elif choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print()
    
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
        print("Error: Invalid choice. Please select a valid option.")
    
    print()

    continue_calculation = input("Do you want to perform another arithmetic calculation? (y/n): ")
    if continue_calculation.lower() != 'y':
        print("Thank you for using the arithmetic calculator!")
        break