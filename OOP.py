class Dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Woof")

class Owner:
    def __init__(self,name,address,contact_number):
        self.name = name
        self.address = address
        self.phone = contact_number

owner1 = Owner("Akash","Shivpuram",9102823628)
dog1 = Dog("Lucy","German Shepard",owner1)
dog1.bark()
print(dog1.name)
print(dog1.breed)
print(dog1.owner.name)

dog2 = Dog("Tom","Scottish Terrier",owner1)
dog2.bark()
print(dog2.name)
print(dog2.breed)
print(dog2.owner.address)

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
print("")      

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
print("")
student2.details()
student2.result_status()
print("")
student3.details()
student3.result_status()
print("")

class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def details(self):
        print(f"Brand:{self.brand}\nModel:{self.model}\nYear:{self.year}")

car1 = Car("Audi","S11",2011)
car2 = Car("Mercedez","A9",2009)
car3 = Car("Ferrari","N19",1996)

car1.details()
print("")
car2.details()
print("")
car3.details()
print("")
        
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def details(self):
        print(f"Title:{self.title}\nAuthor:{self.author}\nPrice:Rs.{self.price}")

    def discount(self):
        if self.price >= 350:
            print(f"{self.author} is on 10% discount")
        else:
            print(f"There is no discount on a {self.author}")


book1 = Book("The Alchemist","Paulo Coelho",300)
book2 = Book("Atomic Habits","James Clear",500)
book3 = Book("The Monk Who Sold His Ferrari","Robin Sharma",350)

book1.details()
book1.discount()
print("")
book2.details()
book2.discount()
print("")
book3.details()
book3.discount()
        