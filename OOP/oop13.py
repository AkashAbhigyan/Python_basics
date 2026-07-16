class Student:
    student_count = 0
    def __init__(self,name):
        self.name = name
        Student.student_count += 1

    @classmethod
    def total_students(cls):
        return cls.student_count

    @staticmethod
    def is_pass_mark(mark):
        return mark >= 27
    

student1 = Student("Akash")
student2 = Student("Astha")
Student3 = Student("adsfg")
Student4 = Student("jhdfvjh")

print(f"Total students: {Student.total_students()}")
print(Student.is_pass_mark(43))
