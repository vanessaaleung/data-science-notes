# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"

    # TODO: create instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price * (1 - self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        # underscore: a hint this attribute is intended to be internal to the class, should not be accessed outside of the class 
        self._discount = amount

# TODO: create some book instances
b1 = Book("War and Peace", "Leo Telstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: print the price of book1
print(b1.getprice())

# TODO: try setting the discount
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())

# TODO: properties with double underscores are hidden by the interpreter
# prevent subclasses use the same name for attributes that's already used
print(b2.__secret)
# AttributeError: 'Book' object has no attribute '__secret'

# Add _CLASSNAME__ATTRNAME to use it
print(b2._Book__secret)
# This is a secret attribute