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
print()
car2.start_engine()
car2.details()
car2.stop_engine()
print()
car3.start_engine()
car3.details()
car3.stop_engine()
print()