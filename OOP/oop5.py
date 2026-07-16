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
print()
book2.details()
book2.discount()
print()
book3.details()
book3.discount()
print()