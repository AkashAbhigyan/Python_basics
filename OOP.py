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

    def start_engine(self):
        print(f"The {self.brand} {self.model} engine has started.")

    def stop_engine(self):
        print(f"The {self.brand} {self.model} engine has stopped.")

car1 = Car("Audi","S11",2011)
car2 = Car("Mercedez","A9",2009)
car3 = Car("Ferrari","N19",1996)

car1.start_engine()
car1.details()
car1.stop_engine()
print("")
car2.start_engine()
car2.details()
car2.stop_engine()
print("")
car3.start_engine()
car3.details()
car3.stop_engine()
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
print("")
        
from datetime import datetime

class User:
    def __init__(self,name,email,password):
        self.name = name
        self._email = email #_makes the data protected, __makes the data private
        self.password = password

    def say_high_to_user(self,user):
        print(f"{self.name} says high to {user.name}")

    def clean_email(self):
        return self._email.lower().strip()
    
    def get_email(self):
        print(f"Email accessed at {datetime.now()} ")
        return self._email

    def set_email(self,new_email):
        if "@gmail.com" in new_email:
            self._email = new_email
        else:
            print("Invalid Email.")
        
user1 = User("Andy","and@gmail.com  ","yvdg2132")
user2 = User("Margot","margo@gmail.com","32jefn2")

user1.say_high_to_user(user2)
print("")
user1.email = "andy@gmail.com"
print("\n",user1.email)
print(user1.clean_email)
print(user1.get_email())

user1.set_email("andy@gmail.com")
print(user1.get_email())

user1.set_email("8213uhrbda")
print(user1.get_email())

class User:
    def __init__(self,name,email,password):
        self.name = name
        self._email = email
        self.password = password

    @property
    def email(self):
        print("Email accessed")
        return self._email
    
    @email.setter
    def email(self,new_email):
        if "@" in new_email:
            self._email = new_email
        else:
            print("Invalid email.")
    
user3 = User("Akash","slsdj@gmail.com","1234kfnh")
user3.email = "ancie3@.ac"
print(user3.email)

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
student1.age = 20
student1.details()
print("")

class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit_money(self, deposit_amount):
        if deposit_amount > 0:
            self.__balance += deposit_amount
            print(f"Rs.{deposit_amount} deposited successfully.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw_money(self, withdraw_amount):
        if withdraw_amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif withdraw_amount > self.__balance:
            print("Insufficient balance.\n")
        else:
            self.__balance -= withdraw_amount
            print(f"Rs.{withdraw_amount} withdrawn successfully.")

    def display_balance(self):
        print(f"Current Balance: Rs.{self.__balance}")

    @property
    def balance(self):
        return self.__balance

account = BankAccount("Akash",2134)

account.display_balance()
print("")
account.deposit_money(23)
account.display_balance()
print("")
account.withdraw_money(32)
account.display_balance()
print("")
print(f"Remaining balance: Rs.{account.balance}\n")

class LibraryBook:
    def __init__(self,title,author,availablecopies,totalcopies):
        self.title = title
        self.author = author
        self.availablecopies = availablecopies
        self.totalcopies = totalcopies

    def borrow_book(self,borrow_quantity):
        if 1 <= borrow_quantity <= self.availablecopies:
            print(f"No. of books borrowed: {borrow_quantity}")
            print("Books borrowed successfully.")
            self.availablecopies -= borrow_quantity
        else:
            print("Invalid quantity.")

    def return_book(self,return_quantity):
            if return_quantity <= self.totalcopies and self.availablecopies <= self.totalcopies:
                print(f"No. of books returned: {return_quantity}")
                print("Books returned successfully.")
                self.availablecopies += return_quantity   
            else:
                print("Invalid quantity.")
    def display_copies(self):
        print(f"Number of books available: {self.availablecopies}")

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Total copies: {self.totalcopies}")
        print(f"Available copies: {self.availablecopies}")

book = LibraryBook("The Alchemist","Paulo Coelho",300,543)

book.display_details()
print()
book.borrow_book(89)
print()
book.display_copies()
print()
book.return_book(56)
print()
book.display_copies()

class Movie:
    def __init__(self,title,director,rating):
        self.title = title
        self.director = director
        if 0 <= rating <= 10:
            self.rating = rating
        else:
            self.rating = 0
            print("Invalid rating!\n")

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Director: {self.director}")
        print(f"Rating: {self.rating}\n")

    def update_rating(self,new_rating):
        if 0 <= new_rating <= 10:
            self.rating = new_rating
        else:
            print("Invalid rating.")
            
movie1 = Movie("adfa","afdfrf",8)

movie1.display_details()
movie1.update_rating(9)
movie1.display_details()

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

