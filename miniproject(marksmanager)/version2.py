student = {}

print("===== STUDENT RECORD MANAGER =====")

while True:
    print("\nChoose an option(1,2,3,4,5,6 or 7)")
    print("1. Add student record")
    print("2. View student record")
    print("3. Search student record")
    print("4. Update marks")
    print("5. Average marks")
    print("6. Highest marks")
    print("7. Lowest marks")
    print("8. Delete student record")
    print("9. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 9:
        print("Thank you for using the manager")
        break

    elif choice == 1:
        name = input("Enter student name:")
        marks = float(input("Enter marks(Marks must be between 0 and 100.): "))
        if name in student:
            print(f"Record for {name} already exists. Use update option to change marks.")
        elif 0 <= marks <= 100:
            student[name] = marks
            print(f"Record for {name} has been added.")
        else:
            print("Invalid marks. Please enter marks between 0 and 100.")

    elif choice == 2:
        if not student:
            print("The student record is empty.")
        else:
            for name, marks in student.items():
                print(f"Student: {name}, Marks: {marks}")

    elif choice == 3:
        search_name = input("Enter the student name to search: ")
        if search_name in student:
            print(f"Student: {search_name}, Marks: {student[search_name]}")
        else:
            print(f"No record found for {search_name}.")

    elif choice == 4:
        update_name = input("Enter the student name to update marks: ")
        if update_name in student:
            new_marks = float(input("Enter new marks(Marks must be between 0 and 100.): "))
            if 0 <= new_marks <= 100:
                student[update_name] = new_marks
                print(f"Marks for {update_name} have been updated.")
            else:
                print("Invalid marks. Please enter marks between 0 and 100.")
        else:
            print(f"No record found for {update_name}.")

    elif choice == 5:
        if not student:
            print("The student record is empty.")
        else:
            average_marks = sum(student.values()) / len(student)
            print(f"The average marks is: {average_marks}")

    elif choice == 6:
        if not student:
            print("The student record is empty.")
        else:
            highest_student = max(student, key=student.get)
            print(f"The highest marks is: {student[highest_student]} by {highest_student}")

    elif choice == 7:
        if not student:
            print("The student record is empty.")
        else:
            lowest_student = min(student, key=student.get)
            print(f"The lowest marks is: {student[lowest_student]} by {lowest_student}")

    elif choice == 8: 
        delete_name = input("Enter the student name to delete record: ")
        if delete_name in student:
            del student[delete_name]
            print(f"Record for {delete_name} has been deleted.")
        else:
            print(f"No record found for {delete_name}.")

    else:
        print("Invalid choice. Please choose a valid option.")

    repeat = input("Do you want to perform another operation? (y/n): ")
    if repeat.lower() != 'y':
        print("Thank you for using the manager")
        break