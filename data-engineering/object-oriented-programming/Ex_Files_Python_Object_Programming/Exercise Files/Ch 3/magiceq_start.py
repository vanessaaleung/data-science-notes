# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: the __eq__ method checks for equality between two objects
    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Book):
            raise ValueError("Can't compare book to a non-book")
        return (self.title == o.title and
        self.author == o.author and
        self.price == o.price)

    # TODO: the __ge__ establishes >= relationship with another obj
    def __ge__(self, o:object) -> bool:
        if not isinstance(o, Book):
            raise ValueError("Can't compare book to a non-book")
        
        return self.price >= o.price

    # TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, o:object) -> bool:
        if not isinstance(o, Book):
            raise ValueError("Can't compare book to a non-book")
        
        return self.price < o.price

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# TODO: Check for equality
# python doesn't do an attribute by attribute comparison, just see they're not the same instance in memory
# print(b1 == b3) # True
# print(b1 == b2) # False
# print(b1 == 42) # ValueError: Can't compare book to a non-book


# TODO: Check for greater and lesser value
print(b2 >= b1) # False
print(b2 < b1) # True

# TODO: Now we can sort them too
books = [b1, b3, b2, b4]
books.sort()
print([book.title for book in books]) # ['To Kill a Mockingbird', 'The Catcher in the Rye', 'War and Peace', 'War and Peace']