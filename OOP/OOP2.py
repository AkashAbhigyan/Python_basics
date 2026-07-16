class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello I am {self.name} and I am {self.age} years old")

person1 = Person("Akash",19)
print("Name:",person1.name)
print("Age:",person1.age)
person1.greet()  
print()