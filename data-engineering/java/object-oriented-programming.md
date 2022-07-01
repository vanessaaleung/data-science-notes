# Java Object-oriented Programming
[Link to the class](#https://www.linkedin.com/learning/java-object-oriented-programming-2/")

- [Non-Static vs Static](#non-static-vs-static)
- [Encapsulation](#encapsulation)
- [Inheritance](#inheritance)
- [Polymorphism](#polymorphism)
- [Abstraction](#abstraction)

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
```java
public class ConditionArrayList extends ArrayList<Integer> {
  ...
  @Override
  public void add(int index, Integer element) {
    ...
  }
}
```
- Compile time Polymorphism - can have more than one methods with the same name. Enable multiple ways to create objects with different sets of input
```java
public class ConditionArrayList extends ArrayList<Integer> {
  public ConditionArrayList(Predicate<Integer> predicate, Integer... nums) {
    ...
  }
  public ConditionArrayList(Predicate<Integer> predicate, ArrayList<Integer> arrayList) {
    ...
  }
}
```
- makes code more flexible by providing multiple ways to use similar functionality

### Abstraction
- generalize features of a system
- An abstract class's like a template class where some functionalities haven't been implemented yet
- Cannot instantiate an abstract class. Other classes can extend the abstract class and implement the functionality
```java
public abstract class AbstractFileReader {
  ...
  protected abstract String parseLine(String line);
}

public class DigitsOnlyFileReader extends AbstractFileReader {
  ...
  @Override
  protected String parseLine(String line) {
    ...
  }
}
```
- Interface: a set of method signatures for to-be-implemented functionality. Like a specification. Cannot be instantiated.
- For a class to implement an interface, it must implement all the classes in the interface.
```java
public interface Event {
  Long getTimeStamp();
  void process();
}

public class PasswordChangeEvent implements Event {
  ...
  @Override
  public Long getTimeStamp() {
    return this.createdTimeStamp;
  }

  @Override
  public void process() {
    ...
  }
}
```
- In Java, a class can only inherits from one class but can implement several interfaces.
- Interface can extends other interfaces
- Common path in java source code
  1. Create an interface with method specifications
  2. Create an abstract class that implements the interface with base implementations and some abstract methods
  3. Create a concrete class that implements the abstract methods

