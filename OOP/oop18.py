class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age,roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display_details(self):
        print(f"Name: {self.name}\nAge: {self.age}\nRoll number: {self.roll_no}")

student = Student("Akash",19,6)
student.display_details()
print()

class Shape:
    def area(self):
        print("Area of shape: area")

class Rectangle(Shape):
    def __init__(self,length,breadth):
        super().__init__()
        self.length = length
        self.breadth = breadth
    def area(self):
        print(f"Area of rectangle: {self.length*self.breadth}")

class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius
    def area(self):
        print(f"Area of circle: {3.14*self.radius**2}")

Areas: list[Shape] = [Rectangle(3,2),Circle(3)]

for AREA in Areas:
    AREA.area()


class Employ:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}\nSalary: Rs.{self.salary}")
        
class Manager(Employ):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department

    def display_details(self):
        print(f"Manager's department: {self.department}")
        return super().display_details()
      
employ = Manager("Akash",32,"DOI")
employ.display_details()


    