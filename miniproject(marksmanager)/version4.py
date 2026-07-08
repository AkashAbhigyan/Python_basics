while True:
    print("1. Enter student details:")
    print("2. View students details")
    print("3. Search for student.")
    print("4. Exit:")

    try:
        choice = int(input("Enter choice:"))
        if choice == 1:
            student = input("Enter student name:")
            try:
                duplicate_found = False
                with open(r'D:\Learning\Github\simple.txt', "r") as file:
                    for line in file:
                        if student.capitalize() == line.split(":")[0]:
                            duplicate_found = True
                            break
                    if duplicate_found:
                        print("Student already exists.")
                    else:
                        while True:
                            marks = int(input("Enter marks:"))
                            if 0<= marks <=100:
                                with open(r'D:\Learning\Github\simple.txt', "a") as file:
                                    file.write(f"{student.capitalize()}:{marks}\n")
                                    print("Marks added successfully.")
                                    break
                            else:
                                print("Invalid marks. Try again")
                    
            except ValueError:
                print("Invalid marks.")

        elif choice == 2:
            with open('D:\Learning\Github\simple.txt', "r") as file:
                print(file.read())

        elif choice == 3:
            student = input("Enter student name:")
            student_found = False
            with open(r'D:\Learning\Github\simple.txt', "r") as file:
                for line in file:
                    if student.capitalize() == line.split(":")[0]:
                        student_found = True
                        break
                else:
                    print("Student record not found.")
                    break
                print(line.strip())
                    
        elif choice == 4:
            print("Thank you:")
            break

    except ValueError:
        print("Invalid choice.")
    
    repeat = input("Do you want to perform another task? (y/n): ")
    if repeat.lower() != 'y':
        print("Thank you.")
        break