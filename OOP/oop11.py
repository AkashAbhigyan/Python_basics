class Student:
    student_count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.student_count += 1

    def display_details(self):
        print(f"Student's name: {self.name}")
        print(f"Student's age: {self.age}")

student1 = Student("Akash",19)
student2 = Student("Astha",25)
student1.display_details()
print()
student2.display_details()
print()
print(f"Number of students: {Student.student_count}")