#double underscore methods : dunder or magicmethods
"""
Dunder methods (short for "double underscore" methods) are special built-in methods in Python
that begin and end with two underscores. Also called magic methods,
They are called whenever we do a built in operation in python
"""

class Book:
    def __init__(self, name, author, pages): #for ex, this dunder method is triggered everytime we make an object
        self.name = name
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.name} by {self.author} of {self.pages} pages"
    
    def __eq__(self, other):
        return self.name == other.name and self.author == other.author
    
    def __lt__(self, other):
        return self.pages < other.pages
    
    def __gt__(self, other):
        return self.pages > other.pages

    def __add__(self, other):
        return self.pages + other.pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        else:
            return f"{key} not found"


book1 = Book("Cosmos", "Carl Sagan", 100)
book2 = Book("Cosmos", "Carl Sagan", 100)
book3 = Book("My Diary", "Me", 500)


print(book1) #if there was no __str__ method, this would return <__main__.Book object at 0x0000029A8BC64950>
print(book1['author']) #this calls the get item dunder method, we have modified it
print(book1 < book2) #returns false, as pages in book1 and 2 are same
print(book1 == book2) #returns true, as pages are same
print(book3 > book1) #returns true as book3 has more pages than book 1
print(book1 + book2) #returns total pages

"""All these operations wouldnt work on the objects we created if we had not modified the dunder methods that are being triggered"""