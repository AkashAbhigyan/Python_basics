print("===== Student Marks Manager =====")

student_list=[]

while True:
    print("\nChoose an option(1,2,3,4,5,6 or 7)")
    print("1. Add marks")
    print("2. View marks")
    print("3. Highest marks")
    print("4. Lowest marks")
    print("5. Average marks")
    print("6. Total students")
    print("7. Grade distribution")
    print("8. Quit")


    choice = int(input("Enter your choice: "))
    
    if choice == 8:
        print("Thank you for using the manager")
        break

    elif choice == 1:
        marks = float(input("Enter marks(Marks must be between 0 and 100.): "))
        if 0 <= marks <= 100:
            student_list.append(marks)
            print("Marks have been added to the list.")
        else:
            print("Invalid marks. Please enter marks between 0 and 100.")

    elif choice == 2:
        if not student_list:
            print("The marks list is empty.")
        else:
            for index, marks in enumerate(student_list,start=1):
                print("Student", index, ":", marks)

    elif choice == 3:
        if not student_list:
            print("The marks list is empty.")
        else:
            print("The maximum marks is: ", max(student_list))

    elif choice == 4:
        if not student_list:
            print("The marks list is empty.")
        else:
            print("The minimum marks is: ", min(student_list))

    elif choice == 5:
        if not student_list:
            print("The marks list is empty.")
        else:
            average_marks = sum(student_list) / len(student_list)
            print("The average marks is: ", average_marks)

    elif choice == 6:
        if not student_list:
            print("The marks list is empty.")
        else:
            print("The total number of students is: ", len(student_list))

    elif choice == 7:
        if not student_list:
            print("The marks list is empty.")
        
        else:
            Acount = 0
            Bcount = 0
            Ccount = 0
            Dcount = 0
            Fcount = 0
            for marks in student_list:
                if marks >= 80:
                    Acount += 1
                elif marks >= 70 and marks < 80:
                    Bcount += 1
                elif marks >= 60 and marks < 70:
                    Ccount += 1
                elif marks >= 50 and marks < 60:
                    Dcount += 1
                else:
                    Fcount += 1

            print("Grade distribution:")
            print("Grade A: ", Acount)
            print("Grade B: ", Bcount)
            print("Grade C: ", Ccount)
            print("Grade D: ", Dcount)
            print("Grade F: ", Fcount)

    else:
        print("Choose valid option")

    repeat = input("Do you want to perform another operation? (y/n): ")
    if repeat.lower() != "y":
        print("Thank you for using the manager")
        break