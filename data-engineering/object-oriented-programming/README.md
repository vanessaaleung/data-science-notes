# Object-Oriented Programming
<p align="center">
  <img src="https://miro.medium.com/max/810/1*xiYI_rl-_pX_27BAjxBL3g.png" height="300px">
</p>

## Class Definition
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

## Instance methods and attributes
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

## Inheritance & Composition
<img src="https://miro.medium.com/max/749/0*J_Dm57bKTppN51oZ.png" height="200px">
