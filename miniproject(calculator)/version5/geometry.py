def area_circle(r):
    if r > 0:
        return 3.14 * r**2
    else:
        print("Invalid radius.")
        return None


def area_rectangle(l, b):
    if l > 0 and b > 0:
        return l * b
    else:
        print("Invalid length and/or breadth.")
        return None


while True:
    print("===== Simple Area Calculator =====")
    print()
    print("1. Area of circle.")
    print("2. Area of rectangle.")
    print("3. Quit")

    try:
        choice = int(input("Enter your choice (1-3): "))
        print()

        if choice == 3:
            print("Thank you for using the calculator!")
            break

        elif choice == 1:
            radius = float(input("Radius: "))
            area = area_circle(radius)

            if area is not None:
                print("Area of the circle:", area)

        elif choice == 2:
            length = float(input("Length: "))
            breadth = float(input("Breadth: "))
            area = area_rectangle(length, breadth)

            if area is not None:
                print("Area of the rectangle:", area)

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


    



