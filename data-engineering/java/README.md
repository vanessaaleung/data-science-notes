- Main()
- Java new Keyword
- Capture User Input
- [Non-Static vs Static](#non-static-vs-static)
- [Encapsulation](#encapsulation)
- [Inheritance](#inheritance)
- [Polymorphism](#polymorphism)

### - Main()
![image](https://user-images.githubusercontent.com/24954551/163208415-bc145071-8dcc-4aa5-924c-87d337237c97.png)

- **main**: tell the compiler it's the starting point of the program
- **public**: access specifier, can be invoked from outside of the class
- **void**: return type, doesn't return anything, does not make sense for the main method to return anything
- **static**: keyword, can be invoked without instantiating the class
- **String[] args**: stores Java command-line arguments


### Java new Keyword
```java 
NewExample obj=new NewExample();
```
- It is used to create the object.
- It allocates the memory at runtime.
- It invokes the object constructor.

<img src="https://user-images.githubusercontent.com/24954551/163467845-0ab2853a-96b6-45b5-9833-c9cd4b76c630.png" height="300px" />


### Capture User Input
- `.next()` is used to get the user input
```java 
Scanner in = new Scanner(System.in);
String name = in.next();
```

### Cast Integer to String
```java
int myVariable = 5;
String myString = Integer.toString(myVariable);
```

### Non-Static vs Static
- Non-static member: a part of a class that's accessible with an instance and belongs to that instance. You'll need to create an instance to access an non-static members. In the below example, you'll need to create a Tree to access the `heightFt` and `trunkDiameterInches` attributes. Also called instance member.
```java
public class Tree {
  double heightFt;
  double trunkDiameterInches;
}
```
- Static member: a part of a class that's accessible through the class and belongs to that class. Behavior that's not based on a particular instance, instead it belongs to all instances.
```java
public class Tree {
  static Color TRUNK_COLOR = new Color(102, 51, 0);
}
...
System.out.println(Tree.TRUNK_COLOR);
```
```java
public class Tree{
  static void announceTree() {
    System.out.println("Look out for that " + TRUNK_COLOR + " tree!");
}
```

### Encapsulation
- Combine data and code acting on that data
- Bind state and behavior together into a single unit
- We need a clear interface between a class and the rest of the program
- Everything can't have direct access - Makek a class's attributes ihdden from other classes - More secure and less error-prone with less code change
- Access modifiers
  - determine where certain variables and methods can be accessed in the code
  - private: only visible in the class
  - public: visible everywhere
  - no modifier: visible in the package
  - protected: visible to the package and all subclasses
- write public methods to access private attributes

## Inheritance
```java
public class Employee {
  private String name;
  private Integer age;
  protected double salary;
}

public class Salesperson extends Employee {
  public Salesperson(String name, double salary, int age) {
    super(name, salary, age); // refers to the superclass's constructor
  }
  
  public double getAnnualBonus() {
    return super.salary * .05;
  }
}
```

### Polymorphism
- runtime and compile-time polymorphism
- reduce complexity and write reusable code
- able to overwrite methods
