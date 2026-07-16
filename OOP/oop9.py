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