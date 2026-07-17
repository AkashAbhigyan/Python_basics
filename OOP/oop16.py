class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Engine starting")

    def stop(self):
        print("Engine stopping")

class Car(Vehicle):
    def __init__(self,brand,model,year,fueltype,no_of_wheels):
        super().__init__(brand,model,year)
        self.fueltype = fueltype
        self.no_of_wheels = no_of_wheels

class Bike(Vehicle):
    def __init__(self,brand,model,year,fueltype,no_of_wheels):
        super().__init__(brand,model,year)
        self.fueltype = fueltype
        self.no_of_wheels = no_of_wheels

car = Car("Ford","Mustang",2013,"Diesel",4)
bike = Bike("Honda","civic",2015,"Petrol",2)

print(car.__dict__)
print(bike.__dict__)
