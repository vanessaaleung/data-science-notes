# Object-Oriented Programming
<p align="center">
  <img src="https://miro.medium.com/max/810/1*xiYI_rl-_pX_27BAjxBL3g.png" height="300px">
</p>

- [Object-Oriented Python](#object-oriented-python)
- [Inheritance and Composition](#inheritance-and-composition)

## Object-Oriented Python
### Class Definition
```python
# create a basic class
class Book:
	# called before any functions in the class
	# self: just naming convention
	def __init__(self, title) -> None:
		self.title = title

# create instances of the class
# whenever you call a method of an object, the object itself gets automatically passed in
b1 = Book("Brave New World")
b2 = Book("War and Peace")

# print the class and property
print(b1)
print(b1.title)
```

### Instance methods and attributes
```python
class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"

    # create instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price * (1 - self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        # underscore: a hint this attribute is intended to be internal to the class, should not be accessed outside of the class 
        self._discount = amount

# create some book instances
b1 = Book("War and Peace", "Leo Telstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# print the price of book1
print(b1.getprice())

# try setting the discount
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())

# properties with double underscores are hidden by the interpreter
# prevent subclasses use the same name for attributes that's already used
print(b2.__secret)
# AttributeError: 'Book' object has no attribute '__secret'

# Add _CLASSNAME__ATTRNAME to use it
print(b2._Book__secret)
# This is a secret attribute
```

### Checking instance types
```python
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
```

### Class methods and members
```python
class Book:
    # Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # double-underscore properties are hidden from other classes
    __booklist = None

    # create a class method
    # class method works on the entire class
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # create a static method
    # don't modify the state of a class or an instance
    # usesful for name spacing + when you want to make a class callable and not have its state modified
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype

# access the class attribute
print("Book types: ", Book.getbooktypes())

# Create some book instances
b1 = Book("Title 1", "HARDCOVER")
# b2 = Book("Title 2", "COMIC")
# ValueError: COMIC is not a valid book type

b2 = Book("Title 2", "PAPERBACK")

# Use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)
```

## Inheritance and Composition
<img src="https://miro.medium.com/max/749/0*J_Dm57bKTppN51oZ.png" height="200px">

### Inheritance
```python
class Publication:
    def __init__(self, title, price) -> None:
        self.title = title
        self.price = price

class Periodical(Publication):
    def __init__(self, title, price, period, publisher) -> None:
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
```

### Abstract base classes
- You want to provide a base class that defines a template for other classes to inherit from, but you don't want the consumer of the base class to be able to create instance of the base class itself, you want subclasses to provide concrete implementation
- There are certain classes in the base class that subclasses have to implement
- Useful for enforcing a set of constraints among the consumers of your classes

```python
# Using Abstract Base Classes to enforce class constraints
from abc import ABC, abstractmethod

# ABC: Abstract Base Class
class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    # want to enforce every shape implement the calcArea function
    # want to prevent the GraphicShape class itself from being instantiated on its own
    @abstractmethod
    # tells there's no implementation in the base class, and each subclass has to override this method
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side

# g = GraphicShape()
# TypeError: Can't instantiate abstract class GraphicShape with abstract methods calcArea

c = Circle(10)
# TypeError: Can't instantiate abstract class Circle with abstract methods calcArea
print(c.calcArea())
s = Square(12)
print(s.calcArea())
```

### Using multiple inheritance
- useful for interface

```python
class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"

# Python use method resolution order to look the attribute up in the class
# in the order in which they are defined from left to right
class C(A, B):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)
    
c = C()
c.showprops()
# foo
# bar
# Class A
print(C.__mro__) # inspect the method resolution order
```
