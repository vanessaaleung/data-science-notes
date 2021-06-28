# Python Object Oriented Programming by Joe Marini course example
# Using data classes to represent data objects
from dataclasses import dataclass

# the decorator will re-write the class to automatically add the init function and the attributes will be initialized
# also automatically implement __repr__ and __eq__
@dataclass
class Book:
    # type isn't actually enforced
    title : str
    author : str
    pages : int
    price : float

    def bookinfo(self):
        return f"{self.title}, by {self.author}"

# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

# access fields
print(b1.title)  # War and Peace
print(b2.author) # JD Salinger

# TODO: print the book itself - dataclasses implement __repr__
print(b1) # Book(title='War and Peace', author='Leo Tolstoy', pages=1225, price=39.95)

# TODO: comparing two dataclasses - they implement __eq__
print(b1 == b3) # True

# TODO: change some fields
b1.title = "Anna Karenina"
b1.pages = 864
print(b1.bookinfo()) # Anna Karenina, by Leo Tolstoy