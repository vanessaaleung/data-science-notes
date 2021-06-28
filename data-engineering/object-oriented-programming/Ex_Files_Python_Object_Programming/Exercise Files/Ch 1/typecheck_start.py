# Python Object Oriented Programming by Joe Marini course example
# Checking class types and instances


class Book:
    def __init__(self, title):
        self.title = title


class Newspaper:
    def __init__(self, name):
        self.name = name


# Create some instances of the classes
b1 = Book("The Catcher In The Rye")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")

# use type() to inspect the object type
print(type(b1))
# <class '__main__.Book'>
print(type(n1))
# <class '__main__.Newspaper'>

# compare two types together
print(type(b1) == type(b2)) # True
print(type(b1) == type(n2)) # False

# use isinstance to compare a specific instance to a known type
print(isinstance(b1, Book)) # True
print(isinstance(b1, Newspaper)) # False
print(isinstance(n1, Newspaper)) # True
print(isinstance(n2, object)) # True, in Python every thing is a subclass of the object class