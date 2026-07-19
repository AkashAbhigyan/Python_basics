def celsius_to_fahrenheit(c):
    f = c*1.8+32
    return f

def km_to_miles(k):
    if k >= 0:
        m = 1.60934*k
        return m
    else:
        print("Invalid length.")
        return None

while True:
    print("===== Simple Converter =====")
    print()
    print("1. Celcius to Fahrenheit.")
    print("2. Kilometer to Mile.")
    print("3. Quit")  

    try:
        choice = int(input("Enter your choice (1-3): "))
        print()

        if choice == 3:
            print("Thank you for using the calculator!")
            break

        elif choice == 1:
            celcius = float(input("Celcius Temperature: "))
            fahrenheit = celsius_to_fahrenheit(celcius)

            if fahrenheit is not None:
                print("Fahrenheit Temperature",fahrenheit)

        elif choice == 2:
            length = float(input("Length in kilometer: "))
            mile = km_to_miles(length)

            if mile is not None:
                print("Area of the rectangle:", mile)

        else:
            print("Error: Invalid choice. Please select a valid option.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    continue_calculation = input(
        "Do you want to perform another calculation? (y/n): ")

    if continue_calculation.lower() != "y":
        print("Thank you for using the calculator!")
        break





