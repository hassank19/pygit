#aggregation: 2 Independent classes exist: It represents a HAS-A relationship, theyre linked but not interdependent, ex: A library has books
class Library:
    def __init__(self, name):
        self.name = name
        self.books = [] #we dont need to mention the list books[] in the parameters of init since its not smth the user would pass, its just declared here

    def add_book(self, new_book):
        self.books.append(new_book)

    def show_list(self):
        return [f"{x.title} by {x.author}" for x in self.books]


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

my_library = Library("Personal Reads")
    
book1 = Book("Cosmos", "Carl Sagan")
book2 = Book("Science of Intersteller", "Kip Thorne")
book3 = Book("Bible", "Jesus")

my_library = Library("Personal Reads")

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

print(f"---{my_library.name}---")

for x in my_library.show_list():
    print(x)