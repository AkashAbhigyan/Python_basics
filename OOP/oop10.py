class Movie:
    def __init__(self,title,director,rating):
        self.title = title
        self.director = director
        if 0 <= rating <= 10:
            self.rating = rating
        else:
            self.rating = 0
            print("Invalid rating!\n")

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Director: {self.director}")
        print(f"Rating: {self.rating}\n")

    def update_rating(self,new_rating):
        if 0 <= new_rating <= 10:
            self.rating = new_rating
        else:
            print("Invalid rating.")
            
movie1 = Movie("adfa","afdfrf",8)

movie1.display_details()
movie1.update_rating(9)
movie1.display_details()