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
print()
user1.email = "andy@gmail.com"
print("\n",user1.email)
print(user1.clean_email)
print(user1.get_email())

user1.set_email("andy@gmail.com")
print(user1.get_email())

user1.set_email("8213uhrbda")
print(user1.get_email())