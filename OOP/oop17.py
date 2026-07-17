class Car:
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
       