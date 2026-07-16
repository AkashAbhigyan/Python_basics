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