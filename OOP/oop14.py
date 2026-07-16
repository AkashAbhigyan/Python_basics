class Animal:
    def __init__(self,name):
        self.name = name
     
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")     

dog = Dog("Dog")
cat = Cat("Cat")

dog.speak()
cat.speak()   
    
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def start_engine(self):
        print(f"{self.brand} {self.model} engine started.")

class Bike(Vehicle):
    def ring_bell(self):
        print(f"{self.brand} {self.model} bell rings: Tring Tring!")

car = Car("Toyota", "Corolla")
bike = Bike("Hero", "Splendor")

car.start_engine()
bike.ring_bell()