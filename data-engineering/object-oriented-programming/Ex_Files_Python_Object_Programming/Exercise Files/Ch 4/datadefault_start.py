# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

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


