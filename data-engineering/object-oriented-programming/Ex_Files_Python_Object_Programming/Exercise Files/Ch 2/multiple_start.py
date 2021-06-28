# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


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
