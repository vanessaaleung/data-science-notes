# Python Object Oriented Programming by Joe Marini course example
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
