while True:
    print("===== Simple Calculator =====")
    print()
    print("1. Arithmetic Calculator")
    print("2. Simple Converter")
    print("3. Area Calculator")
    print("4. Quit")

    try:
        choice = int(input("Enter your choice (1-3): "))
        print()

        if choice == 4:
            print("Thank you for using the calculator!")
            break

        elif choice == 1:
            import arithmetic


        elif choice == 2:
            import conversion

        elif choice == 3:
            import geometry

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