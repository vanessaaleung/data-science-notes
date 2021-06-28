# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
	# called before any functions in the class
	# self: just naming convention
	def __init__(self, title) -> None:
		self.title = title

# TODO: create instances of the class
# whenever call a method of an object, the object itself gets automatically passed in
b1 = Book("Brave New World")
b2 = Book("War and Peace")

# TODO: print the class and property
print(b1)
print(b1.title)


