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

