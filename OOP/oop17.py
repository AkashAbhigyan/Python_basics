'''class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

class Bike:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

Vehicles = [Car("Ford","Mustang",2013),Bike("Honda","ads",2006)]

for vehicle in Vehicles:
    if isinstance(vehicle,Car):
        print(f"Type: {type(vehicle).__name__}\nBrand: {vehicle.brand}\nModel: {vehicle.model}\nYear: {vehicle.year}\n")
    elif isinstance(vehicle,Bike):
        print(f"Type: {type(vehicle).__name__}\nBrand: {vehicle.brand}\nModel: {vehicle.model}\nYear: {vehicle.year}")
    else:
        print("Invalid vehicle.")
       

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

    def start(self):
        print("Car starting")

    def stop(self):
        print("Car stopping")

class Bike(Vehicle):
    def __init__(self,brand,model,year,fueltype,no_of_wheels):
        super().__init__(brand,model,year)
        self.fueltype = fueltype
        self.no_of_wheels = no_of_wheels

    def start(self):
        print("Bike starting")

    def stop(self):
        print("Bike stopping")

Vehicles = [Car("Ford","Mustang",2013,"Diesel",4),Bike("Honda","civic",2015,"Petrol",2)]

for vehicle in Vehicles:
    if isinstance(vehicle,Car):
        print(f"Type: {type(vehicle).__name__}\nBrand: {vehicle.brand}\nModel: {vehicle.model}\nYear: {vehicle.year}\nFuel type: {vehicle.fueltype}\nNumber of wheels: {vehicle.no_of_wheels}")
        vehicle.start()
        vehicle.stop()
        print()
    if isinstance(vehicle,Bike):
        print(f"Type: {type(vehicle).__name__}\nBrand: {vehicle.brand}\nModel: {vehicle.model}\nYear: {vehicle.year}\nFuel type: {vehicle.fueltype}\nNumber of wheels: {vehicle.no_of_wheels}")
        vehicle.start()
        vehicle.stop()'''


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

    def start(self):
        print("Car starting")

    def stop(self):
        print("Car stopping")

class Bike(Vehicle):
    def __init__(self,brand,model,year,fueltype,no_of_wheels):
        super().__init__(brand,model,year)
        self.fueltype = fueltype
        self.no_of_wheels = no_of_wheels

    def start(self):
        print("Bike starting")

    def stop(self):
        print("Bike stopping")

class Aeroplane(Vehicle):
    def __init__(self,brand,model,year,fueltype,no_of_wheels):
        super().__init__(brand,model,year)
        self.fueltype = fueltype
        self.no_of_wheels = no_of_wheels

    def start(self):
        print("Plane starting")

    def stop(self):
        print("Plane stopping")

Vehicles: list[Vehicle] = [Car("Ford","Mustang",2013,"Diesel",4),Bike("Honda","civic",2015,"Petrol",2),Aeroplane("Boeing","707",2022,"Kerosine",8)]

for vehicle in Vehicles:
    print(f"Type: {type(vehicle).__name__}\nBrand: {vehicle.brand}\nModel: {vehicle.model}\nYear: {vehicle.year}\nFuel type: {vehicle.fueltype}\nNumber of wheels: {vehicle.no_of_wheels}")
    vehicle.start()
    vehicle.stop()
    print()