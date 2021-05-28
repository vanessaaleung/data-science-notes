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

## Inheritance & Composition
<img src="https://miro.medium.com/max/749/0*J_Dm57bKTppN51oZ.png" height="200px">
