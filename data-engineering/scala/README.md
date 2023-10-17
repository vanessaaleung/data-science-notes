# Scala
- [Traits](#traits)
- [Testing](#testing)

## Traits
_Traits are used to share interfaces and fields between classes_
- Classes and objects can extend traits, but traits cannot be instantiated and therefore have no parameters.
```scala
trait Iterator[A]:
  def hasNext: Boolean
  def next(): A

class IntIterator(to: Int) extends Iterator[Int]:
  private var current = 0
  override def hasNext: Boolean = current < to
  override def next(): Int =
    if hasNext then
      val t = current
      current += 1
      t
    else
      0
end IntIterator

val iterator = new IntIterator(10)
iterator.next()  // returns 0
iterator.next()  // returns 1
```


## Testing
```sbt
 libraryDependencies += "org.scalatest" %% "scalatest" % "3.0.8" % Test
```

```scala
import org.scalatest.FunSuite

class CubeCalculatorTest extends FunSuite {
   test("CubeCalculator.cube") {
     assert(CubeCalculator.cube(3) === 27)
   }
 }
```

- `"CubeCalculator.cube"`: name for the test. Convention is “ClassName.methodName”

## Definitions and Evaluation
### VAL VS DEF
- `def` is evaluaated on each use
- `val` is evaluated at the point of the definition
```scala
val x = 2
val y = square(x)
```
- `y` refers to `4` not `square(2)`

### Call-by-value AND Call-by-name
- Call-by-value: evaluates every function argument only once. Normally used by Scala
- Call-by-name: a function argument is not evaluated if the corresponding parameter is unused in the evaluation of the function body

## CONDITIONAL EXPRESSIONS
```scala
def factorial(n: Int): Int =
  if (n == 1) 1
  else factorial(n - 1) * n
```

## Lexical Scopes
### BLOCKS AND VISIBILITY
- The definitions inside a block are only visible from within the block
```scala
val x = 0
def f(y: Int) = y + 1
val result = {
  val x = f(3)
  x * x
} + x
```
- result should be 16

### SEMICOLONS
- Semicolons are optional
- Can have more than one statements on a line
```scala
val y = x + 1; y * y
```
- write multi-line expression in parentheses
```scala
(someLongExpression
  + someOtherExpression)
```
- or write the operator on the first line
```scala
someLongExpression +
  someOtherExpression
```

### TOP-LEVEL DEFINITIONS
- `def` and `val` definitions must be writen within a top-level object definition
```scala
object MyExecutableProgram {
  val myVal = …
  def myMethod = …
}
```

### PACKAGES AND IMPORTS
- Definitions located in a package are visible from other definitions located in the same package
```scala
// file foo/Bar.scala
package foo
object Bar { … }
```
```scala
// file foo/Baz.scala
package foo
object Baz {
  // Bar is visible because it is in the `foo` package too
  Bar.someMethod
}
```
- Definitions located in other packages are not directly visible, must use fully qualified names to refer to them:
```scala
// file quux/Quux.scala
package quux
object Quux {
  foo.Bar.someMethod
}
```
- Or import names to avoid repeating their fully qualified form:
```scala
// file quux/Quux.scala
package quux
import foo.Bar
object Quux {
  // Bar refers to the imported `foo.Bar`
  Bar.someMethod
}
```

## TAIL RECURSION
- If a recursive function that calls itself as its last action, then it can reuse the stack frame of that function.
- If the last action of a function consists of calling another function, maybe the same, maybe some other function, the stack frame could be reused for both functions. Such calls are called tail calls.
```scala
@tailrec
def gcd(a: Int, b: Int): Int = …
```
```scala
def factorial(n: Int): Int = {
  @tailrec
  def iter(x: Int, result: Int): Int =
    if (x == 0) result
    else iter(x - 1, result * x)

  iter(n, 1)
}
```

## Structuring Information
### DEFINING ALTERNATIVES WITH SEALED TRAITS
-  something that can be embodied by a fixed set of alternatives
```scala
sealed trait Symbol
case class Note(name: String, duration: String, octave: Int) extends Symbol
case class Rest(duration: String) extends Symbol
```
```scala
val symbol1: Symbol = Note("C", "Quarter", 3)
val symbol2: Symbol = Rest("Whole")
```

### PATTERN MATCHING
```scala
def symbolDuration(symbol: Symbol): String =
  symbol match {
    case Note(name, duration, octave) => duration
    case Rest(duration) => duration
  }
```

### Exhausitivity
Having defined Symbol as a sealed trait gives us the guarantee that the possible case of symbols is fixed. The compiler can leverage this knowledge to warn us if we write code that does not handle all the cases:
```scala
def unexhaustive(): Unit = {
  sealed trait Symbol
  case class Note(name: String, duration: String, octave: Int) extends Symbol
  case class Rest(duration: String) extends Symbol

  def nonExhaustiveDuration(symbol: Symbol): String =
    symbol match {
      case Rest(duration) => duration
    }
}
```
```sbt
[warn] /Users/eric/Documents/Vanessa/scala/example/src/main/scala/ExampleApp.scala:15:7: match may not be exhaustive.
[warn] It would fail on the following input: Note(_, _, _)
[warn]       symbol match {
[warn]       ^
```

### ALGEBRAIC DATA TYPES
An algebraic data type definition can be thought of as a set of possible values.

```scala
sealed trait Duration
case object Whole extends Duration
case object Half extends Duration
case object Quarter extends Duration

def fractionOfWhole(duration: Duration): Double =
  duration match {
    case Whole => 1.0
    case Half => 
0.5

    case Quarter => 
0.25

  }

fractionOfWhole(Half) shouldBe 0.5
fractionOfWhole(Quarter) shouldBe 0.25
```

##  Higher-Order Functions
- Functions that take other functions as parameters or that return functions as results

### Anonymous Functions
```scala
println("abc")
```

## Functional Programming
### Programming Paradigms
- imperative programming
  - modifying mutable variables
  - using assignments
  - control structures such as if-then-else, loops, break, continue, return
- functional programming
  - programming without mutable variables, assignments, loops, and other imperative control strutures
  - focusing on the functions
- logic programming

Orthogonal:
- object-oriented programming

### Read-Eval-Print Loop
- an interactive shell lets one write expressions and responds with results
```sbt
scala> 34+65
res0: Int = 99
```

#### Evaluation
1. Take the leftmost operator
2. Evaluate its operands (left before right)
3. Apply the operator to the operands

#### Parameters and Return Types
```scala
def power(x: Double, y: Int): Double = ...
```
