class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def details(self):
        print(f"Student name:{self.name}\nStudent age:{self.age}\nStudent marks:{self.marks}")
    def result_status(self):
        if self.marks >=27:
            print(f"{self.name} has Passed")
        else:
            print(f"{self.name} has Failed")
        

student1 = Student("Akash",19,12)
student2 = Student("Astha",25,99)
student3 = Student("Nutan",50,97)


student1.details()
student1.result_status()
print()
student2.details()
student2.result_status()
print()
student3.details()
student3.result_status()
print()