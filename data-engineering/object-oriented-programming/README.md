# Object-Oriented Programming
<p align="center">
  <img src="https://miro.medium.com/max/810/1*xiYI_rl-_pX_27BAjxBL3g.png" height="300px">
</p>

- [Object-Oriented Python](#object-oriented-python)
- [Inheritance and Composition](#inheritance-and-composition)
- [Magic Object Methods](#magic-object-methods)
- [Data Classes](#data-classes)

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

### Interfaces
- use combination of multiple inheritance and abstract base class to implementation
- like a promise to provide a certain kind of behavior or capability
```python
from abc import ABC, abstractmethod

# create a small focused class that another class can use to indicate that it knows how to represent itself in JSON
class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

# requires Circle class to override the toJSON abstract class
class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius
    
    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):
        return f"{{\"Circle\" : {str(self.calcArea())}}}"

c = Circle(10)
# TypeError: Can't instantiate abstract class Circle with abstract methods toJSON

print(c.calcArea())
print(c.toJSON())
# {"Circle" : 314.0}
```

### Understanding composition
- Make a monolithic class more extensible and flexible by composing it from simpler class objects, each is responsible for its own features and data
```python
class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result

class Author:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname
    
    def __str__(self) -> str:
        return f"{self.fname} {self.lname}"

class Chapter:
    def __init__(self, name, pagecount) -> None:
        self.name = name
        self.pagecount = pagecount

auth = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, auth)

b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))

print(b1.title)
print(b1.author)
print(b1.getbookpagecount())
```

## Magic Object Methods
- Automatically associate with any class definition
- classes can overwrite the methods to customize object behavior
- Control access to attribute values for get and set
- Built in comparison and equality testing capabilities
- Allow objects to be called like functions - make codes more consise and readable

### Contents
- [String Representation](#string-representation)
- [Equality and Comparison](#equality-and-comparison)
- [Attribute Access](#attribute-access)
- [Callable Objects](#callable-objects)

### String Representation
- The `__str__` function is used to return a user-friendly stringrepresentation of the object. Usually intended to display to user
- The `__repr__` method to used to generate developer-facing strings. Can be used to re-create the object of the current stsate. Used for debugging. Useful when you need an exact representation of the object during development and debugging tasks.

```python
class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # use the __str__ method to return a string
    def __str__(self) -> str:
        return f"{self.title} by {self.author}, costs {self.price}"

    # use the __repr__ method to return an obj representation
    def __repr__(self) -> str:
        return f"title={self.title},author={self.author},price={self.price}"

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

print(b1)
print(b2)
print(str(b1))
print(repr(b2))
```

### Equality and Comparison
- By default, Python doesn't do an attribute by attribute comparison, it just check they're not the same instance in memory

```python
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
```

### Attribute Access
- `__getattr__` called when `__getattribute__` lookup fails in situations like attribute doesn't exist, `__getattribute__` doesn't exist, `__getattribute__` raises an error

```python3
from typing import Any

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    # The __str__ function is used to return a user-friendly string
    # representation of the object
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: __getattribute__ called when an attr is retrieved. Don't
    # directly access the attr name otherwise a recursive loop is created
    def __getattribute__(self, name: str) -> Any:
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(name)

    # TODO: __setattr__ called when an attribute value is set. Don't set the attr
    # directly here otherwise a recursive loop causes a crash
    def __setattr__(self, name: str, value: Any) -> None:
        if name == "price":
            if type(value) is not float:
                raise ValueError("The price attr must be a float")
        return super().__setattr__(name, value)

    # TODO: __getattr__ called when __getattribute__ lookup fails - you can
    # pretty much generate attributes on the fly with this method
    def __getattr__(self, name) -> Any:
        return name + " is not here!"

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

b1.price = 38.95
print(b1) # War and Peace by Leo Tolstoy, costs 35.055

# b2.price = 40
# print(b2) # ValueError: The price attr must be a float

b2.price = float(40)
print(b2) # The Catcher in the Rye by JD Salinger, costs 36.0

print(b1.randomprop) # randomprop is not here!
```

### Callable Objects
- `__call__` method can be used to call the object like a function. Beneficial when the object will be modified frequently. Results in more compact codes.

```python
from typing import Any

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: the __call__ method can be used to call the object like a function
    def __call__(self, title, author, price) -> Any:
        self.title = title
        self.author = author
        self.price = price

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

# TODO: call the object as if it were a function
print(b1)
# War and Peace by Leo Tolstoy, costs 39.95
b1("Anna Karenina", "Leo Tolstoy", 49.95)
print(b1)
# Anna Karenina by Leo Tolstoy, costs 49.95
```

## Data Classes
- [Defining a Data Class](#defining-a-data-class)
- [Using Post Initialization](#using-post-initialization)
- [Using Default Values](#using-default-values)
- [Immutable Data Classes](#immutable-data-classes)

### Defining a Data Class
- the `@dataclass` decorator will re-write the class to automatically add the init function and the attributes will be initialized. It also automatically implements `__repr__` and `__eq__`
```python
from dataclasses import dataclass

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
```

### Using Post Initialization
- the `__post_init__` function lets us customize additional properties after the object has been initialized via built-in `__init__`
- add additional attributes that might depends on the values of other attributes when using dataclasses

```python
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    # TODO: the __post_init__ function lets us customize additional properties
    # after the object has been initialized via built-in __init__
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"


# create some Book objects
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: use the description attribute
print(b1.description) # War and Peace by Leo Tolstoy, 1225 pages
print(b2.description) # The Catcher in the Rye by JD Salinger, 234 pages
```

### Using Default Values
- Multiple ways
  - Specify directly
    `price: float = 10.0`
  - Use the field function
    `price: float = field(default=10.0)`
  - Call a function that can generate values dynamically
    `price: float = field(default_factory=price_func)`
- Default values have to come first, can't have non-default values following default values

```python
from dataclasses import dataclass, field
import random

def price_func() -> float:
    return float(random.randrange(20, 40))

@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    # price: float = 10.0
    # price: float # TypeError: non-default argument 'price' follows default argument
    # price: float = field(default=10.0)
    price: float = field(default_factory=price_func)

# b1 = Book()
# print(b1) # Book(title='No Title', author='No Author', pages=0, price=10.0)

b1 = Book("War and Peace", "Leo Tolstoy", 1225)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234)
print (b1) # Book(title='War and Peace', author='Leo Tolstoy', pages=1225, price=10.0)
print(b2) # Book(title='The Catcher in the Rye', author='JD Salinger', pages=234, price=10.0)

# Book(title='War and Peace', author='Leo Tolstoy', pages=1225, price=31.0)
# Book(title='The Catcher in the Rye', author='JD Salinger', pages=234, price=23.0)
```

### Immutable Data Classes
