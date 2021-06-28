# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces

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