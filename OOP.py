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

owner1 = Owner("Akash","Shivpuram","9102823628")
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




        
    